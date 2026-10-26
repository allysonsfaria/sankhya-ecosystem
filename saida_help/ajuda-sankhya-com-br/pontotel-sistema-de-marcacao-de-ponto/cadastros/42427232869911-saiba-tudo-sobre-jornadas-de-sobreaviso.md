---
id: "42427232869911"
titulo: "Saiba tudo sobre jornadas de sobreaviso (plantão)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427232869911-Saiba-tudo-sobre-jornadas-de-sobreaviso-plant%C3%A3o"
trilha: "PONTOTEL: Sistema de marcação de ponto > Cadastros"
atualizado_em: "2026-08-03T13:30:00Z"
rotulos: ["sync_hc", "pontotel_6a33284f666f637a24282c1c", "sync_hash_a6ea50761728", "pontotel"]
---

# Saiba tudo sobre jornadas de sobreaviso (plantão)

Precisa organizar os períodos de plantão da sua equipe? O **sobreaviso** é o tempo em que o colaborador fica à disposição da empresa, pronto para ser acionado, mesmo sem estar efetivamente trabalhando.
Lançar esses períodos na plataforma Pontotel é fundamental para uma gestão transparente. Isso informa ao sistema que o colaborador está disponível e, caso ele seja acionado e registre o ponto, a plataforma aplicará as regras de cálculo corretas para esse período.
O processo é dividido em duas partes: a **ativação da funcionalidade** (feita apenas uma vez) e o **lançamento da jornada** (feito no dia a dia).
Vamos lá?

---

## Como ativar o Sobreaviso

1. **Habilitar a funcionalidade com time da Pontotel**

   - Antes de começar, verifique se as funcionalidades listadas abaixo estão disponíveis para configuração. Caso não estejam, isso indica que a funcionalidade ainda não foi ativada em seu ambiente.
   - Para solicitar a ativação, entre em contato com nossa equipe por meio da Central de Atendimento, chat integrado ao site Gestão ou WhatsApp.

