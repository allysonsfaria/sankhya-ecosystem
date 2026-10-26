---
id: "26104865160471"
titulo: "Nota possui valor de ISS mas os dados não estão nas tabelas de impostos (TGFDIN/TGFIMN)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26104865160471-Nota-possui-valor-de-ISS-mas-os-dados-n%C3%A3o-est%C3%A3o-nas-tabelas-de-impostos-TGFDIN-TGFIMN"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:43:11Z"
rotulos: ["ISS", "Configuração", "Impostos", "Financeiro", "NFS-e", "Nota possui valor de ISS mas os dados não estão nas tabelas de impostos (TGFDIN/TGFIMN)", "[CORE_E00578]"]
---

# Nota possui valor de ISS mas os dados não estão nas tabelas de impostos (TGFDIN/TGFIMN)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/26401312707607) MENSAGEM:**

[CORE\_E00578] - Nota possui valor de ISS mas os dados não estão nas tabelas de impostos (TGFDIN/TGFIMN)

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26401312710807) SOLUÇÃO:**

Deve ser verificado se realmente os itens que não tem valores de ISS não devem mesmo ter esse valor. Pois, pode ser algum erro no lançamento que causou a situação. Porém, se de fato é correto que um dos itens não tenha seu valor de ISS calculado e que os demais itens devam ter seus valores de ISS calculados, acione o parâmetro **"VALISSZERONFSE".** Dessa forma, o sistema permitirá o andamento de emissão da nota fiscal.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/26401288456215)CAUSA:**

Quando é feito o lançamento de uma nota de serviço, na qual há itens com valores de ISS e outros itens que não tem esses valores, tanto na TGFDIN, quanto na TGFIMN, o sistema valida que um dos itens não tem o  valor de ISS e apresenta a mensagem em tela.
