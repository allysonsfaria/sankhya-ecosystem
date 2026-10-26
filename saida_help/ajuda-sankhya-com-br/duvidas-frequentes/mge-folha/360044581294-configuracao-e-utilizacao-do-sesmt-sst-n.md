---
id: "360044581294"
titulo: "Configuração e utilizaçao do SESMT / SST no MGEPessoal e impactos nos eventos do E-social"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044581294-Configura%C3%A7%C3%A3o-e-utiliza%C3%A7ao-do-SESMT-SST-no-MGEPessoal-e-impactos-nos-eventos-do-E-social"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:33:36Z"
rotulos: ["Segurança e Saúde no trabalho", "SST", "Configuração", "Eventos", "eSocial", "Integração eSocial MGE Pessoal", "Controle EPIs e EPCs", "Treinamento e Saúde Ocupacional", "MGE Pessoal", "SESMT"]
---

# Configuração e utilizaçao do SESMT / SST no MGEPessoal e impactos nos eventos do E-social

Antes de explicarmos o objetivo de cada tela, cabe esclarecer ao usuário que o MGE Pessoal acrescentou em suas rotinas as funcionalidades do SESMT exigidas pelo Esocial e em apoio às outras áreas do sistema que implicam no preenchimento dessas informações para envio ao eSocial. O sistema da Sankhya não possui um módulo próprio de SESMT, devendo o usuário utilizar no MGE Pessoal a rotina apenas como apoio e envio.

#### Fluxo das informações de Saúde e Segurança no Trabalho no eSocial

  

**TELA 1- MGE PESSOAL >> ROTINAS >> SESMT >> EQUIPAMENTOS DE PROTEÇÃO**

**Informações importantes:**

De acordo com a Norma Reguladora 6 - EQUIPAMENTO DE PROTEÇÃO INDIVIDUAL (206.000-0/I0) a empresa é obrigada a fornecer aos empregados equipamentos de proteção gratuitamente adequado ao risco e em perfeitas condições de funcionamento e conservação e cabe ao SESMT recomendar ao empregador o EPI adequado ao risco existente em determinada atividade.

A tela "Equipamento de Proteção" faz esse controle em relação aos EPI´s em conformidade com às determinações do Ministério do Trabalho.

**E-Social:**        Evento S-1060 Tabela de Ambientes de Trabalho:Evento utilizado para inclusão, alteração e exclusão de registros na Tabela de Ambientes de Trabalho do empregador/contribuinte/órgão público. As informações consolidadas desta tabela são utilizadas para validação do evento de Condições Ambientais do Trabalho. Devem ser informados os ambientes de trabalho da empresa em que há trabalhadores exercendo atividades.

**Pré-requisitos: envio do evento S-1000**        – Informações do Empregador/Contribuinte/Órgão Público, S-1005 – Tabela de Estabelecimentos, Obras ou Unidades de Órgãos Públicos e S-1020 – Tabela de Lotações Tributárias.

**E-Social:**        Evento S-1065 – Tabela de Equipamentos de Proteção: Serão descritos, para a criação de uma tabela a ser usada pelo empregador/contribuinte/órgão público em eventos posteriores, os Equipamentos de Proteção Coletiva (EPCs) instalados em cada estabelecimento e os Equipamentos de Proteção Individual (EPIs) utilizados pelos empregados, atribuindo-se um código a cada um deles. A criação da tabela evitará erros na descrição e permitirá maior consistência das informações a serem registradas nos eventos nos quais serão utilizadas.

**Pré-requisitos**       : envio do evento S-1000 – Informações do Empregador/Contribuinte/Órgão Público.

**Sistema: para preenchimento das informações o usuário deverá preencher:**    **Código**   : preenchido pelo sistema e identifica a informação no fluxo do sistema;

**Tipo de proteção**       : nesse local é definido se o equipamento e de uso Individual ou Coletivo;

**Descrição do equipamento**  : nome definido pela NR nro 6.

**Certificado de aprovação do EPI**  : informar o número do CA do equipamento.

