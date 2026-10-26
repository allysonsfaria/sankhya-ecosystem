---
id: "32617033837335"
titulo: "Divergência na entrega do cálculo na tag <vFCPSTRet> para CST 10 na geração de notas fiscais"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32617033837335-Diverg%C3%AAncia-na-entrega-do-c%C3%A1lculo-na-tag-vFCPSTRet-para-CST-10-na-gera%C3%A7%C3%A3o-de-notas-fiscais"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:30:54Z"
rotulos: ["Configuração", "NF-e", "XML", "SEFAZ", "Impostos", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Divergência na entrega do cálculo", "tag <vFCPSTRet>", "CST 10 na geração de notas fiscais"]
---

# Divergência na entrega do cálculo na tag <vFCPSTRet> para CST 10 na geração de notas fiscais

A situação ocorre quando o usuário gera uma nota fiscal com o CST 10 e espera que o valor do FCP ST seja apresentado na tag **<vFCPSTRet>** no XML, conforme entendimento do cliente.

**SOLUÇÃO**

**(1)** Consulte o manual da NF-e para verificar o agrupamento correto das tags de ICMS para cada CST.

**(2)** Observe que, para o CST 10, o manual não prevê a utilização da tag **<vFCPSTRet>**. Essa tag é prevista apenas para os agrupamentos CST 60 ou 500.

**(3)** Para o CST 10, utilize a tag **<vFCPST>** no XML, conforme orientação do manual.

**(4)** Confira o exemplo de XML gerado para o CST 10:

![Imagem 1: (4) Confira o exemplo de XML gerado para o CST 10:](https://ajuda.sankhya.com.br/hc/article_attachments/38631950578711)![Imagem 2: (4) Confira o exemplo de XML gerado para o CST 10:](https://ajuda.sankhya.com.br/hc/article_attachments/38631956399767)

**Observações:**

- Quando **houver ST com FCP**, o **sistema soma o valor do FCP** no campo de **"Vlr.substituição"**, resultando em um valor total maior na nota.
- Para **FCP/ICMS, não há soma** em nenhum campo adicional.
