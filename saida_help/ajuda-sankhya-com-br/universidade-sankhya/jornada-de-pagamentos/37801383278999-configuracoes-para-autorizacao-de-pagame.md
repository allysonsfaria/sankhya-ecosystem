---
id: "37801383278999"
titulo: "Configurações para autorização de pagamentos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37801383278999-Configura%C3%A7%C3%B5es-para-autoriza%C3%A7%C3%A3o-de-pagamentos"
trilha: "Universidade Sankhya > Jornada de Pagamentos"
atualizado_em: "2026-10-13T19:55:53Z"
rotulos: ["Configuração", "Eventos", "Liberação de Limites", "TOP", "Financeiro"]
---

# Configurações para autorização de pagamentos

**Configurar a TOP para o evento 24:**

- Acesse a tela **Tipos de Operação - TOP**.
  Menu: Financeiro > Arquivos > Tipos de Operação - TOP
- No campo de pesquisa, busque pela TOP**“PAGAMENTO”**.
- Acesse a aba **Financeiro**.
- No campo **Valor mínimo para Autorização de Pagamento**, defina um valor (exemplo: R$500,00).
- Clique em **Salvar**.

**Configurar o Usuário Autorizador:**

- Acesse a tela **Usuários**: 
  Menu: Configurações > Controle de Acesso > Usuários.
- Selecione o cadastro do usuário **indicado no case**.
- Clique em **Outras Opções (...)** e escolha **Limites para Liberação**.
- No pop-up aberto, inicie um novo registro clicando no ícone **(+)** e preencha:

  - **Evento:** 24 - Autorização de Pagamento.
  - **Tipo evento:** Valor.
  - **Limite:** 10.000,00 (este é valor limite que o gestor pode liberar).
  - **Tipo limite:** Evento (o que significa que, a cada vez que for necessário realizar uma liberação, o gestor poderá liberar até R$ 10.000,00).
- Clique em **Salvar**.