Importância do CA : 6.2 da NR 6: O equipamento de proteção individual, de fabricação nacional ou importado, só poderá ser posto à venda ou utilizado com a indicação do Certificado de Aprovação - CA, expedido pelo órgão nacional competente em matéria de segurança e saúde no trabalho do Ministério do Trabalho e Emprego.

**Check list de conferência**       : marcações correspondentes a aplicação e eficácia do EPI dentro do contexto que ele será utilizado.

**TELA 2- MGE PESSOAL >> ROTINAS >> SESMT >> AMBIENTE DE TRABALHO**

**Para atender a geração do registro S-2240 no E-Social.**

**eSocial:Evento S-2240 – Condições Ambientais do Trabalho – Fatores de Risco**       : Serão prestadas as informações da exposição do trabalhador aos fatores de risco, conforme Tabela 23. A empresa deverá vincular os trabalhadores a cada ambiente em que exercem atividades (códigos do evento S-1060) e aos fatores de risco aos quais o trabalhador está exposto. Deverão também ser descritos os Equipamentos de Proteção Coletiva (EPCs) instalados e os Equipamentos de Proteção Individual (EPIs) utilizados, previamente cadastrados na Tabela S-1065. Para cada fator de risco informado o empregador/contribuinte/órgão público declarará se as exposições acarretam o direito ao pagamento dos adicionais de insalubridade, periculosidade ou se a exposição enseja o pagamento do adicional previsto na legislação para o custeio da aposentadoria especial.

Ressalta-se que os agentes químicos, físicos e biológicos listados na Tabela 23 estão sujeitos a avaliações quantitativas para mensuração de sua concentração ou intensidade. Entretanto, há que se destacar que, caso em determinado ambiente um agente não seja reconhecido como fator de risco (avaliação qualitativa) com probabilidade de dano à saúde do trabalhador, a avaliação quantitativa correspondente não será necessária. Por exemplo, setores de área administrativa que não possuem fontes geradoras de ruído excessivo, onde há reconhecimento apenas de ruído ambiente.

**Pré-requisitos:**        envio dos eventos S-2200 - Cadastramento Inicial do Vínculo e Admissão/Ingresso de Trabalhador, S-2300 - Trabalhadores Sem Vínculo Emprego/Estatutário – Início, o evento S- 1060

- Tabela de Ambientes de Trabalho e o evento S- 1065 - Tabela de Equipamentos de Proteção.

**Código**       : Gerado automaticamente pelo sistema a cada vez que um novo ambiente de trabalho e criado.

**Descrição**  : Descreva o nome do ambiente.

**Local**      : informe qual é o local, selecione uma das opções abaixo;

1- Estabelecimento do próprio empregador

2-Estabelecimento de Terceiros

3-Prestação de serviços em instalações de terceiros não consideradas como lotação

**Parceiro Tomador**  : Selecione o Parceiro tomador.

**Campo Estabelecimento de Terceiros não lotados na empresa;**

**Selecione o tipo de inscrição** (CNPJ,CAEPF,CNO)

**Informe a inscrição no campo .**

**Aba: Fatores de Risco**

  

**Código do Fator de Risco**       : Selecione o fator de risco desejado, caso necessário inserir este campo é alimentado pela tabela 23 das Tabelas Gerais para o E-Social (MGE Pessoal >> ARQUIVOS >> CADASTROS >> eSocial >> TABELAS GERAIS >> TABELA 23- FATORES DE RISCOS DO MEIO AMBIENTE DE TRABALHO).

**Intensidade ou concentração da exposição**  : Informar a intensidade ou concentração da exposição.

**Limite de Tolerância**  : Informe o limite de tolerância.

**Técnica Medicação da intensidade ou concentração**   : Informe a Técnica de Medição da intensidade ou concentração, campo pode ser preenchido com letras e números.

**Utilização de EPI**       : Selecione uma das opções, Não se aplica, Não Utilizado e Utilizado.

**Utilização de EPC**       : Selecione uma das opções, Não se aplica, Não Implementa e Implementa.

**Os EPCs são eficazes na neutralização dos riscos?**   : Selecione para sim e não selecione para não.

**Tipo de avaliação**   : Selecione 1-Critério quantitativo ou 2-Critério qualitativo.

