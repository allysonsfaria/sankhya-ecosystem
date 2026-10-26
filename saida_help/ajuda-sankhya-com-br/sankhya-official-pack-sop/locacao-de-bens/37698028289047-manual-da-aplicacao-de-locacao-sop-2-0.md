---
id: "37698028289047"
titulo: "Manual da aplicação de locação SOP 2.0"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37698028289047-Manual-da-aplica%C3%A7%C3%A3o-de-loca%C3%A7%C3%A3o-SOP-2-0"
trilha: "Sankhya Official Pack - SOP > Locação de bens"
atualizado_em: "2026-07-22T14:09:53Z"
rotulos: ["Configuração", "Contrato", "faturamento", "locação", "tipos de locação", "categoria de equipamentos", "categoria de operadores", "documentação de operadores", "locação e proposta", "agenda de locação", "locação de bens", "gestão de contratos", "aditivos", "itens da locação", "contrato de locação", "remessa e retorno locação", "SOP", "ERP", "Gestão de Ativos"]
---

# Manual da aplicação de locação SOP 2.0

### **(1)** Introdução

A aplicação SOP Locação 2.0 representa uma evolução significativa na gestão de processos de locação de equipamentos, bens e serviços. Desenvolvida para atender às crescentes demandas do mercado, esta nova versão aprimora e expande as funcionalidades existentes, oferecendo uma solução mais robusta, flexível e automatizada. O foco principal é otimizar o ciclo de vida completo da locação, desde a criação de propostas até o faturamento e a gestão de contratos, incorporando controles detalhados sobre equipamentos, componentes e operadores. A arquitetura da solução foi projetada para integrar-se de forma eficiente com outros módulos do sistema ERP, garantindo consistência de dados e fluidez operacional.

### **(2)** Objetivo da Aplicação

O objetivo primordial da aplicação SOP Locação 2.0 é fornecer uma plataforma abrangente e intuitiva para a gestão eficiente de locações. Isso inclui:

- **Otimização de Processos:** automatizar e simplificar as etapas envolvidas na locação, desde a negociação inicial até o encerramento do contrato.
- **Controle Preciso de Ativos:** manter um controle rigoroso sobre a disponibilidade, localização e status de cada equipamento e componente locado.
- **Flexibilidade Comercial:** permitir a configuração de diversas modalidades de locação, adaptando-se às necessidades específicas de cada cliente e tipo de serviço.
- **Gestão Financeira Acurada:** assegurar o faturamento correto e pontual, com base em medições de uso e reajustes contratuais automatizados.
- **Rastreabilidade e Auditoria:** fornecer um histórico detalhado de todas as operações e alterações nos contratos e equipamentos.
- **Integração:** garantir a comunicação eficiente com módulos de vendas, financeiro e patrimônio do ERP, para uma visão unificada da operação.

Em suma, a aplicação visa aprimorar a capacidade da empresa de gerenciar suas operações de locação de forma mais estratégica, reduzindo custos operacionais, minimizando erros e maximizando a satisfação do cliente.

### **(3)** Cadastros Principais

A aplicação SOP Locação 2.0 é estruturada sobre uma base sólida de cadastros, que permitem a parametrização e o controle detalhado de todos os elementos envolvidos no processo de locação. Estes cadastros são fundamentais para a flexibilidade e a precisão da solução.

#### **(1)** Locais e Obras

Este cadastro é projetado para gerenciar os diferentes endereços ou locais de atuação de um mesmo parceiro (cliente). A sua finalidade principal é otimizar o controle logístico e fiscal, facilitando a emissão de notas fiscais e a organização das entregas e coletas dos equipamentos. Ao permitir que um cliente tenha múltiplos locais/obras associados, o sistema assegura que cada operação de locação seja vinculada ao seu destino exato, melhorando a rastreabilidade e a acuracidade das informações para faturamento e gestão de projetos. Este recurso é crucial para clientes que operam em diversas frentes de trabalho simultaneamente, como construtoras ou empresas de infraestrutura.

#### **(1)** Tipo de Locação

O cadastro de Tipos de Locação é um dos pilares da flexibilidade da aplicação. Ele permite a definição de modelos padronizados de locação, que podem ser replicados para diversas operações, ao mesmo tempo em que oferece a liberdade para ajustes pontuais conforme a necessidade. Cada Tipo de Locação pode ser configurado com regras específicas que governam seu comportamento comercial, financeiro e operacional. Isso inclui:

