---
id: "360045115073"
titulo: "Compensação Financeira"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115073-Compensa%C3%A7%C3%A3o-Financeira"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-10-20T14:27:43Z"
rotulos: ["AJUDA DO SKW", "manual", "Parceiro", "Receitas", "Moeda", "Movimentação Financeira", "TIPTITCREDCLI", "Despesas", "Compensação", "Baixa de Títulos", "Código de Barras", "Preferências", "Financeiro", "Linha Digitável", "Nosso Número", "CONSJURMULNEG", "Acerto", "Compensação Financeira", "PERMFILPARCVAZ", "br.com.sankhya.mgefin.mov.compensacaofinanceira", "Compensação Financeira manual", "Cálculo de juros", "Cálculo de Juros e Multas", "Cálculo de multas", "CONTAPADRAOFIN", "Baixa de títulos: Rotina financeira", "Filtros e preferências: Configurações detalhadas", "Compensação financeira: Cálculo de juros e multas"]
---

# Compensação Financeira

```
 Módulo: Financeiro > Rotinas
```

---

Esta rotina realiza a baixa dos títulos de receita e despesa envolvidos, sendo que a sua grade superior contempla as Despesas e a inferior as Receitas. O sistema traz a totalização dos registros no rodapé da grade e os títulos podem ser ordenados em ambas a grades.

