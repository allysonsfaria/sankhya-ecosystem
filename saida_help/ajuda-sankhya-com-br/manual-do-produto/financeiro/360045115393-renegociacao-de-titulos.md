---
id: "360045115393"
titulo: "Renegociação de Títulos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115393-Renegocia%C3%A7%C3%A3o-de-T%C3%ADtulos"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-09-11T18:45:37Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Parcelamento", "USASNKCIVIL", "Movimentação Financeira", "Juros", "Vencimento", "Financeiro", "Títulos", "Renegociação", "CONSJURMULNEG", "Multas", "Agrupamento de títulos", "Atraso", "CONSPARCALCJURO", "dias", "MANTEMDTENTSAI", "Parcelar", "RENDESCMAIOR", "RENDIASVALJUR", "Renegociação de Títulos", "RENEGPARCDIF", "RENMAIOR", "RENMAIORREC", "RENMENOR", "RENMENORDESP", "RENMULTEMP", "br.com.sankhya.fin.mov.renegociacaotitulos", "Renegociação de Títulos manual", "Renegociação e Agrupamento", "Parcelamento e Juros", "Consulta e Modificação"]
---

# Renegociação de Títulos

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312457233175) Módulo: Financeiro > Rotinas
```

---

#### 📌 Manutenção [Aprimoramento na Renegociação de Títulos]

🔧**Tipo**: Melhoria 📅**Data**: 28/05/2025 🛠️**Versão Aplicável**: 4.35b33

**Descrição**

O processo de **Renegociação de Títulos** foi aprimorado para oferecer uma experiência mais intuitiva e alinhada com suas escolhas. Agora, ao renegociar um título e optar por um novo tipo que não seja "Boleto" ou "Pix" (como, por exemplo, "Nota Fiscal"), o sistema entenderá sua intenção e não apresentará mais a janela para emissão de boletos ou Pix.

Isso significa que você não verá mais avisos desnecessários. A janela de emissão de boleto/Pix só aparecerá quando o novo tipo de título selecionado realmente for um "Boleto" ou "Pix", e se a **Conta Bancária** estiver configurada para emitir boletos, e o **Tipo de Título** estiver marcado para "Imprimir Pix/Boleto/Duplicata para os títulos renegociados".

Com essa melhoria, você pode prosseguir com suas renegociações de forma mais fluida, sabendo que o sistema reage de acordo com o tipo de título que você escolher, evitando etapas extras quando elas não são necessárias.

---

# Funcionalidade Renegociação de Títulos

Podemos renegociar um título em consequência de seu vencimento, reajuste de parcelas do título, agrupamento de dois ou mais títulos em um único documento, de acordo com o processo e demanda da empresa.

A Renegociação de Títulos consiste na geração de um novo título de receita ou despesa em que se alteram os vencimentos e valores conforme necessários, baseando-se em um título original ou vários títulos originais, uma vez que na renegociação vários títulos podem ser agrupados para geração de um único documento.

Para facilitar sua navegação nas funcionalidades desta tela, acesse os links abaixo:

| [Conhecendo a rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115393-Renegocia%C3%A7%C3%A3o-de-T%C3%ADtulos#conhecendoarotina) |  | [Parcelamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115393-Renegocia%C3%A7%C3%A3o-de-T%C3%ADtulos#parcelamento) |
| --- | --- | --- |
| [Mais sobre Parcelamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115393-Renegocia%C3%A7%C3%A3o-de-T%C3%ADtulos#maissobreparcelamento) |  | [Desfazendo uma renegociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115393-Renegocia%C3%A7%C3%A3o-de-T%C3%ADtulos#desfazendoumarenegociao) |
| [Considerações importantes sobre...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115393-Renegocia%C3%A7%C3%A3o-de-T%C3%ADtulos#considera%C3%A7%C3%B5esimportantessobre...) |  | [Exemplos de Renegociação de Títulos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115393-Renegocia%C3%A7%C3%A3o-de-T%C3%ADtulos#exemplosderenegociaodettulos) |
| [Botão Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115393-Renegocia%C3%A7%C3%A3o-de-T%C3%ADtulos#botooutrasopes) |  | [Informações adicionais sobre...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115393-Renegocia%C3%A7%C3%A3o-de-T%C3%ADtulos#informa%C3%A7%C3%B5esadicionaissobre...) |
| [Limite de parcelas em Renegociações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115393-Renegocia%C3%A7%C3%A3o-de-T%C3%ADtulos#limitedeparcelasemrenegociaes) |  | [Segurança na Renegociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115393-Renegocia%C3%A7%C3%A3o-de-T%C3%ADtulos#segurananarenegociao) |
| [Parâmetros que influenciam...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115393-Renegocia%C3%A7%C3%A3o-de-T%C3%ADtulos#parmetrosqueinfluenciam...) |  |  |

### Conhecendo a rotina

![Imagem 2: Conhecendo a rotina](https://ajuda.sankhya.com.br/hc/article_attachments/4421006852887)

No Painel de Filtros, você poderá consultar uma **"Renegociação"**, informando seu número e/ou indicando o **"Parceiro"** e a **"Empresa"**, e complementando com as demais informações sobre **"Ordem de carga"**, **"Período da negociação"**, **"Intervalo das notas"**, **"Nro Único do Pedido"** e **"Tipo de título"**.

Ao efetivar a marcação **"Mostrar renegociados?"**, o sistema exibirá também os títulos que já foram renegociados para o Parceiro.

**Observação:** caso não tenha o número da Renegociação, utilize a lupa localizada à direita do referido campo que, ao ser acionada, será exibido um assistente de pesquisa para facilitar a busca por títulos renegociados.  

Após informar os filtros desejados, clique em **"Aplicar"** e o sistema exibirá os títulos na grade **"Títulos originais"**.

---

Para realizar uma renegociação, selecione os títulos a serem renegociados, acione o botão ![Imagem 3: Para realizar uma renegociação, s elecione os títulos a serem renegociados, acione o botão "Novo" da grade inferior…](https://ajuda.sankhya.com.br/hc/article_attachments/16580622039575) **"Novo"** da grade inferior denominada **"Títulos a renegociar"**, altere os dados necessários, como **"Valor do Desdobramento"**, **"Dt. Vencimento"**, **"Vlr. Juros"** e salve as alterações. Em seguida, clique em **"Renegociar"** para confirmar a operação ou **"Limpar"**, para desistir da operação. 

![Imagem 4: Para realizar uma renegociação, s elecione os títulos a serem renegociados, acione o botão "Novo" da grade inferior…](https://ajuda.sankhya.com.br/hc/article_attachments/4421251514903)

**Nota:** para que todos os campos do painel Títulos a renegociar sejam apresentados, utilize o botão ![Imagem 5: Nota: para que todos os campos do painel Títulos a renegociar sejam apresentados, utilize o botão "Modo grade (F6)" .](https://ajuda.sankhya.com.br/hc/article_attachments/17144294133783) **"Modo grade [F6]"**.

Para agrupar títulos e renegociá-los ao mesmo tempo, pressione a tecla **<Ctrl>** e selecione com um clique os títulos desejados; parcele normalmente de acordo com os novos vencimentos e valores e clique no botão Renegociar.

**Nota:** os botões Limpar e Renegociar só estarão habilitados depois que as alterações forem salvas.

**Observação:** as
renegociações realizadas não podem ser editadas, pois isso pode gerar inconsistências
financeiras. Assim, ao consultar uma renegociação na grade
Títulos a renegociar, quaisquer edições
realizadas não serão aplicadas à movimentação financeira. Portanto, o botão
**"Salvar"** não estará disponível e, ao reaplicar o filtro,
as informações na tela retornarão à forma original, apresentando a renegociação
conforme foi feita.

Se for necessário alterar uma renegociação, as melhores práticas recomendam desfazê-la ou realizar uma nova renegociação com base na negociação já existente. Lembre-se de que esses procedimentos devem estar alinhados com a política da empresa.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115393-Renegocia%C3%A7%C3%A3o-de-T%C3%ADtulos#top)

### Parcelamento

Caso seja necessário que o título seja parcelado, clique no botão ![Imagem 6: Caso seja necessário que o título seja parcelado, clique no botão "Parcelar" , o qual disponibilizará o pop-up de…](https://ajuda.sankhya.com.br/hc/article_attachments/16580622040471) **"Parcelar"**, o qual disponibilizará o pop-up de **"Parcelamento"**, que contém opções para cálculo de juros simples e composto, parcelamento automático e duplicação de títulos. As parcelas serão apresentas na grade Títulos a renegociar.

**Observação:** o botão Parcelar ficará desabilitado para quem não possuir permissão de **"Inclusão"** na tela de Renegociação de Títulos.

![Imagem 7: Observação: o botão Parcelar ficará desabilitado para quem não possuir permissão de "Inclusão" na tela de Renegociação…](https://ajuda.sankhya.com.br/hc/article_attachments/4421251630103)

Observe abaixo os campos dispostos em cada seção:

**Parcelamento**

Defina o **"Número de Parcelas"** em que será dividido o título renegociado.

O **"Desdobramento inicial"** se refere a quantidade de parcelas negociadas.

No campo **"Taxa de Juro"**, determine o valor da taxa em percentual de juro que será cobrado pela frequência, informada no campo abaixo. Se não for preciso acrescer juros, basta colocar zero ou deixar o campo em branco.

Em **"Taxa de multa s/ renegociação"**, informe o valor da multa aplicada sobre o valor total da renegociação, independente do vencimento dos títulos renegociados. Similar ao juro, se não for preciso acrescer multa, basta colocar zero ou deixar o campo em branco.

Selecione a **"Frequência"** dos desdobramentos (parcelas), conforme as opções abaixo:

- Diária;
- Semanal;
- Dezena;
- Quinzenal;
- 30, 60, 90, 120...;
- Mensal;
- Bimestral;
- Trimestral;
- Quadrimestral;
- Semestral;
- Anual;
- Personalizada.

**Nota:** no campo Frequência, a opção Mensal funcionará como o **"Fixa vencimento"** da tela de [Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173). E a opção 30/60/90/120... não fixará a data de vencimento das parcelas.

Efetue a marcação **"Com entrada?"** se houver algum valor de sinal, ou seja, uma parcela à vista e preencha o valor no campo à frente. Todavia, se você efetuar essa marcação e não informar nenhum valor, a entrada será calculada com valor proporcional ao número de parcelas.

Ao realizar a marcação **"Acrescentar número da parcela ao histórico?"**, o sistema gera automaticamente o número que a parcela representa do total, por exemplo, 1/10; 2/10.

Com a marcação **"Calcular juros até a data atual?"** efetuada, se o título já estiver vencido, o sistema calculará os juros referentes ao atraso, usando o valor informado no parâmetro **"Percentual de juro por dia de atraso nas receitas - TAXADIAATRASO"** (neste caso, utiliza-se juros compostos). Em seguida, usará os valores e opções informados na tela de Parcelamento para calcular os juros do parcelamento. Se o título não estiver atrasado, o sistema calculará apenas os juros usando os valores informados na tela citada.

Ao habilitar a marcação **"Considerar entrada ao aplicar multa e juros até a data atual?"**, o cálculo de juros e multa será realizado com base no valor da entrada, até a data atual.

**Importante:** quando os parâmetros **"Calcular multa e juros pelo tipo de título? - RENEGTIPTIT"** e **"Cálculo de juro obrigatório - JUROOBRIG"** estiverem habilitados e o parâmetro Percentual de juro por dia de atraso nas receitas - TAXADIAATRASO preenchido, o sistema irá calcular os juros até a data atual independente da marcação do campo Calcular juros até a data atual?, assim como, o cálculo já irá considerar a entrada, independente da marcação Considerar entrada ao aplicar multa e juros até a data atual? ter sido efetuada.

Quando a marcação **"Zerar juros e multas?"** estiver realizada, fará com que o sistema ignore qualquer configuração para multa e juros.

**Observação:** esta marcação não será salva como as demais, ou seja, sempre que o pop-up Parcelamento for aberto, ela estará desmarcada. O **"Controle de Acesso"** desta opção se dá por meio de um **"Acesso Especial"** da tela de [Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854), denominado **"Permite zerar Juros e Multas"**.

![Imagem 8: Observação: esta marcação não será salva como as demais, ou seja, sempre que o pop-up Parcelamento for aberto, ela…](https://ajuda.sankhya.com.br/hc/article_attachments/4421309874327)

A marcação **"Parcelar considerando juros, multas e descontos?"** será habilitada quando marcado o tipo de Parcelamento com juros composto (fixas). Ao selecionar esta marcação, a base de cálculo do título em atraso será o valor do desdobramento somado ao valor da multa e do juros menos o valor dos descontos. Caso esteja desmarcada, a base de cálculo será somente o valor do desdobramento, neste caso os valores de multas, juros e descontos já efetivos serão proporcionalizados na parcela.

Os campos **"Conta"** e **"Tipo de Título"** deverão ser preenchidos com a respectiva Conta e o Tipo de Título do PIX da cobrança quando houverem renegociações do PIX a serem realizadas.

Dessa forma, quando a renegociação for confirmada, as informações serão enviadas à API e os títulos originais serão cancelados, gerando assim, novas parcelas de Cobranças Pix. Considere ainda que, se o Tipo de título definido para as novas parcelas estiver com a marcação **"Imprimir Pix/boleto/duplicata p/os títulos renegociados?"** habilitada, o documento de cobrança será gerado.

Você ainda poderá realizar a impressão do documento PIX após uma renegociação de forma automática, para isso, realize as seguintes configurações:

![Imagem 9: No cadastro de Contas, aba Boleto(s)/Duplicatas , habilite a marcação "Pix Cobrança API" , e no campo "Modelo Cobrança…](https://ajuda.sankhya.com.br/hc/article_attachments/16115942538135) No cadastro de [Contas,](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas) aba [Boleto(s)/Duplicatas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas#ababoletosduplicatas), habilite a marcação **"Pix Cobrança API"**, e no campo **"Modelo Cobrança Pix"**, inclua o modelo de cobrança pix correspondente;

**(2)** Na aba [Renegociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abarenegociao) da tela [Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo), assinale a marcação **Imprimir Pix/boleto/duplicata p/os títulos renegociados?**. É importante salientar que o sistema irá olhar para o Tipo de Título informado no ato do parcelamento e que, essa marcação é levada em consideração independente do parâmetro RENEGTIPTIT estar ligado ou desligado.

**Tipo de parcelamento**

No **"Parcelamento com juros simples"**, serão calculados juros simples e no **"Parcelamento com Juro Composto"** serão calculados juros compostos para as parcelas. Observe o exemplo abaixo para melhor compreensão:

Temos um título de R$90,00 dividido em 3 parcelas com juros simples de 2% ao mês. Cada parcela ficaria em R$31,80; com vencimentos definidos no campo Frequência.

Se o cálculo for com juros composto, as parcelas ficariam com valores diferentes:

A primeira R$ 30,60; a segunda R$ 31,21 e a terceira R$31,84.

Há a possibilidade de somar os juros calculados de acordo com o número de parcelas e dividi-las em partes iguais (Parcelamento com Juro Composto (Fixas)).

No exemplo acima, efetuando o cálculo com juros composto (fixas), o valor de cada parcela seria de R$ 31,21.

Em **"Parcelamento com Juro Composto** **(fixas)"** os juros compostos serão calculados, porém as parcelas serão divididas de modo que fiquem iguais (fixas).

Já na **"Duplicação sem juros e sem multas (fixas)"**, não serão calculados juros e nem multas fixas para o título duplicado. O valor original do título não será dividido, desta forma, o valor será duplicado segundo o número de parcelas.

**(1)**Observe o exemplo abaixo:

Temos um contrato de locação por 6 meses com prestações mensais de R$100,00; sendo assim, será lançado na Movimentação Financeira um título de R$100,00 e utilizada esta opção para 'duplicar' este lançamento para os próximos 6 meses, obtendo o resultado:

Parcela 1/6: R$ 100,00

Parcela 2/6: R$ 100,00

Parcela 3/6: R$ 100,00

Parcela 4/6: R$ 100,00

Parcela 5/6: R$ 100,00

Parcela 6/6: R$ 100,00

Ressaltamos que, para títulos com origem no estoque não é permitido utilizar a opção Duplicação sem juros e sem multas (fixas).

**Observação:** quando a **"Conta bancária**" for alterada ao renegociar um parcelamento, o **"Banco"** também será modificado conforme a conta informada.

**Gravar Juros e Multas**

Se a marcação **"Somado ao valor"** estiver efetuada, fará com que o sistema some os valores de juros e multas negociados ao valor principal do título. O juro virá somado ao valor de cada parcela.

Efetuando a marcação **"Separado do valor"**, os valores de juros e multa serão registrados nos campos **"Vlr Juros"** e **"Vlr Multa"**, presentes na grade Títulos a renegociar e, além de poderem ser alterados, serão recalculados no momento da baixa, de acordo com os percentuais definidos nos parâmetros de Percentual de juro por dia de atraso nas receitas - TAXADIAATRASO e Percentual da multa - PERCMULTA, caso o recebimento seja realizado em atraso. Em caso de recebimento até a data de vencimento acordada, ou se os parâmetros citados estiverem com valor igual à zero, os valores calculados previamente serão mantidos.

**Nota:** se desejar que os juros e multas calculados na negociação sejam sempre mantidos, não recomendamos a utilização desta marcação.

Se efetuada a marcação **"Separado do valor (negociado)"**, fará com que o sistema grave os juros e multas calculados na renegociação nos campos **"Vlr Juros Negociado"** e **"Vlr Multa Negociada"** da grade Títulos a renegociar, e estes valores não serão reprocessados pelo sistema, nem poderão ser alterados pelo usuário. Estes só poderão ser alterados mediante uma nova Renegociação.

**Observação:** multas e Juros Negociados também podem ser perdoados, no momento da baixa, através da configuração da liberação dos eventos **"30 - Perdão de Multa no Financeiro"** **e "31 - Perdão de Juros no Financeiro"**, respectivamente.

**Importante:** através da ativação do parâmetro **"Considerar juros e multas negociados no cálculo dos juros de mora? - CONSJURMULNEG"**, será realizado o cálculo dos juros de mora sobre o valor dos juros e multas que foram gerados por uma renegociação. Imaginemos um título a ser pago que foi originado de uma renegociação; nesta foram calculados juros e multa; com o parâmetro mencionado ativado, o cálculo dos juros pertinentes ao atraso do título irá utilizar como base além do valor do desdobramento do título, os juros e multa negociados que foram calculados na renegociação.

**Data base de vencimento**

No **"Vencimento original"** serão calculadas as parcelas contando do primeiro vencimento do título.

Será utilizada a data de **"Negociação"** do título original, para cálculo da data base de vencimento das parcelas.

A data base **"Hoje"**, será a data do parcelamento.

Ao **"Informar data"** neste campo, as parcelas seguirão esta data como base para o vencimento.

**Nota:** ao informar a data, o sistema efetuará o cálculo dos juros até a data atual, utilizando a data informada neste campo mais a Frequência informada.

**(1)**Abaixo temos um exemplo:

Frequência = Diária

Taxa = 1 %

Valor do título = 100,00    

Data de Vencimento = 01/02/2022

Data base de vencimento: Informar data = 28/02/2022

Ao confirmar o Parcelamento, a Data de Vencimento do título será = 01/03/2022

(28/02 + Diária = 01/03/2022)

Se a Frequência neste exemplo fosse Mensal, o vencimento do título seria = 29/03/2022

(28/02 + Mensal = 29/03/2022)

**Data de Negociação**

A data de negociação dos novos títulos gerados a partir de um parcelamento será definida de acordo com as marcações desta seção.

Se a marcação **"Negociação original"** for efetuada, fará com que
todos os títulos parcelados apresentem Data de negociação igual à data de negociação do título original.

Efetuando a marcação **"Igual ao novo vencimento"**, todos os títulos parcelados apresentarão Data de negociação de acordo com a Frequência.

**(1)**Por exemplo:

Título original parcelado em 3 vezes, Data de negociação igual à 09/04/2022, Frequência igual à Mensal, marcação Igual ao novo vencimento efetuada:

1ª parcela data de negociação = 08/05/2022

2ª parcela data de negociação = 08/06/2022 

3ª parcela data de negociação = 08/07/2022

Caso a marcação
Hoje seja efetuada, todos os títulos parcelados apresentarão Data de negociação igual a data do dia do parcelamento, data atual do servidor.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115393-Renegocia%C3%A7%C3%A3o-de-T%C3%ADtulos#top)

### Mais sobre Parcelamento

Em um parcelamento, o Sankhya Om possui dois cálculos de juros diferentes, sendo eles:

![Imagem 10: Dado um título em atraso, são calculados os juros até a data atual, ou seja, traz o título até valor presente.](https://ajuda.sankhya.com.br/hc/article_attachments/16115942538135) Dado um título em atraso, são calculados os juros até a data atual, ou seja, traz o título até valor presente.

- Para este cálculo, efetue a marcação Calcular juros até a data atual?, que pode ser influenciada ou não pelo valor da entrada quando se realiza a marcação Considerar entrada ao aplicar multa e juros até data atual?.
- São considerados os parâmetros Percentual de juro por dia de atraso nas receitas - TAXADIAATRASO e Cálculo de juro simples ou composto - JUROSIMPLES.

![Imagem 11: Tomando um título que se deseja renegociar de forma a parcelar em "n" vezes, são aplicados juros por consequência do…](https://ajuda.sankhya.com.br/hc/article_attachments/16115900056215) Tomando um título que se deseja renegociar de forma a parcelar em "n" vezes, são aplicados juros por consequência do parcelamento.

- Para este cálculo, o sistema utiliza a taxa de juros do parcelamento (campo Taxa de Juros) e também o tipo definido no parcelamento (juros simples, juros composto, juros composto (fixa)).

**Observação:** podemos executar no sistema várias possibilidades, portanto, essas duas configurações podem ser utilizadas ao mesmo tempo.

Abaixo, temos alguns exemplos para melhor entendimento das configurações. Para todos eles, utilizaremos as seguintes variáveis:

| ``` M = Montante (Vlr Desdobramento origem+Juros) também chamado de valor futuro (após incidir juros) P = Vlr desdobramento origem, também chamado de valor presente (antes de incidir juros) i = Taxa de juros n = Qtd de períodos ``` |
| --- |

**Importante:** nessa rotina, o cálculo de juros considerará a quantidade de dias em atraso somado aos juros da quantidade de parcelas.

**(1)** Exemplo 1: 

Parcelas = 3

Frequência = Mensal (apenas influencia nos vencimentos das parcelas)

Taxa de Juros = 12%

Parcelamento com juros simples = Sim

Será considerado R$100,00 do título original e aplicar uma taxa de juros de 12%.

Fórmula utilizada:

M = P \* (1 + i)

M = 100 \* (1 + 0,12)

M = 112

P1 = M / n = 112/3 = 37,33

P2 = M / n = 112/3 = 37,33

P3 = M / n = 112/3 = 37,34 (arredondado considerando as demais parcelas)

**(1)** Exemplo 2:

Parcelas = 3

Frequência = Mensal (apenas influencia nos vencimentos das parcelas)

Taxa de Juros = 12%

Parcelamento com juros composto = Sim

Será considerado R$100,00 do título original e aplicada uma taxa de juros compostos de 12% na fórmula M = P \* (1 +  i):

Fórmula utilizada:

M = P \* (1 + i)

Para o P1, o Vlr Desdobramento será R$100/3 = 33,33, já os demais períodos, será o montante da parcela anterior.

P1 = 33,33 \* (1 + 0,12) = 37,33

P2 = 37,33 \* (1 + 0,12) = 41,81

P3 = 41,81 \* (1 + 0,12) = 46,84 (arredondado considerando as demais parcelas)

**(1)** Exemplo 3:

Parcelas = 3

Frequência = Mensal

Taxa de Juros = 12%

Parcelamento com juros composto (fixas)= Sim

Será considerado R$100,00 do título original e aplicada uma taxa de juros compostos de 12%. Como o valor das parcelas deve ser fixo, o sistema calcula primeiro o coeficiente financeiro (CF) para depois encontrar o valor de cada parcela.

Fórmula utilizada:

CF = i / (1 - ( 1 / (1+i)^n))

M = P \* CF

CF = 0,12 / (1 - ( 1 / (1 + 0,12)^3))

CF = 0,4163

P1 = 100 \* 0,4163 = 41,63

P2 = 100 \* 0,4163 = 41,63

P3 = 100 \* 0,4163 = 41,63

**(1)** Exemplo 4:

Parcelas = 1

TAXADIAATRASO = 2

JUROSIMPLES = Desligado

Calcular juros até a data atual = Sim

Dias em atraso = 5

Neste exemplo, desejamos que o sistema leve o título ao valor presente, pois o resultado da renegociação é uma nova data de vencimento para o título cobrando juros compostos pelos dias de atraso do mesmo.

Fórmula:

M = P \* (1 + i) ^ n

M = 100 \* (1 + 0,10) ^ 5

M = 161,05

**(1)** Exemplo 5:

Parcelas = 1

TAXADIAATRASO = 10

JUROSIMPLES = Ligado

Calcular juros até a data atual = Sim

Dias em atraso = 5

Neste exemplo, desejamos que o sistema leve o título a valor presente, pois o resultado da renegociação é uma nova data de vencimento para o título cobrando juros compostos pelos seus dias de atraso.

Fórmula:

M = P \* ( 1 + i \* n)

M = 100 \* (1 + 0,10 \* 5)

M = 150,00

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115393-Renegocia%C3%A7%C3%A3o-de-T%C3%ADtulos#top)

### Desfazendo uma Renegociação

Uma renegociação pode ser revertida ao título original (ou aos títulos originais) a qualquer momento, através do botão ![Imagem 12: Uma renegociação pode ser revertida ao título original (ou aos títulos originais) a qualquer momento, através do botão…](https://ajuda.sankhya.com.br/hc/article_attachments/16582852248855) **"Desfazer"**. Para isso, filtre a renegociação desejada, pelo campo Renegociação do Painel de filtros, onde será aberto o pop-up **"Pesquisando renegociações"**.

![Imagem 13: Uma renegociação pode ser revertida ao título original (ou aos títulos originais) a qualquer momento, através do botão…](https://ajuda.sankhya.com.br/hc/article_attachments/4421392158487)

Com um duplo clique sobre a renegociação desejada, esta será apresentada na grade Títulos a renegociar, onde o botão Desfazer é habilitado para desconstrução da operação de renegociação.

Ao desfazer uma renegociação de um PIX, os títulos PIX gerados serão removidos e as informações de remoção de cobranças enviadas à API. Dessa forma, o título original renegociado terá seu valor recomposto e você deverá acionar a opção [Imprimir PIX](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111893-Movimenta%C3%A7%C3%A3o-Financeira-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#imprimirpix) na [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111893-Movimenta%C3%A7%C3%A3o-Financeira-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es), para gerar a cobrança dos títulos PIX.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115393-Renegocia%C3%A7%C3%A3o-de-T%C3%ADtulos#top)

### Considerações importantes sobre Renegociações

![Imagem 14: Na renegociação será utilizada a "Conta" informada no parâmetro "Conta Padrão para Financeiro - CONTAPADRAOFIN" . Se…](https://ajuda.sankhya.com.br/hc/article_attachments/16115942538135) Na renegociação será utilizada a **"Conta"** informada no parâmetro **"Conta Padrão para Financeiro - CONTAPADRAOFIN"**. Se não houver conta informada neste parâmetro, será utilizada a conta referente ao primeiro Financeiro escolhido.

O campo **"Valor Juros"** apenas sugere um juro caso o título renegociado seja novamente pago em atraso, ou seja, esse valor não é acrescentado à renegociação caso o cliente cumpra o novo prazo estipulado.

![Imagem 15: O sistema não permite fazer uma Renegociação com o Financeiro, quando uma comissão for via nota e outra com comissão…](https://ajuda.sankhya.com.br/hc/article_attachments/16115900056215) O sistema não permite fazer uma Renegociação com o Financeiro, quando uma comissão for via nota e outra com comissão ligada direto no Financeiro. 

Sendo feita a tentativa deste tipo de renegociação, o sistema emitirá a seguinte mensagem:

**"O título XXX tem sua comissão com origem no financeiro e não pode ser renegociado junto com o título XXX porque este possui comissão a ser paga com origem".**

Isto irá ocorrer:

- Quando houver Financeiro gerado com comissão com origem no **"Financeiro"** e também Financeiro gerado com comissão a ser paga com origem na **"Nota"**:

**(2)** Comissão com origem no Financeiro:

1- Lançar Nota + Comissão + tipo de título = Cheque (Central de Vendas)

2- Gerar Comissão (Cálculo de Comissão por Fórmula)

3- Pagar Nota (Mov. Financeira – Baixa)

4- Fechar Comissão (Fechamento de Comissão)

5- Pagar Comissão (Mov. Financeira – Baixa)

6- Devolver Cheque (Devolução de Cheques)

**(2)** Comissão a ser paga com origem na Nota:

1- Lançar Nota + Comissão + tipo de título = Cheque (Central de Vendas)

2- Gerar Comissão (Cálculo de Comissão por Fórmula)

- O vendedor vinculado ao cabeçalho da Nota deve possuir o mesmo parceiro da Nota, pois a tela de Renegociação só apresentará títulos de um mesmo Parceiro;
- Ao tentar renegociar esses dois títulos o sistema emitirá a mensagem:

**"O título XXX tem sua comissão com origem no financeiro, e não pode ser renegociado junto com o título YYY porque este possui comissão a ser paga com origem nas notas fiscais."**

![Imagem 16: Na grade Títulos originais , os campos "INSS Retido" , "ISS Retido" e "IRF Retido" estão habilitados somente para…](https://ajuda.sankhya.com.br/hc/article_attachments/16115942545303) Na grade Títulos originais, os campos **"INSS Retido"**, **"ISS Retido"** e **"IRF Retido"** estão habilitados somente para visualização. Na geração das parcelas o sistema fará a marcação de acordo com os valores de impostos dos títulos originais.

Quando a renegociação possuir mais de um título original e todos forem de Receitas ou todos forem de Despesas, a renegociação não será feita, se entre os títulos existir valor para os impostos normais e valor para os impostos retidos. Por exemplo: um dos títulos possui **"INSS não retido"** e o outro título possui INSS retido. O sistema só permitirá a renegociação se todos os títulos possuírem valor normal para todos os impostos ou valor retido para todos os impostos.

Quando houver uma renegociação com mais de um título original, mesclando títulos de Receita e Despesa, se estes títulos possuírem algum valor informado nos campos **"Vlr ISS"**, **"Vlr INSS"** e **"Vlr IRF"**, o sistema não permitirá a renegociação. Sendo assim, só será permitida a renegociação de receitas e despesas juntas, quando não existirem valores de impostos descriminados nos campos descritos acima. A somatória dos novos valores de cada imposto após a renegociação, deve ser igual a somatória dos valores originais de cada imposto.

**Observação:** somente um dos novos títulos parcelados poderá conter o valor de
INSS/ISS ou IRF
do título original. Por exemplo: três títulos de Receita são renegociados em seis parcelas, sendo que um destes três títulos possuía valor de INSS. O valor deste INSS não será parcelado em seis juntamente com os títulos, e será registrado integralmente em uma única parcela entre as seis.

![Imagem 17: Evite renegociar os títulos de cartão de crédito ou débito, pois a taxa aplicada pela administradora é descontada no…](https://ajuda.sankhya.com.br/hc/article_attachments/16582540564503) Evite renegociar os títulos de cartão de crédito ou débito, pois a taxa aplicada pela administradora é descontada no momento da venda, impactando o valor recebido. Se for necessário mudar o tipo de título, a taxa da administradora será atualizada nas parcelas renegociadas. Lembre-se de que o valor da taxa está configurada no cadastro do [Tipo de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494).

**Impacto no Controle Orçamentário e Liberação de Limites:** Ao realizar a renegociação de títulos que passaram por liberação de limites orçamentários (excesso de despesa), observe o seguinte comportamento:

- **Reserva Orçamentária:** A aprovação anterior não é herdada pelos novos títulos. O sistema entende que a renegociação altera as condições da obrigação original.
- **Campos Financeiros:** O valor desdobrado (**VLRDESDOB**) do título renegociado é zerado e o montante é transferido para o campo **VLRALIBERAR**.
- **Nova Liberação:** O sistema solicitará uma **nova liberação de limites orçamentários** para os títulos gerados. Somente após essa nova aprovação o valor será efetivamente considerado como comprometido no orçamento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115393-Renegocia%C3%A7%C3%A3o-de-T%C3%ADtulos#top)

### Exemplos de Renegociação de Títulos

**(1)** **Exemplo 1 - Mudar apenas a Data de Vencimento**

Para isso, selecione a opção **"Parcelamento com juros simples"**, informe em **"Número de parcelas"** apenas 1 (uma parcela), não preencha nem **"Taxa de juro"** e nem **"Taxa de multa s/ renegociação"** e na opção **"Data base de vencimento"**, selecione uma das opções: **"Hoje"** ou **"Informar data"** e informe a nova data do vencimento.

**(1)** **Exemplo 2 - Calcular a Parcela com juros simples**

Neste caso, selecione a opção Parcelamento com juros simples, informe em Número de parcelas apenas 1 (uma parcela), preencha a Taxa de juro e se houver Taxa de multa s/ renegociação e na opção Data base de vencimento, selecione uma das opções: Hoje ou Informar data e informe a nova data do vencimento.

O sistema calculará a parcela, incluindo ao título original o valor dos juros e multa informada até a data de vencimento escolhida.

**(1)** **Exemplo 3 - Parcelamento com juro simples**

Aqui, selecione a opção Parcelamento com juros simples, informe o Número de parcelas a quantidade combinadas com o cliente, preencha a Taxa de juro e se houver Taxa de multa s/ renegociação e neste caso, a Frequência das parcelas é importante, o sistema oferece várias opções: diária, semanal, mensal, entre outras. A Frequência determina o intervalo entre as parcelas, então na opção Data base de vencimento selecione uma das opções possíveis, e o sistema calculará o valor de cada parcela de acordo com a quantidade informada, e a taxa de juros e multas com base na data de vencimento de cada parcela.

**(1)** **Exemplo 4 - Parcelamento com juro composto**

O procedimento para este caso será igual ao anterior diferindo apenas que, ao invés de se marcar juros simples, marque **"Parcelamento com juro composto"**.

A diferença no cálculo entre juro simples e juro composto, é que no juro simples o cálculo é feito pelo período corrido (diferença entre a data de início e a nova data de vencimento), já o juro composto é feito aplicando-se juro sobre juro.

**(2)** Exemplo juro simples:

Um título de R$100,00 com prazo de 2 meses, com 10% de juro calcula-se desta forma – 10% sobre 100 = R$10,00 x 2 (quantidade de meses)= R$20,00

Logo valor final será igual à = R$120,00

**Nota:** quando o parâmetro **"Considerar Qtd. parcelas no cálc. juro simples? - CONSPARCALCJURO"** estiver ativado, o sistema considera a seguinte fórmula para o cálculo dos juro simples:

J = P . i . n
J = Juros
P = Principal (capital)
i = Taxa de juros
n = Número de períodos

Quando o referido parâmetro for desligado, o sistema não irá considerar o número de períodos, ou seja:

J = P \* i

**(2)** Exemplo juro composto:

Um título de R$100,00 com prazo de 2 meses, com 10% de juro calcula-se desta forma – aplica-se 10% sobre 100 = 110 depois aplica-se novamente 10% referente ao 2º mês mas agora não mais sobre 100 e sim sobre 110.

Logo valor final = R$121,00.

Nesta opção, parcelando em 2 meses o valor das parcelas seria respectivamente: R$60,00 e R$61,00

**(1)** **Exemplo 5 - Juro composto com parcela fixa**

Com base no exemplo anterior, o sistema fará o cálculo do juro composto, mas dividirá o valor das parcelas de modo a terem o mesmo valor em todas as parcelas.

Então o valor das parcelas seriam de: R$ 60,50 cada.

(1)** Exemplo 6 - Duplicação sem juro e sem multa (fixas)**

Esta opção é utilizada para replicar o valor do título em várias parcelas de mesmo valor pra vencimentos posteriores.

A empresa faz um financiamento com parcelas fixas de R$100,00 em 18 vezes, então lança um título no valor de R$100,00 no financeiro e nesta tela faz as duplicações.

- - Selecione a opção **"Duplicação sem juro e sem multa (fixas)"**;
  - Informe no campo **"Quantidade de parcelas"** = 18;
  - Na **"Data base para vencimento"**, selecione **"Vencimento original"**;
  - E em **"Frequência"**, informe **"Mensal"**.

O sistema gerará 18 parcelas de R$100,00 para o mês atual e os próximos 17 meses com o mesmo intervalo, dispensando assim o lançamento das 18 parcelas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115393-Renegocia%C3%A7%C3%A3o-de-T%C3%ADtulos#top)

### Botão Outras Opções

O botão ![Imagem 18: O botão " Outras Opções" , possui como funcionalidade apenas a opção Preferências que, ao ser acionada, abre um pop-up…](https://ajuda.sankhya.com.br/hc/article_attachments/16582371224215) **"Outras Opções"**, possui como funcionalidade apenas a opção Preferências que, ao ser acionada, abre um pop-up com esta mesma nomenclatura:

![Imagem 19: O botão " Outras Opções" , possui como funcionalidade apenas a opção Preferências que, ao ser acionada, abre um pop-up…](https://ajuda.sankhya.com.br/hc/article_attachments/4421128584727)

Observe abaixo os campos dispostos em cada seção deste pop-up:

**Ao renegociar**

Se a marcação **"Zerar descontos, multas e juros?"** estiver realizada, o sistema irá desprezar o valor da multa e de descontos informados no Financeiro. No caso dos juros sempre será ignorado.

As marcações **"Parcelar descontos e multas?"** e **"Manter descontos, multas e juros?"** ratearão o valor do desconto ou multa quando o Financeiro possuir estes valores.

Quando você efetuar a marcação **"Manter nosso número para 1 título?"**, fará com que o campo **"Nosso Número"** do título original, seja registrado no Nosso Número do novo título renegociado.

**Observação:** esta
marcação é válida apenas para quando se renegocia um título em outro título, ou seja 1 pra 1. A renegociação deve ser obrigatoriamente de 1 título antigo para 1 título novo (como o próprio nome do campo diz: Manter nosso número para 1 título). Se você pegar 1 título e renegociá-lo em 2 novos títulos, a marcação não funcionará.

Quando a marcação **"Proibir renegociar título de contatos diferentes?"** for ativada, fará com que o sistema não permita que títulos que possuam diferentes **"Contatos do Parceiro"**, sejam renegociados. Sendo assim, apenas títulos que pertençam a um mesmo **"Contato"** poderão ser renegociados.

Se a marcação **"Atualizar metas financeiras por vencimento?"** estiver realizada, ao fazer a renegociação de um título cuja TOP atualiza **"Meta Financeira por Vencimento"**, o sistema recalculará o **"Realizado"** da meta com o período de vencimento.

**Ao imprimir boleto**

**Importante:** através do parâmetro **"Campo p/ tx. de boleto na Renegociação de Títulos - CAMTXBOLRENTIT"**, realize a configuração inicial da taxa que corresponde à impressão de boletos resultantes da renegociação do(s) título(s). Neste parâmetro, indique em qual campo será inserido o valor desta taxa. São apresentados os seguintes campos para seleção:

- Vlr. do Desdobramento;
- Vlr. Multa;
- Vlr. Juros;
- Despesas c/Cartório;
- Vlr. Vendor;
- Vlr. Multa Negociada;
- Vlr. Juros Negociados.

Após este passo, o valor da referida taxa será apontado no campo **"Ou cobrar taxa"**, localizado na aba [Boleto(s)/Duplicatas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas#ababoletosduplicatas) do cadastro de Contas.

Além disso, para imprimir o boleto de forma automática ao renegociar um título, realize as configurações abaixo:

![Imagem 20: No cadastro de Contas Bancárias , aba Boleto(s)/Duplicatas :](https://ajuda.sankhya.com.br/hc/article_attachments/16115942538135) No cadastro de Contas Bancárias, aba [Boleto(s)/Duplicatas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas#ababoletosduplicatas):

- Realize a marcação **"Boleto Avançado/Duplicatas"**;
- Selecione o **"Modelo"** de boleto que será utilizado como base para as impressões;
- No campo **"Impressora"** preencha o equipamento pelo qual a impressão será realizada. Caso não tenha uma impressora pré-estabelecida, informe um ponto de interrogação **"?"** para que, no momento da impressão, seja feito o questionamento de qual impressora será utilizada.

![Imagem 21: No cadastro de Tipos de Títulos , aba Renegociação , a marcação "Imprimir boleto/duplicata p/os títulos renegociados?"…](https://ajuda.sankhya.com.br/hc/article_attachments/16115900056215) No cadastro de Tipos de Títulos, aba [Renegociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abarenegociao), a marcação **"Imprimir boleto/duplicata p/os títulos renegociados?"** deve estar habilitada.

Esta aba estará visível apenas quando o parâmetro **"Calcular multa e juros pelo tipo de título? - RENEGTIPTIT"** estiver ligado e o sistema seguirá uma determinada hierarquia para obtenção dos valores de juros e multas:

**1.** O cadastro de Parceiros, aba [Juros/Multas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abajurosmultas) é a primeira configuração a ser verificada;

**2.** Caso no cadastro de Tipos de Título, aba Renegociação e no cadastro de Parceiros, aba Juros/Multas não existam configurações, o sistema irá considerar as informações incluídas no [Parcelamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115393-Renegocia%C3%A7%C3%A3o-de-T%C3%ADtulos#parcelamento) da tela Renegociação de Títulos;

**3.** Não existindo nenhuma informação na tela Renegociação de Títulos, no cadastro de Tipos de Título e no cadastro de Parceiros, o sistema irá seguir as parametrizações realizadas na tela [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834);

**4.** Existindo configuração apenas no cadastro de Tipos de Título, o sistema irá utilizá-la para os cálculos;

**5.** Caso o cadastro de Tipos de Título, aba Renegociação e o cadastro de Parceiros, aba Juros/Multas estejam configurados, o sistema irá considerar as informações do cadastro de Parceiros. Em consequência deste 5º preceito, é possível que no decorrer do processo de Renegociação de Títulos, seja apresentada a seguinte mensagem:

**"Existem parceiros que possuem % de multa, % de juro e tipo de juro específicos, por isso alguns títulos tiveram o cálculo com os valores informados no cadastro de parceiro."**

![Imagem 22: Nesta seção, efetue a marcação "Não enviar boleto por e-mail" .](https://ajuda.sankhya.com.br/hc/article_attachments/16115942545303) Nesta seção, efetue a marcação **"Não enviar boleto por e-mail"**.

**Observação:** você poderá configurar esta rotina para que, após a renegociação o sistema possa enviar o boleto por e-mail, de acordo com as opções abaixo:

- Enviar boleto para o e-mail do parceiro;
- Enviar boleto para o e-mail dos contatos marcados para receberem boleto por e-mail.

**Importante:** a opção Enviar boleto para o e-mail do parceiro faz com que o sistema apenas realize o envio do e-mail, não abrindo o pop-up de Impressão de Boletos. Caso deseje que o pop-up seja aberto, selecione a opção Não enviar boleto por e-mail.

**Cores**

Configure as cores em que serão exibidos os títulos de Receitas e Despesas, selecionando-as na tabela de cores que será apresentada ao clicar nos quadrados à frente dos campos **"Cor para receita"** e **"Cor para despesa"**, respectivamente.

**Impressão de Renegociação**

É necessário informar o caminho da **"Impressora"**, o **"Modelo"** e o **"Tipo de impressora"** que será usado para imprimir a renegociação.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115393-Renegocia%C3%A7%C3%A3o-de-T%C3%ADtulos#top)

### Informações adicionais sobre juros e multas

**Sobre os Juros** 

Caso nas Preferências da Renegociação de Títulos, a marcação Manter descontos, multas e juros? seja realizada, o sistema soma o valor dos juros anteriormente calculados (em consequência do atraso do título) ao valor dos juros calculados na renegociação, para se chegar a um valor final de juros.

**Sobre a multa**

O parâmetro **"Percentual da multa - PERCMULTA"** não é utilizado na rotina de Renegociação; em relação à esta configuração, o sistema toma como base a seguinte hierarquia:

- No cadastro de Parceiros, aba [Juros/Multas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abajurosmultas), se o campo **"% de multa"** estiver preenchido, este valor será considerado;
- Caso o parâmetro Calcular multa e juros pelo tipo de título? - RENEGTIPTIT esteja ativado e, consequentemente, os campos **"% Juros"** e **"% Multa"** presentes no cadastro de Tipos de Título, aba [Renegociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abarenegociao), estejam informados; então serão considerados estes valores.
- O sistema irá considerar o valor informado no campo **"Taxa de multa s/ renegociação"** presente no pop-up Parcelamento da própria Renegociação de Títulos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115393-Renegocia%C3%A7%C3%A3o-de-T%C3%ADtulos#top)

### Limite de parcelas em Renegociações

Na tela Usuários, aba [Parc. Máx. em Renegociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874#abaparc.mx.emrenegociao), informe a quantidade máxima de parcelas por empresa que será possível renegociar.

![Imagem 23: Na tela Usuários , aba Parc. Máx. em Renegociação , informe a quantidade máxima de parcelas por empresa que será…](https://ajuda.sankhya.com.br/hc/article_attachments/4421135592855)

No exemplo retratado na imagem acima, podemos constatar que Marcelo terá alçada para realizar parcelamentos em até duas vezes, quando os títulos que estiverem sendo renegociados pertencerem às empresas 34 e 40. Isso significa que, se ele realizar uma renegociação de um título pertencente à uma destas empresas, com parcelas superiores à 2, o sistema não permitirá, solicitando assim, uma pessoa com alçada para este tipo de liberação, onde este o fará através da tela de Liberação de Limites,
evento [39 - Quantidade de parcelas na renegociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#39-quantidadedeparcelasnarenegociao).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115393-Renegocia%C3%A7%C3%A3o-de-T%C3%ADtulos#top)

### Segurança na Renegociação

![Imagem 24: Atenção Implantadores: O sistema grava na tabela TGFREN o "Código do usuário" responsável pela renegociação e a "Data…](https://ajuda.sankhya.com.br/hc/article_attachments/16582540564503) **Atenção Implantadores:** O sistema grava na tabela TGFREN o **"Código do usuário"** responsável pela renegociação e a **"Data hora da alteração"** na tabela DHALTER, registrando assim, as informações dos que renegociaram títulos no sistema.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115393-Renegocia%C3%A7%C3%A3o-de-T%C3%ADtulos#top)

### Parâmetros que influenciam nesta rotina

A validação dos valores dos títulos que são gerados por uma renegociação, pode ser realizada considerando os quatro primeiros parâmetros citados abaixo. Nos referimos aqui, ao somatório dos valores dos documentos renegociados, em comparação com os valores originais dos títulos para mais ou para menos, tanto de despesas, quanto de receitas. São eles:

- **Permitir reneg. para valor MAIOR em DESPESAS? - RENMAIOR:** Quando habilitado, será possível concluir renegociações em que o valor do título de despesa é maior que o valor dos títulos originais.
- **Permitir reneg. para valor MENOR em DESPESAS? - RENMENORDESP:** Ao ativar este parâmetro, será permitido consumar renegociações de títulos de despesa que estiverem com valor menor que os títulos originais.
- **Permitir reneg. para valor MAIOR em RECEITAS? - RENMAIORREC:** Quando habilitado, será possível concluir renegociações em que o valor do título de receita é maior que o valor dos títulos que o originaram.
- **Permitir reneg. para valor MENOR em RECEITAS? - RENMENOR:** Ativando este parâmetro, será permitido consumar renegociações de títulos de receita que estiverem com valor menor que os títulos originais.
- **Permitir renegociação com desconto maior? - RENDESCMAIOR:** Se este parâmetro estiver ligado, o sistema permitirá realizar renegociações com redução de juros ou aumento de descontos com relação ao título original, emitindo a mensagem:

**"Somatório dos novos descontos é superior aos descontos originais. Confirma?"**

Caso o parâmetro esteja desligado, o sistema não permitirá confirmar renegociações com descontos superiores aos originais.

- **Utiliza Sankhya Civil? - USASNKCIVIL:** Se o parâmetro estiver ligado, o total original deve ser calculado tendo como base o valor cheio (Vlr. Desdobramento + Variação Cambial) de cada título presente na grade de **"Títulos originais"**. O Vlr Desdobramento e o Valor base para cálculo de juros e multas dos títulos a renegociar será o **"Total original"**, ou seja, o valor cheio (Vlr. Desdobramento + Variação Cambial) dos títulos da grade Títulos originais. A Variação Cambial dos títulos gerados com a renegociação virá zerada.
- **Mantém Data de Entrada/Saída nas Renegociações - MANTEMDTENTSAI:** Com este parâmetro habilitado, ao gerar os novos títulos originados pela renegociação, será feita a gravação da Data de Entrada/Saída, com o valor igual a maior Data de Entrada/Saída do título original. Além disso, será feito o bloqueio do agrupamento de títulos para renegociação com Data de Entrada/Saída pertencentes a competências diferentes (Meses/Anos); todos os títulos renegociados terão a Data de Entrada/Saída pertencentes a mesma competência.
- **Dias toleráveis para perdoar juros na renegociação - RENDIASVALJUR:** Informe neste parâmetro, a quantidade máxima de dias que os juros serão tolerados em uma renegociação de um título em atraso. A configuração deste parâmetro acompanha o que for determinando no campo **"Dias tol. juros reneg."** presente na aba [Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874#abaidentificao) do Cadastro de Usuários, de forma que, o sistema verifica primeiramente o campo citado no cadastro do usuário e, caso este não tenha nenhuma informação, analisa a quantidade estipulada no parâmetro. Caso ambos os locais não estejam preenchidos, nenhuma validação quanto aos dias para perdão de juros será realizada, e a renegociação será permitida.
- **Permite renegociar p/Parceiro diferente? - RENEGPARCDIF:** Se habilitado, na Renegociação de Títulos será possível incluir parcelas para parceiros diferentes do Parceiro dos títulos originais. O filtro por Parceiro não será obrigatório e na tela de parcelamento aparecerá o campo **"Parceiro (Novos Títulos)"**, esse campo sempre virá preenchido com o Parceiro do primeiro título selecionado na grade. Você poderá alterá-lo para gerar todas as parcelas para um determinado parceiro, ou gerar para o parceiro sugerido e na grade inferior da tela o campo **"Parceiro"** poderá ser alterado, dando a possibilidade de gerar cada parcela para um parceiro diferente. Quando este parâmetro estiver desligado, o filtro por Parceiro torna-se obrigatório, o campo Parceiro (Novos Títulos) não aparece e o campo Parceiro na grade inferior torna-se não editável.
- **Permitir múltiplas empresas na renegociação de títulos? - RENMULTEMP:** Se habilitado, na Renegociação de Títulos será possível incluir parcelas para empresas diferentes da Empresa dos títulos originais. O filtro por Empresa não será obrigatório e na tela de parcelamento aparecerá o campo **"Empresa (Novos Títulos)"**, esse campo sempre virá preenchido com a Empresa do primeiro título selecionado na grade. Você poderá alterá-la para gerar todas as parcelas para uma determinada empresa, ou gerar para a empresa sugerida e na grade inferior da tela, o campo **"Empresa"** poderá ser alterado, dando a possibilidade de gerar cada parcela para uma empresa diferente. Quando este parâmetro estiver desligado, o filtro por Empresa torna-se obrigatório e o campo Empresa (Novos Títulos) não aparece, porém, o campo Empresa da grade
  inferior continua editável, independente da situação deste parâmetro.

Quando ambos os parâmetros RENEGPARCDIF e RENMULTEMP estão ativados, ou seja, quando os filtros de Parceiro e Empresa não são obrigatórios, você deverá informar pelo menos um filtro. Esse filtro pode ser o Parceiro, ou Empresa, ou Ordem de Carga ou ainda um Filtro Personalizado.

![Imagem 25: O parâmetro "Valida tipo de natureza (Receita / Despesa) na movimentação - VALIDATIPONAT" não realiza validação nesta…](https://ajuda.sankhya.com.br/hc/article_attachments/16582540564503) O parâmetro **"Valida tipo de natureza (Receita / Despesa) na movimentação - VALIDATIPONAT"** não realiza validação nesta rotina, pois essa verificação ocorre apenas na [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115393-Renegocia%C3%A7%C3%A3o-de-T%C3%ADtulos#top)
