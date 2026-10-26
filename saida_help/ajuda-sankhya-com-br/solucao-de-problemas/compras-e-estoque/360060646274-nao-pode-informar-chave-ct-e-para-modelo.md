---
id: "360060646274"
titulo: "Não pode informar Chave CT-e para \"Modelo do Documento\" diferente de 57 ou 67"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360060646274-N%C3%A3o-pode-informar-Chave-CT-e-para-Modelo-do-Documento-diferente-de-57-ou-67"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T15:25:46Z"
rotulos: ["CT-e", "Fiscal", "NF-e", "SEFAZ", "#formatadoroger", "CORE_E02400", "#emconstruçao", "Correção de Informações de Chave em Documentos Fiscais", "Erro"]
---

# Não pode informar Chave CT-e para "Modelo do Documento" diferente de 57 ou 67

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16302040633111) MENSAGEM:**

[CORE\_E02400]  Não pode informar Chave CT-e para "Modelo do Documento" diferente de 57 ou 67.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16302060858007)SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Quando a Nota for Modelo de Documento: 55 (NF-e), informe a chave no campo Chave NF-e](https://ajuda.sankhya.com.br/hc/article_attachments/16302060858519) Quando a Nota for Modelo de Documento: 55 (NF-e), informe a chave no campo Chave NF-e

![Imagem 4: Quando a Nota for Modelo de Documento: 55 (NF-e), informe a chave no campo Chave NF-e](https://ajuda.sankhya.com.br/hc/article_attachments/15023021516183)

![Imagem 5: Quando a Nota for Modelo de Documento: 57/67, informe a chave CT-e no campo Chave CT-e da aba: "Financeiro da…](https://ajuda.sankhya.com.br/hc/article_attachments/16302040639639) Quando a Nota for Modelo de Documento: 57/67, informe a chave CT-e no campo Chave CT-e da aba: **"Financeiro da Nota/Transporte"**

![Imagem 6: Quando a Nota for Modelo de Documento: 57/67, informe a chave CT-e no campo Chave CT-e da aba: "Financeiro da…](https://ajuda.sankhya.com.br/hc/article_attachments/15023086930839)

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16302060862359) CAUSA:**

Ocorre quando o cliente está tentando informar uma chave de nota fiscal eletrônica, no campo **"Chave CT-e"** da nota de compra.
Ou seja o campo Chave CT-e é para receber o mesmo, o campo Chave NF-e é para receber a chave da nota fiscal eletrônica e não o inverso.