- **Ativação:** Controla se o Tipo de Locação está disponível para uso.
- **Descrição:** Identificação clara do tipo (ex: “Diária”, “Contrato Mensal”, “Diária HT/HD”).
- **Tipo de Cobrança:** Define a periodicidade de cobrança (Diária, Semanal, Quinzenal, Mensal, Diária HT/HD).
- **Alocação:** Determina como o equipamento é reservado:

  - **Por Demanda:** Equipamento alocado em períodos específicos, mediante agendamento.
  - **Tempo de Contrato:** Equipamento reservado durante toda a vigência do contrato.
- **Vigência:** Definição de tempo mínimo e máximo de contrato em dias.
- **Reajuste:** Indica se o tipo de locação permite reajuste periódico e qual índice de reajuste (ex: IGPM, IPCA) será utilizado.
- **Medição:** Configura se o contrato requer medição de uso (horas ou quilômetros), com opções de frequência (Diária, Mensal, Global) e dias de início/fim da medição.
- **Faturamento:** Dia padrão para emissão do faturamento.
- **Operador:** Define a obrigatoriedade de alocação de operadores (Sim, Não, Opcional).

Essa granularidade na configuração permite que a empresa crie e gerencie uma vasta gama de ofertas de locação, desde as mais simples até as mais complexas, garantindo que as regras de negócio sejam aplicadas de forma consistente e automatizada. As validações automáticas ao salvar garantem a coerência entre as configurações, como a obrigatoriedade de preencher o Tipo de Medição e Frequência se “Tem Medição” for ativado. Este recurso é essencial para padronizar processos e reduzir erros operacionais.

##

#### **(1)** Itens de Locação

O cadastro de Itens de Locação é o ponto central para a gestão dos equipamentos e bens que serão disponibilizados para locação. Este cadastro permite um controle aprimorado sobre cada item, independentemente de sua natureza (produto ou bem patrimonial), oferecendo flexibilidade para empresas que utilizam ou não o módulo patrimonial do ERP. As informações registradas aqui são cruciais para a gestão de disponibilidade, agendamento, medição e faturamento.

Os principais atributos e regras de negócio associados aos Itens de Locação incluem:

- **Identificação e Status:** Cada item possui uma identificação única e um Status que reflete sua situação atual (Disponível, Reservado, Em Manutenção, Locado). Apenas itens Ativos e com Status = Disponível podem ser alocados. A transição para Locado é automática na remessa de saída e o retorno para Disponível ocorre após o registro da devolução.
- **Vínculo com ERP:** Possibilidade de vincular o item a um Código do Produto (para integração com estoque e faturamento) ou a um Código do Bem (para integração com o módulo de Patrimônio), garantindo a integridade dos dados.
- **Configurações Específicas:**

  - **Aceita Componente:** Define se o item pode ter acessórios vinculados, permitindo a inclusão de componentes opcionais ou obrigatórios na proposta.
  - **Categoria:** Vincula o item a uma Categoria de Equipamento, herdando regras de controle de capacidade e precificação.
  - **Capacidade:** Campo obrigatório se a Categoria exigir controle de capacidade (ex: 30 toneladas para uma escavadeira).
  - **Categorias de Operadores Aptos:** Indica quais tipos de operadores estão habilitados para manusear o item.

Este cadastro é fundamental para a precisão na gestão da frota e dos ativos, assegurando que cada equipamento seja locado sob as condições corretas e com a devida rastreabilidade. A integração com a agenda bloqueia automaticamente a disponibilidade durante agendamentos ou manutenções, evitando conflitos.

##

#### **(1)** Categoria de Equipamentos

A Categoria de Equipamentos é um agrupamento lógico que permite classificar equipamentos com características similares, tanto para fins técnicos quanto comerciais. Este cadastro é crucial para a definição de regras de negócio e precificação, trazendo um nível de organização e automação que otimiza a gestão de grandes frotas. As principais características incluem:

- **Descrição:** Nome da categoria (ex: “Guindaste”, “Escavadeira”, “Compressor de Ar”).
- **Controle de Capacidade:** Um indicador (Sim/Não) que define se os equipamentos desta categoria terão controle de capacidade. Se ativado, exige a definição de uma Unidade de Capacidade (ex: Toneladas, Litros, Metros cúbicos).

**Regras de Negócio:**

