---
id: "42429281327511"
titulo: "Explorador de registros"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42429281327511-Explorador-de-registros"
trilha: "NEPPO: Personalização de atendimento > Omnichannel"
atualizado_em: "2026-08-11T15:43:24Z"
rotulos: ["sync_hc", "neppo", "neppo_50298895", "sync_hash_eb4167a37355"]
---

# Explorador de registros

O módulo de Explorador de Registros permite a visualização detalhada dos eventos ocorridos dentro do sistema, oferecendo uma interface gráfica e opções de pesquisa para facilitar a análise e monitoramento dos logs gerados por diferentes componentes do sistema.

Para acessar o módulo de explorador de registros, siga as etapas:

**Buscar Menu > Explorador de registros**

![Imagem 1: Buscar Menu > Explorador de registros](https://ajuda.sankhya.com.br/hc/article_attachments/42637072394647)

## Objetivo de negócio

O objetivo de negócio do módulo de Explorador de Registros é fornecer uma ferramenta essencial para que as empresas monitorem, analisem e auditem eventos e atividades em seus ambientes Neppo de forma eficiente e em tempo real. Ao permitir a visualização detalhada e filtrada dos logs, o módulo ajuda a identificar e resolver rapidamente problemas, garantindo a continuidade das operações e a conformidade com políticas de governança e segurança. Além disso, ele oferece insights valiosos que suportam a melhoria contínua dos processos, mitigação de riscos e a tomada de decisões estratégicas, contribuindo diretamente para o crescimento e a eficiência operacional da organização.

## Funcionalidades principais

1. **Filtro de datas e componentes**

   - É possível filtrar os registros de eventos por data e componente específico. A interface permite a seleção de um intervalo de datas e a escolha do componente desejado, facilitando a análise de eventos específicos.
   - ![Imagem 2: É possível filtrar os registros de eventos por data e componente específico. A interface permite a seleção de um…](https://ajuda.sankhya.com.br/hc/article_attachments/42637016444055)
2. **Visualização de gráfico**

   - Um gráfico de barras é exibido na parte superior, mostrando o volume de eventos por dia. Este gráfico pode ser ocultado clicando na opção “Ocultar gráfico”, caso o usuário prefira focar apenas nos detalhes textuais dos registros.
3. **Listagem de eventos**

   - Abaixo do gráfico, há uma listagem detalhada dos eventos. Cada evento é listado com as seguintes colunas:

     - **Data & tempo**: Indica a data e a hora exata do evento.
     - **Tipo do evento**: Descreve o tipo de atividade registrada (ex.: Atividade do agente, Mensagem).
     - **Status**: Exibe o status associado ao evento (ex.: Normal).
     - **Descrição**: Uma breve descrição do evento (ex.: O agente ficou online, Mensagem enviada).
     - **Ação**: Possui opções para visualizar mais detalhes do registro e para fazer download do log específico.
4. **Detalhes do registro**

   - Ao clicar no ícone de visualização na coluna "Ação", uma janela lateral é aberta com detalhes mais profundos do evento selecionado. Esta janela é dividida em duas abas:

     - **Detalhes**: Exibe informações como o componente envolvido, nível de log, timestamp, tenant, código de erro, entre outros.

       - ![Imagem 3: Detalhes : Exibe informações como o componente envolvido, nível de log, timestamp, tenant, código de erro, entre outros.](https://ajuda.sankhya.com.br/hc/article_attachments/42637011339031)
     - **JSON RAW**: Apresenta o log completo em formato JSON, incluindo detalhes técnicos como ID do agente, número máximo de canais de chat ativos, status do agente, entre outros metadados relevantes.

       - ![Imagem 4: JSON RAW : Apresenta o log completo em formato JSON, incluindo detalhes técnicos como ID do agente, número máximo de…](https://ajuda.sankhya.com.br/hc/article_attachments/42637026342679)

## Fluxo de utilização

1. **Seleção de filtros**: O usuário inicia selecionando as datas e, opcionalmente, um componente específico no menu suspenso.
2. **Visualização e interpretação do gráfico**: Com base no filtro aplicado, o gráfico de barras é atualizado para refletir o número de eventos em cada dia. O usuário pode optar por ocultar o gráfico se desejar.
3. **Análise de registros**: A listagem detalhada dos eventos fornece uma visão geral dos logs. O usuário pode navegar pelos eventos e clicar no ícone de olho para ver detalhes específicos de um registro.
4. **Exame de detalhes avançados**: Ao acessar os detalhes do registro, o usuário pode revisar as informações específicas e até mesmo visualizar o log completo em formato JSON, permitindo uma análise técnica mais profunda.
5. **Exportação e documentação**: Caso necessário, o usuário pode fazer o download do log em formato JSON para análises adicionais ou documentação externa.

## Possíveis aplicações

- **Monitoramento de sistema**: Permite aos administradores e desenvolvedores monitorar o estado e o comportamento dos agentes e mensagens no sistema em tempo real.
- **Auditoria**: Fornece uma trilha de auditoria detalhada, útil para revisões de segurança e conformidade.
- **Análise de incidentes**: Facilita a investigação de problemas ao fornecer acesso rápido a logs e detalhes completos dos eventos.
