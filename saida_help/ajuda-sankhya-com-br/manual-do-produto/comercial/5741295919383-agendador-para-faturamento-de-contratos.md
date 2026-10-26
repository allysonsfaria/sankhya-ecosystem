---
id: "5741295919383"
titulo: "Agendador para Faturamento de Contratos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/5741295919383-Agendador-para-Faturamento-de-Contratos"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-09-02T18:18:48Z"
rotulos: ["Configuração", "Faturamento", "Contrato", "Agendamento", "Agendador de Faturamento de Contratos", "br.com.sankhya.agend.faturamento.contratos", "Agendador Faturamento Contratos", "Parâmetro", "Comercial"]
---

# Agendador para Faturamento de Contratos

| ```  Módulo: Comercial > Avançado > Agendadores  Versão disponível: A partir da 4.12 ``` |
| --- |

---

Por meio desta tela, realize agendamentos para tornar automático o faturamento dos contratos. Após a criação dos agendamentos, na tela [Controle de Jobs](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594634) será criado um registro correspondente a tarefa configurada, para execução.

Para iniciar o cadastro do agendamento, acione o botão ![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/15992740170263) **"Cadastrar Agendamento Tarefa"**, em seguida, no painel principal preencha o campo**"Descrição agendamento"** e acione a marcação **"Ativo"**.

