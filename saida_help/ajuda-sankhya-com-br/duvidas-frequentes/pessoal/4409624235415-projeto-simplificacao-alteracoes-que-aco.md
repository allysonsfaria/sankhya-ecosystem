---
id: "4409624235415"
titulo: "Projeto  Simplificação - Alterações que aconteceram no Pessoal+, Pessoal/G e SaneSocial"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4409624235415-Projeto-Simplifica%C3%A7%C3%A3o-Altera%C3%A7%C3%B5es-que-aconteceram-no-Pessoal-Pessoal-G-e-SaneSocial"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-07-29T13:29:37Z"
rotulos: ["Configuração", "Atualização", "#validadoRayssa", "eSocial", "Atualizações no Sistema de Folha de Pagamento eSocial Simplificado", "Pessoal+", "Pessoal/G", "Sanesocial"]
---

# Projeto  Simplificação - Alterações que aconteceram no Pessoal+, Pessoal/G e SaneSocial

#### Requisitos mínimos:

**Versão banco de dados:** 4.40.0.21

**Versão executável:** 4.40.0.21

**Versão Do Sanesocail:** 3.0b1218

**Script do SanEsocial:** Atualizado

### Imagem 1: Introdução Introdução

Conforme publicada na Portaria Conjunta SEPRT/RFB nº 82, foi aprovado o layout  final do eSocial Simplificado, versão S-1.0. O eSocial Simplificado foi previsto na Lei nº 13.874/19.

Os prazos para entrada em vigor de cada fase e da versão Simplificada estão na Portaria Conjunta SEPRT/RFB/ME Nº 71, de 06/2021 e Notas Orientativas e Técnicas.

Houve redução em mais de 30% do número de campos dos layout  do eSocial, o que inclui a simplificação de vários eventos e a exclusão total de 12 eventos transmitidos/a transmitir pelas empresas.

### Detalhamento do que foi criado no Pessoal/G e Pessoal+ por evento

#### Caminhos para o módulo Pessoal+/W

Pessoal+ » Rotinas Folha » SESMT » Treinamento e Capacitação

Pessoal+ » Rotinas Folha » SESMT » Equipamentos de Proteção

Pessoal+ » Rotinas Folha » SESMT » Ambiente de Trabalho

Pessoal+ » Cadastros » Atestado de Saúde Ocupacional (ASO)

Pessoal+ » Rotinas Folha » SESMT » CAT - Comunicação de Acidente de Trabalho