- A Categoria de Equipamento é um critério obrigatório na Tabela de Preços de Locação, permitindo a criação de faixas de preço diferenciadas com base na categoria e capacidade.
- Cada Item de Locação só pode ser vinculado a uma única Categoria.
- Se o controle de capacidade estiver ativo, o sistema exige o preenchimento da capacidade padrão ao cadastrar um novo item de locação nessa categoria.

Este cadastro é fundamental para a flexibilidade na precificação e na gestão de recursos, permitindo que a empresa adapte suas ofertas de locação de acordo com as especificidades de cada tipo de equipamento.

#### **(1)** Categoria de Operadores

A Categoria de Operadores permite a classificação dos profissionais que operam os equipamentos, com base nos tipos de máquinas para os quais estão aptos. Este cadastro é essencial para garantir que o operador correto seja alocado para o equipamento adequado, aumentando a segurança e a eficiência das operações. As principais características são:

- **Descrição:** Campo texto para definir o nome da categoria (ex: “Motorista”, “Maquinista de Guindaste”, “Operador de Escavadeira”).

**Regras de Negócio:**

- Um operador pode ser vinculado a uma ou mais Categorias de Operadores, refletindo suas múltiplas habilidades.
- No momento do agendamento de um equipamento, o sistema realiza uma validação automática para assegurar que o operador selecionado possui a categoria necessária para operar o tipo de equipamento em questão. Isso evita alocações indevidas e garante a conformidade com as exigências operacionais e de segurança.

Este recurso aprimora a gestão de recursos humanos, garantindo que apenas operadores qualificados sejam designados para tarefas específicas, o que é vital em operações de locação de equipamentos pesados ou especializados.

### **(1)** Documentação de Operadores

O cadastro de Documentação de Operadores é um módulo que permite o gerenciamento dos documentos, certificados e licenças exigidos dos operadores para a execução de suas funções. Este controle é fundamental para a conformidade legal, a segurança operacional e a garantia de que os profissionais estão devidamente qualificados. As características incluem:

- **Descrição:** Campo texto para definir o tipo de documento (ex: “Certificado de Operador de Guindaste”, “Treinamento NR-12”).
- **Tem Validade:** Campo Sim/Não que indica se o documento requer controle de validade. Se Sim, o sistema exige a data de validade e emite alertas próximos ao vencimento.
- **Anexo:** Permite o upload de arquivos (PDF, imagens) para armazenar digitalmente os documentos dos operadores.

**Regras de Negócio:**

- Se um documento for configurado com Tem Validade = Sim, o sistema obriga o preenchimento da data de validade e pode emitir notificações ou bloquear a alocação de operadores com documentos vencidos.
- Este cadastro se integra com a Categoria de Operadores e com o agendamento, garantindo que apenas operadores com documentação válida e adequada sejam escalados para as operações.

Este recurso é vital para a gestão de riscos e para assegurar que a empresa esteja em conformidade com as regulamentações trabalhistas e de segurança, além de facilitar a auditoria e o acesso rápido às informações dos operadores.

###

### **(4)** Jornada do Usuário e Processos Operacionais

A jornada do usuário na aplicação SOP Locação 2.0 é projetada para ser intuitiva e eficiente, guiando o usuário através das etapas cruciais da locação, desde a criação da proposta até o faturamento e a gestão pós-contrato. Cada processo é suportado por funcionalidades robustas e automatizações que visam reduzir a carga de trabalho manual e minimizar erros.

#### **(1)** Portal de Locação e Proposta

O Portal de Locação é o ponto de entrada para o vendedor iniciar o processo de locação, no qual as propostas são criadas e gerenciadas. A proposta funciona como um documento pré-contrato, permitindo a negociação e a validação de condições antes da formalização. A flexibilidade é um ponto chave, permitindo que o usuário configure diversas informações financeiras e de faturamento diretamente na proposta.

**Funcionalidades Principais:**

