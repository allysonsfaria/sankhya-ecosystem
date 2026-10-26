---
id: "42634479723671"
titulo: "Como informar o contrato de trabalho no processo trabalhista"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42634479723671-Como-informar-o-contrato-de-trabalho-no-processo-trabalhista"
trilha: "Manual do Produto > Pessoas+ > Processos Trabalhistas > Processo Trabalhista no eSocial"
atualizado_em: "2026-10-02T17:46:13Z"
rotulos: ["Processo Trabalhista", "br.com.sankhya.ProcessoTrabalhista", "Informações do Contrato de Trabalho"]
---

# Como informar o contrato de trabalho no processo trabalhista

**Módulo:** Pessoal+
**Caminho de Acesso:** Pessoal+ > Rotinas Folha > Processo Trabalhista > Informações do Contrato de Trabalho
**Versão disponível:** A partir da 4.21
**ID da Tela:** br.com.sankhya.ProcessoTrabalhista

---

## Descrição e Usabilidade

### 1. Descrição da Funcionalidade

O menu **Informações do Contrato de Trabalho** permite registrar os contratos de trabalho relacionados ao processo trabalhista.

É possível cadastrar um ou mais contratos, conforme as informações reconhecidas ou determinadas no processo. O **Tipo de Contrato** selecionado define os campos e as informações que deverão ser preenchidos.

As informações cadastradas nessa etapa podem refletir no cadastro do colaborador e nos eventos enviados ao eSocial, conforme as características do processo e as alterações determinadas judicialmente.

### 2. Pré-requisitos

- Processo trabalhista previamente iniciado.
- Informações do trabalhador preenchidas.
- Dados do contrato de trabalho disponíveis para preenchimento.
- Decisão judicial ou demais documentos do processo disponíveis para consulta, quando houver alteração de informações do contrato.

### 3. Jornada de Uso