[Painel de Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115073-Compensa%C3%A7%C3%A3o-Financeira#paineldefiltros)                                                                 [Botões de Ação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115073-Compensa%C3%A7%C3%A3o-Financeira#bot%C3%B5esdea%C3%A7%C3%A3o)

[Parâmetros que influenciam a rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115073-Compensa%C3%A7%C3%A3o-Financeira#par%C3%A2metrosqueinfluenciamarotina)

![Imagem 1: Parâmetros que influenciam a rotina](https://ajuda.sankhya.com.br/hc/article_attachments/1500002725501)

![Imagem 2: A compensação de títulos que possuem moedas só pode ser realizada envolvendo 1 despesa e 1 receita.](https://ajuda.sankhya.com.br/hc/article_attachments/25496842591895) A compensação de títulos que possuem moedas só pode ser realizada envolvendo 1 despesa e 1 receita.

É possível consultar a [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874) de cada título através de um duplo clique sobre os mesmos, em ambas as grades. Além disto, esta tela possui Filtros Personalizados e Estáticos, Botões de Ação e o botão de **"Preferências"** que contém os parâmetros que podem impactar nos cálculos de juros, multas e descontos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115073-Compensa%C3%A7%C3%A3o-Financeira#top)

## Painel de Filtros

Temos no painel de Filtros os campos que auxiliarão na localização dos títulos, de maneira direcionada, rápida e singular.

![Imagem 3: Temos no painel de Filtros os campos que auxiliarão na localização dos títulos, de maneira direcionada, rápida e…](https://ajuda.sankhya.com.br/hc/article_attachments/1500002725601)

O acionamento do botão ![Imagem 4: O acionamento do botão "Filtro" abre o pop-up "Assistente para a Criação de Filtros" , que permite realizar à…](https://ajuda.sankhya.com.br/hc/article_attachments/16116936501783) **"Filtro"** abre o pop-up **"Assistente para a Criação de Filtros"**, que permite realizar à construção de filtros específicos, visando assim, agilizar e facilitar a busca dos títulos que serão compensados. Como por exemplo, um filtro por número único, empresa, natureza, entre outros.

O campo **"Acerto"** permite que você efetue a busca de acertos de títulos realizados anteriormente.

O botão **"Desfazer"** ficará habilitado quando você selecionar um acerto no campo mencionado acima. Ao acioná-lo, o sistema emitirá uma mensagem questionando se você realmente confirma o estorno. Se a confirmação for realizada, as grades da compensação financeira serão preenchidas com os títulos pertencentes à esta compensação. Se confirmado, o sistema desfaz a compensação e o título volta a ficar como baixado igual a não, ou seja, este botão realiza o estorno de um acerto já realizado.

**Importante:** se o título tiver uma Natureza de Rendimento vinculada à EFD-Reinf, o Sankhya Om exclui automaticamente o respectivo registro da tabela `TGFRNF` ao desfazer a compensação, permitindo a conclusão do processo — desde que esse lançamento ainda não esteja associado a nenhum evento já gerado da EFD-Reinf.

Através do botão **"Limpar"**, efetue a retirada do acerto que estava no filtro, deixando o campo em branco.

Ao habilitar a marcação **"Somente Títulos com Moeda"**, serão filtrados na tela apenas os títulos com moedas.

Além disto, é possível que você filtre os títulos levando em consideração o **"Parceiro matriz"**, o **"Parceiro"**, o **"Nro. da nota"** e o seu **"Período de vencimento"**.

**Observação:** quando o parâmetro **"Permite parceiro vazio no filtro da compensação financeira-PERMFILPARCVAZ"** estiver desligado, os filtros **"Parceiro Matriz"** e **"Parceiro"** devem ser configurados. Quando ligado, mesmo que os campos Parceiro ou Parceiro Matriz não sejam preenchidos, será possível realizar a busca de títulos pelos filtros da tela.

No momento da compensação, quando houverem títulos vencidos que possuam descontos, será utilizado o valor de índice abaixo para o cálculo:

```
 Valor do indice = vlrRef(valor despesa).divide(VlrTotal(valor liquido da receita))
```

Depois, todos os campos abaixo são submetidos ao índice:

- VLRDESC
- VLRJURO
- VLRMULTA
- VLRVENDOR
- VLRIRF
- VLRISS
- VLRINSS
- VLRPROV
- BASEICMS
- DESPCART
- CARTAODESC
- VLRMULTANEGOC
- VLRJURONEGOC
- VLRVARCAMBIAL
- VLRMULTAEMBUT
- VLRJUROEMBUT

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115073-Compensa%C3%A7%C3%A3o-Financeira#top) 

## Botões de Ação

| [Botão Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115073-Compensa%C3%A7%C3%A3o-Financeira#bot%C3%A3oprefer%C3%AAncias) | [Botão Cal. Juros/Multas/Descontos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115073-Compensa%C3%A7%C3%A3o-Financeira#bot%C3%A3ocalc.juros/multas/descontos) |
| --- | --- |
| [Botão Acertar](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115073-Compensa%C3%A7%C3%A3o-Financeira#bot%C3%A3oacertar) |  |

![Imagem 5: Botão Acertar](https://ajuda.sankhya.com.br/hc/article_attachments/360101569854)

## Botão Preferências

O botão **"Preferências"** permite que você informe a quantidade de dias de carência para o cálculo de Juros, Percentual da multa, Percentual de juro por dia de atraso, Percentual de desconto por dia de antecipação e cálculo de juros (simples e composto). Ao acionar esta opção, será aberta uma tela que possibilitará a configuração das preferências. Esta tela é separada por duas abas Receitas e Despesas que possuem os mesmos campos, porém, definimos os cálculos desejados para cada operação separadamente.

![Imagem 6: O b otão "Preferências" permite que você informe a quantidade de dias de carência para o cálculo de Juros, Percentual…](https://ajuda.sankhya.com.br/hc/article_attachments/1500002688082)

Informe no campo **"Dias de carência para o cálculo de juros"**, a quantidade de dias que serão considerados como carência para que o cálculo de juros não seja considerado.

**Seção Antes do vencimento**

- Acionar a marcação **"Zerar Juros?"** fará com que os juros sejam zerados antes do vencimento.
- Efetuar a marcação **"Zerar Multa?"** fará com que os valores de multa sejam zerados antes do vencimento.
- Com a marcação **"Manter Descontos?"** acionada, os descontos calculados no título antes do vencimento serão mantidos. **É importante notar que, em casos de baixa parcial, o valor do desconto será proporcionalizado.**
- O percentual informado no campo **"Percentual de desconto por dia de antecipação"** será considerado a cada dia de antecipação para cálculo de desconto.

**Seção No vencimento**

- Com a marcação **"Zerar Juros?"** habilitada, os juros serão zerados no vencimento do título.
- Ao efetuar a marcação **"Zerar Multa?"**, os valores de multa serão zerados no vencimento.
- Ao acionar a marcação **"Manter Descontos?"**, os descontos calculados no título no vencimento serão mantidos. **Assim como antes do vencimento, em baixas parciais, o sistema irá proporcionalizar o valor do desconto.**

**Seção Até X dias após o vencimento**

- Com a marcação **"Zerar Juros?"**, os juros serão zerados até X dias após o vencimento do título.
- Acionando a marcação **"Zerar Multa?"**, os valores de multa serão zerados até X dias após o vencimento.
- Se você efetuar a marcação **"Zerar Descontos?"**, fará com que os descontos calculados no título até X dias após o vencimento sejam mantidos.

**Seção Após X dias do vencimento**

Por meio da marcação **"Recalcular Juros?"** você define se os juros serão recalculados após X dias do vencimento do título.

Caso você habilite a marcação **"Recalcular Multa?"**, as multas serão recalculadas após X dias do vencimento do título.

Efetuando a marcação **"Zerar Descontos?"**, os descontos serão zerados após X dias do vencimento do título.

O **"Cálculo de Juro"** poderá ser Simples ou Composto. Caso não deseje calcular os juros, é necessário informar valores iguais a zero nas **"Preferências"**.

No campo **"Percentual da multa"** informe o percentual que será considerado como multa pelo atraso.

O percentual informado no campo **"Percentual de juro por dia de atraso"** refere-se ao juro por dia de atraso.

**Notas:**

1. Quando algum título estiver sem a data de vencimento, o sistema irá interromper o cálculo e lançará uma mensagem notificando que não é possível calcular juros/multas/descontos, pois o título não possui data de vencimento.
2. Caso a marcação Manter Descontos, mencionada acima esteja desabilitada, ao realizar uma compensação financeira de títulos que possuam desconto, o sistema gerará um novo título com valor do desconto separado da baixa realizada. Após a realização do acerto, a tela será recarregada com a informação desse desconto separado do título original.
3. Após a realização do acerto, a tela será recarregada exibindo os títulos envolvidos no acerto e caso exista uma diferença no valor dos títulos compensados o novo título criado pelo sistema com o valor pendente também será exibido. Todos os títulos atrasados selecionados terão juros e multas calculados de acordo com os campos informados nas Preferências.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115073-Compensa%C3%A7%C3%A3o-Financeira#top) [[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115073-Compensa%C3%A7%C3%A3o-Financeira#bot%C3%B5esdea%C3%A7%C3%A3o)

## Botão Calc. Juros/Multas/Descontos

Quando você utilizar o botão Calc. Juros/Multas/Descontos, o sistema realizará o cálculo dos títulos selecionados nas grades de despesa e receita. Esses cálculos serão executados conforme os dados informados na seção Preferências, e os resultados exibidos nos totalizadores do rodapé da tela.

**Observação:** ao ligar o parâmetro **"Cons. Juro/Multa para compor Vlr.Liq Comp. Fin.? - CONSJMVLRLIQCOM"**, o valor base para o cálculo dos juros será o valor líquido do título, assim, após o primeiro cálculo, os juros sobre os juros serão considerados e por esse motivo, a cada cálculo o valor será maior. Com o parâmetro desligado, o sistema não utilizará o **"Vlr Juro"** e o **"Vlr Multa"** na base do valor no cálculo do juros e multa na tela, dessa forma, não serão calculados os juros e os valores de compensação serão respeitados.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115073-Compensa%C3%A7%C3%A3o-Financeira#top) [[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115073-Compensa%C3%A7%C3%A3o-Financeira#bot%C3%B5esdea%C3%A7%C3%A3o)

## Botão Acertar

Ao acionar o botão **"Acertar"**, teremos o cálculo de juros, multas e descontos. Em seguida, será aberta uma janela para que você informe os **"Tipos de Operação – TOP's"** de Despesas e Receitas, a **"Data da Baixa"** e o **"Valor do Acerto"**.

[GIF animado: Imagem 7: Ao acionar o botão "Acertar" , teremos o cálculo de juros, multas e descontos. Em seguida, será aberta uma janela para…](https://ajuda.sankhya.com.br/hc/article_attachments/360103725673)

**Observações:**

1. Só será possível informar a data da baixa se o parâmetro **"Digitar data da baixa na Compensação Financeira? - DIGDTBAIXACF"** estiver habilitado. Caso contrário, o sistema realizará o acerto com a data atual.
2. Ao realizar um acerto, o valor do campo **"Valor Acerto"** não poderá ser maior que o total das Despesas ou o total das Receitas.

Quando a compensação for parcial, teremos a criação de um novo título para executar a compensação (valor da compensação) e o título atual fica travado com o valor pendente. Lembrando que, caso a compensação do financeiro baixado possua outros impostos, se o valor estiver abaixo do mínimo não será apresentado o imposto da parcela da pendência.

Após a realização do acerto, a tela será recarregada exibindo os títulos envolvidos no acerto e, caso exista uma diferença no valor dos títulos compensados, o sistema criará um novo título com o valor pendente, esse novo título será exibido.

**Nota:** o sistema realiza algumas consultas para efetuar a baixa. Se uma opção não se aplica, ele avança para a próxima, seguindo esta ordem:

1. Verifica se há uma conta vinculada ao usuário logado;
2. Avalia se o parâmetro **"Conta padrão para financeiro - CONTAPADRAOFIN"** está preenchido com uma conta válida;
3. Confirma se na aba [Cadastros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas#abacadastros) existe uma [Conta](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas#top) configurada como **"Exclusiva da empresa"** e com o campo **"Empresa"** informado com a empresa correspondente ao título.

Assim, é possível utilizar o botão **"Desfazer"** para realizar o estorno do acerto que foi realizado.

**Nota:** na realização da Compensação Financeira, quando o título original for rateado, os campos **"Nosso Número"**, **"Código de Barras"** e **"Linha Digitável"** referentes a este título serão limpos e será exibida a seguinte mensagem:

**"Existem boletos selecionados para compensação. As informações de Código de Barras, Nosso Número e Linha Digitável serão apagadas de modo irreversível caso o valor de desdobramento do título seja alterado na compensação. Deseja continuar?".**

**Observação:** para os casos em que se fizer necessário o reajuste de boletos, ou seja, seus dados forem recalculados, este procedimento irá ocorrer se as seguintes condições forem atendidas:

- Deve ser um título de **"Receita"**;
- O campo **"NOSSONUM"** deve estar preenchido;
- A **"LINHADIGITAVEL"** deve também estar preenchida;
- O **"CODIGOBARRA"** deve estar informado;
- A conta bancária ([Cadastro de Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas), aba [Boleto(s)/Duplicatas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas#ababoletosduplicatas)) deve estar com o campo **"Emite"** marcado.

**Importante:** a compensação financeira de parceiros que possuem a marcação **"Bloquear venda a prazo"** da aba [Crédito](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abacrdito) (tela [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros)) habilitada, será realizada somente se o parâmetro **"Pode compensar finan. parc. bloq. p/ venda a prazo - COMPENSPARCBLOQ"** estiver ligado.

As informações dos campos **"Data Cotação"** e **"Vlr. Moeda Atual"** poderão ser alteradas se o usuário logado tiver a marcação **"Permite alterar valor de moeda na baixa?"** (tela [Cadastros de Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874), aba [Segurança](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abasegurana)) habilitada.

A seção **"Detalhamento"** exibirá os detalhes de Receitas e Despesas referente à moeda do título que você irá acertar.

**Observação:** se houver mais de um título a ser acertado, eles deverão conter o mesmo código de **"Moeda"** ao utilizar o botão Acertar.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115073-Compensa%C3%A7%C3%A3o-Financeira#top) [[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115073-Compensa%C3%A7%C3%A3o-Financeira#bot%C3%B5esdea%C3%A7%C3%A3o)

## Parâmetros que influenciam a rotina

**Permite parceiro vazio no filtro da compensação financeira -  PERMFILPARCVAZ:** quando este parâmetro estiver desligado, o sistema não permitirá que os filtros estáticos **"Parceiro Matriz"** e **"Parceiro"** não sejam informados, exibindo mensagem de erro ao aplicar o filtro de busca para os títulos sem estas marcações. Quando ligado, mesmo que não se preencha os campos Parceiro ou Parceiro Matriz, será possível realizar a busca de títulos pelo filtros na tela de Compensação Financeira.

**Dias para retroação da baixa - DIASRETROACAO**

**Dias para lançamentos futuros - DIASFUTURO**

**Utilizar índice da moeda para descontos? - CALCINDCDESCMOE**

**Digitar data da baixa na Compensação Financeira?-DIGDTBAIXACF:** Ao habilitar este parâmetro, você poderá digitar a data da baixa na compensação financeira.

**Nota:** se os parâmetros **"Dias para lançamentos futuros (ref.data hoje) -DIASFUTURO"** e **"Dias para retroação da baixa - DIASRETROACAO"** estiverem habilitados para o usuário logado, o sistema permitirá que se faça a compensação financeira de títulos com data de baixa futura ou retroativa.

Será validado o valor desses parâmetros com a data de baixa informada. Trouxemos um exemplo:

Se o parâmetro **DIASFUTURO** estiver igual a 3 e você informar uma data de baixa com 3 dias a mais que a data atual, o sistema barra a rotina e apresenta a seguinte mensagem:

**"A data da baixa deve obedecer os parâmetros de 'Dias para Retroação' e 'Dias para Lançamentos Futuros".**

É fundamental a configuração dos valores padrões dos parâmetros **DIASFUTURO** e **DIASRETROACAO** no usuário SUP, definindo uma configuração geral que atenda a todos os usuários responsáveis pelas baixas, com as permissões mínimas necessárias. Usuários gestores, que podem precisar de limites mais amplos e personalizados, devem ter suas configurações ajustadas de forma individual.

**Observação:** os referidos parâmetros estão associados ao usuário SUP; portanto, o valor configurado será aplicado como padrão geral para todos os usuários que realizam baixas, exceto para aqueles com configurações personalizadas.

**Utiliza Sankhya Civil? - USASNKCIVIL:** caso este parâmetro esteja habilitado, ao compensar um título o valor líquido considerado será com a Variação Cambial do título embutido e se por acaso ocorrer baixa parcial de um título o residual deve ter a Variação Cambial proporcional.

**Considera Variação Cambial p/ Juros e Multas? - VARCAMBJURMULT**: se este parâmetro estiver ligado, juntamente com o parâmetro de chave USASNKCIVIL, o Cálculo de Juros e Multas será feito tendo como base o valor cheio (Vlr. Desdobramento + Variação Cambial).

**Considera Variação Cambial p/ Descontos? - VARCAMBDESC:** ao habilitar este parâmetro e o de chave USASNKCIVIL simultaneamente, o Cálculo de Descontos por Dia de Antecedência será calculado tendo como base o valor cheio (Vlr. Desdobramento + Variação Cambial).

**Considerar juros e multas negociados no cálculo dos juros de mora? - CONSJURMULNEG:** habilite este parâmetro para que seja realizado o cálculo dos juros de mora sobre o valor dos juros e multas que foram gerados por uma renegociação. Imaginemos um título a ser pago que foi originado de uma renegociação; nesta renegociação foram calculados juros e multa; com o parâmetro mencionado ativado, o cálculo dos juros pertinentes ao atraso do título irá utilizar como base além do valor do desdobramento do título, os juros e multa negociados que foram calculados na renegociação.

**Mostrar valores de moedas convertido no financeiro** **-** **MOSTRAVLRMOEDA**: este parâmetro permite que você verifique nas rotinas de Movimentação Financeira e Baixa de títulos os valores de moedas estrangeiras convertidos na moeda atual.

Ao tentar compensar um título que tenha moeda informada, será exibida uma mensagem notificando que a rotina não está preparada para efetuar a compensação de títulos com moeda. Pode-se acessar o link [Apresentação de valores em moedas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110233) para maiores detalhes.

**Realizar compensação financeira com moedas do Tipo - COMPMOEDAINDICE:** com esse parâmetro ligado, o sistema permitirá que você realize a compensação financeira com títulos que possuírem moedas distintas no Sankhya Om; esse tipo de compensação ocorrerá da seguinte maneira:

- Com ambas as moedas do Tipo Índice; ou
- Quando um dos títulos não possuir moeda enquanto o outro tiver moeda do Tipo Índice;

Assim, ao realizar o acerto, o sistema irá baixar os títulos de Receitas e Despesas conforme o valor informado no acerto. Lembre-se que a compensação com moedas distintas ocorrerá somente com moedas do **"Tipo"** configurado como **"Índice"** na tela [Valores de Moedas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604754-Valores-de-Moedas), no Painel Principal.

Com o parâmetro desativado, ao tentar realizar a compensação com moedas diferentes, o sistema o alertará que a conclusão da compensação não foi possível, pois os títulos envolvidos possuem moedas de tipos diferentes.

**Observação:** essa funcionalidade não será eficaz, quando na tela Valores de Moedas, no Painel Principal, o campo Tipo for selecionado com a opção Valor, pois ela é exclusiva para moedas selecionadas com a opção Índice. 

**Verif. se imposto ret. compensado atinge Vlr. Mín. - VERIMPTOTCOMPEN:** com este parâmetro ativado, é possível realizar a compensação financeira de um documento que tenha impostos retidos, garantindo que esses impostos continuem sendo calculados sobre os títulos desmembrados, mesmo que o **"Vlr Mínimo do Imposto"** (localizado na tela de [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos)) não seja atingido. Dessa forma, o valor final baixado dos novos títulos corresponderá ao valor original do título ao final da compensação. 

**Tipo de título para compensação de Crédito - TIPTITCREDCLI:** neste parâmetro é definido o [Tipo de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494) no qual a parcela do [Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173) usada na devolução foi configurada para geração do crédito.

Exemplo: foi realizado uma venda à vista, porém o cliente optou por devolver. Na devolução é necessário alterar o Tipo de Negociação para um que gere crédito para o cliente. Esse Tipo de Negociação precisa ter seu Tipo de Título idêntico ao informado no parâmetro, para que o crédito seja gerado corretamente.

**Importante:** na tela Compensação Financeira, ao receber a mensagem de validação:

**"Ocorreu um erro na BAIXA: Os financeiros estão vinculados a uma NF-e: não autorizada pela Sefaz. Não é possível baixá-los."**

Deve-se:

- Verificar a configuração do Tipo de Negociação e do Tipo de Título utilizado;
- Garantir que o Tipo de Título esteja corretamente configurado com base no parâmetro TIPTITCREDCLI, evitando inconsistências na validação.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115073-Compensa%C3%A7%C3%A3o-Financeira#top)