**Unidade de medida intensidade ou concentração**   : Selecione uma da opções abaixo: 01 - Dose diária de ruído (número adimensional) Q=5

- Decibel linear (dB (linear))

- Decibel (C) (dB(C))

- Decibel (A) (dB(A))

- Quilocaloria por hora (kcal/h) 06 - Gray (Gy)

- Sievert (Sv)

- Quilograma-força por centímetro quadrado (kgf/cm2)       **Insalubridade**      :

Selecione para sim e não selecione para não.       **Periculosidade**      :

Selecione para sim e não selecione para não.       **Aposentadoria Especial**      :

Selecione para sim e não selecione para não.

**Sub Aba Equipamento de Proteção Individual**    - EPI (só habilita se na Aba Fatores de Risco o campo Utilização de EPI for selecionado Utilizado)

Código Equipamento: selecione um equipamento cadastrado em MGE PESSOAL >> ROTINAS >> SESMT >>EQUIPAMENTOS DE PROTEÇÃO

**Certificado de Aprovação**   : Campo preenchido automaticamente pelo código do equipamento cadastrado.

**Descrição do EPI**       : Campo preenchido automaticamente pelo código do equipamento cadastrado.

**É eficaz na neutralização do risco ao trabalhador**   : Campo preenchido automaticamente pelo código do equipamento cadastrado ou pode ser alterado de acordo com a necessidade.

**Foram implementadas medidas coletiva, optando-se pelo EPI por inviabilidade técnica, insuficiência ou interinidade?**   : Campo preenchido automaticamente pelo código do equipamento cadastrado ou pode ser alterado de acordo com a necessidade.

**Observadas condições de funcionamento ao longo do tempo?**   : Campo preenchido automaticamente pelo código do equipamento cadastrado ou pode ser alterado de acordo com a necessidade.

**Observado prazo de validade, conforme CA do MTE?**   : Campo preenchido automaticamente pelo código do equipamento cadastrado ou pode ser alterado de acordo com a necessidade.

**Observada a periodicidade de troca, comprovada mediante recibo assinado pelo usuário em época própria?**   : Campo preenchido automaticamente pelo código do equipamento cadastrado ou pode ser alterado de acordo com a necessidade.

**Observada a higienização?**       : Campo preenchido automaticamente pelo código do equipamento cadastrado ou pode ser alterado de acordo com a necessidade.

**Observado uso ininterrupto ao longo do tempo?**   : Campo preenchido automaticamente pelo código do equipamento cadastrado ou pode ser alterado de acordo com a necessidade.

**Aba: Atividade periculosa(s), insalubre(s) ou especial(is) desempenhada(s);**

Cód.Atividade: Selecione a atividade desejada, caso necessário inserir este campo é alimentado pela tabela 28 das Tabelas Gerais para o E-Social. (MGE Pessoal >> ARQUIVOS >> CADASTROS >> ESOCIAL >> TABELAS GERAIS >> TABELA 28-ATIVIDADES PERICULOSAS, INSALUBRES E/ OU ESPECIAIS).

**Descrição**      : Preenchido automaticamente pelo Cód.Atividade.

**Aba: Profissionais responsáveis;**

**CPF Responsável**  : Informe o CPF do responsável.

**NIS Responsável**  : Informe o NIS do responsável.

**Nome do Responsável**  : Informe o nome do responsável.

**Órgão de Classe**       : Selecione a Classe do responsável, 1 - Conselho Regional de Medicina (CRM), 2 - Conselho Regional de Engenharia e Agronomia (CREA) ou 9 - Outros.

**Descrição do Órgão de Classe:**   Informe a descrição da Classe caso seja outros.

**Inscrição no Órgão de Classe:**   Informe a inscrição do Órgão de Classe.

**UF do Órgão de Classe**  : Selecione a Unidade Federativa do Órgão de Classe.

**Aba: Descrição das Atividades desempenhadas;**

Descreva a atividade.

**Aba: Metodologia utilizada para o levantamento dos riscos ergonômicos;**

Descreva toda a Metodologia utilizada para o levantamento dos riscos ergonômicos.

