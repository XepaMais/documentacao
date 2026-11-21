<p align="center">
  <img src="assets/logo-texto-colorida.png" alt="Logo do Xepa+" width="280">
</p>

# Xep.AI (Xepinha)

<p align="center">
  <img src="assets/xepinha.jpeg" alt="Xepinha, mascote da Xep.AI em forma de pera" width="240">
</p>

**Sumário**

1. [O que é a Xepinha](#1-o-que-é-a-xepinha)
2. [O que ela faz](#2-o-que-ela-faz)
3. [Onde ela aparece](#3-onde-ela-aparece)
4. [Disponibilidade nos planos](#4-disponibilidade-nos-planos)
5. [Tecnologia](#5-tecnologia)
6. [Privacidade](#6-privacidade)
7. [Limites](#7-limites)

<br>



# 1. O que é a Xepinha

A **Xep.AI**, apresentada como **Xepinha**, é a assistente virtual do Xepa+, criada para tornar a experiência mais simples, prática e divertida.

Ela é representada por uma **pera** com expressão simpática, no mesmo estilo de frutas e legumes da identidade visual do Xepa+. A personagem aproxima a tecnologia de feirantes que podem ter pouca familiaridade com ferramentas digitais: em vez de procurar em menus, o feirante pode perguntar à Xepinha.

<br>

# 2. O que ela faz

| Função | Descrição |
| :--- | :--- |
| **Tira dúvidas na hora** | Responde sobre pedidos, planos e o uso da plataforma. |
| **Ajuda no dia a dia da banca** | Orienta o feirante a cadastrar xepas e cestas e a organizar o financeiro. |
| **Conversa simples e divertida** | Usa linguagem leve e acolhedora, como uma amiga da feira. |

<br>

Exemplos de perguntas que o feirante pode fazer:
<br>
- "Como eu cadastro uma cesta de xepa?"
- "Quantos pedidos tenho para retirar hoje?"
- "Qual plano fica mais barato para quem vende R$ 1.000 por mês?"
- "Como registro uma despesa da Ceagesp?"

<br>

# 3. Onde ela aparece

- **Página inicial do feirante:** botão **"Falar com a Xepinha"**, no quadro "O que vamos fazer hoje?".
- **Menu Xep.AI:** atalho no menu superior da área do feirante, com a interface de conversa.
- **Rodapé da área do feirante:** link Xep.AI na seção Gestão.

<br>

# 4. Disponibilidade nos planos

| Plano | Mensalidade | Xep.AI |
| :--- | :---: | :---: |
| **Grátis** | R$ 0,00 | - |
| **Crescer** | R$ 29,90 | Sim |
| **Pro** | R$ 59,90 | Sim |

A Xepinha é um dos recursos que diferenciam os planos pagos. Os detalhes dos planos estão em [Financeiro](financeiro.md).

<br>

# 5. Tecnologia

A Xep.AI foi criada com a **API Gemini**, integrada ao back-end em Java com Spring Boot pelo endpoint `POST /api/ia/mensagens`. No banco de dados, as conversas com a Xep.AI ficam na tabela `tb_mensagem_ia`, ligadas à conta do usuário.

<br>

# 6. Privacidade

As mensagens trocadas com a Xep.AI são tratadas conforme a LGPD, com base legal de **execução de contrato**: servem para responder ao feirante e não são vendidas a terceiros. 

<br>

# 7. Limites

- A Xepinha orienta e responde dúvidas, mas não faz pagamentos, não altera pedidos nem toma decisões pelo feirante.
- As respostas geradas por inteligência artificial podem conter erros; informações sobre valores, comissões e regras devem ser conferidas nas telas da plataforma.
- As possibilidades e os limites do assistente devem seguir a implementação efetiva do projeto.
