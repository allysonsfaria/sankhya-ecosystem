---
id: "37141553594135"
titulo: "1124 Rejeição: Valor do Crédito Presumido da CBS não pode ser superior a vProd [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37141553594135-1124-Rejei%C3%A7%C3%A3o-Valor-do-Cr%C3%A9dito-Presumido-da-CBS-n%C3%A3o-pode-ser-superior-a-vProd-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:19:08Z"
rotulos: ["NF-e", "Central de Vendas", "SEFAZ", "Crédito", "Erro", "CBS", "Artigo atualizado KCS", "4-Aquisição de bens móveis de PF não contribuinte para revenda", "Valor do Crédito Presumido da CBS", "código de classificação do crédito presumido", "Docs Eletrônicos - KCS"]
---

# 1124 Rejeição: Valor do Crédito Presumido da CBS não pode ser superior a vProd [nItem: 999]

**MENSAGEM**

1124 Rejeição: Valor do Crédito Presumido da CBS não pode ser superior a vProd [nItem: 999]

**SITUAÇÃO**

A nota fiscal foi emitida com a informação de crédito presumido da CBS vinculada a uma operação classificada como aquisição de bens móveis de pessoa física não contribuinte para revenda, na qual o valor do crédito presumido informado supera o valor total do produto registrado no documento.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas) e localize o documento que apresentou a rejeição.

**(2)** Verifique o item que está apresentando o erro (indicado pelo número no final da mensagem de rejeição [nItem: 999]).

**(3)** Na grade **''Itens''**, aperte em **''Outras opções'' (ícone com três pontos)**, e selecione a opção **''Consultar/Alterar Dados do Imposto do Item''**.

**(4)** Verifique o valor informado no campo **''Valor do Crédito Presumido''**.

**(5)** Certifique-se de que o valor do crédito presumido da CBS não seja superior ao valor do produto (vProd) para o item em questão.

**(6)** Ajuste o valor do crédito presumido da CBS para que seja **igual ou inferior** ao valor do produto.

**(7)** Caso esteja utilizando o código de classificação do crédito presumido **"4-Aquisição de bens móveis de PF não contribuinte para revenda"**, verifique se o valor do crédito presumido está sendo calculado corretamente.

**(8)** Salve as alterações e tente emitir o documento fiscal novamente.

**CAUSA**

Esta rejeição ocorre devido a uma **regra específica de validação** da Sefaz para operações com código de classificação do crédito presumido igual a "4-Aquisição de bens móveis de PF não contribuinte para revenda" (como veículos ou itens de brechó). Nestes casos, o valor do crédito presumido da CBS não pode ser superior ao valor do produto (vProd).

A regra de validação UB129-10 estabelece que, quando informado o valor do crédito presumido da CBS e o código de classificação do crédito presumido for igual a "4-Aquisição de bens móveis de PF não contribuinte para revenda", o valor do crédito presumido (tag: vCredPres) não pode ser superior ao valor do produto (vProd).

Esta limitação visa garantir que o crédito presumido da CBS não exceda o valor do próprio produto, mantendo a coerência fiscal nas operações de aquisição de bens móveis de pessoas físicas não contribuintes para revenda.
