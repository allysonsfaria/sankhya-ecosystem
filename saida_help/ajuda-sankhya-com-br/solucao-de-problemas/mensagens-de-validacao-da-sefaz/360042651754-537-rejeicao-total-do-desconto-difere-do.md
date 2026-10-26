---
id: "360042651754"
titulo: "537 Rejeição: Total do Desconto difere do somatório dos itens."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042651754-537-Rejei%C3%A7%C3%A3o-Total-do-Desconto-difere-do-somat%C3%B3rio-dos-itens"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:07:07Z"
rotulos: ["ERRONF", "Configuração", "NF-e", "SEFAZ", "Impostos", "537", "Divergência no Total de Desconto", "Erro"]
---

# 537 Rejeição: Total do Desconto difere do somatório dos itens.

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16505642799511) MENSAGEM**:

537 Rejeição: Total do Desconto difere do somatório dos itens.

**![Imagem 2: SOLUÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/16505642801047) SOLUÇÃO**:

Para correção, siga os passos abaixo:

![Imagem 3: Acesse: Configurações » Avançado » Preferências](https://ajuda.sankhya.com.br/hc/article_attachments/16505662399511) Acesse: Configurações » Avançado » Preferências

(1)** PARÂMETROS:**

- **"DISTJDCONF**-**Distribuir desc. na confirmação da nota?"**: ligado
- **"DISTJURO**-**Opção para distribuir Juros entre os Produtos?"**: ligado
- **"DISTDESCNFE-Distribuir desc. na confirmação da NFE?":** ligado

Os 2(dois) primeiros parâmetros são para qualquer documento e o último para Nota Fiscal Eletrônica.

- Com os parâmetros ligados, qualquer desconto/juro dado no rodapé da nota será automaticamente 'rateado' entre os itens da nota na confirmação . Importante não efetuar a adição de desconto/juro após a nota ser confirmada, pois não haverá o rateio automático entre os itens.
- Deve-se verifique e refaça o somatório do Valor do Desconto de cada item e corrija o Valor do Desconto informado nos Totais da NF-e.

Há uma tolerância para mais ou para menos de R$ 0,01 de diferença do valor calculado sem aproximações.

![Imagem 4: Após os ajustes, gere lote da NF-e/NFC-e novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16505662407959) Após os ajustes, gere  lote da NF-e/NFC-e novamente.

**![Imagem 5: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/16505642811159) CAUSA**:

Quando for emitida uma NF-e/NFC-e com Total do Desconto da NF-e/NFC-e diferente do somatório do Valor de Desconto de cada item da NF-e/NFC-e, será retornada a rejeição.

![Imagem 6: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16505642813463) **OBSERVAÇÃO:**

[Manual de Orientação do Contribuinte](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=9hd38oni4Nc=)
