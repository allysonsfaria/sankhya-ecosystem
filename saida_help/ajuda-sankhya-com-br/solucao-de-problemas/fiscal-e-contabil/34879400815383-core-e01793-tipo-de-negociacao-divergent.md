---
id: "34879400815383"
titulo: "CORE_E01793 - Tipo de Negociação Divergente! No cabeçalho da nota, o Tipo de Negociação informa X parcela(s). No XML Importado, está informando X parcela(s)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34879400815383-CORE-E01793-Tipo-de-Negocia%C3%A7%C3%A3o-Divergente-No-cabe%C3%A7alho-da-nota-o-Tipo-de-Negocia%C3%A7%C3%A3o-informa-X-parcela-s-No-XML-Importado-est%C3%A1-informando-X-parcela-s"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:26:29Z"
rotulos: ["Configuração", "NF-e", "XML", "Importação", "Preferências", "CORE_E01793", "Tipo de Negociação Divergente", "No XML Importado está informando", "O Tipo de Negociação da nota deve ser alterado", "No cabeçalho da nota o Tipo de Negociação informa"]
---

# CORE_E01793 - Tipo de Negociação Divergente! No cabeçalho da nota, o Tipo de Negociação informa X parcela(s). No XML Importado, está informando X parcela(s)

**MENSAGEM**

[CORE\_E01793] Tipo de Negociação Divergente! No cabeçalho da nota, o Tipo de Negociação informa X parcela(s). No XML Importado, está informando X parcela(s). O Tipo de Negociação da nota deve ser alterado!

**SITUAÇÃO**

Ocorre ao importar um arquivo XML de Nota Fiscal quando a quantidade de parcelas informada no XML é diferente da quantidade de parcelas definida no **"Tipo de Negociação"** do cabeçalho da nota. O usuário tenta importar o XML sem que o parâmetro adequado esteja ativado.

**SOLUÇÃO**

**(1)**  Acesse a tela **"Preferências"** (Configurações » Avançado » Preferências).

**(2)**  Localize o parâmetro **"Importa negociação divergente do xml da compra?" (IMPNEGDIVXMLCMP)** e altere para **"Ligado"**.

![Imagem 1: (1) Acesse a tela "Preferências" (Configurações » Avançado » Preferências). (2) Localize o parâmetro "Importa…](https://ajuda.sankhya.com.br/hc/article_attachments/34879400811927)

**(3)**  Feche a tela da **"Central de Compras"**

**(4)**  Realize novamente a importação do XML.

**CAUSA**

O erro ocorre porque o parâmetro **IMPNEGDIVXMLCMP** está desligado, impedindo a importação de XMLs em que a quantidade de parcelas diverge da quantidade definida no **"Tipo de Negociação"** do cabeçalho da Nota Fiscal.
