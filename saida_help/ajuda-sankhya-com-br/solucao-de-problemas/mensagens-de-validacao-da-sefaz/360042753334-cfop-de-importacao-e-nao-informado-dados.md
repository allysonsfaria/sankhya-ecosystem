---
id: "360042753334"
titulo: "CFOP de Importação e não informado dados de IPI"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042753334-CFOP-de-Importa%C3%A7%C3%A3o-e-n%C3%A3o-informado-dados-de-IPI"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:06:19Z"
rotulos: ["ERRONF", "#criadoRoger", "#revisadohugo", "Configuração", "NF-e", "Importação", "SEFAZ", "Impostos", "CFOP", "597", "CFOP importação sem IPI", "Corrigir cálculo IPI e refaturar", "NF-e importação sem IPI informado"]
---

# CFOP de Importação e não informado dados de IPI

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16087145784983) MENSAGEM**:

597-Rejeição: CFOP de Importação e não informado dados de IPI.

**![Imagem 2: SOLUÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/16087145788439) SOLUÇÃO**:

Para correção, siga os passos abaixo:

![Imagem 3: Identifique na Central de Notas, os itens, a incidência do CST IPI. Deverá estar diferente de ' -1:Não sujeita ao IPI '.](https://ajuda.sankhya.com.br/hc/article_attachments/16087113285655) Identifique na Central de Notas, os itens, a incidência do CST IPI.
Deverá estar diferente de '**-1:Não sujeita ao IPI**'.

![Imagem 4: Identifique na Central de Notas, os itens, a incidência do CST IPI. Deverá estar diferente de ' -1:Não sujeita ao IPI '.](https://ajuda.sankhya.com.br/hc/article_attachments/14659750382359)

![Imagem 5: Caso não houve o cálculo de IPI nos itens da NOTA, verifique as configurações para o correto cálculo de IPI.](https://ajuda.sankhya.com.br/hc/article_attachments/16087145800855) Caso não houve o cálculo de IPI nos itens da NOTA, verifique as [configurações para o correto cálculo de IPI.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042753354)

Identifique e faça os ajustes para o correto cálculo de IPI nos itens da nota.

![Imagem 6: Redigite os itens ou fature novamente o pedido e, posteriormente, gere o lote da Nota.](https://ajuda.sankhya.com.br/hc/article_attachments/16087145804951) Redigite os itens ou fature novamente o pedido e, posteriormente, gere o lote da Nota.

**![Imagem 7: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/16087113294743) CAUSA**:

Quando for emitida uma NF-e com CFOP iniciado por 3, indicando uma Operação com o Exterior (idDest = 3) e de Entrada (tpNF = 0), e não for informado o Grupo do Imposto sobre Produtos Industrializados (IPI), será retornada a rejeição.

**Exceções a regra:**

![Imagem 8: A regra 597 não se aplica para os seguintes CFOP: 3.201, 3.202, 3.211, 3.503 e 3.553.](https://ajuda.sankhya.com.br/hc/article_attachments/16087113285655) A regra 597 não se aplica para os seguintes CFOP: 3.201, 3.202, 3.211, 3.503 e 3.553.
