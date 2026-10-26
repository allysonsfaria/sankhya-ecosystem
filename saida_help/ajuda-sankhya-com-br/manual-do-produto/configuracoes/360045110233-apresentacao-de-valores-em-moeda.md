---
id: "360045110233"
titulo: "Apresentação de Valores em Moeda"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110233-Apresenta%C3%A7%C3%A3o-de-Valores-em-Moeda"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:56:34Z"
rotulos: ["AJUDA DO SKW", "Configuração", "Cotação", "Moeda", "Movimentação Financeira", "Apresentação de Valores em Moeda", "Apresentação de Valores em Moeda manual", "Baixa de Títulos", "Financeiro", "MOSTRAVLRMOEDA"]
---

# Apresentação de Valores em Moeda

Para que você possa verificar nas rotinas de [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira) e [Baixa de títulos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600534-Movimenta%C3%A7%C3%A3o-Financeira-Baixa-de-T%C3%ADtulos) os valores de moedas estrangeiras convertidos na moeda atual, o parâmetro **"Mostrar valores de moedas convertido no financeiro - MOSTRAVLRMOEDA"** necessita estar habilitado.

### Movimentação Financeira

Na tela de Movimentação Financeira ao gerar um novo titulo que tenha moeda informada, será exibido um pop-up com as Informações de Moeda correspondente àquele título. Este pop-up também é aberto no momento da informação da moeda ou através do botão **"Outras Opções"**, opção **"Visualizar dados em Moeda"**:

