---
id: "7091805775255"
titulo: "Como calcular férias"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/7091805775255-Como-calcular-f%C3%A9rias"
trilha: "Manual do Produto > Pessoas+ > Férias > Cálculo de Férias"
atualizado_em: "2026-10-02T15:41:51Z"
rotulos: ["CLT", "eSocial", "Folha de Pagamento", "FPLIBFOLPORLOTE", "Recibo de Férias", "FPRELATRECFE", "Cálculo eSocial", "Parâmetros e Afastamentos", "FPOCOPRORROGADO", "Recursos Humanos"]
---

# Como calcular férias

Todo colaborador com carteira assinada tem direito a férias depois de 12 meses de trabalho (chamado de período aquisitivo).

As principais regras são:

- o funcionário tem direito a 30 dias de férias por ano;
- as férias podem ser divididas em até três períodos, se o trabalhador e a empresa concordarem. Um dos períodos deve ter pelo menos 14 dias corridos e os demais não poderão ser inferiores a cinco dias corridos, cada um.;
- o início das férias não pode ocorrer nos dois dias que antecedem feriado ou o dia de repouso semanal remunerado (DSR);
- o funcionário pode solicitar o abono pecuniário (venda de férias) com o máximo de dez dias e o adiantamento do 13° salário;
- o pagamento das férias deve ser feito até dois dias antes do início das férias;
- se o funcionário não tirar as férias até 12 meses depois do direito adquirido, a empresa precisa pagar as férias em dobro, além disso, se o funcionário faltou muito sem justificar, ele pode perder parte dos dias de férias;
- o período de férias deve ser informado ao funcionário com pelo menos 30 dias de antecedência.

Essas regras ajudam a garantir que o trabalhador tenha seu descanso de forma organizada e de acordo com a lei.

