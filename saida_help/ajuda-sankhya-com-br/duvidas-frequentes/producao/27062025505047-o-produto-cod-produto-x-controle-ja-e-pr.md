---
id: "27062025505047"
titulo: "O produto Cód.Produto X, controle \" \" já é produzido por um outro processo produtivo padrão"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/27062025505047-O-produto-C%C3%B3d-Produto-X-controle-j%C3%A1-%C3%A9-produzido-por-um-outro-processo-produtivo-padr%C3%A3o"
trilha: "Dúvidas Frequentes > Produção"
atualizado_em: "2026-07-22T14:40:12Z"
rotulos: ["Produtos", "Configuração", "Processo Produtivo", "Produção", "Passos para resolver", "Razão do erro", "Detalhe do erro", "PROD_E00429", "O produto Cód.Produto X controle", "já é produzido por um outro processo produtivo padrão", "Erro"]
---

# O produto Cód.Produto X, controle " " já é produzido por um outro processo produtivo padrão

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/27062017272855) **MENSAGEM:**

[PROD\_E00429] O produto Cód.Produto X, controle "  " já é produzido por um outro processo produtivo padrão (Cód.Processo XX - Id.Processo YY). Não pode haver mais de um processo produivo padrão para um dado Produto/Controle.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/27062025489431)SOLUÇÃO:**

Acesse a tela **"Composição do produto"**, busque o produto X e verifique quais processos estão vinculados.

Depois, acesse a tela **"Processo produtivo"** e verifique se o processo com a marcação padrão está correto, caso não esteja corrija a marcação no processo.

Caso o processo produtivo não seja considerado como padrão para os novos lançamentos, versione o processo produtivo e desmarque a opção padrão.

**Observação:** essa alteração afeta todos os produtos vinculados ao processo.

Caso necessite de um novo processo padrão para o produto X, utilize a marcação padrão por produto no novo processo produtivo.

[GIF animado: Imagem 3: Caso necessite de um novo processo padrão para o produto X, utilize a marcação padrão por produto no novo processo…](https://ajuda.sankhya.com.br/hc/article_attachments/27121056813335)

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/27062025498135)CAUSA:**

Ocorre ao tentar vincular um produto em um processo produtivo marcado como padrão e esse produto já está cadastrado em outro processo produtivo padrão.
