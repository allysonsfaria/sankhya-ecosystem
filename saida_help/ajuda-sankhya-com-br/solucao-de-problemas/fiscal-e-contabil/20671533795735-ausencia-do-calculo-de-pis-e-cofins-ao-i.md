---
id: "20671533795735"
titulo: "Ausência do cálculo de PIS e COFINS ao importar XML de nota de compra, o que pode impactar?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/20671533795735-Aus%C3%AAncia-do-c%C3%A1lculo-de-PIS-e-COFINS-ao-importar-XML-de-nota-de-compra-o-que-pode-impactar"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:50:47Z"
rotulos: ["Configuração", "NF-e", "COFINS", "PIS", "XML", "Impostos"]
---

# Ausência do cálculo de PIS e COFINS ao importar XML de nota de compra, o que pode impactar?

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/20677006417815) SITUAÇÃO:**

Ao importar um XML de nota de compras, onde se tem o destaque do PIS e COFINS, espera-se que esses impostos sejam calculados após a confirmação do documento com base nas configurações previamente definidas (TOP, Empresa, Produto, Alíquotas de PIS/COFINS). No entanto, às vezes, mesmo com todas as configurações corretas, outras configurações podem impactar na rotina, fazendo com que o sistema não gere os dados de tais impostos na nota.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/20671564878871)SOLUÇÃO:**

A marcação que poderá impactar na rotina é o campo "Importar o XML mantendo as despesas acessórias com os valores do XML". Caso o campo esteja marcado, o sistema irá considerar os valores de PIS e COFINS do XML.  Com o campo desmarcado o PIS e COFINS serão calculados corretamente.

Contudo, a marcação desse campo pode influenciar no cálculo de outros impostos no que diz respeito às despesas acessórias.

Portanto, foi desenvolvido o parâmetro **'Manter PIS e COFINS do XML importado - MANPISCOFXMLIMP'** para que, caso o cliente não ache viável desmarcar o campo "Importar o XML mantendo as despesas acessórias com os valores do XML", ele desligue a preferência. Assim, o sistema irá manter o cálculo do **PIS** e **COFINS** de acordo com os cadastros do sistema e não irá considerar os valores desses dois impostos no XML. Os demais impostos não deverão ser afetados com o parâmetro desabilitado.
