---
id: "37097856297751"
titulo: "1089 Rejeição: Total Devolvido da CBS difere da soma dos itens"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37097856297751-1089-Rejei%C3%A7%C3%A3o-Total-Devolvido-da-CBS-difere-da-soma-dos-itens"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:20:28Z"
rotulos: ["NF-e", "Central de Vendas", "XML", "SEFAZ", "Impostos", "Erro", "Alíquotas de CBS", "nota fiscal de devolução com valores de CBS", "total devolvido da CBS", "soma dos valores de CBS"]
---

# 1089 Rejeição: Total Devolvido da CBS difere da soma dos itens

**MENSAGEM**

1089 Rejeição: Total Devolvido da CBS difere da soma dos itens

**SITUAÇÃO**

Ao emitir uma nota fiscal de devolução com valores de CBS, o sistema está calculando incorretamente o total devolvido da CBS, gerando uma divergência entre o valor total informado e a soma dos valores de CBS de cada item da nota.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas).

**(2)** Localize a nota fiscal rejeitada.

**(3)** Acesse a **grade de Itens** da nota e selecione qualquer item.

**(4)** Forçe o recálculo dos valores:

- Altere temporariamente um campo do item (por exemplo, modifique a **quantidade** de 1 para 2 e pressione Enter);
- Em seguida, retorne o valor ao original (de 2 para 1);
- Salve o item e a nota fiscal para que o sistema recalcule automaticamente os valores.

**(5)** Na aba **''Reforma Tributária''**, verifique se o campo **''Valor total de devolução de tributos (CBS)''** está preenchido corretamente nos itens aplicáveis.

**(6)** Após a validação dos dados, **gere um novo lote** ou **reenvie a nota fiscal** para transmissão.

**(7)** O sistema irá **gerar um novo XML com os totais atualizados**, permitindo a **autorização da nota fiscal**.

**CAUSA**

Esta rejeição ocorre quando o valor total devolvido da CBS informado no documento fiscal é diferente da soma dos valores de CBS de cada item da nota. Conforme as regras de validação da SEFAZ, o total do valor devolvido da CBS deve corresponder exatamente à soma dos valores de CBS de todos os itens da nota fiscal de devolução. A divergência pode ocorrer quando o sistema não está configurado para calcular proporcionalmente os valores de CBS nos itens, ou quando há arredondamentos que não estão sendo tratados corretamente no cálculo total.
