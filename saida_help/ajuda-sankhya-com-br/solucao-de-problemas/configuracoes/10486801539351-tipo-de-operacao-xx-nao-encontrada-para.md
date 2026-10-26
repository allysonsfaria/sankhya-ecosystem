---
id: "10486801539351"
titulo: "Tipo de operação XX não encontrada para a data XX/XX/XXXX"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10486801539351-Tipo-de-opera%C3%A7%C3%A3o-XX-n%C3%A3o-encontrada-para-a-data-XX-XX-XXXX"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:03:22Z"
rotulos: ["Lançamento", "Configuração", "TOP", "Financeiro", "CORE_E02414", "CORE_E02394", "CORE_E02676", "CORE_E02677", "Erro de Data em Tipo de Operação", "Erro"]
---

# Tipo de operação XX não encontrada para a data XX/XX/XXXX

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18603563845271) MENSAGEM:**

[CORE\_E02394] Tipo de operação XX não encontrada para a data XX/XX/XXXX.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18603563847703) SITUAÇÃO:**

Ao inserir em um lançamento um novo Tipo de Operação -TOP com data de criação superior ao do lançamento, a mensagem é apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18603563854743) SOLUÇÃO:**

Verifique a data de criação do **Tipo de operação TOP** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP), pois não é possível informar a determinada TOP em lançamentos que foram criados antes da data de criação da TOP.

![Imagem 4: Verifique a data de criação do Tipo de operação TOP (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) , pois…](https://ajuda.sankhya.com.br/hc/article_attachments/18603548813847)

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18603548811415) CAUSA:**

Ocorre ao utilizar um novo Tipo de Operação -TOP em um lançamento, onde a data do lançamento seja inferior a data de criação da Top.
