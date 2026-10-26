---
id: "360046681853"
titulo: "SubmissionQuotaExceededException"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360046681853-SubmissionQuotaExceededException"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T15:32:37Z"
rotulos: ["Configuração", "Limite de envio de e-mails excedido", "Contatar o provedor de e-mail; ajustar configurações SMTP", "Bloqueio por ultrapassar a cota de envio", "Detalhe do erro", "Contas SMTP", "Servidor SMTP", "Erro"]
---

# SubmissionQuotaExceededException

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16311402408343) MENSAGEM:**

554 5.2.0 STOREDRV.Submission.Exception:SubmissionQuotaExceededException; Failed to process message due to a permanet exception with message The message can't be submitted because the sender's submission quota was exceeded.
SubmissionQuotaExceededException: The message can't be submitted because the sender's submission quota was exceeded.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16311386267031) SOLUÇÃO:**

![Imagem 3: Essa mensagem será apresentada quando o provedor do e-mail utilizado não permitir o envio do e-mail, normalmente…](https://ajuda.sankhya.com.br/hc/article_attachments/16311386269975) Essa mensagem será apresentada quando o provedor do e-mail utilizado não permitir o envio do e-mail, normalmente justificando o limite de cota de envio ultrapassado.

![Imagem 4: Nesse caso, contate o seu provedor de e-mail para alinhamento/solução ou a criação de uma nova conta de e-mail para…](https://ajuda.sankhya.com.br/hc/article_attachments/16311402418711) Nesse caso, contate o seu provedor de e-mail para alinhamento/solução ou a criação de uma nova conta de e-mail para utilização. Realizando os devidos ajustes nas respectivas rotinas **"Servidor SMTP"** e/ou **"Contas SMTP"**.

Para mais detalhes:

- **[Contas SMTP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603194)**
- **[Servidor SMTP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593494)**

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16311402419863) CAUSA:**

Mensagem retornada quando o provedor de e-mail bloqueia o envio, normalmente justificando que o limite de cotas de envio foi atingido.
