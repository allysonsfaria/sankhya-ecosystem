---
id: "10117094653975"
titulo: "Tipo de movimento inválido nesta opção"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10117094653975-Tipo-de-movimento-inv%C3%A1lido-nesta-op%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:04:32Z"
rotulos: ["CT-e", "Configuração", "Movimentação Financeira", "TOP", "Financeiro", "CORE_E01860", "CORE_E02834", "Correção de Tipo de Movimento Inválido", "Erro", "Artigo atualizado KCS", "Plataforma - KCS"]
---

# Tipo de movimento inválido nesta opção

**MENSAGEM:**

[CORE\_E01860] Tipo de Movimento inválido nesta opção.

**SITUAÇÃO:**

Ao tentar confirmar uma nota na central de vendas ou tentar cadastrar um modelo de nota para uma TOP financeiro a mensagem é apresentada.

**CAUSA:**

Ocorre quando se utiliza uma TOP com tipo de movimento diferente do realizado ou a TOP não vincula no modelo de nota.

**SOLUÇÃO:**

**(1)** Lançamento de notas:

**(1)** Acesse a tela do Tipo de operação utilizado na central de vendas e verifique se o campo 'Tipo de movimento' está preenchido com a opção: 'VENDA'.

![Imagem 1: (1) Acesse a tela do Tipo de operação utilizado na central de vendas e verifique se o campo 'Tipo de movimento' está…](https://ajuda.sankhya.com.br/hc/article_attachments/10116892767767)

**(1)** Criação do modelo de nota (existem duas maneiras diferentes):

**(2)** Crie um **Tipo de operação TOP** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) do tipo compras caso queira apenas uma nota para CT-e. No financeiro insira despesas, para que o sistema gere notas "avulsas" apenas para CT-e e, assim, consequentemente possa vê-las no portal de compras ou;

![Imagem 2: (2) Crie um Tipo de operação TOP (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) do tipo compras caso…](https://ajuda.sankhya.com.br/hc/article_attachments/10116985402391)

**(2)** No**portal de importação XML** (Comercial » Rotinas » Portal de importação de XML) vá até 'Outras opções', em seguida clique em 'Preferências para importar CT-e' e associe sua TOP financeira de CT-e à uma nota. Vale destacar que essa ação fará a junção e não será possível ver separado.

![Imagem 3: (2) No portal de importação XML (Comercial » Rotinas » Portal de importação de XML) vá até 'Outras opções', em seguida…](https://ajuda.sankhya.com.br/hc/article_attachments/10117046459799)
