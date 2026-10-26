---
id: "360043696393"
titulo: "Há um ou mais produtos cujo valor não é suficiente para subtrair os valores de desconto e de repasse de redução: XXXX"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043696393-H%C3%A1-um-ou-mais-produtos-cujo-valor-n%C3%A3o-%C3%A9-suficiente-para-subtrair-os-valores-de-desconto-e-de-repasse-de-redu%C3%A7%C3%A3o-XXXX"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:03:24Z"
rotulos: ["#criadoRoger", "Produtos", "Configuração", "NF-e", "ICMS", "Impostos", "TOP", "CORE_E00346", "Verifique alíquotas de ICMS e ajuste valores", "Valor insuficiente para desconto/repasse: XXXX", "Repasse de imposto parcial/total sem cálculo"]
---

# Há um ou mais produtos cujo valor não é suficiente para subtrair os valores de desconto e de repasse de redução: XXXX

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16309998331415) MENSAGEM:**

[CORE\_E00346] Há um ou mais produtos cujo valor não é suficiente para subtrair os valores de desconto e de repasse de redução: XXXX.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16309998334999) SOLUÇÃO:**

Para correção siga  os passos abaixo:

**(1)** Acesse a tela **"Alíquotas de ICMS"** (Caminho de acesso: Comercial » Arquivo » Cadastros » Alíquotas):

**(2)** De acordo com a TOP utilizada, no documento criado (Pedido/Nota/Orçamento), se houver cálculo de ICMS nos itens, acesse o cadastro de Alíquotas de ICMS, identifique a regra de ICMS que incidiu nos itens.

**(2)** Verifique as marcações sobre **[Repassar para o cliente](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934)**, se os valores unitários dos itens forem zero ou insuficiente para o repasse, será apresentado a mensagem. Deverá então, considerar de acordo com a contabilidade, o ajuste nas alíquotas de ICMS ou inserir valor unitário nos itens.

![Imagem 3: (2) Verifique as marcações sobre Repassar para o cliente , se os valores unitários dos itens forem zero ou insuficiente…](https://ajuda.sankhya.com.br/hc/article_attachments/14393601641495)

**![Imagem 4: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/16309998344471) CAUSA**:

Ocorre quando o repasse do imposto é parcial ou total ao cliente e não há o cálculo para considerar o repasse, geralmente quando o pedido/nota calculou ICMS e não possui valor unitário nos itens.
