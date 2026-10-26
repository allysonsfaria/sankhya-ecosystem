---
id: "37308310375703"
titulo: "Duplicação de pedido antigo mantém desconto promocional expirado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37308310375703-Duplica%C3%A7%C3%A3o-de-pedido-antigo-mant%C3%A9m-desconto-promocional-expirado"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-31T21:41:58Z"
rotulos: ["Configuração", "Portal de Vendas", "Atualização", "Desconto", "Vendas", "Duplicação de pedido antigo", "condições comerciais vigentes", "Atualiza preço", "desconto promocional expirado", "recálculo do preço do produto", "ATUALPRECOCPVEN"]
---

# Duplicação de pedido antigo mantém desconto promocional expirado

Ao duplicar um pedido de venda no [**''Portal de Vendas''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas) que **possuía desconto promocional, o sistema mantém automaticamente o desconto**, mesmo que a promoção já tenha expirado, e não solicita a liberação de limites.

Essa situação ocorre **quando não é solicitado o recálculo do preço do produto no momento da duplicação**, o que faz com que o desconto original seja aplicado ao novo pedido, **podendo gerar divergências em relação às condições comerciais vigentes**.

**Procedimento**

**(1)** Ao duplicar um pedido, no pop-up **“Duplicar/Copiar Documento”**, é exibida a opção **“Atualiza preço”**.

**(1)** Quando essa opção é marcada, o sistema recalcula os valores dos itens e verifica se há alguma promoção vigente.

**(1)**Caso não exista promoção ativa, o desconto não será aplicado no novo pedido. Portanto, marque a flag **“Atualiza preço”** no pop-up **“Duplicar/Copiar Documento”**.

**OBSERVAÇÃO:** Se o parâmetro **ATUALPRECOCPVEN** estiver habilitado, essa opção já será apresentada marcada automaticamente.
