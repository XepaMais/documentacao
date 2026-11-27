<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/logo-texto-branca.png">
    <img src="assets/logo-texto-colorida.png" alt="Logo do Xepa+" width="280">
  </picture>
</p>

# Escalabilidade

Este documento mostra como o Xepa+ suportaria um crescimento grande de usuários, acessos e dados, saindo do piloto na Freguesia do Ó e na Brasilândia para toda São Paulo e outras cidades. Para cada fase, ele explica:
- o que muda na arquitetura;
- quando é hora de mudar;
- quanto custa;
- como ficam o desempenho, a segurança e a manutenção.

<br>

# 1. Arquitetura atual

```text
Navegador ──HTTPS──> Vercel (site React, CDN)
                        │  /api/*
                        └──HTTPS──> api.xepamais.com.br (EC2)
                                      Nginx (certificado Let's Encrypt)
                                        └─> API Java / Spring Boot (porta interna)
                                              └─> MySQL 8 (mesmo servidor)
```

| Parte | Hoje |
| :--- | :--- |
| **Site** | React na Vercel: arquivos estáticos em CDN, escala sozinho, sem custo |
| **API** | Uma instância Spring Boot na Amazon EC2, atrás do Nginx com HTTPS |
| **Banco** | MySQL 8 no mesmo servidor, com snapshots do disco para backup |
| **Fotos** | Guardadas no próprio banco (`tb_imagem`), já reduzidas no navegador |
| **IA** | API do Gemini (Xepinha), chamada só pelo servidor |

**O que já foi feito pensando em crescer:**
- **A API não guarda estado em memória.**
  - O login é um token assinado. A sessão fica no banco (`tb_dispositivo_sessao`), não na memória do servidor.
  - Por isso várias cópias da API podem rodar lado a lado sem nenhuma mudança no código. Esse é o ponto mais importante para escalar.
- **As consultas usam índices.**
  - O catálogo usa `idx_xepa_busca` e o financeiro usa `idx_renda_feirante_data` e `idx_despesa_feirante_data`.
  - O catálogo carrega feirante, produto e feira na mesma consulta, sem uma consulta extra para cada xepa.
- **Vendas ao mesmo tempo são seguras.**
  - O controle de versão da xepa (`@Version`) impede vender duas vezes a última unidade.
  - O saque trava a linha do feirante durante o pedido, então dois saques juntos nunca passam do saldo.
- **O banco se atualiza sem parar o site.** Colunas novas são criadas pela API ao iniciar (`AtualizacaoBanco`), sem precisar tirar o site do ar.
- **Há proteção contra abuso.**
  - O login bloqueia por 15 minutos depois de 5 senhas erradas.
  - O demo da Xepinha tem limite por visitante e um teto geral de perguntas por hora.

<br>

# 2. Fases de crescimento

As faixas abaixo são estimativas para planejamento, com o perfil de uso do piloto: a maioria dos acessos é de leitura (catálogo e mapa) e há picos no fim das feiras, das 11h às 14h.

| Fase | Usuários ativos | Gatilho para avançar | Custo AWS estimado |
| :--- | :--- | :--- | :--- |
| **0. Piloto (hoje)** | até ~2 mil | — | ~US$ 37–40/mês (08-financeiro) |
| **1. Bairros de SP** | até ~20 mil | CPU acima de 70% no horário de pico ou banco acima de 70% do disco | ~US$ 90/mês |
| **2. Cidade de São Paulo** | até ~200 mil | Respostas acima de 500 ms no pico ou uma réplica do banco sobrecarregada | ~US$ 350/mês |
| **3. Outras cidades** | 1 milhão ou mais | Volume de pedidos e dados por região | Proporcional a cada região |

## Fase 1: separar as peças

- **Banco no Amazon RDS (MySQL):**
  - backups automáticos diários com recuperação para qualquer minuto;
  - atualizações gerenciadas pela AWS;
  - réplica em outra zona da AWS, que assume se a principal cair;
  - a API só troca o `DB_URL`, sem mudar código.
- **Fotos no Amazon S3 com CloudFront:** as imagens saem do banco (hoje em `tb_imagem`) e passam a ser entregues por CDN. O banco fica menor e mais rápido, e as fotos carregam mais perto do usuário.
- **Monitoramento com CloudWatch:** alertas de CPU, memória, erros 5xx e tempo de resposta.
- **Pool de conexões ajustado:** número máximo de conexões da API combinado com o limite do banco.

## Fase 2: várias cópias da API

- **Application Load Balancer** com **2 a N instâncias da API** em um *Auto Scaling Group*.
  - Novas instâncias sobem sozinhas no pico do fim de feira e desligam depois.
  - Isso funciona porque a API não guarda estado em memória.
