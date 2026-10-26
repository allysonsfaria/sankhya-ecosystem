---
id: "39803370510359"
titulo: "Tela Monitoramento de Banco de Dados"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39803370510359-Tela-Monitoramento-de-Banco-de-Dados"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T14:01:19Z"
rotulos: ["Configuração", "Requisições", "Monitoramento", "Preferências", "Sankhya", "br.com.sankhya.mge.MonitoramentoBancoDeDados", "monitoramento de banco de dados", "ENBLMONBD", "Banco de Dados"]
---

# Tela Monitoramento de Banco de Dados

**Módulo:** Configurações > Controle de Acesso

---

## O que é e para que serve

A tela de **Monitoramento de Banco de Dados** permite visualizar, em tempo real, todos os comandos SQL que estão sendo executados pelo servidor de aplicação Sankhya. Ela serve para que administradores de sistema e analistas diagnostiquem lentidões, identifiquem queries com alto volume de execução e rastreiem a origem exata de operações que estão pressionando o servidor. Esta ferramenta atua exclusivamente como um rastreador de requisições da aplicação, e não como um otimizador de consultas (tuning) ou monitorador da infraestrutura física do banco de dados.

![Imagem 1: A tela de Monitoramento de Banco de Dados permite visualizar, em tempo real, todos os comandos SQL que estão sendo…](https://ajuda.sankhya.com.br/hc/article_attachments/39822909961367)

(Resultado do monitoramento com filtros aplicados em 04/2026)

## Antes de começar

O monitoramento é controlado globalmente pelo parâmetro de sistema **ENBLMONBD** (Ativa monitoramento BD), que você pode configurar na tela de [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias).

Para que o sistema popule a grade com os dados, este parâmetro deve estar ativado com o valor (S). Quando estiver desativado (N), o servidor ignorará todos os eventos SQL e nenhum dado será exibido na tela, poupando processamento da aplicação.

## Como usar a tela

Você não precisa acessar o painel de parâmetros toda vez que quiser usar a ferramenta. A tela oferece controles rápidos para gerenciar a captura e a atualização dos dados da sessão:

- **Ativação rápida:** utilize a marcação **Monitorar Banco de Dados** no canto superior direito. Ele altera o parâmetro em tempo real, iniciando ou pausando a captura de comandos sem a necessidade de reiniciar o servidor.

| **Atenção:**   Manter o monitoramento ativado continuamente consome alto nível de processamento do servidor de aplicação e pode impactar o desempenho do ERP para outros usuários. Ative a captura apenas durante a investigação de um problema e desligue-a imediatamente após o diagnóstico. |
| --- |

## Análise de comandos e rastreamento

Com o monitoramento rodando, a grade principal exibe uma linha para cada requisição em andamento. Ali você já consegue identificar o usuário logado na aplicação, o GLOBALID da requisição, a origem da operação (HTTP ou JOB), o tipo do comando (QUERY ou DML) e o nome do executor.

| **Dica:**  Ative a opção **Atualizar automaticamente** (disponível no painel de filtros rápidos) para que a grade recarregue sozinha. Lembre-se de que a tela captura os comandos no exato milissegundo da requisição; sem o auto-refresh, você precisará clicar em recarregar manualmente para ver o que está rodando naquele instante. |
| --- |

### Detalhamento da requisição

Para diagnosticar exatamente o que está causando lentidão ou peso no banco, clique sobre qualquer registro da grade. O sistema abrirá uma visão aprofundada contendo duas informações técnicas críticas:

Ao clicar sobre qualquer registro da grade, o sistema abrirá uma visão aprofundada.

Na aba **Comando**, você visualiza a sintaxe do SQL formatada, incluindo o cabeçalho Runtime-info que identifica a origem exata da operação, indicando a tela, o serviço e a URL que originaram o comando.

![Imagem 2: Na aba Comando , você visualiza a sintaxe do SQL formatada, incluindo o cabeçalho Runtime-info que identifica a origem…](https://ajuda.sankhya.com.br/hc/article_attachments/39822909967639)

Na aba **Stacktrace** será possível visualizar a pilha de chamadas da linguagem Java no momento exato do disparo. Isso facilita o trabalho da equipe de desenvolvimento e suporte na hora de localizar o ponto exato do código que solicitou a operação.

![Imagem 3: Na aba Stacktrace será possível visualizar a pilha de chamadas da linguagem Java no momento exato do disparo. Isso…](https://ajuda.sankhya.com.br/hc/article_attachments/39822894705559)

## Perguntas frequentes

**Deixar o monitoramento ligado afeta o desempenho do sistema?**

Sim. Manter o parâmetro de monitoramento (toggle) ativado continuamente consome recursos de processamento do servidor de aplicação. É uma boa prática de governança ativar o monitoramento apenas durante a investigação de um problema e desligá-lo logo após o diagnóstico.

**Consigo cancelar (derrubar) uma query pesada diretamente por esta tela?**

Não. A tela de Monitoramento de Banco de Dados tem função estritamente consultiva e de rastreamento (exibindo o SQL e o Stacktrace). Para encerrar uma sessão no banco de dados (kill session), você deve utilizar as ferramentas de administração do seu SGBD (como Oracle SQL Developer ou SQL Server Management Studio).

**Por que a tela não está exibindo nenhum comando?**

A tela **não guarda histórico**, ela exibe estritamente o que está em execução no exato instante da sua pesquisa. Como a maioria das requisições ao banco duram apenas milissegundos, elas são concluídas rápido demais para serem capturadas na grade. Você só verá registros se o toggle estiver ativado e houver uma operação mais pesada ou demorada rodando no exato milissegundo em que a tela for atualizada.
