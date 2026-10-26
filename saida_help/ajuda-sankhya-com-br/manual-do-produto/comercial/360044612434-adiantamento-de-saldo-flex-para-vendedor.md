---
id: "360044612434"
titulo: "Adiantamento de Saldo Flex para Vendedores"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612434-Adiantamento-de-Saldo-Flex-para-Vendedores"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:27:00Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Crédito", "Financeiro", "Vendedores", "Adiantamento de Saldo Flex para Vendedores", "br.com.sankhya.adiantamentodesaldoflexvendedor", "Adiantamento de Saldo Flex para Vendedores manual", "Cadastro de Adiantamentos", "PERCRETENCAO", "CODVENDACUVLRRE", "Comercial"]
---

# Adiantamento de Saldo Flex para Vendedores

```
![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42311979698327) Módulo: Comercial > Rotinas
```

---

Cadastre os adiantamentos de saldo para vendedores nesta tela. Após configurar o adiantamento, é possível realizar o débito de forma parcelada. O saldo disponível será atualizado com os créditos/débitos do adiantamento após a liberação das parcelas pendentes realizada através da tela [Atualizar Parcelas Pendentes de Adiantamentos de Saldo Flex](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612254).

![essencial](https://ajuda.sankhya.com.br/hc/article_attachments/16023491531415) A base deve estar atualizada a partir da última versão 3.14 do banco de dados. Além disso, a empresa precisa ter em sua licença os produtos **"Conta Corrente Flex/G"** e/ou **"Conta Corrente Flex/W"**.

### Botões da tela

![Imagem 3: Botões da tela](https://ajuda.sankhya.com.br/hc/article_attachments/23339623890967)

Na parte superior desta tela, têm-se os botões:

#### Novo

Ao clicar no botão ![botão](https://ajuda.sankhya.com.br/hc/article_attachments/15992349420055) **"Novo"**, os campos abaixo serão disponibilizados para configurar o adiantamento:

![Imagem 5: A o clicar no botão "Novo" , os campos abaixo serão disponibilizados para configurar o adiantamento:](https://ajuda.sankhya.com.br/hc/article_attachments/23339954009495)

- **Vendedor:** informe aqui, o vendedor para o qual o adiantamento será realizado;
- **Valor do Adiantamento:** preencha esse campo com o valor a ser antecipado ao vendedor;
- **Dt. do Crédito:** nesse campo deve ser inserida a data na qual o crédito para o vendedor será realizado, ou seja, a data em que ele irá receber o adiantamento;
- **Dt. do Débito da Prim.Parcela:** esse campo deve ser preenchido com a data de débito da primeira parcela do adiantamento realizado na conta do vendedor;
- **Forma de Desconto:** defina aqui a forma que irá ocorrer o desconto. Nesse campo têm-se as opções **"Descontar do Adiantamento Saldo Flex"** e **"Não descontar"**;
- **Parcelas:** preencha esse campo com a quantidade de parcelas que o valor adiantado será descontado do vendedor;
- **Intervalo de dias:** esse campo deverá ser preenchido com o intervalo de dias entre o desconto das parcelas;
- **Observações:**acrescente aqui alguma observação pertinente ao adiantamento realizado que caracterize a operação e facilite seu entendimento futuro.

#### Gerar Parcelas

Depois de preenchidos os campos acima citados, clique no botão ![botão](https://ajuda.sankhya.com.br/hc/article_attachments/15992392118551) **"Gerar Parcelas"** para que a quantidade de parcelas definidas sejam calculadas.

#### Confirmar

Quando a geração das parcelas for realizada, para que elas sejam gravadas no banco de dados, acione o botão ![botão](https://ajuda.sankhya.com.br/hc/article_attachments/15992525555991) **"Confirmar"**.

#### Cancelar

O botão ![botão](https://ajuda.sankhya.com.br/hc/article_attachments/15992525556759) **"Cancelar"** permite limpar a grade dos adiantamentos e inicializar os campos para inserção do adiantamento. Vale ressaltar que, este botão não remove um adiantamento já inserido no banco de dados.

### Exemplo de aplicação dessa tela

Após acionar o botão Novo, os seguintes dados foram inseridos para configurar o adiantamento de saldo flex:

| **Cód.Vendedor** | 1 – Marcos |
| --- | --- |
| **Valor do Adiantamento** | R$ 300,00 |
| **Dt.Crédito** | 27/01/2018 |
| **Dt.Débito primeira parcela** | 10/02/2018 |
| **Forma de desconto** | Descontar do Adiantamento Saldo Flex |
| **Número de parcelas** | 2 |
| **Intervalo de dias** | 15 |

Dessa forma, será gerado um adiantamento com as sequências:

- 0 - Receita R$ 300,00 27/01/2018 Pendente: Sim
- 1 - Despesa R$ 150,00 10/02/2018 Pendente: Sim
- 2 - Despesa R$ 150,00 25/02/2018 Pendente: Sim

Ou seja, o crédito/receita do adiantamento será gerado na data 27/01/2018 com o valor total do adiantamento R$ 300,00.

Além disso, ao selecionar a opção **"Descontar do Adiantamento Saldo Flex"** do campo **"Forma de Desconto**" e informar duas parcelas no campo **"Parcelas"**, com data inicial do débito em 10/02/2018, foram geradas as sequências 1 e 2.

Todas as sequências do adiantamento estão pendentes. Para liberá-las, é necessário acessar a tela [Atualizar Parcelas Pendentes de Adiantamentos de Saldo Flex](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612254) e escolher a data do adiantamento 27/01/2018, o crédito/receita será liberado e o saldo do vendedor "1", acrescido de R$ 300,00.

Feito isso, novamente na tela Adiantamento de Saldo Flex para Vendedores, a linha referente à receita será apresentada como Pendente igual a "Não", o que irá caracterizar o adiantamento realizado.

---

**![Imagem 9: Informações adicionais referentes à retenção:](https://ajuda.sankhya.com.br/hc/article_attachments/20951939054871) Informações adicionais referentes à retenção:**

- Ao preencher um valor no parâmetro **"Código do vendedor que acumulará o vlrretencao - CODVENDACUVLRRE"**, irá influenciar nas opções **"Forma de Desconto"**, pois será inserida a terceira opção **"Descontar da Retenção"**. O código do vendedor do adiantamento nos débitos/despesas será o código informado no parâmetro.
- Assim, o parâmetro CODVENDACUVLRRE indicará a conta do vendedor que o saldo da retenção será gravado. Esse vendedor receberá os créditos de todas as retenções feitas pelas vendas dos outros vendedores e será considerado como um vendedor curinga, apenas para lançamento desse saldo.
- No lançamento da venda, o campo **"Vlr Retenção"** dos itens da nota na [Central](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110973-Central-Compras-Vendas-Mov-Internas) será preenchido conforme a percentagem informada no parâmetro **"% Retenção do acréscimo - PERCRETENCAO"**.

---

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612434-Adiantamento-de-Saldo-Flex-para-Vendedores#top)

![Imagem 10: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/16970121790103) Acesse também:

[Saldo Flex](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603054)
