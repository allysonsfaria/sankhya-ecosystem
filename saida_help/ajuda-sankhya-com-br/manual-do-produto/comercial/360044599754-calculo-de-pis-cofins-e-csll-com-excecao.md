---
id: "360044599754"
titulo: "Cálculo de PIS, COFINS e CSLL com exceção por Finalidade da Operação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599754-C%C3%A1lculo-de-PIS-COFINS-e-CSLL-com-exce%C3%A7%C3%A3o-por-Finalidade-da-Opera%C3%A7%C3%A3o"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:22:23Z"
rotulos: ["AJUDA DO SKW", "Configuração", "COFINS", "PIS", "CSLL", "Finalidade da Operação - PIS/COFINS/CSLL manual", "Finalidade", "Operação", "Impostos", "Configuração de PIS/COFINS/CSLL por Finalidade da Operação", "Finalidade da Operação"]
---

# Cálculo de PIS, COFINS e CSLL com exceção por Finalidade da Operação

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311773824663) Módulo: Comercial > Arquivo > Cadastros
```

---

Através da configuração efetuada na tela [Finalidade da Operação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599434-Finalidade-da-Opera%C3%A7%C3%A3o), é possível realizar cadastros para serem utilizados na rotina de exceção para o cálculo do [PIS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600434-Al%C3%ADquotas-de-PIS), [COFINS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108813-Al%C3%ADquotas-de-COFINS) e [CSLL](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109933-Al%C3%ADquotas-de-CSLL)  em pedidos e/ou notas fiscais.

Para isso, ao cadastrar a Finalidade da Operação, deve-se definir no campo **"Sigla"** a variável que será usada como parâmetro para definir a exceção. Esta sigla pode ser, por exemplo, a primeira letra que melhor identifique a finalidade.

Na prática, pode-se ter o seguinte cadastro: na **"Descrição"**, define-se a finalidade da operação como **"Imobilizado"** e, na sigla, a variável **"I"**.

![Imagem 2: Na prática, pode-se ter o seguinte cadastro: na "Descrição" , define-se a finalidade da operação como "Imobilizado" e,…](https://ajuda.sankhya.com.br/hc/article_attachments/23943682598679)

Uma vez definida a variável de exceção, é necessário criar as alíquotas correspondentes de PIS, COFINS e CSLL para que, no lançamento do pedido e/ou nota, o sistema possa buscar a informação correta. A descrição do grupo das alíquotas de PIS, COFINS e CSLL deve indicar a descrição da regra padrão seguida pela sigla definida anteriormente, separadas por dois pontos (:). Considere o seguinte exemplo:

Suponha que um **"Grupo de PIS"** no cadastro de produtos: **"TODOS"**, com as seguintes Finalidades de Operação: **"Imobilizado: I"** e **"Consumo: C"**, sendo que para cada situação aplicam-se diferentes alíquotas, como descrito abaixo:

- Alíquota de PIS para Revenda (padrão): 3%
- Alíquota de PIS para Consumo: 9%
- Alíquota de PIS para Imobilizado: 6%

Neste caso, a alíquota de PIS deverá ser cadastrada três vezes, da seguinte forma:

- Grupo: TODOS à Alíquota: 3%
- Grupo: TODOS:I à Alíquota: 6%
- Grupo: TODOS:C à Alíquota: 9%

Na ótica do pedido e/ou nota, ao informar o código da Finalidade da Operação cadastrada anteriormente no lançamento do item, o sistema irá verificar se existe alguma alíquota de PIS, COFINS e CSLL registrada nos moldes indicados acima. Caso exista, esta será considerada na aplicação do cálculo dos impostos citados. Caso contrário, será utilizada a alíquota padrão. 

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599754-C%C3%A1lculo-de-PIS-COFINS-e-CSLL-com-exce%C3%A7%C3%A3o-por-Finalidade-da-Opera%C3%A7%C3%A3o#top)
