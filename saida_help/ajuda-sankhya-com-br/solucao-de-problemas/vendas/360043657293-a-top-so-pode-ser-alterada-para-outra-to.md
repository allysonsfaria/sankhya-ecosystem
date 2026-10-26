---
id: "360043657293"
titulo: "A TOP só pode ser alterada para outra TOP que aceite produto repetido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043657293-A-TOP-s%C3%B3-pode-ser-alterada-para-outra-TOP-que-aceite-produto-repetido"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:04:30Z"
rotulos: ["#RevisadoBernardo", "Produtos", "Configuração", "TOP", "Estoque", "CORE_E01491", "TOP Produto Repetido", "Erro"]
---

# A TOP só pode ser alterada para outra TOP que aceite produto repetido

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16137833571479) MENSAGEM:**

[CORE\_E01491] A TOP só pode ser alterada para outra TOP que aceite produto repetido.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16137847645079) SITUAÇÃO:**

Ao alterar a TOP de uma nota/pedido, ocorre a mensagem.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16137847654295) CAUSA:**

Ocorre quando a TOP que está tentando alterar tem a informação incompatível no campo **"Aceitar Produto repetido"** da TOP atual da nota/pedido.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16137847646359) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 5: Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP :](https://ajuda.sankhya.com.br/hc/article_attachments/16137833579031) Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP:

- Aba: **"Estoque"**
- Campo **"Aceitar Produto Repetido":** use o Parâmetro Global
  Ambas as TOP's devem estar configuradas com a mesma informação no campo acima.

![Imagem 6: Campo "Aceitar Produto Repetido": use o Parâmetro Global Ambas as TOP's devem estar configuradas com a mesma informação…](https://ajuda.sankhya.com.br/hc/article_attachments/14684343285271)

**(2)** O campo **"Aceitar Produto Repetido"** serve para determinar se será ou não permitido lançar itens repetidos nos Portais. O sistema tem um parâmetro global, **"Aceita Produto Repetido -ACEITARPRODREP"** que, se estiver ativado, permitirá lançar produtos repetidos; se estiver desativado, não permitirá lançar produtos repetidos. Ainda nesse contexto, considerando que seja inserido o mesmo produto, porém com local de origem e/ou controles diferentes, a inclusão de forma repetida será concedida, independente dos parâmetros mencionados.

**(2)** Desse modo, temos no campo **"Aceitar Produto Repetido"** as seguintes alternativas:

- **Usar o parâmetro Global:** se estiver marcada, o sistema respeitará o que foi definido no parâmetro **"Aceita Produto Repetido -ACEITARPRODREP"**.
- **Sim:** Se estiver marcada, independente do parâmetro global será permitido lançar itens repetidos.
- **Não:** Se estiver marcada, independente do parâmetro global não será permitido lançar itens repetidos.

![Imagem 7: Após o ajuste, modifique a TOP na nota/pedido.](https://ajuda.sankhya.com.br/hc/article_attachments/16137833585687) Após o ajuste, modifique a TOP na nota/pedido.
