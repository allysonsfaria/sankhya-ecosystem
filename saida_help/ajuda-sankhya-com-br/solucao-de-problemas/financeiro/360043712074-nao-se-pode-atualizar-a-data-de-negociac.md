---
id: "360043712074"
titulo: "Não se pode atualizar a data de negociação, o código do tipo de negociação ou o valor da nota de uma nota que já foi baixada no financeiro"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043712074-N%C3%A3o-se-pode-atualizar-a-data-de-negocia%C3%A7%C3%A3o-o-c%C3%B3digo-do-tipo-de-negocia%C3%A7%C3%A3o-ou-o-valor-da-nota-de-uma-nota-que-j%C3%A1-foi-baixada-no-financeiro"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T16:00:52Z"
rotulos: ["Movimentação Financeira", "Financeiro", "ORA-20101", "ORA-06512", "Mensagem: Erro ao alterar nota já baixada no financeiro.", "Solução: Estornar lançamentos financeiros e tentar novamente.", "Causa: Tentativa de modificar nota com lançamentos financeiros baixados.", "Erro"]
---

# Não se pode atualizar a data de negociação, o código do tipo de negociação ou o valor da nota de uma nota que já foi baixada no financeiro

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/17290440023063) MENSAGEM:**

[ORA-20101]: Não se pode atualizar a data de negociação, o código do tipo de negociação ou o valor da nota de uma nota que já foi baixada no financeiro.Nota de Nro Único: 'X'
[ORA-06512]: em "SANKHYA.TRG\_UPD\_TGFCAB", line 960
[ORA-04088]: erro durante a execução do gatilho 'SANKHYA.TRG\_UPD\_TGFCAB'

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17290425090327)  SITUAÇÃO:**

Ao tentar alterar informações de lançamentos na Central, é apresentada a mensagem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17290440030743) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 4: Acesse: Financeiro » Rotinas » Movimentação Financeira](https://ajuda.sankhya.com.br/hc/article_attachments/17290425098135) Acesse: Financeiro » Rotinas » Movimentação Financeira

Localize os financeiros gerados pelo respectivo lançamento e proceda com o **estorno** dos mesmos.

![Imagem 5: Realizado o estorno, teste uma nova alteração dos dados desejados na respectiva 'Central'.](https://ajuda.sankhya.com.br/hc/article_attachments/17290425105815) Realizado o estorno, teste uma nova alteração dos dados desejados na respectiva 'Central'.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17290425108759) CAUSA:**

Mensagem apresentada ao tentar alterar informações de lançamentos que possuem financeiros baixados.
