---
id: "42427230158231"
titulo: "Como configurar e utilizar pausas pré-assinaladas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427230158231-Como-configurar-e-utilizar-pausas-pr%C3%A9-assinaladas"
trilha: "PONTOTEL: Sistema de marcação de ponto > Administração"
atualizado_em: "2026-08-03T12:50:56Z"
rotulos: ["sync_hc", "pontotel_6a33284f206228b3ab9d77e1", "sync_hash_4906fe0815c5", "pontotel"]
---

# Como configurar e utilizar pausas pré-assinaladas

As pausas pré-assinaladas permitem que a Pontotel insira automaticamente os horários de pausa e retorno de pausa na folha de ponto dos colaboradores, sem a necessidade de registros manuais durante a jornada.
Essa funcionalidade é especialmente útil para empresas em que os colaboradores registram apenas a entrada e a saída do expediente, garantindo que os intervalos obrigatórios sejam considerados corretamente nos cálculos da jornada.

Atualmente, a plataforma oferece três formas de realizar o preenchimento automático das pausas:

- Pela jornada prevista.
- Pela jornada executada.
- Pela jornada adaptativa.
  Cada uma possui um comportamento diferente para definir a duração e o posicionamento da pausa ao longo da jornada.

---

## Como funcionam as pausas pré-assinaladas

Quando a funcionalidade está habilitada, o sistema analisa os registros realizados pelo colaborador e, caso não existam marcações de início e retorno de pausa, realiza automaticamente a inclusão desses apontamentos na folha de ponto.

> ⚠️ Atenção: O preenchimento automático acontece somente quando o colaborador registra entrada e saída sem registrar nenhuma pausa manualmente. Caso exista qualquer registro de início ou retorno de pausa, o sistema respeitará os horários informados pelo colaborador e não realizará inserções automáticas.

---

## Pré-requisitos para utilizar pausas pré-assinaladas

Antes de configurar a regra de cálculo, é necessário habilitar a funcionalidade no cadastro do colaborador.

1. Acesse **Cadastros > Empregados**.
2. Selecione o colaborador desejado.
3. Clique em **editar**.
4. Acesse a seção **Config. de ponto e benefícios**.
5. Habilite a opção "**registrar pausas pré-assinaladas**".

![Imagem 1: Habilite a opção " registrar pausas pré-assinaladas ".](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1v65uln.png)

Sem essa configuração, o sistema não realizará a inserção automática das pausas, mesmo que a regra de cálculo esteja configurada.

---

## Como configurar pausas pré-assinaladas

A configuração é realizada na regra de cálculo utilizada pela empresa.

1. Acesse **Regras > Cálculo**.
2. Edite a regra desejada.
3. Localize a seção **Pausas intrajornadas (refeição)**.
4. Configure os limites de horas trabalhadas e os intervalos desejados.
5. Escolha o comportamento de preenchimento automático das pausas.

![Imagem 2: Escolha o comportamento de preenchimento automático das pausas.](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_jytb8f.png)

---

## Tipos de pausas pré-assinaladas

A Pontotel disponibiliza três comportamentos diferentes para o preenchimento automático das pausas.

### Pausa pela jornada prevista

Nesse modo, o sistema utiliza exatamente os horários configurados na jornada esperada do colaborador.
Tanto a duração quanto o horário da pausa seguem o planejamento da jornada.

**Exemplo**:
Jornada cadastrada:

- Entrada: 08h00
- Pausa: 12h00 às 13h00
- Saída: 17h00
  Registro realizado:
- Entrada: 08h00
- Saída: 17h00
  Resultado:
- Início da pausa: 12h00
- Retorno da pausa: 13h00

Esse é o comportamento mais tradicional e indicado para empresas com jornadas fixas e previsíveis.

### Pausa pela jornada executada

Nesse modo, o sistema calcula a duração da pausa com base na quantidade de horas efetivamente trabalhadas pelo colaborador.
O horário da pausa é definido utilizando o ponto médio entre a entrada e a saída registradas.

**Exemplo**:
Registro realizado:

- Entrada: 08h00
- Saída: 14h00
  Como o colaborador trabalhou 6 horas, o sistema identifica a faixa correspondente e aplica a duração configurada para esse cenário.
  Em seguida, calcula o ponto médio da jornada para posicionar a pausa.
  Esse comportamento é indicado para empresas que possuem jornadas variáveis e desejam que a pausa acompanhe a realidade trabalhada pelo colaborador.

### Pausa pela jornada adaptativa

