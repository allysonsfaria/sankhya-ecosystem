---
id: "42427268347671"
titulo: "Como cadastrar uma jornada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427268347671-Como-cadastrar-uma-jornada"
trilha: "PONTOTEL: Sistema de marcação de ponto > Cadastros"
atualizado_em: "2026-08-03T13:29:56Z"
rotulos: ["sync_hc", "pontotel", "sync_hash_17667e38432f", "pontotel_6a332850f1db2abcec07a68e"]
---

# Como cadastrar uma jornada

Cadastrar as jornadas de trabalho dos colaboradores de forma precisa é fundamental para garantir uma gestão eficiente, controlar as horas corretamente e manter a organização das folhas de ponto. A jornada definida serve como base para correlacionar os pontos registrados e calcular os apontamentos diários de cada colaborador.

Neste artigo, vamos mostrar como configurar uma nova jornada de trabalho na plataforma, criando uma base sólida para a organização das escalas e a gestão das folhas de ponto.

Existem dois tipos de jornadas: **com trabalho** e **sem trabalho**. As jornadas com trabalho possuem um horário de entrada e saída definidos, com uma duração estabelecida. Já as jornadas sem trabalho não têm previsão de comparecimento do colaborador, o que significa que, caso o colaborador não registre o ponto, ele não receberá falta. Abaixo, vamos explicar como cadastrar cada tipo de jornada.

---

## Como cadastrar uma jornada com trabalho

