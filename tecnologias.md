<p align="center">
  <img src="assets/logo-texto-colorida.png" alt="Logo do Xepa+" width="280">
</p>

# Tecnologias

**Sumário**

1. [Tecnologias](#1-tecnologias)
2. [Banco de Dados](#2-banco-de-dados)
3. [Estratégia de Dados](#3-estratégia-de-dados)
4. [Segurança e Privacidade](#4-segurança-e-privacidade)
5. [Infraestrutura](#5-infraestrutura)
6. [Acessibilidade](#6-acessibilidade)

<br>

# 1. Tecnologias

| Camada | Tecnologia |
|---|---|
| Front-end | React, JavaScript, HTML e CSS |
| Back-end | Java com Spring Boot |
| API | REST |
| Banco de dados | MySQL 8 |
| Inteligência artificial | API Gemini (Xep.AI) |
| Design e protótipos | Figma |
| Versionamento | Git e GitHub |
| Hospedagem | VPS Hostinger KVM 2 + Cloudflare |
| Organização das tarefas | Trello |

A integração entre front-end e back-end é realizada por meio de endpoints REST. Todos os integrantes participaram do desenvolvimento front-end utilizando React e Figma.

**Endpoints REST planejados:**

| Método | Endpoint | Finalidade | Acesso |
|---|---|---|---|
| POST | /api/auth/cadastro | Criar conta | Público |
| POST | /api/auth/login | Entrar | Público |
| GET, PUT | /api/usuarios/me | Consultar e editar perfil | Logado |
| GET | /api/planos | Listar planos | Público |
| PUT | /api/feirantes/me/plano | Alterar o plano | Feirante |
| GET | /api/feiras | Listar feiras do mapa | Público |
| POST, PUT, DELETE | /api/feirantes/me/feiras | Gerenciar suas feiras | Feirante |
| GET | /api/xepas | Listar ofertas | Público |
| POST | /api/xepas | Cadastrar oferta | Feirante |
| GET | /api/xepas/{id} | Consultar oferta | Público |
| PUT, DELETE | /api/xepas/{id} | Alterar ou remover oferta | Feirante |
| GET, POST | /api/pedidos | Consultar e criar pedidos | Consumidor |
| GET | /api/feirantes/me/vendas | Consultar vendas | Feirante |
| PATCH | /api/pedidos/{id}/status | Atualizar situação | Feirante |
| POST | /api/pedidos/{id}/pagamento | Registrar pagamento | Consumidor |
| GET, POST | /api/financeiro/gastos | Consultar e registrar gastos | Feirante |
| GET, POST | /api/financeiro/lancamentos | Consultar e registrar rendas | Feirante |
| GET | /api/financeiro/resumo | Consultar indicadores | Feirante |
| GET | /api/conversas | Listar conversas | Logado |
| GET, POST | /api/conversas/{id}/mensagens | Ler e enviar mensagens | Logado |
| POST | /api/ia/mensagens | Conversar com a Xep.AI | Feirante |

<br>

# 2. Banco de Dados

O dossiê registra a implementação do banco de dados em MySQL 8, por meio do script `xepaDB 1.0`. O banco possui 25 tabelas organizadas em cinco grupos:

- Contas e acesso.
- Feiras e ofertas.
- Compra.
- Comunicação.
- Receitas e financeiro.

O banco será acessado pelo back-end em Java com Spring Boot, por meio da API REST. Enquanto a API não é publicada, o front-end guarda os dados no navegador, por meio do `localStorage`.

**Principais relacionamentos:**

- Uma conta pode ter um perfil de consumidor, um de feirante e um de colaborador, cada um em relação 1:1.
- Um feirante trabalha em várias feiras, e uma feira reúne vários feirantes (`tb_feirante_feira`).
- Um feirante cadastra vários produtos; cada produto pode gerar várias xepas, cada uma ligada a uma feira.
- No checkout, o carrinho do consumidor é dividido em um pedido por feirante.
- Um chat liga um consumidor a um feirante; as conversas com a Xep.AI ficam ligadas à conta (`tb_mensagem_ia`).
- Um feirante registra vários gastos, cada um em uma categoria de gasto.

<br>

# 3. Estratégia de Dados

- **Contas:** identificação, contato e perfil de acesso de consumidores e feirantes.
- **Operação:** feiras, xepas, pedidos, pagamentos e conversas.
- **Gestão:** gastos por categoria, vendas e plano de cada feirante.
- **Indicadores:** volume de vendas, comissões, recompra, produtos mais vendidos e alimentos aproveitados.
- **Integridade:** o controle de versão da xepa impede que a mesma unidade seja vendida duas vezes, e o preço de cada item fica registrado no momento da compra.

<br>

# 4. Segurança e Privacidade

O projeto considera senhas armazenadas com hash, controle de acesso por perfil, coleta apenas dos dados necessários e tratamento adequado de dados pessoais conforme a LGPD (Lei nº 13.709/2018).

O Xepa+ guarda apenas o método, o valor e o status do pagamento, sem armazenar dados de cartão. O controle de versão da xepa busca impedir que a mesma unidade seja vendida duas vezes, e o preço de cada item fica registrado no momento da compra.

| Dado | Finalidade | Base legal |
|---|---|---|
| Nome, e-mail, telefone, CPF e senha (hash) | Criar a conta, dar acesso e permitir o pagamento via Pix | Execução de contrato |
| Dados do feirante (nome fantasia, CNPJ, matrícula) | Identificar o feirante e verificar se atua de forma regular | Execução de contrato e legítimo interesse |
| Pedidos e pagamentos | Processar a compra, calcular a comissão e cumprir obrigações fiscais | Execução de contrato e obrigação legal |
| Mensagens do chat e da Xep.AI | Comunicação sobre pedidos e respostas ao feirante | Execução de contrato |
| Aparelhos e sessões | Manter o acesso seguro e permitir desconectar aparelhos | Legítimo interesse |
| E-mail para novidades | Marketing | Consentimento (opcional) |


- Senhas e tokens de sessão são guardados como hash, e o site usa HTTPS.
- No cadastro, o usuário marca a caixa "Li e aceito os Termos de Uso e a Política de Privacidade".

- Os dados dos usuários não são vendidos a terceiros.

<br>

# 5. Infraestrutura

- Hospedagem compatível com React, Java e MySQL: **VPS Hostinger KVM 2** (2 vCPU, 8 GB de RAM e 100 GB NVMe), com front-end, back-end e banco de dados no mesmo servidor.
- **Cloudflare** (plano gratuito) para DNS, HTTPS, proteção básica e cache.
- Domínio personalizado **.com.br**.
- Armazenamento de banco de dados, imagens e arquivos no espaço da VPS.
- Backups para recuperação de dados, incluídos na hospedagem.



<br>

# 6. Acessibilidade

Implementação do widget UserWay para facilitar a navegação, inclusão de rótulos nos campos de formulário, textos alternativos nas imagens, atributos ARIA para melhorar a interpretação dos elementos por leitores de tela, layout responsivo e vídeos adaptados à preferência do usuário por redução de movimentos.