**Aba: Observação(ões) complementar(es) a registros ambientais;**

Descreva Observação(ões) complementar(es) a registros ambientais se necessário.

**TELA 3- MGE PESSOAL >> ROTINAS >> SESMT >> TREINAMENTO E CAPACITAÇÃO eSocial:**

**Evento S-2245 – Treinamentos e Capacitações:**        Serão prestadas informações sobre os treinamentos, capacitações, exercícios simulados realizados, bem como informações aos trabalhadores relativas a segurança e saúde no trabalho, conforme Tabela 29. Para facilitar a identificação da referência normativa, os dois primeiros dígitos do código correspondente se referem à Norma Regulamentadora que dispõe sobre a realização do treinamento, capacitação, exercício simulado ou informações aos trabalhadores.

MGE - Treinamento-Capacitação: tela de treinamento para atender a geração do registro S-2245 no eSocial.

**Número único treinamento**   : Número único treinamento, código de identificação do treinamento.

**Código de Treinamento/Capacitação no eSocial**   : Selecione o Treinamento desejado caso necessário inserir este campo é alimentado pela tabela 29 das Tabelas Gerais para o eSocial.

**Modalidade**      : Escolha uma das opções conforme abaixo;

1-Presencial

2-Educação a distância (EAD)

3-Mista

**Tipo**      : Escolha uma das opções conforme o tipo do exame abaixo;

1-inicial

2-Periódico

3-Reciclagem

4-Eventual

5-Outros

**Data início treinamento**  : A data inicial do treinamento.

**Duração em horas**  : O tempo de treinamento.

**Observação**       : Informar qualquer observação a ser feita, exemplo: Treinamento membros da CIPA.

**Aba: Funcionários;**

Informar o Funcionário selecionando: Cód.Empresa, Cód.Funcionário e o campo Nome Funcionário será preenchido.

**Aba: Profissionais responsáveis;**

Preencher os dados do profissional responsável pelo Exame com os dados abaixo;

CPF profissional, Nome, Tipo, Matricula, Formação do Profissional e CBO(Classificação Brasileira de Ocupações).

**TELA 4 - MGE PESSOAL >> ROTINAS >> SESMT >> ASO - ATESTADO DE SAÚDE OCUPACIONAL**

**Esocial: Evento S-2220 – Monitoramento da Saúde do Trabalhador e Exame Toxicológico:**        neste evento será feito o acompanhamento da saúde do trabalhador durante o seu contrato de trabalho, com as informações relativas aos atestados de saúde ocupacional (ASO) e seus exames complementares. Tais informações correspondem àquelas exigidas no Perfil Profissiográfico Previdenciário – PPP e no Programa de Controle Médico e Saúde Ocupacional (PCMSO). Também serão prestadas neste mesmo evento as informações do exame toxicológico obrigatório para o motorista profissional.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044581294-Configura%C3%A7%C3%A3o-e-utiliza%C3%A7ao-do-SESMT-SST-no-MGEPessoal-e-impactos-nos-eventos-do-E-social#top)

**Campos exigidos pelo eSocial:**

**Empresa:**        Informe a qual empresa pertence o funcionário do exame a ser inserido, após salvar esse campo não permitirá mais alterações.

**Funcionário:**        Informe o funcionário que realizou o exame, após salvar esse campo não permitirá mais alterações.

**Tipo de Exame:**       Selecione qual dos exames abaixo o funcionário realizou;

0 - Exame médico ocupacional

1 - Exame toxicológico do motorista profissional

**Data do Vencimento**       : Informar qual a data de vencimento, para que o funcionário realize o novo exame.

**Data de realização:**   Informar a data de realização do exame.

**Tipo de ASO:**   Selecione uma das opções abaixo;

- Admissional
- Periódico (PCMSO)
- Retorno ao trabalho
- Mudança de função
- Monitorização pontual
- Demissional

**Resultado do ASO;**   Selecione o resultado do ASO conforme opções abaixo;

- Sem resultado
- Apto
- Apto c/ restrições
- Inapto

**Unidade de atendimento:**   Informar as opções do campo,   **código CNES**   ("O Cadastro Nacional de Estabelecimentos de Saúde"),   **Forma de contato**   e   **E-mail**  .

