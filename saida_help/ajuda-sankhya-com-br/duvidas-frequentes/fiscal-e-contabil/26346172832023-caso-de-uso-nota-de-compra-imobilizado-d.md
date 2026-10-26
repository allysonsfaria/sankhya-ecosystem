---
id: "26346172832023"
titulo: "Caso de uso - Nota de compra imobilizado - DIFAL ( diferencial de alíquotas ) apenas quando temos ST ( substituição tributária ) na operação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26346172832023-Caso-de-uso-Nota-de-compra-imobilizado-DIFAL-diferencial-de-al%C3%ADquotas-apenas-quando-temos-ST-substitui%C3%A7%C3%A3o-tribut%C3%A1ria-na-opera%C3%A7%C3%A3o"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:42:31Z"
rotulos: ["Configuração", "NF-e", "DIFAL", "Imobilizado", "Impostos", "ST", "Nota de compra imobilizado - DIFAL", "diferencial de alíquotas", "apenas quando temos ST"]
---

# Caso de uso - Nota de compra imobilizado - DIFAL ( diferencial de alíquotas ) apenas quando temos ST ( substituição tributária ) na operação

Conheça a seguir o efeito do parâmetro  "**GERDIFICMSEMST - Gerar dif. de alíq. para consumo/imob sem S.T"** no lançamento das notas de compras, de itens configurados como **Imobilizado ou Consumo quando houver cálculo de ST na operação:**

Quando este parâmetro está marcado, o sistema só **não** vai gerar a dif. para produtos do tipo consumo/imobilizado e que tenham S.T.

Para os itens de consumo/imobilizado sem S.T. e os outros tipos de produtos (revenda, matéria prima, produção própria, entre outros), o sistema vai gerar a diferença de alíquota normalmente. Quando o parâmetro estiver desabilitado, e o sistema estiver configurado para calcular a dif. de ICMS, o sistema vai gerar a dif. de alíq. para todos os itens, independente de sua classificação ou cálculo de S.T.

A configuração para que o sistema calcule a dif. de ICMS pode ser verificada [aqui.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044465693-Configura%C3%A7%C3%B5es-necess%C3%A1rias-para-c%C3%A1lculo-do-Diferencial-de-Al%C3%ADquotas-autom%C3%A1tico-na-entrada-da-NF)

[GIF animado: Imagem 1: A configuração para que o sistema calcule a dif. de ICMS pode ser verificada aqui.](https://ajuda.sankhya.com.br/hc/article_attachments/26395920491671)
