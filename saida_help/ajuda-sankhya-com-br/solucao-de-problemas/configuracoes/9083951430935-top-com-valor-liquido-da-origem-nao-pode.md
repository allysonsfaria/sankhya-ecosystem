---
id: "9083951430935"
titulo: "TOP com 'Valor Líquido da origem' não pode ser lançada aqui"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9083951430935-TOP-com-Valor-L%C3%ADquido-da-origem-n%C3%A3o-pode-ser-lan%C3%A7ada-aqui"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:10:54Z"
rotulos: ["Configuração", "TOP", "CORE_E01488", "Correção de Erro em Configuração de Preço em Tipo de Operação", "Erro", "Compras"]
---

# TOP com 'Valor Líquido da origem' não pode ser lançada aqui

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18952491291159) MENSAGEM:**

[CORE\_E01488] TOP com 'Valor Líquido da origem' não pode ser lançada aqui.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18952491297303) SITUAÇÃO:**

Ao tentar lançar uma compra na central de compras a mensagem é apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18952491306263)SOLUÇÃO:**

![Imagem 4: Revise a configuração do campo "Usar como preço" no Tipo de operação TOP (Comercial » Arquivo » Cadastros » Tipos de…](https://ajuda.sankhya.com.br/hc/article_attachments/18952491315991) Revise a configuração do campo "Usar como preço" no **Tipo de operação TOP** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) utilizada no lançamento. Para TOP de compra, o campo 'Usar como preço' não deverá estar selecionado como Valor Líquido da origem.

**![Imagem 5: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/18952491318679) IMPORTANTE:**

Existe um processo Específico envolvendo o campo Usar como Preço, onde:

A opção Valor líquido da origem deverá ser utilizada nas TOP's de Remessa, nas quais a "Nota de Remessa" será gerada com o valor líquido da origem. Para mais informações acesse o [manual de Tipos de Operação.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18952470070551)CAUSA:**

Ocorre ao definir o campo usar como preço como valor liquido da origem em TOP de compra.
