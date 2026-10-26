---
id: "42427228755863"
titulo: "Como fazer a Gestão de Solicitações"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427228755863-Como-fazer-a-Gest%C3%A3o-de-Solicita%C3%A7%C3%B5es"
trilha: "PONTOTEL: Sistema de marcação de ponto > Gestão"
atualizado_em: "2026-08-03T12:50:38Z"
rotulos: ["sync_hc", "pontotel_6a3328e97990d448393c9d91", "sync_hash_3e52ec6b57ff", "pontotel"]
---

# Como fazer a Gestão de Solicitações

A funcionalidade de **solicitações** é uma ferramenta indispensável para garantir um controle eficiente e transparente sobre os eventos que impactam as folhas de ponto dos colaboradores. Ele permite que determinadas ações sejam revisadas e aprovadas antes de sua aplicação definitiva, assegurando maior conformidade e precisão nos registros.

Entre os eventos que podem gerar solicitações estão:

- Correções de ponto;
- Dispensas;
- Suspensões;
- Conversões de horas em banco de horas;
- Alterações de escala;
- Férias;
- Horas extras;
- Bloqueios de solicitações

Com um design moderno e filtros otimizados, a ferramenta centraliza todo o gerenciamento de solicitações, proporcionando mais governança e agilidade tanto para gestores quanto para equipes de RH. Confira abaixo como configurar e aproveitar essa funcionalidade.

---

## Benefícios da funcionalidade de Solicitações

- **Controle centralizado:** Todas as solicitações são gerenciadas em um único lugar, facilitando o acompanhamento e a auditoria.
- **Transparência:** Permite que as regras sejam configuradas para que determinados perfis aprovem ou reprovem solicitações.
- **Flexibilidade:** As regras podem ser personalizadas para locais, empregados, perfis de usuário ou toda a empresa.
- **Segurança:** Bloqueios podem ser configurados para impedir alterações em eventos antigos ou fora de prazo.

---

## Como habilitar a funcionalidade