1. No menu da plataforma, clique em **Cadastros** e, em seguida, selecione **Jornadas**.
2. Confira se a categoria **com trabalho** está selecionada. Caso contrário, selecione-a.

   ![Imagem 1: Confira se a categoria com trabalho está selecionada. Caso contrário, selecione-a.](https://storage.crisp.chat/users/helpdesk/website/-/c/2/7/f/c27f0fa4cf579800/441daaf7-7842-408f-8a60-bb21fd_i0m312.png)
3. Clique na opção **Criar nova jornada** para iniciar o cadastro.

   ![Imagem 2: Clique na opção Criar nova jornada para iniciar o cadastro.](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1m2zu8r.png)
4. Preencha os campos necessários:

   - **Nome**: Defina um nome para a jornada. Se preferir, mantenha o campo sem alterações. Ao informar os horários de entrada, pausa, retorno e saída, o nome será atualizado automaticamente com base nos horários configurados.
   - **Código**: Insira um código para identificar e organizar as jornadas no sistema. Este código ajuda na consulta e gestão, facilitando o acompanhamento das jornadas no dia a dia.
   - **Entrada**: Informe o horário de início da jornada de trabalho.
   - **Pausa**: Informe o horário de início da pausa para refeição.
   - **Retorno**: Informe o horário de retorno da pausa.
   - **Saída**: Informe o horário de término da jornada de trabalho.
   - **Jornada inclui pausa(s):** Caso a jornada não deva ter pausa prevista, desabilite essa opção.

**Exemplo**: Para ilustrar, veja o exemplo de preenchimento correto dos campos para uma jornada das 08:00 às 18:00, com pausa de uma hora:

![Imagem 3: Exemplo : Para ilustrar, veja o exemplo de preenchimento correto dos campos para uma jornada das 08:00 às 18:00, com…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_wc8pw3.png)

**Configurações avançadas**
Por padrão, você pode deixar esses campos em branco, mas há opções que permitem ajustes mais específicos para o cálculo e controle das jornadas.

- **Forma de pagamento:** Escolha o método de pagamento aplicável para o dia de trabalho referente a essa jornada. Por exemplo, se o pagamento incluir as horas extras realizadas em dias úteis, selecione “hora extra”. Caso seja para dias sem jornada de trabalho prevista, como feriados ou dias de folga, escolha a opção “extraordinária”, ou selecione a opção “especial”, caso tenha configurado previamente um percentual diferente de horas extras. Se nenhuma opção for selecionada, o tempo trabalhado dentro da jornada será considerado como horas normais, e somente o excedente ao esperado será calculado como hora extra.
- **Regra de cálculo:** Caso seja orientado por um Analista da Pontotel para atender uma necessidade específica, vincule uma regra à jornada. Caso contrário, deixe o campo em branco, e o sistema utilizará automaticamente a regra de cálculo definida no cadastro do empregado.
- **Duração legal:** Caso a jornada de trabalho precise ser calculada com uma duração diferente da automática (definida pelos horários de entrada e saída), preencha este campo para ajustá-la conforme exigido pela legislação ou acordos específicos. Após atingir a duração legal definida, o sistema calculará as horas excedentes como horas extras.
- **Jornada com presença obrigatória:** Ative ou desative essa opção conforme necessário. Se ativada, a jornada exigirá que o colaborador registre o ponto; caso contrário, a falta será registrada automaticamente no dia em que não houver ponto registrado.
- **Visível para:** Define em quais locais de trabalho, grupos ou perfis de usuário essa jornada ficará disponível para seleção e vinculação. Utilize essa opção para restringir a jornada apenas aos locais necessários ou mantenha como “todos os locais” para que ela possa ser utilizada em qualquer unidade, setor ou operação cadastrada na plataforma.
- **Adicionar limite de acompanhamento de horas extras na jornada:** Ative essa opção para definir um limite de horas extras que poderá ser acompanhado durante a jornada. Ao atingir o tempo configurado, o sistema poderá utilizar esse parâmetro em funcionalidades de acompanhamento e notificações relacionadas às horas extras, ajudando gestores a monitorar excessos e agir de forma preventiva.

> ⚠️ Atenção: A funcionalidade "adicionar limite de acompanhamento de horas extras na jornada" faz parte no módulo "Controle de Custos". Caso não tenha contratado e queira conhecer essa e outras funcionalidades, entre em contato com nossa equipe pelo e-mail

5. **Salve o cadastro**

Após preencher os campos necessários, clique em **salvar**.

### Múltiplas pausas na jornada

Além da pausa para refeição, a Pontotel também permite configurar múltiplas pausas de descanso dentro da mesma jornada, atendendo empresas que precisam seguir normas regulamentadoras específicas, como a NR-17, ou políticas internas que exigem intervalos adicionais ao longo do expediente.
Com essa funcionalidade, é possível cadastrar quantas pausas forem necessárias na jornada, desde que os horários não se sobreponham. A primeira pausa cadastrada deve corresponder à pausa para refeição, enquanto as demais serão consideradas pausas de descanso.

![Imagem 4: Além da pausa para refeição, a Pontotel também permite configurar múltiplas pausas de descanso dentro da mesma jornada,…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image-5_1dg4tqv.png)
> ⚠️ Atenção: A funcionalidade de múltiplas pausas não está habilitada automaticamente em todos os ambientes. Caso sua empresa deseje utilizar esse recurso, entre em contato com o time de Suporte da Pontotel para solicitar a ativação da funcionalidade.

---

## Como cadastrar uma jornada sem trabalho

1. No menu da plataforma, clique em **Cadastros** e, em seguida, selecione **Jornadas**.
2. Mude para a categoria **"sem trabalho"**.

   ![Imagem 5: Mude para a categoria "sem trabalho" .](https://storage.crisp.chat/users/helpdesk/website/-/2/3/5/2/235292a259c8d800/d86ba35e-a324-4094-b4f4-8f8ccd_19lrtwx.png)
3. Clique na opção **Criar nova jornada** para iniciar o cadastro.
4. Preencha os campos necessários:

   - **Nome**: Atribua um nome à jornada.
   - **Código**: Insira um código para facilitar a identificação e organização das jornadas no sistema.
   - **Descrição**: Este campo é opcional. Use-o para adicionar uma breve descrição, caso necessário.
   - **Característica**: Selecione o tipo da jornada: **normal**, **compensatória** ou **DSR**. Se não houver uma necessidade específica, deixe como "normal". Esse campo serve para identificar a característica da jornada no AEJ - Arquivo Eletrônico de Jornada, e não terá impacto nos cálculos dos apontamentos do dia.
   - **Tipo de pagamento**: Defina o método de pagamento aplicável caso o colaborador registre o ponto em um dia com essa jornada.

**Configurações Avançadas**
Por padrão, você pode deixar esses campos em branco, mas há opções que permitem ajustes mais específicos para o cálculo e controle das jornadas.

- **Regra de cálculo:** Se houver uma necessidade específica que exija um cálculo diferente, vincule uma regra à jornada. Caso contrário mantenha sem preencher, assim o sistema usará a regra de cálculo definida no cadastro do empregado para realizar os cálculos.
- **Visível para:** Define em quais locais de trabalho, grupos ou perfis de usuário essa jornada ficará disponível para seleção e vinculação. Utilize essa opção para restringir a jornada apenas aos locais necessários ou mantenha como “todos os locais” para que ela possa ser utilizada em qualquer unidade, setor ou operação cadastrada na plataforma.

**Exemplo**: Para ilustrar, confira o exemplo de preenchimento correto dos campos para uma jornada sem trabalho previsto, mas com o método de pagamento definido como hora extra caso o colaborador trabalhe no dia. Essa jornada será aplicada aos sábados:

![Imagem 6: Exemplo : Para ilustrar, confira o exemplo de preenchimento correto dos campos para uma jornada sem trabalho previsto,…](https://storage.crisp.chat/users/helpdesk/website/-/a/8/c/e/a8ceadbab8e3480/cfe7f3ca-55ae-4890-b1d7-b4d5c8_14xdcq7.png)

5. Após preencher os campos necessários, clique em **Adicionar** para salvar a jornada.

---

> ⚠️ Atenção:

- Se o funcionário trabalha em horários variados, é importante cadastrar cada um desses horários, ou seja, todas as jornadas que ele cumpre.
- Os horários da jornadas não podem ser editados, exceto o nome, código e configurações extras.
- Caso a jornada já tenha sido atribuída a uma folha de ponto, ela não poderá ser excluída.
- Sua plataforma já inclui uma jornada padrão chamada “folga”, com o tipo de pagamento extraordinário.

---

> 💡 Dica: A Pontotel conta com o Tour Guiado, uma funcionalidade interativa disponível dentro do próprio site Pontotel Gestão, criada para auxiliar você na configuração de cadastros, parametrizações e utilização das principais ferramentas da plataforma. Com orientações passo a passo diretamente na tela, o Tour ajuda a tornar o processo mais simples, rápido e intuitivo, reduzindo dúvidas e evitando erros durante as configurações. Sempre que precisar, você poderá ativar a funcionalidade em: Admin > Tour. Para mais detalhes sobre como utilizar o recurso, confira o artigo: [Como utilizar o Tour Guiado](https://sankhya.zendesk.com/hc/pt-br/articles/42427249823127).

---

Pronto! Sua nova jornada foi cadastrada com sucesso. Com essas configurações, você terá um controle mais preciso sobre os horários de entrada, pausa e saída dos colaboradores, o que facilita a gestão das jornadas e melhora a organização das folhas de ponto. Agora, você está pronto para garantir o registro correto das horas trabalhadas, mantendo sua operação ainda mais eficiente e bem organizada!

Caso ainda tenha dúvidas ou precise de auxílio, entre em contato com o nosso time de Suporte pelo chat integrado ao [site Gestão](https://gestao.pontotel.com.br/#/cognito/login) ou pelo [WhatsApp](https://api.whatsapp.com/send/?phone=551131852700&text&type=phone_number&app_absent=0).