**Médico Responsável**  : Informar as opções do campo,   **Nome**  ,   **Telefone**  ,   **CRM**   ("Conselho Regional de  Medicina"),   **UFU CRM**  ,   **CPF**   e   **NIS**  .

**Médico Responsável pela monitorização**  : Informar as opções do campo,   **Nome**  ,   **Telefone**  ,   **CRM**

("Conselho Regional de Medicina"),   **UFU CRM**  ,   **CPF**   e   **NIS**

**Aba Exames realizados**       ; Traz o histórico de todos o exames cadastrados dá ASO em questão referenciada no Código no início da tela.

Para cadastro do exame realizado, o usuário deverá preencher os seguintes campos:

**Data realização**  : informe a data de realização do exame;   **Descrição do exame**  : informe qual exame o funcionário realizou;   **Código do Exame**  : código do exame gerado pelo sistema;

**Vencimento Exame em dias:**    quando o exame irá vencer, preenchimento automático do sistema;

**Data Vencimento:**   preenchimento automático pelo sistema;

**CRM do responsável:**   número do registro do médico responsável;   **UF do CRM:**   Estado do registro do médico responsável;   **Toxicológico?:**   se for toxicológico, marcar o campo;

**CNPJ do Laboratório**  : campo autoexplicativo.

**Cod. Exame Esocial:**   informe o código do evento conforme tabela do Esocial;

**Descrição do exame Esocial:**    informando o código do exame esse campo é preenchido automaticamente;

**Ordem do Exame:**   informar se o exame é inicial ou sequencial;

**Indicação de Resultados:**    indicar no campo o resultado do exame: 1-normal, 2- alterado, 3- estável, e 4- agravamento;

**Nome do Médico:**   informar o nome do médico responsável pelo exame;

**Atenção**: Os campos da grade por conterem       **Data**       serão armazenados e pode-se considerar que haverá um       **Histórico**       , entretanto, as informações da parte superior desta tela, inicialmente,       **não**      **registrará**    cada ASO realizado no Banco de Dados, essa necessidade será analisada em outros leiautes relacionados à   **CAT**   e   **Afastamento Temporário**  .

**Observação:** Filtro na tela com a opções de : Empresa e Funcionário

**Inserção automática**        de um novo registro ao realizar a criação de um ASO como: Campo Tipo ASO igual a :

- Admissional: deverá ser realizada antes que o trabalhador assuma suas atividades;
- Periódico (PCMSO): de acordo com os intervalos mínimos de tempo abaixo discriminados:
- a)-para trabalhadores expostos a riscos ou a situações de trabalho que impliquem o desencadeamento ou agravamento de doença ocupacional, ou, ainda, para aqueles que sejam portadores de doenças crônicas, os exames deverão ser repetidos:
- a1)-a cada ano ou a intervalos menores, a critério do médico encarregado, ou se notificado pelo médico agente da inspeção do trabalho, ou, ainda, como resultado de negociação coletiva de trabalho;
- a2)-de acordo com à periodicidade especificada no Anexo n.º 6 da NR 15, para os trabalhadores expostos a condições hiperbáricas;
- b)-para os demais trabalhadores:
- b1)-anual, quando menores de 18 (dezoito) anos e maiores de 45 (quarenta e cinco) anos de idade;
- b2)-a cada dois anos, para os trabalhadores entre 18 (dezoito) anos e 45 (quarenta e cinco) anos de idade.
- Retorno ao Trabalho:deverá ser realizada obrigatoriamente no primeiro dia da volta ao trabalho de trabalhador ausente por período igual ou superior a 30 (trinta) dias por motivo de doença ou acidente, de natureza ocupacional ou não, ou parto.
- Mudança de Função: era obrigatoriamente realizada antes da data da mudança.
- Demissional: no exame médico demissional, será obrigatoriamente realizada em até 10 (dez) dias contados a partir do término do contrato, desde que o último exame médico ocupacional tenha sido realizado há mais de: 135 (cento e trinta e cinco) dias para as empresas de grau de risco 1 e 2, segundo o Quadro I da NR 4;90 (noventa) dias para as empresas de grau de risco 3 e 4, segundo o Quadro I da NR 4.7.4.3.5. No exame médico demissional, será obrigatoriamente realizada até a data da homologação, desde que o último exame médico ocupacional tenha sido realizado há mais de: 135 (cento e trinta e cinco) dias para as empresas de grau de risco 1 e 2, segundo o Quadro I da NR 4;90 (noventa) dias para as empresas de grau de risco 3 e 4, segundo o Quadro I da NR 4.
- Monitorização pontual: quando não se encaixa nos casos acima.

