---
id: "4409629147159"
titulo: "Projeto simplificação -  Criação de novas informações no Pessoal+, Pessoal/G e SaneSocial"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4409629147159-Projeto-simplifica%C3%A7%C3%A3o-Cria%C3%A7%C3%A3o-de-novas-informa%C3%A7%C3%B5es-no-Pessoal-Pessoal-G-e-SaneSocial"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-07-29T13:29:39Z"
rotulos: ["Configuração", "Atualização", "#validadoRayssa", "eSocial", "Projeto de Simplificação: Novas Informações no Pessoal+ Pessoal/G e SaneSocial", "Pessoal+", "Pessoal/G", "Sanesocial"]
---

# Projeto simplificação -  Criação de novas informações no Pessoal+, Pessoal/G e SaneSocial

#### Requisitos mínimos:

**Versão banco de dados:** 4.40.0.21

**Versão executável:** 4.40.0.21

**Versão Do Sanesocail:** 3.0b1218

**Script do SanEsocial:** Atualizado

### Imagem 1: Introdução Introdução

Conforme publicada na Portaria Conjunta SEPRT/RFB nº 82, foi aprovado o leiaute final do eSocial Simplificado, versão S-1.0. O eSocial Simplificado foi previsto na Lei nº 13.874/19.

Os prazos para entrada em vigor de cada fase e da versão Simplificada estão na Portaria Conjunta SEPRT/RFB/ME Nº 71, de 06/2021 e Notas Orientativas e Técnicas.

Houve redução em mais de 30% do número de campos dos leiautes do eSocial, o que inclui a simplificação de vários eventos e a exclusão total de 12 eventos transmitidos/a transmitir pelas empresas.

###

### Detalhamento do que foi criado no Pessoal/G e Pessoal+ por evento:

#### S-1020 - Tabela de Lotações Tributárias:

Na tela **Empresas >> Informações Fiscais,** incluímos no Tipo de Lotação a opção “08 Operador Portuário tomador de serviços de trabalhadores avulsos”.

###

#### S-1200 - Remuneração de Trabalhador vinculado ao Regime Geral de Previd. Social:

As informações relativas ao Intermitente foram alteradas e a partir dessa versão serão inseridos os dias efetivamente trabalhados. Serão considerados aqueles dias previstos na Convocação do Trabalho intermitente em que o funcionário tenha comparecido ao trabalho.

###

#### S-2190 - Registro Preliminar de Trabalhador:

Neste evento passam a ser consideradas dentro do grupo “Informações do registro preliminar do trabalhador” e “Informações referentes ao registro eletrônico de empregados e à Carteira de Trabalho e Previdência Digital - CTPS Digital”, algumas informações adicionais, tais como: Matrícula, Categoria do eSocial, Natureza de Atividade, CBO do Cargo/Função, Valor do Salário, Unidade do Salário, Tipo de contrato de trabalho e Data do término do contrato por prazo determinado;

#### S-2200 - Cadastramento Inicial do Vínculo e Admissão/Ingresso de Trabalhador

#### S-2205 - Alteração de Dados Cadastrais do Trabalhador

#### S-2206 - Alteração de Contrato de Trabalho/Relação Estatutária

Passou a exigir Informações do trabalhador imigrante, solicitando as seguintes informações:

Tempo de residência do trabalhador imigrante, será preenchido com a informação da tela Funcionários >> Pessoais >> Estrangeiro, o campo **“Tempo de residência do trabalhador imigrante”**, com um das opções, Prazo indeterminado ou Prazo determinado;

Condição de ingresso do trabalhador imigrante, será preenchido com a informação da tela Funcionários >> Pessoais >> Estrangeiro, com o campo **“Condição de ingresso do trabalhador imigrante”**, com uma das opções: 1 - Refugiado, 2 - Solicitante de refúgio, 3 - Permanência no Brasil em razão de reunião familiar, 4 - Beneficiado pelo acordo entre países do Mercosul, 5 - Dependente de agente diplomático e/ou consular com acordo de reciprocidade e atividade remunerada, 6 - Beneficiado pelo Tratado de Amizade, Cooperação e Consulta entre o Brasil e Portugal, 7 - Outra condição;

Dentro do conjunto já exigido de Informações do trabalhador celetista, incluíram:

Número que identifica o processo trabalhista, quando a admissão se der por decisão judicial, localizado na tela Funcionários >> Admissão, campo **“Nro do processo p/ admissão por decisão judicial”**. Importante, não é necessário para esse caso existir um cadastro na tela Arquivos >> Cadastro >> Processos, o cliente pode incluir direto no número do processo;

Dentro do conjunto já exigido de Informações do contrato de trabalho, serão enviadas algumas informações dos eventos extintos S-1030 e S-1040.