1. Acesse o **processo trabalhista cadastrado**.
2. No menu **Informações do Contrato de Trabalho**, clique em **Incluir novo contrato de trabalho**.

   [GIF animado: Imagem 1: No menu Informações do Contrato de Trabalho , clique em Incluir novo contrato de trabalho .](https://ajuda.sankhya.com.br/hc/article_attachments/42871436587543)
3. Selecione o **Tipo de Contrato** correspondente à situação determinada no processo:

   - 1 - Trabalhador com vínculo formalizado, sem alteração nas datas de admissão e de desligamento;
   - 2 - Trabalhador com vínculo formalizado, com alteração na data de admissão;
   - 3 - Trabalhador com vínculo formalizado, com inclusão ou alteração de data de desligamento;

     | ℹ️ **Nota**  Para situações em que a decisão judicial altera a data de desligamento para uma competência diferente da rescisão original, consulte o artigo [**Processo Trabalhista - Alteração de data de desligamento em competência diferente da rescisão original**](https://ajuda.sankhya.com.br/hc/pt-br/articles/42692991766807). |
     | --- |
   - 4 - Trabalhador com vínculo formalizado, com alteração nas datas de admissão e de desligamento;
   - 5 - Empregado com reconhecimento de vínculo;
   - 6 - Trabalhador sem vínculo de emprego/estatutário (TSVE), sem reconhecimento de vínculo empregatício;
   - 7 - Trabalhador com vínculo de emprego formalizado em período anterior ao eSocial;
   - 8 - Responsabilidade indireta;
   - 9 - Trabalhador cujos contratos foram unificados (unicidade contratual).

   | ℹ️ **Notas**  - Quando a marcação **Há responsabilidade indireta?** estiver habilitada no menu **Declarante**, ficam disponíveis somente os tipos de contrato **6 e 8**. - Para os processos trabalhistas com tipo de contrato **2** ou **4**, se houver uma [Comunicação de Acidente de Trabalho - CAT](https://ajuda.sankhya.com.br/hc/pt-br/articles/7067272406807) do tipo **1 (Inicial)** ou **3 (Óbito)** não será possível informar uma data de admissão posterior à data do óbito registrada na CAT. |
   | --- |
4. Preencha as informações apresentadas conforme o **Tipo de Contrato** selecionado.
   - **Informações sobre o contrato de trabalho enviados ao eSocial?**

     Essa marcação indica se as informações do contrato já foram enviadas ao eSocial pelos eventos **S-2190, S-2200 ou S-2300**.

     Ela é preenchida automaticamente para contratos dos tipos **1 a 4**, exceto quando houver responsabilidade indireta.

     A partir dessa informação, o sistema determina quais dados complementares do contrato deverão ser preenchidos.
   - **Data admissão original**

     É preenchida automaticamente quando houver indicação de que o trabalhador foi contratado pelo declarante.
   - **Data de Admissão (Decisão Judicial)**

     Para os tipos de contrato **2 e 4**, informe a **Data de Admissão (Decisão Judicial)** quando a decisão determinar alteração da data de admissão do trabalhador.

     Ao informar uma nova data de admissão, o sistema exibirá a mensagem:

     **"A nova data de admissão será atualizada no cadastro do funcionário após confirmar o cadastro do processo trabalhista."**

     Após a confirmação do processo, o sistema atualizará as informações correspondentes no cadastro do colaborador:

     - **Data de alteração S-2200**;
     - **Data admissão (decisão judicial)**;
     - **Indicativo de admissão**;
     - **Nº do processo p/ admissão por decisão judicial**).

     Se a alteração ocorrer após o envio das informações ao eSocial, poderão ser gerados eventos de retificação dos eventos **S-2200 e S-2500**.

     Se ocorrer antes do envio ao eSocial, os campos permanecerão sem preenchimento até que o evento seja transmitido.
   - **Data demissão (Decisão Judicial)**

     Para os tipos de contrato **3** e **4**, informe a **Data demissão (Decisão Judicial)** quando a decisão determinar a inclusão ou alteração da data de desligamento.

     Nesse caso, os valores da rescisão e a apuração dos tributos serão calculados dentro do respectivo processo através de depósito judicial ou DCTFWeb.

     Quando a marcação **Trabalhador contratado pelo declarante** do menu **Informações do Trabalhador**, estiver habilitada, também será apresentada a marcação **Incluir data de desligamento** e, abaixo dela, os campos **Data de desligamento** e **Tipo de Rescisão**.

     | **⚠️** **Atenção**  Se o colaborador possuir transferência, aviso prévio registrado ou cálculo de rescisão realizado, o sistema apresentará um alerta solicitando ajustes antes da alteração da data de desligamento. |
     | --- |

     Após a confirmação do processo, o sistema atualizará automaticamente as informações de desligamento nas telas:

     - **Configuração Funcionários**: Situação, Data demissão (Decisão Judicial), Nº Processo Trabalhista (desligamento), Data de Alteração S-2200 e Data de Alteração S-2299);
     - **Aviso Prévio**: Tipo Rescisão, Tipo Aviso (Dispensado), Fim das Atividades, Data Homologação e Nro. Processo Trabalhista;
     - **Cálculos**: ao tentar calcular a folha de rescisão para esse colaborador, será exibida a seguinte mensagem:
       **"Alerta!**
       **O funcionário selecionado foi demitido ou transferido!"**

     Se a **data de desligamento** já tiver sido enviada ao eSocial, serão geradas as retificações correspondentes (eventos S-2200 ou S-2299).

     Se for necessário excluir a informação, os eventos serão removidos na seguinte ordem:

     - S-2501 (se existir);
     - S-2500 (Processo Trabalhista);
     - S-2299 (retificação);
     - S-2200.

     Se o processo for removido, os dados alterados do colaborador serão retornados ao status anterior, conforme as regras do sistema.
   - **Houve reintegração?**

     Marque quando o colaborador for reintegrado à empresa.
   - **Houve reconhecimento de categoria do trabalhador diferente do eSocial/GFIP?**

     Quando a decisão judicial determinar o reconhecimento de uma categoria diferente daquela informada no eSocial/GFIP, marque **Houve reconhecimento de categoria do trabalhador diferente do eSocial/GFIP?**.

     O sistema exibirá o campo **Código Categoria do Trabalhador (Decisão Judicial)** para preenchimento.

     Após a confirmação do processo, o código informado será utilizado para atualizar o cadastro do colaborador e, quando aplicável, gerar as retificações correspondentes no eSocial:

     - se a alteração ocorrer no mesmo mês da admissão, o sistema retificará o **S-2200**;
     - se ocorrer em mês posterior ao mês de admissão, o sistema enviará o **S-2206**.
   - **Houve reconhecimento de natureza de atividade diferente da informada pelo declarante?**

     Quando a decisão judicial determinar uma natureza de atividade diferente daquela informada pelo declarante, marque **Houve reconhecimento de natureza de atividade diferente da informada pelo declarante?**.

     O sistema apresentará o campo **Natureza da atividade (Decisão Judicial)**.

     Após a confirmação do processo, a informação será atualizada no cadastro do colaborador e, quando aplicável, serão gerados os eventos de retificação correspondentes:

     - se a alteração ocorrer no mesmo mês da admissão, o sistema retificará o **S-2200**;
     - se ocorrer em mês posterior ao mês de admissão, o sistema enviará o **S-2206**.

       | **⚠️** **Atenção**  Quando o **Código Categoria do Trabalhador (Decisão Judicial)** for **104**, a opção **Trabalho Urbano** será selecionada automaticamente. Para o código **102**, será selecionada **Trabalho Rural**. |
       | --- |
   - **Houve reconhecimento de motivo de desligamento diferente da informada pelo declarante?**

     Quando a decisão judicial determinar um motivo de desligamento diferente daquele informado pelo declarante, marque **Houve reconhecimento de motivo de desligamento diferente da informada pelo declarante?**.

     Para os tipos de contrato **1** e **4**, quando também a marcação **Informações sobre o contrato de trabalho enviados ao eSocial?** estiver habilitada, o sistema apresentará o campo **Tipo Rescisão (Decisão Judicial)**.

     Após a confirmação do processo, as informações de desligamento correspondentes serão atualizadas no cadastro do colaborador:

     - **Causa do Afastamento**;
     - **Motivo do Afastamento para FGTS**;
     - **Motivo do Afastamento para RAIS**;
     - **Motivo de desligamento E-Social**;
     - **Número processo trabalhista (desligamento)**.

     Se o motivo de desligamento já tiver sido enviado ao eSocial e precisar ser alterado, serão gerados os eventos de retificação **S-2299** e **S-2500**.

     Caso o contrato de trabalho precise ser excluído, os eventos serão removidos na seguinte ordem:

     - S-2501 (se existir);
     - S-2500;
     - S-2299.
   - **Matrícula e Categoria do trabalhador**

     A **Matrícula do trabalhador** e o **Código Categoria do trabalhador** são preenchidos automaticamente quando as informações do contrato já estiverem disponíveis no cadastro do colaborador e as marcações **Informações sobre o contrato de trabalho enviados ao eSocial?** e **Trabalhador contratado pelo declarante**, do menu **Informações do Trabalhador**, estiverem habilitadas.

     Caso o trabalhador vinculado ao declarante possua evento **S-2300** enviado ao eSocial, mas não tenha matrícula cadastrada, informe a matrícula manualmente.

     Para contratos em que as informações não forem obtidas automaticamente, informe o **Código Categoria do trabalhador** conforme o cadastro do colaborador.

     Para o **Tipo de Contrato 6**, pode ser necessário informar também a **Data de início do TSVE**, conforme as condições do contrato e do envio ao eSocial.
5. Salve o cadastro.
6. Preencha as informações complementares conforme o contrato, quando aplicável.

   | **⚠️** **Atenção**  As seções **Informações Complementares**, **Informações Sobre Vínculo**,**Informações da Sucessão Trabalhista**e **Informações do Desligamento** devem ser preenchidas quando a marcação **Informações sobre o contrato de trabalho enviados ao eSocial?** não estiver habilitada. |
   | --- |

   - **Informações Complementares do Contrato de Trabalho**

     [GIF animado: Imagem 2: Informações Complementares do Contrato de Trabalho](https://ajuda.sankhya.com.br/hc/article_attachments/42871468592023)

     - **CBO**: quando o **Código Categoria do trabalhador** estiver com uma opção diferente de **901**, **903** e **904**.
     - **Natureza da atividade:** deve ser informada obrigatoriamente quando o **Código Categoria do trabalhador** for relativo à **Empregado**, **Agente Público**, **Avulso**ou igual aos códigos **401**, **731**, **734** e **738**.

       Para os códigos **721, 722, 771 e 901**, a **Natureza da atividade** não deverá ser indicada.

       Quando o **Código Categoria do trabalhador** for **104**, o sistema selecionará automaticamente a natureza **Trabalho Urbano**. Para o código **102**, será selecionado **Trabalho Rural**.
     - **Incluir Remunerações**

       Quando a marcação **Informações sobre o contrato de trabalho enviados ao eSocial?** estiver desabilitada, o **Tipo de Contrato** for diferente da opção **6** e o **Tipo de regime trabalhista** for CLT, ou ainda se o **Código Categoria do trabalhador** for **721**, **722** ou **771**, será possível incluir as remunerações relacionadas ao contrato.

       Clique em **Incluir Remuneração** e informe:

       - **Data início da remuneração**;
       - **Salário base;**
       - **Unidade de pagamento**.

       O campo **Descrição do salário variável** será exibido para pagamento **Por tarefa** ou **Salário exclusivamente variável**.
     - Salve as informações em **Finalizar Adição**.

       As remunerações serão apresentadas em modo grade, com possibilidade de edição ou exclusão.

       | **⚠️** **Atenção**  As **remunerações não deverão ser adicionadas** se o **Tipo de Contrato** for **6** e o **Tipo de regime trabalhista** for igual a **2 - Estatutário/legislações específicas (servidor temporário, militar, agente político, etc.)**. |
       | --- |
   - **Informações Sobre Vínculo**

     Preencha, quando aplicável:

     - **Tipo de regime trabalhista.**

       A opção **CLT - Consolidação das Leis de Trabalho e legislações trabalhistas específicas** será automaticamente selecionada quando o **Código Categoria do trabalhador** for **104**.
     - **Tipo de regime previdenciário.**

       A opção **RPPS - Regime Próprio de Previdência Social, Reg. Parlamentares e Sistema de Proteção dos Militares** será desabilitada, quando o **Código Categoria do trabalhador** for **101**, **102**, **103**, **105**, **106**, **107**, **108** ou **111**.
     - **Data de admissão;**
     - **Tipo de contrato em tempo parcial** apenas para trabalhadores com o **Tipo de regime trabalhista CLT**;
     - **Tipo de contrato de trabalho**;
     - **Data de término para contratos por prazo determinado**;
     - **Contrato por prazo determinado com cláusula assecuratória?** se o contrato por prazo determinado conter alguma cláusula assecuratória do direito recíproco de rescisão antes da data de seu término;
     - **Objeto determinante da contratação por prazo determinado** quando a contratação for por um prazo determinado, vinculado a ocorrência de um fato, como, por exemplo, obra, serviço, safra;
     - **Observações do contrato de trabalho** é destinado a qualquer tipo de informação pertinente ao contrato de trabalho.
     - Clique em **Finalizar Adição** para salvar.
   - **Informações da Sucessão Trabalhista**

     Quando houver sucessão trabalhista, informe:

     - **Tipo de inscrição**;
     - **Número de inscrição**;
     - **Matrícula anterior**;
     - **Data de transferência**;
     - Clique em **Finalizar Adição** para salvar.
   - **Informações do Desligamento**

     Quando aplicável, informe:

     - **Data do desligamento**;
     - **Motivo de desligamento**;
     - **Data fim do Aviso Prévio Indenizado**;

     Quando o **Tipo de regime trabalhista** for **CLT**, também serão apresentadas informações de pensão alimentícia para fins de retenção de FGTS.

     - **Indicativo de pensão alimentícia para fins de retenção de FGTS**;
     - **Percentual a ser destinado a pensão alimentícia**;
     - **Valor da pensão alimentícia**;
     - Clique em **Finalizar Adição** para salvar.
   - **Informações de término de Trabalhador Sem Vínculo Empregatício**

     Preencha quando o **Tipo de Contrat**o for **6 - Trabalhador sem vínculo de emprego/estatutário (TSVE), sem reconhecimento de vínculo empregatício**:

     - **Data de término** do contrato de trabalho;
     - **Motivo do término do diretor não empregado com FGTS** se o **Código Categoria do trabalhador** for **721**.
     - Clique em **Finalizar Adição** para salvar.
   - **Inclusão de Nova Categoria e/ou Natureza**

     [GIF animado: Imagem 3: Inclusão de Nova Categoria e/ou Natureza](https://ajuda.sankhya.com.br/hc/article_attachments/42871911527959)

     Quando as marcações **Houve reconhecimento de categoria do trabalhador diferente do eSocial/GFIP?** ou **Houve reconhecimento de natureza de atividade diferente da informada pelo declarante?** estiverem habilitadas, clique em **Incluir categoria/natureza** e preencha:

     - **Código Categoria do Trabalhador**;
     - **Natureza da atividade**;

       Quando o código for **104**, o sistema selecionará automaticamente **Trabalho Urbano**. Para o código **102**, será selecionado **Trabalho Rural**.

       Para os códigos **721, 722, 771 e 901**, o campo **Natureza da Atividade** ficará desabilitado.
     - **Data início da categoria ou natureza**.
     - Clique em **Salvar**.
   - **Reconhecimento Judicial de Unicidade Contratual**

     [GIF animado: Imagem 4: Reconhecimento Judicial de Unicidade Contratual](https://ajuda.sankhya.com.br/hc/article_attachments/42872091000087)

     Quando o **Tipo de Contrato** for **9 - Trabalhador cujos contratos foram unificados (unicidade contratual)**, clique em **Incluir Unicidade Contratual** e informe:

     - **Matrícula Incorporada;**
     - **Código Categoria do Trabalhador**;
     - **Data de início (TSVE)** correspondente ao período reconhecido.
     - Clique em **Salvar**.
   - **Empresa Responsável Pelo Pagamento ao Trabalhador**

     Informe os dados da empresa que será responsável por efetuar o pagamento do trabalhador:

     - **Tipo de inscrição**;
     - **Número de incrição**.
     - Salve as informações clicando em **Finalizar Adição**.
   - **Períodos decorrentes do processo trabalhista**

     [GIF animado: Imagem 5: Períodos decorrentes do processo trabalhista](https://ajuda.sankhya.com.br/hc/article_attachments/42872294083607)

     Preencha os dados do período decorrente ao processo trabalhista em questão:

     - **Competência inicial**;
     - **Competência final**;
     - **Indicativo de repercussão do processo trabalhista ou de demanda submetida à CCP ou ao NINTER**;
     - **Decisão p/ pgto da indenização do seguro-desemprego?**;
     - **Decisão p/ pgto da indenização de abono salarial?**;
     - Quando a opção de indenização do abono salarial estiver habilitada, é exibido o botão **Incluir Ano Base Abono Salarial** que deve ser acionado para inclusão dos anos-base correspondentes.
     - Clique em **Salvar**.
   - **Períodos Referente às Bases de Cálculo**

     [GIF animado: Imagem 6: Períodos Referente às Bases de Cálculo](https://ajuda.sankhya.com.br/hc/article_attachments/42872437638551)

     Clique em **Incluir Período Base de Cálculo** para informar os dados das bases de cálculos relacionadas ao processo:

     - **Período**;
     - **Base de cálculo da contribuição previdenciária - Remuneração**;
     - **Base de cálculo da contribuição previdenciária - 13º salário**;
     - **FGTS não declarado em SEFIP/eSocial reconhecido no proc. trabalhista**;
     - **FGTS declarado apenas em SEFIP (não em eSocial) e não recolhido**;
     - **FGTS declarado anteriormente no eSocial e não recolhido**;
     - **FGTS transacionado pago diretamente ao trabalhador?** (habilitada quando o valor do FGTS for pago diretamente ao trabalhador);
     - **Grau de exposição aos agentes nocivos**;
     - **Código Categoria do Trabalhador**;
     - **Valor da remuneração para fins previdenciários declarada em GFIP**.
     - Clique em **Salvar**.
7. Após preencher todas as informações aplicáveis ao contrato, clique em **Confirmar cadastro**.

   [GIF animado: Imagem 7: Após preencher todas as informações aplicáveis ao contrato, clique em Confirmar cadastro .](https://ajuda.sankhya.com.br/hc/article_attachments/42872618400023)

### 4. Pontos de Atenção

- O **Tipo de Contrato** deve corresponder à situação determinada no processo trabalhista.
- Os campos apresentados e sua obrigatoriedade variam conforme o tipo de contrato e as demais marcações selecionadas.
- Antes de alterar datas de admissão ou desligamento, verifique se existem eventos já enviados ao eSocial.
- Alterações judiciais atualizam informações no cadastro do colaborador e geram eventos de retificação no eSocial.
- Se o colaborador possuir transferência, aviso prévio registrado ou cálculo de rescisão realizado, alterações na data de desligamento podem exigir ajustes prévios.
- Para contratos do tipo **6**, a **Data de início do TSVE** possui regras específicas de preenchimento.
- As informações complementares, de vínculo, sucessão e desligamento devem ser preenchidas conforme as características do contrato.
- Para contratos cuja informação já foi enviada ao eSocial, observe quais dados precisam ser retificados antes de confirmar o processo.

### 5. Dicas de Usabilidade

- Tenha a decisão judicial em mãos antes de cadastrar as informações do contrato.
- Confirme o **Tipo de Contrato** antes de iniciar o preenchimento dos demais campos.
- Revise principalmente as datas de admissão, desligamento e início das alterações determinadas judicialmente.
- Quando houver alteração de categoria ou natureza da atividade, confira a data de início da alteração.
- Antes de confirmar o processo, revise as informações que poderão atualizar o cadastro do funcionário e os eventos do eSocial.

## Perguntas Frequentes (FAQ)

**1. Posso cadastrar mais de um contrato no mesmo processo?**

Sim. É possível cadastrar um ou mais contratos de trabalho no processo, conforme as informações reconhecidas ou determinadas na decisão.

**2. Quando devo utilizar os tipos de contrato 2 e 4?**

Utilize esses tipos quando houver alteração judicial da **data de admissão**. O tipo 2 corresponde à alteração da data de admissão, enquanto o tipo 4 contempla alteração das datas de admissão e desligamento.

**3. Quando devo utilizar os tipos 3 e 4?**

Utilize esses tipos quando houver inclusão ou alteração judicial da **data de desligamento**. O tipo 3 contempla a alteração do desligamento, enquanto o tipo 4 contempla alterações de admissão e desligamento.

**4. O que acontece quando altero a data de admissão por decisão judicial?**

Após a confirmação do processo, o sistema poderá atualizar as informações correspondentes no cadastro do funcionário. Quando aplicável, também serão gerados eventos de retificação no eSocial.

**5. O que acontece quando altero a data de desligamento?**

O sistema poderá atualizar as informações relacionadas ao desligamento no cadastro do funcionário e nas rotinas de **Aviso Prévio** e **Cálculos**, conforme as características do processo.

**6. Preciso preencher todas as seções do contrato?**

Não. As seções e campos apresentados dependem do **Tipo de Contrato** e das demais informações selecionadas. Preencha somente as informações aplicáveis ao processo.

## Artigos Relacionados

- [Cadastro de Processo Trabalhista](https://ajuda.sankhya.com.br/hc/pt-br/articles/42632245838871)
- [Informações de Tributos Decorrentes de Processo Trabalhista](https://ajuda.sankhya.com.br/hc/pt-br/articles/42834315267351)
- [Consulta e Exclusão de Processos Trabalhistas](https://ajuda.sankhya.com.br/hc/pt-br/articles/42844767586071)