Campo Resultado do ASO igual a:       **Apto**

Caso esses campos ao salvar estejam selecionados, o sistema irá criar um novo registrando copiando as informações dos campos:

➔    Empresa

➔    Funcionário

➔    Tipo do Exame

➔    Data do Vencimento

➔    Tipo ASO

➔    Resultado do ASO

Para os campos, Data do Vencimento o valor do novo registro será de um ano a mais da data de vencimento do antigo ASO, e alterar o campo Resultado do ASO para "Sem Resultado", para ser possível visualizar os ASOs que estão a vencer perto do período da data de vencimento.

**TELA 5- MGE PESSOAL >> ROTINAS >> SESMT >> CAT- COMUNICAÇÃO DE ACIDENTE DE TRABALHO**

**Aba: Informações Gerais do CAT**

Selecione o   **TIPO de CAT**   conforme sua categoria;

- Inicial
- Reabertura
- Comunicação de Óbito

**CAT inicial:**        irá se referir a acidente de trabalho típico, trajeto, doença profissional, do trabalho ou óbito imediato;

**CAT de reabertura:**        será utilizada para casos de afastamento por agravamento de lesão de acidente do trabalho ou de doença profissional ou do trabalho;

**CAT de comunicação de óbito:**        será emitida exclusivamente para casos de falecimento decorrente de acidente ou doença profissional ou do trabalho, após o registro da CAT inicial;

**CAT de reabertura:**        deverão constar as mesmas informações da época do acidente, exceto quanto ao afastamento, último dia trabalhado, atestado médico e data da emissão, que serão relativos à data da reabertura. Não será considerada CAT de reabertura a situação de simples assistência médica ou de afastamento com menos de 15 dias consecutivos.

Fonte: INSS

Indique o   **Emitente**  ;

- Empregador
- Sindicato trb.avulso nao portuarios
- Médico assistente
- Empregado
- Autoridade Pública
- Cooperativa
- Órgão Gestor de Mão de Obra
- Entidade Sindical competente
- Dependente do Empregado

Informe a   **Data da CAT**

Informe o   **Número da CAT**

**CAT PArcial?**   selecione se for o caso.

**Houve Óbito?**   selecione se for o caso.

**Houve Comunicação Policial?**   selecione se for o caso.

Selecione o   **Tipo do Acidente**  ;

- Típico
- Doença
- Trajeto

**Acidente de trabalho ou de trajeto**       : é o acidente ocorrido no exercício da atividade profissional a serviço da empresa ou no deslocamento residência / trabalho / residência, e que provoque lesão corporal ou perturbação funcional que cause a perda ou redução – permanente ou temporária – da capacidade para o trabalho ou, em último caso, a morte;

**Doença ocupacional:**        é aquela produzida ou desencadeada pelo exercício do trabalho peculiar a determinada atividade e constante da respectiva relação elaborada pelo Ministério do Trabalho e da Previdência Social.

Fonte: INSS

Informe a   **Data do acidente**  ,   **Hora do acidente**   e   **Horas Trabalhadas**   de acordo com a CAT.

Selecione a   **Situação Geradora do acidente**   , se não cadastrada a situação pode ser cadastrada conforme caminho abaixo;

Arquivos >> Cadastros >> E-social >>Tabelas gerais >>   **16 - Situação Geradora do acidente**

Selecione o   **Tipo de Acidente de Trabalho**   , se não cadastrada a situação pode ser cadastrada conforme caminho abaixo;

Arquivos >> Cadastros >> E-social >> Tabelas gerais >>   **24 - Codificação de Tipo de Acidente de Trabalho**

