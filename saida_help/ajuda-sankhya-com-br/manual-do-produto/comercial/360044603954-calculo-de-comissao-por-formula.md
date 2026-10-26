---
id: "360044603954"
titulo: "Cálculo de Comissão por Fórmula"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603954-C%C3%A1lculo-de-Comiss%C3%A3o-por-F%C3%B3rmula"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:25:03Z"
rotulos: ["manual", "Configuração", "Parceiro", "Fórmulas", "TOP", "Comissão", "Cálculo de Comissão por Fórmula", "CODVENDCALC", "Comissão MúltiplA", "LANCCOMMULT", "Premiações de Campanha", "Tipo de Cálculo", "TRATAPREMIACAO", "br.com.sankhya.com.avancado.calculocomissaoformula", "Cálculo de Comissão por Fórmula manual", "CALCCOMGER", "Vendedores e Gerentes", "Configuração e Execução", "Cálculo de Comissões", "Comercial"]
---

# Cálculo de Comissão por Fórmula

| ``` ![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42311888625175) Módulo: Comercial > Avançado ``` |
| --- |

---

Através desta tela você pode realizar o cálculo das comissões de vendedores e gerentes.

O cálculo é feito para Notas confirmadas que tenham TOP marcada para calcular Comissão e sejam dos tipos **"Venda"**, **"Pedido de Venda"** ou **"Devolução"**. Atualmente não se calcula comissão para Compras, Transferências, Requisições, Produções ou Financeiros. Considerando que este cálculo visa gerar uma despesa no Financeiro, para pagamento ao vendedor, somente são apresentadas Notas de Vendedores que sejam também Parceiros dentro do sistema.

