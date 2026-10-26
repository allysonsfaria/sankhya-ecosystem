---
id: "44012174101143"
titulo: "[TMS] - Envio de e-mail para resolução de pendências"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012174101143--TMS-Envio-de-e-mail-para-resolu%C3%A7%C3%A3o-de-pend%C3%AAncias"
trilha: "Lincros > TMS > Sistema - TMS"
atualizado_em: "2026-10-05T19:21:13Z"
rotulos: ["sync_hc", "lincros", "lincros_13434321", "sync_hash_7a61ffe31860"]
---

# [TMS] - Envio de e-mail para resolução de pendências

**Menu**: Sistema > Agendamento de processos

**Objetivo**: Como notificar os usuários que os mesmos possuem pendências em seu nome.

**Considerações**:

- Funciona somente para pendências com responsáveis;
- Para habilitar o mesmo em um cliente mais antigo, deve ser passado o login dos usuários da empresa para a Infra limpar a fila SQS dos mesmos, para não notificar as pendências legadas;

## Atributos

![Imagem 1: Atributos](https://ajuda.sankhya.com.br/hc/article_attachments/44012169184919)

![Imagem 2: Atributos](https://ajuda.sankhya.com.br/hc/article_attachments/44012169312151)

![Imagem 3: Atributos](https://ajuda.sankhya.com.br/hc/article_attachments/44012160785047)

Abaixo os procedimentos de como realizar a configuração:

1. Acessar o menu: Sistema > Agendamento de Processos;
2. Clicar na opção 'Novo';
3. No campo 'Processo', selecionar o job 'PendenciaMessageConsumerJob', a classe o sistema irá preencher automaticamente com 'com.transpobrasil.job.PendenciaMessageConsumerJob';

   ![Imagem 4: No campo 'Processo', selecionar o job 'PendenciaMessageConsumerJob', a classe o sistema irá preencher automaticamente…](https://ajuda.sankhya.com.br/hc/article_attachments/44012139523479)
4. Após, clicar em 'Salvar';

 "Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
