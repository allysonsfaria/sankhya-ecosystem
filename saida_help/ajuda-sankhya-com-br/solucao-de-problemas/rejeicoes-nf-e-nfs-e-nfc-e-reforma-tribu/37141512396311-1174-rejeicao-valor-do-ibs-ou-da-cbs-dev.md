---
id: "37141512396311"
titulo: "1174 Rejeição: Valor do IBS ou da CBS deve ser maior que zero no estorno de crédito [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37141512396311-1174-Rejei%C3%A7%C3%A3o-Valor-do-IBS-ou-da-CBS-deve-ser-maior-que-zero-no-estorno-de-cr%C3%A9dito-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:19:12Z"
rotulos: ["NF-e", "Central de Vendas", "SEFAZ", "Impostos", "Alíquotas de CBS", "Alíquotas de IBS", "Valor do IBS ou da CBS", "Valor deve ser maior que zero no estorno de crédito", "Estorno de crédito do IBS e da CBS", "Estorno de Crédito"]
---

# 1174 Rejeição: Valor do IBS ou da CBS deve ser maior que zero no estorno de crédito [nItem: 999]

**MENSAGEM**

1174 Rejeição: Valor do IBS ou da CBS deve ser maior que zero no estorno de crédito [nItem: 999]

**SITUAÇÃO**

Ao emitir uma nota fiscal com estorno de crédito do IBS e da CBS, o documento foi rejeitado pela SEFAZ porque os valores do IBS e da CBS no grupo de estorno de crédito foram informados como zero ou não foram preenchidos.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas) e localize a nota fiscal que foi rejeitada.

**(2)** Gere o arquivo da XML e verifique se a nota fiscal é do tipo **''Nota de Débito''** (finNFe=6) e se possui o grupo de estorno de crédito.

**(3)** Na grade **"Itens"** da nota fiscal e verifique o item que está apresentando a rejeição.

**(4)** Clique em **''Outras opções'' (ícone com três pontos)** e selecione a opção **''Consultar/Alterar Dados do Imposto do Item''**.

**(5)** Verifique o grupo de **Estorno de Crédito**.

**(6)** Certifique-se de que pelo menos um dos campos abaixo esteja preenchido com valor **maior que zero**:

- Campo **"Valor"** (vIBS);
- Campo **"Valor"** (vCBS).

**(7)** Após corrigir os valores, salve as alterações e tente emitir a nota fiscal novamente.

**CAUSA**

Esta rejeição ocorre quando o grupo de estorno de crédito (**gEstornoCred**) é informado na nota fiscal, mas os valores do IBS e da CBS estão zerados ou não foram preenchidos. De acordo com a regra de validação UB116-30, quando o grupo de estorno de crédito é informado, pelo menos um dos valores (IBS ou CBS) deve ser maior que zero.

A única exceção para esta regra é quando a nota fiscal de débito é do tipo "07-Perda em estoque" (campo **tpNFDebito**), situação em que a regra não se aplica.
