---
id: "21238784689943"
titulo: "Atualização do sistema Sankhya Om via WPM"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/21238784689943-Atualiza%C3%A7%C3%A3o-do-sistema-Sankhya-Om-via-WPM"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-09-29T14:06:23Z"
rotulos: ["Configuração", "Atualização", "WPM", "Módulos", "Sankhya Om"]
---

# Atualização do sistema Sankhya Om via WPM

## Sobre este artigo

Este artigo traz o passo a passo para atualizar o Sankhya Om, com os cuidados necessários em cada etapa.

Você tem duas opções: atualizar o sistema completo ou atualizar apenas um módulo específico, de forma independente. A segunda opção reduz o impacto na operação. Se é o seu caso, vá direto para a seção [Aba atualizações de módulos](https://ajuda.sankhya.com.br/hc/pt-br/articles/21238784689943-Atualiza%C3%A7%C3%A3o-do-sistema-Sankhya-Om-via-WPM#modulos).

**Neste artigo você vai encontrar:**

- [Atualizando o sistema via WPM](https://ajuda.sankhya.com.br/hc/pt-br/articles/21238784689943-Atualiza%C3%A7%C3%A3o-do-sistema-Sankhya-Om-via-WPM#sistema): o passo a passo completo para atualizar a versão do Sankhya Om.
- [Aba atualizações de módulos](https://ajuda.sankhya.com.br/hc/pt-br/articles/21238784689943-Atualiza%C3%A7%C3%A3o-do-sistema-Sankhya-Om-via-WPM#modulos): como atualizar módulos individualmente, sem precisar atualizar o sistema completo.
- [Módulos do Sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/21238784689943-Atualiza%C3%A7%C3%A3o-do-sistema-Sankhya-Om-via-WPM#descricao-modulos): uma descrição de cada módulo disponível para atualização independente.

| **O que é o WPM?**  O Web Package Manager (WPM) é o atualizador de pacotes do Sankhya Om, executado diretamente pelo navegador. É por meio dele que você aplica tanto as atualizações do sistema completo quanto as atualizações dos módulos individuais, sem precisar instalar nada manualmente no servidor. |
| --- |

---

## Atualizando o sistema via WPM

Esta seção descreve o processo de atualização do sistema completo, que envolve o core do Sankhya Om. Essa é a atualização tradicional e deve ser usada quando você quer aplicar uma nova versão do sistema como um todo.

Antes de iniciar, vale lembrar: **durante o processo todos os usuários precisarão estar fora do sistema**. Então é uma boa prática programar a atualização para um horário de baixa demanda e comunicar o time com antecedência.

### Passo 1 - acesse a tela de atualização

Para começar, abra a tela **Administração do Servidor**. Na aba **Geral**, clique em "Atualização do Sistema". É a partir daqui que todo o fluxo se inicia.

![Tela do Sankhya Om informando que o Atualizador do Sistema foi lançado em outra janela, com links para a Central de…](https://ajuda.sankhya.com.br/hc/article_attachments/40042051283479)

Tela exibida no Sankhya Om antes da nova guia do WPM ser aberta.

### Passo 2 - leia as informações sobre o processo

Na tela que será apresentada, o sistema exibe um resumo das informações sobre o processo de atualização. Vale uma leitura atenta antes de prosseguir: essa tela funciona como um checklist rápido do que está por vir.

Em seguida, o sistema abrirá uma nova guia no navegador com a tela de login do WPM. Se a nova guia não aparecer, verifique o bloqueador de pop-ups do seu navegador. É importante que ele esteja desativado para este domínio.

| **Observação**  Se a sua versão do WPM estiver desatualizada, não se preocupe: o sistema realizará a atualização do próprio WPM automaticamente antes de seguir para a atualização do Sankhya Om. |
| --- |

### Passo 3 - faça o login no WPM

Com a tela de login aberta, use as credenciais de acesso ao WPM. Se é a primeira vez que você acessa, considere os seguintes cenários:

- Para o primeiro acesso, utilize a senha "admin". Por questões de segurança, o sistema solicitará a alteração da senha logo em seguida.
- Se a senha "admin" não for aceita, experimente as senhas "tecsis" ou "123456". Se nenhuma delas funcionar, consulte o artigo [Como alterar a senha do WPM?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043864974-Como-alterar-a-senha-do-WPM).

![- **Alt text:** Tela de login do Web Package Manager com o logotipo Sankhya, o campo de senha em destaque e o botão…](https://ajuda.sankhya.com.br/hc/article_attachments/40042051287447)

Tela de login do WPM (Web Package Manager 9.0).

### Passo 4 - visualize as versões disponíveis

Depois de acessar o WPM, vá até a aba **Atualizações do sistema**. É nela que você encontra todas as opções de atualização disponíveis para o seu ambiente.

![: Aba Atualizações do sistema no WPM, exibindo a release atual 4.35b637 instalada e a versão 4.36b23 disponível para…](https://ajuda.sankhya.com.br/hc/article_attachments/40042051288599)

Modo simplificado da aba Atualizações do sistema.

Por padrão, o WPM exibe apenas versões estáveis (e betas, caso você tenha permissão). Para visualizar a lista completa, clique em **Exibir todas as versões**, no canto superior esquerdo da aba.

![Opção Exibir todas as versões em destaque no canto superior esquerdo da aba Atualizações do sistema, indicada por uma…](https://ajuda.sankhya.com.br/hc/article_attachments/40042040716439)

Localização do botão Exibir todas as versões.

As versões beta aparecem com um ícone identificador, para que você consiga diferenciá-las facilmente das versões estáveis.

![Lista completa de versões no WPM com o ícone de versão beta em destaque ao lado da versão 4.36b17, indicada por uma…](https://ajuda.sankhya.com.br/hc/article_attachments/40082182417815)

Ícone identificador de versão beta na lista de releases.

| **Atenção às versões beta**  Versões beta são liberadas para testes e podem conter ajustes pendentes. Avalie com cuidado antes de aplicar uma versão beta em ambiente de produção. |
| --- |

### Passo 5 - decida: atualizar agora ou agendar?

A partir deste ponto, você tem duas opções: executar a atualização imediatamente ou agendá-la para um momento mais conveniente. Escolha o cenário que se aplica ao seu caso.

#### Agendando a atualização

Se preferir agendar, clique em **Agendar a versão corrente**.

![Botão vermelho Agendar a versão corrente em destaque na aba Atualizações do sistema, com seta verde apontando para a…](https://ajuda.sankhya.com.br/hc/article_attachments/40042040717591)

Botão de agendamento da atualização.

Será exibido um pop-up para você informar a data e o horário desejados. Depois de preencher, clique em **Agendar**. O sistema confirmará o agendamento e já iniciará o download do pacote em segundo plano, para que tudo esteja pronto no horário combinado.

![Pop-up Agendamento da versão 4.36b17 com os campos de data e horário em branco e os botões Fechar e Agendar.](https://ajuda.sankhya.com.br/hc/article_attachments/40082158528407)

Formulário para agendar a atualização.

| **Sobre o fuso horário do agendamento**  A data e a hora informadas precisam ser maiores que a data e a hora atual do servidor onde o WPM está instalado. Isso é importante porque, se o seu fuso horário for diferente do servidor, o sistema sempre vai considerar o horário do servidor como referência. |
| --- |

Veja um exemplo prático:

- Hora atual no servidor (Uberlândia, GMT-03:00): 15h00.
- Usuário no fuso do Acre (GMT-05:00): hora local 13h00.
- Se o usuário tentar agendar para 14h00, o sistema rejeita, porque, para o servidor, 14h00 já passou.

Nesse cenário, a seguinte mensagem será exibida:

"A data e hora informadas devem ser maior que a data e hora atual do servidor. Data e hora atual do servidor: 13/11/2024 15:00."

#### Atualizando manualmente

Se preferir atualizar imediatamente, clique em **Obtenha a última versão**. O sistema iniciará o download da versão disponível.

![Card vermelho Obtenha a última versão exibindo a versão 4.36b23, com a data de disponibilização e o tamanho do pacote…](https://ajuda.sankhya.com.br/hc/article_attachments/40042040719255)

Botão de atualização manual para a versão mais recente.

### Passo 6 - instale a versão

Com o download concluído, clique em **Instalar versão agora!** para dar sequência ao processo. Em seguida, clique em **Prosseguir** para que o pacote seja instalado. A partir deste momento, o sistema executará a atualização.

| **Importante antes de prosseguir**   - Todos os usuários deverão estar fora do sistema durante a atualização. - Todas as informações do processo serão registradas em um log, que fica disponível para consulta. - Caso ocorra algum erro, entre em contato com o nosso suporte levando a mensagem de erro e o log do WPM. - Você pode baixar o log na opção disponível na aba **Configurações** do WPM. |
| --- |

### Passo 7 - aguarde a conclusão

O tempo de atualização varia conforme o tamanho do ambiente. Ao final do processo, o WPM exibirá uma mensagem de sucesso e reinicializará o sistema automaticamente. Depois disso, basta avisar os usuários que o Sankhya Om está de volta.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/21238784689943-Atualiza%C3%A7%C3%A3o-do-sistema-Sankhya-Om-via-WPM#sumario)

---

## Aba atualizações de módulos

| **Disponibilidade**  Esta aba está acessível a partir da versão 4.24 do Sankhya Om. |
| --- |

Com a modularização do Sankhya Om, cada módulo do sistema passa a ter seu próprio ciclo de atualização, independente do core do produto. Na prática, isso significa que você pode receber as evoluções dos módulos que mais utiliza sem precisar parar o sistema inteiro para aplicar uma atualização, uma mudança que reduz o impacto na operação e dá mais autonomia ao time de TI.

A aba **Atualizações de módulos** é onde você gerencia essas atualizações independentes.

### Quais módulos já contam com atualização independente?

Atualmente, o método está disponível para os seguintes módulos:

- Pessoal
- Livros Fiscais
- Contabilização
- Logística
- Manufatura
- ERP Core
- Imobilizado

Mais adiante, na seção [Módulos do Sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/21238784689943-Atualiza%C3%A7%C3%A3o-do-sistema-Sankhya-Om-via-WPM#descricao-modulos), você encontra uma descrição do que cada um desses módulos cobre, útil para identificar rapidamente o que será atualizado.

### Como acessar a aba

Para atualizar um módulo, acesse a aba **Atualizações de módulos** dentro do WPM. Nela, você consegue visualizar, em uma única tela:

- A versão que está instalada no seu ambiente para cada módulo.
- A versão disponível para atualização.
- A versão mínima do Sankhya Om necessária para instalar aquele módulo.

![Aba Atualizações de módulos no WPM com os cards de Contabilidade, ERP Core, Imobilizado, Livros Fiscais, Logística,…](https://ajuda.sankhya.com.br/hc/article_attachments/40042040720279)

Visão geral dos módulos disponíveis para atualização independente.

Essa visualização centralizada ajuda você a tomar a decisão de atualizar com mais segurança, verificando se o seu ambiente atende aos pré-requisitos antes mesmo de iniciar o processo.

### Como atualizar um módulo

Depois de decidir qual módulo você quer atualizar, o processo é direto. Siga os passos abaixo.

#### Passo 1 - abra os detalhes do módulo

Na aba **Atualizações de módulos**, clique na seta ao lado do módulo desejado. Será apresentada a opção **Ir para Detalhes do Módulo**.

![Tooltip Ir para Detalhes do Módulo exibido ao clicar na seta do card Pessoal, indicada por uma seta verde.](https://ajuda.sankhya.com.br/hc/article_attachments/40042051295895)

Acesso à tela de detalhes de um módulo.

#### Passo 2 - verifique a versão disponível

Ao selecionar essa opção, você acessa a tela com a data de disponibilidade da versão e a versão mínima exigida, esta última aparece quando a versão instalada no Sankhya é menor que a mínima requerida pelo módulo.

![Tela de detalhes do módulo Pessoal (mgepes) com a versão 5.89.5 instalada e o card Atualize para a versão 5.90.20, com…](https://ajuda.sankhya.com.br/hc/article_attachments/40042040722583)

Detalhes da versão disponível para o módulo Pessoal.

#### Passo 3 - inicie a atualização

Se tudo estiver certo, clique sobre o card do módulo para iniciar o processo. Como alternativa, você também pode iniciar a atualização clicando diretamente no botão de versão disponível.

Antes de iniciar a atualização, dê uma olhada nas novidades: o botão da versão disponível indica se o módulo recebeu alterações estruturais, novas funcionalidades ou correções. Assim você entra no processo sabendo exatamente o que esperar.

![Tooltip sobre o botão de versão 5.90.20 do módulo Pessoal, exibindo a data de disponibilização e a descrição "Novas…](https://ajuda.sankhya.com.br/hc/article_attachments/40042051302935)

Informações exibidas ao passar o mouse sobre o botão de versão disponível.

### O que acontece durante a atualização?

Esta é uma das grandes vantagens da modularização: durante a atualização, apenas as telas do módulo em questão ficam temporariamente indisponíveis. O restante do sistema continua funcionando normalmente, e os demais usuários podem seguir com suas atividades sem interrupção.

Se alguém tentar acessar uma tela do módulo que está sendo atualizado nesse período, o sistema exibirá uma mensagem informando que o módulo está em processo de atualização. Nada quebra, é só questão de esperar a conclusão.

Ao concluir o processo, uma mensagem confirmará que o pacote do módulo foi instalado com sucesso. A partir desse momento, todas as telas voltam a ficar disponíveis, já com a nova versão em operação.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/21238784689943-Atualiza%C3%A7%C3%A3o-do-sistema-Sankhya-Om-via-WPM#sumario)

---

## Módulos do Sistema

Para ajudar você a identificar rapidamente o que cada módulo cobre, reunimos abaixo uma descrição dos módulos disponíveis para atualização independente no Sankhya Om. Ao lado do nome de cada um, você encontra a versão a partir da qual o módulo passou a contar com atualização independente.

### Fiscal

O módulo **Livros Fiscais** é responsável pela apuração de impostos e pela geração das obrigações acessórias fiscais. Ele gera automaticamente os livros de Entradas, Saídas, Serviços, Apuração de ICMS/IPI, Produção, Estoque e Inventário, além dos arquivos para SINTEGRA, SPED Fiscal, SPED Contribuições e demais obrigações estaduais e federais.

É também o módulo responsável pela configuração e pelo motor de cálculo dos novos impostos da reforma tributária (IBS, CBS e IS).

Disponível a partir da versão **4.33** do Sankhya Om.

### Contabilidade

O módulo **Contabilidade** centraliza a gestão contábil da empresa, automatizando lançamentos e garantindo conformidade com as normas contábeis. Permite a geração do plano de contas, dos livros contábeis (Diário e Razão), de balancetes, da DRE e dos balanços patrimoniais.

Oferece ainda recursos de bloqueio contábil, que preservam a integridade das informações após os fechamentos mensais, além de integração com as obrigações acessórias.

Disponível a partir da versão **4.33** do Sankhya Om.

### Logística

O módulo **Logística (WMS)** gerencia as operações de armazenagem e a movimentação de materiais, otimizando os processos de estoque e distribuição. Controla o endereçamento de produtos, a separação de pedidos (picking), a expedição, os inventários e a rastreabilidade de lotes, com integração a dispositivos móveis (coletores de dados) para operações em tempo real no armazém.

Permite a gestão de múltiplos depósitos, o controle de validade dos produtos e a otimização do espaço físico, garantindo agilidade e precisão nas operações logísticas da empresa.

Disponível a partir da versão **4.31** do Sankhya Om.

### Pessoal

O **Pessoal+** é o módulo de gestão de Recursos Humanos do Sankhya Om. Ele centraliza e automatiza os processos de RH, desde o recrutamento e seleção até o controle de ponto.

Possui integração nativa com a Pontotel, permitindo a sincronização instantânea de usuários, escalas, férias e ocorrências, além do envio automático de apontamentos e faltas para o fechamento da folha, o que elimina processos manuais.

Disponível a partir da versão **4.24** do Sankhya Om.

### Manufatura

O módulo **Manufatura** controla todo o ciclo produtivo da empresa, do planejamento à execução. Gerencia ordens de produção, estruturas de produtos (BOM), roteiros de fabricação, apontamentos de produção e controle de qualidade.

Permite o cálculo de custos de produção, o controle de perdas e refugos, a gestão de recursos produtivos (máquinas e mão de obra) e a rastreabilidade de lotes, com integração aos módulos de Estoque e Comercial para garantir a disponibilidade de matéria-prima e o atendimento dos pedidos.

Disponível a partir da versão **4.32** do Sankhya Om.

### Imobilizado

O módulo **Imobilizado** controla o ativo fixo da empresa, gerenciando os bens patrimoniais desde a aquisição até a baixa. Calcula a depreciação contábil e fiscal, gera os lançamentos contábeis e atende a obrigações como CIAP e EFD-Contribuições.

Permite ainda o controle de localização física, manutenções, seguros, reavaliações e o inventário de bens, com integração aos módulos de Compras, Financeiro e Contábil para uma gestão completa do patrimônio.

Disponível a partir da versão **4.36** do Sankhya Om.

### ERP Core

O **ERP Core** reúne os cadastros, controles e operações essenciais para o funcionamento da empresa. É composto por nove submódulos, cada um com uma responsabilidade específica dentro do ciclo de gestão. Conheça cada um deles abaixo.

Disponível a partir da versão **4.36** do Sankhya Om.

#### ERP Core · Comercial

Gerencia o ciclo completo de vendas: orçamentos, pedidos, faturamento, devoluções e comissões. Controla tabelas de preços, descontos e metas, com integração automática aos módulos de Estoque, Financeiro e Fiscal.

Oferece ainda análises de performance e ferramentas como o Gerente Online, que permitem o acompanhamento dos resultados em tempo real.

#### ERP Core · Financeiro

Centraliza as contas a pagar e a receber, o fluxo de caixa e as movimentações bancárias, com baixas via intercâmbio ou manuais. Gera movimentos bancários automáticos e disponibiliza ferramentas gerenciais como o Fluxo de Caixa Matricial, o controle de provisões e a análise de ciclo financeiro.

Integra-se a todos os módulos para a consolidação automática das informações financeiras.

#### ERP Core · Inventário

Controla a contagem física dos estoques para ajuste e conferência de saldos, permitindo a realização de inventários totais ou rotativos. Registra divergências e processa ajustes automáticos após a aprovação.

Integra-se ao WMS, ao Contábil e aos Livros Fiscais, oferecendo relatórios de acuracidade que apoiam a melhoria contínua dos processos.

#### ERP Core · Checkout

Solução de ponto de venda para o varejo, com operação integrada ou off-line, que registra vendas, devoluções e movimentações de caixa. Integra-se a TEF, balanças, leitores e impressoras fiscais.

Sincroniza automaticamente os cadastros e as vendas com a retaguarda, atualizando Estoque, Financeiro e Fiscal.

#### ERP Core · Armazém

Voltado para empresas que armazenam produtos de terceiros, controla a entrada, a estocagem e a saída com segregação física e contábil. Gerencia contratos de armazenagem, cobrança por espaço ou volume e rastreabilidade de lotes.

Integra-se ao WMS, ao Financeiro e ao Fiscal para o faturamento dos serviços prestados.

#### ERP Core · Contratos e Serviços

Controla atendimentos, projetos e contratos de serviços por meio de Ordens de Serviço com histórico e apontamentos. Gerencia projetos complexos com controle de horas e produtividade.

Integra-se aos módulos de Compras, Vendas, Estoque e Patrimonial, permitindo o rastreamento completo dos itens locados.

#### ERP Core · Gestão de Indicadores

Permite acompanhar os resultados financeiros, comerciais e operacionais de forma visual e centralizada, apoiando a tomada de decisão estratégica com dados atualizados em tempo real.

#### ERP Core · Cotação

Otimiza o processo de compras por meio de pesquisas junto a fornecedores, comparando preços, prazos e qualidade. Gera análises comparativas automáticas e converte cotações aprovadas em pedidos de compra.

Integra-se ao módulo de Compras para o levantamento de necessidades e ao Financeiro para a provisão de despesas.

#### ERP Core · Base

Responsável pelos cadastros e configurações estruturais do sistema, como produtos, parceiros, centros de resultado, parâmetros gerais e integrações. Serve de base para o funcionamento correto de todos os demais módulos, centralizando as informações compartilhadas entre as diferentes áreas da empresa.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/21238784689943-Atualiza%C3%A7%C3%A3o-do-sistema-Sankhya-Om-via-WPM#sumario)
