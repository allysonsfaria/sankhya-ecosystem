---
id: "360043579594"
titulo: "Nota com Valor Igual a Zero. Cancelando Operação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043579594-Nota-com-Valor-Igual-a-Zero-Cancelando-Opera%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T16:01:27Z"
rotulos: ["CORE_E04657", "Produtos", "Configuração", "NF-e", "TOP", "Estoque", "Cancelamento da Operação devido a Valor Zero na Nota", "Erro"]
---

# Nota com Valor Igual a Zero. Cancelando Operação

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16191888236311) MENSAGEM:**

[CORE\_E04657] Nota com Valor Igual a Zero. Cancelando Operação.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16191888238743) SOLUÇÃO:**

![Imagem 3: Acesse o cadastro da TOP que irá originar o lançamento ( Caminho de acesso: Comercial » Arquivo » Cadastros » Tipos de…](https://ajuda.sankhya.com.br/hc/article_attachments/16191902295191) Acesse o cadastro da TOP que irá originar o lançamento (Caminho de acesso: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

![Imagem 4: Na aba Geral verifique a informação que consta no campo: "Usar como preço"](https://ajuda.sankhya.com.br/hc/article_attachments/16191888240919) Na aba **Geral** verifique a informação que consta no campo: **"Usar como preço"**

(1)** Caso de Uso 1:**

- Caso esteja definido, por exemplo: **"Preço de Venda"**, é necessário o produto ter um Preço de Tabela.
- Para comprovar se esse preço existe, acesse a rotina **"[Variação de preços de produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119753)"** e filtre os respectivos produtos, analisando se algum desses não possui preço de venda.
- Utilize o processo de precificação atual da empresa para corrigir essa situação ou reveja a marcação da TOP.

(1)** Caso de Uso 2:**

- Caso escolha por exemplo, **"Custo de Reposição"**, se faz necessário ter um registro de Custo de Reposição.
- Para comprovar se esse preço existe, acesse a rotina Variação de custos de produtos e filtre os respectivos produtos, analisando se algum desses não possui informações na coluna Custo de Reposição.
- Utilize o processo de atualizações de custo atual da empresa para corrigir essa situação ou reveja a marcação da TOP.

![Imagem 5: Por fim, através da rotina " Consulta de Produtos " realize uma verificação do estoque atual dos produtos envolvidos,…](https://ajuda.sankhya.com.br/hc/article_attachments/16191888243735) Por fim, através da rotina "[**Consulta de Produtos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353)" realize uma verificação do estoque atual dos produtos envolvidos, visto que essa mensagem pode ocorrer por ausência de estoque e solicitação de Baixar estoque da TOP utilizada.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16191902303127) CAUSA:**

Ao realizar uma Devolução de Compra, a mensagem poderá ser apresentada nas seguintes situações:

- Quando não tem estoque do produto;
- Quando não possui registro de CUSTO ou Preço Unitário, de acordo com as definições da TOP de devolução.
