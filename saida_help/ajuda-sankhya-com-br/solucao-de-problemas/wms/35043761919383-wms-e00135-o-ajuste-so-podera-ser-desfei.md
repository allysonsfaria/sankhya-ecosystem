---
id: "35043761919383"
titulo: "WMS_E00135: o ajuste só poderá ser desfeito após a deleção da nota de ajuste"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35043761919383-WMS-E00135-o-ajuste-s%C3%B3-poder%C3%A1-ser-desfeito-ap%C3%B3s-a-dele%C3%A7%C3%A3o-da-nota-de-ajuste"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T14:26:06Z"
rotulos: ["Portal de Compras", "Inventário", "WMS", "Portal de Vendas", "Histórico de Ajuste de Estoque", "Estoque", "Erro", "WMS_E00135", "O ajuste só poderá ser desfeito após a deleção da nota de ajuste", "Tipo de divergência"]
---

# WMS_E00135: o ajuste só poderá ser desfeito após a deleção da nota de ajuste

**MENSAGEM**

[WMS\_E00135] O ajuste só poderá ser desfeito após a deleção da nota de ajuste.

**SITUAÇÃO**

Esta mensagem aparece quando o usuário tenta desfazer um ajuste de inventário que já possui \*\*notas de ajuste\*\* (falta ou sobra) geradas e vinculadas ao processo.

**SOLUÇÃO**

**(1)** Acesse a tela **"Histórico de Ajuste de Estoque"** (WMS » Inventário » Histórico de Ajuste de Estoque) e verifique qual o **"Tipo de divergência"** gerada: **"Falta" ou "Sobra".**

**(2)** Se existir mais de um ajuste para o mesmo inventário, valide **todos os ajustes** gerados.

**(3)** Caso o tipo de ajuste seja **Falta:**

- Acesse a tela **"Portal de Vendas"** (Comercial » Consulta » Portal de Vendas)
- Filtre a nota de ajuste de saída gerada para os produtos e exclua essa nota

**(4)** Caso o tipo de ajuste seja **Sobra:**

- Acesse a tela **"Portal de Compras"** (Comercial » Consulta » Portal de Compras)
- Filtre a nota de ajuste de sobra gerada para os produtos  e exclua essa nota

**(5)** Retorne à tela **"Histórico de Ajuste de Estoque"** (WMS » Inventário » Histórico de Ajuste de Estoque) e desfaça o ajuste gerado, agora sem as notas vinculadas.

**CAUSA**

O erro ocorre quando um ajuste de inventário já teve as notas de sobra ou falta geradas e vinculadas ao ajuste, impedindo que o processo seja desfeito diretamente.
