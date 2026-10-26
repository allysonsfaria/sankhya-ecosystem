---
id: "34679688805271"
titulo: "334 Rejeição: Número do processo de drawback não informado na importação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34679688805271-334-Rejei%C3%A7%C3%A3o-N%C3%BAmero-do-processo-de-drawback-n%C3%A3o-informado-na-importa%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T14:26:52Z"
rotulos: ["NF-e", "XML", "Importação", "SEFAZ", "CFOP", "Rejeição 334", "334 Rejeição", "Número do processo de drawback não informado na importação", "Drawback"]
---

# 334 Rejeição: Número do processo de drawback não informado na importação

**MENSAGEM**

334 Rejeição: Número do processo de drawback não informado na importação

**SITUAÇÃO**

Ao tentar processar a Nota Fiscal Eletrônica de importação com CFOP **"3127"** ou **"3211"**, o sistema apresenta a rejeição informando que o número do processo de drawback não foi informado. O usuário estava lançando produtos importados e não preencheu o campo obrigatório referente ao regime drawback na adição da declaração de importação.

**SOLUÇÃO**

**(1)**  Abra a **"Nota Fiscal Eletrônica"** na central de compras.

**(2)**  Clique no botão **"Outras Opções"** do item e selecione **"Declaração de Importação e Adições"**.

![Imagem 1: (1) Abra a "Nota Fiscal Eletrônica" na central de compras. (2) Clique no botão "Outras Opções" do item e selecione…](https://ajuda.sankhya.com.br/hc/article_attachments/34679641965207)

**(3)**  No pop-up da **"Declaração de Importação"**, preencha corretamente o campo **"Nro. Ato Conc. regime DrawBack"** para cada produto.

![Imagem 2: (3) No pop-up da "Declaração de Importação" , preencha corretamente o campo "Nro. Ato Conc. regime DrawBack" para cada…](https://ajuda.sankhya.com.br/hc/article_attachments/34679688790551)

**(4)**  Repita o procedimento para todos os produtos da NFe que utilizam os CFOP **"3127"** ou **"3211"**.

**(5)**  Para conferência, gere o XML da NFe e pesquise pela TAG **"nDraw"** para certificar que foi gerada corretamente em todos os produtos com os CFOP citados.

![Imagem 3: (4) Repita o procedimento para todos os produtos da NFe que utilizam os CFOP "3127" ou "3211" . (5) Para conferência,…](https://ajuda.sankhya.com.br/hc/article_attachments/34679688792215)

**CAUSA**

A rejeição ocorre quando o campo **"Nro. Ato Conc. regime DrawBack"** não é informado na adição da declaração de importação para produtos lançados com CFOP **"3127"** ou **"3211"**.
