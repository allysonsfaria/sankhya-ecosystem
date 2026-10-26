---
id: "9371049526039"
titulo: "Nota/Pedido com financeiro não pode ter valor negativo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9371049526039-Nota-Pedido-com-financeiro-n%C3%A3o-pode-ter-valor-negativo"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T15:08:30Z"
rotulos: ["Configuração", "NF-e", "Movimentação Financeira", "Impostos", "Financeiro", "CORE_E04472", "Nota/pedido com valor negativo não permitido", "Problema causado por configuração incorreta", "Ajuste desconto/impostos para evitar valor negativo", "Erro"]
---

# Nota/Pedido com financeiro não pode ter valor negativo

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18603251913495) MENSAGEM:**

[CORE\_E04472]  Nota/Pedido com financeiro não pode ter valor negativo.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18603251917207) SITUAÇÃO:**

Ao tentar confirmar uma nota/pedido a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18603307510295) CAUSA:**

Quando alguma configuração está incorreta como desconto ou impostos fazem com que o campo Vlr nota fique negativo.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18603307511703) SOLUÇÃO:**

- Verifique se a nota tem impostos e se tem redução, caso não tenha que ser tributada não poderá ter redução.
- Verifique o campo desconto se está correto, caso não esteja necessário realizar os ajustes. A mensagem irá ocorrer quando por alguma configuração indevida o campo Vlr nota ficará com valor negativo.

![Imagem 5: Verifique o campo desconto se está correto, caso não esteja necessário realizar os ajustes. A mensagem irá ocorrer…](https://ajuda.sankhya.com.br/hc/article_attachments/18603307515287)