- **Criação e Configuração:** O usuário pode montar a proposta inserindo informações essenciais como parceiro (cliente), local/obra, vigência do contrato, e detalhes financeiros. A flexibilidade do faturamento é destacada, permitindo a escolha de frequências de faturamento variadas (diário, semanal, quinzenal, mensal), dias fixos de faturamento, entre outros.
- **Inclusão de Itens, Componentes e Operadores:** A proposta permite adicionar os Itens de Locação (equipamentos), seus Componentes (acessórios, que podem ser opcionais ou obrigatórios) e os Operadores necessários para a operação. O sistema valida a disponibilidade desses recursos em tempo real.
- **Cálculo de Vigência e Valores:** O sistema calcula automaticamente a vigência e os valores por item, considerando as configurações do Tipo de Locação e as regras de precificação.
- **Geração do Documento da Proposta:** Após a montagem, é possível gerar um documento formal da proposta para ser enviado ao cliente.
- **Confirmação e Aprovação:** Uma vez que o cliente aprova a proposta, o usuário retorna ao sistema para Confirmar Proposta. Este processo pode envolver um fluxo de aprovação interno, onde a proposta pode ser enviada para aprovação e, após ser aprovada, pode ser editada. Qualquer alteração após a aprovação retorna o status para “Aguardando Aprovação”, exigindo uma nova validação.
- **Geração de Contrato:** Após a aprovação e confirmação da proposta, o sistema habilita a opção para Gerar Contrato, consolidando todos os itens aprovados e suas configurações em um único contrato.

Este processo garante que todas as condições comerciais e operacionais sejam acordadas e validadas antes da formalização do contrato, minimizando riscos e garantindo a conformidade.

#### **(1)** Contrato de Locação

O Contrato de Locação é o documento oficial que formaliza a operação, sendo gerado a partir de uma Proposta de Locação aprovada. Ele serve como a base para o controle operacional, financeiro e fiscal de toda a locação. A aplicação garante que todas as informações aprovadas na proposta sejam transferidas para o contrato, consolidando múltiplos itens em um único documento, mesmo que possuam diferentes tipos de cobrança, necessidades de operador ou regras de medição.

**Características e Regras Principais:**

- **Geração Automática:** O contrato é gerado automaticamente a partir de uma proposta aprovada, herdando a periodicidade de faturamento definida no cabeçalho da proposta. Isso assegura a consistência entre a negociação e a formalização.
- **Estrutura Detalhada:** O contrato inclui:

  - Número do Contrato, Empresa, Parceiro (Cliente), Local/Obra.
  - Vigência geral do contrato (Data Início e Fim).
  - Periodicidade de Faturamento (Diário, Semanal, Quinzenal ou Mensal).
  - Itens Locados, cada um com suas configurações individuais: Tipo de Locação, Tipo de Cobrança, Valor Unitário e Total, Necessidade de Operador, Franquia, Regra de Medição, Data de Início e Término da Locação por item.
  - Sub-abas para Componentes (quando aplicável) e Operadores Alocados (quando aplicável).
  - Condições Comerciais (valores, reajustes, franquias por item) e Forma de Faturamento.
  - Histórico de Remessas e Retornos de Equipamentos.

- **Confirmação do Contrato:** Após a conferência das informações, o usuário pode Confirmar Contrato. Ao clicar neste botão, um pop-up será exibido, exigindo o anexo do contrato assinado digitalmente ou fisicamente escaneado. Somente após o anexo e a confirmação, o contrato é ativado para liberação de agendamentos, remessas, medições e faturamentos. Uma vez confirmado e com o anexo validado, o contrato não permite alterações estruturais, que devem ser feitas via Aditivos Contratuais.
- **Integração:** O contrato se integra diretamente com a Agenda de Equipamentos e Operadores, Medição de Contratos, Faturamento e Reajustes Automáticos, garantindo que todas as movimentações operacionais, logísticas e financeiras sejam controladas com base neste documento.
- **Validações:** O sistema impede movimentações fora da vigência geral do contrato e das datas específicas de locação de cada item, além de não permitir a criação de contratos sem o preenchimento de cadastros obrigatórios.

Este módulo centraliza a gestão da locação, proporcionando uma visão completa e controlada de cada acordo com o cliente.

####

#### **(1)** Remessa e Retorno

As operações de remessa e retorno de equipamentos são etapas cruciais na jornada da locação, marcando o início e o fim físico do período de utilização do bem pelo cliente. A aplicação SOP Locação 2.0 automatiza e controla essas movimentações, garantindo a integridade do estoque e a atualização correta do status dos Itens de Locação e Componentes.

**Processo de Remessa:**

