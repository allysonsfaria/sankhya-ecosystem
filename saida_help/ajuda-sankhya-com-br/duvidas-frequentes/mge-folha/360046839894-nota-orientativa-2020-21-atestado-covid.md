---
id: "360046839894"
titulo: "Nota Orientativa 2020.21 - Atestado COVID-19. Saiba Mais ! "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360046839894-Nota-Orientativa-2020-21-Atestado-COVID-19-Saiba-Mais"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:34:47Z"
rotulos: ["Configuração", "Impostos", "eSocial", "Folha de Pagamento", "Dedução das Contribuições para Atestado COVID-19", "Legislação", "COVID-19"]
---

# Nota Orientativa 2020.21 - Atestado COVID-19. Saiba Mais ! 

**Orientação sobre a dedução nas contribuições previdenciárias do custo salarial dos primeiros 15 dias de afastamento de empregado com Covid-19.**

- Durante os primeiros quinze dias consecutivos ao do afastamento da atividade por motivo de doença, incumbirá à empresa pagar ao segurado empregado o seu salário integral.

- A Lei nº 13.982 de 02 de abril de 2020, artigo 5º, autoriza as empresas a deduzirem de suas contribuições devidas à previdência social os valores pagos em relação aos 15 primeiros dias de salário do trabalhador afastado por enfermidade causada pelo Covid-19.

