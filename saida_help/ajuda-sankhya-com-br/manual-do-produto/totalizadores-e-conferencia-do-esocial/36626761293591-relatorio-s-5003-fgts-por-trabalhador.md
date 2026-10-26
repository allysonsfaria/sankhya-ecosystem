---
id: "36626761293591"
titulo: "Relatório S-5003 (FGTS por trabalhador)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36626761293591-Relat%C3%B3rio-S-5003-FGTS-por-trabalhador"
trilha: "Manual do Produto > Pessoas+ > eSocial > Totalizadores e Conferência do eSocial"
atualizado_em: "2026-10-22T16:53:14Z"
rotulos: ["Conferência", "Relatórios", "eSocial", "Central do eSocial", "FGTS", "FGTS mensal", "FGTS rescisório", "Pessoal+", "Depósito Indenizatório (eSocial)", "Base Rescisória (eSocial)", "Base 13º (eSocial)", "FGTS do 13º Salário", "FGTS Indenizatório", "Base Indenizatória (eSocial)", "Base 13º Rescisório (eSocial)", "FGTS do 13º Rescisório", "Relatório S-5003 – Conferência de Informações do FGTS por Trabalhador", "ID: br.com.sankhya.mgepes.rh.DashEsocial5003"]
---

# Relatório S-5003 (FGTS por trabalhador)

**Módulo:** Pessoal+
**Versão Mínima:** 5.66.0 
**Caminho de Acesso:** Pessoal+ > Consultas
**ID da Tela:** br.com.sankhya.mgepes.rh.DashEsocial5003

---

## Descrição e Usabilidade

### 1. Descrição da Funcionalidade

O **Relatório S-5003 -Conferência de Informações do FGTS por Trabalhador** apresenta, de forma clara e estruturada, os valores referentes à base de FGTS e aos depósitos apurados por colaborador no sistema, comparando-os com as informações retornadas pelo evento S-5003. Além disso, o relatório evidencia eventuais divergências entre os valores calculados pelo sistema e os informados no retorno do eSocial, facilitando a identificação e o tratamento de inconsistências.

