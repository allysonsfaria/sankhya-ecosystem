---
id: "360042643374"
titulo: "Total do PIS difere do somatório dos itens sujeitos ao ICMS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042643374-Total-do-PIS-difere-do-somat%C3%B3rio-dos-itens-sujeitos-ao-ICMS"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:07:21Z"
rotulos: ["ERRONF", "#RevisadoBernardo", "Configuração", "NF-e", "PIS", "SEFAZ", "Impostos", "602", "Divergência no Total do PIS", "Erro", "Artigo atualizado KCS", "Docs Eletrônicos - KCS"]
---

# Total do PIS difere do somatório dos itens sujeitos ao ICMS

**MENSAGEM**

Rejeição 602: Total do PIS difere do somatório dos itens sujeitos ao ICMS.

**SITUAÇÃO**

Ao realizar a emissão de uma nota fiscal, o sistema apresenta a rejeição 602, indicando que o valor total do PIS informado no cabeçalho da nota não corresponde à soma dos valores de PIS calculados em cada item da nota.

**CAUSA**

Esta rejeição ocorre quando há uma divergência entre o valor total do tributo acumulado nos itens e o valor total reportado no rodapé da nota, geralmente causado por diferenças de arredondamento ou parametrizações incorretas de impostos nos itens da nota.

**SOLUÇÃO**

Para corrigir esta situação, siga os passos abaixo:

Acesse a tela **"Portal de vendas"** (Comercial >>consulta >> Portal de Vendas).

Localize a nota que apresentou a rejeição e clique na aba **"Itens"**.

Verifique se o valor do PIS em cada item está calculado corretamente conforme a configuração de impostos definida na tela **"Alíquotas de PIS"** (Comercial >> Arquivo >> Cadastros >> Alíquotas).

Certifique-se de que não existem itens com valores de PIS zerados que deveriam possuir tributação, ou vice-versa.

Revise os itens e as alterações se necessário

Salve a nota e tente realizar a emissão novamente.