- **Geração da Remessa:** Após a confirmação do contrato, o usuário pode gerar a remessa de saída diretamente pela tela do contrato. Esta ação é fundamental, pois ela formaliza a entrega do equipamento ao cliente. As remessas podem ser realizadas por itens específicos ou para todos os itens do contrato de uma só vez.
- **Atualização de Status:** A geração da remessa de saída provoca a alteração automática do status do Item de Locação (e de seus componentes vinculados) de Disponível ou Reservado para Locado. Isso garante que o sistema reflita o estado real do equipamento, bloqueando-o para novas alocações durante o período de locação.
- **Faturamento Proporcional:** A data de remessa impacta diretamente o faturamento. **Exemplo:** se um contrato inicia no dia 1, mas o item é remetido apenas no dia 5, o sistema calcula o valor a ser cobrado proporcionalmente ao período de uso efetivo (a partir do dia 5), garantindo justiça e precisão na cobrança.
- **Integração com Vendas:** A remessa é gerada automaticamente no portal de vendas, assegurando a comunicação entre os módulos e a emissão dos documentos fiscais necessários.

**Processo de Retorno:**

- **Registro de Retorno:** Quando o equipamento é devolvido pelo cliente, o usuário registra o retorno na tela do contrato. Este registro vincula o retorno à remessa de saída correspondente, fechando o ciclo da movimentação física.
- **Atualização de Status:** O registro do retorno do equipamento altera automaticamente o status do Item de Locação (e de seus componentes) de Locado para Disponível. Isso libera o equipamento para novas locações ou manutenções, atualizando a agenda de disponibilidade.
- **Validação de Componentes:** No momento da devolução, o sistema pode validar o retorno de todos os componentes vinculados ao contrato, evitando perdas de ativos e garantindo a integridade do conjunto locado.

Essas funcionalidades garantem um controle logístico eficiente, com rastreabilidade completa das movimentações dos ativos e atualização automática de seus status, o que é vital para a gestão da disponibilidade e para a precisão dos registros contábeis e fiscais.

#### **(1)** Faturamento

O processo de faturamento na aplicação SOP Locação 2.0 é desenhado para ser flexível e automatizado, adaptando-se às diversas periodicidades e condições estabelecidas nos contratos. Ele garante a correta cobrança pelos serviços de locação, considerando as medições de uso e os reajustes contratuais.

**Etapas e Funcionalidades:**

- **Liberação do Faturamento no Contrato:** Após a geração da remessa de saída, o usuário pode Liberar Faturamento na tela do contrato. Este botão aciona o cálculo dos faturamentos futuros vinculados àquele contrato, preenchendo a tabela de controle de faturamento.
- **Flexibilidade de Faturamento:** A aplicação suporta diversas frequências de faturamento (diária, semanal, quinzenal, mensal) e a possibilidade de faturamento em dias fixos, conforme configurado no Tipo de Locação e na Proposta.
- **Controle de Faturamento:** Após a liberação do faturamento no contrato, o sistema gera um controle detalhado de todas as próximas faturas daquele contrato. Este controle oferece uma visão de negócio abrangente para o usuário, permitindo planejar receitas e acompanhar as cobranças futuras.
- **Faturamento Periódico e Dias Fixos:** Ao decorrer das datas necessárias, o usuário acessa a tela de faturamento para executar os faturamentos pendentes. Esta tela lista os contratos aptos a serem faturados com base na periodicidade e nas condições definidas. A mecânica de dias fixos de faturamento permite que os contratos tenham faturas em datas específicas, como todo dia 30, independentemente da data de início da locação.
- **Serviços Adicionais:** É possível adicionar serviços ao contrato, e esses serviços serão incluídos para serem cobrados na próxima fatura em questão, permitindo a cobrança de itens como transporte, montagem, ou outros serviços agregados à locação.
- **Impacto da Medição:** Para contratos que exigem medição de uso, o faturamento é diretamente impactado pelos dados coletados e aprovados na rotina de Medição, garantindo que a cobrança seja proporcional ao uso real do equipamento.

Este módulo assegura que a empresa possa gerenciar seu fluxo de receita de forma precisa e automatizada, com a capacidade de se adaptar a diferentes modelos de cobrança e integrar serviços adicionais ao faturamento. É importante ressaltar que todas as notas fiscais serão geradas utilizando o endereço cadastrado no local/obra associado ao contrato.

####

#### **(1)** Medição

A funcionalidade de Medição é crucial para contratos de locação onde o custo ou a cobrança estão diretamente vinculados ao uso efetivo do equipamento (ex: horas de motor, quilômetros rodados). Este módulo permite o registro, controle e aprovação dos dados de uso, impactando diretamente o faturamento do contrato.