![Imagem 2: Pessoal+ » Rotinas Folha » SESMT » CAT - Comunicação de Acidente de Trabalho](https://ajuda.sankhya.com.br/hc/article_attachments/4409707618199)

#### Caminhos para o módulo Pessoal/G

Rotinas » SESMT » Treinamento e Capacitação

Rotinas » SESMT » Equipamentos de Proteção

Rotinas » SESMT » Ambiente de Trabalho

Rotinas » SESMT » Atestado de Saúde Ocupacional (ASO)

Rotinas » SESMT » CAT - Comunicação de Acidente de Trabalho

![Imagem 3: Rotinas » SESMT » CAT - Comunicação de Acidente de Trabalho](https://ajuda.sankhya.com.br/hc/article_attachments/16083505942295)

###

#### S-1005 - Tabela de Estabelecimentos, Obras ou Unidades de Órgãos Públicos:

**(1)**A tela **Processos >> Propriedades >> Tipo**, sofreu alteração no grupo “Tipo”, a descrição que antes estava como “Processo FAP” passou para “4 - Processo FAP de exercício anterior a 2019”;

**(1)**O grupo de Informações de apuração da alíquota GILRAT do estabelecimento alterou o comportamento de envio das informações relativas a alíquota RAT e Fator Acidentário de Prevenção - FAP. Elas apenas serão enviadas quando forem divergentes da legislação para a atividade (CNAE) preponderante. Ressaltamos que neste deve existir um evento S-1070 com o respectivo processo.

#### S-1010 - Tabela de Rubricas:

**(1)**No grupo Detalhamento das informações da rubrica, algumas opções não estão mais disponíveis para escolha das incidências em INSS e IRRF; 

**Código de incidência tributária da rubrica para a Previdência Social:**

Na tela **Eventos >> Incidência >> E-Social >>** Incidência p/ Previdência não estarão mais disponíveis as opções:

- 23 - Auxílio doença mensal - Regime Próprio de Previdência Social;
- 24 - Auxílio doença 13o salário doença - Regime próprio de previdência social;
- 61 - Complemento de salário-mínimo - Regime próprio de previdência social

Se um dos clientes estiver usando uma destas opções, quando o usuário acessar a tela de Eventos será emitida uma mensagem, alertando o usuário de uma possível revisão;

**Código de incidência tributária da rubrica para o Imposto de Renda Retido na Fonte - IRRF:**

Na tela **Eventos >> Incidência >> E-Social >> Incidência p/ IRRF** não estarão mais disponíveis as opções:

- 91 - Remuneração mensal;
- 92 - 13º salário;
- 93 - Férias;
- 94 - PLR;
- 95 - RRA;

Se um dos clientes estiverem usando uma destas opções, quando o usuário acessar a tela de **"Eventos"** será emitida uma mensagem, alertando o usuário de uma possível revisão;

As incidências foram reestruturadas e o eSocial disponibilizou a tabela 21 - Códigos de Incidência Tributária da Rubrica para o IRRF. Estas informações estão disponíveis na tela **Arquivos >> Eventos >> Incidência >> E-Social >> Incidência p/ IRR**F. Ela manteve boa parte das opções anteriores, mas passou por mudanças;

Houve alterações em três códigos de incidência da rubrica para o Fundo de Garantia do Tempo de Serviço - FGTS:

Alteradas as descrições:

11 - Base de cálculo do FGTS mensal,

21 - Base de cálculo do FGTS aviso prévio indenizado

91 - Incidência suspensa em decorrência de decisão judicial - FGTS mensal;

**Novos códigos:**

92 - Incidência suspensa em decorrência de decisão judicial  FGTS 13º salário

d93 - Incidência suspensa em decorrência de decisão judicial - FGTS aviso prévio indenizado;

#### S-1070 - Tabela de Processos Administrativos/Judiciais:

**(1)**A tela de Processos passou por mudanças bem significativas e que terão impacto no envio de processos ao ambiente do eSocial;

**(1)**No grupo de Identificação do processo e período de validade das informações: 

**(2)** O campo que retorna com o código correspondente ao tipo de processo não será mais enviada a opção “Tipo: 3 - Número de Benefícios (NB) do INSS”, apesar de continuar em tela ela não será mais enviada ao eSocial. Teremos uma mensagem orientando a este respeito.

**(2)**O número do processo administrativo/judicial passou a ter mais opções de tamanho e que variam conforme o tipo do Processo. Ele agora aceita valores de 10, 16, 17, 20 ou 21;

**(1)**O grupo responsável por determinar os Dados do Processo, passou por uma reformulação, no que diz respeito ao Indicativo da Matéria do Processo. Basicamente ele ficou restrito a matérias Tributárias e de Contribuições;

O grupo responsável por determinar os Dados do Processo, passou por uma reformulação, no que diz respeito ao Indicativo da Matéria do Processo.
Basicamente ele ficou restrito a matérias Tributárias e de Contribuições;

Na tela Processos >> Propriedades >> Matéria do Processo ou Alvará Judicial (E-Social) , não estarão mais disponíveis as opções abaixo:

2 - Autorização de trabalho de menor;
3 - Dispensa, ainda que parcial, de contratação de pessoa com deficiência (PCD);
4 - Dispensa, ainda que parcial, de contratação de aprendiz;
5 - Segurança e Saúde no Trabalho;
6 - Conversão de Licença Saúde em Acidente de Trabalho;
8 - Contribuição sindical;
99 - Outros assuntos

**(1)**Estas opções não estão mais disponíveis e possuem correspondência com o campo **“Identificação do Processo”**. Caso o cliente tenha esses processos e tenha a intenção de mantê-los no sistema, o cadastro passa para este local;

**(1)**Para viabilizar a permanência de Processos que não serão mais enviados, criamos no campo **“Matéria do Processo ou Alvará Judicial (E-Social):”** a opção **“Não se aplica”**. Ela será marcada automaticamente quando o campo Identificação do processo, for uma das opções descritas acima.

#### S-2190 - Registro Preliminar de Trabalhador:

**(1)**Será possível enviar este evento para os casos em que a Categoria do eSocial do Funcionário, esteja dentro dos códigos 201, 202, 308, 401, 410, 701, 711, 712, 721, 722, 723, 731, 734, 738, 741, 761, 771, 901, 902, 903, 904 e 905 a partir desta versão simplificada;

###

#### S-2240 - Condições Ambientais do Trabalho - Agentes Nocivos:

**(1)**Para o grupo Informações sobre o ambiente de trabalho, atividades desempenhadas e exposição a agentes nocivos, a Data de Início da Condição corresponde a data em que o trabalhador iniciou as atividades nas condições descritas, deve ser uma data igual ou posterior à data de admissão do vínculo a que se refere. Ela não pode ser posterior a 30 (trinta) dias da data atual no momento do envio do evento ao eSocial.

#### S-2298 - Reintegração/Outros Provimentos:

**(1)**O grupo Informações da reintegração, a data do efetivo retorno ao trabalho não  pode ser posterior a 30 (trinta) dias da data atual no momento do envio do evento ao eSocial.

#### S-2299 - Desligamento:

**(1)**Informações relativas ao desligamento do vínculo

**(2)**Os Códigos Motivos 11, 12, 13, 15, 16, 18, 26, 28, 30, 31 e 35 não podem ser usados com a Categoria igual a 104;

**(2)**Os Códigos Motivos 19, 20, 22, 25 e 29 são compatíveis apenas com as Categorias iguais a 301, 302, 303, 306, 307 e 309;

**(2)**Os Códigos Motivos 23 e 24, são compatíveis com as Categorias iguais a 301, 302, 303, 306, 307, 309, 310 e 312;

**(2)**O Código Motivo igual a 33, é compatível com a Categoria igual a 307;

**(2)**O Código Motivo igual a 34, é  compatível com a Categoria igual a 104;

**(2)**O Código Motivo igual a 37, é compatível com as Categorias iguais a 301, 306, 307 e 309;

**(2)**O Código Motivo igual a 38, é compatível com as Categorias iguais a 101, 301, 302 e 312;

**(2)**O Código Motivo igual a 39, é compatível com as Categorias iguais a 301, 306 e 309;

**(2)**O Código Motivo igual a 40, é compatível com a Categoria igual a 303;

**(2)**Código Motivo igual a 41 e 42, são compatíveis com a Categoria igual a 103;

**(2)**O Código do motivo de desligamento (Tabela 19 - Motivos de Desligamento do eSocial), a partir desta versão passou a validar o Motivo com a Categoria do eSocial (Cadastro do Funcionário). Fizemos as mesmas validações na tela de Cálculo de Rescisão para evitar o envio de eventos que não serão aceitos pelo ambiente do eSocial. Outros motivos que não foram mencionados são compatíveis com todas as categorias.

### Detalhamento das criações e alterações nas Tabelas de Cadastro SaneSocial:

#### Tabela 01 -  Categorias de Trabalhadores (TFPCTG):

**(1)Inclusões: códigos || Descrição**

**(2)**304 || Servidor público exercente de mandato eletivo, inclusive com exercício de cargo em comissão;

**(2)**310 || Servidor público eventual;

**(2)**311 || Ministros, juízes, procuradores, promotores ou oficiais de justiça à disposição da Justiça Eleitoral;

**(2)**312 || Auxiliar local;

**(2)**313 || Servidor público exercente de atividade de instrutoria, capacitação, treinamento, curso ou concurso, ou convocado para pareceres técnicos ou depoimentos;

**(1)Alteração de Descrição: códigos || Descrição**

**(2)**303 || Exercente de mandato eletivo;

**(2)**306 || Servidor público contratado por tempo determinado, sujeito a regime administrativo especial definido em lei própria;

**(2)**307 || Militar;

**(2)**410 || Trabalhador cedido/exercício em outro órgão/juiz auxiliar - Informação prestada pelo cessionário/destino;

#### Tabela 03 - Natureza das Rubricas da Folha de Pagamento (TFPRUB):

(1)**Inclusões: códigos || Nome || Descrição**

**(2)**1001 || Subsídio || Corresponde à remuneração paga na forma de subsídio;

**(2)**1216 || Adicional de localidade || Adicional pela realização de atividade em localidade transfronteiriços;

**(2)**1217 || Gratificação de curso/concurso || Verba de natureza remuneratória por atividade exercida em curso/concurso;

**(2)**1411 || Auxílio-natalidade || Valor relativo ao nascimento do filho de servidor público, previsto em lei;

**(2)**1412 || Abono permanência || Valor relativo ao abono de permanência, de acordo com a CF/1988;

**(2)**1800 || Alimentação concedida em pecúnia || Alimentação concedida sob a forma de pecúnia;

**(2)**1806 || Alimentação em ticket ou cartão, vinculada ao PAT || Alimentação concedida sob a forma de ticket ou cartão, por empresa vinculada ao Programa de Alimentação do Trabalhador PAT;

**(2)**1807 || Alimentação em ticket ou cartão, não vinculada ao PAT || Alimentação concedida sob a forma de ticket ou cartão, por empresa não vinculada ao PAT;

**(2)**1808 || Cesta básica ou refeição, vinculada ao PAT || Alimentação concedida sob a forma de cesta básica ou refeição, por empresa vinculada ao PAT;

**(2)**1809 || Cesta básica ou refeição, não vinculada ao PAT || Alimentação concedida sob a forma de cesta básica ou refeição, por empresa não vinculada ao PAT;

**(2)**1899 || Outros auxílios || Valores relativos a outros auxílios não previstos nos demais itens;

**(2)**3510 || Gratificação (jeton) || Valor correspondente a gratificação (jeton) por comparecimento a sessões ou reuniões;

**(2)**3511 || Gratificação eleitoral || Valor correspondente ao exercício da atividade pelo juiz eleitoral;

**(2)**4011 || Complemento de saláriomínimo RPPS || Valor correspondente à diferença entre o salário||mínimo e o valor do vencimento do cargo efetivo pago a servidor público vinculado a Regime Próprio de Previdência Social || RPPS;

**(2)**7006 || Auxílio-reclusão - Valor de auxílio || reclusão para o servidor público de baixa renda;

**(2)**7007 || Pensões especiais || Valor das pensões de caráter especial diferentes de pensão por morte;

**(2)**7008 || Complementação de aposentadoria/pensão || Valor relativo à complementação de aposentadoria/pensão vinculada ao Regime Geral de Previdência Social - RGPS;

**(2)**9202 || Contribuição militar || Desconto relativo à seguridade do militar e seus dependentes;

**(2)**9207 || Faltas || Desconto decorrente de ausência de trabalho durante todo o dia em razão de, por exemplo, falta injustificada, suspensão disciplinar, greve;

**(2)**9208 || Atrasos || Desconto decorrente de ausência de trabalho em razão de, por exemplo, atrasos no início da jornada de trabalho ou de saída antecipada do trabalhador;

**(2)**9211 || DSR sobre faltas || Desconto correspondente ao Descanso Semanal Remunerado - DSR, calculado sobre faltas do trabalhador;

**(2)**9212 || DSR sobre atrasos || Desconto correspondente ao Descanso Semanal Remunerado - DSR, calculado sobre atrasos do trabalhador;

**(2)**9240 || Alimentação concedida em pecúnia - Desconto || Desconto referente à alimentação concedida sob a forma de pecúnia;

**(2)**9241 || Alimentação em ticket ou cartão, vinculada ao PAT - Desconto || Desconto referente à participação do trabalhador no custo de alimentação concedida sob a forma de ticket ou cartão, por empresa vinculada ao Programa de Alimentação do Trabalhador - PAT;

**(2)**9242 || Alimentação em ticket ou cartão, não vinculada ao PAT - Desconto || Desconto referente à participação do trabalhador no custo de alimentação concedida sob a forma de ticket ou cartão, por empresa não vinculada ao PAT;

**(2)**9243 || Cesta básica ou refeição, vinculada ao PAT - Desconto || Desconto referente à participação do trabalhador no custo de alimentação concedida sob a forma de cesta básica ou refeição, por empresa vinculada ao PAT;

**(2)**9244 || Cesta básica ou refeição, não vinculada ao PAT - Desconto || Desconto referente à participação do trabalhador no custo de alimentação concedida sob a forma de cesta básica ou refeição, por empresa não vinculada ao PAT;

**(2)**9291 || Abate||teto || Valor deduzido da remuneração total do segurado que supere o teto remuneratório constitucional;

**(2)**9292 || Ressarcimento ao erário || Valor deduzido da remuneração para pagamento de ressarcimento ou de penalidade;

**(2)**9293 || Honorários advocatícios || Valor descontado do trabalhador por determinação judicial a ser pago ao advogado/escritório de advocacia;

**(2)**9294 || Redutor EC 41/03 || Valor descontado da remuneração do instituidor da pensão (Emenda Constitucional 41/2003);

**(2)**9907 || Total da contribuição da previdenciária patronal - RPPS || Valor total da contribuição previdenciária patronal para o RPPS (normal, suplementar e aportes);

(1)**Alterações de conteúdo: códigos || Nome || Descrição**

**(2)**1000 || Salário, vencimento, soldo || Correspondente ao salário básico contratual do empregado contratado de acordo com a CLT e o vencimento mensal do servidor público e do militar;

**(2)**1099 || Outras verbas salariais || Outras verbas salariais não previstas nos demais itens;

**(2)**1299 || Outros adicionais || Valores relativos a outros adicionais não previstos nos demais itens;

**(2)**1619 || Ajuda compensatória - Lei 14.020/2020 || Ajuda compensatória paga pelo empregador ao empregado durante período de suspensão do contrato de trabalho ou redução proporcional de salário e jornada, nos termos da Lei 14.020/2020 (conversão da MP 936/2020);

**(2)**1629 || Ressarcimento de outras despesas || Ressarcimento de outras despesas pagas pelo trabalhador, não previstas nos demais itens;

**(2)**6119 || Indenização rescisória - Lei 14.020/2020 || Indenização pela dispensa sem justa causa que ocorrer durante o período de garantia provisória no emprego de que trata o art. 10 da Lei 14.020/2020 (conversão da MP 936/2020);

**(2)**6129 || Outras multas ou indenizações || Valor correspondente a outras multas ou indenizações previstas em leis ou em Instrumentos Coletivos de Trabalho, exceto as previstas nos demais itens;

**(2)**7001 || Proventos || Valor dos proventos de Aposentadoria a servidor público;

**(2)**7002 || Proventos - Pensão por morte Civil || Valor dos proventos por morte a beneficiário de servidor público;

**(2)**9230 || Contribuição sindical laboral || Valor correspondente ao desconto da contribuição laboral correspondente a um dia de trabalho a título de contribuição sindical;

**(2)**9299 || Outros descontos || Outros descontos não previstos nos demais itens;

**(2)**9930 || Salário-maternidade pago pela Previdência Social || Valor correspondente à remuneração mensal do(a) trabalhador(a) durante a licença maternidade, quando paga pela Previdência Social (RGPS ou pela Unidade Gestora do RPPS);

**(2)**9931 || Salário-maternidade pago pela Previdência Social - 13° salário || Valor correspondente ao 13° salário do(a) trabalhador(a) durante a licença maternidade, quando pago pela Previdência Social (RGPS ou pela Unidade Gestora do RPPS);

**(2)**Teremos uma validação e mensagem na tela de **Eventos** orientando que as **Naturezas de Rubrica** 1801, 2920, 9209, 9210 e 9220 perdem a validade com a versão Simplificada. E que será necessário reclassificar a incidência destes eventos com outras naturezas.

#### Descontinuada na 1.0 1619:

**(1)** Ajuda Compensatória

**(1)**Lei 14.020/2020 (conversão da MP 936/2020) 6108

**(1)**Tempo de espera do motorista profissional 6119

**(1)** Indenização rescisória – Lei 14.020/2020(conversão da MP 936/2020) 9989

**(1)** Outros valores informativos

#### Tabela 15 - Agente Causador / Situação Geradora de Doença Profissional ou do Acidente de Trabalho:

**(1)**Para atender a nova tabela Tabela 15, criamos na **tela de CAT - Comunicação Acidente de Trabalho** >> Informações Gerais da CAT, o campo “Situação Geradora de Doença Profissional”, localizado abaixo do campo “Situação Geradora do Acidente”. O campo de pesquisa neste, retorna com as opções desta tabela.

#### Tabela 18 - Motivos de Afastamento (TFPMTA):

(1)**Inclusões: Código || Descrição**

**(2)**36 || Afastamento temporário de exercente de mandato eletivo para cargo em comissão;

(1)**Alterações nas descrições: Código || Descrição**

**(2)**05 || Afastamento/licença de servidor público prevista em estatuto, sem remuneração;

**(2)**10 || Afastamento/licença de servidor público prevista em estatuto, com remuneração;

**(2)**17 || Licença maternidade;

**(2)**20 || Licença maternidade - Afastamento temporário por motivo de licença maternidade para o cônjuge sobrevivente ou decorrente de adoção ou de guarda judicial de criança;

**(2)**22 || Mandato eleitoral - Afastamento temporário para o exercício de mandato eleitoral;

**(2)**18 || Licença maternidade - Prorrogação por 60 dias, Lei 11.770/2008 (Empresa Cidadã), inclusive para o cônjuge sobrevivente;

**(1)**Incluímos uma validação na tela de **"Registro de Ocorrências"**, que emite uma mensagem na sua abertura, descrevendo que os “**Motivos Afastamento p/ E-Social**” iguais a **“08, 14, 23, 30, 33”**, perdem a validade a partir da entrada em vigor da versão Simplificada. Caso existam ocorrências com algum destes código, será necessário rever os Históricos de Ocorrências que estão assim classificados.

###

#### Tabela 19 -  Motivos de Desligamento (TFPMTD):

(1)**Inclusões: Código || Descrição**

**(2)**37 || Remoção, em caso de alteração do órgão declarante

**(2)**38 || Aposentadoria, exceto por invalidez

**(2)**39 || Aposentadoria de servidor estatutário, por invalidez

**(2)**40 || Término do exercício do mandato eletivo

**(2)**41 || Rescisão do contrato de aprendizagem por desempenho insuficiente ou inadaptação do aprendiz

**(2)**42 || Rescisão do contrato de aprendizagem por ausência injustificada do aprendiz à escola que implique perda do ano letivo

(1)**Alterações nas descrições: Código || Descrição**

**(2)**21 || Reforma militar

**(2)**22 || Reserva militar

**(2)**23 || Exoneração

**(2)**24 || Demissão

**(2)**25 || Vacância de cargo efetivo

**(1)**Incluímos uma validação na tela de **Tipos de Rescisão** que emite uma mensagem na sua abertura, descrevendo que os “**Motivos desligamento E-Social**” iguais a **“15, 18, 19, 20 e 28”**, perdem a validade a partir da entrada em vigor da versão simplificada. Caso existam tipos com algum destes códigos, será necessário rever os Tipos de Rescisão que estão assim classificados.

#### Tabela 21 - Códigos de Incidência Tributária da Rubrica para o IRRF (TFPINCIRRF):

(1)**Inclusões: Código || Descrição**

**(2)**48 || Previdência privada - Férias;

**(2)**700 || Auxílio moradia;

**(2)**701 || Parte não tributável do valor de serviço de transporte de passageiros ou cargas;

**(2)**9011 || Exigibilidade suspensa - Rendimento tributável - Remuneração mensal;

**(2)**9012 || Exigibilidade suspensa - Rendimento tributável - 13º salário;

**(2)**9013 || Exigibilidade suspensa - Rendimento tributável - Férias;

**(2)**9014 || Exigibilidade suspensa - Rendimento tributável - PLR;

**(2)**9031 || Exigibilidade suspensa - Retenção - Remuneração mensal;

**(2)**9032 || Exigibilidade suspensa - Retenção - 13º salário;

**(2)**9033 || Exigibilidade suspensa - Retenção - Férias;

**(2)**9034 || Exigibilidade suspensa - Retenção - PLR;

**(2)**9831 || Exigibilidade suspensa - Retenção - Depósito judicial - Mensal;

**(2)**9832 || Exigibilidade suspensa - Retenção - Depósito judicial - 13º salário;

**(2)**9833 || Exigibilidade suspensa - Retenção - Depósito judicial - Férias;

**(2)**9834 || Exigibilidade suspensa - Retenção - Depósito judicial - PLR;

**(2)**9041 || Exigibilidade suspensa - Dedução - Previdência oficial - Remuneração mensal;

**(2)**9042 || Exigibilidade suspensa - Dedução - Previdência oficial - 13º salário;

**(2)**9043 || Exigibilidade suspensa - Dedução - Previdência oficial - Férias;

**(2)**9046 || Exigibilidade suspensa - Dedução - Previdência privada - Salário mensal;

**(2)**9047 || Exigibilidade suspensa - Dedução - Previdência privada - 13º salário;

**(2)**9048 || Exigibilidade suspensa - Dedução - Previdência privada - Férias;

**(2)**9051 || Exigibilidade suspensa - Dedução - Pensão alimentícia - Remuneração mensal;

**(2)**9052 || Exigibilidade suspensa - Dedução - Pensão alimentícia - 13º salário;

**(2)**9053 || Exigibilidade suspensa - Dedução - Pensão alimentícia - Férias;

**(2)**9054 || Exigibilidade suspensa - Dedução - Pensão alimentícia - PLR;

**(2)**9061 || Exigibilidade suspensa - Dedução - FAPI - Remuneração mensal;

**(2)**9062 || Exigibilidade suspensa - Dedução - FAPI - 13º salário;

**(2)**9063 || Exigibilidade suspensa - Dedução - Previdência complementar do servidor público - Remuneração mensal;

**(2)**9064 || Exigibilidade suspensa - Dedução - Previdência complementar do servidor público - 13º salário;

**(2)**9065 || Exigibilidade suspensa - Dedução - Previdência complementar do servidor público - Férias;

**(2)**9066 || Exigibilidade suspensa - Dedução - FAPI - Férias;

**(2)**9067 || Exigibilidade suspensa - Dedução - Plano privado coletivo de assistência à saúde;

**(2)**9082 Compensação judicial do ano-calendário;

**(2)**9083 Compensação judicial de anos anteriores;

(1)**Alterações nas descrições: Código || Descrição**

**(2)**9 || Verba transitada pela folha de pagamento de natureza diversa de rendimento ou retenção/isenção/dedução de IR;

**(2)**11 || Rendimento tributável Remuneração mensal;

**(2)**12 || Rendimento tributável 13º salário;

**(2)**13 || Rendimento tributável Férias;

**(2)**14 || Rendimento tributável PLR;

**(2)**31 || Retenção Remuneração mensal;

**(2)**32 || Retenção 13º salário;

**(2)**33 || Retenção Férias;

**(2)**34 || Retenção PLR;

**(2)**41 || Dedução do rendimento - Previdência oficial - Remuneração mensal;

**(2)**42 || Dedução do rendimento - Previdência oficial - 13º salário;

**(2)**43 || Dedução do rendimento - Previdência oficial - Férias;

**(2)**46 || Dedução do rendimento - Previdência privada - Salário mensal;

**(2)**47 || Dedução do rendimento - Previdência privada - 13º salário;

**(2)**48 || Dedução do rendimento - Previdência privada - Férias;

**(2)**51 || Dedução do rendimento - Pensão alimentícia - Remuneração mensal;

**(2)**52 || Dedução do rendimento - Pensão alimentícia - 13º salário;

**(2)**53 || Dedução do rendimento - Pensão alimentícia - Férias;

**(2)**54 || Dedução do rendimento - Pensão alimentícia - PLR;

**(2)**61 || Dedução do rendimento - Fundo de Aposentadoria Programada Individual - FAPI - Remuneração mensal;

**(2)**62 || Dedução do rendimento - Fundo de Aposentadoria Programada Individual - FAPI - 13º salário;

**(2)**63 || Dedução do rendimento - Fundação de previdência complementar do servidor público - Remuneração mensal;

**(2)**64 || Dedução do rendimento - Fundação de previdência complementar do servidor público - 13º salário;

**(2)**65 || Dedução do rendimento - Fundação de previdência complementar do servidor público - Férias;

**(2)**66 || Dedução do rendimento - Fundo de Aposentadoria Programada Individual - FAPI - Férias;

**(2)**67 || Dedução do rendimento - Plano privado coletivo de assistência à saúde;

**(2)**70 || Rendimento não tributável ou isento - Parcela isenta 65 anos - Remuneração mensal;

**(2)**71 || Rendimento não tributável ou isento Parcela isenta 65 anos - 13º salário;

**(2)**72 || Rendimento não tributável ou isento - Diárias;

**(2)**73 || Rendimento não tributável ou isento - Ajuda de custo;

**(2)**74 || Rendimento não tributável ou isento - Indenização e rescisão de contrato, inclusive PDV e acidentes de trabalho;

**(2)**75 || Rendimento não tributável ou isento - Abono pecuniário;

**(2)**76 || Rendimento não tributável ou isento - Rendimento de beneficiário com moléstia grave ou acidente em serviço - Remuneração mensal;

**(2)**77 || Rendimento não tributável ou isento - Rendimento de beneficiário com moléstia grave ou acidente em serviço - 13º salário;

**(2)**79 || Rendimento não tributável ou isento - Outras isenções;

**(1)**Incluímos uma validação na tela de **Eventos**, que emite uma mensagem na sua abertura, descrevendo que as **Incidência p/ IRRF** iguais a **00, 01, 15, 35, 44, 55, 78, 81, 82, 83, 91, 92, 93, 94 e 95**, perdem a validade a partir da entrada em vigor da versão simplificada. Caso existam tipos com algum destes códigos, será necessário rever a Incidência do IRRF que estão assim classificados.

#### Tabela 27 - Procedimentos Diagnósticos (TFPPDI):

**(1)Inclusões: Código || Descrição**

**(2)**1419 || Coronavírus/COVID-19 - SARS-CoV-2 - IgA;

**(2)**1420 || Coronavírus/COVID-19 - SARS-CoV-2 - IgG;

**(2)**1421 || Coronavírus/COVID-19 - SARS-CoV-2 - IgM;

**(2)**1422 || Coronavírus/COVID-19 - SARS-CoV-2 - Pesquisa de antígeno;

**(2)**1423 || Coronavírus/COVID-19 - SARS-CoV-2 - RT-PCR;

**(1)Alterações nas descrições: Código || Descrição**

**(2)**0704 || Hepatite B - HBsAC (anti-HBs);

**(2)**0234 || Hepatite B - HBsAG;

**(2)**1106 || Sumário de urina;
