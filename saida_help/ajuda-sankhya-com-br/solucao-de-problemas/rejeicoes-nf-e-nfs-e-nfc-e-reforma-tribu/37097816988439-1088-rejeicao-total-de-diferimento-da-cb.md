---
id: "37097816988439"
titulo: "1088 Rejeição: Total de Diferimento da CBS difere da soma dos itens"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37097816988439-1088-Rejei%C3%A7%C3%A3o-Total-de-Diferimento-da-CBS-difere-da-soma-dos-itens"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:20:29Z"
rotulos: ["NF-e", "SEFAZ", "Impostos", "Erro", "Nota Fiscal Eletrônica (NF-e)", "Nota Fiscal de Consumidor Eletrônica (NFC-e)", "Alíquotas de CBS", "Alíquotas de IBS", "CBS (Contribuição sobre Bens e Serviços)", "Grupo de diferimento (gCBS/gDif)"]
---

# 1088 Rejeição: Total de Diferimento da CBS difere da soma dos itens

**MENSAGEM**

1088 Rejeição: Total de Diferimento da CBS difere da soma dos itens

**SITUAÇÃO**

Ao tentar emitir uma Nota Fiscal Eletrônica (NF-e) ou Nota Fiscal de Consumidor Eletrônica (NFC-e) contendo itens com diferimento da CBS (Contribuição sobre Bens e Serviços), o documento foi rejeitado pela SEFAZ porque o valor total do diferimento da CBS informado no documento não corresponde à soma dos valores de diferimento da CBS de cada item.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

**(2)** Verifique se o **''Código de Situação Tributária''** (CST) selecionado possui o indicador que exige o uso de diferimento (ind\_gDif = 1).

**(3)** Acesse a nota fiscal em questão e confira se os valores de diferimento da CBS estão calculados corretamente para cada item, seguindo a fórmula:

```
vDif = vBC x (pCBS / 100) x (pDif / 100).
```

**(4)** Certifique-se de que o **grupo de diferimento (gCBS/gDif)** esteja **corretamente informado** em todos os itens que utilizam **CST com indicador de diferimento obrigatório**.

**(5)** Verifique se o **valor total do diferimento da CBS** informado no documento **corresponde exatamente à soma dos valores de diferimento da CBS de todos os itens**. Embora o sistema realize esse cálculo automaticamente, é importante confirmar se **não há divergências**.

**(6)** Caso sejam identificadas inconsistências, **ajuste os valores de diferimento da CBS nos itens** ou **corrija o valor total do diferimento no documento**, garantindo que ele reflita corretamente a soma dos itens.

**CAUSA**

Esta rejeição ocorre quando há uma inconsistência entre o valor total do diferimento da CBS informado no documento fiscal e a soma dos valores de diferimento da CBS de cada item. Conforme as regras de validação da SEFAZ, quando um CST possui indicador que exige o uso de diferimento (ind\_gDif = 1), é obrigatório informar o grupo de diferimento (gCBS/gDif) e o valor do diferimento deve ser calculado corretamente seguindo a fórmula: vDif = vBC x (pCBS / 100) x (pDif / 100).

O erro pode ocorrer devido a:

- Cálculo incorreto do valor de diferimento em um ou mais itens
- Ausência do grupo de diferimento em itens que utilizam CST com diferimento obrigatório
- Erro na totalização dos valores de diferimento da CBS no documento
- Inconsistências nos percentuais de diferimento aplicados