**Processo e Funcionalidades:**

- **Registro de Uso:** Para clientes que utilizam esta funcionalidade, o sistema permite o registro periódico dos dados de medição (horas, quilômetros) dos itens locados. A frequência de medição é definida no Tipo de Locação (Diária, Mensal, Global).
- **Fluxo de Aprovação:** As medições registradas podem passar por um fluxo de aprovação. Isso garante que os dados sejam verificados e validados antes de serem considerados para o faturamento.
- **Impacto no Faturamento:** Uma medição aprovada é utilizada como base para o cálculo do valor a ser faturado, garantindo que a cobrança seja proporcional ao uso real do equipamento. Contratos com medição obrigatória podem ter o faturamento bloqueado caso a medição não esteja aprovada, assegurando a conformidade com as regras contratuais.

Este recurso oferece transparência e justiça na cobrança, alinhando o valor da locação ao consumo real do equipamento, o que é um diferencial importante para certos modelos de negócio.

#### **(1)** Aditivos e Ocorrências

A gestão de contratos de locação frequentemente exige a capacidade de realizar alterações após a formalização inicial. A aplicação SOP Locação 2.0 oferece funcionalidades robustas para a criação de aditivos contratuais e o registro de ocorrências, garantindo a flexibilidade necessária para adaptar os contratos às novas realidades e manter um histórico completo de todas as modificações.

**Aditivos Contratuais:**

- **Geração de Aditivos:** O sistema permite a geração de aditivos para contratos existentes, possibilitando a inclusão de novos itens, a prorrogação de prazos, a alteração de valores ou outras condições comerciais. Esta funcionalidade é essencial para acomodar mudanças nas necessidades do cliente ou nas condições de mercado sem a necessidade de criar um novo contrato do zero. Ao criar um aditivo, é necessário que ele também tenha seu faturamento liberado, o que irá acionar o recálculo completo do controle de faturamento do contrato pai, incorporando os novos valores do aditivo.
- **Atualização de Condições:** Ao gerar um aditivo, o sistema atualiza as condições do contrato principal, garantindo que todas as novas regras e valores sejam aplicados aos faturamentos e movimentações futuras.

**Lançamento de Ocorrências:**

- **Registro de Alterações e Eventos:** A funcionalidade de lançamento de ocorrências permite registrar eventos ou alterações significativas que afetam o contrato. Teremos alguns tipos de ocorrências pré-definidos, e ao serem processadas, executarão ações específicas no contrato. Isso pode incluir mudanças operacionais, observações relevantes, ou qualquer informação que precise ser associada ao histórico do contrato.
- **Impacto no Contrato e Faturamento:** Dependendo do tipo de ocorrência, ao ser processada, ela pode disparar ações automáticas no contrato, como a alteração de status, o ajuste de datas, e em algumas situações, pode ser necessário até recalcular o faturamento do contrato, garantindo que as implicações financeiras da ocorrência sejam refletidas.
- **Armazenamento de Histórico:** Todas as ocorrências são armazenadas, criando um histórico detalhado das interações e modificações do contrato. Este histórico é valioso para auditorias, resolução de disputas e para a compreensão completa da evolução do relacionamento com o cliente.

Essas ferramentas proporcionam uma gestão contratual dinâmica, permitindo que a empresa responda rapidamente às mudanças e mantenha um registro preciso e auditável de todas as adaptações e eventos relacionados ao contrato.

####

#### **(1)** Agenda de Locação

A Agenda de Locação é uma ferramenta visual crucial para a gestão da disponibilidade dos bens locados. Apresentada em um formato de calendário, ela oferece uma visão clara e organizada dos equipamentos que estão reservados, locados ou disponíveis em um determinado período. Através de filtros configuráveis, o usuário pode personalizar a visualização para focar em categorias específicas de equipamentos, locais de obra, ou status de locação, facilitando o planejamento e a tomada de decisões.

**Funcionalidades Principais:**

- **Visualização em Calendário:** Permite uma rápida identificação dos períodos de ocupação e disponibilidade dos equipamentos.
- **Filtros Dinâmicos:** Possibilita filtrar por status (reservado, locado, disponível), tipo de equipamento, local/obra, entre outros, para uma análise detalhada.
- **Gestão de Conflitos:** Ajuda a identificar e evitar conflitos de agendamento, garantindo que os equipamentos sejam alocados de forma eficiente e sem sobreposições.
- **Otimização de Recursos:** Oferece uma visão estratégica sobre a utilização da frota, auxiliando na otimização do uso dos ativos e na identificação de períodos de alta e baixa demanda.