Selecione o   **Registrador da CAT**  ;

- CPF
- CNPJ

Selecione a   **Emissão da CAT**  ;

- iniciativa do empregador
- Ordem judicial

Determinação de órgão fiscalizador Caso tenha informe       **Observações**      :

**Aba: Local do Acidente;**

Indicar o   **Tipo de Local**  ;

- Estabelecimento do empregador no Brasil.
- Estabelecimento de terceiros onde o empregador
- Via pública
- Área rural
- Embarcação
- Estabelecimento do empregador no Exterior
- Outros

Preencher manualmente os campos abaixo;

➔    Especificação do local

➔    CEP

➔    Endereço

➔    Cidade

➔    Complemento

➔    Bairro

➔    Código Postal

➔    Data do Óbito

**Aba: Partes do corpo Atingidas;**

Informar qual a       **Parte do corpo**        atingida, caso não cadastrado pode ser adicionado na tabela conforme caminho abaixo;

Arquivos >> Cadastros >> eSocial >> Tabelas gerais >>   **13 - Parte do Corpo Aba Agentes causadores;**

Informar qual foi o agente causador da CAT, caso o agente não esteja cadastrado, o agente tem que ser cadastrado na tabela conforme caminho abaixo;

Arquivos >> Cadastros >> eSocial >> Tabelas gerais >> 14 - Agente Causador Acidente Trabalho

**Aba: Testemunha;**

Adicionar se necessário com os dados da testemunha como   **nome, Endereço, Numero Endereço, Bairro, Cidade, CEP**   e   **Telefone**  .

Aba Atestado Médico;

Esta aba é para informar os dados do atestado com as informações conforme abaixo;

- Código da Unidade de Atendimento
- Data do Atendimento
- Hora do Atendimento
- Houve Internação?
- Duração do tratamento (dias)
- Houve afastamento?
- Descrição da lesão (opção selecionável)
- Descrição complementar / natureza da lesão
- Diagnóstico provável
- CID(CÓDIGO DE IDENTIFICAÇÃO DA DOENÇA)
- Observações
- Emitente que contém a identificação do emitente da CAT

**OBJETIVO PARA O ESOCIAL- COMUNICAÇÃO DOS DADOS**

**SIGLAS E SIGNIFICADOS**

- **MGE PESSOAL**       : módulo do sistema Sankhya responsável por gerenciar as informações referente ao departamento pessoal, com exceção das rotinas completas da Medicina e Segurança do Trabalho.
- **Exame Clínico**       : exames obrigatórios determinados pela NR nº 7 relacionados ao PCMSO;

a) avaliação clínica, abrangendo anamnese ocupacional e exame físico e mental;

b) exames complementares, realizados de acordo com os termos específicos nesta NR e seus anexos.

- **Exame Toxicológico**   : exame obrigatório para motorista profissional, conforme art. 168, III, § 6o, da CLT “   serão exigidos exames toxicológicos, previamente à admissão e por ocasião do desligamento, quando se tratar de motorista profissional, assegurados o direito à contraprova em caso de resultado positivo e a confidencialidade dos resultados dos respectivos exames  ”.
- **PCMSO**       : Programa de Controle Médico de Saúde Ocupacional. (NR nº07)
- **PPRA**      : Programa de Prevenção de Riscos Ambientais (NR nº09)
- **PPP**       : Perfil Profissiográfico Previdenciário (§ 4º do art. 58 da Lei 8.213/91)
- **SESMT**       - Serviços Especializados em Engenharia de Segurança e em Medicina do Trabalho.( NR nº 04)
- **ASO**       - Atestado de Saúde Ocupacional (NR nº 07)
- **CAT**      - Comunicação de Acidente de Trabalho
- **e-Social**       - Sistema de Escrituração Digital das Obrigações Fiscais, Previdenciárias e Trabalhistas (Decreto nº 8373/2014)

                                                                                                                                                                    [[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044581294-Configura%C3%A7%C3%A3o-e-utiliza%C3%A7ao-do-SESMT-SST-no-MGEPessoal-e-impactos-nos-eventos-do-E-social#top)