> ⚠️ Atenção: o sobreaviso faz parte do módulo **Cálculos e Tratamento**. Caso sua empresa ainda não tenha contratado esse módulo, preencha o [Formulário de Solicitação](https://forms.ploomes.com/form/70de62ee610b42bd82e4c0f9b6d2e195) para que nosso time responsável entre em contato em breve com a cotação e a melhor solução para a sua necessidade.

2. **Habilitar no Local de Trabalho**

   - No menu de navegação do [site Gestão](https://gestao.pontotel.com.br/), abra o menu **Cadastros** e selecione a opção **Locais de trabalho**.
   - Edite o local de trabalho que terá a funcionalidade (ou crie um novo).
   - Em **Configurações avançadas**, marque a opção "**Ativar sobreaviso para esse local de trabalho"**.
   - Clique em **Salvar**.

   ![Imagem 1: Clique em Salvar .](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_124dt6v.png)
3. **Habilitar no Cadastro do Empregado**

   - No menu de navegação do [site Gestão](https://gestao.pontotel.com.br/), abra o menu **Cadastros** e selecione a opção **Empregados**.
   - Edite o cadastro do colaborador que fará plantões.
   - Vá para a aba **Config. de ponto e benefícios**.
   - Marque a opção **ativar sobreaviso**.
   - Clique em **Salvar**.

   ![Imagem 2: Clique em Salvar .](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_wxue29.png)

---

## Como inserir uma jornada de sobreaviso na folha de ponto

Com a funcionalidade ativa, você já pode lançar os períodos de plantão para os colaboradores habilitados.

1. No menu de navegação do [site Gestão](https://gestao.pontotel.com.br/), abra o menu **Folha** e selecione a opção **Folha de pontos**.
2. Localize o colaborador desejado e abra a folha de ponto correspondente que receberá o sobreaviso
3. Clique com o **botão direito** no dia desejado.
4. No menu que aparece, selecione a opção **jornada sobreaviso**.

   ![Imagem 3: No menu que aparece, selecione a opção jornada sobreaviso .](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1f21aim.png)
5. Uma janela de **Lançamento de sobreaviso** será aberta. Preencha os campos:

   - **Data:** O dia do plantão.
   - **Dias de sobreaviso:** a quantidade de dias que receberão a jornada de sobreaviso, caso seja múltiplos dias
   - **Sobreaviso de 24h:** Utilizado quando não há jornaa de trabalho prevista para o dia, e o colaborador deve realizar um plantão de 24 horas.
   - **Usar duração:** adicione o horário de início e término do sobreaviso.
   - **Início:** O horário que o sobreaviso começa, sendo no formato HH:MM.
   - **Fim:** O horário que o sobreaviso termina, sendo no formato HH:MM.
   - Clique em **Adicionar**.

   ![Imagem 4: Clique em Adicionar .](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1s0guo5.png)

> 💡 Dicas:

- Os horários de **sobreaviso** não podem coincidir com a **jornada esperada de trabalho** do colaborador.
- É possível cadastrar **mais de um período de sobreaviso no mesmo dia**. Para isso, clique em **“+ mais sobreaviso”** e preencha os campos de **início** e **término** de cada período.
- Se o sobreaviso **começar em um dia e terminar no seguinte**, selecione a opção **“+1d”**, localizada ao lado do campo **“fim”**, para garantir o registro correto.

6. A jornada de sobreaviso aparecerá na folha como uma **jornada amarela**, logo abaixo da jornada de trabalho esperada (verde).

![Exemplo de dia com jornada de sobreaviso](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_m4hmy.png)

Exemplo de dia com jornada de sobreaviso

---

## Entendendo os apontamentos na folha

Depois de lançar a jornada de sobreaviso (amarela), o sistema calculará os apontamentos com base no registro de ponto do colaborador.
Existem dois cenários principais:

### Cenário 1: Colaborador não foi acionado (sem registro de ponto)

Se o colaborador esteve de plantão mas não precisou trabalhar (ou seja, não registrou ponto durante o período de sobreaviso), o sistema exibirá o apontamento:

- **Duração de Sobreaviso:** Mostra o tempo total que o colaborador esteve à disposição, mas que não foi efetivamente trabalhado.

### Cenário 2: Colaborador foi acionado (com registro de ponto)

Se o colaborador foi chamado e registrou a entrada e a saída durante o período de sobreaviso, o sistema exibirá o apontamento:

- **H. Extra Sobreaviso (Horas Extras de Sobreaviso):** Mostra o tempo que o colaborador efetivamente trabalhou dentro do período de plantão.

![Exemplo de jornada onde os dois apontamentos são gerados, conforme o período trabalhado](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_13gm6va.png)

Exemplo de jornada onde os dois apontamentos são gerados, conforme o período trabalhado

> 💡 Dicas:

- Por padrão, o apontamento H. Extra Sobreaviso é automaticamente direcionado para o **Banco de Horas**do colaborador, caso ele possua bando de horas ativo.
- Caso os **apontamentos mencionados acima não estejam sendo exibidos**, é necessário **habilitar a visualização** deles na **regra de cálculo** aplicada ao dia em questão. Para isso, acesse o menu **Admin > Regras de cálculo**, edite a regra correspondente e, na aba **“Apontamentos”**, localize os apontamentos desejados e **ative-os**.

---

## Sobreaviso em Horário Noturno

Para que o sistema calcule corretamente os plantões que ocorrem na madrugada (ex: das 22h às 05h), o lançamento da jornada de sobreaviso deve ser feito no **dia em que o trabalho é realizado**.

**Exemplo Prático:** Um colaborador iniciará um sobreaviso à **02:00 da manhã do dia 29**.

- **Lançamento Incorreto:** Se a jornada de sobreaviso for lançada no dia 28 (dia anterior), o sistema não calculará as horas da madrugada corretamente.
- **Lançamento Correto:** A jornada de sobreaviso deve ser lançada no **dia 29**, pois é a data de referência do início do trabalho.

![Imagem 7: Lançamento Correto: A jornada de sobreaviso deve ser lançada no dia 29 , pois é a data de referência do início do…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_ok4e09.png)

---

## Como excluir um sobreaviso

Caso tenha lançado uma jornada de sobreaviso erroneamente:

- Clique sobre ela no dia correspondente (jornada amarela).
- No menu do sobreaviso, clique no botão **"excluir"**.

![Imagem 8: No menu do sobreaviso, clique no botão "excluir" .](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1word1q.png)

---

## ✨ Novidade: Limites mensais de sobreaviso

Além das configurações tradicionais de sobreaviso, a Pontotel também permite controlar a quantidade máxima de horas de sobreaviso que podem ser acumuladas no banco de horas dentro de um mesmo mês.
Essa funcionalidade é ideal para empresas que possuem acordos coletivos ou políticas internas que limitam o acúmulo de horas de sobreaviso, exigindo que os excedentes sejam pagos diretamente em folha.
Quando o limite configurado é atingido, o sistema continua calculando normalmente as horas de sobreaviso. No entanto, as horas que ultrapassarem o teto definido deixam de ser enviadas para o banco de horas e passam a ser direcionadas automaticamente para a folha de pagamento.

> ⚠️ Importante: Esse controle atua exclusivamente sobre horas de sobreaviso e funciona de forma independente dos limites gerais configurados para o banco de horas.

### Tipos de horas contemplados

Atualmente, o limite mensal pode ser aplicado aos seguintes tipos de horas de sobreaviso:

- Horas extras de sobreaviso
- Horas extraordinárias de sobreaviso
- Horas especiais de sobreaviso
- Horas extras noturnas de sobreaviso
- Horas extraordinárias noturnas de sobreaviso
- Horas especiais noturnas de sobreaviso

### Como configurar

1. Acesse a regra de banco de horas utilizada pela empresa, em **Regras > Banco de horas**.
2. Edite a regra desejada.
3. Localize a seção **Limites**.
4. Habilite a opção **Definir limites mensais de sobreaviso**.
5. Após a ativação, será possível escolher uma das modalidades de controle disponíveis.

![Imagem 9: Após a ativação, será possível escolher uma das modalidades de controle disponíveis.](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1srdqml.png)

### Limite por tipo de hora

Nesse modelo, cada tipo de hora possui um limite mensal individual.
Por exemplo, é possível permitir o acúmulo de até 10 horas extras de sobreaviso e até 5 horas extraordinárias de sobreaviso no mesmo mês, cada uma com seu próprio controle.
Quando o limite de um tipo específico for atingido, apenas o excedente daquele tipo de hora será direcionado para folha de pagamento.

### Limite por grupo compartilhado

Nesse modelo, vários tipos de horas compartilham um único limite mensal.
Todos os tipos incluídos no grupo consomem o mesmo saldo disponível.

Por exemplo, se um grupo possuir limite de 20 horas mensais, todas as horas de sobreaviso configuradas nesse grupo utilizarão esse mesmo saldo. Quando o limite for atingido, os apontamentos excedentes deixarão de ser acumulados no banco de horas e serão enviados para folha de pagamento.

> ⚠️ Atenção: Um mesmo tipo de hora não pode ser utilizado simultaneamente em mais de um grupo compartilhado.

### Como o limite é aplicado

O sistema realiza a validação diariamente durante o processamento do banco de horas.
Nesse momento, a plataforma:

- Verifica quanto já foi acumulado no mês.
- Soma as horas do dia em processamento.
- Compara o resultado com o limite configurado.
- Envia para o banco apenas o saldo ainda disponível.
- Direciona automaticamente o excedente para folha de pagamento.

### Perguntas frequentes

**O limite é reiniciado mensalmente?**
Sim. O controle considera apenas os apontamentos do mês corrente. Ao iniciar um novo mês, o saldo utilizado é reiniciado automaticamente.

**O que acontece com as horas que ultrapassarem o limite?**
As horas excedentes continuam sendo calculadas normalmente, porém deixam de compor o banco de horas e passam a ser destinadas para folha de pagamento.

**Posso utilizar limite por tipo de hora e por grupo compartilhado ao mesmo tempo?**
Não. É necessário escolher apenas um dos modelos de configuração.

**Tipos de horas sem limite configurado são afetados?**
Não. Apenas os tipos de horas incluídos na configuração participam do controle de limite mensal.

---

## ✨ Novidade: Sobreaviso sobreposto à jornada

Até agora, um período de sobreaviso só podia ser lançado na folha fora do horário da jornada esperada do colaborador. Isso mudou.
Passa a ser possível registrar períodos de sobreaviso que coincidem com a jornada de trabalho do colaborador. Para isso, a regra de cálculo aplicada ao dia precisa ser do tipo Flexível.
Na prática: se o colaborador está de sobreaviso no mesmo intervalo em que cumpre a jornada, e o dia usa uma regra de cálculo Flexível, o lançamento é aceito sem bloqueio.
Essa funcionalidade precisa ser habilitada pelo nosso time. Fale com o suporte para ativar na sua conta.

> ⚠️ Atenção: a sobreposição funciona apenas quando a regra de cálculo vigente para o dia é do tipo Flexível. Em dias com outras regras de cálculo, o sobreaviso continua sendo lançado fora do horário da jornada esperada.

---

> 💡 Dica: agora também é possível solicitar sobreaviso diretamente pela folha, com fluxo de aprovação. Veja o passo a passo no artigo [Como fazer a gestão de solicitações](https://sankhya.zendesk.com/hc/pt-br/articles/42427228755863).

---

Com o sobreaviso configurado e lançado corretamente, sua plataforma fará a gestão automática dos plantões, garantindo o cálculo exato das horas de disponibilidade e das horas trabalhadas durante os acionamentos.

Caso ainda tenha dúvidas ou precise de auxílio, entre em contato com o nosso time de Suporte pelo chat integrado ao [site Gestão](https://gestao.pontotel.com.br/#/cognito/login) ou pelo [WhatsApp](https://api.whatsapp.com/send/?phone=551131852700&text&type=phone_number&app_absent=0).
