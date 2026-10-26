---
id: "37097916535063"
titulo: "1087 Rejeição: Total de Crédito Presumido da CBS difere da soma dos itens"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37097916535063-1087-Rejei%C3%A7%C3%A3o-Total-de-Cr%C3%A9dito-Presumido-da-CBS-difere-da-soma-dos-itens"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:20:27Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Passos para resolver", "Erro", "Como Resolver", "Alíquotas de CBS", "Soma dos itens", "Total de Crédito Presumido", "Crédito Presumido da CBS", "Total de Crédito Presumido da CBS"]
---

# 1087 Rejeição: Total de Crédito Presumido da CBS difere da soma dos itens

**MENSAGEM**

1087 Rejeição: Total de Crédito Presumido da CBS difere da soma dos itens

**SITUAÇÃO**

O valor total do Crédito Presumido da CBS informado na NF-e não corresponde ao somatório dos valores de Crédito Presumido da CBS dos itens do documento fiscal.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas).

**(2)** Na grade **''Itens''**, clique em **''Outras Opções'' (ícone com três pontos)** e selecione **''Consultar/Alterar Dados do Imposto do Item''**.

**(3)** Localize a aba correspondente à **''CBS''** e verifique se todos os itens que deveriam possuir **Crédito Presumido** estão devidamente configurados.

**(4)** Para cada item, verifique se o **Código de Classificação do Crédito Presumido** está corretamente selecionado, conforme a natureza da operação realizada.

**(5)** Confira se os **valores do Crédito Presumido** estão sendo calculados corretamente para cada item. O valor deve ser resultante da fórmula:

```
vCredPres = vCBS * (1 - pCredPres / 100), exceto para o código 4 (Aquisição de bens móveis de PF não contribuinte para revenda).
```

**(6)** Acesse a tela **''Tipos de Operação - TOP''** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP), e verifique se o TOP utilizado na nota está configurado corretamente para a operação com Crédito Presumido da CBS.

**(7)** Após realizar as correções, recalcule os valores da nota e tente emitir novamente o documento fiscal.

**CAUSA**

A rejeição ocorre devido a uma **inconsistência no cálculo do Crédito Presumido da CBS**. Esta inconsistência pode ser causada por:

- Erro no cálculo automático do sistema ao somar os valores de Crédito Presumido da CBS de cada item;
- Configuração incorreta do Código de Classificação do Crédito Presumido em um ou mais itens da nota;
- Alteração manual dos valores de Crédito Presumido da CBS sem o devido recálculo do total;
- Divergência entre o percentual do Crédito Presumido aplicado e o valor calculado, conforme a regra de validação UB81-10 que determina que o valor do Crédito Presumido deve ser resultante do valor da CBS multiplicado pelo fator (1 - pCredPres / 100).