Este módulo é essencial para o planejamento logístico e operacional, garantindo que os itens de locação sejam gerenciados de forma eficaz e que as promessas de entrega aos clientes sejam cumpridas com precisão.

### **(5)** Telas do Produto (Interfaces de Usuário)

Para facilitar a compreensão das funcionalidades e da jornada do usuário, as telas da aplicação são ilustradas a seguir. Estas imagens representam a interface do usuário e os pontos de interação com as funcionalidades descritas.

#####

#### **(1)** Tela de Cadastro de Tipos de Locação

Esta imagem ilustra a tela de cadastro de Tipos de Locação, onde o usuário pode configurar as diversas modalidades de locação, definindo regras de cobrança, alocação, vigência, reajuste, medição e necessidade de operador. Esta tela é fundamental para a flexibilidade comercial da aplicação.

![Tela de Cadastro de Tipos de Locação](https://ajuda.sankhya.com.br/hc/article_attachments/37698016359319)

Tela de Cadastro de Tipos de Locação

##

#### **(1)** Tela de Proposta de Locação (Cabeçalho)

Esta imagem apresenta o cabeçalho da tela de Proposta de Locação, onde são inseridas as informações gerais da proposta, como número da proposta, parceiro, local/obra, vigência do contrato, e detalhes de faturamento e financeiro. É o ponto de partida para a negociação com o cliente.

![Tela de Proposta de Locação (Cabeçalho)](https://ajuda.sankhya.com.br/hc/article_attachments/37698016360343)

Tela de Proposta de Locação (Cabeçalho)

##

#### **(1)** Tela de Proposta de Locação (Itens de Locação)

Esta imagem detalha a seção de Itens de Locação dentro da proposta, onde o usuário adiciona os equipamentos a serem locados, especificando a quantidade negociada, valor unitário, e as datas de início e término da vigência para cada item. Esta seção permite a gestão granular dos ativos na proposta.

![Tela de Proposta de Locação (Itens de Locação)](https://ajuda.sankhya.com.br/hc/article_attachments/37698016363927)

Tela de Proposta de Locação (Itens de Locação)

#### **(1)** Tela de Proposta de Locação (Componentes do Item de Locação)

Esta imagem mostra a sub-aba de Componentes do Item de Locação na proposta. Aqui, o usuário pode vincular acessórios ou itens complementares aos equipamentos principais, controlando a quantidade negociada e os valores associados. Essencial para locações que exigem kits de equipamentos ou acessórios específicos.

![Tela de Proposta de Locação (Componentes do Item de Locação)](https://ajuda.sankhya.com.br/hc/article_attachments/37698028284695)

Tela de Proposta de Locação (Componentes do Item de Locação)

#### **(1)** Tela de Proposta de Locação (Operadores Locação)

Esta imagem exibe a sub-aba de Operadores Locação na proposta. Nesta seção, o usuário pode alocar operadores para os itens de locação que exigem acompanhamento, garantindo que profissionais qualificados estejam associados à operação. A sequência do operador e o valor total são gerenciados aqui.

![Tela de Proposta de Locação (Operadores Locação)](https://ajuda.sankhya.com.br/hc/article_attachments/37698016366743)

Tela de Proposta de Locação (Operadores Locação)

#### **(6)** Considerações Finais

A aplicação SOP Locação 2.0 se estabelece como uma solução robusta e abrangente para a gestão de locações, oferecendo um controle granular e flexibilidade sem precedentes. A integração de cadastros detalhados, como Categorias de Equipamentos e Operadores, Tipos de Locação customizáveis, e a gestão completa de Itens de Locação e Componentes, cria uma base sólida para qualquer operação de locação. A jornada do usuário, cuidadosamente desenhada desde a Proposta até o Contrato, Remessa, Faturamento, Medição, Aditivos e Ocorrências, é suportada por automações inteligentes que minimizam a intervenção manual e maximizam a eficiência.

Em suma, o SOP Locação 2.0 não apenas atende às necessidades atuais do mercado de locação, mas também oferece uma plataforma escalável e adaptável para futuras evoluções, garantindo uma gestão mais estratégica, transparente e lucrativa.
