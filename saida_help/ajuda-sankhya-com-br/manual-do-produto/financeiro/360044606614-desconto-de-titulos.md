---
id: "360044606614"
titulo: "Desconto de Títulos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606614-Desconto-de-T%C3%ADtulos"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-07-29T14:40:18Z"
rotulos: ["Configuração", "Despesa", "Parceiro", "Rateio", "Movimentação Financeira", "Centro de Resultado", "Juros", "Critério de Rateio", "Desconto de Títulos", "Histórico do Financeiro", "Juro Composto", "Juro Simples", "Taxa de Juros", "Taxa Diária", "br.com.sankhya.mgefin.desconto.titulos", "Desconto de Títulos manual", "Título", "Recebimento", "Desconto", "Financeiro", "Pagamento", "Baixa", "Natureza", "Receita", "Desconto de Títulos: Operação financeira", "Configurações e Preferências: Ajustes necessários", "Funcionalidades da Rotina: Procedimentos detalhados", "DATATUALDESC"]
---

# Desconto de Títulos

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312335363479) Módulo: Financeiro > Rotinas
```

---

A rotina de Desconto de Títulos possibilita o cálculo de descontos de títulos de receita com vencimento futuro para obtenção de recursos Financeiros à vista, pagando uma taxa de juros pela operação.

![Imagem 2: Com o parâmetro "Considerar "Data atual" como data de baixa de títulos d - DATATUALDESC" ligado, o sistema irá utilizar…](https://ajuda.sankhya.com.br/hc/article_attachments/27324469247127) Com o parâmetro **"Considerar "Data atual" como data de baixa de títulos d - DATATUALDESC"** ligado, o sistema irá utilizar a data atual para realização da baixa futura do título, desconsiderando a data de vencimento do mesmo.

Acesse os links abaixo para conhecer as funcionalidades desta tela:

[Filtros personalizados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606614-Desconto-de-T%C3%ADtulos#filtrospersonalizados)                                        [Dados da baixa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606614-Desconto-de-T%C3%ADtulos#dadosdabaixa)

[Receitas/Despesas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606614-Desconto-de-T%C3%ADtulos#receitasdespesas)                                            [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606614-Desconto-de-T%C3%ADtulos#preferncias)

[Trabalhando na rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606614-Desconto-de-T%C3%ADtulos#trabalhandonarotina)                                        [Botões no topo da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606614-Desconto-de-T%C3%ADtulos#botesnotopodatela)

![Imagem 3: Trabalhando na rotina Botões no topo da tela](https://ajuda.sankhya.com.br/hc/article_attachments/8734744795927)

## Filtros personalizados

![Imagem 4: Filtros personalizados](https://ajuda.sankhya.com.br/hc/article_attachments/8734831552535)

Os resultados apresentados ao preencher o campo **"Data do desconto"** serão exibidos na grade principal da tela (Resultados), apenas os títulos com data de vencimento maior que a data de desconto informada neste campo.

Se você selecionar a marcação **"Considerar desconto do financeiro"**, o sistema também buscará os títulos que possuem desconto no financeiro. Destacamos ainda que os títulos que possuem desconto no financeiro precisam ter sido liberados pelo evento [29 - Desconto no Financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601034-Libera%C3%A7%C3%A3o-de-Limites#29-descontonofinanceiro); só assim o valor do desconto será visualizado na grade. O sistema só reconhecerá o desconto aplicado no financeiro caso este já tenha sido aprovado.

Com o desconto do financeiro liberado e o título selecionado na tela, devem ser informe os valores de **"Taxa de Desc. por título"** e **"Taxa de Desc. da Operação"** (presentes no quadrante Dados da Baixa); a soma destes dois campos será o valor de desconto total a ser aplicado. Assim, teremos o exemplo:

Suponhamos o lançamento de um título de R$100,00 com desconto de R$ 90,00, nesta tela é apresentado o título com valor de desdobramento de R$90,00; informa-se R$ 5,00 para cada campo Taxa de Desc. por título e Taxa de Desc. da Operação; então, será descontado R$10,00 do valor do desdobramento. Clicando-se no botão Efetuar Desconto o título será baixado com valor da baixa igual a R$90,00 e será criado um novo título de despesa no valor de R$10,00 que é o valor descontado da receita que foi baixada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606614-Desconto-de-T%C3%ADtulos#top)

## Dados da baixa

![Imagem 5: Dados da baixa](https://ajuda.sankhya.com.br/hc/article_attachments/8734873912727)

Se a marcação **"Baixa separada"** for realizada, uma movimentação bancária para cada receita e despesa da operação será gerada.

Informe na **"Empresa da baixa"**, aquela empresa que será utilizada nos títulos de despesa gerados nas operações de desconto de títulos.

A conta bancária cadastrada no campo **"Código da conta"** será utilizada na baixa dos títulos de despesa gerados nas operações de desconto de títulos.

Em **"Documento"**, insira o código do documento em que será gravado no campo Núm. Documento da documento da movimentação bancária gerada, seguindo a regra:

- Ao informar algo diferente de "0" no campo Documento, será utilizado este valor;
- Caso não seja preenchido, ou seja informado "0", o sistema irá verificar se a opção Preferir 'Nosso Número' para o campo documento está assinalada (presente no botão Outras Opções...), se estiver e o nosso numero não for vazio, será utilizado o campo nosso número do financeiro;
- Caso o Nosso Número esteja vazio ou a opção citada não esteja marcada, o sistema verifica se o título possui número de duplicata diferente de zero; se possuir, usa o mesmo; do contrário, utiliza o número da nota.

Os dados inseridos no campo **"Histórico"**, serão gravados no campo Histórico da Movimentação Bancária juntamente com um complemento respeitando a regra:

- Caso a marcação **"Usar histórico do financeiro"** localizada no botão Outras Opções... esteja efetuada (só pode ser marcada no caso de Baixa Separada), e o financeiro utilizado possuir histórico o sistema utilizará o mesmo como complemento;
- Caso a marcação não esteja realizada, mas o parâmetro **"Apresentar nome ou Razão social do Parceiro? - NOMERAZAOPARC"** esteja ligado, o sistema utilizará a Razão Social do parceiro referente ao título que está sendo descontado;
- Não sendo atendidas as duas condições citadas, será utilizado o nome do parceiro referente ao título que está sendo descontado.

**Taxa de desconto por título:** Tem-se neste campo, o valor que será utilizado no momento da geração da despesa para cada título descontado; informando-se um valor de R$10,00 e descontar 10 títulos por exemplo, tem-se R$100,00 em despesa.

Em **"Taxa de desconto por título"** teremos valor que será utilizado ao gerar a despesa da operação, lembrando que essa taxa é para operação, ou seja, sendo informado um valor de R$100,00, esse será o valor da despesa independente se forem descontados 1 ou 20 títulos.

**Importante:** o sistema gera uma despesa com a soma da taxa de desconto da operação e taxa de desconto por título, por exemplo, sendo descontados 2 títulos e a taxa de desconto por título é R$10,00, e a taxa de desconto da operação é R$ 20,00, será gerado um título de despesa de R$ 40,00.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606614-Desconto-de-T%C3%ADtulos#top)

## Receitas/Despesas

![Imagem 6: Receitas/Despesas](https://ajuda.sankhya.com.br/hc/article_attachments/8734957142935)

**Baixa das receitas:**

A informação inserida no **"Lançamento"** será gravada na movimentação bancária gerada por meio dos títulos das receitas utilizadas para efetuar o desconto.

No campo **"TOP da baixa"** informe a TOP que será utilizada na baixa de receitas e também será gravada na movimentação financeiros do(s) título(s) de receita utilizados para efetuar o desconto, e na movimentação bancária gerada através do mesmo.

**Baixa dos juros e taxas:**

Em **"Lançamento"** será gravado na movimentação bancária que foi gerada por meio das despesas da operação.

Insira em **"TOP da baixa"** a TOP utilizada para baixa dos juros e taxas e que será gravada na movimentação financeira do(s) título(s) de despesa gerados através da operação e na movimentação bancária do mesmo.

O sistema irá usar TOPs de pagamento na baixa dos juros e de recebimento na baixa de receitas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606614-Desconto-de-T%C3%ADtulos#top)

## Preferências

![Imagem 7: Preferências](https://ajuda.sankhya.com.br/hc/article_attachments/8734995867799)

Informe em **"Parceiro"** para o qual será gerada a despesa dos jutos calculados para o desconto.

Teremos no **"Título"**, o referido título que será utilizado na despesa gerada.

Informe também a **"Natureza"** será usada para a despesa gerada.

Insira o **"Centro de Resultado"** que será utilizado para a despesa.

Teremos em **"Taxa de juros diária"**, a taxa para o cálculo do desconto. 

Caso existam outras taxas de juros para serem calculadas, adicione no campo **"Outra taxa diária"** a somatória delas.

A marcação **"Rateio"** determina se o título de despesa gerado será ou não rateado.

Definindo-se por Rateio, informe o **"Critério"** que será utilizado para rateio do título. Os critérios são previamente cadastrados na tela [Critérios de Rateio](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606574). 

Ao fazer o desconto do título, o novo título de despesa gerado com o valor dos juros e será aberto o pop-up **"Rateando o título XX"** para realização do rateio de acordo com o critério escolhido. Neste procedimento será possível dividir o custo do desconto em diversas naturezas, para analisar, por exemplo, valor de IOF, juros e outras taxas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606614-Desconto-de-T%C3%ADtulos#top)

## Trabalhando na rotina

Para que os Títulos do Financeiro sejam apresentados na grade principal, deve-se atentar para as seguintes regras:

- O título não pode estar baixado;
- Não pode ser uma Provisão;
- A moeda do título deve ser a moeda corrente, ou seja, o Real;
- Os valores de Multa, de Juros, de Despesa com Cartório, do Vendedor e de impostos como IRF, INSS, ISS e Taxa Administradora, não poderão existir. Caso exista, por exemplo, o valor de R$0,01 informado para apenas um destes campos, o título não será exibido na tela. Logo, qualquer valor diferente de "0" (zero) para qualquer um dos dados descritos anteriormente, ocultará o título financeiro nesta rotina;
- Os títulos que tiverem o campo Valor de Desconto preenchidos, só serão apresentados se a marcação **"Considerar desconto do financeiro"** estiver efetuada (quadrante Filtros personalizados), caso contrário, os valores de Desconto não serão apresentados na tela.

Uma vez estas regras satisfeitas, pode-se trabalhar por meio dos passos abaixo:

![Imagem 8: Nos Filtros personalizados , Dados da baixa , Receitas/Despesas e Preferências , alguns campos são de preenchimento…](https://ajuda.sankhya.com.br/hc/article_attachments/16243959976087) Nos [Filtros personalizados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606614-Desconto-de-T%C3%ADtulos#filtrospersonalizados), [Dados da baixa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606614-Desconto-de-T%C3%ADtulos#dadosdabaixa), [Receitas/Despesas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606614-Desconto-de-T%C3%ADtulos#receitasdespesas) e [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606614-Desconto-de-T%C3%ADtulos#preferncias), alguns campos são de preenchimento obrigatório (assinalados com um asterisco '\*') para posterior apresentação dos dados na grade de Resultados;

![Imagem 9: Depois de configurados os filtros desejados, o sistema apresenta apenas títulos com data de vencimento maior que a Data…](https://ajuda.sankhya.com.br/hc/article_attachments/16243965993623) Depois de configurados os filtros desejados, o sistema apresenta apenas títulos com data de vencimento maior que a Data do Desconto informada no quadrante Filtros Personalizados;

![Imagem 10: Clique no botão "Aplicar" para visualização dos títulos filtrados. Através dos botões "Remover itens selecionados" e…](https://ajuda.sankhya.com.br/hc/article_attachments/16243965994647) Clique no botão **"Aplicar"** para visualização dos títulos filtrados. Através dos botões **"Remover itens selecionados"** e **"Remover itens não selecionados"** pode-se retirar os títulos que não forem sofrer descontos;

![Imagem 11: Utiliza-se do quadrante de filtros "Preferências" para configuração das opções para o cálculo;](https://ajuda.sankhya.com.br/hc/article_attachments/16243959984407) Utiliza-se do quadrante de filtros **"Preferências"** para configuração das opções para o cálculo;

![Imagem 12: Clique no botão "Calcular Juros" para que sejam aferidos os juros dos títulos selecionados;](https://ajuda.sankhya.com.br/hc/article_attachments/16243965998743) Clique no botão **"Calcular Juros"** para que sejam aferidos os juros dos títulos selecionados;

![Imagem 13: Realiza-se as devidas verificações dos valores de juros;](https://ajuda.sankhya.com.br/hc/article_attachments/16243966000791) Realiza-se as devidas verificações dos valores de juros;

![Imagem 14: Caso seja necessário que as informações sejam gravadas no Financeiro, clica-se no botão "Efetuar Desconto" ; ou pode-se…](https://ajuda.sankhya.com.br/hc/article_attachments/16243959990551) Caso seja necessário que as informações sejam gravadas no Financeiro, clica-se no botão **"Efetuar Desconto"**; ou pode-se somente visualizar os valores, bastando sair da tela sem gravar as informações.

**Nota:** a despesa gerada com o valor do juro será baixada automaticamente e com data da baixa do dia; as receitas também serão baixadas automaticamente utilizando a data do vencimento como data da baixa, para evitar que se conclua que o cliente pagou antecipado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606614-Desconto-de-T%C3%ADtulos#top)

## Botões no topo da tela

![Imagem 15: - Remover itens selecionados e Remover itens não selecionados - Estes botões são responsáveis por manter ou retirar da…](https://ajuda.sankhya.com.br/hc/article_attachments/16242791421847)![Imagem 16: - Remover itens selecionados e Remover itens não selecionados - Estes botões são responsáveis por manter ou retirar da…](https://ajuda.sankhya.com.br/hc/article_attachments/16242814455191)- Remover itens selecionados e Remover itens não selecionados - Estes botões são responsáveis por manter ou retirar da grade Resultado os títulos que vão ou não sofrer descontos. Para utilizá-los, basta selecionar as linhas desejadas, mantendo-se pressionado no teclado o botão Ctrl; em seguida, clica-se em um dos botões para manter na grade os títulos que serão trabalhados.

![Imagem 17: - O acionamento do botão "Calcular Juros" implica no cálculo dos juros dos títulos selecionados.](https://ajuda.sankhya.com.br/hc/article_attachments/16243402320023) - O acionamento do botão **"Calcular Juros"** implica no cálculo dos juros dos títulos selecionados.

![Imagem 18: - O botão "Ajustar Juros" a justa o valor real dos juros cobrados pelo banco para descontar os títulos. Depois de…](https://ajuda.sankhya.com.br/hc/article_attachments/16243884282135) - O botão **"Ajustar Juros"** ajusta o valor real dos juros cobrados pelo banco para descontar os títulos. Depois de digitá-lo, deve-se clicar neste botão para que o sistema insira o valor dos juros para os respectivos títulos.

![Imagem 19: - O botão "Efetuar desconto" é utilizado caso seja necessário que as informações trabalhadas na rotina sejam gravadas…](https://ajuda.sankhya.com.br/hc/article_attachments/16243865602583) - O botão **"Efetuar desconto"** é utilizado caso seja necessário que as informações trabalhadas na rotina sejam gravadas no Financeiro.

![Imagem 20: - O botão Outras Opções... possui as seguintes funcionalidades:](https://ajuda.sankhya.com.br/hc/article_attachments/16242814458775) - O botão Outras Opções... possui as seguintes funcionalidades:

- **Usar histórico do financeiro:** Se houver histórico no financeiro do título que está sendo descontado, o mesmo será concatenado junto ao histórico informado na tela e será inserido na movimentação bancária gerada pela operação.
- **Preferir 'Nosso Número' para o campo documento:** Se o campo Documento localizado no quadrante Dados da baixa não for informado e o título possuir Nosso Número, este último será inserido na movimentação bancária gerada pela operação.
- **Baixar quando valor líquido igual a zero:** Se esta opção estiver assinalada, o filtro passa a trazer os títulos que tenham valor líquido igual a zero, ou seja, se um título possui valor de desdobramento de R$ 50,00 e um desconto de R$ 50,00, ele só irá aparecer caso essa opção esteja marcada, já que o valor de desdobramento subtraído do valor do desconto foi R$ 0,00.
- **Taxa de juros simples:** Por padrão, esta rotina trabalha com a taxa de juros composta; se esta opção estiver assinalada passa a considerar taxa de juros simples.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606614-Desconto-de-T%C3%ADtulos#top)
