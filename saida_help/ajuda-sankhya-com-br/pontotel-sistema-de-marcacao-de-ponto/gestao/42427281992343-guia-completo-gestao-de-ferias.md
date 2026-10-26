---
id: "42427281992343"
titulo: "Guia Completo: Gestão de Férias"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427281992343-Guia-Completo-Gest%C3%A3o-de-F%C3%A9rias"
trilha: "PONTOTEL: Sistema de marcação de ponto > Gestão"
atualizado_em: "2026-08-03T13:29:52Z"
rotulos: ["sync_hc", "pontotel_6a33285ade1116dd764124dc", "pontotel", "sync_hash_2bd3bb2a27ac"]
---

# Guia Completo: Gestão de Férias

A gestão de férias é um dos processos mais críticos do RH. Envolve prazos legais, cálculos financeiros, organização de escalas e, claro, o bem-estar do colaborador.
Para transformar essa rotina em algo **simples**, **transparente** e descentralizado, a Pontotel desenvolveu o **Módulo de Gestão de Férias**. Ele permite que colaboradores solicitem seus períodos de descanso, que gestores aprovem com visão da capacidade do time e que o RH tenha controle total das regras, tudo em um único lugar.

> 💎 Funcionalidade Exclusiva: as ferramentas apresentadas neste artigo fazem parte do módulo adicional "Gestão de Férias". Caso sua empresa ainda não possua esse módulo e queira levar mais automação, controle e estratégia para o RH, agende uma apresentação exclusiva sem compromisso: <https://zcal.co/i/BEMijplm>

---

## Como configurar uma regra de férias

Antes de iniciar as solicitações, é fundamental definir as "regras do jogo". A **Regra de Férias** permite que você parametrize os limites e permissões de acordo com a política da sua empresa.