A pausa pela jornada adaptativa combina os benefícios dos dois modelos anteriores.
Primeiro, o sistema identifica quanto tempo de pausa deve ser aplicado com base nas horas efetivamente trabalhadas.
Depois, avalia se existe uma jornada prevista para aquele dia.
Se existir uma jornada planejada e o horário da pausa estiver compatível com os registros realizados, o sistema utiliza o horário configurado na jornada.
Caso contrário, posiciona a pausa automaticamente utilizando o ponto médio da jornada trabalhada.

**Exemplo 1 - Jornada prevista compatível**:
Jornada prevista:

- Entrada: 08h00
- Pausa: 12h00 às 13h00
- Saída: 17h00
  Registro realizado:
- Entrada: 08h00
- Saída: 17h00
  Resultado:
- Pausa inserida das 12h00 às 13h00.
  Justificativa: o horário previsto se encaixa perfeitamente dentro da jornada realizada.

**Exemplo 2 - Jornada diferente da prevista**:
Jornada prevista:

- Entrada: 08h00
- Pausa: 12h00 às 13h00
- Saída: 17h00
  Registro realizado:
- Entrada: 07h00
- Saída: 11h30
  Resultado:
  O sistema recalcula a pausa utilizando o ponto médio da jornada executada.

Exemplo 3 - Trabalho em folga
Registro realizado:

- Entrada: 08h00
- Saída: 16h00
  Como não existe jornada prevista para o dia, o sistema utiliza as configurações da regra de cálculo e posiciona a pausa no ponto médio da jornada trabalhada.

### Como a jornada adaptativa define a duração da pausa

A duração da pausa é determinada pelas faixas configuradas na regra de cálculo.

Exemplo:

| Horas trabalhadas | Resultado |
| --- | --- |
| Até 4 horas | Sem pausa |
| Entre 4 e 6 horas | 15 minutos |
| Acima de 6 horas | 60 minutos |

Assim, um colaborador que trabalhou 5 horas receberá automaticamente uma pausa de 15 minutos.
Já um colaborador que trabalhou mais de 6 horas receberá uma pausa de 60 minutos, respeitando as configurações da empresa.

### Como o sistema define o horário da pausa

Quando a jornada adaptativa precisa posicionar a pausa pela jornada executada, o sistema utiliza o ponto médio entre a entrada e a saída.
Após encontrar esse horário intermediário, o valor é arredondado para a hora cheia mais próxima.

Exemplos:

- Ponto médio às 11h20 → pausa posicionada às 11h00.
- Ponto médio às 11h45 → pausa posicionada às 12h00.
  Esse comportamento garante uma distribuição mais equilibrada da pausa ao longo da jornada.

### Comparativo entre os modos de pausa pré-assinalada

| Modo | Duração da pausa | Horário da pausa |
| --- | --- | --- |
| Jornada prevista | Definida pela jornada | Definido pela jornada |
| Jornada executada | Definida pelas horas trabalhadas | Ponto médio da jornada |
| Jornada adaptativa | Definida pelas horas trabalhadas | Jornada prevista quando possível; caso contrário, ponto médio da jornada |

---

## Perguntas frequentes

### O sistema insere a pausa mesmo sem registro de pausa?

Sim. Essa é justamente a finalidade das pausas pré-assinaladas.
Desde que o colaborador tenha registrado entrada e saída e possua a opção de registro automático habilitada, o sistema realizará a inclusão dos apontamentos automaticamente.

### O que acontece se o colaborador registrar a pausa manualmente?

Nesse caso, nenhuma pausa automática será inserida.
O sistema sempre prioriza os registros realizados pelo próprio colaborador.

### A funcionalidade interfere no cálculo de horas extras?

Sim. As pausas inseridas automaticamente passam a fazer parte da folha de ponto e são consideradas normalmente durante os cálculos da jornada, banco de horas, horas extras e demais apontamentos.

### Quem pode configurar essa funcionalidade?

Usuários com permissão para editar regras de cálculo e cadastros de empregados, normalmente administradores, RH e gestores responsáveis pela parametrização da plataforma.

---

As pausas pré-assinaladas ajudam a automatizar o controle dos intervalos, reduzindo ajustes manuais na folha de ponto e garantindo maior aderência às regras de jornada da sua empresa. Ao escolher o modelo mais adequado entre jornada prevista, jornada executada ou jornada adaptativa, é possível tornar o tratamento das pausas mais preciso e compatível com a realidade dos colaboradores.

Caso ainda tenha dúvidas ou precise de auxílio, entre em contato com o nosso time de Suporte pelo chat integrado ao[site Gestão](https://gestao.pontotel.com.br/#/cognito/login) ou pelo[WhatsApp](https://api.whatsapp.com/send/?phone=551131852700&text&type=phone_number&app_absent=0).
