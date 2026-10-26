---
id: "42427347938839"
titulo: "Como cadastrar um empregado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427347938839-Como-cadastrar-um-empregado"
trilha: "PONTOTEL: Sistema de marcação de ponto > Cadastros"
atualizado_em: "2026-08-07T16:17:36Z"
rotulos: ["sync_hc", "pontotel", "pontotel_6a33ee0e5d900db61039b68c", "sync_hash_f4178729170a"]
---

# Como cadastrar um empregado

Neste artigo, vamos mostrar como cadastrar um novo empregado, detalhando cada campo essencial para garantir que todos os dados estejam completos e ajustados às necessidades da sua empresa. Com um cadastro bem estruturado, você terá armazenado todos os dados cadastrais do seu colaborador, relevantes para uma boa gestão da folha, marcação de pontos e a organização de benefícios, promovendo uma experiência de trabalho ainda mais eficiente.

---

## Como cadastrar um empregado:

1. No menu de navegação do[site Gestão](https://gestao.pontotel.com.br/), clique em **Cadastros**. Depois selecione a opção **Empregados**.
2. Clique em **Criar novo empregado**.

   ![Imagem 1: Clique em Criar novo empregado .](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1h4ckre.png)
3. Preencha os campos principais:

   - **Nome:** Insira o nome completo do empregado. Para a exportação correta do AFD, o nome deve ter no máximo 25 caracteres.
   - **Código:** Insira um código para identificar o colaborador, como a matrícula ou um número interno utilizado pela sua empresa. Esse campo é especialmente importante se houver integração com outros sistemas, pois o código deve ser o mesmo utilizado nesses sistemas. Para levar informações de apontamentos de um sistema para o outro, é essencial que seja o mesmo código registrado no sistema de folha de pagamento, garantindo consistência e correta sincronização dos dados.
   - **PIN para registro do ponto:** O PIN deve ter no mínimo **4 dígitos** e ser **único** para cada empregado. Recomendamos usar a matrícula ou dígitos do CPF para facilitar a padronização.
   - **CPF:** Insira o CPF do empregado.
   - **Dia de início da folha:** Defina o primeiro dia de apuração da folha de ponto. **Exemplo**: Se o campo for preenchido com "1", a folha de ponto será calculada do dia 1 a 31.
   - **Sincronizar com o REP-P:** Ative essa opção para sincronizar com o REP-P, que registra os pontos e gera arquivos como o AFD e o comprovante de ponto. Essa configuração é essencial para que o colaborador possa registrar o ponto, seguindo as diretrizes da vigente Portaria MTP nº 671/2021.
4. Preencha os campos dentro de cada seção:

As próximas informações a serem preenchidas estão dentro de seções. Vamos passar por cada seção.
Campos que são de preenchimento obrigatório possuem um `*` .

![Imagem 2: As próximas informações a serem preenchidas estão dentro de seções. Vamos passar por cada seção. Campos que são de…](https://storage.crisp.chat/users/helpdesk/website/-/2/4/7/f/247f004c26946c00/a8b7bf55-65c5-4e3f-aac8-dd5bbd_wxgh6m.png)

**4.1. Dados de trabalho**

- **Empregador:** Selecione o empregador ao qual o colaborador está vinculado.
- **Local de trabalho:** Informe o local de trabalho do colaborador. É importante garantir que o empregador selecionado também esteja incluído no cadastro do local de trabalho, permitindo uma associação correta entre o empregador e o local de trabalho.
- **Regra de cálculo:** Defina a regra de cálculo que se aplica ao colaborador.
- **Regra de banco de horas:** Caso o colaborador utilize banco de horas, selecione a regra de banco de horas. A regra de banco de horas deve ter sido parametrizada previamente.
- **Data de Admissão:** Informe a data de contratação.
- **Líder direto desse empregado**: Caso já tenha cadastrado o líder direto desse colaborador, selecione-o nessa opção.
- **Data de início de banco de horas:** Informe a data que deverá iniciar o banco de horas do colaborador (se houver regra de banco de horas selecionada). Se o campo não estiver preenchido, o banco de horas iniciará a partir da data de admissão.

**4.2. Escala**

- **Escala:** Selecione a escala do colaborador, que deve ter sido previamente cadastrada.
- **Calendário:** Primeiro, informe a "data inicial da escala", que será o primeiro dia em que o colaborador começará a registrar o ponto. Assim que definir a data, a **escala** escolhida aparecerá logo abaixo, e embaixo dela haverá um **calendário** para visualização, começando a partir do dia inicial definido. O próximo passo é selecionar, na escala, a jornada que está acima do primeiro dia no calendário.

**Exemplo prático:**

- Vamos atribuir uma escala **5x2** para um colaborador que iniciará suas atividades no dia **01/10/2024 (terça-feira)**.
- Por padrão, o sistema seleciona automaticamente a primeira jornada da escala, o que pode gerar um erro na alocação das jornadas no calendário, isso porque o sistema assume que a escala começa em uma segunda-feira.
- Como neste caso o início é em uma terça-feira, precisamos ajustar manualmente a jornada para que as datas fiquem corretamente alinhadas.
- Portanto, devemos selecionar a 2ª jornada da escala, que corresponde à posição correta dentro do ciclo e se alinha com o dia de início do colaborador.

[GIF animado: Imagem 3: Portanto, devemos selecionar a 2ª jornada da escala, que corresponde à posição correta dentro do ciclo e se alinha com…](https://storage.crisp.chat/users/helpdesk/website/-/c/3/0/2/c30254840dd7f800/d1eec0c2-e8c4-416d-94ea-7659c9_44wpkz.gif)

> ⚠️ Atenção: Caso o colaborador não registre ponto a partir da data inicial informada, será gerada falta ou débito no banco de horas, conforme as regras aplicáveis. Então será necessário o preenchimento manual dos pontos nos dias não registrados.

**4.3. Configuração de ponto e benefícios**

Nesta seção, você encontra configurações opcionais para o registro de ponto do colaborador. Algumas opções são recomendadas para uma gestão de ponto mais eficiente; no entanto, habilite apenas aquelas que atendam às necessidades específicas da empresa:

![Imagem 4: Nesta seção, você encontra configurações opcionais para o registro de ponto do colaborador. Algumas opções são…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_ckwoaq.png)

**Medidas de segurança**

- **Gravar ponto com foto no aplicativo (dispositivos móveis)**: Exige que o colaborador tire uma foto no momento do registro de ponto pelo aplicativo no celular ou tablet. Essa foto fica vinculada ao ponto registrado, trazendo mais segurança e rastreabilidade.
- **Gravar ponto com voz no aplicativo:** Solicita uma validação por voz durante o registro de ponto no aplicativo móvel, funcionando como uma camada adicional de autenticação.
- **Gravar ponto com foto (web)**: Exige captura de foto ao registrar ponto pelas plataformas web da Pontotel, utilizando a câmera do computador.
- **Gravar ponto com voz no Pontotel Web (computador):** Solicita validação por voz durante o registro de ponto realizado no navegador do computador.
- **Cerca virtual obrigatória nos momentos:** Define em quais tipos de registro a validação de localização será obrigatória. Quando ativa, o colaborador só conseguirá registrar o ponto dentro da área permitida pela empresa. Saiba como configurar uma cerca virtual neste artigo: [Como restringir o registro de ponto por geolocalização (cerca virtual)](https://sankhya.zendesk.com/hc/pt-br/articles/42427230315031)

**Prevenção de erros**

- **Mostrar jornada no aplicativo (dispositivos móveis)**: Exibe ao colaborador sua jornada esperada e o histórico de registros diretamente no aplicativo, facilitando o acompanhamento dos horários corretos de trabalho.
- **Mostrar feedback no aplicativo:** Apresenta mensagens informativas nos aplicativos móveis, como alertas de atraso, hora extra ou inconsistências.
- **Avisar não cumprimento de interjornada:** Notifica o colaborador quando não houver o intervalo mínimo entre uma jornada e outra, ajudando a empresa a acompanhar possíveis riscos trabalhistas.

**Registro de benefícios**

- **Possui vale refeição**: Ative esta opção caso a empresa forneça o benefício. O sistema calculará a quantidade de vales-refeição devida ao colaborador para o período desejado. Acompanhe essas informações pelo relatório R18.
- **Possui vale transporte:** Habilite se a empresa paga o vale-transporte ao colaborador. Assim, o sistema calculará a quantidade a ser paga no período desejado, com dados acessíveis também no [relatório R18](https://sankhya.zendesk.com/hc/pt-br/articles/42427230315031).

**Aplicações de ponto autorizadas**

- **BatePonto Web (Computador):** Permite que o colaborador registre ponto pelo navegador em computadores e notebooks, através do site [BatePonto Web](https://bateponto.pontotel.com.br/#/).
- **BatePonto Web (Dispositivos Móveis)**: Permite o registro de ponto pelo navegador em celulares e tablets, através do site [BatePonto Web](https://bateponto.pontotel.com.br/#/).

**Personalização de uso**

- **Ativar ponto sequencial**: Obriga que os registros sigam a ordem correta da jornada, evitando, por exemplo, registrar uma saída antes da entrada. Ao ativar essa opção, o colaborador não escolherá o tipo de ponto. O próprio sistema fará a alocação com base na jornada esperada.
- **Registrar pausas pré-assinaladas:** Define que as pausas serão lançadas automaticamente pelo sistema, sem necessidade de registro manual pelo colaborador. Com essa opção ativada, o colaborador registrará somente pontos de entrada e saída. Os pontos de pausa e retorno serão criados com base na jornada esperada.
- **Omitir pontos de pausa e retorno no registro**: Oculta os registros relacionados às pausas durante o fluxo de marcação de ponto.
- **Registra ponto em qualquer local de trabalho:** Permite que o colaborador registre ponto independentemente do local de trabalho vinculado ao cadastro.
- **Ativar dupla confirmação de registro de ponto (computador):** Solicita uma confirmação adicional antes de concluir o registro de ponto pelo computador, reduzindo registros acidentais.

**Sobreaviso**

- **Ativar sobreaviso:** Habilita o controle de períodos de sobreaviso do colaborador, permitindo registrar e acompanhar jornadas em que ele permanece disponível para atendimento fora do horário habitual.

**Controle de atividades**

- **Ativar registros de atividades com aloque:** Permite que o colaborador registre atividades, projetos ou demandas vinculadas ao módulo Timesheet (gestão de atividades), possibilitando acompanhamento operacional e análise de produtividade. Para utilizar essa funcionalidade, é necessário que o módulo Timesheet esteja contratado e ativo na plataforma. Saiba mais sobre esse módulo no artigo: [Conheça o módulo Timesheet (Gestão de Atividades)](https://sankhya.zendesk.com/hc/pt-br/articles/42427254805783).

**4.4. Campos opcionais**

Aqui, você pode adicionar informações complementares sobre o colaborador. Embora não sejam obrigatórios para o funcionamento do sistema, esses campos ajudam a centralizar informações úteis, facilitando o acesso a dados mais completos sobre cada colaborador em um único lugar.

Recomendamos o preenchimento dos seguintes campos para garantir que outras áreas do sistema e relatórios contenham informações completas:

- **E-mail:** Endereço eletrônico do colaborador. Se inserido, o campo correspondente será preenchido automaticamente ao [criar o usuário do funcionário](https://sankhya.zendesk.com/hc/pt-br/articles/42427218638871).
- **RG:** Número do Registro Geral (identidade).
- **PIS:** Número do Programa de Integração Social, obrigatório para registros oficiais e cálculos trabalhistas. Alguns relatório não serão emitidos corretamente se o PIS não estiver preenchido.
- **Função:** Cargo ou posição ocupada pelo colaborador. A função aparece na folha e espelho de ponto.

**4.5. Campos customizáveis e Campos customizáveis da folha**

Essas seções permitem criar novos campos para armazenar informações específicas dos colaboradores, conforme as necessidades da empresa. Por exemplo, é possível adicionar um campo para registrar o nome social do colaborador, entre outros dados personalizados que auxiliem na gestão e no acompanhamento.

5. **Finalize o Cadastro**

Após preencher todos os campos, clique em **Criar empregado.**

---

> 💡 Dica: A Pontotel conta com o Tour Guiado, uma funcionalidade interativa disponível dentro do próprio site Pontotel Gestão, criada para auxiliar você na configuração de cadastros, parametrizações e utilização das principais ferramentas da plataforma. Com orientações passo a passo diretamente na tela, o Tour ajuda a tornar o processo mais simples, rápido e intuitivo, reduzindo dúvidas e evitando erros durante as configurações. Sempre que precisar, você poderá ativar a funcionalidade em: Admin > Tour. Para mais detalhes sobre como utilizar o recurso, confira o artigo: [Como utilizar o Tour Guiado](https://sankhya.zendesk.com/hc/pt-br/articles/42427249823127).

---

Pronto! Seu colaborador está devidamente cadastrado no sistema, e apto a registrar o ponto. Com o cadastro criado, a folha de ponto do colaborador será gerada automaticamente, ajudando você a acompanhar os registros de maneira prática e eficiente.

Caso ainda tenha dúvidas ou precise de auxílio, entre em contato com o nosso time de Suporte pelo chat integrado ao [site Gestão](https://gestao.pontotel.com.br/#/cognito/login) ou pelo [WhatsApp](https://api.whatsapp.com/send/?phone=551131852700&text&type=phone_number&app_absent=0).
