---
id: "9653403555735"
titulo: "Informe o 'Tipo de Importação de CTe' para o arquivo: XX"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9653403555735-Informe-o-Tipo-de-Importa%C3%A7%C3%A3o-de-CTe-para-o-arquivo-XX"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-09-16T13:52:36Z"
rotulos: ["CT-e", "Configuração", "Movimentação Financeira", "XML", "Importação", "TOP", "CFOP", "CORE_E00235", "Informe o 'Tipo de Importação de CTe'", "Campo Tipo de Importação não definido", "Defina Tipo de Importação em Preferências de Importação de CT-e"]
---

# Informe o 'Tipo de Importação de CTe' para o arquivo: XX

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19112901204119) MENSAGEM:**

[CORE\_E00235] Informe o 'Tipo de Importação de CTe' para o arquivo: XX.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19112863202071) SITUAÇÃO:**

Ao tentar importar o CT-e a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19112901211543) CAUSA:**

Ocorre quando o campo Tipo de Importação não está definido corretamente de acordo com o lançamento.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19112901222551) SOLUÇÃO:**

Acesse a tela **Portal de Importação de XML** (Caminho de acesso à tela: Comercial » Rotinas » Portal de importação de XML), em seguida, clique no botão Outras opções e depois em "Preferências para Importar CT-e" e na aba CT-e de Terceiros defina corretamente o campo Tipo de Importação de acordo com o lançamento.

![Imagem 5: Acesse a tela Portal de Importação de XML (Caminho de acesso à tela: Comercial » Rotinas » Portal de importação de…](https://ajuda.sankhya.com.br/hc/article_attachments/19112901227287)

![Imagem 6: Acesse a tela Portal de Importação de XML (Caminho de acesso à tela: Comercial » Rotinas » Portal de importação de…](https://ajuda.sankhya.com.br/hc/article_attachments/19112901234967)

O campo **"Tipo de Importação"**apresenta as seguintes opções:

- **Movimentação Financeira:** A TOP utilizada no Financeiro do CT-e será a que foi informada no grupo Movimentação Financeira e a nota inserida na Central será confirmada;
- **Central de Compras:** A TOP utilizada no Financeiro do CT-e será a que foi informada no grupo Nota de Compra e a nota inserida na Central não será confirmada automaticamente.

**Nota:** Quando a opção Central de Compras estiver selecionada, realiza-se a conversão e a informação desta irá preencher o campo **"CFOP"**(Tela [Portal de Importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML), grade **"Itens"**).