[GIF animado: Imagem 1: O Relatório S-5003 -Conferência de Informações do FGTS por Trabalhador apresenta, de forma clara e estruturada, os…](https://ajuda.sankhya.com.br/hc/article_attachments/36691142397847)

### 2. Estrutura do Relatório

O relatório é organizado da seguinte forma:

- **FGTS Mensal e seus Depósitos**
- **FGTS do 13º Salário e seus Depósitos**
- **FGTS Rescisório e seus Depósitos**
- **FGTS do 13º Rescisório e seus Depósitos**
- **FGTS Indenizatório e seus Depósitos**
- **FGTS Mensal Suspenso**
- **FGTS 13º Suspenso**
- **FGTS Aviso Indenizado Suspenso**

Para cada tipo, o sistema mostra:

- valor calculado no sistema;
- valor retornado pelo eSocial;
- diferença entre eles (quando existir).

Os valores são exibidos somente para trabalhadores que atendem às regras definidas pelo eSocial, considerando:

- Categoria do trabalhador;
- Regime trabalhista;
- Situação do vínculo (ativo ou demitido);
- Motivo de desligamento (quando houver).

### 3. Pré-requisitos

#### Permissões necessárias

- Deve ter permissão para **consultar dados dos colaboradores.**
- Deve **ter acesso liberado para a tela do dashboard**. Essa liberação é feita na tela **Acessos** (Configurações > Controle de Acesso), pelo administrador do sistema.

#### Configurações relacionadas

É possível escolher quais colunas deseja visualizar no dashboard.

1. Clique no botão **Configuração da Grade**.
2. Na seção **Colunas disponíveis**, selecione as colunas desejadas.
3. Mova as colunas para o quadro **Colunas selecionadas**.
4. Clique em **Salvar** para aplicar as alterações.

[GIF animado: Imagem 2: Clique em Salvar para aplicar as alterações.](https://ajuda.sankhya.com.br/hc/article_attachments/36774422643095)

### 4. Jornada de Uso

**(1)** O dashboard **S-5003 - Conferência de Informações do FGTS por Trabalhador** (Pessoal+ > Consultas) pode ser acessado de duas maneiras:

1. Diretamente pela barra de pesquisa do Sankhya Om;

   ![Imagem 3: Diretamente pela barra de pesquisa do Sankhya Om;](https://ajuda.sankhya.com.br/hc/article_attachments/36692568431255)
2. Pela **Central do eSocial** (Pessoal+ > Rotinas Folha), clicando no botão **Dashboard de Conferência**, ao lado inferior direito da tela.

   [GIF animado: Imagem 4: Pela Central do eSocial (Pessoal+ > Rotinas Folha), clicando no botão Dashboard de Conferência , ao lado inferior…](https://ajuda.sankhya.com.br/hc/article_attachments/37856371315607)

**(2)** Ao acessar a tela, **use os filtros** para localizar as informações e clique em **Atualizar**:

- **Empresa;**
- **Período;**
- **Com diferença**.

O dashboard apresenta as informações separadas em cada coluna exibida no relatório e os critérios usados para apuração.

#### Regras de Apuração da Base Mensal (Sistema)

Entram no cálculo os **trabalhadores** com:

- **Tipo de Regime Trabalhista = 1 (CLT) Consolidação das Leis de Trabalho e legislações trabalhistas específicas.**
- **Categoria 1**xx, **3**xx, **201, 202, 721, 401** ou **410**.
- **Diretor com FGTS - Motivo Desligamento:** **diferente de** ('01','02','04','06').
- **Motivo Desligamento eSocial:** **diferente de** ('02','03','05','06','14','17','23','26','27','33','47','48','49') - para empregados.
- **Ou** trabalhadores com **situação diferente** de **demitido.**

A **Base Mensal (Sistema)** do relatório **S-5003** corresponde à soma dos valores dos eventos classificados como **proventos**, deduzidos os valores dos eventos classificados como **descontos**, considerado neste cálculo, apenas os eventos que estão devidamente configurados, atendendo simultaneamente aos seguintes critérios: 

- **Evento** esteja marcado o campo **Outros = FGTS**;

  ![Imagem 5: Evento esteja marcado o campo Outros = FGTS ;](https://ajuda.sankhya.com.br/hc/article_attachments/37277025438487)
- **Evento** com codIncFGTS = 11 - Base de cálculo do FGTS mensal.

  ![Imagem 6: Evento com codIncFGTS = 11 - Base de cálculo do FGTS mensal.](https://ajuda.sankhya.com.br/hc/article_attachments/37277025439255)

---

#### Regras de Apuração da Base Mensal (eSocial)

A **Base Mensal eSocial** é apurada pelo retorno do **S-5003** através do grupo **infoBaseFGTS** subgrupo **BASEPERAPUR**, considerando apenas as tags abaixo:

- **INDINCID =** 1 (Indicativo de incidência de FGTS)
- **REMFGTS** (Remuneração - valor da base de cálculo do FGTS)
- **tpValor =** {11, 13, 15, 17}

**XML de Retorno** vai identificar o retorno na tag <tot tipo="**S5003**">

![Imagem 7: XML de Retorno vai identificar o retorno na tag <tot tipo=" S5003 ">](https://ajuda.sankhya.com.br/hc/article_attachments/37277043953047)

---

#### Regras de Apuração do Depósito Mensal (Sistema)

Os mesmos critérios aplicados para a **Base Mensal (Sistema)** são utilizados para **identificar os trabalhadores elegíveis** ao cálculo do **depósito**.

O **Depósito Mensal (Sistema)** do relatório **S-5003** corresponde à soma dos valores dos eventos que estão devidamente configurados, atendendo simultaneamente aos seguintes critérios: 

- Característica = **FGTSNORMAL**
- Identificação do evento = **102 – FGTS Mensal**
- Natureza da rubrica = **9908**

| ℹ️ **Nota**  Na configuração padrão, o evento com essas características é o **995 – FGTS NORMAL**, calculado por colaborador e truncado em duas casas decimais. Por isso, a soma da coluna **Depósito Mensal (Sistema)** acompanha a soma do evento 995 no corpo do Resumo da Folha. Ela pode ficar alguns centavos abaixo do total de **Dados FGTS** da seção **Total Guia** do Resumo da Folha, que aplica o percentual sobre a base total de FGTS.  📚 Para saber mais, acesse o artigo [**Geração do Resumo da Folha**](https://ajuda.sankhya.com.br/hc/pt-br/articles/17268960280727), etapa de conferência dos valores de FGTS no corpo e no rodapé do resumo. |
| --- |

---

#### Regras de Apuração do Depósito Mensal (eSocial)

A **Base Mensal eSocial** é apurada pelo retorno do **S-5003** através do grupo **infoBaseFGTS** subgrupo **BASEPERAPUR**, considerando apenas as tags abaixo:

- **INDINCID =** 1 (Indicativo de incidência de FGTS)
- **DPSFGTS** **(FGTS a ser depositado)**
- **tpValor =** {11, 13, 15, 17}

---

#### Regras de Apuração da Base 13º (Sistema)

Entram no cálculo os **trabalhadores** com:

- **Tipo de Regime Trabalhista = 1 (CLT) Consolidação das Leis de Trabalho e legislações trabalhistas específicas.**
- **Categoria 1**xx, **3**xx, **201, 202, 721, 401** ou **410**
- **Diretor com FGTS - Motivo Desligamento:** **diferente de** ('01','02','04','06')
- **Motivo Desligamento eSocial:** **diferente de** ('02','03','05','06','14','17','23','26','27','33','47','48','49') - para empregados.
- **Ou** trabalhadores com **situação diferente** de **demitido.**

A **Base 13º (Sistema)** do relatório **S-5003** corresponde à soma dos valores dos eventos classificados como **proventos**, deduzidos os valores dos eventos classificados como **descontos**, considerado neste cálculo, apenas os eventos que estão devidamente configurados, atendendo ao seguinte critério: 

- **Evento** esteja marcado campo **Outros** = **FGTS 13°**;
- **Evento** com **codIncFGTS** = 12 - Base de cálculo do FGTS 13º salário.

---

#### Regras de Apuração da Base 13º (eSocial)

A **Base 13º eSocial** é apurada pelo retorno do **S-5003** através do grupo **infoBaseFGTS** subgrupo **BASEPERAPUR**, considerando apenas as tags abaixo:

- **INDINCID =** 1 (Indicativo de incidência de FGTS)
- **REMFGTS** **(Remuneração (valor da base de cálculo) do FGTS)**
- **tpValor =** {12, 14, 16, 18}

---

#### Regras de Apuração do Depósito 13º (Sistema)

Os mesmos critérios aplicados para o **Base 13º (Sistema)** são utilizados para **identificar os trabalhadores elegíveis** ao cálculo do **depósito**.

O **Depósito 13º (Sistema)** do relatório **S-5003** corresponde à soma dos valores dos eventos que estão devidamente configurados, atendendo simultaneamente aos seguintes critérios: 

- Característica = **FGTS13SALARIO**
- Identificação do evento = **105 – Evento FGTS 13º Sal.Empregados**
- Natureza da rubrica = **9908**

---

#### Regras de Apuração do Depósito 13º (eSocial)

O **Depósito 13º eSocial** é apurado pelo retorno do **S-5003** através do grupo **infoBaseFGTS** subgrupo **BASEPERAPUR**, considerando apenas as tags abaixo:

- INDINCID **= 1 (Indicativo de incidência de FGTS)**
- **DPSFGTS (FGTS a ser depositado)**
- tpValor **=  {12,14,16,18}**

---

#### Regras de Apuração da Base Rescisória (Sistema)

Entram no cálculo os **trabalhadores** com:

- **Tipo de Regime Trabalhista = 1 (CLT) Consolidação das Leis de Trabalho e legislações trabalhistas específicas.**
- **Categoria 1**xx, **3**xx, **201, 202, 721, 401** ou **410**.
- **Diretor com FGTS - Motivo Desligamento:** **igual a** ('01','02','04','06').
- **Motivo Desligamento eSocial:** **igual a** ('02','03','05','06','14','17','23','26','27','33','47','48','49') - para empregados.
- **Ou** trabalhadores com **Situação igual a demitido**.

A **Base Rescisória (Sistema)** do relatório **S-5003** corresponde à soma dos valores dos eventos classificados como **proventos**, deduzidos os valores dos eventos classificados como **descontos**, considerado neste cálculo, apenas os eventos que estão devidamente configurados, atendendo ao seguinte critério: 

- **Evento** esteja marcado campo **Outros** =**FGTS**;
- **Evento** com **codIncFGTS** = 11 - Base de cálculo do FGTS mensal.

---

#### Regras de Apuração da Base Rescisória (eSocial)

A **Base Rescisória eSocial** é apurada pelo retorno do **S-5003** através do grupo **infoBaseFGTS** subgrupo **BASEPERAPUR**, considerando apenas as tags abaixo:

- INDINCID = **1 (Indicativo de incidência de FGTS)**
- **REMFGTS (Remuneração (valor da base de cálculo) do FGTS)**
- tpValor =  **{21, 24, 27, 30}**

---

#### Regras de Apuração do Valor Depósito Rescisório (Sistema)

Os mesmos critérios aplicados para a **Base Rescisória (Sistema)** são utilizados para **identificar os trabalhadores elegíveis** ao cálculo do **depósito**.

O **Depósito Rescisório (Sistema)** do relatório **S-5003** corresponde à soma dos valores dos eventos que estão devidamente configurado, atendendo simultaneamente aos seguintes critérios: 

- Característica = **FGTSNORMAL**
- Identificação do evento = **102 – Evento FGTS**
- Natureza = **9908**

---

#### Regras de Apuração do Valor Depósito Rescisório (eSocial)

O **Depósito Rescisório eSocial** é apurado pelo retorno do **S-5003** através do grupo **infoBaseFGTS** subgrupo **BASEPERAPUR**, considerando apenas as tags abaixo:

- INDINCID = **1 (Indicativo de incidência de FGTS)**
- **DPSFGTS (FGTS a ser depositado)**
- tpValor =  **{21, 24, 27, 30}**

---

#### Regras de Apuração da Base 13º Rescisória (Sistema)

Os mesmos critérios aplicados para a **Base Rescisória (Sistema)** são utilizados para **identificar os trabalhadores elegíveis** ao cálculo da **Base 13º Rescisória**.

A **Base 13º Rescisória (Sistema)** do relatório **S-5003** corresponde à soma dos valores dos eventos que estão devidamente configurado, atendendo ao seguinte critério: 

- **Evento** esteja marcado campo **Outros** =**FGTS 13°**;
- **Evento** com **codIncFGTS** = 12 - Base de cálculo do FGTS 13° salário.

---

#### Regras de Apuração da Base 13º Rescisória (eSocial)

A **Base 13º Rescisória eSocial** é apurada pelo retorno do **S-5003** através do grupo **infoBaseFGTS** subgrupo **BASEPERAPUR**, considerando apenas as tags abaixo:

- INDINCID = **1 (Indicativo de incidência de FGTS)**
- **REMFGTS (Remuneração (valor da base de cálculo) do FGTS)**
- tpValor =  **{22, 25, 28, 31}**

---

#### Regras de Apuração do Depósito 13º Rescisório (Sistema)

Os mesmos critérios aplicados para a **Base Rescisória (Sistema)** são utilizados para **identificar os trabalhadores elegíveis** ao cálculo do **Depósito 13º Rescisório.**

O **Depósito 13º Rescisório (Sistema)** do relatório **S-5003** corresponde à soma dos valores dos eventos que estão devidamente configurado, atendendo simultaneamente aos seguintes critérios: 

- Característica = **FGTS13SALARIO**
- Identificação do evento = **105 - Evento FGTS 13° Sal.Empregados**
- Natureza da Rubrica = **9908**

---

#### Regras de Apuração do Depósito 13º Rescisório (eSocial)

O **Depósito 13º Rescisório eSocial** é apurado pelo retorno do **S-5003** através do grupo **infoBaseFGTS** subgrupo **BASEPERAPUR**, considerando apenas as tags abaixo:

- INDINCID = **1 (Indicativo de incidência de FGTS)**
- **DPSFGTS(FGTS a ser depositado)**
- tpValor = **{22, 25, 28, 31}**

---

#### Regras de Apuração da Base Indenizatória (Sistema)

Os mesmos critérios aplicados para a **Base Rescisória (Sistema)** são utilizados para **identificar os trabalhadores elegíveis** ao cálculo da **Base Indenizatória.**

A **Base Indenizatória (Sistema)** do relatório **S-5003** corresponde à soma dos valores dos eventos que estão devidamente configurado, atendendo ao seguinte critério: 

- **Evento** esteja marcado campo **Outros** = **FGTS Rescisão**;
- **Evento** com **codIncFGTS = 21** - Base de cálculo do FGTS aviso prévio indenizado.

---

#### Regras de Apuração da Base Indenizatória (eSocial)

A **Base Indenizatória eSocial** é apurada pelo retorno do **S-5003** através do grupo **infoBaseFGTS** subgrupo **BASEPERAPUR**, considerando apenas as tags abaixo:

- INDINCID = **1 (Indicativo de incidência de FGTS)**
- **REMFGTS (Remuneração (valor da base de cálculo) do FGTS)**
- tpValor =  **{23, 26, 29, 32}**

---

#### Regras de Apuração do Depósito Indenizatório (Sistema)

Os mesmos critérios aplicados para a **Base Rescisória (Sistema)** são utilizados para **identificar os trabalhadores elegíveis** ao cálculo do **Depósito Indenizatório.**

O **Depósito Indenizatório (Sistema)** do relatório **S-5003** corresponde à soma dos valores dos eventos que estão devidamente configurado, atendendo simultaneamente aos seguintes critérios: 

- Característica = **FGTSRESCISORIO**
- Identificação do evento = **207 - Evento FGTS Indenizações**
- Natureza da Rubrica = **9908**

---

#### Regras de Apuração do Depósito Indenizatório (eSocial)

O **Depósito Indenizatório** é apurado pelo retorno do **S-5003** através do grupo **infoBaseFGTS** subgrupo **BASEPERAPUR**, considerando apenas as tags abaixo:

- INDINCID = **1 (Indicativo de incidência de FGTS)**
- **DPSFGTS(FGTS a ser depositado)**
- tpValor = **{23, 26, 29, 32}**

---

#### Regras de Apuração do FGTS Mensal Suspenso (Sistema)

Apresenta os valores de FGTS Mensal com exigibilidade suspensa por processo judicial.

Um evento somente será considerado no totalizador quando os trabalhadores se enquadrarem em pelo menos uma das seguintes condições:

**Categoria do Trabalhador e Regime Trabalhista**

- Empregado / Temporário: {codCateg} ∈ [1xx] e {tpRegTrab} = 1
- Trabalhador avulso / Diretor com FGTS (TSVE): {codCateg} ∈ [201, 202, 721]
- Agente Público: {tpRegTrab} = 1 e {codCateg} ∈ [3xx]
- Dirigente sindical / Trabalhador cedido (TSVE): {codCateg} ∈ [401, 410] e {tpRegTrab} = 1

**Colaboradores Demitidos**: poderão ser considerados, desde que não possuam motivos de desligamento:

- MTVDESLIGTSV = (01, 02, 04, 06)
- MOTDESLIGESOCIAL = (02, 03, 05, 06, 14, 17, 23, 26, 27, 33, 47, 48, 49)

Além disso, serão considerados apenas eventos:

- Da competência selecionada;
- Com FGTS = '**N**' e codIncFGTS = **91**;
- Vinculados a Processo Judicial.

---

#### Regras de Apuração do FGTS Mensal Suspenso (eSocial)

O **FGTS Mensal Suspenso** é apurado por meio do retorno do evento **S-5003**, grupo **infoBaseFGTS,** subgrupo **BASEPERAPUR,** para os eventos S-1200, S-2299 e S-2399.

Para composição do totalizador, serão consideradas apenas as seguintes informações:

- INDINCID = **9 (FGTS suspenso por decisão judicial)**
- **REMFGTS** (Remuneração base do FGTS)
- tpValor ∈ **(11,13,15,17,21,24,27,30,41,43,45,48)**
- Existência de processo judicial vinculado por meio da tag **ideProcessoFGTS tem nrProc vinculado**

---

#### Regras de Apuração do FGTS 13º Suspenso (Sistema)

Apresenta os valores de FGTS incidentes sobre o 13º salário cuja exigibilidade encontra-se suspensa por decisão judicial.

Um evento somente será considerado no totalizador quando os trabalhadores se enquadrarem em pelo menos uma das seguintes condições:

**Categoria do Trabalhador e Regime Trabalhista**

- Empregado / Temporário: {codCateg} ∈ [1xx] e {tpRegTrab} = 1
- Trabalhador avulso / Diretor com FGTS (TSVE): {codCateg} ∈ [201, 202, 721]
- Agente Público: {tpRegTrab} = 1 e {codCateg} ∈ [3xx]
- Dirigente sindical / Trabalhador cedido (TSVE): {codCateg} ∈ [401, 410] e {tpRegTrab} = 1

Serão considerados apenas eventos:

- Da competência selecionada;
- Com FGTS = '**N**' e codIncFGTS = **92;**
- Vinculados a Processo Judicial.

---

#### Regras de Apuração do FGTS 13º Suspenso (eSocial)

O FGTS 13º Suspenso é apurado por meio do retorno do evento **S-5003**, grupo **infoBaseFGTS**, subgrupo **basePerApur**, para os eventos **S-1200**, **S-2299** e **S-2399**.

Para composição do totalizador, serão consideradas apenas as seguintes informações:

- INDINCID **= 9 - Incidência de FGTS suspensa por decisão judicial**
- **REMFGTS** (Remuneração, ou seja, o valor da base de cálculo do FGTS)
- tpValor **∈ (12,14,16,18,22,25,28,31,42,44,46,49)**
- Existência de processo judicial vinculado por meio da tag **ideProcessoFGTS tem nrProc vinculado.**

---

#### Regras de Apuração do FGTS Aviso Indenizado Suspenso (Sistema)

Apresenta os valores de FGTS incidentes sobre o Aviso Prévio Indenizado cuja exigibilidade encontra-se suspensa por decisão judicial.

Um evento somente será considerado no totalizador quando os trabalhadores se enquadrarem em pelo menos uma das seguintes condições:

**Categoria do Trabalhador e Regime Trabalhista**

- Empregado / Temporário: {codCateg} ∈ [1xx] e {tpRegTrab} = 1
- Trabalhador avulso / Diretor com FGTS (TSVE): {codCateg} ∈ [201, 202, 721]
- Agente Público: {tpRegTrab} = 1 e {codCateg} ∈ [3xx]
- Dirigente sindical / Trabalhador cedido (TSVE): {codCateg} ∈ [401, 410] e {tpRegTrab} = 1

**Colaboradores Demitidos**: poderão ser considerados desde que possuam os seguintes motivos de desligamento:

- MTVDESLIGTSV = (01, 02, 04, 06)
- MOTDESLIGESOCIAL = (02, 03, 05, 06, 14, 17, 23, 26, 27, 33, 47, 48, 49)

Além disso, serão considerados apenas eventos:

- Da competência selecionada;
- Com FGTS = **N** e codIncFGTS = **93;**
- Vinculados a um Processo Judicial.

---

#### Regras de Apuração do FGTS Aviso Indenizado Suspenso (eSocial)

O FGTS Aviso Indenizado Suspenso é apurado por meio do retorno do evento **S-5003**, grupo **infoBaseFGTS**, subgrupo **basePerApur**, para os eventos **S-1200**, **S-2299** e **S-2399**.

Para composição do totalizador, serão consideradas apenas as seguintes informações:

- INDINCID = **9 - Incidência de FGTS suspensa em decorrência de decisão judicial**
- **REMFGTS** (Remuneração (valor da base de cálculo) do FGTS)
- tpValor ∈ **(23,26,29,32,47,50)**
- Existência de processo judicial vinculado por meio da tag **ideProcessoFGTS tem nrProc vinculado**

---

#### Coluna de Diferenças

Para cada estrutura do relatório S-5003, há uma coluna de **Diferença** que compara o valor do Sistema com o Valor do eSocial, facilitando a identificação de divergências com destaques no relatório.

**Como identificar as diferenças de valores:**

- **Sistema com valor** e **eSocial sem valor**
  Indica que os eventos de remuneração **S-1200, S-2299 ou S-2399** não foram enviados ao eSocial ou não foram retornados no S-5003. Nesse cenário, o eSocial não possui base para apuração, resultando na divergência.

  Caso o valor **não retorne** no **S-5003**, recomenda-se verificar no **eSocial** a configuração das rubricas, validando se estão corretamente classificadas e com as incidências parametrizadas de forma adequada.

  📚 Para conferir as incidências vigentes no eSocial, acesse: [Relatório de Conferência de Rubricas (S-1010)](https://ajuda.sankhya.com.br/hc/pt-br/articles/41258999019159). Se a incidência de FGTS do evento foi alterada e ainda não foi reenviada, reenvie o S-1010 antes de analisar novamente a divergência.
- **Sistema com valor maior que o Valor do eSocial**
  Indica a necessidade de verificar:
  - O que foi efetivamente considerado no cálculo pelo Sistema.
  - As configurações dos eventos que possuem incidência de **FGTS**, garantindo que a mesma incidência e classificação estejam corretamente configuradas para parte folha e eSocial.

---

#### Informações Importantes:

**(3)**Alíquotas aplicáveis exclusivamente quando indicativo de incidência de FGTS, é igual **"1 - Normal (incidência de FGTS)"** para conferir o valor do depósito.

- **8%** para **tpValor** = 11, 12, 13, 14, 21, 22, 23, 24, 25, 26;
- **2%** para **tpValor** = 15, 16, 17, 18, 27, 28, 29, 30, 31, 32;
- **3,2%** para **tpValor** = 41, 42, 43, 44, 45, 46, 47, 48, 49, 50.

**(3)**Código de incidência da rubrica para FGTS, configurado na aba eSocial, com os seguintes valores válidos de codIncFGTS:

00 - Não é base de cálculo do FGTS

11 - Base de cálculo do FGTS mensal

12 - Base de cálculo do FGTS 13° salário

21 - Base de cálculo do FGTS aviso prévio indenizado

31 - Desconto eConsignado

91 - Incidência suspensa em decorrência de decisão judicial - FGTS mensal

92 - Incidência suspensa em decorrência de decisão judicial - FGTS 13º salário

93 - Incidência suspensa em decorrência de decisão judicial - FGTS aviso prévio indenizado

**Lembrete:**

- Para utilização de código [91, 92, 93], é necessária a existência das informações relativas ao processo.
- A utilização do código [31] é obrigatória e exclusiva quando Natureza da Rubrica = [9253].

---

#### Possui empréstimo (Cred. Trabalhador)

O evento S-5003 também retorna dados sobre descontos da parcela do crédito do trabalhador (eConsignado) quando nos eventos S-1200, S-2299 ou S-2399 existir algum valor registrado em rubrica com natureza [9253].

Para isso, basta dá um duplo na linha do funcionário e o relatório será exibido.

[GIF animado: Imagem 8: Para isso, basta dá um duplo na linha do funcionário e o relatório será exibido.](https://ajuda.sankhya.com.br/hc/article_attachments/37220076886807)

Para saber mais detalhes, acesse: [Envio da folha como eConsignado para o eSocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/35831517422871-Lan%C3%A7amento-do-Cr%C3%A9dito-do-Trabalhador-no-Pessoal#h_01K88QC05E6H9YS8G26AW1ZYQ9).

## Artigos Relacionados

[Central do eSocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/7064222145175)

[Relatório S-5001: Contribuições sociais (INSS e PIS)](https://ajuda.sankhya.com.br/hc/pt-br/articles/36419467638551)

[Relatório S-5002 – Conferência de Imposto de Renda Retido na Fonte por Trabalhador](https://ajuda.sankhya.com.br/hc/pt-br/articles/37202771074071)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/36626761293591-Relat%C3%B3rio-S-5003-FGTS-por-trabalhador#top)