Diferente do que tínhamos nos eventos citados, agora teremos apenas Nome do Cargo, CBO Cargo, Nome da Função e o CBO Função;

**Para aqueles clientes que possuem CBO em ambos, será preciso configurar os parâmetros chave “FPGERAS1040” e “FPUTILIZACBO”, sendo o primeiro como Sim e o segundo como Função;**

Fazendo essa configuração o CBO estará disponível nos dois cadastros;

Estando desta forma, serão preenchidos tanto os dados do Cargo como da Função nos eventos S-2200 e S-2206;

Importante, como antes não tínhamos o envio da Função, caso o cliente faça essas configurações, serão gerados eventos S-2206 para **todos os funcionários,** que estejam sujeitos a essa condição;

No grupo destinados aos Dependentes, passou a requerer o sexo do dependente, que está disponível no cadastro de Dependentes;

Com o fim do evento S-1050 (Horários), o grupo de Informações do horário contratual do trabalhador, passou a solicitar:

Indicar se a jornada semanal possui horário noturno (no todo ou em parte), que é configurado no cadastro de Carga Horária, no campo **“Possui Horário Noturno (total ou parcial)”** com as opções “S - Sim e N - Não”;

A Descrição da jornada semanal contratual, que deverá conter os dias da semana e os respectivos horários contratuais (entrada, saída e intervalos) será o correspondente do cadastro de Carga Horária, no campo **"Descrição da Carga Horária"**;

Para os Treinamentos, capacitações, exercícios simulados, autorizações ou outras anotações que devam ser anotadas no registro de empregados e/ou na CTPS, por determinação de Norma Regulamentadora - NR, serão utilizadas as informações da tela de Treinamentos e Capacitações;

Com o fim do evento S-1050, o grupo Informações do horário contratual do trabalhador, passou a requerer novas informações e para atender a essa demanda, criamos o campo de **“Tipo de jornada”** na tela Carga Horária, com as opções abaixo:

#### ![Imagem 2: Jornada 12 x 36 (12 horas de trabalho seguidas de 36 horas ininterruptas de descanso);](https://ajuda.sankhya.com.br/hc/article_attachments/42310146545431) Jornada 12 x 36 (12 horas de trabalho seguidas de 36 horas ininterruptas de descanso);

####

#### ![Imagem 3: Jornada com horário diário fixo e folga variável;](https://ajuda.sankhya.com.br/hc/article_attachments/42310176676247) Jornada com horário diário fixo e folga variável;

####

#### ![Imagem 4: Jornada com horário diário fixo e folga fixa (no domingo);](https://ajuda.sankhya.com.br/hc/article_attachments/42310176677015) Jornada com horário diário fixo e folga fixa (no domingo);

####

#### ![Imagem 5: Jornada com horário diário fixo e folga fixa (exceto no domingo);](https://ajuda.sankhya.com.br/hc/article_attachments/42310176677783) Jornada com horário diário fixo e folga fixa (exceto no domingo);

####

#### ![Imagem 6: Jornada com horário diário fixo e folga fixa (em outro dia da semana), com folga adicional periódica no domingo;](https://ajuda.sankhya.com.br/hc/article_attachments/42310176678423) Jornada com horário diário fixo e folga fixa (em outro dia da semana), com folga adicional periódica no domingo;

####

#### ![Imagem 7: Turno ininterrupto de revezamento;](https://ajuda.sankhya.com.br/hc/article_attachments/42310146551447) Turno ininterrupto de revezamento;

####

#### ![Imagem 8: Demais tipos de jornada;](https://ajuda.sankhya.com.br/hc/article_attachments/42310176679831) Demais tipos de jornada;

Como antes o próprio sistema criava a regra, iremos utilizar dela para aplicar ao novo campo e não gerar alterações ou o cliente precisar cadastrar novamente. Entretanto, podem existir casos que existia a opção do cliente e ele optou por 9, nestes casos é interessante uma revisão e até alteração se for o caso;

Os códigos 3, 5, 6 e 7 não têm correspondência com a regra anterior e não serão alimentados pelo sistema. Optamos em não fazer porque elas diferem do que tínhamos no sistema e na versão anterior, e ainda porque é um cadastro muito flexível e permite uma quantidade grande de combinações.

#### S-2230 - Afastamento Temporário:

As Informações referentes ao período aquisitivo de férias passam a ser enviadas neste evento e basicamente correspondem ao Histórico de Férias **(**parâmetro chave **“FPCODHIS”)** inserido no Registro de Ocorrências depois da confirmação do Cálculo de Férias;

#### S-2240 - Condições Ambientais do Trabalho - Agentes Nocivos:

Dentro das Informações relativas ao ambiente de trabalho já existentes, foram necessário alguns ajustes no sistema:

