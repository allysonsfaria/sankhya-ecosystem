---
id: "360051439534"
titulo: "Como analisar os problemas de performance (Lentidão) que ocorrem no sistema"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360051439534-Como-analisar-os-problemas-de-performance-Lentid%C3%A3o-que-ocorrem-no-sistema"
trilha: "Melhores Práticas > Configurações Sankhya"
atualizado_em: "2026-07-22T15:30:00Z"
rotulos: ["Configuração", "Log", "Performance", "Diagnóstico de Lentidão do Sistema", "Sistema", "Banco de Dados", "Diagnóstico"]
---

# Como analisar os problemas de performance (Lentidão) que ocorrem no sistema

Abaixo segue uma lista com as **informações essenciais para abertura de um atendimento relacionado a lentidão.**

Caro cliente e/ou consultor, caso esteja passando por esse cenário, recomendamos que realize a abertura de um chamado através dessa 'Central de Ajuda' [Clique [aqui](https://ajuda.sankhya.com.br/hc/pt-br) e selecione a opção "ENTRAR" >> Abrir Chamado], e no campo **"Descrição" inserir as respostas de todas as perguntas abaixo.**

Esse procedimento adiantará sua análise, fornecendo as informações principais para um possível diagnóstico da causa.

| 1. Quando começou a ocorrer a lentidão?  2. Existe um horário específico, ou ocorre a todo momento?  3. Em quais rotinas do sistema ocorre?  4. Foi feito algum tipo de atualização recente?  5. Acontece com todos os usuários?  6. Acontece em todas as máquinas?  7. Acontece em todos os navegadores?  8. Foram feitas mudanças na estrutura do banco de dados/servidor?  9. Existe integração com outro sistema, extensões ou objetos personalizados que participam do processo?  10. Acontece em bases de produção e de testes?  11. Há algum agendamento sendo executado (análise de giro, consolidação, e-mails...)?  12. Foi realizado algum ajuste de configuração ou parâmetro para esta rotina recentemente?  13. É necessário anexar Log;  13 - A base é local ou é em DataCenter?    **Como gerar o log?**  Anexar o log extraído pela tela de Administração do Servidor e o log do monitor de consultas (Caso se tratar de lentidão em uma rotina/ação específica). |
| --- |

Para profissionais de T.I e/ou usuários com conhecimentos avançados nessa área, listamos análises mais aprofundadas para colaborar com esse diagnóstico:

| - Verificar os agendamentos de Backup, monitorando nesse período como está o desempenho do sistema; - Observar através do 'Gerenciador de Tarefas' o monitor de recursos ou no 'Painel de controles' o Monitor de Recursos para analisar os processos, aplicações e recursos utilizados neste momento de lentidão; - Verificar no servidor se outros programas e recursos que estão em funcionamento; - Verificar se existem outros sistemas em operação no mesmo servidor; - Verifique com os usuários do sistema e analise com eles as rotinas usadas neste horário de lentidão; - Verificar com o TI da empresa questões como conectividade entre as máquinas, hardware, infraestrutura de rede, firewall, antivírus e outros que possa bloquear e/ou causar lentidão no processamento de dados do sistema. - Através de um DBA, se existe alguma procedure agendada que possa estar sendo executada.   Lentidão DB: Comando para verificar se houve atualização de estatísticas das Tabelas do DB nos ultimos 7 dias:  - **ORACLE:**  SELECT TABLE\_NAME, LAST\_ANALYZED FROM USER\_TABLES WHERE LAST\_ANALYZED IS NULL OR LAST\_ANALYZED < TRUNC(SYSDATE -7) ORDER BY LAST\_ANALYZED ASC   - **SQL:**   SELECT name AS Estatística, STATS\_DATE(object\_id, stats\_id) AS Data FROM sys.stats Where STATS\_DATE(object\_id, stats\_id) >= Dateadd(M,-7, GetDate()) Order by Data Asc  Se estiverem desatualizadas, este é um ponto inicial de uma provável lentidão.  No caso, solicitar intervenção de um DBA para que venha atualizá-las. Caso não resolva, este próprio terá condições de avaliar questões de hardware, infra, índices, etc. |
| --- |
