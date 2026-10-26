---
id: "5764158461847"
titulo: "Como calcular a rescisão"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/5764158461847-Como-calcular-a-rescis%C3%A3o"
trilha: "Manual do Produto > Pessoas+ > Rescisão > Cálculo da Rescisão por Tipo de Desligamento"
atualizado_em: "2026-10-21T13:06:51Z"
rotulos: ["Folha", "eSocial", "ID: br.com.sankhya.rh.CalculoIndFolha", "Gerenciador de Folhas", "Rescisão", "Cálculos", "Central do eSocial", "Projeção API", "Rescisão coletiva", "Rescisão individual", "FCEVECALCSPER", "FPBLANKTRCT", "Rescisão Coletiva: Processo para grupo", "Rescisão Complementar: Pagamento adicional", "Cálculos de Rescisão: Individual e coletivo", "FGTS", "FPRELATHOLRESC", "FPRELACORDRSC"]
---

# Como calcular a rescisão

```
 Módulo: Pessoal+ > Rotinas Folha              Versão disponível: A partir da 4.12
```

Por meio da tela [Cálculos](https://ajuda.sankhya.com.br/hc/pt-br/articles/20441795691031) são realizados todos os tipos de cálculos de folhas para funcionários e/ou empresas específicas de forma individual ou coletiva. Este artigo irá tratar sobre os cálculos de Rescisão.

Com a [Requisição de Rescisão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360059085273-Requisi%C3%A7%C3%B5es#Rescis%C3%A3o) aprovada ou o registro do [Aviso Prévio](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405017022231) cadastrado, pode-se realizar o cálculo da folha de rescisão do funcionário. Se houver mais de um funcionário com os mesmos dados de datas de pagamento é possível realizar o cálculo de forma coletiva.

| Cálculos de Rescisão | |
| --- | --- |
| [Rescisão Coletiva](https://ajuda.sankhya.com.br/hc/pt-br/articles/5764158461847-Como-calcular-a-rescis%C3%A3o#rescisaocoletiva) | [Rescisão Individual](https://ajuda.sankhya.com.br/hc/pt-br/articles/5764158461847-Como-calcular-a-rescis%C3%A3o#rescisaoindividual) |
| [Rescisão Complementar](https://ajuda.sankhya.com.br/hc/pt-br/articles/39447728136727) | [Pontos de Atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/5764158461847-Como-calcular-a-rescis%C3%A3o#01J0VEK9XD3WXHV7C6YPE2X9QM) |
| [Parâmetros que influenciam nesta rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/5764158461847-Como-calcular-a-rescis%C3%A3o#Par%C3%A2metrosqueinfluenciamnestarotina) |  |

---

### Rescisão Coletiva

Para realizar o processo de cálculo da rescisão coletiva de funcionários, inicialmente, selecione o tipo de Cálculo e Folha, acionando os botões **"Coletivo"** e **"Rescisão"**, respectivamente.

[GIF animado: Imagem 1: Para realizar o processo de cálculo da rescisão coletiva de funcionários, inicialmente, selecione o tipo de Cálculo e…](https://ajuda.sankhya.com.br/hc/article_attachments/24320092680087)

Em seguida, preencha as informações em cada etapa:

#### ![Imagem 2: - Informações Gerais](https://ajuda.sankhya.com.br/hc/article_attachments/42315322928663) - Informações Gerais

Preencha nesta etapa a **"Referência"**, a **"Data de Pagamento"** e  a **"Data da Demissão"**.

Ao selecionar o código de um funcionário que possua alguma Referência mensal anterior à data de demissão reaberta, uma mensagem surgirá informando:

**"As referência(s) abaixo estão abertas. Para correta apuração dos valores, é necessário que estejam finalizadas. Você quer prosseguir com a rescisão?"**

Ao selecionar a opção **"Sim"**, será possível finalizar a operação, se selecionar **"Não"**, a operação será cancelada.

#### ![Imagem 3: - Empresas](https://ajuda.sankhya.com.br/hc/article_attachments/42315322929559) - Empresas

Indique a **"Empresa"** que os funcionários pertencem.

#### ![Imagem 4: - Departamento](https://ajuda.sankhya.com.br/hc/article_attachments/42315322930839) - Departamento

Aqui, selecione os departamentos relacionados à Empresa definida na etapa anterior.

#### ![Imagem 5: - Funcionários](https://ajuda.sankhya.com.br/hc/article_attachments/42315329120791) - Funcionários

Selecione os **"Funcionários"** que serão desligados da empresa. No card de cada funcionário será indicado se o mesmo já está com **"Aviso Prévio cadastrado"**.

#### ![Imagem 6: - Informações Rescisão/Aviso Prévio](https://ajuda.sankhya.com.br/hc/article_attachments/42315329128855) - Informações Rescisão/Aviso Prévio

Nesta etapa, preencha as informações referente ao tipo de rescisão e aviso prévio nas seções abaixo:

**Info. Tipo Rescisão**

Selecione o tipo de rescisão de acordo com as opções abaixo:

- Demissão Sem Justa Causa - Inic. Empresa;
- Demissão a Pedido S/ Justa Causa;
- Término de Contrato;
- Demissão Por Justa Causa - Inic. Empresa;
- Quebra de Contrato - Inic. Empresa;
- Quebra de Contrato - A Pedido;
- Demissão Por Aposent. por Tempo de Serv.;
- Demissão Por Aposentadoria por Idade;
- Demissão Por Invalidez;
- Rescisão por Culpa Recíproca;
- Rescisão por Falecimento;
- Demissão Sem Justa Causa - Por acordo.

**Observação:** outros tipos de rescisão podem ser cadastrados na tela [Tipo de Rescisão](https://ajuda.sankhya.com.br/hc/pt-br/articles/13737586332695). Além da tela de Cálculos da Rescisão (Individual e Coletivo), os mesmos serão exibidos na tela [Aviso Prévio](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405017022231) e na [Requisição de Rescisão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360059085273-Requisi%C3%A7%C3%B5es#Rescis%C3%A3o). É aconselhável seguir os tipos de rescisão listados pelo e-Social na Tabela 19- Motivos de Desligamento.

Efetue a marcação **"Programa de Demissão Voluntária"** caso o funcionário seja desligado através da adesão ao Programa de Demissão Voluntária para dispensa individual ou coletiva, que pode ser previsto em CCT ou ACT, conforme [Art. 477-B](https://www.planalto.gov.br/ccivil_03/Decreto-Lei/Del5452.htm#art477b) da CLT. É importante ressaltar que, esta marcação só será habilitada quando o código do motivo de desligamento do eSocial for diferente dos códigos: **"10"**, **"11"**, **"12"**, **"13"**, **"28"**, **"29"**, **"30"**, **"34"**, **"36"**, **"37"**, **"40"**, **"43"** e **"44"**. 

**FGTS**

Marque a opção **Calcula Mês Anterior** se desejar que o FGTS da competência anterior ao mês da rescisão seja calculado separadamente, e não junto com a folha mensal.

- Se a opção **não** estiver marcada, o valor do FGTS da competência anterior é gerado normalmente na folha mensal.
- Se a opção estiver marcada, a folha mensal sai **sem** o valor de FGTS do mês anterior, e esse valor será apresentado na referência seguinte, dentro do resumo de rescisão, no campo **25 - Mês Anterior a Rescisão** da GRRF.

Quando o dia da data de rescisão for **menor que 10**, o sistema marca essa opção automaticamente, seguindo a regra do FGTS Digital. Essa marcação automática não bloqueia o campo: você pode desmarcá-la manualmente, se for necessário para o seu caso.

**Tipo**

Indique se o aviso prévio foi **"Trabalhado"**, **"Indenizado"** ou **"Dispensado"**.

Informe as datas referente a **"Recebimento Aviso Desligamento"**, **"Início do Aviso Prévio"**, **"Fim das atividades"**, **"Homologação"** e **"Quitação Rescisão"**.

Selecione no campo **"Iniciativa"**, se a **"Empresa"** ou o **"Funcionário"** que optou pelo desligamento.

**Indicador de Cumprimento Aviso Prévio**

Determine o cumprimento do aviso prévio, conforme abaixo:

- Total;
- Parcial (Novo Emprego);
- Parcial (Iniciativa Empregador);
- Parcial (Outras Hipóteses);
- Indenizado / Não Exigível.

**Observação:** caso preencha os dados da rescisão e aviso prévio direto na tela Cálculos, sendo o Tipo de aviso prévio, Trabalhado e o Indicador de aviso prévio for marcado como cumprimento Parcial (Iniciativa Empregador), será exibida a seguinte mensagem:

**"Atençao!**
**Preencher os dias a serem indenizados diretamente na tela Aviso Prévio.**
**Prosseguindo com o cálculo sem preenchimento serão considerados os dias acima de 30 como indenizados."**

**Campos HomologNet**

Defina se no cumprimento do aviso prévio será considerado como **"Semana da Rescisão Integral"** ou **"Compensa Sábado"**.

**Importante:** todas as informações desta etapa serão preenchidas automaticamente se estiverem sido cadastradas anteriormente na tela Aviso Prévio. Assim, ao selecionar apenas funcionários que tenham aviso prévio cadastrado, esta etapa será desabilitada e avançada diretamente para o cálculo.
Caso selecione funcionários com aviso prévio cadastrado e não cadastrado, será exibida a mensagem abaixo alertando que os dados preenchidos diretamente no Cálculo valerão apenas para os funcionários sem aviso prévio cadastrado no sistema:

**"Atenção!**
**Os dados preenchidos nesta tela valerão apenas para os funcionários que não possuem aviso prévio cadastrado no sistema."**

Assim, após preencher todos os dados, pode-se avançar para a próxima etapa.

#### ![Imagem 7: - Calcular](https://ajuda.sankhya.com.br/hc/article_attachments/42315329129623) - Calcular

Agora, efetue o cálculo das rescisões solicitadas clicando no botão **"Calcular"**.

![Imagem 8: Agora, efetue o cálculo das rescisões solicitadas clicando no botão "Calcular" .](https://ajuda.sankhya.com.br/hc/article_attachments/18757373751447)

![Imagem 9: Ao acionar o botão Calcular , caso exista algum evento enviado com sucesso ao eSocial após a Data da Demissão , será…](https://ajuda.sankhya.com.br/hc/article_attachments/16536878753047) Ao acionar o botão Calcular, caso exista algum evento enviado com sucesso ao eSocial após a Data da Demissão, será exibida uma mensagem informando que será necessário realizar a análise e a exclusão desse evento através da [Central do eSocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/7064222145175) antes do envio do S-2299. 

Após a finalização, realize a conferência na tela [Gerenciador de Folhas](https://ajuda.sankhya.com.br/hc/pt-br/articles/4424800696599), onde poderá visualizar os cálculos realizados e emitir os relatórios, como, **"Aviso Prévio"**, **"Rescisão"**, **"Termo de Homologação de Rescisão"** e **"Termo de Quitação de Rescisão"**.

![Imagem 10: Após a finalização, realize a conferência na tela Gerenciador de Folhas , onde poderá visualizar os cálculos realizados…](https://ajuda.sankhya.com.br/hc/article_attachments/18603097727383)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5764158461847-Como-calcular-a-rescis%C3%A3o#top)

---

### Rescisão Individual

Para efetuar o cálculo de rescisão individual de funcionários, comece selecionando o tipo de cálculo e folha, clicando nos botões **"Individual"** e **"Rescisão"**, respectivamente, e preencha as informações de cada etapa:

[GIF animado: Imagem 11: Para efetuar o cálculo de rescisão individual de funcionários, comece selecionando o tipo de cálculo e folha, clicando…](https://ajuda.sankhya.com.br/hc/article_attachments/24320347430423)

#### Imagem 12: - Informações Gerais - Informações Gerais

Selecione nesta etapa a **"Referência"**, **"Data de Pagamento"**, **"Empresa"**, **"Funcionário"** e **"Data de Demissão"**.

Ao selecionar o código de um funcionário que possua alguma Referência mensal anterior à data de demissão reaberta, uma mensagem surgirá informando:

**"As referência(s) abaixo estão abertas. Para correta apuração dos valores, é necessário que estejam finalizadas. Você quer prosseguir com a rescisão?"**

Ao selecionar a opção **"Sim"**, será possível finalizar a operação, se selecionar **"Não"**, a operação será cancelada.

#### ![Imagem 13: - Info Tipo Rescisão e FGTS](https://ajuda.sankhya.com.br/hc/article_attachments/42315322929559) - Info Tipo Rescisão e FGTS

Nesta etapa, preencha as informações referente ao [Tipo de Rescisão](https://ajuda.sankhya.com.br/hc/pt-br/articles/13737586332695) e FGTS nas seções abaixo:

**Info. Tipo Rescisão**

Informe o Tipo de Rescisão de acordo com as opções abaixo:

- Demissão Sem Justa Causa - Inic. Empresa;
- Demissão a Pedido S/ Justa Causa;
- Término de Contrato;
- Demissão Por Justa Causa - Inic. Empresa;
- Quebra de Contrato - Inic. Empresa;
- Quebra de Contrato - A Pedido;
- Demissão Por Aposent. por Tempo de Serv.;
- Demissão Por Aposentadoria por Idade;
- Demissão Por Invalidez;
- Rescisão por Culpa Recíproca;
- Rescisão por Falecimento;
- Demissão Sem Justa Causa - Por acordo.

Efetue a marcação **"Programa de Demissão Voluntária"** caso o funcionário seja desligado através da adesão ao Programa de Demissão Voluntária para dispensa individual ou coletiva, que pode ser previsto em CCT ou ACT, conforme [Art. 477-B](https://www.planalto.gov.br/ccivil_03/Decreto-Lei/Del5452.htm#art477b) da CLT. É importante ressaltar que, esta marcação só será habilitada quando o código do motivo de desligamento do eSocial for diferente dos códigos: **"10"**, **"11"**, **"12"**, **"13"**, **"28"**, **"29"**, **"30"**, **"34"**, **"36"**, **"37"**, **"40"**, **"43"** e **"44"**.

**FGTS**

Marque a opção **Calcula Mês Anterior** se desejar que o FGTS da competência anterior ao mês da rescisão seja calculado separadamente, e não junto com a folha mensal.

- Se a opção **não** estiver marcada, o valor do FGTS da competência anterior é gerado normalmente na folha mensal.
- Se a opção estiver marcada, a folha mensal sai **sem** o valor de FGTS do mês anterior, e esse valor será apresentado na referência seguinte, dentro do resumo de rescisão, no campo **25 - Mês Anterior a Rescisão** da GRRF.

Quando o dia da data de rescisão for **menor que 10**, o sistema marca essa opção automaticamente, seguindo a regra do FGTS Digital. Essa marcação automática não bloqueia o campo: você pode desmarcá-la manualmente, se for necessário para o seu caso.

**Importante:** todas as informações desta etapa serão preenchidas automaticamente se estiverem sido cadastradas anteriormente na tela [Aviso Prévio](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405017022231).  

#### Imagem 14: - Desligamento - Desligamento

O preenchimento desta etapa se dá, em casos de decisão judicial, falecimento de funcionário ou exoneração de diretores.

Descreva o **"Processo de Deslig. por Decisão Judicial"**, se a rescisão tiver ocorrido por decisão judicial.

Em caso de falecimento do funcionário, informe o **"Número da certidão de óbito"**.

Preencha o **"Nro processo de término de TSVE por decisão judicial"** se for término de contrato de Trabalhador Sem Vínculo de Emprego/Estaturário.

O campo **"Motivo do desligamento"** estará habilitado para edição apenas quando no cadastro do funcionário, aba [Admissão](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639-Configura%C3%A7%C3%A3o-Funcion%C3%A1rios#admisso), o **"Código de Categoria para o eSocial"** do trabalhador estiver com a opção **"721-CONTRIBUINTE INDIVIDUAL - DIRETOR NÃO EMPREGADO, COM FGTS"** selecionada. Além disso, após a confirmação do cálculo, o mesmo Motivo do desligamento será preenchido automaticamente na aba [Afastamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639-Configura%C3%A7%C3%A3o-Funcion%C3%A1rios#afastamento) da tela [Configuração Funcionários](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639).

As **"Informações de remuneração após o desligamento"** deverão ser preenchidas para funcionários que terão remuneração após o desligamento. Para isso, selecione o **"Indicativo de situação de remuneração após desligamento"** de acordo com as seguintes opções:

- Desligamento/Termino legal com data anterior a competências com remunerações informadas no eSocial;
- Quarentena.

**Nota:** as Informações de remuneração após o desligamento serão preenchidas nessa tela automaticamente se estiverem sido cadastradas na tela Aviso Prévio anteriormente. 

Preencha a **"Data fim remuneração"** considerando que, no caso do indicativo igual a Quarentena, deve ser uma data superior à data de desligamento/término do funcionário, e precisa ser a data do último dia trabalhado quando o indicativo for igual a Desligamento/Termino legal com data anterior a competências com remunerações informadas no eSocial.

**Importante**

- O **evento de DSR sobre a hora extra** pode **não retornar valores** quando a variável `DIASNAOUTEISTRAB` estiver com valor **0 (zero)**. Isso normalmente ocorre **em casos de desligamento**, pois **não há dias úteis após a data de demissão**.
- Já, o **evento de DSR na Rescisão** depende de condições específicas para retornar valores:

  1. A **causa do afastamento** (`&CAUAFA`) **não pode ser igual a 63** (rescisão por término de contrato determinado).
     Exemplo de regra: `IF(&CAUAFA = 63, 0, ...)`
  2. Além disso, o valor será gerado **somente se**:

     - O **dia da semana da data** calculada com: **Data de Demissão + Dias de Aviso - Dias de Descumprimento do Aviso for uma sexta-feira** e a variável `COMPENSASABADO = 'S'`;
       OU
     - O **dia da semana da Data de Demissão** for **sábado**.

#### Imagem 15: - Aviso Prévio - Aviso Prévio

Nesta etapa, preencha as informações referente ao aviso prévio nas seções abaixo:

**Tipo**

Indique se o aviso prévio foi **"Trabalhado"**, **"Indenizado"** ou **"Dispensado"**.

Informe as datas referente a **"Recebimento Aviso Desligamento"**, **"Data Início do Aviso Prévio"**, **"Fim das atividades"**, **"Data da Homologação"** e **"Quitação Rescisão"**.

Selecione no campo **"Iniciativa"**, se a **"Empresa"** ou o **"Funcionário"** que optou pelo desligamento.

Preencha o **"Número de dias para Aviso Prévio"**.

**Indicador de Cumprimento Aviso Prévio**

Determine o cumprimento do aviso prévio conforme abaixo:

- Total;
- Parcial (Novo Emprego);
- Parcial (Iniciativa Empregador);
- Parcial (Outras Hipóteses);
- Indenizado / Não Exigível.

**Campos HomologNet**

Defina se no cumprimento do aviso prévio será considerado como **"Semana da Rescisão Integral"** ou **"Compensa Sábado"**.

#### Imagem 16: - Calcular - Calcular

Por fim, defina no campo **"Modo de cálculo"** se deseja **"Calcular com log"**, **"Calcular sem log"** ou **"Calcular com log de incorporações"**, visto que, a opção Calcular com log é a opção padrão desse campo e acione o botão Calcular.

No Log serão apresentados os dados das fórmulas principais e suas auxiliares, as variáveis utilizadas no cálculo e logo abaixo, os valores das funções contidas em cada uma delas. 

**Observação:** se existir na fórmula a chamada de algum Evento através das variáveis &E ou &F, este será apresentado em formato de link para visualização dentro do próprio Log. Caso o Evento não possua fórmula associada, será exibida uma mensagem informando que a fórmula está vazia. É possível acessar quantos Logs forem necessários e retornar ao Log inicial da consulta.  

Para facilitar a conferência de valores, pode-se ainda exportar o Log de cálculo das fórmulas para o arquivo TXT por meio da opção **"Download do log"**. Esse arquivo será salvo com o nome **"LOGCALC\_MESEANOREF\_TIPO DE FOLHA.TXT"**.  

![Imagem 17: Ao acionar o botão Calcular , caso exista algum evento enviado com sucesso ao eSocial após a Data da Demissão , será…](https://ajuda.sankhya.com.br/hc/article_attachments/16536878753047) Ao acionar o botão Calcular, caso exista algum evento enviado com sucesso ao eSocial após a Data da Demissão, será exibida uma mensagem informando que será necessário realizar a análise e a exclusão desse evento através da [Central do eSocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/7064222145175) antes do envio do S-2299.  

Realize a [conferência da folha](https://ajuda.sankhya.com.br/hc/pt-br/articles/20441795691031-C%C3%A1lculos#Confer%C3%AAnciaindividualdafolha) e, estando tudo certo, clique em Confirmar Folha. Logo após, poderá emitir os relatórios, como, Aviso Prévio, Rescisão, Termo de Homologação de Rescisão e Termo de Quitação de Rescisão.

![Imagem 18: Realize a conferência da folha e, estando tudo certo, clique em Confirmar Folha . Logo após, poderá emitir os…](https://ajuda.sankhya.com.br/hc/article_attachments/18603097727383)

**Importante:** para confirmar uma folha de rescisão zerada é necessário que o lançamento de algum evento/movimento demonstrativo seja realizado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5764158461847-Como-calcular-a-rescis%C3%A3o#top)

### Pontos de Atenção

- Quando houver **cálculo de folha mensal processado na mesma competência da demissão**, é necessário **excluir o cálculo da folha mensal antes de realizar o cálculo da rescisão**.

  O sistema bloqueia o cálculo da rescisão enquanto existir uma folha mensal processada para a mesma competência.

  Para realizar a rescisão:

  1. Acesse a tela **Gerenciador de Folhas** (Pessoal+ > Rotinas Folha).
  2. Localize a folha mensal da competência da demissão.
  3. Exclua o cálculo da folha mensal.
  4. Retorne à rotina de **Cálculos** e realize o cálculo da rescisão.
- Caso ocorra o desligamento do colaborador durante um [Processo Trabalhista](https://ajuda.sankhya.com.br/hc/pt-br/articles/11592868813719), cujo o **Tipo de Contrato** seja **3 - Trabalhador com vínculo formalizado, com inclusão ou alteração de data de desligamento** ou **4 - Trabalhador com vínculo formalizado, com alteração nas datas de admissão e de desligamento**, o sistema não permitirá que o cálculo de rescisão individual ou coletiva seja efetuado, pois os valores dessa rescisão e a apuração dos tributos serão realizados dentro do processo através de depósito judicial ou DCTFWeb.
- O nome social do colaborador será exibido nos relatórios de rescisão quando informado no [cadastro do funcionário](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639-Configura%C3%A7%C3%A3o-Funcion%C3%A1rios#pessoais), garantindo o respeito à identidade de gênero conforme o Decreto nº 8.727/2016, que assegura o uso do nome social por pessoas travestis e transexuais.

  O uso do nome social é permitido após validação do CPF na Receita Federal.

  Relatórios contemplados:

  - Aviso Prévio (com ou sem cumprimento);
  - Termo de Rescisão do Contrato de Trabalho (TRCT);
  - Termo de Quitação e Homologação da Rescisão;
  - Comunicação de Dispensa para Seguro-Desemprego (SD).
- Se um evento calculado na rescisão não aparece no Termo de Rescisão do Contrato de Trabalho (TRCT), associe-o a um campo livre do termo na tela **Regras de Cálculo**, aba **TRCT**, sub-aba **Eventos**: campos 95.1 a 95.40 para proventos e 115.1 a 115.40 para descontos.

  📚 Configure isso em: [Configuração das Regras de Cálculos](https://ajuda.sankhya.com.br/hc/pt-br/articles/39936375428503#eventos-fora-do-trct).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5764158461847-Como-calcular-a-rescis%C3%A3o#top)

---

### Parâmetros que influenciam nesta rotina

**Cód. Eventos para ñ aplicar reajuste no calculo - FCEVECALCSPER:** neste parâmetro deve-se inserir os eventos que não estão sujeitos à aplicação do percentual de reajuste e ainda os eventos de médias para que eles tenham suas fórmulas refeitas. Assim, o evento S-9010 deve estar listado nesse parâmetro, para que o evento INSS seja recalculado com as recomposições de base.

**Hab. linhas vazias no TRCT - FPBLANKTRCT:** com este parâmetro ligado, as células com valores e descrição zerados do holerite de rescisão serão desconsideradas na geração do relatório.

**Código Relatório Termo Acordo Rescisão - FPRELACORDRSC**: neste parâmetro deve-se inserir o código do Relatório Formatado para definir o modelo do termo de Rescisão por Acordo.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5764158461847-Como-calcular-a-rescis%C3%A3o#top)