| **⚠️** **Atenção**  **Sobre o recesso de estagiários**  O [**estagiário**](https://ajuda.sankhya.com.br/hc/pt-br/articles/41826803259415) não possui vínculo empregatício regido pela CLT. Sua relação é regulamentada pela Lei nº 11.788/2008, que assegura o direito ao recesso remunerado de 30 dias quando o estágio possui duração igual ou superior a um ano, ou de forma proporcional nos contratos com duração inferior.  Quando a empresa possui férias coletivas, o recesso do estagiário pode ser concedido no mesmo período, facilitando o alinhamento operacional.  A restrição prevista no art. 134, § 3º, da CLT, que impede o início das férias nos dois dias que antecedem feriado ou DSR, aplica-se exclusivamente aos empregados celetistas. Assim, o recesso do estagiário pode iniciar nesse período, desde que respeitadas as condições previstas na Lei do Estágio e eventuais normas internas da empresa ou da instituição de ensino. |
| --- |

O cálculo de férias é realizado individualmente ou coletivamente, acesse os links abaixo para saber como se efetua cada um deles:

| Cálculos de férias | |
| --- | --- |
| [Cálculo de férias individuais](https://ajuda.sankhya.com.br/hc/pt-br/articles/7091805775255-Como-calcular-f%C3%A9rias#C%C3%A1lculodeF%C3%A9riasIndividuais) | [Cálculo de férias coletivas](https://ajuda.sankhya.com.br/hc/pt-br/articles/17266680029335) |
| [Bloqueio de Cálculo de Férias para Funcionários Afastados](https://ajuda.sankhya.com.br/hc/pt-br/articles/42521124311575) | [Quitação de Férias em caso de Afastamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/35498082386071) |

---

### Cálculo de férias individuais

Visto que as requisições de férias foram aprovadas pelo líder e DP da empresa, agora chegou o momento de fazer o cálculo da folha de pagamento e demais obrigações acessórias.

Com o aviso de férias emitido, pode-se realizar o cálculo da folha de férias. Para isso acesse a tela [Gerenciador de DP](https://ajuda.sankhya.com.br/hc/pt-br/articles/18367435782935) e, em seguida, o menu **"Cálculos"**.

![Imagem 1: Com o aviso de férias emitido, pode-se realizar o cálculo da folha de férias. Para isso acesse a tela Gerenciador de DP…](https://ajuda.sankhya.com.br/hc/article_attachments/31710414560407)

Clicando nesse menu, a tela [Cálculos](https://ajuda.sankhya.com.br/hc/pt-br/articles/18612838324631) será aberta, apresentando todas as folhas com pendência para serem executadas.

[GIF animado: Imagem 2: Clicando nesse menu, a tela Cálculos será aberta, apresentando todas as folhas com pendência para serem executadas.](https://ajuda.sankhya.com.br/hc/article_attachments/31710521033111)

Clique no card do funcionário que deseja calcular as férias e serão apresentadas as informações do aviso, bastando ajustar a data de pagamento.

![Imagem 3: Clique no card do funcionário que deseja calcular as férias e serão apresentadas as informações do aviso, bastando…](https://ajuda.sankhya.com.br/hc/article_attachments/7091834354327)

Realize a conferência da folha de férias, navegando pelas abas horizontais da tela, sendo **"Folha"**, **"Movimentações"**, **"Avisos"** e **"Regras"**.

Para a realização da quitação de férias automática de férias e 13º para funcionários afastados a mais de 180 dias na abertura do sistema, ligue o parâmetro **"Quita férias na abertura para afastados - FPQUITAFERABERT"**. Desse modo, na aba Avisos desta tela uma mensagem será exibida para informá-lo da quitação. Com o parâmetro desativado, a quitação automática não será efetuada na abertura.

Já, para que haja prorrogação do período de gozo por afastamento, é necessário que o parâmetro **"Dias afastados altera fim do período concessivo - FPOCOPRORROGADO"** esteja ligado. Dessa forma, ao inserir a data de retorno de um afastamento, será apresentada a seguinte mensagem:

**"Aviso**
**Atenção! O fim do período concessivo do funcionário será prorrogado. Sugerimos que no retorno definitivo ao trabalho, o funcionário entre em gozo de férias de imediato."**

Na aba LOG serão apresentados os dados das fórmulas e as variáveis utilizadas no cálculo.

**Nota:** a variável &DIAFERADI demonstra a quantidade de dias de férias que pertencem à competência seguinte, quando o período de gozo das férias atravessa a virada de um mês para o outro (por exemplo, férias de 30/09 a 14/10). Essa variável alimenta o evento **Demonstrativo Dias de Férias Adiantados (evento 4431)**, utilizado para segregar corretamente os valores entre a referência atual e a referência seguinte.

Quando o funcionário precisar ser afastado por mais de 180 dias dentro um período aquisitivo, as férias relacionadas a esse período serão quitadas. Porém, caso haja um período concessivo garantido antes do afastamento, este deverá ser aproveitado após o retorno do funcionário ao trabalho, sendo que, também, terá uma data limite para que essas férias sejam utilizadas.

Além disso, após o cálculo da folha de férias do período concessivo, o sistema realizará a abertura de um novo período aquisitivo com a data inicial um dia após o retorno do afastamento.

**Observação:** a liberação da folha de férias considerará a data do pagamento. Por exemplo: as férias calculadas no mês de março, tem pagamento programado para 27 de fevereiro, sendo assim, será liberado para o eSocial na referência do mês de fevereiro.

**Importante:** quando inserir no campo **"Texto"** do parâmetro **"Lista dos eventos de férias do processo antigo - FPLISTEVFERDEST"** o código dos eventos antigos de férias, estes serão desativados. Logo, ao realizar a confirmação será exibida a seguinte mensagem:

**"Atenção! Os eventos de férias (...) listados no parâmetro "FPLISTEVFERDEST" foram DESATIVADOS. Será necessário cadastrar os novos eventos do Recibo de Férias, procure um consultor Sankhya."**

**Nota:**em caso de férias fracionadas, o parâmetro **Holerite de Férias - FPRELATRECFE** não deve ser configurado com nenhum código, do contrário, o recibo de férias irá buscar sempre a data de saída do primeiro período gozado.

O evento **Demonstrativo Dias de Férias Adiantados (evento 4431)** é apresentado sempre que o período de gozo das férias atravessa a virada de um mês para outro, por exemplo, férias que começam em setembro e terminam em outubro. Nesse caso, o sistema identifica automaticamente quantos dias do período pertencem à competência seguinte e lança esse evento para representar essa fração, dividindo corretamente os valores entre a referência atual e a próxima. Esse comportamento **não tem relação com o período aquisitivo do funcionário**, ele ocorre mesmo quando o período aquisitivo já está corretamente vencido e adquirido, pois depende apenas de o período de gozo cruzar dois meses.

Ainda sobre férias fracionadas, é importante conferir se o evento **Demonstrativo Dias de Férias Adiantados** **(evento 4431)** está devidamente lançado. A ausência deste evento na folha de férias pode gerar impactos significativos nas folhas mensais seguintes, como: cálculo incorreto de médias, inconsistências em provisões, erros nos reflexos de férias e divergências na apuração de encargos trabalhistas. Caso esteja ausente, revise a configuração do evento ou a fórmula vinculada.

Em seguida, acione o botão **Confirmar Folha**, ao lado esquerdo da tela:

![Imagem 4: Em seguida, acione o botão Confirmar Folha , ao lado esquerdo da tela:](https://ajuda.sankhya.com.br/hc/article_attachments/31710887583383)

Após a confirmação da folha, verifique na aba Avisos se há algum ajuste a ser realizado; se houver, faça as devidas correções ou arquivamentos para prosseguir. É importante ressaltar que só após realizados os ajustes ou arquivamentos a folha estará pronta para integração financeira e contábil.

| ``` Os avisos estarão registrados como arquivados. Vale lembrar que uma marcação com o  usuário logado será criada sinalizando quem arquivou os avisos e em qual horário. ``` |
| --- |

Após fazer os arquivamentos ou ajustes dos avisos e realizada a conferência da folha do cálculo de férias, emita os documentos correspondentes. Para isso, na lateral esquerda da tela, clique no menu **"Documentos"**.

![Imagem 5: Após fazer os arquivamentos ou ajustes dos avisos e realizada a conferência da folha do cálculo de férias, emita os…](https://ajuda.sankhya.com.br/hc/article_attachments/31710887585047)

Realizando a baixa do **"Relatório de Médias"** de cálculo, você poderá conferir nele as configurações estabelecidas para o cálculo das médias, por meio da tela [Regras de Cálculo](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405310442007-Regras-de-C%C3%A1lculos#top). Assim, para cada média apresentada será possível analisar em detalhes o cálculo realizado pelo sistema.

**Observação:** caso queira personalizar o Relatório de Médias e defini-lo como modelo padrão, após as alterações desejadas no arquivo, acesse a tela [Relatórios formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597694-Relat%C3%B3rios-Formatados) e o inclua como novo relatório. Copie o **"Código"** do relatório e o informe no parâmetro **"Código Relatório de médias e provisões - FPRELMEDIAS"**, desse modo, o sistema passará a considerar esse relatório como padrão de impressão.

Aqui pode-se emitir também o aviso de férias, caso não tenha sido entregue anteriormente ao funcionário.

Caso deseje fazer uma comparação das folhas entre referências diferentes desse mesmo funcionário, ou entre outros colaboradores, acione o menu **"Comparação"**.

![Imagem 6: Caso deseje fazer uma comparação das folhas entre referências diferentes desse mesmo funcionário, ou entre outros…](https://ajuda.sankhya.com.br/hc/article_attachments/31710887588375)

Se desejar também fazer o cálculo de uma folha de férias sem que haja requisição, utilize a opção de cálculo individual, acionando o botão **"Individual"** na tela Cálculos. Em seguida, selecione o tipo de folha **"Férias"** e faça o mesmo processo citado anteriormente:

[GIF animado: Imagem 7: Se desejar também fazer o cálculo de uma folha de férias sem que haja requisição, utilize a opção de cálculo…](https://ajuda.sankhya.com.br/hc/article_attachments/31710887590167)

![Imagem 8: Informações adicionais sobre o cálculo da folha de férias](https://ajuda.sankhya.com.br/hc/article_attachments/16539445827991) **Informações adicionais sobre o cálculo da folha de férias**

**(1)** Se a marcação Abono Pecuniário proporcional ao período de gozo presente na tela [Regras de Cálculo](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405310442007-Regras-de-C%C3%A1lculos), aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405310442007-Regras-de-C%C3%A1lculos#abapropriedades), sub-aba **"Férias"** estiver acionada, ao efetuar o cálculo de férias na tela Cálculos não será permitido que a quantidade de **"Dias de Abono"** seja superior ao limite de ⅓ dos dias de férias informado. Caso ultrapasse o limite, será apresentada a mensagem: **"Total de dias de abono informado ultrapassou o limite de ⅓ das férias"**.

**(1)** A quantidade de dias informada no campo Dias de abono também deve respeitar o número de dias limite de abono pecuniário definido no parâmetro **"Valor Máximo de Abono Pecuniário-FPABONO"**. Do contrário, será apresentada a mensagem: **"Total de dias de abono ultrapassou o limite de X dias"**.

**(1)** Além disso, se o parâmetro FPABONO estiver configurado e na tela Cálculos, for informada uma quantidade de **"Faltas"** dentro do período, o limite de dias de Abono Pecuniário deverá ser ajustado para ⅓ dos dias de direito de férias, para que respeite a tabela de faltas para férias. Para melhor compreensão considere o seguinte exemplo:

Na tela Cálculos, em **"Informações Complementares de férias"** os campos abaixo foram preenchidos com os seguintes valores:

**(2)** Faltas = 9

**(2)** Dias de férias = 24

O fato do funcionário ter 9 faltas injustificadas no período aquisitivo o faz ter apenas 24 dias de férias por direito, logo, embora no parâmetro FPABONO esteja definido que o limite para dias de abono seja de 10 dias, neste caso, seria de apenas 8 dias (24/3 = 8), dentro do período aquisitivo, independente de férias únicas ou quebradas em vários períodos de gozo.

![Imagem 9: O fato do funcionário ter 9 faltas injustificadas no período aquisitivo o faz ter apenas 24 dias de férias por direito,…](https://ajuda.sankhya.com.br/hc/article_attachments/20799431485207)

**Tabela 1- Tabela de faltas para férias**

---

Após concluído o cálculo da folha de férias e realizadas as conferências, pode-se fazer o envio da mesma ao eSocial. Para isso, acesse a tela [Gerenciador de Folhas](https://ajuda.sankhya.com.br/hc/pt-br/articles/4424800696599), disponível também nos menus do Gerenciador de DP ou pela barra de pesquisa do Sankhya Om.

Para facilitar a busca, preencha os campos disponíveis nos filtros, no canto esquerdo da tela.

Localize a folha e, na barra lateral direita, acione o botão **"Liberação para eSocial"**, informe o **"Tipo de Folha"**, a **"Referência"** e clique no card da empresa que deseja selecionar.

**Importante:** para que haja a liberação da folha por lote, é necessário ativar o parâmetro **"Liberação folha para Esocial em lotes? - FPLIBFOLPORLOTE"**.

**Observação:** quando for liberar a folha complementar ou rescisão complementar para o eSocial de um funcionário demitido, se o parâmetro **"Utiliza parceiro tomador da época do desligamento - USA\_TOM\_EPC\_DLG"** estiver ligado, no CODLOTACAO da TFPTFOL será levado o parceiro em que o funcionário estava lotado na época do desligamento. Porém, se o parâmetro estiver desligado, será levado o parceiro da empresa.

**Nota:** quando calcular férias com data de pagamento anterior à referência do gozo, serão gerados os eventos S1200 e S1210 considerando as tags **<perapur>** e **<perref>** geradas pela data de pagamento.

**Nota:** conforme o Manual do eSocial, quando há mais de um pagamento na referência os demonstrativos de pagamento serão enviados cada um com sua identificação de maneira separada. Por exemplo:

Se informado um único evento S-1210, no caso de pagamento de salário da competência anterior no dia 05, adiantamento pago no dia 20 e PLR paga no dia 25, estes serão identificados por distintos demonstrativos de pagamento no evento S-1200, por meio da tag ideDMDEV.

Sendo que, os demonstrativos de pagamento do intermitente serão apresentados separados por convocação e para o autônomo o detalhamento de cada pagamento será efetuado na referência.

[GIF animado: Imagem 10: Sendo que, os demonstrativos de pagamento do intermitente serão apresentados separados por convocação e para o autônomo…](https://ajuda.sankhya.com.br/hc/article_attachments/7092016852631)

Na aba **"Funcionários"**, selecione o card do funcionário e clique no botão **"Liberar Dados para eSocial"**.

[GIF animado: Imagem 11: Na aba "Funcionários" , selecione o card do funcionário e clique no botão "Liberar Dados para eSocial" .](https://ajuda.sankhya.com.br/hc/article_attachments/7092475796375)

Pronto! Sua folha estará disponível para geração e envio na tela Central do eSocial.

**Observação:** caso queira, é possível também enviar os dados ao eSocial após a confirmação da folha, para isso, após configurar os eventos S-1200, S-2299, S-2399 e S-1210, o sistema exibirá o botão **"Liberar dados para o esocial"**; assim, após o envio da folha ao esocial, será informado por meio do ícone **"Bloquear liberação"** que a liberação para o esocial está bloqueada.

Na tela Central do eSocial, faça a geração do evento de forma individual ou coletiva e, no menu Eventos Pendentes, realize a liberação para transmissão. Para visualizar o status clique no menu Acompanhamento.

Agora que a Folha de Férias já foi transmitida ao eSocial e conferida, também se pode efetuar a liberação do recibo de férias para o funcionário.

Para isso, na tela do Gerenciador de Folhas, utilize o botão ![lançar](https://ajuda.sankhya.com.br/hc/article_attachments/15481372420503) **"Liberação para PortalRH"**.

Informe o Tipo de Folha, a Referência e clique no card da empresa que deseja selecionar. Em seguida, na aba Funcionários, selecione o card do funcionário e clique no botão **"Liberar Dados para PortalRH"**:

[GIF animado: Imagem 13: Informe o Tipo de Folha , a Referência e clique no card da empresa que deseja selecionar. Em seguida, na aba…](https://ajuda.sankhya.com.br/hc/article_attachments/7092582928151)

Pronto. Sua folha estará disponível para visualização do funcionário por meio do Portal RH e aplicativo Pessoas+.

---

![Imagem 14: Informações adicionais](https://ajuda.sankhya.com.br/hc/article_attachments/16539445827991) **Informações adicionais**

**(2)** A partir da versão da simplificação 1.0 do e-Social, o evento S-1200 do cálculo realizado no recibo de férias será liberado de acordo com a data de pagamento, conforme [Manual de Orientação do e-Social-MOS](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-0-consolidada-ate-a-no-s-1-0-11-2022-retificada-em-17-05-2022.pdf), com exemplos claros nas páginas 128 e 129. Desse modo, caso realize o cálculo no processo antigo será apresentada a seguinte advertência:

**"Não foi possível realizar o cálculo do recibo de Férias, pois existem eventos de Férias com configurações desatualizadas (processo descontinuado). Necessário entrar em contato com sua unidade de serviços"**

Para mais informações sobre essa configuração acesse os artigos [Configuração de férias](https://ajuda.sankhya.com.br/hc/pt-br/articles/7084333899415-Configura%C3%A7%C3%A3o-de-f%C3%A9rias-Saiba-mais-) e [Instrução de modificação de envio de férias no layout S-1200 para versão 1.0 do eSocial a partir de 22/05/2022](https://ajuda.sankhya.com.br/hc/pt-br/articles/6934782221719-Instru%C3%A7%C3%A3o-de-modifica%C3%A7%C3%A3o-de-envio-de-f%C3%A9rias-no-layout-S-1200-para-vers%C3%A3o-1-0-do-eSocial-a-partir-de-22-05-2022-).

**(2)** O pagamento das férias e de antecipação do 13° salário serão efetuados em parcela única mesmo se houver licença maternidade em vigor.

**(2)** Para o cálculo de médias, o sistema não considerará o cálculo da folha complementar, tipo **"O- Folha complementar de dissídio"** e sequência **"700"** do acumulados do ano.

**(2)** O sistema irá realizar a apuração do INSS, conforme o regime de competência definido no art. 214, § 14 do [Decreto 3.048/99](https://www.jusbrasil.com.br/topicos/11728348/artigo-214-do-decreto-n-3048-de-06-de-maio-de-1999#:~:text=valor%20das%20di%C3%A1rias.-,(Revogado%20pelo%20Decreto%20n%C2%BA%2010.410%2C%20de%202020).,na%20forma%20da%20legisla%C3%A7%C3%A3o%20trabalhista.):

**“A incidência da contribuição sobre a remuneração das férias ocorrerá no mês a que elas se referirem, mesmo quando pagas antecipadamente na forma da legislação trabalhista”.**

A saber:

1. A base de INSS é apurada na totalidade considerando todos os eventos incidentes do cálculo;
2. O desconto não possui natureza de imposto final e, sim, de adiantamento do imposto a ser retido na apuração mensal;
3. Durante o processamento da folha normal, existem eventos que transitam na folha que proporcionalizam o cálculo de férias e estes compõe a base de INSS, juntamente com os eventos da folha;
4. O desconto de INSS prévio nas férias será proporcionalizado também e deduzido do valor final do INSS da folha;
5. Caso seja menor do que o devido é realizado o desconto da diferença em folha, do contrário é realizada a restituição.

---

### Emissão do Aviso de Férias

A geração do Aviso de Férias e do Recibo de Férias é controlada por dois parâmetros, configurados previamente na tela **Preferências** (Configurações > Avançado):

- **Aviso de Férias - FPRELATAVISOFER**;
- **Holerite de Férias - FPRELATRECFE**.

Cada um deles tem dois usos possíveis, e não devem ser misturados:

- Para usar o **relatório padrão** do sistema: deixe os parâmetros em branco, ou com o campo preenchido como 0.
- Para usar um **relatório personalizado**: informe o código do relatório personalizado correspondente, previamente cadastrado na tela **Relatórios Formatados** (Configurações > Avançado).

⚠️ Se um desses parâmetros ficar configurado com um código inválido, ou com um código quando deveria estar em branco (e vice-versa), o aviso ou o recibo pode ser gerado com dados incompletos, com valores em branco ("null"), ou o sistema pode não conseguir gerar o relatório. Esse é o motivo mais comum de erro na emissão do aviso e do recibo de férias; confira sempre esses dois parâmetros antes de investigar outras causas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/7091805775255-Como-calcular-f%C3%A9rias#top)