[Configurações Necessárias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603954-C%C3%A1lculo-de-Comiss%C3%A3o-por-F%C3%B3rmula#configura%C3%A7%C3%B5esiniciais)                                                        [Como operar esta tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603954-C%C3%A1lculo-de-Comiss%C3%A3o-por-F%C3%B3rmula#comooperarestatela)

[Premiações de Campanha](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603954-C%C3%A1lculo-de-Comiss%C3%A3o-por-F%C3%B3rmula#premia%C3%A7%C3%B5esdacampanha)

![Imagem 2: Premiações de Campanha](https://ajuda.sankhya.com.br/hc/article_attachments/360077198834)

## Configurações necessárias

Na tela [Vendedores/Compradores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111133-Vendedores-Compradores), informe o campo **"Código"**, que será também o vendedor. Na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111133-Vendedores-Compradores#abageral) desta mesma tela, insira a **"Fórmula Comissão"** que será usada para o cálculo e, no campo **"Pagamento de Comissão por data de"**, defina como esta será paga, se será pela data de negociação ou pela data da baixa.

Após isto, no [Cadastro de Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral), selecione no campo **"Comissão"** a opção **"Calcular"**. É importante ressaltar que, o cálculo das comissões das notas só serão efetivados a partir desta marcação da TOP.

Em seguida, na tela [Fórmulas de Comissão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108013-F%C3%B3rmulas-de-Comiss%C3%A3o) cadastre a fórmula de comissão de acordo com as definições de sua empresa. Esta fórmula é que será informada no Cadastro de Vendedores.

**Observação:** Toda fórmula de comissão é utilizada para cada item da Nota, portanto, não se utiliza o valor total da Nota para fazer cálculos. Considere alguns exemplos:

**1.** Para pagar Comissão de 10%, utilize a fórmula: (queItens.VLRTOT \* 0.1)

Se utilizar (queCab.VLRNOTA \* 0.1) e existirem 5 itens na Nota, então serão pagos 50% de comissão.

Valores totais podem ser utilizados para testes condicionais.

**2.** ((queCab.VLRNOTA \* IF(queTotalVendas.VALOR < 250000,1.5,0.75)) / 100)

Poderão ocorrer casos em que algum valor da nota necessitará ser rateado entre os itens para cálculo da comissão. Nestes casos, podem-se montar expressões para apropriar estes valores aos itens proporcionalmente.

**3.** (queCab.VLRNOTA / queCab.VLRDESTAQUE)

Esta expressão retorna um índice que, multiplicado por qualquer valor, agrega o valor de destaque digitado na Nota a este valor.

**4.** É possível também, configurar fórmulas diferenciadas por vendedores.

Vendedor 7, fórmula 10.

Vendedor 5, fórmula 6.

**Nota:** quando a variável CODVENDCALC for utilizada em uma fórmula de comissão e a nota de venda possuir comissão múltipla (opção Comissão do Financeiro da [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414)), a comissão para o Gerente do Vendedor que utilizar essa fórmula não será calculada.

**Observação:** quando o parâmetro **"Calcular comissão p/ gerente do vendedor - CALCCOMGER"** estiver ligado será calculada a comissão de gerentes.

![Imagem 3: Caso necessite alterar uma fórmula de comissão que já tenha sido calculada e fechada para um vendedor, realize os…](https://ajuda.sankhya.com.br/hc/article_attachments/30995175144855) Caso necessite alterar uma **fórmula de comissão** que já tenha sido calculada e fechada para um vendedor, realize os seguintes passos:

1. estorne os valores de comissão já calculados;
2. altere a fórmula de comissão;
3. recalcule a comissão com base na nova fórmula.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603954-C%C3%A1lculo-de-Comiss%C3%A3o-por-F%C3%B3rmula#top)

## Como operar esta tela

Inicialmente, realize a busca pelo documento que servirá como base para cálculo da comissão, informando seu **"Número único"**.

Em seguida, em **"Período"**, defina como será a apresentação dos dados, se por data de **"Negociação"**, **"Movimento"** ou **"Faturamento"**; feito isso, estabeleça uma data inicial e final, que servirá como base para busca dos documentos que terão sua comissão calculada.

No campo **"Vendedor"** informe o Vendedor para o qual a comissão será calculada.

O campo **"Empresa do Vendedor"**deve ser preenchido com a empresa do vendedor da nota. Este campo é apresentado com a descrição **"Vend/Comp"**, quando a tela é visualizada em modo grade.

Temos no campo **"Aplicar fórmula a"** os aspectos aos quais a fórmula será aplicada. Defina dentre as seguintes opções:

- **Configuração da TOP:** Esta opção irá respeitar a configuração realizada no campo **"Kit/Componentes - Impressão e Livro Fiscal"** presente na tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [Impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpresso).
- **Kit:** Irá considerar os itens da nota para realizar o cálculo da comissão, apenas os produtos que são **"kit's"**; não considerando os produtos que são componentes.
- **Componentes:** De forma contrária a opção anterior, esta alternativa irá considerar os itens da nota para realizar o cálculo da comissão apenas os produtos que são **componentes**; não considerando os produtos que são kit's.
- **Kit e Componentes:** Irá considerar ambos para o cálculo da comissão, ou seja, produtos que são kit's ou componentes farão parte do resultado. Neste caso, se na fórmula não existir, um filtro para um tipo de produto especificar o cálculo da comissão, poderá ser dobrado.

![informações](https://ajuda.sankhya.com.br/hc/article_attachments/16033143436951)   **Atenção Consultor Sankhya:**   Se na fórmula de comissão estiver configurado para não considerar os componentes, ou seja, **"usoprod <> D"**, pode ser que venha zerado o valor da comissão.

Depois de definidos os filtros, escolha no campo **"Calcular para"** para quais comissionados serão efetuados os cálculos:

- Vendedor da nota;
- Vendedor do parceiro;
- Assessor do parceiro;
- Vendedor do item
- Executante do item
- Vendedor da Comissão Múltipla;
- Vend. do centro de resultado.

Comissões para **"Vendedor do item"** e **"Executante do item"** devem ser calculadas separadamente das outras.

Comissões para **"Vendedor da Comissão Múltipla"** também devem ser calculadas separadamente das outras. Esta opção ficará visível quando o parâmetro **"Lançar Comissão p/Múltiplos Vendedores? - LANCCOMMULT"** estiver ligado. Ao escolher essa opção, o sistema irá apresentar as notas com seus respectivos múltiplos vendedores e os  campos **"Valor Comissão"** e **"Comissão"**, que serão apresentados de acordo com as informações inseridas no rodapé da nota.

**Observação:** para visualizar o valor da comissão calculada por fórmula, dê um duplo clique na linha da nota após o cálculo ou recálculo da comissão desejada.

**Nota:** O filtro rápido de pesquisa do vendedor irá buscar sempre o vendedor cadastrado no campo **"Vendedor"** no cabeçalho da nota. Com uma única exceção, quando efetuada a marcação **"Vendedor da Comissão Múltipla"**, o sistema utilizará os vendedores cadastrados na aba [Comissões](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#abacomisses) presente na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) no rodapé da nota.

Em **"Outros"**, temos mais duas opções de marcação que irão influenciar no cálculo da comissão. São elas:

Efetuando a marcação **"Calcular para comprador?"**, ao calcular a comissão, esta será considerada também para as pessoas configuradas como **"Compradores"**.

Quando a marcação **"Zerar comissão no recálculo"** estiver selecionada, o sistema verifica na tabela interna do sistema se existe comissão do vendedor; se não existir nenhuma comissão para o vendedor, será zerada a comissão do vendedor na nota de venda.

Para visualizar as notas de devoluções que possuam valor negativo, basta que você realize a marcação **"Exibir Devoluções com sinal negativo?"**.

Depois de definidos os filtros, clique no botão **"Aplicar"** para que os documentos que terão suas comissões calculadas, sejam apresentados na grade.

O botão **"Calcular comissão"** realiza o cálculo das comissões referentes aos documentos que estão na grade.

Caso seja necessário, o botão **"Recalcular comissão"** irá refazer o cálculo, porém, se essa Comissão já tiver gerado um financeiro, os dados não serão limpos.

Há a possibilidade de gerar relatórios rápidos com os dados da grade, clicando no botão **"Impressão do Grid"**.

**Observação:** Os valores dos campos **"% Comissão"** e **"Vlr. Comissão"** representarão a comissão Total da Nota, ou seja, quando houver mais de um vendedor participante da comissão, o valor nestes campos representará o que será dividido por eles de acordo com a configuração de comissão de cada um.

**Nota:** Não se deve agrupar pedidos (venda/compra) quando utilizar este tipo de comissão, pois, suas informações não serão copiadas para a Nota de Destino.

Notas que totalizem zero na resolução da fórmula, não são alteradas. Portanto, o cálculo da comissão nunca zera valores de Comissões das Notas.

Se uma nota escolhida para cálculo possuir valor de Comissão e o resultado da fórmula for zero, o valor que estava na nota permanecerá inalterado e a Nota não será registrada na tabela de comissões interna do sistema. Esta rotina cria nesta tabela uma linha para cada Nota/Vendedor com o seu valor correspondente. Nota/vendedor que já estejam nesta tabela não são calculadas.

Caso seja necessário, o botão **"Recalcular comissão"** exclui as linhas da tabela interna do sistema que não foram pagas aos vendedores e, depois, chama a mesma função do botão **"Calcular comissão"**. Esta opção não zera o valor de comissão das notas que estão na tela.

**Observação:** A tabela interna do sistema é gerada por vendedor, mas não por tipo **"Calcular para"**, portanto, se houver necessidade de se recalcular comissões, todas deverão ser recalculadas. Com isto, também se evita que, após a alteração em uma nota, corra-se o risco de recalcular para um tipo e esqueça-se de recalcular para outro.

Para cada **"nota"**, a comissão de todos os vendedores e gerentes, marcados nas opções do Calcular para, será calculada e seus resultados serão somados para registrar o total no campo Comissão da Nota.

Se marcar uma opção do Calcular para de cada vez, para calcular em etapas, o campo Comissão da Nota permanecerá correto.

Se em uma das etapas você utilizar o botão **"Recalcular comissão"**, com a opção **"Zerar Comissão no recálculo"** em **"Outros"** marcada, o Total da Nota ficará errado, visto ter sido zerado um total intermediário.

Considere o seguinte exemplo, a empresa calcula Comissão para o vendedor da Nota e para o vendedor do Parceiro. O usuário resolve calcular em duas etapas.

A nota está com um total de Comissão igual a zero.

Na primeira, para o vendedor do Parceiro, o cálculo resulta em R$10,00 (dez reais) de Comissão. Após o cálculo, a nota fica com um total de R$10,00 (dez reais).

Na segunda, para o vendedor da Nota, o cálculo resulta em R$15,00 (quinze reais) de Comissão. Após o cálculo, a Nota fica com um total de R$25,00 (vinte e cinco reais).

**Procedimento errado:**

A Nota está com um total de Comissão igual a zero.

Na primeira, para o vendedor do Parceiro, o cálculo resulta em R$10,00 (dez reais) de Comissão. Após o cálculo, a Nota fica com um total de R$10,00 (dez reais).

Clique no botão **"Recalcular comissão"** com a opção **"Zerar Comissão no Recalculo"**. A Nota ficará com um total de Comissão igual a zero.

Na segunda, para o vendedor da Nota, o cálculo resulta em R$15,00 (quinze reais) de Comissão. Após o cálculo, a Nota fica com um total de R$15,00 (quinze reais).

**Outro procedimento errado:**

A Nota está com um total de Comissão igual a zero.

Na primeira, para o vendedor do Parceiro, o cálculo resulta em R$10,00 (dez reais) de Comissão. Após o cálculo, a Nota fica com um total de R$10,00 (dez reais).

Na segunda, para o vendedor da Nota, o cálculo resulta em R$15,00 (quinze reais) de Comissão. Após o cálculo, a Nota fica com um total de R$25,00 (vinte e cinco reais).

Na terceira, para o vendedor da Nota, clique no botão Recalcular comissão com a opção **"Zerar Comissão da Nota no Recalculo"** desmarcada. O cálculo resulta em R$15,00 (quinze reais) de Comissão. Após o cálculo, a Nota fica com um total de R$40,00 (quarenta reais).

Certas empresas promovem campanhas comerciais para incentivar as vendas, gerando para seus vendedores uma premiação especial, fora a comissão de venda. Além do cálculo das comissões, o sistema fará o cálculo destas premiações especiais. Tendo assim, comissões e premiações sendo calculadas sobre o mesmo fato gerador.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603954-C%C3%A1lculo-de-Comiss%C3%A3o-por-F%C3%B3rmula#top)

## Premiações de Campanha

O parâmetro **"Habilita tratamento de premiações por campanha? - TRATAPREMIACAO"**, habilitará a opção Fórmulas de premiações para o cálculo de comissões de premiação.

**Observação:** Ainda referente ao parâmetro acima, considere:

- Se ambos os parâmetros TRATAPREMIACAO e **"Usar Fechamento de comissão conforme cad. vendedor - FECHCOMVEN"** forem desligados, o tipo de integração no fechamento de comissão a ser utilizado será conforme o campo **"Gerar comissão para"** da tela [Fechamento de Comissão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607034-Fechamento-de-Comiss%C3%A3o);
- Porém, quando apenas o parâmetro TRATAPREMIACAO for habilitado, o tipo de integração a ser utilizado será o do campo **"Tipo de Integração"** localizado na aba [Integração](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108013-F%C3%B3rmulas-de-Comiss%C3%A3o#abaintegrao) da tela [Fórmulas de Comissão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108013-F%C3%B3rmulas-de-Comiss%C3%A3o);
- Por fim, com o parâmetro FECHCOMVEN acionado, o sistema utilizará a informação do campo **"Tipo de fechamento de comissão"** da tela [Cadastro de Vendedores/Compradores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111133-Vendedores-Compradores#abageral).

Neste caso, informe aqui a fórmula de premiação a ser usada.

Ao pressionar o botão **"Calcular comissão"** desta tela, o sistema calculará as fórmulas de comissão/premiação que estejam marcadas em Fórmulas de premiações, e que também estejam vinculadas ao vendedor.

Na grade desta tela são apresentadas as linhas das notas com os percentuais e valores de comissão acumulados.

**Nota:** Na tabela de comissões (TGFCOM), o campo CODFORM exibirá o código da fórmula. No cálculo das Comissões/Premiações será gerada uma linha para cada fórmula calculada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603954-C%C3%A1lculo-de-Comiss%C3%A3o-por-F%C3%B3rmula#top)

Acesse também:

[Fechamento de Comissão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607034-Fechamento-de-Comiss%C3%A3o).

Entidade Centro de Resultado para **"Cálculo de comissão por OS"**, **"Cálculo de Comissão por Fórmula"**, **"Comissão de Terceiros"** e **"Fechamento de Comissão"** no help da tela [Central de Certificações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110053-Central-de-Certifica%C3%A7%C3%B5es).