![Imagem 1: Na tela de Movimentação Financeira ao gerar um novo titulo que tenha moeda informada, será exibido um pop-up com as…](https://ajuda.sankhya.com.br/hc/article_attachments/360101568994)

No exemplo, o valor do título é de 100,00 e o valor da moeda de 5,39 informada na movimentação financeira e na cotação com data atual, no caso, 17/02 o valor da moeda é de 5,37.

Então, o Valor no Título equivale às informações do título e o Valor atual equivale à cotação atual.

Nesta janela, temos as seguintes informações:

**Valor no Título:** Equivale as informações do título, como o valor da moeda e o código da moeda.

**Moeda:** Se refere ao valor da moeda informada no título, normalmente é o valor proveniente da negociação.

**Desdobramento em moeda:** É a conversão do título de reais para a moeda informada no título. Exemplo: 100,00 convertidos para Dólar no valor da moeda de 5,39, resultam em 18,55 dólares.

**Valor Atual:** Equivale a informações da cotação atual do código da moeda informada no título.

**Moeda:** Se refere ao valor da moeda da cotação atual, informada na tela [Valores de Moedas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604754).

**Desdobramento em moeda:** É a conversão do título de reais para a moeda informada no título utilizando o valor da moeda na cotação atual. Exemplo: 100,00 convertidos para Dólar no valor da moeda de 5,37, resultam em 18,62 dólares.

**Observações:**

- Se o título não tiver código de moeda informado, os valores do pop-up ficarão zerados e a opção Visualizar dados em Moeda do botão Outras Opções, será desabilitado.
- Se o valor da moeda do título alterar, ao confirmar a alteração, o sistema refaz os cálculos.
- Se a tela estiver aberta e você realizar movimentações entre os títulos, o sistema irá trazer os valores provenientes destes.

### Botão Baixar

Ao baixar um título que tenha moeda e tenha o parâmetro habilitado, será exibida uma nova aba na tela de baixa com o nome **"Fechamento Baixa em Moeda"**.

![Imagem 2: Ao baixar um título que tenha moeda e tenha o parâmetro habilitado, será exibida uma nova aba na tela de baixa com o…](https://ajuda.sankhya.com.br/hc/article_attachments/360103725773)

**Nota:** a aba Fechamento Baixa em Moeda só estará habilitada se o título que tiver sendo baixado tiver sido lançado com "Moeda" estrangeira.

**Observação:** será permitido que os Valores de Moeda e Valor Total na baixa sejam alterados na baixa de moeda, desde que no [Cadastro do Usuário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios), aba [Segurança](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abasegurana), a opção **"Permite alterar valor de moeda na baixa?"** esteja habilitada.

#### Aba Fechamento Baixa em Moeda

![Imagem 3: Aba Fechamento Baixa em Moeda](https://ajuda.sankhya.com.br/hc/article_attachments/1500002688722)

Nesta aba,  temos os seguintes dados:

**Vlr Negociação:** Aqui é apresentado, os campos **"Vlr. Moeda"**, **"Vlr. Desdob. "Moeda"** e **"Desdobramento"**, preenchidos com os respectivos valores da data de negociação.

**Vlr Atual:** Apresenta os campos Vlr. Moeda, Vlr. Desdob. Moeda e Desdobramento preenchidos com os respectivos valores na data atual, tendo em mente que se não há cotação na data atual o sistema buscará a última cotação registrada para atualizar os valores.

**Variação Cambial:** Apresenta a variação cambial de Vlr. Moeda e do Desdobramento, variação essa proveniente da atualização de cotação da moeda.

**Vlr Baixa:** Apresenta Vlr. Desdob. Moeda e Desdobramento atualizados após a atualização da moeda.

**Nota:** se no Fechamento da Moeda for informado um valor de moeda que não está cadastrado o sistema emitirá o aviso:

**"Valor não encontrado. Utilize um valor cadastrado na cotação de moeda".**

Caso o usuário possua na tela [Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854), módulo **"Financeiro > Rotinas > Movimentação Financeira"** o acesso **"Digita Cotação"** liberado; o parâmetro **"Mostrar valores de moedas convertido no financeiro - MOSTRAVLRMOEDA"** esteja ativado; e o título possua valores para baixa com tipo de moeda estrangeira, o campo **"Vlr. Atual"** além de ser preenchido pelo modo de pesquisa, será habilitado para edição, na qual pode-se informar um valor de moeda ainda não cadastrado.

**Exemplos:**

Sem variação cambial:

| **Vlr. Título: 1000,00** | **Vlr. Moeda** | **Vlr. Desdob. Moeda** | **Desdobramento** |
| --- | --- | --- | --- |
| Vlr. Negociação: | 1,8100 | 552,49 | 1000,00 |
| Vlr. Atual: | 1,8100 | 552,49 | 1000,00 |
| Variação Cambial: | 0 | 0 | 0 |
| Vlr. Baixa: | 0 | 552,49 | 1000,00 |

Com variação cambial sendo o Vlr. Atual maior que o Vlr. Negociação:

| **Vlr. Título: 100,00** | **Vlr. Moeda** | **Vlr. Desdob. Moeda** | **Desdobramento** |
| --- | --- | --- | --- |
| Vlr. Negociação: | 2,00 | 50,00 | 100,00 |
| Vlr. Atual: | 2,18 | 50,00 | 109,00 |
| Variação Cambial: | 0,18 | 0 | 9,00 |
| Vlr. Baixa: | 0 | 50,00 | 109,00 |

Com variação cambial sendo o Vlr. Atual menor que o Vlr. Negociação:

| **Vlr. Título: 100,00** | **Vlr. Moeda** | **Vlr. Desdob. Moeda** | **Desdobramento** |
| --- | --- | --- | --- |
| Vlr. Negociação: | 2,22 | 45,05 | 100,00 |
| Vlr. Atual: | 1,00 | 49,10 | 49,00 |
| Variação Cambial: | -1,22 | 0 | -50,90 |
| Vlr. Baixa: | 0 | 49,10 | 49,10 |

**Nota:** quando o parâmetro estiver ligado e a baixa do título for parcial o sistema não permite que seja considerado o valor da diferença entre o valor calculado e o valor da baixa como **"Desconto"**:

![Imagem 4: Nota: quando o parâmetro estiver ligado e a baixa do título for parcial o sistema não permite que seja considerado o…](https://ajuda.sankhya.com.br/hc/article_attachments/360101580594)

### Compensação Financeira

Na rotina de Compensação Financeira ao tentar compensar um título que tenha moeda informada, será exibida a seguinte mensagem:

**"Rotina de Compensação não está preparada para compensar títulos em moeda."**
