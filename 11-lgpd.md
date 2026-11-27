<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/logo-texto-branca.png">
    <img src="assets/logo-texto-colorida.png" alt="Logo do Xepa+" width="280">
  </picture>
</p>

# LGPD e privacidade

O Xepa+ segue a Lei Geral de Proteção de Dados (Lei nº 13.709/2018). Este documento mostra:
- quais dados são coletados e para quê;
- por quanto tempo ficam guardados e com quem são compartilhados;
- como funcionam o consentimento e os direitos do titular, e onde cada regra está implementada.

O texto para o usuário está nas páginas [Diretrizes de privacidade](https://xepamais.com.br/privacidade) e [Termos de uso](https://xepamais.com.br/termos-de-uso) do site.

<br>

# 1. Dados coletados e finalidade

O Xepa+ coleta só o necessário para cada função (princípio da necessidade, art. 6º, III).

| Dado | Quem informa | Finalidade | Base legal (art. 7º) |
| :--- | :--- | :--- | :--- |
| **Nome, e-mail, telefone** | Consumidor e feirante | Criar a conta, entrar e receber avisos sobre pedidos | Execução de contrato (V) |
| **CPF** | Consumidor e feirante | Identificar a pessoa, evitar contas duplicadas e permitir pagamento via Pix | Execução de contrato (V) |
| **Senha** | Consumidor e feirante | Proteger o acesso (guardada só como hash, nunca legível) | Execução de contrato (V) |
| **Data de nascimento** | Opcional | Confirmar maioridade | Execução de contrato (V) |
| **Foto de perfil** | Opcional | Identificação visual no chat e no perfil da banca | Consentimento (I) |
| **Nome da banca, CNPJ, CCM, matrícula, grupo de comércio** | Feirante | Verificar que o feirante atua regularmente na feira livre | Execução de contrato (V) e legítimo interesse (IX) |
| **Endereço de entrega** | Consumidor, só se escolher entrega | Entregar o pedido em casa | Execução de contrato (V) |
| **Localização no momento** | Consumidor, só se autorizar no navegador | Mostrar feiras e xepas próximas. **Não é guardada** no banco | Consentimento (I) |
| **Pedidos, itens, pagamentos** | Gerados na compra | Processar a compra, calcular a comissão, emitir comprovantes | Execução de contrato (V) e obrigação legal (II) |
| **Lucros, gastos e saques** | Feirante | Gestão financeira da banca (planos Broto e Colheita) | Execução de contrato (V) |
| **Chave Pix do saque** | Feirante | Transferir o valor das vendas | Execução de contrato (V) |
| **Mensagens do chat** | Consumidor e feirante | Combinar retirada ou entrega do pedido | Execução de contrato (V) |
| **Perguntas à Xepinha** | Feirante | Responder dúvidas sobre o uso do app e a gestão da banca | Execução de contrato (V) |
| **Aparelhos conectados** (tipo, navegador, último acesso) | Gerado no login | Segurança: permitir ver e desconectar aparelhos | Legítimo interesse (IX) |
| **Mensagens de suporte** | Qualquer visitante | Responder ao pedido de ajuda | Legítimo interesse (IX) |
| **E-mail para novidades** | Opcional, no cadastro ou no perfil | Enviar novidades e ofertas | **Consentimento (I)**, revogável a qualquer momento |

**O que o Xepa+ não coleta nem guarda:**
- dados de cartão;
- dados sensíveis (art. 5º, II), como saúde, religião ou origem racial;
- a localização contínua do usuário.

<br>

# 2. Consentimento

| Momento | Como funciona | Onde está no sistema |
| :--- | :--- | :--- |
| **Cadastro** | Caixa **obrigatória**: "Li e aceito os Termos de uso e as Diretrizes de Privacidade", com links que abrem em nova aba | Site: `AceiteTermos.jsx`. API: recusa o cadastro sem `aceiteTermos: true` |
| **Registro do aceite** | O banco grava **data e hora** e a **versão dos termos** aceita | `tb_conta.aceite_termos_em` e `tb_conta.versao_termos` |
| **Novidades por e-mail** | Caixa **opcional** e desmarcada no cadastro | `tb_conta.aceite_marketing` |
| **Mudar de ideia** | Em **Perfil → Privacidade e dados**, a pessoa liga ou desliga as novidades quando quiser | `PUT /api/conta/{id}/consentimento` |
| **Localização** | O navegador pede permissão antes. Sem permissão, o mapa funciona pela busca | Site: `localizacao.js` |
| **Novos termos** | Ao mudar os termos, a versão (`LGPD_VERSAO_TERMOS`) e a data nas páginas são atualizadas | `application.yaml` |

<br>

# 3. Direitos do titular (art. 18)

| Direito | Como exercer no Xepa+ | Implementação |
| :--- | :--- | :--- |
| **Confirmação e acesso** | Perfil → Privacidade e dados → **Baixar meus dados** | `GET /api/conta/{id}/dados`: arquivo JSON com perfil, banca, pedidos, vendas, financeiro, conversas e aparelhos |
| **Portabilidade** | O mesmo arquivo JSON, em formato aberto | Idem |
| **Correção** | Perfil → **Editar perfil** | `PUT /api/conta/{id}/perfil` |
| **Revogar consentimento** | Perfil → desmarcar **Novidades por e-mail** | `PUT /api/conta/{id}/consentimento` |
| **Eliminação** | Perfil → **Excluir minha conta**, confirmando com a senha | `DELETE /api/conta/{id}` (detalhes na seção 4) |
| **Informação sobre compartilhamento** | Esta página e as Diretrizes de privacidade | Seção 5 |
| **Dúvidas e outros pedidos** | E-mail do encarregado (seção 7) | — |

Só o próprio titular acessa esses dados. Toda rota com `{id}` exige o token de login **da mesma conta**: o token de outra conta recebe `403`.

<br>

# 4. Exclusão da conta e retenção

Ao excluir a conta:
1. Nome, e-mail, CPF, telefone, data de nascimento, foto e endereço de entrega são **apagados ou trocados por marcadores** que não identificam ninguém.
2. Os dados da banca (CNPJ, CCM, matrícula, titular) são apagados e as ofertas saem do catálogo.
3. A senha é trocada por uma aleatória e **todos os aparelhos são desconectados**.
4. O banco registra a data da exclusão (`tb_conta.data_exclusao`).

**O que continua guardado, sem identificar a pessoa:** pedidos, pagamentos e lançamentos financeiros, por **obrigação legal** (art. 16, I). Esses registros sustentam comprovantes, comissões e obrigações fiscais.

| Dado | Por quanto tempo |
| :--- | :--- |
| Conta e perfil | Enquanto a conta existir; anonimizados ao excluir |
| Pedidos, pagamentos, rendas e despesas | 5 anos após o pedido (prazo fiscal), sem identificar a pessoa depois da exclusão |
| Mensagens do chat | Enquanto a conta existir |
| Conversas com a Xepinha | Enquanto a conta existir |
| Aparelhos conectados | O login vence em 30 dias; o registro some com a conta |
| Mensagens de suporte | 2 anos após o atendimento |
| Dados de demonstração | Fictícios (`@demo.xepamais.com.br`); apagados com `05-limpar-demo.sql` |

<br>

# 5. Compartilhamento (operadores e terceiros)

O Xepa+ **não vende** dados. Eles só são compartilhados para o serviço funcionar:

| Com quem | O que recebe | Para quê |
| :--- | :--- | :--- |
| **Feirante ↔ consumidor** | Nome, mensagens do chat e endereço de entrega (só no pedido de entrega) | Combinar a retirada ou a entrega |
| **Amazon Web Services** | Todo o banco de dados e a API | Hospedagem |
| **Vercel** | Acessos ao site (endereço IP, navegador) | Hospedagem do site |
| **Google Maps** | Localização, só se a pessoa autorizar | Mostrar o mapa e calcular distâncias |
| **Google Gemini** | Só o texto das perguntas e o histórico da conversa com a Xepinha. Nome, CPF e e-mail **não** são enviados | Gerar as respostas da assistente |
| **UserWay** | Preferências do widget de acessibilidade | Recursos de acessibilidade do site |
| **Autoridades** | O que a lei ou a Justiça exigir | Cumprir obrigação legal |

Quando os dados são tratados fora do Brasil (servidores da AWS, da Vercel ou do Google em outro país), vale o art. 33: só com provedores que tenham cláusulas contratuais de proteção de dados.

<br>

# 6. Segurança (art. 46)

- **HTTPS** em toda a comunicação: navegador, site e API.
- **Senhas** guardadas só como hash PBKDF2-HMAC-SHA256 com 210.000 iterações e sal aleatório.
- **Login** com token assinado e sessão registrada no banco, desconectável por aparelho. Bloqueio de 15 minutos depois de 5 senhas erradas.
- **Acesso** só ao dono da conta: a API confere o token em toda rota da conta.
- **Banco** acessível só pela API, com credenciais em variáveis de ambiente fora do Git.
- **Menos dados guardados:** nenhum dado de cartão, e a localização não é salva.
- **Em caso de incidente:** a equipe avalia o ocorrido, avisa os titulares afetados e a ANPD em até 3 dias úteis (Resolução CD/ANPD nº 15/2024) e registra as medidas tomadas.

<br>

# 7. Encarregado (DPO) e contato

Dúvidas, pedidos sobre dados pessoais e reclamações: **xepamais8@gmail.com**, com o assunto "Privacidade". Resposta em até 15 dias (art. 19, II).

<br>

# 8. Crianças e adolescentes

O Xepa+ não é destinado a menores de 18 anos sem autorização de um responsável legal. Se forem identificados dados de menores coletados sem essa autorização, eles serão excluídos.

<br>

---

<p align="center"><a href="10-escalabilidade.md">← 10. Escalabilidade</a> · <a href="README.md">Início</a></p>
