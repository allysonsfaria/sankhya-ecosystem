---
id: "360044607034"
titulo: "Fechamento de Comissão"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607034-Fechamento-de-Comiss%C3%A3o"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-10-13T19:37:10Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Parceiro", "Movimentação Financeira", "Premiação", "Comissão", "Financeiro", "Cálculo de Comissão", "Fechamento de Comissão", "br.com.sankhya.fin.cad.fechamentocomissao", "Fechamento de Comissão manual", "Define regras e filtros para comissão incluindo renegociações e premiações", "Fechamento Comissão: Calcula e gera títulos/folha conforme fórmula", "Configura integração com financeiro/folha e ajustes para descontos e taxas."]
---

# Fechamento de Comissão

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312391561367) Módulo: Financeiro > Rotinas
```

---

A tela de Fechamento de Comissão encerra o processo de pagamento de comissões a vendedores. A partir da tela **"Cálculo de Comissão por Fórmula"**, as comissões são calculadas, e através do **"Fechamento de Comissão"** são gerados ou os títulos financeiros (contas a pagar) ou eventos da folha de pagamento para o vendedor.

O cálculo também depende da configuração de cada vendedor. Cada vendedor é configurado para ter sua comissão calculada a partir da data de negociação da venda, ou a partir da data da baixa do financeiro da nota.

A fórmula para o cálculo deverá ser definida na tela [Fórmulas de Comissão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108013-F%C3%B3rmulas-de-Comiss%C3%A3o) e pode ser construída conforme a política da empresa. Sendo assim, por padrão, o cálculo da comissão é feito sobre o valor do desdobramento, ou seja, sobre o valor bruto não considerando as despesas que incidem sobre a operação, como, por exemplo, os impostos.

Quando a comissão é calculada a partir da data de negociação, o pagamento da comissão (Financeiro/Folha de Pgto.) é gerado para o valor de comissão calculado para o vendedor.

No caso do vendedor ter sua comissão calculada pela data da baixa, o processo é semelhante, porém, a comissão (Financeiro/Folha de Pgto.) é gerada proporcionalmente ao recebimento da venda. Por exemplo, se uma venda é negociada em 3 parcelas, e apenas a 1ª foi paga, apenas 1/3 da comissão é gerada.

Um caso especial do cálculo pela baixa envolve renegociações. Nesse caso, o sistema calcula a parcela de cada etapa da renegociação e gera uma nova linha na tabela de cálculo de comissão para cada etapa, gravando apropriadamente o número do financeiro de origem para cada uma delas.

Nesta tela as opções marcadas são salvas possibilitando o usuário sair da tela e entrar novamente e as opções estarem salvas.

**Observação:** só serão apresentados nesta tela os registros de comissão pertinentes ao vendedor que possua em seu cadastro um Parceiro informado.

**Nota:** não é possível realizar comparações de valores/registros entre esta tela e a tela de [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874) quando a empresa trabalhar com renegociações que agrupam títulos, visto que, durante a renegociação é possível utilizar títulos do financeiro que pertencem a vendedores diferentes.

**Observação:** quando ocorrer o fechamento de múltiplos vendedores, o sistema exibirá na grade de múltiplos vendedores, várias linhas que ao serem somadas irão gerar um determinado valor. E ao gerar financeiro, cada vendedor terá um financeiro diferente e estes poderão ser arredondados individualmente, de forma que, ao serem somados, o valor gerado não será exatamente o valor a ser exibido no rodapé da tela. Considere o exemplo:

Vendedor 1: Comissão Total: 33,6565
Vendedor 2: Comissao Total: 33,6565
Vendedor 3: Comissao Total: 33,6565

Total rodapé: 100,97 (ou seja, 100,9695 arredondado)

**Observação:** o **"Total rodapé"** é referente a soma da coluna **"Comissão Parc. Líq"**.

**Importante:**apesar do cálculo total do fechamento ser realizado considerando as quatro casas decimais, o arredondamento para duas casas decimais acontece para que o valor apresentado no Fechamento de Comissão seja o mesmo valor que irá surgir no Valor de Desdobramento do título financeiro que, por padrão, aceita apenas duas casas decimais para prevenir divergências de valores que poderiam ocorrer sem esse arredondamento.

**Nota:** quando você realizar a exclusão do financeiro da comissão gerado a partir dessa tela, para que todos os títulos sejam exibidos novamente no Fechamento de comissão após o recálculo, é preciso realizar todo o processo de comissão novamente, ou seja, realizar o cálculo de comissão, em seguida o fechamento desta, para posteriormente, efetuar a geração do financeiro.

Ao considerar o exibido acima, teremos os seguintes tópicos referente à tela Fechamento de Comissão:

[Painel de Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607034-Fechamento-de-Comiss%C3%A3o#paineldefiltros)                                             [Botão Ao Gerar integração (Fin./Folha de Pgto.)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607034-Fechamento-de-Comiss%C3%A3o#bot%C3%A3oaogerarintegra%C3%A7%C3%A3o(fin./folhadepgto.))

[Integração MGE/Jiva Pessoal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607034-Fechamento-de-Comiss%C3%A3o#integra%C3%A7%C3%A3omge/jivapessoal)                    [Botão Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607034-Fechamento-de-Comiss%C3%A3o#bot%C3%A3ooutrasop%C3%A7%C3%B5es...)

[Premiações de Campanha](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607034-Fechamento-de-Comiss%C3%A3o#premia%C3%A7%C3%B5esdecampanha)                          [Devoluções de Cheques](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607034-Fechamento-de-Comiss%C3%A3o#devolu%C3%A7%C3%B5esdecheques)

[Cálculo de Renegociações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607034-Fechamento-de-Comiss%C3%A3o#c%C3%A1lculoderenegocia%C3%A7%C3%B5es)                         [Parâmetros que influenciam a Rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607034-Fechamento-de-Comiss%C3%A3o#par%C3%A2metrosqueinfluenciamarotina)

![Imagem 2: Cálculo de Renegociações Parâmetros que influenciam a Rotina](https://ajuda.sankhya.com.br/hc/article_attachments/360082228814)

## Painel de Filtros

Será necessário definir as regras de geração de comissão e essas devem ser através do filtro. Você sempre deverá filtrar por data da baixa os lançamentos na tela de Fechamento de Comissão. Os títulos apresentados na tela terão suas Comissões fechadas proporcionalmente ao valor dos títulos escolhidos, então se uma Nota possuir dois financeiros e apenas um deles for fechado, a Comissão da Nota será paga apenas referente ao título escolhido, permanecendo o outro em aberto.

No cálculo da Comissão o sistema usa o valor do desdobramento para gerar o valor da Comissão, pois não considera juros ou descontos financeiros.

Para não agrupar comissões de empresas diferentes, filtre as empresas pelo campo do filtro Empresa. Para Despesa no Financeiro usamos o Parceiro que estiver informado no cadastro de vendedores, para a Folha, usamos o Código do Funcionário. Desta forma, no Painel de Filtros, tem-se os seguintes campos:

O campo **"Comissionado"** é usado para filtrar vendedor, se ficar em branco, aparecerão todos os comissionados de acordo com o filtro informado.

Em **"Empresa do Comissionado"**, o sistema irá filtrar pela empresa do vendedor.

Utilize a **"Empresa"** para filtrar os registros.

A **"Data Neg."** será utilizado para filtrar data de negociação da despesa gerada ou data de referência da folha de pagamento.

O campo **"Gerar comissão para"** indicará se a comissão será gerada para **"Financeiro"** ou **"Folha de pagamento".**

**Observação:** ao habilitar o parâmetro **"Habilita tratamento de premiações por campanha? - TRATAPREMIACAO"**, o sistema irá exibir a aba [Integração](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108013-F%C3%B3rmulas-de-Comiss%C3%A3o#abaintegrao) da tela [Fórmulas de Comissão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108013-F%C3%B3rmulas-de-Comiss%C3%A3o) e utilizará a configuração do campo **"Tipo de Integração"** dessa mesma aba para realizar o tipo de integração que será usado no fechamento de comissões. Porém, quando desligado, o sistema buscará a configuração do parâmetro **"Usar Fechamento de comissão conforme cad. vendedor - FECHCOMVEN"**, sendo que ele utilizará o campo **"Tipo de fechamento de comissão"** da aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111133-Vendedores-Compradores#abageral) da tela [Vendedores/Compradores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111133-Vendedores-Compradores) para realizar o fechamento, mas ao usar esse parâmetro, o sistema fecha a comissão sem gerar o Financeiro e nem Folha de pagamento.

O **"Financeiro"** indicará se ela será calculada para pagamento pelo financeiro.

Na opção **"Folha"** será calculada para pagamento na folha de pagamento do vendedor.

Se marcada a opção **"Considerar Valor do Desconto"** e na baixa do Financeiro tiver ocorrido um desconto, o percentual relativo ao desconto será aplicado sobre a Comissão devida e será lançado um desconto de comissão. Sendo assim, considere o exemplo:

Tendo-se R$10,00 (dez reais) de Comissão, na hora de receber do cliente o financeiro precisou conceder 5% de desconto. O vendedor perderá R$0,50 (cinquenta centavos) da comissão, que corresponde a 5% da comissão devida.

**Observação:** quando o parâmetro **"Usa comissão negativa no fechamento de comissão? - USACOMISSAONEG"** estiver habilitado juntamente com a marcação Considerar Valor do Desconto acionada, os descontos inseridos nas baixas dos títulos serão considerados para comissões com valores negativos originados de uma venda.

Quando a opção **"Considerar Taxa de Cartões"** for marcada, é descontada proporcionalmente da comissão do vendedor a taxa do cartão informada na baixa do financeiro da nota no campo **"Taxa Administrativa"**. Considere o exemplo:

Uma nota de R$ 1.000,00 paga comissão de R$ 50,00, mas o financeiro é baixado com taxa de cartão de R$ 100,00. Nesse caso, são descontados R$ 5,00 de baixa e pago R$ 45,00 de comissão.

O campo **"Tratar Desconto/Taxa na Devolução"** será habilitado apenas quando as opções **"Considerar Valor do Desconto"** ou **"Considerar Taxa de Cartões"** forem selecionadas. Nesse caso, o tratamento de desconto e/ou taxa do cartão é aplicado também em comissões originadas em notas de devolução.

**Nota:** o comportamento das duas últimas opções somente pode ser observado em comissões pagas pela baixa da nota, e não pela negociação.

O processo para gerar comissão é:

0 - Cadastrar vendedor, fórmula de comissão, configurar TOP de venda para calcular comissão

1 - Lançar nota de venda

2 - Baixar o financeiro da nota

3 - Calcular comissão pela tela "Cálculo de Comissão por Fórmula"

4 - Gerar o financeiro/folha de pgto. da comissão na tela "Fechamento de Comissão".

Se a opção **"Tratar renegociações"** estiver desmarcada o sistema não vai considerar as renegociações no cálculo de comissão, vai buscar apenas os títulos com rec/desp=1.

Se estiver marcado, o sistema vai fazer também uma busca nos títulos renegociados. Assim, teremos o exemplo:

No mês de agosto foi gerado uma receita de 100,00 através de uma venda com o vendedor código 5. Estes 100,00 foram renegociados em dois títulos no valor de 50,00 cada sendo um com o vencimento em Setembro e outro com vencimento em Outubro, o titulo de 50,00 do mês de setembro o cliente pagou e foi efetuada a baixa deste. Para que este título apareça na tela de fechamento de comissão a opção de Tratar Renegociação tem que estar marcada.

Ao selecionar a marcação **"Descartar cálculos intermediário de renegociação"**, fará com que as renegociações sejam recalculadas a cada consulta.

**Observação:** para saber mais sobre a aplicabilidade do campo acima, acesse o tópico [Cálculo de Renegociações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607034-Fechamento-de-Comiss%C3%A3o#c%C3%A1lculoderenegocia%C3%A7%C3%B5es).

A marcação do campo **"Lançar rescisão complementar para demitidos?"** possibilita ao usuário efetuar geração de rescisão complementar para pagamentos de comissão para funcionários que não fazem mais parte do quadro de colaboradores da empresa.

Caso esta opção não esteja marcada o sistema não gerará lançamentos para funcionários que já foram demitidos.

Para que essa opção seja habilitada é necessário que Comissão seja por Folha de Pagamento.

![Imagem 3: Para que essa opção seja habilitada é necessário que Comissão seja por Folha de Pagamento.](https://ajuda.sankhya.com.br/hc/article_attachments/360082232074)

#### Configurações necessárias:

- O campo **"Tipo de Integração"**  (tela [Fórmulas de Comissão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108013), aba **"Integração"**) deverá ser por **"Folha"**.
- No cadastro do Vendedor realizado em [Vendedores/Compradores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603034), preencha os campos **"Fórmula Comissão"** e **"Funcionário"**.
- A situação do funcionário (Tela **"Funcionário"**, aba **"Afastamento"**, campo **"Situação"**) deve constar como demitido.
- Voltando à tela de fechamento de comissão, e marque a opção **"Lançar Rescisão Comp. p/ Demitidos?"**.
- Se marcado, o sistema irá gerar a comissão na folha de pagamento se o funcionário for demitido será gerado um movimento de rescisão complementar, caso o funcionário não seja demitido será gerado um movimento mensal.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607034-Fechamento-de-Comiss%C3%A3o#a)

## Botão Ao Gerar Integração (Fin./Folha de Pgto.)

**Importante:** caso você tenha migrado do Jiva Evo para o Sankhya Om, não possua a licença **"JIVA-CENTRO DE RESULTADOS/W"** e não utilize Centro de Resultado, ao abrir a tela de Preferências para os campos Centro de Resultado e Projetos, informe o número 0 pois esses campos são obrigatórios no Sankhya Om.

Se ficar definido que a comissão será gerada para o Financeiro, o campo **"Histórico da Movimentação Financeira"** apresentará o nome da fórmula.

Se a comissão for gerada para a Folha o sistema utilizará o Evento definido na fórmula, se este estiver preenchido, senão, será usado o Evento que estiver informado na janela de Preferências desta rotina.

Cálculo de comissão para Títulos Renegociados, utilizando o seguinte critério:

Parceiro 10 com vendedor 5

Parceiro 10 com vendedor 7

Se os títulos tiverem sido renegociados com 2 ou 3 parcelas diferentes, e se apenas uma parcela tiver sido paga, será calculado o valor da Comissão de 1/3 para cada vendedor.

Ao clicar em Gerar Interação (Fin/Folha de Pgto) será aberta a janela de Preferências.

o pop up **"Preferências"** trata da configuração das informações do Financeiro ou da Folha de Pagamento. Configuram-se aqui os campos Financeiros tais como: Natureza, TOP, Tipo de Título, etc.

![Imagem 4: o pop up "Preferências" trata da configuração das informações do Financeiro ou da Folha de Pagamento. Configuram-se…](https://ajuda.sankhya.com.br/hc/article_attachments/360082233714)

**Conta bancária:** Conta corrente correspondente ao débito da despesa que será gerada. Se não for informada usaremos a conta do parâmetro **"Número da conta padrão na baixa -CONTAPADRAO"**.

**Banco:** Código do banco em que será efetuado o pagamento do título.

**Tipo de título:** Tipo de título utilizado no pagamento posterior.

**Tipo de operação:** Tipo de Operação, que deve gerar despesa no financeiro.

**Histórico:** qualquer informação adicional sobre a geração da comissão.

**Evento:** Evento para lançamento na Folha de Pagamento.

**Natureza:** Natureza da operação.

**Centro de resultado:** Código do Centro de Resultados para que seja direcionada a despesa.

**Importante:** para o Jiva Evo, a empresa deve possuir o opcional **"JIVA-CENTRO DE RESULTADOS /W"**habilitado.

**Projeto:** Código do projeto, caso haja.

**Empresa:** O programa gera para APENAS uma empresa.

**Dt. Venc.\Ref.:** Para a opção gerar integração(financeiro), é a data do vencimento para pagamento da comissão.

Para a opção gerar integração(Folha), é a data de referencia da folha de pagamento que será incluída a comissão.

Esta tela o permitirá que, você realize a seleção de um ou vários títulos entre todos os visualizados, permite a exclusão dos que não gerarão seus financeiros, ou seja, dos que não serão pagos naquele momento.

Quando for selecionada uma linha da tabela para a Exclusão, todas as outras linhas referentes à mesma Nota também serão excluídas para aquele comissionado.

Depois de listados, se tiver algum lançamento onde não se deseja gerar o Financeiro, selecione-o com CRTL+ Clique com mouse e depois escolha a opção de **"Remover selecionados"**.

O botão **"Remover NÃO selecionados"** excluirá da tela os que não estiverem marcados.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607034-Fechamento-de-Comiss%C3%A3o#a)

## Integração MGE/JIVA Pessoal

#### Lançamentos> Movimentação Rescisão Complementar

**Importante:** caso a fórmula de comissão seja alterada (criando-se um novo registro no cadastro de fórmula e alterando-se no [Cadastro de Vendedores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111133) o código da fórmula utilizada), porém a realização do cálculo de comissão por fórmula já tenha ocorrido e os registros pertinentes à fórmula antiga ainda não tenham sido fechados, ao proceder com o fechamento de comissão, serão gerados dois financeiros, sendo um correspondente à configuração antiga da fórmula, e outro à alteração feita. Portanto, é essencial atentar-se para o momento do processo da empresa em que são realizadas modificações nas fórmulas de comissão.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607034-Fechamento-de-Comiss%C3%A3o#a)

## Botão Outras Opções...

- **Remover nota(s):** Exclui da grade todas as notas com o mesmo numero da nota selecionada.
- **Remover vendedor(es):** Exclui da grade todas as notas com o mesmo código do vendedor selecionado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607034-Fechamento-de-Comiss%C3%A3o#a)

## Premiações de Campanha

Certas empresas promovem campanhas comerciais para incentivar as vendas, gerando para seus vendedores uma premiação especial, fora a comissão de venda. As comissões e premiações serão calculadas sobre o mesmo fato gerador. Para isto deve-se habilitar o parâmetro **"Habilita tratamento de premiações por campanha? - TRATAPREMIACAO"**.

As comissões calculadas na tela Cálculo de Comissão por Fórmula são efetivamente geradas nesta rotina, através do botão **"Gerar Interação (Fin/Folha de Pgto.)"**.

A definição de se gerar a comissão para o Financeiro ou para a Folha já foi feita na aba Integração da tela Fórmulas de Comissão.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607034-Fechamento-de-Comiss%C3%A3o#a)

## Devoluções de cheques

Quando for devolvido um cheque de receita que deu origem à Comissão, o sistema gerará um Financeiro negativo com o valor da Comissão para anular o título de pagamento da comissão, além de gerar outro título pendente para o pagamento da comissão em outra data.

Renegociação de títulos e pagamento com vários títulos no cálculo e fechamento de comissão

Quando um título for Renegociado, o sistema rateará os valores das comissões proporcionalmente aos valores de cada novo título gerado.

Para desfazer uma renegociação, não poderá haver nenhuma comissão paga para nenhum dos títulos renegociados.

O sistema não permite parcelar pela movimentação financeira e nem formar duplicatas com títulos que tenham Comissão com origem no Financeiro.

Ao fazer uma baixa parcial, o sistema alterará proporcionalmente o valor das Comissões na tabela TGFCOM. O mesmo acontece quando o usuário faz pagamento com vários títulos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607034-Fechamento-de-Comiss%C3%A3o#a)

## Cálculo de Renegociações

O cálculo de renegociações pode afetar drasticamente o desempenho da tela. Isso se deve ao fato de que um título pode ser renegociado diversas vezes, de forma que cadeias de renegociações muito longas podem ser formadas.

Quando um título que é resultado de uma renegociação é baixado, o sistema precisa calcular o peso desse título na cadeia de renegociações até o título original, ou seja, o sistema calcula exatamente a parcela do título original que foi paga para que o valor de comissão seja calculado corretamente. Então, esse cálculo é armazenado em uma tabela temporária no banco de dados, de forma que consultas subsequentes à cadeia de renegociações são otimizadas, representando ganhos significativos de desempenho.

Essa abordagem representa uma desvantagem, que é a possibilidade das cadeias de renegociações estarem desatualizadas, neste caso, a opção **"Descartar cálculos intermediários de renegociação"** deve ser marcada para que o cálculo seja refeito.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607034-Fechamento-de-Comiss%C3%A3o#a)

## Parâmetros que influenciam a rotina

O parâmetro **"Apres VlrBaixa negat Devol Venda Fecham. Comissão - FECHCOMDVVLRNEG"** terá os seguintes comportamentos:

- **Ligado:** Quando o campo **"Tipo de movimento"** for **"Devolução de Venda"**, na tela de Fechamento de Comissão será alterado o sinal de positivo para negativo do campo **"Vlr. Baixa"**.
- **Desligado:** Quando o campo Tipo de movimento for Devolução de Venda, na tela Fechamento de Comissão será alterado o sinal de negativo para positivo do campo Vlr. Baixa.

Parâmetro **"Tipos de negociação p/ ajuste - AJUSTECOMIS"** quando o lógico estiver marcado, o inteiro representará o prazo máximo entre a negociação e o recebimento para não alterar a Comissão. Acima deste prazo o número representará o percentual de comissão a ser pago para o vendedor. O texto conterá os tipos de negociação sujeitos a estas regras. Dessa forma, temos o exemplo:

A empresa paga 10% de comissão para todas as vendas recebidas com menos de 30 dias e 3% para as vendas recebidas com mais de 30 dias.

Na fórmula de comissão, calcula-se 10%, já que não se sabe, se o cliente pagará em dia ou não.

Na hora de gerar o Financeiro, checa-se a data de recebimento com a data de negociação e para os títulos que superaram 30 dias, das notas de alguns tipos de negociação que foram escolhidos, calcula-se 3% de comissão e gera um lançamento de desconto de comissão de 7%.

Para lançar comissão para mais de um vendedor, o parâmetro **"Lançar Comissão p/Múltiplos Vendedores? - LANCCOMMULT"**, deve ser habilitado.

Na tela Comercial> Configuração> Configurador de layout da nota na aba Comissão de vendedores, deve-se selecionar os campos **"Vendedor"** e **"% de Comissão"**.

Para esta funcionalidade operar corretamente, deve-se ter uma fórmula de comissão cadastrada, e no cadastro do vendedor, selecionar esta fórmula.

Quando se utiliza comissão múltipla, o valor que é informado no campo % Comissão é utilizado como uma variável que será adicionada na fórmula de comissão.

**Nota:** não se deve Agrupar Pedidos (venda / compra) quando utilizar este tipo de comissão, pois, suas informações não serão copiadas para a "Nota de Destino".

Quando o parâmetro **"Usar Fechamento de comissão conforme cad. Vendedor - FECHCOMVEN"**, estiver ligado: o fechamento da comissão e geração do crédito, executados através de **"Financeiro>Rotinas>Fechamento de comissão"**, passará a funcionar de acordo com o indicado no campo **"Tipo de fechamento de comissão:"** da tela Configurações>Cadastros> Vendedores/Compradores>aba Geral’. A opção 'Gerar comissão para:' fica invisível na tela e o título do botão que executa o fechamento de comissão muda para 'Gerar comissão'.

São três as opções que o usuário poderá escolher para gerar a comissão: Nenhuma, Financeiro e Folha de Pagamento. Ao acessar a tela **"Financeiro> Rotinas> Fechamento de comissão"** o sistema apresenta a opção de filtros e o botão **"Gerar comissão"** que gera a comissão de acordo com a opção selecionada no campo Tipo de fechamento de comissão da tela Cadastro de Vendedores/Compradores, sendo elas:

**Nenhuma** - Não será gerado nem financeiro e nem evento de folha de pagamento;

**Financeiro** – Será gerado movimento no financeiro;

**Folha de pagamento** – Será gerado evento em folha de pagamento.

Leia os tópicos: Entidade Centro de Resultado para 'Cálculo de comissão por OS', 'Cálculo de Comissão por Fórmula', ‘Comissão de Terceiros’ e 'Fechamento de Comissão' no artigo da tela: [Central de Certificações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110053).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607034-Fechamento-de-Comiss%C3%A3o#a)