1. No menu de navegação do [site Gestão](https://gestao.pontotel.com.br/), abra o menu **Regras** e clique em **Férias**.
2. Clique em **Criar nova regra**.
3. Defina os parâmetros:

   - **Nome da regra:** Defina um nome para identificação interna
   - **Status**: Defina se a regra estará **ativa** ou **inativa**. Se inativada, ela não será considerada para a gestão de férias.
   - **Data limite para iniciar férias com o adiantamento da 1ª parcela do 13º:** Aqui você define o prazo máximo para o início do gozo das férias que permite solicitar o adiantamento. Exemplo: Se você configurar "Dia 04 de Fevereiro", o colaborador só poderá marcar a opção de adiantamento do 13º se as férias dele começarem antes ou nesta data.
   - **Mês limite para solicitar o adiantamento da 1ª parcela do 13º:** Define até qual mês do ano a opção de "solicitar adiantamento" ficará disponível. Após o período configurado, o adiantamento não poderá ser solicitado.
   - **Permitir pedir férias no período aquisitivo:**
   - **Desmarcado:** O colaborador só pode pedir férias após completar 1 ano de casa (período concessivo).
   - **Marcado:** O colaborador pode pedir férias proporcionais antes de completar 1 ano (férias antecipadas), conforme a política da empresa.
   - **Quando for lançado (Público-Alvo):**
   - Defina quem deve obedecer a esta regra. Você pode vincular por **Locais de Trabalho**, **Empregados** específicos, **Grupos** ou **Perfis de Acesso**.
   - **Hierarquia das Regras (Prioridade)** Se um colaborador estiver vinculado a mais de uma regra (ex: uma regra para o Local de Trabalho dele e outra para o Grupo dele), o sistema seguirá esta ordem de prioridade para decidir qual aplicar:
     - Regra do **Perfil de Usuário** (Maior prioridade).
     - Regra do **Empregado**.
     - Regra do **Local de Trabalho**.
     - Regra do **Grupo** (Menor prioridade).

   ![Imagem 1: Regra do Grupo (Menor prioridade).](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1ll9eq5.png)
4. Finalize clicando em **Salvar**

---

## Como fazer a gestão de férias | Visão geral e navegação

1. No menu de navegação do [site Gestão](https://gestao.pontotel.com.br/), abra o menu **Férias** e selecione a opção **Controle de férias**.
2. Esta é a central de comando. O que é exibido nela variam de acordo com as permissões do usuário:

   - **Usuário com acesso apenas aos próprios dados (como a permissão de funcionário):** Visualiza as abas "Minhas solicitações de férias" e "Minhas férias já programadas".
   - **Usuário com permissão de acesso à todos ou alguns locais (que não tem empregado vinculado):** Visualiza as abas "Solicitações de férias" e "férias dos meus liderados já programadas".
   - **Usuário com permissão de acesso à todos ou alguns locais (que tem empregado vinculado):** Tem visão completa de todas as abas e filtros avançados.

   ![Visão completa da tela de Gestão de Férias](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1gqks5r.png)

   Visão completa da tela de Gestão de Férias

### Para Gestores e RH (Visão da Equipe)

- **Aba ‘Solicitações de Férias’:**

  - **O que mostra:** Todas as solicitações feitas pelos seus liderados que ainda precisam de análise.
  - **Filtros:** Você pode buscar por local, empregado, grupo ou perfil.
  - **Dica de Uso:** A busca não é automática! Selecione os filtros desejados e clique em **Buscar**. O sistema salva seu último filtro para agilizar o próximo acesso.

  ![Imagem 3: Dica de Uso: A busca não é automática! Selecione os filtros desejados e clique em Buscar . O sistema salva seu último…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_14h6r5d.png)
- **Aba ‘Férias dos meus liderados já programadas’:**

  - **O que mostra:** As férias que já foram **aprovadas** e agendadas.
  - **Filtros:** Mesma lógica da aba anterior (local, empregado, etc). A data padrão vem preenchida com o mês atual, mas você pode alterar para ver o ano todo.

  ![Imagem 4: Filtros: Mesma lógica da aba anterior (local, empregado, etc). A data padrão vem preenchida com o mês atual, mas você…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_lmae0f.png)

### Para Colaboradores (Visão Pessoal)

- **Aba ‘Minhas solicitações de férias’:**

  - Mostra o histórico dos seus pedidos e o status de cada um (Pendente, Aprovado ou Reprovado).
  - A busca é automática ao entrar na aba, trazendo dados do ano atual.

  ![Imagem 5: A busca é automática ao entrar na aba, trazendo dados do ano atual.](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_c2cd2n.png)
- **Aba ‘Minhas férias já programadas’:**

  - Mostra suas férias futuras já confirmadas. É aqui que você consulta quando será seu próximo descanso.

  ![Imagem 6: Mostra suas férias futuras já confirmadas. É aqui que você consulta quando será seu próximo descanso.](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1bfwru5.png)

---

## Como agendar ou solicitar férias | fluxo de solicitação

Existem dois caminhos principais, dependendo de quem está operando o sistema:

### Cenário A: O Colaborador ou Gestor solicita

1. Na tela de Gestão de Férias, clique no botão **Solicitar Férias** (ou "Agendar Férias" na aba de liderados).
2. Preencha a data de início. O sistema preenche a data final automaticamente baseada nos dias solicitados (padrão 30 dias, mas editável).
   - Nota: O sistema valida automaticamente regras como antecedência mínima de 30 dias e proibição de início em DSR/Feriado.
3. Se desejar, marque as opções de **abono Pecuniário** (dias vendidos) ou **adiantamento do 13º** (se estiver dentro do prazo da regra).
4. Ao clicar em Salvar, gera-se uma **Solicitação Pendente**
   - **Status:** Pendente (aguardando aprovação).
   - **Visualização:** Aparece na aba de solicitações e na folha de ponto (como pendência).

### Cenário B: O RH agenda (Permissão Administrativa)

1. O usuário com perfil de RH segue o mesmo processo de preenchimento.
2. Porém, ao clicar em Salvar, **não é gerada pendência**.
   - **Status:** As férias entram diretamente como **Agendadas/Aprovadas**.
   - **Visualização:** Já aparecem na aba "Férias Programadas" e na folha de ponto como jornada oficial.

---

## Como aprovar ou reprovar solicitações | fluxo de resposta

Se você é gestor ou RH e precisa aprovar os pedidos da equipe:

1. Acesse a tela de [Solicitações](https://sankhya.zendesk.com/hc/pt-br/articles/42427228755863) (`Gestão > Solicitações`).
2. Em **Tipo de evento**, selecione "**Férias**".
3. Localize o pedido de férias com status **Pendente**.
4. Analise as datas e selecione a linha do pedido correspondente.
5. No menu que abrirá, clique em **Aprovar**ou **Reprovar**.

   - **Se Aprovado:** A solicitação vira "Férias Agendadas" e atualiza a jornada do colaborador.
   - **Se Reprovado:** A solicitação é encerrada e não impacta a folha.

   ![Imagem 7: Se Reprovado: A solicitação é encerrada e não impacta a folha.](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1pi0el3.png)

---

## Como solicitar e excluir solicitações

Entender a diferença entre essas duas ações é vital para a organização da folha:

### Cancelamento (Para solicitações que AINDA NÃO foram aprovadas)

Se o colaborador pediu férias, mas mudou de ideia antes do gestor aprovar (status "Pendente"):

- O colaborador, gestor ou RH podem acessar "Solicitações" e clicar em **Cancelar**.
- **Resultado:** O pedido desaparece da lista de pendências do gestor. Nenhuma ação de aprovação é necessária.

![Imagem 8: Resultado: O pedido desaparece da lista de pendências do gestor. Nenhuma ação de aprovação é necessária.](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_2k53k7.png)

### Exclusão (Para férias que JÁ ESTÃO agendadas/aprovadas)

Se as férias já estão marcadas na folha e precisam ser desfeitas, o processo é mais rigoroso:

1. O colaborador ou gestor acessa a aba de "Férias Programadas" e clica no ícone de **lixeira** (Excluir).
2. Isso **não apaga** as férias na hora! Isso gera uma **Solicitação de Exclusão**.
3. O RH ou Gestor responsável receberá essa solicitação na tela de [Solicitações](https://sankhya.zendesk.com/hc/pt-br/articles/42427228755863).
   - **Se Aceitar a exclusão:** As férias são removidas da folha e o saldo retorna para o colaborador.
   - **Se Negar a exclusão:** As férias permanecem agendadas e o colaborador deve cumpri-las.

> ⚠️ Atenção: Se um usuário com perfil de RH (Administrador) clicar em excluir, a exclusão é imediata, sem gerar solicitação.

![Imagem 9: ⚠️ Atenção: Se um usuário com perfil de RH (Administrador) clicar em excluir, a exclusão é imediata, sem gerar…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1s75uih.png)

---

## Visualização na Folha de Ponto

Uma vez que as férias estão com status **Agendado/Aprovado**, elas deixam de ser apenas um pedido e se tornam a **Jornada Oficial** do colaborador para aquele período.
Ao acessar a folha de ponto (`Folha > Folha de pontos`), você verá os dias correspondentes marcados como **"Férias"** na coluna de jornada. Isso isenta o colaborador de registrar ponto e garante que os cálculos de pagamento e benefícios sejam feitos corretamente, sem gerar faltas indevidas.

![Visualização do status da solicitação e da jornada esperada na folha de ponto](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_lgaabw.png)

Visualização do status da solicitação e da jornada esperada na folha de ponto

---

> 💡 Dicas:

- Quer sair das listas e ter uma visão clara de quem sai e quem fica, evitando desfalques na equipe? Conheça o novo **Calendário de Férias**! Com ele, você visualiza todas as ausências em uma linha do tempo interativa e ainda conta com um **Assistente de IA** para te ajudar a tomar as melhores decisões. [Clique aqui](https://sankhya.zendesk.com/hc/pt-br/articles/42427333429655) e veja o artigo completo!
- Caso queira fazer a gestão de férias da sua equipe pelo Aplicativo Pontotel Gestão, consulte [este artigo](https://sankhya.zendesk.com/hc/pt-br/articles/42427288969111) e veja o passo a passo!

---

O módulo de Gestão de Férias elimina planilhas paralelas e trocas intermináveis de e-mail, centralizando tudo na plataforma Pontotel com segurança jurídica e agilidade.

Caso ainda tenha dúvidas ou precise de auxílio, entre em contato com o nosso time de Suporte pelo chat integrado ao [site Gestão](https://gestao.pontotel.com.br/#/cognito/login) ou pelo [WhatsApp](https://api.whatsapp.com/send/?phone=551131852700&text&type=phone_number&app_absent=0).
