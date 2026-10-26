---
id: "360044597794"
titulo: "Geração do ECD/ECF"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597794-Gera%C3%A7%C3%A3o-do-ECD-ECF"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:46:40Z"
rotulos: ["Configuração", "Empresa", "Contábil", "Digital", "ECD", "Escrituração", "Blocos", "ECF", "Registros", "Connection", "SPED", "Tabelas Dinâmicas", "Web", "Geração do ECD/ECF manual", "Fiscal", "Contas", "Plano", "Referencial", "Contabilidade", "Preferências", "Plano de Contas", "Configurações para Geração de ECD e ECF no Sankhya Om"]
---

# Geração do ECD/ECF

Tomaremos conhecimento neste tópico, das configurações necessárias acerca das Preferências da Empresa de Contabilidade e do Plano de Contas, de modo que ao realizá-las, seja possível efetuar a geração dos arquivos "ECD - Escrituração Contábil Digital" e "ECF - Escrituração Contábil Fiscal".

Destacaremos abaixo as abas e campos que caso não sejam devidamente configurados, interferem diretamente na geração dos referidos arquivos:

## Contabilidade > Preferências > Empresa

#### Aba Plano de Contas

![Imagem 1: Aba Plano de Contas](https://ajuda.sankhya.com.br/hc/article_attachments/8930352031255)

Instituição Resp. Man. Plano Contas Referencial: Define-se neste campo, qual a empresa responsável pela manutenção de seu plano de contas referencial. Tem-se as seguintes possibilidades de escolha:

- Nenhuma;
- 1 - PJ em Geral;
- 2 - PJ em Geral - Lucro Presumido;
- 3 - Financeiras;
- 4 - Seguradoras ou Entidades Abertas de Previdência Complementar;
- 5 - Imunes e Isentas em Geral;
- 6 - Imunes e Isentas - Financeiras;
- 7 - Imunes e Isentas - Seguradoras;
- 8 - Entidades Fechadas de Previdência Complementar;
- 9 - Partidos Políticos.

#### Aba ECD - Escrituração Contábil Digital

![tela](https://ajuda.sankhya.com.br/hc/article_attachments/15589935834519)

Situação Especial: Define-se aqui a situação especial na qual a empresa se enquadra. São disponíveis as seguintes opções:

- Extinção;
- Fusão;
- Incorporação/Incorporada;
- Incorporação/Incorporadora;
- Cisão Total;
- Cisão Parcial;
- Transformação;
- Desenquadramento de Imune/Isenta;
- Inclusão no Simples Nacional;
- Transferência de Sede.

As situações especiais "Transformação" e "Transferência de Sede" não são mais aplicadas a partir de 2017. No processo de cadastramento de uma destas ocorrências com data superior a 01/01/2017, ao tentar confirma-lo será exibido um pop-up com a seguinte mensagem:

"As situações especiais "Transformação" e "Transferência de Sede" não são mais utilizadas a partir de 2017."

#### Aba Relacionamento com Participantes - ECD

![tela](https://ajuda.sankhya.com.br/hc/article_attachments/15589935840535)

Cód. Relacionamento: Define-se neste campo o código referente ao relacionamento da empresa com o parceiro. Podem ser escolhidas dentre as seguintes opções:

- Matriz no exterior;
- Filial, inclusive agência ou dependência, no exterior;
- Coligada, inclusive equiparada;
- Controladora;
- Controlada (exceto subsidiária integral);
- Subsidiária integral;
- Controlada em conjunto;
- Entidade de Propósito Específico (conforme definição da CVM);
- Participante do conglomerado;
- Vinculadas (Art. 23 da Lei 9.430/96);
- Localizada em país com tributação favorecida.

#### Aba Signatários

![tela](https://ajuda.sankhya.com.br/hc/article_attachments/15589935845527)

#### Aba SCP - Sociedade em Cota de Participação

![tela](https://ajuda.sankhya.com.br/hc/article_attachments/15602644384919)

Tipo de Empresa: Define-se neste campo como é a integração da empresa em relação à sociedade em cota de participação. Tem-se três opções para escolha:

- 0 – Empresa não participante de SCP como sócio ostensivo;
- 1 – Empresa participante de SCP como sócio ostensivo;
- 2 – SCP.

CNPJ da SCP: Informa-se neste campo, o CNPJ da Sociedade em Cota de Participação; pode-de digitar ou mesmo pesquisar os dados do Cadastro de Empresas.

Nome da SCP: De acordo com o preenchimento realizado no campo anterior, tem-se aqui o nome da Sociedade em Cota de Participação.

**Observação:** será permitido cadastrar um registro nos dois últimos campos citados, apenas se o campo "Tipo de Empresa" for definido com a opção "1 - Empresa participante de SCP como sócio ostensivo".

#### Aba Auditores Independentes

![tela](https://ajuda.sankhya.com.br/hc/article_attachments/15602644385431)

Registro na CVM: Este campo é de preenchimento obrigatório, e nele informa-se o registro na Comissão de Valores Mobiliários.

Nome do Auditor: Preenche-se aqui o nome do auditor correspondente ao registro inserido no campo anterior.

#### Aba ECF - Escrituração Contábil Fiscal

![tela](https://ajuda.sankhya.com.br/hc/article_attachments/15602644385815)

O detalhamento da composição das abas "Blocos", "Parâmetros de Tributação" e "Parâmetros Complementares" é apresentado na documentação da tela "Contabilidade > Preferências > Empresa".

## Contabilidade > Conexão > ECF > Configurações P/ ECF > Plano de Contas Referencial

Através desta tela, realiza-se a importação/atualização das tabelas dinâmicas. Esta atualização ocorre com o intermédio da aplicação "[Sankhya Web Connection](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394)".

![tela](https://ajuda.sankhya.com.br/hc/article_attachments/15602644386199)

Primeiramente, define-se o tipo de tabela a ser importado. Tem-se as seguintes opções:

- 1 - PJ em Geral ( L100\_A + L300\_A )
- 2 - PJ em Geral - Lucro Presumido ( P100 + P150 )
- 3 - Financeiras ( L100\_B + L300\_B )
- 4 - Seguradoras ou Entidades Abertas de Previdência Complementar ( L100\_C + L300\_C )
- 5 - Imunes e Isentas em Geral ( U100\_A + U150\_A )
- 6 - Financeiras - Imunes e Isentas ( U100\_B + U150\_B )
- 7 - Seguradoras - Imunes e Isentas ( U100\_C + U150\_C )
- 8 - Entidades Fechadas de Previdência Complementar ( U100\_D + U150\_D )
- 9 - Partidos Políticos ( U100\_E + U150\_E )

Uma vez definido o tipo de tabela a ser importado/atualizado, clica-se no botão **"Atualizações Sped ECF"**.

## Contabilidade > Conexão > ECF > Configurações P/ ECF > Configurador de Blocos e Registros

Por meio desta tela, realiza-se a conformação dos blocos e registros acerca da Escrituração Contábil Fiscal.

![tela](https://ajuda.sankhya.com.br/hc/article_attachments/15602644386583)

Inicialmente na aba Geral, determina-se qual o "Bloco" a ser configurado; tem-se as seguintes alternativas:

- N
- P
- T
- U
- X
- Y

Registro: Informa-se aqui o registro a ser configurado relacionado ao bloco anteriormente definido; pode-se inserir o numeral entre "2" e "899".

Código: Campo de preenchimento obrigatório; nele será feita a concatenação do Bloco e do Registro e nas Tabelas Dinâmicas o sistema busca o valor correspondente a esta tabela.

#### Aba Geral

Tipo de Dados: Define-se qual o tipo de dados relacionado ao Bloco/Registro em questão. Tem-se as seguintes opções:

- P - Plano de Contas;
- V - Valor;
- S - Comando SQL;
- A - Arquivo Texto.

Ativo: Esta marcação irá definir se o registro está ativo ou não.

Permite gerar registro com valor zerado: O registro que possuir esta marcação efetuada, poderá ser gerado com valor zerado.

Arquivo: Por meio deste campo, pode-se fazer o upload de um arquivo ".txt" e o mesmo será salvo no Repositório de Arquivos do Sistema com o seguinte caminho: "Contabilidade / ECF / Arquivos", enquanto que apenas o nome do arquivo será salvo neste campo. Esta marcação estará ativa, apenas se o campo "Tipo de Dados" for definido como "A – Arquivo Texto".

SQL: Neste espaço, pode-se construir uma query e posteriormente validá-la. Estará ativo para uso, apenas se o campo "Tipo de Dados" for definido como "S – Comando SQL".

Valor: Este é um campo para valores monetários. Ele estará ativo apenas se o campo "Tipo de Dados" for definido como "V – Valor".

#### Aba Contas p/ Configurador de Blocos e Registros

![tela](https://ajuda.sankhya.com.br/hc/article_attachments/15602636371095)

Esta aba estará habilitada apenas se o campo "Tipo de Dados" presente na aba Geral for definido como "P – Plano de Contas".

Cód. Reduzida: Neste campo, informa-se a conta reduzida relacionada ao Bloco/Registro que estão sendo configurados.

Cód. Conta: Este campo será alimentado automaticamente com o código da conta de acordo com a informação inserida no campo anterior.

## Contabilidade > Cadastros > Plano de Contas

Também contribuindo para a geração dos arquivos "ECD - Escrituração Contábil Digital" e "ECF - Escrituração Contábil Fiscal", tem-se as configurações feitas na tela de cadastro de "Plano de Contas" as quais podem ser acessadas clicando-se no link [Plano de Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116393).

## Contabilidade > Arquivos > Lançamentos Contábeis

Também contribuindo para a geração dos arquivos "ECD - Escrituração Contábil Digital" e "ECF - Escrituração Contábil Fiscal", tem-se as configurações feitas na tela de cadastro de "Lançamentos Contábeis" as quais podem ser acessadas clicando-se no link [Lançamentos Contábeis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116173).

## Atualização das Tabelas Dinâmicas

O processo de atualização das Tabelas Dinâmicas funciona com o auxílio da aplicação Web Connection, aplicação esta que irá rodar localmente na máquina do usuário. Vejamos o caminho da Atualização:

Parte 1 – A atualização das Tabelas Dinâmicas ocorre através do aplicativo da Receita Federal, o Sped ECF; pode-se obter o referido aplicativo por meio do seguinte link:

http://idg.receita.fazenda.gov.br/orientacao/tributaria/declaracoes-e-demonstrativos/sped-sistema-publico-de-escrituracao-digital/escrituracao-contabil-fiscal-ecf/programa-sped-contabil-fiscal-para-windows

![sped](https://ajuda.sankhya.com.br/hc/article_attachments/15602644387607)

Parte 2 – O Web Connection irá compactar estes arquivos e enviar para o Repositório de Arquivos do Sankhya-Om; para tal deve-se atentar para as seguintes marcações:

#### Aba Geral

![Imagem 12: Aba Geral](https://ajuda.sankhya.com.br/hc/article_attachments/15602644388247)

Usa SPED ECF: Esta opção quando assinalada, define se o usuário da máquina em questão irá realizar o envio ou não do arquivo compactado com as tabelas dinâmicas para o Repositório de Arquivos do Sankhya-W. Se marcada, a aba "SPED ECF" será habilitada e o usuário poderá realizar as devidas configurações para esta ação.

#### Aba SPED ECF

![configuracoes](https://ajuda.sankhya.com.br/hc/article_attachments/15602636373399)

Url do Sistema: Deve-se informar neste campo qual a URL o Sankhya-W está rodando, para que o Web Connection consiga fazer o envio do arquivo compactado para o Repositório de Arquivos.

Diretório: Informa-se neste campo o caminho padrão para onde o aplicativo da Receita efetua a importação das tabelas dinâmicas. O Web Connection irá buscar os arquivos através deste diretório; pode-se buscar o diretório através do botão de Pesquisa localizado à frente do campo. O diretório possui um valor padrão e caso não seja informado nenhum valor, o que será salvo no arquivo de configuração do Web Connection será:

C:/Arquivos de Programas RFB/Programas SPED/ECF/recursos/tabelas

Tipo Execução: Por este campo, define-se como será a forma de execução do Web Connection. Tem-se duas opções:

- Ao iniciar web connection: Na inicialização do Web Connection ela fará a verificação se existem tabelas a serem atualizadas e existindo, fazer o envio. Se esta opção estiver selecionada, ele fará essa verificação/envio apenas em sua inicialização. Somente se o Web Connection for reiniciado será feita outra verificação/envio;
- Todos os dias: Na inicialização do Web Connection, será feita a verificação se existem tabelas a serem atualizadas e existindo, fazer o envio. Se esta opção estiver marcada, ele criará uma "Thread" que ficará executando durante todo o tempo que o Web Connection estiver em execução, e a cada 24 horas ela irá verificar se há novas tabelas para envio; se houver o envio será feito (opção interessante para quem não desliga sua máquina).

Nesta aba tem-se dois botões que possuem o seguinte comportamento:

Testar: O Web Connection fará um teste de conexão através da URL informada e irá verificar se o diretório informado é realmente um diretório e se existem arquivos dentro dele. Ao final do teste uma mensagem de sucesso ou erro, será apresentada.

Enviar Agora: O Web Connection irá compactar todos os arquivos existentes no diretório informado e enviá-los independente do histórico de tabelas já enviadas anteriormente.

**Observação:** sempre que o Web Connection enviar arquivos para o Repositório de Arquivos do Sankhya-Om, ele irá salvar em uma lista de histórico quais foram os nomes desses arquivos enviados. Na próxima vez que for executada, se o arquivo estiver nesta lista ele não será enviado, a menos que o usuário tenha clicado no botão "Enviar Agora", pois dessa forma o Web Connection enviará todos os arquivos independente do histórico.

O nome do arquivo dentro do WebConnection que contém o nome desses arquivos é lista.tabelas.ecf.conf. Porém, quando fala-se em todos os arquivos, não será de fato todos os arquivos. Vejamos um exemplo:

Suponhamos que no diretório tenhamos os arquivos:

SPEDECF\_DINAMICO\_2014$SPEDECF\_DINAMICA\_M300\_A$7$448

SPEDECF\_DINAMICO\_2015$SPEDECF\_DINAMICA\_M300\_A$1$622

Ambos arquivos correspondem a mesma tabela que será importada para o Sankhya-W, M300\_A. Contudo, uma está mais atualizada que outra. A primeira é do ano ade 2014 e a segunda do ano de 2015, logo somente a de 2015 será enviada para o Repositório de Arquivos no Sankhya-Om.

Para o envio dos arquivos o Web Connection sempre levará em consideração a versão dos arquivos. Somente as versões mais recentes serão enviadas, seja pelo processo normal do Web Connection buscando o histórico salvo das tabelas já enviadas, quanto pelo processo em que o usuário clica no botão **"Enviar Agora"**.

Os arquivos compactados serão salvos no endereço "Contabilidade / ECF / TabelasDinamicas" no Repositório de Arquivos.

Parte 3 – O Sankhya-Om irá descompactar o arquivo localizado no Repósitório de Arquivos e proceder com a atualização das Tabelas Dinâmicas. A atualização das tabelas dinâmicas dentro do Sankhya-Om pode ser realizada através de 3 telas:

- Contabilidade > Cadastros > Plano de Contas;
- Contabilidade > Conexão > ECF > Configuração P/ ECF > Configurador de Blocos e Registros;
- Contabilidade > Conexão > ECF > Configuração P/ ECF > Plano de Contas Referencial.

Todas as telas possuem o botão "Atualizações Sped ECF". Ao clicar nesse botão, um pop-up será aberto contendo as informações da atualização das tabelas.

![plano](https://ajuda.sankhya.com.br/hc/article_attachments/15602636374295)

Última atualização: Este campo tratá a data da última atualização das tabelas da ECF.

Status: Tem-se aqui o status da atualização; podendo ser "Em execução" ou "Parado".

Última execução: Apresenta a data da última execução.

Tempo decorrido: Visualiza-se o tempo gasto na execução.

Tipo da execução: Tem-se aqui a que se refere a execução; este campo pode assumir três valores:

- Apenas verificação;
- Atualizou tabelas;
- Falhou.

Observações: serão apresentadas aqui as observações do processo. Para cada tipo de execução será exibida uma mensagem diferente:

- Apenas verificação: A verificação da atualização das tabelas dinâmicas foi concluída, mas não houve atualização a ser realizada.
- Atualizou tabelas: As tabelas dinâmicas foram atualizadas.
- Falhou: Trará o erro ocorrido durante o processo.
