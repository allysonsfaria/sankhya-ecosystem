---
id: "37141563909143"
titulo: "1137 Rejeição: Valor total do Item (vItem) não informado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37141563909143-1137-Rejei%C3%A7%C3%A3o-Valor-total-do-Item-vItem-n%C3%A3o-informado"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:19:03Z"
rotulos: ["NF-e", "XML", "SEFAZ", "Detalhe do erro", "Erro", "valor total do item (vItem) não foi informado no XML", "Arquivo XML", "valor total do item (vItem) no XML da nota fiscal", "Valor total do Item não informado"]
---

# 1137 Rejeição: Valor total do Item (vItem) não informado

**MENSAGEM**

1137 Rejeição: Valor total do Item (vItem) não informado

**SITUAÇÃO**

Ao tentar emitir uma Nota Fiscal Eletrônica (NF-e) ou Nota Fiscal de Consumidor Eletrônica (NFC-e), o documento foi rejeitado pela SEFAZ porque o valor total do item (vItem) não foi informado no XML do documento fiscal.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Portal de Vendas"** (Comercial » Consulta » Portal de Vendas).

**(2)** Localize o documento fiscal que foi rejeitado.

**(3)** Clique em **"Gerar Arquivo XML"** para verificar o arquivo XML gerado.

**(4)** Abra o XML gerado e verifique se o campo vItem está preenchido para todos os itens da nota fiscal.

**(5)** Caso o campo não esteja preenchido, acesse a tela **"Central de Vendas"** (Comercial » Rotinas » Central de Vendas).

**(6)** Localize a nota fiscal rejeitada e abra-a para edição.

**(7)** Verifique nos seguintes campos garantindo que:

- O **"Vlr. Unitário"** (vItem) esteja preenchido;
- A **"Quantidade"** (qFaturada) esteja preenchida;
- O **"Vlr. Total''** (vProd) seja igual a vItem × qFaturada.

**(8)** Corrija os valores conforme necessário e salve as alterações.

**(9)** Tente emitir a nota fiscal novamente.

**CAUSA**

A rejeição 1137 ocorre quando o sistema não consegue calcular ou informar o valor total do item (vItem) no XML da nota fiscal. Conforme as regras de totalização da NF-e/NFC-e, o sistema deve calcular o valor total de cada item (vItem) seguindo fórmulas específicas:

Para a **Regra Geral** (quando tpOp ≠ 2 ou nulo):

```
vItem = vProd - vDesc - vICMSDeson (se indDeduzDeson=1) + vICMSST + vICMSMonoReten + vFCPST + vFrete + vSeg + vOutro + vII + vIPI + vIPIDevol + vServ + vPIS (se indSomaPISST=1) + vCofins (se indSomaCOFINSST=1) + vIBS + vCBS + vIS + vTotIBSMonoItem + vTotCBSMonoItem
```

Para **Faturamento Direto** (quando tpOp = 2):

```
vItem = vProd - vDesc - vICMSDeson (se indDeduzDeson=1) + vFrete + vSeg + vOutro + vII + vIPI + vServ + vPIS (se indSomaPISST=1) + vCofins (se indSomaCOFINSST=1) + vIBS + vCBS + vIS
```

Quando o sistema não consegue calcular este valor devido à falta de informações necessárias ou inconsistências nos dados, a nota é rejeitada com o código 1137.