A tela SESMT >> Ambiente de Trabalho >> Local(\*), ocultamos a opção “3. Prestação de serviços em instalação de terceiros, não considerados como Lotação”, porque o eSocial retirou do leiaute, e aqueles cadastros que estiverem com essa opção, passam automaticamente para “2 - Estabelecimentos de Terceiros”.

Serão mantidas na tela de Ambiente de Trabalho as informações referentes a Fatores de Risco, embora o eSocial não esteja mais solicitando no evento S-2240;

Substituindo os Fatores de Risco o eSocial passou a adotar Agentes Nocivos. Para atender a esta demanda criamos uma aba com este nome, na tela de **"Ambiente de Trabalho".**

A tela eSocial >> Tabelas Gerais possui a nova aba Agentes Nocivos e Atividades - Aposentadoria especial, que basicamente contém as informações da tabela do eSocial “Tabela 24 - Agentes Nocivos e Atividades - Aposentadoria Especial”.

As informações se neste Agente Nocivo utilizam EPI e EPC, ocorrem na própria grade com o restante das informações.

Há uma grade exclusiva para o Equipamento de Proteção Individual - EPI, porque o eSocial pede os Requisitos da Norma Regulamentadora 06 (NR-06) e da Norma Regulamentadora 09 (NR-09) pelo(s) EPI(s) informado(s). O que não acontece com os EPC’s;

Os campos basicamente correspondem aos que existiam na aba **"Fatores de Risco"**, exceto:

Código e Descrição do Agente Nocivo, que correspondem às opções da Tabela Agentes Nocivos e Atividades - Aposentadoria Especial;

Unidade de Medida, que apresenta um conjunto diferente de opções;

**Com a extinção do evento S-1060, as informações correspondentes a Local do Ambiente, Descrição do Setor, Tipo de Inscrição e o Número da Inscrição passam a ser enviadas neste evento. Estas informações estão disponíveis na tela de Ambiente de Trabalho;**

#### S-2300 - Trabalhador Sem Vínculo de Emprego/Estatutário - Início:

Assim como aconteceu com o campo **"Matrícula"**, passou a ser enviadas as Informações de mudança de CPF do trabalhador, antes que elas existiam apenas no S-2200;

A matrícula passou a ser solicitada para o TSVE, entretanto, como podemos ter casos em que esse campo não será preenchido, criamos no Cadastro do Funcionário >> Admissão, o campo “Dispensado de matrícula”. Este campo estaria disponível quando:

A Categoria do eSocial for igual a 201, 202, 304, 305, 308, 401, 410, 721, 189, 722, 723, 731, 734, 738, 761, 771, 901 ou 902;

Essa marcação tem prioridade em relação a Empresas >> Informações Gerais >> Matrícula (Pessoal/G) ou Empresas >> Informações Gerais >> Gera Matrícula do Funcionário automaticamente (Pessoal+/W), para essas categorias definidos acima;

Se o campo Matrícula já estiver com informação, ela não será alterada no nosso Produto ou eSocial. 

Não é possível incluir informação de matrícula em um evento S-2300 enviado na versão anterior do leiaute, quando o campo ainda não existia no evento. Ou seja, tanto a sua retificação ou a alteração devem ser feitas sem a informação da matrícula;

O trabalhador que já tiver sido informado em evento S-2300, antes da inclusão do campo relativo à matrícula, continua sendo identificado apenas pelo CPF e categoria. Se o declarante desejar incluir matrícula para esse trabalhador, tem de enviar o evento de término de TSVE (S-2399) desse trabalhador e só então um novo evento S-2300 contendo a matrícula

#### S-2299 - Desligamento:

Com a extinção do evento S-2250, este evento passou a considerar no grupo Informações relativas ao desligamento do vínculo, a Data de concessão do aviso prévio;

As informações para os dias de trabalho do Intermitente são as mesmas estabelecidas no S-1200;

#### S-2399 - Trabalhador Sem Vínculo de Emprego/Estatutário - Término:

Incluídas nas informações já solicitadas do grupo TSVE - Término, o Número que identifica o processo trabalhista, quando o término de TSVE se der por decisão judicial:

Criamos na tela de Informações Complementares para Rescisão, presente na tela de Cálculo >> Individual ou Automático >> Rescisão, o campo **“Nro processo de término de TSVE por decisão judicial”**. Da mesma forma que tivemos no evento S-2200, não é necessário para esse caso existir um cadastro na tela Arquivos >> Cadastro >> Processos, o cliente deve incluir direto o número do processo;

No Pessoal+ esse novo campo está na tela de Cálculo de Rescisão;

Uma vez preenchido na tela acima, esta informação será gravada na tela de Funcionários >> Afastamento;
