---
id: "360043656193"
titulo: "A base e o valor do IPI devem ser zero (0)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043656193-A-base-e-o-valor-do-IPI-devem-ser-zero-0"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:04:38Z"
rotulos: ["Produtos", "Configuração", "NF-e", "Central de Vendas", "IPI", "Impostos", "ORA-20101", "Base de IPI", "Valor de IPI"]
---

# A base e o valor do IPI devem ser zero (0)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16143358736535) MENSAGEM:**

ORA-20101: A base e o valor do IPI devem ser zero (0).
ORA-06512: em "SANKHYA.TRG\_INC\_TGFITE", line 406
ORA-04088: erro durante a execução do gatilho 'SANKHYA.TRG\_INC\_TGFITE'
SQL-50001 - A base e o valor de IPI devem ser zero (0)

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16143366443287) SITUAÇÃO:**

Ao realizar o faturamento de um pedido em nota pela tela **"[Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas)"** no **SankhyaW**, apresenta a mensagem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16143366444695) SOLUÇÃO:**

Para solução, siga os passos abaixo:

![Imagem 4: Acesse: Comercial » Consulta » Portal de Vendas:](https://ajuda.sankhya.com.br/hc/article_attachments/16143358742039) Acesse: Comercial » Consulta » Portal de Vendas:

**(2)** Selecione o pedido/nota, acesse a grade de itens e verifique os campos de **"Base do IPI"**, **"Aliq. IPI"** e **"Vlr. IPI"**, em todos os itens da nota.

![Imagem 5: Pode ser que algum produto tenha informações do valor de IPI, porém no cadastro do produto não está marcado para…](https://ajuda.sankhya.com.br/hc/article_attachments/16143366449687) Pode ser que algum produto tenha informações do valor de IPI, porém no cadastro do produto não está marcado para **"Calcular IPI na Venda"**. Então acesse:

**(2)** Configurações » Cadastros » Produtos » Produtos:

**(3)**Aba **"Imposto"**, campo **"Tem IPI na Venda"**

![Imagem 6: (3) Aba "Imposto" , campo "Tem IPI na Venda"](https://ajuda.sankhya.com.br/hc/article_attachments/14662051331479)

**(2)** Confira o % (percentual) de IPI que incide em cada item, antes de confirmar/faturar o pedido/nota.

**(2)** O mesmo vale para processo de compra, alterando para a opção: **"Tem IPI na Compra".**

**![Imagem 7: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16143358753175) OBSERVAÇÃO:**

Qualquer dúvida nas configurações, sobre a incidência de IPI, procure a contabilidade para esclarecimentos.

![Imagem 8: Após os ajustes, redigite os itens e fature.](https://ajuda.sankhya.com.br/hc/article_attachments/16143358754967) Após os ajustes, redigite os itens e fature.

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16143358755735)CAUSA:**

Após o lançamento foram realizadas alterações no cadastro do produto em relação a incidência de IPI e com isso causa divergência do cálculo de IPI.