- Certifique-se de que a opção "**Solicitações**" aparece no menu de navegação do [\_\_site Gestão](https://gestao.pontotel.com.br/).\_\_

![Imagem 1: Certifique-se de que a opção " Solicitações " aparece no menu de navegação do __site Gestão .__](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1dqmoat.png)

- Se a opção exibida no print acima não estiver disponível, entre em contato com nossa equipe para verificar se a funcionalidade está incluída no plano contratado. Caso esteja, solicite sua ativação.

---

## Como configurar os perfis de usuário

Primeiramente, acesse as permissões em "**Regras > Perfil de permissão**", e habilite as opções correspondentes aos perfis que terão acesso à funcionalidade desejada. Para cada tipo de evento (como dispensa ou correção de ponto), ajuste as permissões de acordo com as necessidades específicas de cada perfil.

- **Exemplo:** Para que um determinado perfil possa visualizar a opção de dispensa na folha, habilite a permissão "ver". Caso deseje que o perfil possa lançar ou editar dispensas, habilite a opção "criar/editar". Por fim, para permitir que o perfil possa remover dispensas já lançadas, habilite a permissão "excluir".

Com as três opções selecionadas, a opção para lançamento de dispensa ficaria dessa forma:

![Imagem 2: Com as três opções selecionadas, a opção para lançamento de dispensa ficaria dessa forma:](https://storage.crisp.chat/users/helpdesk/website/-/e/b/1/c/eb1ce4d68abd4800/11932ca1-c940-4b95-b6b4-dbe921_k4xxn7.png)

---

## Crie a regra de solicitação

1. No menu de navegação do [site Gestão](https://gestao.pontotel.com.br/), abra o menu **Regras** e selecione a opção **Solicitações**.
2. Clique em **Criar nova regra.**
3. Defina os **parâmetros** da regra

![Imagem 3: Defina os parâmetros da regra](https://storage.crisp.chat/users/helpdesk/website/-/d/5/a/b/d5ab8a362acc6000/fe062784-2826-40bf-887d-ed9315_hscx45.png)

- **Nome da regra**: Defina um nome que identifique a regra de aprovação.
- **Tipo de evento:** Escolha o tipo de evento que será gerenciado por esta regra de aprovação. Entre os tipos de eventos disponíveis estão:
  - **Correção de ponto**: Lançamentos e/ou exclusões de pontos manuais ou reais.
  - **Dispensa**: Inclusão de atestados médicos ou justificativas de ausência.
  - **Suspensão**: Lançamento ou remoção de suspensões.
  - **Transferência de apontamentos em BH**: Conversão de horas para banco de horas.
  - **Alteração de escala**: Modificações na escala de trabalho do colaborador.
  - **Horas extras**: Solicitação e justificativa de horas extras.
  - **Férias**: Solicitação e agendamento de férias.
  - **Bloqueio de solicitações**: Utilizado para bloquear perfis, usuários, empregados, locais ou grupos de efetuar solicitações.
  - **Sobreaviso**: Utilizado para lançar jornadas de sobreaviso

> 💡 Dica: Para os eventos "dispensa" e "suspensão", é possível definir que a regra seja aplicada somente para determinados motivos.

- **Quando for lançado:** Selecione o critério que determinará quando a regra será aplicada. As opções disponíveis são:

  - Para alguns locais: Aplicada a eventos lançados por colaboradores de locais de trabalho específicos.
  - Para alguns empregados: Restringida a eventos lançados para determinados colaboradores.
  - Para os grupos: Aplicada a eventos lançados em locais associados a grupos específicos.
  - Pelos perfis de usuário: A regra será ativada quando usuários de perfis específicos realizarem lançamentos.
  - Para todo local/empregado: Abrange todos os eventos lançados na empresa.
- **Limite de dias para lançamento de solicitações após a data do evento:** Defina o período máximo para o lançamento de solicitações a partir da data do evento. Por exemplo:

  - Se configurado como "5" dias, solicitações só poderão ser lançadas até 5 dias após o evento.
  - Caso configurado como "sem limite", não haverá restrição de prazo para o lançamento.
- **Aprovar automaticamente as solicitações geradas pela regra:** Quando ativada, todas as solicitações geradas com base nesta regra serão aprovadas automaticamente, sem a necessidade de intervenção manual. Essa configuração agiliza processos para eventos com menor complexidade.
- **Pré-registrar eventos e cálculos resultantes no sistema enquanto a solicitação estiver pendente**: Ao ativar esta opção, os eventos lançados aparecerão na folha de ponto como pré-registrados, mesmo que ainda estejam pendentes de aprovação. Caso sejam aprovados, o registro será mantido. Se reprovados, o registro será removido e os apontamentos serão recalculados.
- **Bloquear respostas a pedidos em [X] Dias a partir da data em que o pedido foi gerado:** Define o prazo máximo para que uma solicitação seja respondida (aprovada ou reprovada). Após esse período, as solicitações pendentes são bloqueadas e não podem mais ser respondidas.
- **Permitir que usuários sem perfil de RH respondam às solicitações geradas por essa regra**: Quando ativada, permite que, além de usuários com permissão de RH, usuários com outras permissões como supervisores ou gerentes aprovem ou reprovem solicitações.
  - Ao habilitar essa opção, também poderá ser definido o limite de solicitações que o perfil selecionado poderá responder por mês.

> ⚠️ Atenção: Alguns tipos de evento podem ter opções diferentes para serem preenchidas, como regra de eventos para "horas extras" ou "alteração de escala". Atente-se no preenchimento dos campos e, caso tenha alguma dúvida, entre em contato conosco para que possamos auxiliar no preenchimento.

**Parâmetros específicos do motivo "Horas Extras":**

![Imagem 4: Parâmetros específicos do motivo "Horas Extras":](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_19ax4fb.png)

- **Modos de justificativa:** Define o momento em que a solicitação deve ser criada.**Pedidos feitos antes de realizá-las e justificativa feita após realizá-las:** O colaborador pode pedir autorização prévia ou realizar a justificativa após ter feito as horas extras sem solicitação prévia.**Justificativa feita após realizá-las:** O colaborador registra a justificativa da hora extra depois que ela aconteceu. Funciona como uma regularização do ponto.
- **Limitar solicitar horas extras em [X] horas por dia:** Define um teto máximo diário. Por exemplo, se configurado para "02:00", o sistema não permitirá que o colaborador solicite mais de 2 horas extras num único dia, ajudando a controlar a fadiga e o passivo trabalhista.
- **Dispensar justificativa quando as horas extras forem inferiores a:** Traz agilidade para o dia a dia. Você pode definir uma tolerância (ex: 10 minutos). Se a hora extra for menor que esse tempo, o sistema não exigirá a abertura de uma solicitação formal, reduzindo o volume de tarefas manuais para micro-ocorrências.
- **Bloquear justificativas em [X] dias [corridos/úteis]:** Estabelece um prazo limite (deadline) para o colaborador justificar a hora extra realizada. Após esse período (contado a partir da data da ocorrência), o sistema bloqueia novas solicitações. Isso é essencial para garantir que a folha de ponto seja fechado dentro do prazo correto.
- **Formato da Solicitação:Solicitar por intervalo:** O colaborador precisa informar o horário exato de início e fim da hora extra (ex: das 18:00 às 19:30). Oferece maior precisão e rastreabilidade.**Solicitar por duração:** O colaborador informa apenas a quantidade de tempo (ex: "01:30" de hora extra), sem precisar especificar em qual horário exato ela ocorreu. É mais flexível, mas menos detalhado.

4. Para finalizar a configuração da regra, clique em **salvar.**

---

## Como acompanhar e gerenciar as solicitações

1. Agora é o momento de analisar e aprovar ou reprovar as solicitações geradas. Para acessar a funcionalidade, no menu de navegação do [site Gestão](https://gestao.pontotel.com.br/), clique em **Solicitações**.
2. Preencha os **filtros** de busca:

![Imagem 5: Preencha os filtros de busca:](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_7e0lba.png)

- **Tipo de evento**: Escolha o tipo de evento a ser exibido, como correção de ponto ou dispensa. A opção "todos" mostra todos os eventos.
- **Status**: Filtra por status das solicitações, como pendentes, aprovadas, reprovadas, com erros, canceladas ou todas.
- **Período (Início e Término)**: Restringe as solicitações ao intervalo de datas especificado.
- **Filtrar por**: Define o critério de busca, como locais de trabalho, empregados, grupos ou perfis.

  - A depender do filtro escolhido, no campo seguinte selecione os locais de trabalho, empregados, grupos ou perfis que deseja verificar.
- Finalize clicando em **Buscar.**

3. Faça o **gerenciamento** das solicitações:

[GIF animado: Imagem 6: Faça o gerenciamento das solicitações:](https://storage.crisp.chat/users/helpdesk/website/-/5/0/a/b/50abceff7d3edc00/af5f47b4-bcbc-4d42-ab05-f3d3fc_1oe5msj.gif)

**Lista de solicitações**

- A tela apresenta uma lista com as solicitações, divididas em colunas com as seguintes informações:
- Data: Exibe o dia correspondente à solicitação registrada.
- Empregado: Nome do colaborador que gerou ou está vinculado à solicitação.
- Tipo: Tipo de evento solicitado, como correção de ponto, dispensa ou alteração de escala.
- Solicitação: Descrição do evento solicitado, como "adicionar ponto de entrada às 08:15".
- Motivo: Razão apresentada pelo colaborador ou gestor, por exemplo, "Esqueceu de bater ponto".

**Ações individuais**

- Cada solicitação pode ser selecionada para análise detalhada, com diversas outras informações, como quem fez a solicitação, ou qual a regra de aprovação utilizada no caso. Dentro do detalhamento, é permitido que o gestor ou RH aprove ou reprove a solicitação individualmente.
- Caso a solicitação seja aprovada, é permitido colocar um motivo para a aprovação.
- Caso a solicitação seja reprovada, é obrigatório colocar um motivo para a reprovação.

**Ações em massa**

- Acima da lista de solicitações, os botões permitem realizar ações de forma coletiva para todas as solicitações pendentes exibidas na lista (na qual mostra até 10 solicitações por vez):
- Reprovar os pendentes: reprova todas as solicitações exibidas na tela atual.
- Aprovar os pendentes: aprova todas as solicitações exibidas na tela atual.
- Além das ações em massa, é possível gerar um arquivo com o resultado da análise, contendo informações das solicitações filtradas.

4. Verifique o **status** da solicitação

Após realizar a aprovação ou reprovação das solicitação, é possível verificar o status na tela de Gestão ou diretamente na folha de ponto do colaborador.

Para visualizar na folha de ponto:

- Acesse a folha de ponto do colaborador relacionado à solicitação.
- Localize o dia referente à solicitação analisada.
- Verifique o ícone exibido na linha do evento:

Solicitação **aprovada**: O ícone abaixo indica que o evento foi aceito e aplicado à folha.

![Imagem 7: Solicitação aprovada : O ícone abaixo indica que o evento foi aceito e aplicado à folha.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/574ca4e4c6979138ff609a77/images/6765d06e7f1157651916ea35/file-qOd7KTmBv1.png)

Solicitação **reprovada**: O ícone abaixo será exibido, e o evento não será considerado no cálculo da folha.

![Imagem 8: Solicitação reprovada : O ícone abaixo será exibido, e o evento não será considerado no cálculo da folha.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/574ca4e4c6979138ff609a77/images/6765d08f6f0cc22ccff87eaf/file-YMvpAZAvc0.png)

Solicitação **pendente**: O ícone abaixo será exibido, indicando que a solicitação ainda precisa ser respondida.

![Imagem 9: Solicitação pendente : O ícone abaixo será exibido, indicando que a solicitação ainda precisa ser respondida.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/574ca4e4c6979138ff609a77/images/6765d0bda7c4aa1cadfab1d1/file-90a6Yy5pAu.png)

---

## ✨ Novidades de Solicitações

### Separação de solicitações

Agora, o sistema separa automaticamente as solicitações que você precisa aprovar daquelas que você mesmo criou. A tela passa a contar com duas abas: Solicitações da minha equipe, para a gestão do time, e Minhas solicitações, onde você acompanha o status dos seus pedidos sem misturar os perfis. Além disso, agora é possível cancelar solicitações pendentes diretamente na aba Minhas solicitações

![Visão das Solicitações de um usuário de gestor que possui empregado associado](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_664piq.png)

Visão das Solicitações de um usuário de gestor que possui empregado associado

### Cancelamento de solicitações pelo próprio usuário

Agora o usuário tem mais autonomia para corrigir erros! Se uma solicitação incorreta foi enviada, pode cancelá-la diretamente na aba **"Minhas solicitações"**, desde que ela ainda esteja com o status **"Pendente de resposta"**.

**Regras:**

- O botão de cancelamento aparece apenas para o usuário que criou a solicitação.
- Não é possível cancelar pedidos já analisados (aprovados/reprovados), vencidos ou gerados automaticamente pelo sistema.
- Gestores e RH podem cancelar apenas os seus próprios pedidos, mantendo o fluxo de aprovação/reprovação para as solicitações da equipe.

![Imagem 11: Gestores e RH podem cancelar apenas os seus próprios pedidos, mantendo o fluxo de aprovação/reprovação para as…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1nin4w6.png)

---

> ⚠️ Atenção:

- A funcionalidade **Solicitações** está inclusa no módulo "**Gestão de Ponto Participativa**". Se sua empresa ainda não adquiriu este módulo, mas deseja contar com essa funcionalidade, entre em contato com o nosso Time de Sucesso do Cliente.
- A funcionalidade **Solicitação de férias** está inclusa no módulo "**Gestão de Férias**". Se sua empresa ainda não adquiriu este módulo, mas deseja contar com essa funcionalidade, entre em contato com o nosso Time de Sucesso do Cliente.
- A funcionalidade **Solicitação de Horas Extras** está inclusa no módulo "**Controle de Custos**". Se sua empresa ainda não adquiriu este módulo, mas deseja contar com essa funcionalidade, entre em contato com o nosso Time de Sucesso do Cliente.

---

Gerenciar as solicitações é fundamental para garantir a precisão e a transparência nos registros da folha de ponto. A funcionalidade permite **descentralizar** tarefas, possibilitando que supervisores ou outros perfis realizem lançamentos diretamente no sistema. Ainda assim, todas as ações podem ser validadas por gestores ou RH, assegurando que o controle e a conformidade sejam mantidos. Com opções para aprovações e reprovações individuais ou em massa, além da geração de relatórios detalhados, essa ferramenta otimiza o fluxo de trabalho e promove maior organização no processo.

Caso ainda tenha dúvidas ou precise de auxílio, entre em contato com o nosso time de Suporte pelo chat integrado ao [site Pontotel Gestão](https://gestao.pontotel.com.br/#/cognito/login) ou pelo [WhatsApp](https://api.whatsapp.com/send/?phone=551131852700&text&type=phone_number&app_absent=0)!
