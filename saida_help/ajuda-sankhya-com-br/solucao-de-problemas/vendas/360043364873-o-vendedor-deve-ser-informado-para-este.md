---
id: "360043364873"
titulo: "O vendedor deve ser informado para este item"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043364873-O-vendedor-deve-ser-informado-para-este-item"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:05:18Z"
rotulos: ["#PUBLIFER", "CORE_E03250", "Configuração", "Vendedor", "TOP", "Itens", "Verifique \"Exige vendedor nos itens\" no Tipo de Operação", "Mensagem: Vendedor obrigatório para item", "Preencha o campo Vendedor ou ajuste configuração", "Erro"]
---

# O vendedor deve ser informado para este item

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16309602196759) MENSAGEM:**

[CORE\_E03250] O vendedor deve ser informado para este item.

![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16309602197783) **SOLUÇÃO:**

![Imagem 3: Verifique se a marcação "Exige vendedor nos itens" , realizada no cadastro do "Tipo de Operação" utilizado, está de…](https://ajuda.sankhya.com.br/hc/article_attachments/16309542085399) Verifique se a marcação **"Exige vendedor nos itens"**, realizada no cadastro do **"Tipo de Operação"** utilizado, está de acordo com o processo da empresa:

**(1)**Tela [**Tipos de Operação - TOP**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Caminho de acesso: Comercial » Arquivo » Cadastros)

**(1)**Campo Exige vendedor nos itens

O campo Exigir vendedor nos itens é usado quando vários vendedores atendem uma mesma nota ou pedido, para permitir cálculo de comissão e organização dos dados. Se esta opção for selecionada, será obrigatório o preenchimento do campo **"Vendedor"** nos itens das notas nos Portais.

![Imagem 4: Caso a configuração acima esteja incorreta, desmarque a mesma, salve as alterações. Após ajustes exclua o lançamento…](https://ajuda.sankhya.com.br/hc/article_attachments/16309602204055) Caso a configuração acima esteja incorreta, desmarque a mesma, salve as alterações. Após ajustes exclua o lançamento atual e refaça o mesmo.

![Imagem 5: Caso a configuração esteja correta, revise para cada item do lançamento, qual deles consta com a informação Vendedor em…](https://ajuda.sankhya.com.br/hc/article_attachments/16309542090775) Caso a configuração esteja correta, revise para cada item do lançamento, qual deles consta com a informação Vendedor em branco ou zero e preencha com um código de vendedor ativo:

![Imagem 6: Caso a configuração esteja correta, revise para cada item do lançamento, qual deles consta com a informação Vendedor em…](https://ajuda.sankhya.com.br/hc/article_attachments/14339538141463)

![Imagem 7: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/17372192224535) **IMPORTANTE:**

Caso trabalhe com vendedor por itens e não visualize esse campo em seu lançamento, basta adicioná-lo em 'Itens' através da tela **"Configurador de layout da nota"**.

Para mais detalhes: **[Configurador de Layout da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634)**

![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16309542094615) **CAUSA:**

Quando utilizado um Tipo de Operação que exija vendedor nos itens e determinado item da nota não possuir essa informação, a validação acontecerá.
