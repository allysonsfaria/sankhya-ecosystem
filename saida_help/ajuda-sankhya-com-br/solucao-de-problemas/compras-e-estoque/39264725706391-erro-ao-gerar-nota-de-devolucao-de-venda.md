---
id: "39264725706391"
titulo: "Erro ao gerar nota de devolução de venda - código MGE_EV_203"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39264725706391-Erro-ao-gerar-nota-de-devolu%C3%A7%C3%A3o-de-venda-c%C3%B3digo-MGE-EV-203"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-08-31T01:35:37Z"
rotulos: ["NF-e", "Central de Vendas", "Portal de Vendas", "Estoque", "Devolução", "Erro", "Artigo criado KCS", "CVE - KCS"]
---

# Erro ao gerar nota de devolução de venda - código MGE_EV_203

**Mensagem**

[MGE\_EV\_203] Não possui quantidade de itens pendentes para devolução, verifique em "Outras Opções" no menu "Documentos Relacionados".

**Situação**

Ao tentar gerar uma nota fiscal de devolução de venda pelo Portal de Vendas ou pela Central de Vendas, o sistema não localiza itens pendentes na nota de origem selecionada.

**Solução**

Para resolver esta situação, siga os passos abaixo:

**(1)** Acesse a nota fiscal de venda original na Central de Vendas (Comercial > Movimentação > Central de Vendas).
**(2)** Clique em "Outras Opções" > "Documentos Relacionados".
**(3)** Localize a nota de devolução já gerada para essa nota de origem.
**(4)** Se a devolução necessária já existir, prossiga a partir dela em vez de tentar gerar uma nova.
**(5)** Se já existirem uma ou mais devoluções parciais, confirme se todos os itens da nota original já foram devolvidos, nesse caso, não há mais saldo para uma nova devolução.

**Causa**

Essa mensagem só aparece quando **já existe uma nota de devolução gerada anteriormente para essa mesma nota de origem**, seja total ou por meio de devoluções parciais que já consumiram todos os itens disponíveis. O sistema identifica esse vínculo automaticamente antes de exibir o erro, por isso, sempre haverá uma devolução relacionada a ser encontrada.
