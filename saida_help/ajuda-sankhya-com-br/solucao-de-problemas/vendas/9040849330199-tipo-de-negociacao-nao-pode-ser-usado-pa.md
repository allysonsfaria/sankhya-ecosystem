---
id: "9040849330199"
titulo: "Tipo de Negociação não pode ser usado para Parceiro com 'Classificação ICMS' igual a Consumidor"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9040849330199-Tipo-de-Negocia%C3%A7%C3%A3o-n%C3%A3o-pode-ser-usado-para-Parceiro-com-Classifica%C3%A7%C3%A3o-ICMS-igual-a-Consumidor"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T15:11:12Z"
rotulos: ["Configuração", "Fiscal", "Parceiro", "NF-e", "ICMS", "CORE_E04508", "Marcar opção \"Pode ser usado por consumidor\"", "Ajustar configuração no cadastro do parceiro", "Restrição de Tipo de Negociação para Consumidor"]
---

# Tipo de Negociação não pode ser usado para Parceiro com 'Classificação ICMS' igual a Consumidor

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16671371877143) MENSAGEM:**

[CORE\_E04508]: Tipo de Negociação não pode ser usado para Parceiro com 'Classificação ICMS' igual a Consumidor.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16671371880855) SITUAÇÃO:**

Ao tentar lançar notas para parceiros que estão classificados como consumidor e o tipo de negociação estiver configurada para não ser usada por consumidor.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16671368479127) SOLUÇÃO:**

Com a opção **"Pode ser usado por consumidor"** marcada, o Tipo de Negociação poderá ser utilizado nos lançamentos para Parceiros classificados como Consumidor Final ([Cadastro de Parceiros »](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros) [Aba Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abafiscal) » campo Classificação ICMS). Ao lançar uma Nota de venda com um Tipo de Negociação que esteja com esta opção desmarcada, se o Parceiro da nota estiver configurado como Consumidor Final, será apresentada uma mensagem de alerta na confirmação da nota alertando que Tipo de Negociação não pode ser usado por Consumidor Final.

![Imagem 4: Com a opção "Pode ser usado por consumidor" marcada, o Tipo de Negociação poderá ser utilizado nos lançamentos para…](https://ajuda.sankhya.com.br/hc/article_attachments/16671368482199)

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16671371888407) CAUSA:**

Ocorre quando o tipo de negociação não está marcada para ser usada por consumidor e o parceiro está configurado como consumidor.
