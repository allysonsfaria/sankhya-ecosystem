---
id: "360043577154"
titulo: "Lote deve ser informado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043577154-Lote-deve-ser-informado"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T16:01:59Z"
rotulos: ["#criadoRoger", "#Revisadoclaudio", "Produtos", "Configuração", "Lote", "Estoque", "Movimentações de Estoque", "ORA-20101", "ORA-06512", "ORA-04088", "Controle de Lote", "Informação de Lote", "Erro"]
---

# Lote deve ser informado

![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16107145270551) **MENSAGEM**:

[ORA-20101]: Lote deve ser informado.
[ORA-06512]: em "SANKHYA.TRG\_UPT\_TGFITE", line 703
[ORA-04088]: erro durante a execução do gatilho 'SANKHYA.TRG\_UPT\_TGFITE'

**![Imagem 2: SOLUÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/16107129546519) SOLUÇÃO**:

Considere o Comportamento da Aplicação conforme abaixo:

![Imagem 3: Quando o produto possuir controle adicional de LOTE, no ato da Compra informe o número de lote (geralmente seguido de…](https://ajuda.sankhya.com.br/hc/article_attachments/16107145279127) Quando o produto possuir controle adicional de LOTE, no ato da Compra informe o número de lote (geralmente seguido de data de Fabricação e Validade).

![Imagem 4: A principal premissa é que esse produto não sofra alteração em seu cadastro, ou seja, não alterar a configuração do…](https://ajuda.sankhya.com.br/hc/article_attachments/16107145280407) A principal premissa é que esse produto não sofra alteração em seu cadastro, ou seja, não alterar a configuração do controle adicional.

(1)** Vejamos:**
No ato da Compra ou Produção um produto com controle adicional de estoque deverá informar o número de Lote.

**(2)** Se houver devolução de compra, informe o número de Lote.

**(2)** Se houver venda, informe o número de Lote.

**(2)** Se houver devolução da venda, informe o número de lote.

Esse controle é imprescindível para que não ocorra a mensagem (ORA-20101: Lote deve ser informado. ), em algum documento.

Recomendações caso ocorre a mensagem: **"ORA-20101: Lote deve ser informado".**

![Imagem 5: Verifique o histórico do produto em " Gerência de Produtos " , para observar as movimentações do produto (atentar-se…](https://ajuda.sankhya.com.br/hc/article_attachments/16107129567383) Verifique o histórico do produto em **"[Gerência de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111253-Ger%C3%AAncia-de-Produtos)"**, para observar as movimentações do produto (atentar-se para Local, Controle).

![Imagem 6: Verifique o cadastro do produto, aba " Medidas e Estoque " , sub-aba "Controle Adicional" , campo "Controlar por:"…](https://ajuda.sankhya.com.br/hc/article_attachments/16107145294487) Verifique o cadastro do produto, aba **"[Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abamedidaseestoque)"**, sub-aba **"Controle Adicional"**, campo **"Controlar por:" "Numero de Lote"**

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16107129570711) CAUSA:**

Ocorre quando o produto tem controle adicional por lote e o lote não foi informado.