- **Réplicas de leitura no MySQL.** O catálogo, o mapa, as receitas e os planos (a maior parte do tráfego) leem das réplicas. Pedidos, pagamentos e financeiro continuam no banco principal.
- **Cache (Amazon ElastiCache / Redis)** para dados que quase não mudam: lista de feiras, planos e receitas, com validade de alguns minutos. O mesmo cache passa a guardar os limites de tentativas, que hoje ficam na memória de cada instância.
- **Paginação em todas as listagens** do catálogo, histórico de pedidos e financeiro, por cursor (data + id).
- **Filas (Amazon SQS)** para o que não precisa ser na hora: e-mails, notificações e geração de planilhas. A resposta ao usuário não espera essas tarefas.

## Fase 3: expansão para outras cidades

- **Dados separados por região:** um banco por cidade ou região metropolitana. A conta da pessoa fica num cadastro central e os pedidos ficam no banco da região. O índice `idx_feira_cidade` já prepara a busca por cidade e UF.
- **Arquivamento:** pedidos com mais de 2 anos vão para armazenamento barato (S3 + Athena para relatórios), mantidos pelo prazo fiscal de 5 anos.
- **Relatórios separados:** indicadores de impacto e de vendas são calculados em uma réplica ou num banco analítico, sem pesar no banco das compras.

<br>

# 3. Desempenho das consultas

| Consulta | Volume esperado | Estratégia |
| :--- | :--- | :--- |
| Catálogo de xepas | Mais acessada (leitura) | Índice `(id_feira, status_xepa, data_retirada)`; só xepas do dia; carga junta de feirante, produto e feira; cache e réplica na fase 2 |
| Feiras próximas | Toda abertura do mapa | Hoje a distância é calculada em memória para todas as feiras, o que é rápido até alguns milhares. Na fase 2: filtrar no banco por faixa de latitude e longitude e usar índice espacial (`POINT` + `SPATIAL INDEX`) |
| Checkout | Pico no fim da feira | Transação curta; trava só as xepas do pedido; `@Version` contra venda dupla |
| Financeiro do feirante | Diário | Índices por feirante e data; total de despesa calculado e guardado no banco |
| Chat | Constante | Índice `(id_chat, data_envio)`; na fase 2, carregar só as últimas mensagens |

**Como acompanhar:**
- ligar o *slow query log* do MySQL a partir de 200 ms;
- rodar `EXPLAIN` nas consultas novas antes de publicar;
- revisar os índices a cada fase.

<br>

# 4. Segurança ao crescer

- **HTTPS em toda a comunicação:** do navegador até a Vercel e da Vercel até a API. A API só ouve dentro do servidor, atrás do Nginx.
- **O banco nunca fica exposto à internet:** fica em sub-rede privada no RDS, e só a API acessa.
- **Segredos fora do código:** senha do banco, chave do token e chave do Gemini ficam em variáveis de ambiente. Na fase 1, passam para o AWS Secrets Manager, com troca periódica.
- **Proteção contra abuso:**
  - limite de tentativas de login;
  - limite do demo da IA;
  - na fase 2, AWS WAF com limite por IP e regras contra ataques comuns.
- **Dados pessoais:** os controles de LGPD (aceite registrado, exportação e exclusão) já funcionam por conta e continuam iguais em qualquer escala. Veja [11-lgpd](11-lgpd.md).

<br>

# 5. Manutenção futura

- **Mudanças no banco versionadas:** hoje a API cria colunas novas ao iniciar. Na fase 1, a ideia é migrar para uma ferramenta de migração (Flyway), com um script numerado por mudança, revisado no pull request.
- **Testes automatizados:** 34 testes de integração no back-end hoje. Rodar os testes a cada pull request (GitHub Actions) antes de publicar.
- **Publicação sem parar o site:** na fase 2, o Load Balancer troca as instâncias uma de cada vez.
- **Atualização de dependências:** Spring Boot, Java e bibliotecas do front revisados a cada mês (Dependabot).
- **Custos:** alertas de orçamento no painel da AWS, como já está previsto no [08-financeiro](08-financeiro.md).

<br>

# 6. Resumo

| Pergunta | Resposta |
| :--- | :--- |
| O que limita o crescimento hoje? | API e banco no mesmo servidor e fotos dentro do banco |
| Primeiro passo | Banco no RDS e fotos no S3 (fase 1), sem mudar código |
| Por que dá para ter várias APIs? | Ela não guarda estado em memória: login por token e sessão no banco |
| Como o banco aguenta mais leitura? | Índices já criados, cache e réplicas de leitura |
| Como evitar vender duas vezes? | Controle de versão da xepa e transações curtas |

<br>

---

<p align="center"><a href="09-tecnologias.md">← 9. Tecnologias</a> · <a href="11-lgpd.md">11. LGPD →</a></p>
