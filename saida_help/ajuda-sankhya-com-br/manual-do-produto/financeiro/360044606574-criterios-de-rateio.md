---
id: "360044606574"
titulo: "Critérios de Rateio"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606574-Crit%C3%A9rios-de-Rateio"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-07-29T19:38:26Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Despesa", "Rateio", "Projeto", "Centro de Resultado", "Relatórios Gerenciais", "Financeiro", "Natureza", "Análise Gerencial", "Critérios de Rateio", "Receita", "br.com.sankhya.fin.cad.criteriosrateio", "Critérios de Rateio manual", "Visualização resultados gráficos", "Divisão despesas receitas", "Critérios rateio automáticos"]
---

# Critérios de Rateio

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312349869463) Módulo: Financeiro > Avançado
```

---

O rateio consiste na divisão de **"Receitas"** e **"Despesas"** por determinadas **"Naturezas"** e/ou **"Centros de Resultado"**(este último apenas se JIVA-CENTRO DE RESULTADOS /W estiver habilitado), para futuras análises gerenciais dos resultados da empresa. Assim, teremos os seguintes tópicos referente à esta tela:

[Considerações Iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606574-Crit%C3%A9rios-de-Rateio#considera%C3%A7%C3%B5esiniciais)                                                                      [Aba Manutenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606574-Crit%C3%A9rios-de-Rateio#abamanuten%C3%A7%C3%A3o)

[Aba Resultado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606574-Crit%C3%A9rios-de-Rateio#abaresultado)

## Considerações Iniciais

No sistema cadastram-se os Critérios de Rateio, que são fórmulas nas quais o administrador da empresa define a divisão das Despesas e Receitas da Empresa, pré-definindo as formas de rateio para apenas aplicá-los aos títulos.

Este cadastro torna o rateio mais fácil, pois, não haverá a necessidade de ter que digitar todos os dados do rateio a cada rateio de um mesmo tipo de ocorrência (rec/ desp), pois estes já estarão pré-definidos. Vejamos um exemplo:

Uma empresa de informática poderá definir como critério para ratear as despesas com energia elétrica entre os setores, por exemplo, o número de computadores em cada um, por ser o ativo mais representativo neste tipo de gasto. Assim, cadastra os percentuais que serão alocados em cada área na tela de Critérios de Rateio para posterior utilização no rateio da despesa.

                                         ![Imagem 2: Uma empresa de informática poderá definir como critério para ratear as despesas com energia elétrica entre os setores,…](https://ajuda.sankhya.com.br/hc/article_attachments/8534974611351)

Sendo o critério para rateio de despesas com energia elétrica o número de computadores, teremos:

![Imagem 3: Sendo o critério para rateio de despesas com energia elétrica o número de computadores, teremos:](https://ajuda.sankhya.com.br/hc/article_attachments/8534725217687)

Quando for lançada a despesa de energia e rateá-la utilizando este critério, será possível visualizar nos relatórios gerenciais quanto cada setor está consumindo do total. Lembrando que este é apenas um exemplo genérico para facilitar o entendimento de como funcionam os critérios de rateio.

**Observação:** nos casos em que o Critério de Rateio utilizar apenas um Centro de Resultado (100%), ao faturar um pedido para nota de venda, através da ativação do parâmetro **"Aceitar rateio de uma linha (100%) - ACEITARATUNICO"** o sistema copia o rateio deste pedido para a nota de venda. Mantendo-se o parâmetro desligado (forma como ele é apresentado), o sistema não copia o rateio.

Para cadastrar um rateio, preencha as informações abaixo:

![Imagem 4: Para cadastrar um rateio, preencha as informações abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/8535449132823)

Informe o **"Código"** para o critério.

A **"Descrição"** identificará o critério.

Através da marcação **"Automático"** defina se o critério é ou não automático. Se estiver marcada, habilitará os campos **"Natureza"**, **"Centro de Resultado"** e **"Projeto"** no cabeçalho do cadastro do Critério. Quando o critério é automático e for lançada uma nota que tenha o mesmo trio Natureza, Centro Resultado e Projeto definido no cabeçalho do Cadastro de Critérios, nos relatórios gerenciais os títulos serão apresentados já rateados, da maneira como foi definida no critério.

**Importante:** o critério automático possibilita análises gerenciais sem a necessidade de se aplicar os critérios a cada nota/título. Contudo, a marcação **"Automático"** é utilizada apenas nos **"Relatórios Gerenciais"**, de modo que o sistema irá considerar o critério que possui esta marcação realizada. Ao efetuar essa marcação, não será feito o rateio automático do financeiro, quando informar-se a natureza que está no critério.

Informe também o código da **"Natureza"** das Receitas e/ou Despesas que utilizarão o critério para rateio.

Insira o **"Centro de Resultado"** para o qual serão alocadas as Receitas/Despesas.

**Nota:** lembrando que este campo estará disponível apenas se o opcional JIVA-CENTRO DE RESULTADOS /W estiver habilitado.

Deve-se informar o **"Projeto"** para alocar as Receitas/Despesas, caso a empresa utilize.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606574-Crit%C3%A9rios-de-Rateio#top)

## Aba Manutenção

![Imagem 5: Aba Manutenção](https://ajuda.sankhya.com.br/hc/article_attachments/8535449132823)

No campo **"% Rateio"** informe o percentual que será alocado para o trio Natureza/Centro de Resultado/Projeto, quando for utilizado o critério em questão.

Caso a contabilização seja feita pelo rateio, e cada linha do rateio possua contas contábeis diferentes, deve-se informar o campo **"Conta Contábil"** em cada linha do critério.

**Observação:** na Pesquisa da Conta Contábil, quando o campo de Pesquisa for igual à Conta Contábil, será necessária a digitação do ponto entre os números da conta para efetuar a pesquisa. Exemplo: 2.1.1. Isto porque poderá haver planos de contas de várias empresas e cada um com uma máscara.

O campo **"Site"** é de uso específico de um Parceiro Sankhya.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606574-Crit%C3%A9rios-de-Rateio#top) 

## Aba Resultado

![Imagem 6: Aba Resultado](https://ajuda.sankhya.com.br/hc/article_attachments/8535706250775)

Nesta aba, você poderá visualizar o resultado do rateio por **"Natureza"**, **"Centro de Resultado"** e **"Projeto"** de forma gráfica.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606574-Crit%C3%A9rios-de-Rateio#top)
