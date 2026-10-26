---
id: "43753845412503"
titulo: "Agendador de Cálculos de Folha de Pagamento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43753845412503-Agendador-de-C%C3%A1lculos-de-Folha-de-Pagamento"
trilha: "Manual do Produto > Pessoas+ > Folha Mensal > Cálculo da Folha"
atualizado_em: "2026-09-25T18:50:06Z"
rotulos: ["FPHABTELAGECALC", "FPCALCFOLASYNC", "Agendador de Cálculos de Folha de Pagamento", "br.com.sankhya.mgepes.CalculoFolhaAgendador"]
---

# Agendador de Cálculos de Folha de Pagamento

**Módulo:** Pessoal+
**Versão Mínima:**5.126
**Caminho de Acesso:**Pessoal+ > Rotinas Folha
**ID da Tela:**br.com.sankhya.mgepes.CalculoFolhaAgendador

---

#### Sumário

1. [O que é o Agendador](https://ajuda.sankhya.com.br/hc/pt-br/articles/43753845412503-Agendador-de-C%C3%A1lculos-de-Folha-de-Pagamento#1-o-que-%C3%A9-o-agendador)
2. [Antes de começar](https://ajuda.sankhya.com.br/hc/pt-br/articles/43753845412503-Agendador-de-C%C3%A1lculos-de-Folha-de-Pagamento#2-antes-de-come%C3%A7ar)
3. [Como o agendamento funciona](https://ajuda.sankhya.com.br/hc/pt-br/articles/43753845412503-Agendador-de-C%C3%A1lculos-de-Folha-de-Pagamento#3-como-o-agendamento-funciona)
4. [Conhecendo a tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/43753845412503-Agendador-de-C%C3%A1lculos-de-Folha-de-Pagamento#4-conhecendo-a-tela)
5. [Como criar um agendamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/43753845412503-Agendador-de-C%C3%A1lculos-de-Folha-de-Pagamento#5-passo-a-passo-criar-um-agendamento)
6. [Como o sistema define a data de pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/43753845412503-Agendador-de-C%C3%A1lculos-de-Folha-de-Pagamento#6-como-o-sistema-define-a-data-de-pagamento)
7. [Alterar, pausar, duplicar e excluir](https://ajuda.sankhya.com.br/hc/pt-br/articles/43753845412503-Agendador-de-C%C3%A1lculos-de-Folha-de-Pagamento#7-alterar-pausar-duplicar-e-excluir)
8. [Conferir o resultado da execução](https://ajuda.sankhya.com.br/hc/pt-br/articles/43753845412503-Agendador-de-C%C3%A1lculos-de-Folha-de-Pagamento#8-conferir-o-resultado-da-execu%C3%A7%C3%A3o)
9. [Exemplos práticos](https://ajuda.sankhya.com.br/hc/pt-br/articles/43753845412503-Agendador-de-C%C3%A1lculos-de-Folha-de-Pagamento#9-exemplos-pr%C3%A1ticos)
10. [Solução de Problemas](https://ajuda.sankhya.com.br/hc/pt-br/articles/43753845412503-Agendador-de-C%C3%A1lculos-de-Folha-de-Pagamento#10-solu%C3%A7%C3%A3o-de-problemas)
11. [Perguntas Frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/43753845412503-Agendador-de-C%C3%A1lculos-de-Folha-de-Pagamento#11-perguntas-frequentes)

---

### 1. O que é o Agendador

O **Agendador de Cálculos de Folha** programa o cálculo da folha **Mensal** ou do **Adiantamento** para ser executado automaticamente nos dias e horários que você definir, para uma ou mais empresas.

Com ele, você não precisa lembrar de disparar o cálculo todo mês.

Por exemplo:

- calcular o **Adiantamento** todo dia 15, às 7h;
- calcular a **folha Mensal** todo dia 23, às 18h;
- programar mais de um horário para o mesmo dia, para que colaboradores que ainda estejam pendentes sejam calculados em uma nova execução.

| 💡 **Dica**  Pense no Agendador como um despertador do cálculo. Você define **quando** ele deve executar e **o que** deve calcular. No horário programado, o sistema executa o cálculo e registra o resultado. |
| --- |

O que a tela guarda:

Para cada agendamento, o sistema mantém:

- a **programação**, com meses, dias e horários de execução;
- as **configurações do cálculo**, como tipo de folha, data de pagamento e empresas;
- o **resultado de cada execução**, com a quantidade de folhas calculadas e as que apresentaram erro;
- o **log de alterações**, com o histórico das alterações realizadas no agendamento.

### 2. Antes de começar

Antes de utilizar o Agendador, verifique:

**Permissões:**

- se você tem acesso à tela **Agendador de Cálculos Folha de pagamento** (Pessoal+ > Rotinas Folha). Essa liberação é feita na tela **Acessos** (Configurações > Controle de Acesso), pelo administrador do sistema.

**Parâmetros:**

| Parâmetro | Para que serve | O que acontece se estiver desligado |
| --- | --- | --- |
| FPHABTELAGECALC | Exibe a tela no menu. | A tela não aparece no menu Rotinas Folha. |
| FPCALCFOLASYNC | Liga o cálculo em segundo plano, usado pelo agendador. | **Nada é calculado e nenhum aviso aparece.** O agendamento pode até mostrar status Finalizado, mas o Resumo fica vazio. |

Se você não tiver acesso aos parâmetros, solicite a configuração ao administrador do sistema.

**Configurações prévias:**

- **Referência aberta da empresa**

  O Agendador calcula a empresa somente quando a referência aberta no DP corresponde ao **mês atual** no momento da execução.
- **Cadastro de feriados**

  Quando a data de pagamento cai em um feriado, o sistema antecipa o pagamento para um dia útil anterior. Para que isso aconteça corretamente, os feriados precisam estar cadastrados na tela **Feriados** (Pessoal+> Cadastros).
- **Cidade da empresa**

  Os feriados são aplicados conforme a cidade informada no cadastro da **Empresa** (Configurações > Cadastros).

### 3. Como o agendamento funciona

Antes de criar o primeiro agendamento, é importante entender algumas regras. Elas ajudam a identificar por que uma empresa ou funcionário pode não ter sido calculado.

- #### O Agendador calcula somente quem está pendente

  A cada execução, o sistema calcula **apenas os funcionários que ainda não possuem cálculo** naquele tipo de folha e naquela competência.

  Isso significa que:

  - colaboradores que já foram calculados não são recalculados;
  - alterações feitas depois do cálculo não são aplicadas automaticamente aos colaboradores que já foram calculados;
  - uma nova execução pode calcular colaboradores que ficaram pendentes desde a execução anterior, como uma admissão lançada posteriormente.

  | **⚠️** **Atenção**  O Agendador não substitui o recálculo manual. Se você alterar um evento, uma regra da CCT, um reajuste ou outra informação que exija o recálculo de funcionários já calculados, utilize a rotina de cálculo manual da folha. |
  | --- |
- #### Quem entra no cálculo

  São considerados:

  - funcionários **ativos** da empresa;
  - funcionários admitidos **até o último dia do mês** da competência;
  - funcionários que ainda **não possuem cálculo** para o tipo de folha agendado;
  - funcionários transferidos, quando a transferência ocorre posteriormente à referência.
- #### Qual competência será calculada

  A competência é sempre o **mês atual no momento da execução**.

  A empresa só será calculada se a **referência aberta no DP for o mês atual**. Se a referência da empresa estiver em outro mês, ela será ignorada, **sem nenhuma mensagem de erro.**

  **Exemplo:**

  Se o Agendador executar em **3 de outubro**, mas a referência aberta da empresa ainda for **setembro**, a empresa não será calculada.

  Se a folha de setembro já estiver fechada e a referência tiver avançado para outubro, uma execução em outubro calculará **outubro**, e não setembro.
- #### Quando o cálculo é executado

  O sistema verifica os agendamentos **a cada minuto**.

  Quando encontra um agendamento **ativo** cuja **Próxima execução em** seja igual ou anterior ao horário atual, o cálculo é disparado.

  Depois de cada execução, mesmo que ocorra erro, o sistema calcula a próxima execução de acordo com a frequência configurada.

  Até **5 agendamentos** podem ser executados simultaneamente. Os demais aguardam na fila.

  **Se o servidor estiver indisponível no horário programado:** o cálculo será executado no primeiro minuto após o retorno do servidor.
- #### Quando nenhuma empresa é selecionada

  Se nenhuma empresa for adicionada ao agendamento, o cálculo será realizado para **todas as empresas com cadastro ativo na folha**.

  | 🚨 **Risco operacional**  Em bases com muitas empresas, essa configuração pode iniciar um cálculo grande e incluir empresas que não deveriam fazer parte daquela programação. Sempre que possível, selecione as empresas que devem ser calculadas. |
  | --- |

### 4. Conhecendo a tela

#### Listagem (grade)

Ao abrir a tela, os agendamentos aparecem em uma grade. Para abrir um agendamento, dê **duplo clique** sobre a linha.

| Coluna | O que mostra |
| --- | --- |
| Nro. agendamento | Código sequencial gerado pelo sistema. |
| Descrição agendamento | Nome atribuído ao agendamento. |
| Próxima execução em | Data e hora do próximo disparo. |
| Status Última Execução | Situação da última execução. Fica vazio enquanto o agendamento não tiver executado. |
| Ativo | Indica se o agendamento está ativo. |

| ℹ️ **Nota**  Agendamentos criados pela **BIA** também aparecem nesta grade. Quando não possuem descrição, são identificados como **Agendamento feito pela BIA**. |
| --- |

#### Barra de ferramentas

| Botão | Ação |
| --- | --- |
| Casa | Volta à tela inicial. |
| Funil | Abre os filtros da grade. |
| Grade / Formulário | Alterna entre a listagem e o formulário. |
| **+** (verde) | Cria um novo agendamento. |
| Lixeira | Exclui o agendamento selecionado. |
| Duplicar | Cria uma cópia do agendamento aberto. |
| Atualizar | Recarrega os dados. |
| Estrela | Adiciona a tela aos favoritos. |
| Documento (seta) | Exporta ou imprime. |
| Clipe | Anexos. |
| Engrenagem (seta) | Pesquisar campos, Layout do Formulário e Iniciar Tour. |

Durante a edição, ficam disponíveis os botões **Salvar [F7]** e **Descartar**.

| ℹ️ **Nota**  A tela não possui o botão **Executar agora**. Para realizar um cálculo imediatamente, utilize a rotina de cálculo manual da folha. |
| --- |

#### Cabeçalho

O cabeçalho fica disponível acima das abas.

| Campo | Como preencher |
| --- | --- |
| Nro. agendamento | Gerado automaticamente ao salvar. Não pode ser editado. |
| Descrição agendamento | Informe um nome que facilite a identificação. É recomendável informar a empresa, o tipo de folha e o dia. Ex.: `LOJON – Mensal – dia 23`. |
| Ativo | Ativa ou desativa a execução automática. |

#### Abas

**Geral**

Exibe o **Status Última Execução**, que informa se o agendamento já foi executado.

Para verificar quantos funcionários foram calculados e quantos apresentaram erro, consulte a aba **Resumo**.

**Horários**

Os campos dessa aba são preenchidos pelo sistema.

O campo **Próxima execução em** exibe Data e hora do próximo disparo. O sistema calcula esse valor a partir da frequência configurada.

Para parar o cálculo automático, desative o agendamento.

**Frequência Agendamento**

Define **em que horários**, **em que meses** e **em que dias** o cálculo roda. A execução só acontece quando os três coincidem.

- **Horários de execução**
  - **1ª execução:** informe o horário do primeiro disparo.
  - **+**: adiciona outro horário para o mesmo dia. Cada horário extra tem uma lixeira para removê-lo.
  - **Vassoura:** remove todos os horários cadastrados.

    Uma segunda execução no mesmo dia calcula somente os funcionários que ainda estiverem pendentes.
  - **Meses**

    Selecione os meses em que o agendamento deve executar:

    - **Jan** a **Dez**;
    - **Todos**.
  - **Periodicidade**

    Escolha uma das opções:

    | **Opção** | **Configuração** | **Quando executa** |
    | --- | --- | --- |
    | Diário | Não selecione dias específicos. | Todos os dias dos meses selecionados. |
    | Semanal | Selecione os dias da semana. | Nos dias da semana selecionados. |
    | Mensal | Selecione os dias de 1 a 31, **Último dia** ou **Todos**. | Nos dias do mês selecionados. |

    | 💡 **Dica**  Pense no Agendador como um despertador do cálculo. Você define **quando** ele deve executar e **o que** deve calcular. No horário programado, o sistema executa o cálculo e registra o resultado. |
    | --- |

**Configurações**

Define **o que será calculado**.

| **Campo** | **Opções** | **Regra** |
| --- | --- | --- |
| Tipo Folha | Mensal / Adiantamento | O padrão é **Mensal**. |
| Sugestão de data de pagamento | Até o 5º dia útil / Dentro do mês | A opção disponível depende do tipo de folha. |
| Dia do pagamento | Número | A faixa aceita depende da configuração da data de pagamento. |
| Empresa | Adicionar / Remover / Limpar | Define as empresas que participarão do cálculo. Se nenhuma for selecionada, serão consideradas todas as empresas ativas. |

Ao alterar o **Tipo Folha** ou a **Sugestão de data de pagamento**, o campo **Dia do pagamento** é limpo. Informe novamente o dia após realizar a alteração.

**Resumo**

Exibe o resultado das execuções do agendamento.

Os registros mais recentes aparecem primeiro.

**Log de alterações**

Registra as alterações realizadas no agendamento.

O detalhamento do resultado e do log está em [Como conferir o resultado](https://ajuda.sankhya.com.br/hc/pt-br/articles/43753845412503-Agendador-de-C%C3%A1lculos-de-Folha-de-Pagamento#8-conferir-o-resultado-da-execu%C3%A7%C3%A3o).

### 5. Como criar um agendamento

[GIF animado: Imagem 1: 5. Como criar um agendamento](https://ajuda.sankhya.com.br/hc/article_attachments/43760416693783)

Para programar um cálculo automático:

1. Clique em**+ Cadastrar Agendamento Tarefa**.
2. No cabeçalho:
   - preencha a **Descrição agendamento**;
   - ative a chave **Ativo**.
3. Na aba **Frequência Agendamento**:
   - informe o horário da **1ª execução**;
   - selecione os **meses** ou **Todos**;
   - escolha a periodicidade: **Diário**, **Semanal** ou **Mensal**;
   - marque os dias correspondentes.
4. Na aba **Configurações**:
   - selecione o **Tipo Folha**;
   - selecione a **Sugestão de data de pagamento**;
   - informe o **Dia do pagamento**, quando necessário;
   - clique em **Adicionar** e selecione as empresas. Se não selecionar nenhuma, o cálculo roda para **todas** as empresas ativas.
5. Clique em **Salvar [F7]**.

   Você não precisa preencher a **Próxima execução em** (aba Horários). O sistema calcula esse campo automaticamente com base na frequência configurada.
6. Depois do horário programado, acesse a aba **Resumo** para conferir o resultado da execução.

**Se não for possível salvar**

Algumas mensagens indicam problemas específicos:

- **“Já existe um agendamento ativo...”**

  Já existe um agendamento ativo para a mesma empresa e tipo de folha. Ajuste o agendamento existente ou verifique se ele deve ser excluído antes de criar outro.
- **“Dia do pagamento inválido para a referência selecionada.”**

  O dia informado não é válido para a combinação de tipo de folha e sugestão de pagamento selecionada.

### 6. Como o sistema define a data de pagamento

A data de pagamento é definida a partir de:

- **Tipo Folha**;
- **Sugestão de data de pagamento**;
- **Dia do pagamento**.

#### Combinações disponíveis

| Tipo Folha | Sugestão de pagamento | Mês do pagamento | Dia do pagamento | Preenchimento |
| --- | --- | --- | --- | --- |
| Mensal | Até o 5º dia útil | Mês **seguinte** à competência | 1 a 7 | Opcional |
| Mensal | Dentro do mês | **Mesmo mês** da competência | 8 a 31 | Informe o dia |
| Adiantamento | Dentro do mês (única opção) | **Mesmo mês** da competência | 1 a 31 | Informe o dia |

#### Até o 5º dia útil — folha Mensal

O pagamento acontece no **mês seguinte** à competência.

O **Dia do pagamento** é opcional:

| Dia do pagamento | Data sugerida |
| --- | --- |
| Vazio | 5º dia útil do mês seguinte. |
| 1 a 7 | O **menor** entre o dia útil informado e o 5º dia útil. |

**Exemplo:** para uma competência de setembro de 2026:

- sem informar o dia: pagamento no 5º dia útil de outubro;
- informar **3**: pagamento no 3º dia útil;
- informar **5**: pagamento no 5º dia útil;
- informar **7**: pagamento no 5º dia útil, porque 5 é menor que 7.

#### Dentro do mês — Mensal e Adiantamento

O pagamento acontece no **mesmo mês** da competência.

| Dia informado | Regra |
| --- | --- |
| Dia que existe no mês | Utiliza o próprio dia. |
| 29 ou 30, em mês que não tem esse dia | Antecipa para o último dia útil anterior. |
| 31 | Considera o último dia do mês, independentemente de o mês possuir 28, 29, 30 ou 31 dias. |

#### Antecipação da data

Quando necessário, o sistema aplica os ajustes nesta ordem:

1. Se **o dia informado não existir no mês**, aplica a regra correspondente a 29, 30 ou 31.
2. Se a data cair em um **fim de semana**, antecipa para a sexta-feira anterior.
3. Se a data cair em um **feriado**, antecipa para o primeiro dia útil anterior.

O resultado final é sempre um dia útil.

| ℹ️ **Nota**  O cadastro de feriados e a cidade da empresa precisam estar configurados para que a antecipação por feriado seja aplicada corretamente. |
| --- |

### 7. Como gerenciar os agendamentos

#### Alterar

1. Abra o agendamento.
2. Altere as informações necessárias.
3. Clique em **Salvar** **[F7]**.

A alteração será considerada na próxima execução e ficará registrada no **Log de alterações**.

#### Desativar

Para interromper temporariamente o cálculo automático:

1. Abra o agendamento.
2. Desligue a chave **Ativo**.
3. Salve.

As configurações permanecem salvas e podem ser reutilizadas quando o agendamento for ativado novamente.

#### Duplicar

Use **Duplicar** quando quiser reaproveitar uma configuração existente.

1. Abra o agendamento que deseja copiar.
2. Clique em **Duplicar**.
3. Altere a **Descrição agendamento**.
4. Ajuste a **Empresa** ou o **Tipo Folha**, conforme necessário.
5. Salve.

Se a cópia mantiver a mesma empresa e o mesmo tipo de folha de um agendamento ativo existente, o sistema poderá impedir o salvamento.

#### Excluir

Para excluir um agendamento:

1. Selecione o agendamento na grade.
2. Clique em **Lixeira**.

### 8. Como conferir o resultado

Depois que o agendamento executar, consulte a aba **Resumo**.

| **⚠️** **Atenção**  Erros no cálculo não geram notificação nem e-mail. Por isso, é importante conferir o resultado das execuções programadas. |
| --- |

Depois de cada execução, abra a aba **Resumo**:

| Coluna | O que conferir |
| --- | --- |
| Referência | Competência calculada, no formato MM/AAAA. |
| Tipo Folha | Mensal ou Adiantamento. |
| Qtd Folhas Carregadas | Quantidade de funcionários pendentes encontrados. |
| Qtd Folhas Calculadas | Quantidade de funcionários calculados com sucesso. |
| Qtd Folhas Cálculo Erro | Quantidade de funcionários que não foram calculados por erro. |
| Data Hora Início / Fim | Duração da execução. |

Também é possível consultar o detalhamento por **Cód. Empresa** e **Qtd Funcionários**.

Como referência para a conferência:

**Qtd Folhas Carregadas = Qtd Folhas Calculadas** e **Qtd Folhas Cálculo Erro = 0** indicam que não houve funcionários com erro nessa execução.

**Quando o Resumo fica vazio**

O Resumo recebe uma linha quando o cálculo chega a ser iniciado.

Ele pode permanecer vazio, mesmo com o status **Finalizado**, quando:

- a referência aberta da empresa não corresponde ao mês atual;
- não havia funcionários pendentes;
- o parâmetro FPCALCFOLASYNC estava desligado.

**Log de alterações**

O log permite verificar:

- número do log;
- data e hora da alteração;
- campo alterado;
- valor anterior;
- novo valor;
- usuário responsável pela alteração.

São registrados, entre outros, os seguintes campos:

- dias do mês;
- meses;
- dias da semana;
- sugestão de data de pagamento;
- dia do pagamento;
- empresas;
- Ativo;
- horários de execução.

Não são registrados:

- a criação do agendamento;
- alterações na descrição;
- alterações no tipo de folha;
- alterações na próxima execução.

Os campos podem aparecer com seus nomes técnicos. Por exemplo:

- MODOPAGAMENTO;
- DIAEXECUCAO.

As empresas são apresentadas pelos códigos separados por vírgula, como 1,22.

| ℹ️ **Nota**  O Log de alterações é mantido por **90 dias**. |
| --- |

### 9. Exemplos práticos

| Objetivo | Configuração |
| --- | --- |
| Calcular a folha Mensal todo dia 23, às 18h | Frequência: dia 23, às 18h; Tipo Folha: Mensal; Sugestão: Até o 5º dia útil; empresas selecionadas. |
| Calcular o Adiantamento no dia 15 e considerar pagamento no dia 20 | Frequência: dia 15, às 7h; Tipo Folha: Adiantamento; Sugestão: Dentro do mês; Dia do pagamento: 20. |
| Calcular a folha considerando o último dia do mês | Frequência: utilizar **Último dia**; Tipo Folha: Mensal; Sugestão: Dentro do mês. |
| Verificar admissões lançadas depois da primeira execução | Configure mais de um horário ou dia de execução no mesmo período. As novas execuções calcularão somente os funcionários que ainda estiverem pendentes. |
| Criar uma programação semelhante para outra empresa | Duplique o agendamento e altere a empresa e a descrição antes de salvar. |

| **⚠️** **Atenção**  O dia de execução precisa estar dentro do período em que a empresa possui a referência correspondente. Um agendamento executado no mês seguinte não recalcula automaticamente a competência anterior. |
| --- |

### 10. Solução de Problemas

- #### Agendei, mas não calculou

  Confira, nesta ordem:

  1. O agendamento está **Ativo**?
  2. O parâmetro FPCALCFOLASYNC está habilitado?
  3. A **referência aberta da empresa** corresponde ao mês atual?
  4. Existem funcionários **sem cálculo** para aquele tipo de folha?
  5. O **mês**, o **dia** e o **horário** configurados correspondem à data esperada?
  6. A **Próxima execução em** apresenta a data esperada?
- #### Calculou somente alguns funcionários

  Isso pode acontecer porque o Agendador calcula somente funcionários que ainda não possuem cálculo.

  Confira também a **Qtd Folhas Cálculo Erro** no Resumo. Funcionários com erro precisam ser analisados e, se necessário, calculados manualmente.
- #### Uma das empresas não foi calculada

  Confira a referência aberta dessa empresa.

  Se ela não corresponder ao mês atual, a empresa será ignorada sem mensagem de erro.
- #### O status está Finalizado, mas o Resumo está vazio

  Confira:

  - a referência aberta da empresa;
  - se havia funcionários pendentes;
  - se o parâmetro FPCALCFOLASYNC estava habilitado.
- #### A próxima execução está com uma data que já passou

  O sistema verifica os agendamentos a cada minuto e recalcula a próxima execução após cada processamento.

  Se a data permanecer no passado, pode haver um problema no serviço responsável pelo agendamento. Nesse caso, acione o suporte ou o administrador do servidor.
- #### Já existe um agendamento ativo para a empresa e tipo de folha

  Verifique se já existe um agendamento ativo para a combinação de **empresa + tipo de folha**.

  | **⚠️** **Atenção**  A trava não cobre todos os cenários de múltiplas empresas. Ela compara somente a primeira empresa da lista do agendamento que está sendo salvo e não é aplicada quando a lista está vazia, ou seja, quando o agendamento considera todas as empresas. Nesses casos, confira a grade antes de criar uma nova programação. |
  | --- |
- #### O dia do pagamento é inválido

  O valor informado não está dentro da faixa aceita para a combinação de **Tipo Folha** e **Sugestão de data de pagamento**.

  Consulte [Como o sistema define a data de pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/43753845412503-Agendador-de-C%C3%A1lculos-de-Folha-de-Pagamento#6-como-o-sistema-define-a-data-de-pagamento).
- #### A tela não aparece no menu

  Verifique se o parâmetro FPHABTELAGECALC está habilitado.
- #### O cálculo apresentou erro e ninguém foi avisado

  O Agendador não envia notificação nem e-mail.

  Crie o hábito de consultar a aba **Resumo** após as execuções programadas.

### 11. Perguntas Frequentes

**1. Consigo executar o agendamento imediatamente, sem esperar o horário programado?**

Não. A tela não possui a opção **Executar agora**. Para calcular a folha imediatamente, utilize a rotina de cálculo manual.

**2. O Agendador recalcula funcionários que já foram calculados?**

Não. O Agendador considera somente funcionários que ainda não possuem cálculo para o tipo de folha e a competência.

**3. O agendamento calcula uma folha já fechada?**

Não. Depois que a folha é fechada, a referência avança e a empresa deixa de corresponder à competência anterior.

**4. Como faço para o cálculo automático parar de executar?**

Desative a chave **Ativo** e salve o agendamento. As demais configurações serão mantidas.

**5. Posso programar mais de um horário por dia?**

Sim. Utilize o botão **+** na aba **Frequência Agendamento** para adicionar outros horários.

Cada execução adicional calcula somente os funcionários que ainda estiverem pendentes.

**6. Se eu não selecionar empresa, o que acontece?**

O cálculo roda para todas as empresas com cadastro ativo na folha.

**7. Posso ter um agendamento de Mensal e outro de Adiantamento para a mesma empresa?**

Sim. A combinação considerada para a trava é **empresa + tipo de folha**.

**8. O que acontece se o servidor estiver indisponível no horário programado?**

Quando o servidor voltar, o sistema verifica os agendamentos e executa o que estiver pendente no primeiro minuto disponível.

**9. Agendamentos criados pela BIA aparecem aqui?**

Sim. Quando não possuem descrição, aparecem como **Agendamento feito pela BIA**.

**10. Por quanto tempo o Log de alterações fica guardado?**

As informações do log são mantidas por **90 dias**.
