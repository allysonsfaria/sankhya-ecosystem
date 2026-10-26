---
id: "44013100931607"
titulo: "[TMS] - Como configurar para disparar um e-mail de resolução da pendência de Cálculo divergente de Fatura"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013100931607--TMS-Como-configurar-para-disparar-um-e-mail-de-resolu%C3%A7%C3%A3o-da-pend%C3%AAncia-de-C%C3%A1lculo-divergente-de-Fatura"
trilha: "Lincros > TMS > Financeiro - TMS"
atualizado_em: "2026-10-05T19:48:03Z"
rotulos: ["sync_hc", "lincros", "lincros_13432949", "sync_hash_380c961d7115"]
---

# [TMS] - Como configurar para disparar um e-mail de resolução da pendência de Cálculo divergente de Fatura

**Menu**: Financeiro > Faturas

**Objetivo**: Como configurar para disparar um e-mail de resolução da pendência de Cálculo divergente de Fatura

**Considerações**:

- Serve para notificar os usuários que os mesmos tem pendências em seu nome;
- Funciona somente para pendências com responsáveis;

Atualmente existe uma rotina pronta no TMS que pode ser configurada de acordo com a necessidade do cliente, abaixo segue os procedimentos:

1. Acessar o menu: Sistema > Agendamento de Processos;
2. Clicar na opção 'Novo';
3. Cadastrar o job 'com.transpobrasil.job.PendenciaMessageConsumerJob', conforme exemplo abaixo:

![Imagem 1: Cadastrar o job 'com.transpobrasil.job.PendenciaMessageConsumerJob', conforme exemplo abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/44013141026583)

4. Pode ser utilizado o programa a 'CronMaker' -> Link:<http://www.cronmaker.com/;jsessionid=node07gx97p68d8fk1j8fmxw4pkq1k391019.node0?0>, para validar o campo 'Cron';

5. No exemplo do print acima, o agendamento foi parametrizado para executar todos os dias às 17:30h;

![Imagem 2: 5. No exemplo do print acima, o agendamento foi parametrizado para executar todos os dias às 17:30h;](https://ajuda.sankhya.com.br/hc/article_attachments/44013141201559)

**Obs.:** Para habilitar o mesmo em um cliente mais antigo, deve ser passado o login dos usuários da empresa para a Infra limpar a fila SQS dos mesmos, para não notificar as pendências legadas. Basta solicitar ao Help Desk da Lincros através do e-mail: [atendimento@lincros.com](mailto:atendimento@lincros.com)

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