![Imagem 2: Para iniciar o cadastro do agendamento, acione o botão "Cadastrar Agendamento Tarefa" , em seguida, no painel principal…](https://ajuda.sankhya.com.br/hc/article_attachments/23349695926295)

![Imagem 3: Acompanhe o status da última execução do agendador através do campo "Status última execução" .](https://ajuda.sankhya.com.br/hc/article_attachments/16090207715991) Acompanhe o status da última execução do agendador através do campo **"Status última execução"**.

---

Agora, iremos configurar as abas da tela, sendo elas:

[Aba Horários](https://ajuda.sankhya.com.br/hc/pt-br/articles/5741295919383-Agendador-para-Faturamento-de-Contratos#abahorarios)                                                                                  [Aba Frequência Agendamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/5741295919383-Agendador-para-Faturamento-de-Contratos#abafrenquenciaagendamento)

[Aba Filtros/ Parâmetros Obrigatórios](https://ajuda.sankhya.com.br/hc/pt-br/articles/5741295919383-Agendador-para-Faturamento-de-Contratos#abafiltros/par%C3%A2metrosobrigat%C3%B3rios)                                      [Aba Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/5741295919383-Agendador-para-Faturamento-de-Contratos#abaconfigura%C3%A7%C3%B5es)

[Aba Histórico](https://ajuda.sankhya.com.br/hc/pt-br/articles/5741295919383-Agendador-para-Faturamento-de-Contratos#abahistorico)

---

#### Aba Horários

Nesta aba, preencha o campo **"Próxima execução em"** com a data e o horário da próxima execução. Você pode definir também a **"Data Final de Execução"** e o horário final.

![Imagem 4: Nesta aba, preencha o campo "Próxima execução em" com a data e o horário da próxima execução. Você pode definir também…](https://ajuda.sankhya.com.br/hc/article_attachments/5743898902935)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5741295919383-Agendador-para-Faturamento-de-Contratos#agora)

#### Aba Frequência Agendamento

Configure nesta aba, a frequência de execução do agendador.

![Imagem 5: Configure nesta aba, a frequência de execução do agendador.](https://ajuda.sankhya.com.br/hc/article_attachments/5743854803863)

Assim, informe o horário da **"1° Execução"**, e caso seja necessário adicione mais execuções acionando o botão ![botão](https://ajuda.sankhya.com.br/hc/article_attachments/15992695701015) **"Adicionar novo horário para execução"** ou remova todos os horários de execução por meio do botão ![botão](https://ajuda.sankhya.com.br/hc/article_attachments/15992740171031) **"Remover todos os horários de execução"**.

Além do horário, você pode definir a frequência das execuções do agendador em:

- **Diário:** Clicando nesta opção, será efetuada diariamente;
- **Semanal** e **Mensal:** Selecionando uma destas opções, serão exibidas para marcação, os dias da semana e do mês, respectivamente.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5741295919383-Agendador-para-Faturamento-de-Contratos#agora)

#### Aba Filtros/Parâmetros Obrigatórios

Nesta aba, configure os filtros e os parâmetros para a execução do faturamento, por meio das seguintes seções:

![Imagem 8: Nesta aba, configure os filtros e os parâmetros para a execução do faturamento, por meio das seguintes seções:](https://ajuda.sankhya.com.br/hc/article_attachments/5743705778327)

**Seção Filtros**

Para filtrar o faturamento, informe a **"Empresa"**, o **"Parceiro"** e a**"Data de Reajuste"** do contrato. Os filtros configurados aqui, incluindo múltiplos filtros personalizados, agora são aplicados de forma consistente no processo de faturamento.

A marcação **"Considerar Contatos/Perfil/Serviço"** funciona da seguinte maneira:

- Caso o parceiro possua um perfil vinculado e este possua um perfil de consumo, na nota gerada no faturamento do contrato com essa opção marcada serão gerados também itens para cada produto desse perfil de consumo do parceiro;
- Se esta opção estiver desmarcada e o parâmetro **"Contrato para software? - CONTSOFT"**estiver ligado, o sistema validará se existe ISS cadastrado para a relação Natureza x Serviço e incluirá um item na nota com valor zero para o serviço encontrado na relação com a natureza.

**Seção Parâmetros Obrigatórios**

Os campos desta seção são preenchidos com os valores presentes nos seguintes parâmetros:

- **TOP Padrão para Faturamento de Contratos - FATSERVTOP:**Campo **"Tipo de Operação"**;
- **Tipo de Título para Faturamento de Contratos - FATSERVTIT:**Campo **"Tipo de Título"**;
- **Tipo de Negociação para Faturamento de Contratos - FATSERVTPV:**Campo **"Tipo de Negociação"**.

Ressaltamos que, ao acessar essa rotina, caso não haja qualquer informação no campo **"TOP para faturamento em contratos"** no [Cadastro de Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos), de [Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-) ou de [Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Servi%C3%A7o), ao realizar o faturamento de um contrato, a TOP da nota faturada será a mesma informada no campo **"Tipo de Operação"** dessa tela.

Os **"Parâmetros Obrigatórios"** serão aplicados somente para o faturamento, ou seja, serão utilizados na nota gerada após o faturamento do contrato ou serviço complementar, então não é necessário informá-los para realizar o filtro.

Na tela [Observações para Notas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596474 "br.com.sankhya.com.cad.observacoesNotas") pode-se cadastrar a observação padrão que será impressa nas Notas Fiscais. Para mais informações sobre esta tela, verifique a documentação de apoio referente a mesma clicando no link acima.

No faturamento de um contrato o sistema utiliza a conta informada no campo **"Conta bancária** **empresa"**, da aba [Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abaidentificao) do [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros), diferentemente dos outros faturamentos que utilizam a conta do Tipo de Negociação.

Se o parâmetro **"Contrato para software - CONTSOFT"**estiver habilitado, será exibido o campo **"Conta Bancária"**. Caso seja necessário utilizar uma conta diferente da conta do Cadastro de Parceiros, informe-a neste campo.

O campo **"Data para Faturamento"** indica que a data para o faturamento será sempre a mesma do dia da execução do agendamento, ou seja, se o agendamento for executado no dia 27/01/2022, a data para o faturamento também será igual a 27/01/2022.

Você poderá definir os campos **"Mês para Referência"**, **"Mês para Referência do V.T. e dos Insumos"** e **"Mês para Referência do V.A"** de acordo com as seguintes alternativas:

- **Mês do faturamento:** esta opção indicará que o mês de referência seja o mesmo da execução do faturamento. Ou seja, se executado em 27/01/2022, o mês para referência será 01/01/2022.
- **Mês anterior ao faturamento:** esta opção determinará que o mês de referência seja o mês anterior ao da execução do faturamento. Isto é, se executado em 27/01/2022, o mês para referência será 01/12/2021.
- **Mês posterior ao faturamento:** esta opção indicará que o mês de referência seja o posterior ao da execução do faturamento. Ou seja, se executado em 27/01/2022, o mês para referência será 01/02/2022.

**ℹ️ Nota**

O campo **Mês para Referência** define apenas a DTREF utilizada no faturamento do contrato. A competência da prestação do serviço exibida na observação da nota fiscal é definida separadamente pelo campo **Tipo de Pagamento**, no cadastro de **Contratos**, podendo resultar em um mês diferente da DTREF sem que isso indique uma inconsistência. Para saber mais, acesse [Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos).

**Observação:** Os campos Mês para Referência do V.T. e dos Insumos e Mês para Referência do V.A só estarão visíveis na tela quando a TOP informada no campo **"Tipo de Operação"** possuir em sua aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos) a marcação **"Tem VA e/ou VT no contrato"** acionada. Além disso, as informações destes campos não serão utilizadas na busca dos contratos.

A marcação **"Gerar 1 única fatura"**, quando acionada, fará com que o sistema gere uma única nota agrupando o faturamento de serviços complementares com o faturamento mensal do contrato. Essa opção estará habilitada somente se o parâmetro Contrato para software - CONTSOFT estiver ligado.

No campo **"Série"**, informe a série da nota a ser gerada. Se houver uma série que irá enviar uma Nota Fiscal de Serviço, ao ser informada neste campo, o sistema irá gerar a nota fiscal de serviço automaticamente no final do processo.

Além disso, se não houver nenhuma informação no campo **"Série para faturamento em contratos"** no [Cadastro de Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos), de [Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-) ou de [Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Servi%C3%A7o), ao faturar um contrato, a série da nota faturada será àquela informada no campo Série dessa tela.

Não havendo informação nos campos TOP para faturamento em contratos e/ou Série para faturamento em contratos nas telas mencionadas acima, ao efetuar o faturamento de um contrato, a TOP e Série da nota faturada serão as mesmas informadas nesses campos, respeitando a hierarquia abaixo:

1. Cadastro de Produtos / Serviço;
2. Cadastro de Contratos, aba Produtos/Serviços, sub-aba Geral;
3. Cadastro de Contatos, aba Geral.

A marcação **"Agrupar Contratos"** agrupará o faturamento de vários contratos em uma única nota. O Agrupamento do contrato seguirá a ordem: Parceiro, Dia de Pagamento, Dia útil e Critério de Rateio.

Ressaltamos que para utilizar esta marcação, deve-se ligar os parâmetros **"Utiliza grupos de faturamento de contratos? - GRUPFATCONT?"** e **"Utiliza faturamento de contratos pro rata? - FATCONTPRORATA"**, assim como o campo **"Grupo de Faturamento"** (tela [Cadastro de Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774#abageral)) deverá ser preenchido com o faturamento a qual o grupo pertence.

Ainda sobre a marcação Agrupar Contratos, temos que:

- Ao faturar um contrato que gere comissão, se a marcação se encontrar habilitada, a comissão do contrato não será gerada na nota.
- Quando você utilizar a marcação e faturar, caso possua contratos pro-rata e não pro-ratas na seleção, eles não serão agrupados entre si.
- O agrupamento de contratos que não são pro-rata respeitará a ordem Parceiro, Dia de Pagamento, Dia útil, Critério de Rateio, TOP e Série.
- Se nos contratos convencionais (não pro-rata) tiver produtos com TOP's diferentes, o sistema respeitará essa configuração e irá faturar esses produtos separadamente, assim como ocorre nos contratos pro-rata.
- Caso algum dos contratos selecionados (não pro-rata) tenham produtos com TOP's distintas, o sistema irá faturar separadamente os produtos que possuem TOP's diferentes, ou seja, não agrupando esses produtos.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5741295919383-Agendador-para-Faturamento-de-Contratos#agora)

#### Aba Configurações

Nesta aba, temos a seção **"Opções"**, onde você poderá preencher o campo **"E-mail para notificação de execução"** com um ou mais e-mails, separados por ponto e vírgula (**;**), que será(ão) utilizado(s) para envio de notificação em caso de problemas na execução. Além disso, após a conclusão da execução de cada agendamento, o destinatário informado neste campo receberá um e-mail para que possa ter ciência do resultado e em caso de qualquer impedimento, promover as ações corretivas necessárias.
A configuração da tela [Servidor SMTP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593494) será utilizada para definir o remetente da mensagem.

Informe também, a quantidade de dias que será mantido o histórico por meio do campo **"Qtd. dias para manter histórico"**.

![Imagem 9: Informe também, a quantidade de dias que será mantido o histórico por meio do campo " Qtd. dias para manter histórico" .](https://ajuda.sankhya.com.br/hc/article_attachments/5743887378583)

Na seção **"Configurações para Faturamento"**, temos as seguintes marcações:

Quando a marcação **"Exibir Parcela Faturamento"** estiver acionada o sistema irá informar automaticamente no campo **"Nro Nota"** na aba [Provisões Financeiras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos#abaprovisesfinanceiras) do [Cadastro de Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos#top), o número da fatura referente à nota gerada pelo faturamento do contrato. Para isso, o parâmetro **"Exibir parcelas no faturamento de contratos? - EXIBPARCFATCON"** deve estar ligado.

A marcação **"Usar Tipo de Negociação do Contrato"** necessita estar desmarcada caso se deseje utilizar o Tipo de Negociação desta tela.

Se habilitada a marcação **"Calcular Impostos Mensais"** será realizado o cálculo dos impostos mensais nas notas geradas pelo processo de faturamento. Ressaltamos que, o cálculo ocorrerá somente se o valor do faturamento for maior ou igual ao valor mínimo da base mensal dos outros impostos.

Se acionada a marcação **"Gerar taxa conforme Conta Bancária"** não será utilizada a taxa da conta estabelecida no [Cadastro do Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494). Além disso:

- Caso esteja marcada, o parâmetro **"Taxa de boleta no total da nota - TAXBOLNOT"**estiver ligado e o valor da nota for inferior ao valor mínimo da conta, o campo VLRJURO do FINANCEIRO da nota resultante do faturamento ficará com o valor da taxa informada no cadastro da conta bancária.
- Se estiver marcada, o parâmetro de chave TAXBOLNOT estiver desligado e o valor da nota for inferior ao valor mínimo da conta, o campo VLRJURO do FINANCEIRO da nota resultante do faturamento ficará com o valor da taxa informada no cadastro da conta bancária.

**Observação:** O Tipo de Juro depende do parâmetro **"Taxa de boleta com tipo INCLUSO - TAXBOLNOTTJ"**. Assim, se este parâmetro estiver ligado, o valor do juro será somado ao valor do Desdobramento.

Quando habilitada a marcação **"Gerar Rateio por Critério para a Nota"**, o critério de rateio informado no Cadastro de Contratos é copiado para a nota destino que será gerada pelo processo de faturamento.

Se a marcação **"Usar Série maiúscula"** for habilitada, o sistema alterará a série que foi informada no faturamento com letra minúscula, para letra maiúscula, possibilitando assim a geração da fatura em casos de conflito entre a configuração da TOP e o faturamento. Considere os seguinte exemplo:

Na Central de Faturamento de Contratos são validadas as configurações do Controle de Numeração da TOP, utilizada no Faturamento. Se na Central a série for informada com letra minúscula e na configuração do Controle de Numeração da TOP tiver sido informada com letra maiúscula, o sistema não permitirá a geração da Fatura. Marcando esta opção, o sistema altera a série informada de minúscula para maiúscula, possibilitando assim a geração da fatura.

Com a marcação **"Copiar observação dos itens do contrato"** habilitada tem-se a cópia da observação digitada no campo **"Local de instalação"** do Cadastro de Contratos, para o campo **"Observação"** nos itens de Produto/Serviço da nota gerada por meio do faturamento.

Se no [Cadastro do Contrato](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos) houver alguma informação de **"Observação Padrão"**, ao acessar a tela de Faturamento de Contratos e utilizar a marcação **"Usar observação padrão do contrato"** disponível nesse botão, ao faturar, a nota será gerada com a Observação do Contrato.

Caso haja a informação do Tipo de Título no Cadastro do Contrato e na tela [Faturamento de Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos) utilize a opção **"Usar tipo de título do contrato"**, ao faturar, a nota será gerada com o Tipo de Título do Contrato independente das demais configurações que impactem no tipo de negociação utilizado.

Através da marcação**"Gerar provisões a partir do vencimento da nota faturada"** você define se será calculado o vencimento das provisões a partir do vencimento real da nota faturada ou não.

**Observação:**Caso a marcação acima esteja selecionada e a marcação **"Gerar Financeiro pelo Tipo de Negociação usando Vencto da tela + (mais) Prazo das Parcelas"** também esteja realizada, o sistema fará a conta dos vencimentos das provisões considerando a data para vencimento da primeira provisão.

Sendo assim, ao faturar o contrato, quando a marcação Gerar provisões a partir do vencimento da nota faturada estiver realizada, será utilizada a data fixa também para as provisões subsequentes ao faturamento do contrato, independente da data do faturamento deste e do tipo de negociação.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5741295919383-Agendador-para-Faturamento-de-Contratos#agora)

#### Aba Histórico

Você pode acompanhar nesta aba o histórico com as informações básicas de execução dos reajustes realizados a partir dos agendamentos programados.

Neste histórico, os registros serão mantidos apenas pelo número de dias definido no campo Qtd. dias para manter histórico da aba [Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/5741295919383-Agendador-de-Faturamento-de-Contratos#abaconfigura%C3%A7%C3%B5es).

![Imagem 10: Neste histórico, os registros serão mantidos apenas pelo número de dias definido no campo Qtd. dias para manter…](https://ajuda.sankhya.com.br/hc/article_attachments/6142521578391)

Ao acionar o botão "**Ver Detalhes"**, será aberto o pop-up **"Resumo da Operação - Faturamento de Contratos"** com as informações detalhadas dos faturamentos processados na respectiva execução selecionada.

A aba **"Não faturados"** será exibida quando houver contratos com impedimentos no faturamento, destacando o motivo pelo qual cada um não foi faturado. Esta aba foi aprimorada para exibir corretamente todos os contratos não faturados. Ao dar um **duplo clique** nos contratos listados nesta aba ou acionando o botão **"Ver Contrato"**, você será redirecionado à tela **Contratos** e contextualizado no respectivo registro.

![Imagem 11: A aba "Não faturados" será exibida quando houver contratos com impedimentos no faturamento, destacando o motivo pelo…](https://ajuda.sankhya.com.br/hc/article_attachments/7723938949655)

A aba **"Faturas geradas"** será exibida caso hajam contratos sem impedimentos no faturamento, listando as respectivas notas geradas. Ao clicar duas vezes em uma nota, você será redirecionado para a [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414) ou [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793), conforme o tipo de faturamento, e posicionado no respectivo documento. Já ao acionar o botão **"Mostrar no Portal"**, você será redirecionado ao [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654) ou [Portal de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953) exibindo somente as notas listadas nesta aba.

![Imagem 12: Pode existir uma divergência entre o valor exibido nos campos "Contratos Faturados" e "Faturas Geradas" na parte…](https://ajuda.sankhya.com.br/hc/article_attachments/33557657208855) Pode existir uma divergência entre o valor exibido nos campos **"Contratos Faturados"** e **"Faturas Geradas"** na parte superior do pop-up de detalhes da operação e as informações listadas na aba **"Faturas Geradas"**.

Essa diferença ocorre porque:

- Os campos **"Contratos Faturados"** e **"Faturas Geradas"** registram o histórico de faturamento diretamente do detalhe do faturamento (TGFDFT).
- A grade da aba **"Faturas Geradas"** exibe os dados diretamente dos cabeçalhos de nota (**TGFCAB**).
- Se uma nota fiscal for gerada e posteriormente excluída, ela será movida para uma tabela de exclusões (**TGFCAB\_EXC**). Nesses casos, a nota não aparecerá mais na grade da aba **"Faturas Geradas"**, mas os campos no resumo superior continuarão a contabilizar que o faturamento original ocorreu. Esse comportamento é esperado e reflete a real situação do sistema.

![Imagem 13: Se uma nota fiscal for gerada e posteriormente excluída, ela será movida para uma tabela de exclusões ( TGFCAB_EXC ).…](https://ajuda.sankhya.com.br/hc/article_attachments/7724021419415)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5741295919383-Agendador-para-Faturamento-de-Contratos#agora) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5741295919383-Agendador-para-Faturamento-de-Contratos#top)

---

![Imagem 14: Agora que você configurou o agendamento, será criado um registro correspondente a esta tarefa na tela "Controle de…](https://ajuda.sankhya.com.br/hc/article_attachments/16090207715991) Agora que você configurou o agendamento, será criado um registro correspondente a esta tarefa na tela **"Controle de Jobs"**, para execução. Para mais informações sobre esta tela acesse o link [Controle de Jobs](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594634).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5741295919383-Agendador-para-Faturamento-de-Contratos#top)