Saiba Mais: [Portal E-Social](https://portal.esocial.gov.br/manuais/nota-orientativa-2020-21-deducao-nas-cps-dos-15-de-afastamento-por-covid-19-v2.pdf)

**Pré-Requisitos:**

- Versão 4.33.0.25 ou superior
- Versão 4.34.0.6 ou superior
- Versão 4.35.0.0 ou superior

**Parametrizações no sistema:**

![Imagem 1: Acesse o caminho: MGE Pessoal >>Lançamentos >>Histórico dos Colaboradores >>Histórico de Ocorrência:](https://ajuda.sankhya.com.br/hc/article_attachments/19152097843607) Acesse o caminho: MGE Pessoal >>Lançamentos >>Histórico dos Colaboradores >>Histórico de Ocorrência:

O usuário deverá criar um novo histórico de ocorrência para ser utilizado nos casos de afastamento temporário de até 15 dias cujo diagnóstico acusou positivo para Covid-19, conforme exemplo abaixo:

![Imagem 2: O usuário deverá criar um novo histórico de ocorrência para ser utilizado nos casos de afastamento temporário de até 15…](https://ajuda.sankhya.com.br/hc/article_attachments/19152097846679)

- **Situação do colaborador**= ‘T’  Atestado em Dias
- **Motivo afastamento para eSocial**=03
- **Deduz dos dias trabalhados**= ‘SIM’ ou marcado

**![Imagem 3: Registro de Ocorrência:](https://ajuda.sankhya.com.br/hc/article_attachments/19152097850775) Registro de Ocorrência:**

Acessar o caminho: MGE Pessoal >>Lançamentos >>Histórico dos colaboradores >>Registro de Ocorrência:

Com o histórico da ocorrência criado, o usuário deverá lançar no sistema o registro de ocorrência do atestado médico relacionado ao Covid. 

**IMPORTANTE !!!!! [Muita ATENÇÃO]**

- Durante esse período de possibilidades de entregas de atestados médicos do COVID-19 e também de outras doenças, orientamos nossos clientes para melhor funcionamento da rotina e para envio do afastamento temporário ao eSocial que todos os campos do Atestado sejam preenchidos quando for lançado ocorrência de atestado médico em dias, tais como Órgão de Classe, Emitente, Inscrição do Órgão de Classe, CID, dias afastado e especialidade médica.
- Para que possamos identificar qual ocorrência de atestado em dias se trata do Covid-19, o usuário necessariamente precisa preencher o código do CID igual a B342 correspondente ao Covid que fica localizado no Registro de Ocorrência no cadastro de Atestados.
- O CID correto foi disponibilizado pelo Ministério da Saúde através do [material/modelo de formulário médico](https://www.saude.gov.br/images/pdf/2020/marco/20/20200318-Fast-Track-ver002.pdf);

**Exemplo de lançamento:**

![Imagem 4: Exemplo de lançamento:](https://ajuda.sankhya.com.br/hc/article_attachments/19152099719319)

![Imagem 5: Exemplo de lançamento:](https://ajuda.sankhya.com.br/hc/article_attachments/360074997394)

Importante preencher a data fim da ocorrência que é de responsabilidade da empresa e que terá dedução, conforme Lei 13.982/2020 no art. 5º. Posteriormente preencher os dados do Atestado, sendo de cadastro obrigatório o código do CID, conforme orientação acima.

![Imagem 6: Importante preencher a data fim da ocorrência que é de responsabilidade da empresa e que terá dedução, conforme Lei…](https://ajuda.sankhya.com.br/hc/article_attachments/19152097870359)

![Imagem 7: Eventos e fórmulas:](https://ajuda.sankhya.com.br/hc/article_attachments/19152099728535) **Eventos e fórmulas:**

Diante da omissão da legislação vigente e da Nota Orientativa do eSocial 2020.21 não esclarecer de forma clara as incidências de tributos, criamos dois eventos e fórmulas do atestado médico específico da COVID para que um tenha as incidências dos tributos enviando para o eSocial o evento de atestado médico com a natureza de rubrica igual a 1050- Remuneração de dias de afastamento e um outro evento enviando para o eSocial, conforme orientação do item 2 da N.O. 2020.21, natureza da rubrica igual a 9933- auxílio doença e incidência p/ previdência igual a 51- salário família para que haja compensação em favor da empresa dos primeiros 15 dias de afastamento do empregado com Covid-19.

**3.1.** **Evento- ATESTADO MÉDICO COVID (EVENTO COM INCIDÊNCIA)**

**Aba Propriedade:**

![Imagem 8: Aba Propriedade:](https://ajuda.sankhya.com.br/hc/article_attachments/360074993194)

**Aba Incidência:**

![Imagem 9: Aba Incidência:](https://ajuda.sankhya.com.br/hc/article_attachments/19152097882903)

**Aba Base de Cálculo:**

![Imagem 10: Aba Base de Cálculo:](https://ajuda.sankhya.com.br/hc/article_attachments/360074993294)

**3.2-Fórmula ATESTADO MÉDICO COVID-EMPRESA**

**a.2. Fórmula**

**Fórmula auxiliar- XX- Dias de Atestado por Referencia**

IF(PDESPARAM('COUNT(\*)','TFPOCO O,TFPATT A,TFPHIS H','O.CODEMP = :INT\_CODEMP AND O.CODFUNC = :INT\_CODFUNC AND O.DTFINALOCOR >= :DAT\_INIREFERENCIA AND O.DTINICOCOR <= :DAT\_FIMREFERENCIA AND H.AFASTAMENTO = 'T' AND A.CODCID = 'B342' AND A.NUOCOR = O.NUOCOR AND O.CODHISTOCOR = H.CODHISTOCOR',STR(queFuncionario.CODEMP), STR(queFuncionario.CODFUNC),DTOC(&REFERE),DTOC(FSOMAMES(&REFERE,1)-1))=0, 0,
IF(MES(DTOC(&REFERE)) = MES(MemSetVar('VARFINALCOVD',PDESPARAM('O.DTFINALOCOR','TFPOCO O,TFPATT A,TFPHIS H','O.CODEMP = :INT\_CODEMP AND O.CODFUNC = :INT\_CODFUNC AND O.DTFINALOCOR >= :DAT\_INIREFERENCIA AND O.DTINICOCOR <= :DAT\_FIMREFERENCIA AND H.AFASTAMENTO = 'T' AND A.CODCID = 'B342' AND A.NUOCOR = O.NUOCOR AND O.CODHISTOCOR = H.CODHISTOCOR',STR(queFuncionario.CODEMP), STR(queFuncionario.CODFUNC),DTOC(&REFERE),DTOC(FSOMAMES(&REFERE,1)-1)))),
DIA(MemGetVar('VARFINALCOVD')), IF(quePrefSindicato.TIPMES = 'C',30,DIA(DTOC(&REFERE))))-
IF(MES(DTOC(&REFERE)) = MES(MemSetVar('VARINICIALCOVD',PDESPARAM('O.DTINICOCOR','TFPOCO O,TFPATT A,TFPHIS H','O.CODEMP = :INT\_CODEMP AND O.CODFUNC = :INT\_CODFUNC AND O.DTFINALOCOR >= :DAT\_INIREFERENCIA AND O.DTINICOCOR <= :DAT\_FIMREFERENCIA AND H.AFASTAMENTO = 'T' AND A.CODCID = 'B342' AND A.NUOCOR = O.NUOCOR AND O.CODHISTOCOR = H.CODHISTOCOR',STR(queFuncionario.CODEMP), STR(queFuncionario.CODFUNC),DTOC(&REFERE),DTOC(FSOMAMES(&REFERE,1)-1)))),(DIA(MemGetVar('VARINICIALCOVD')) - 1),0))

**Fórmula Atestado Covid**

IF(PDESPARAM('CODCID','TFPATT A,TFPOCO O','CODEMP = :INT\_CODEMP AND CODFUNC = :INT\_CODFUNC AND A.CODCID='B342' AND A.NUOCOR = O.NUOCOR',STR(queFuncionario.CODEMP), STR(queFuncionario.CODFUNC))='B342',((QueFuncionario.SALBASE \* IF(QueFuncionario.TIPSAL=5,220,1)) / 30) \* &FORMULAAUXILIARDIASATESTADOCOVID,0)

**Fórmula do índice**

&FORMULAAUXILIARDIASATESTADOCOVID

| **Observação:**  Substituir &FORMULAAUXILIARDIASATESTADOCOVID pelo código da fórmula auxiliar “Dias de Atestado por Referencia”.  **Exemplo:**  Se a fórmula auxiliar for 5000 alterar para: &F5000 |
| --- |

**3.3.ATESTADO MÉDICO COVID INFORMATIVO**

**Aba Propriedade:**

![Imagem 11: Aba Propriedade:](https://ajuda.sankhya.com.br/hc/article_attachments/19152099744407)

Preencher os itens acima, conforme modelo. A identificação do evento como 116- Evento Salário faz-se necessário para que o evento alimente o Resumo da Folha>>Campo 6>>Salário Família.

**Aba Incidência:**

![Imagem 12: Aba Incidência:](https://ajuda.sankhya.com.br/hc/article_attachments/19152099747351)

Conforme [Nota Orientativa 2020.21](https://portal.esocial.gov.br/manuais/nota-orientativa-2020-21-deducao-nas-cps-dos-15-de-afastamento-por-covid-19-v2.pdf) o eSocial irá recepcionar esse evento com natureza de rubrica e incidência previdenciária diferenciados para que seja possível a diferenciação das verbas ao serem enviadas.

“2) Adicionalmente, em afastamento por motivo de Covid-19, deve criar uma nova rubrica informativa utilizando o código de incidência de contribuição previdenciária = 51 (o mesmo de salário-família) e a Natureza de Rubrica = 9933 (auxílio-doença) e informar o valor da rubrica (quinze primeiros dias de afastamento por Covid-19) até o limite máximo do salário de-contribuição. Desta forma não haverá tributação e o valor dessa rubrica será enviado para a DCTFWeb para dedução, junto com os valores referentes ao salário-família, quando for o caso. A RFB fará a distinção dos benefícios a partir do código da tabela de natureza de rubrica.”

**Aba Base de Cálculo:**

![Imagem 13: Aba Base de Cálculo:](https://ajuda.sankhya.com.br/hc/article_attachments/360076203993)

**3.4. Fórmula ATESTADO MÉDICO COVID INFORMATIVO**

IF(&F565>0,&F565,0)

**INDICE:**

&F566

&F565 ATESTADO MÉDICO COVID

&F566 DIAS DE ATESTADO POR REFERENCIA

**3.5. Ajuste na fórmula ATESTADO MEDICO / DIAS**

IF(PDESPARAM('CODCID','TFPATT A, TFPOCO O',' CODEMP = :INT\_CODEMP AND CODFUNC = :INT\_CODFUNC AND A.NUOCOR = O.NUOCOR',STR(queFuncionario.CODEMP), STR(queFuncionario.CODFUNC)) <>'B342',((QueFuncionario.SALBASE\* IF(QueFuncionario.TIPSAL=5,220,1)) / 30) \* (FDiasAfaMotivo(QueFuncionario.CODEMP,QueFuncionario.CODFUNC,&REFERE,'T',&TIPFOL)-&FORMULAAUXILIARDIASATESTADOCOVID),0)

**Índice**

FDiasAfaMotivo(QueFuncionario.CODEMP,QueFuncionario.CODFUNC,&REFERE,'T',&TIPFOL)-&FORMULAAUXILIARDIASATESTADOCOVID

**Observação: substituir &FORMULAAUXILIARDIASATESTADOCOVID pelo código da fórmula auxiliar “Dias de Atestado por Referencia”**

**Observação:** a dedução tratada pela lei 13.982/2020 poderá ser feita no período de três meses, podendo ser prorrogada por ato do Poder Executivo, conforme art.6º da referida lei.

“Art. 6º O período de 3 (três) meses de que trata o caput dos arts. 2º, 3º, 4º e 5º poderá ser prorrogado por ato do Poder Executivo durante o período de enfrentamento da emergência de saúde pública de importância internacional da Covid-19, definida pela Lei nº 13.979, de 6 de fevereiro de 2020.”

**![Imagem 14: Lançamento Movimento por Funcionário e Folha Mensal:](https://ajuda.sankhya.com.br/hc/article_attachments/19152097901335) Lançamento Movimento por Funcionário e Folha Mensal:**

Acessar o caminho: MGE PESSOAL >> Lançamentos >>Movimentação por Funcionário:

- O usuário deverá lançar manualmente no Movimento por Funcionário o evento do atestado médico Covid para que seja apresentado no cálculo, conforme exemplo abaixo:

![Imagem 15: Folha Mensal:](https://ajuda.sankhya.com.br/hc/article_attachments/360068760273)**Folha Mensal:**

![Imagem 16: Folha Mensal:](https://ajuda.sankhya.com.br/hc/article_attachments/19152099759383)

**![Imagem 17: Resumo da folha:](https://ajuda.sankhya.com.br/hc/article_attachments/19152097911575) Resumo da folha:**

Acessar MGE Pessoal >> Relatórios >>Resumo da folha:

![Imagem 18: Acessar MGE Pessoal >> Relatórios >>Resumo da folha:](https://ajuda.sankhya.com.br/hc/article_attachments/19152099768087)

Conforme [Nota Orientativa 2020.21](https://portal.esocial.gov.br/manuais/nota-orientativa-2020-21-deducao-nas-cps-dos-15-de-afastamento-por-covid-19-v2.pdf) apesar de terem a mesma incidência previdenciária e serem enviados juntos, o evento de salário família e o evento de atestado médico Covid serão diferenciados pela Receita Federal através da natureza de rubrica, para facilitar a conferência dos valores pelo usuário decidimos centralizar todos os valores em uma só linha, ou seja, os eventos de salário família e atestado Covid irão para a mesma linha do Resumo da Folha, assim como para será enviado para a DCTFWeb.
