---
id: "360044616253"
titulo: "Local address contains control or whitespace"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616253-Local-address-contains-control-or-whitespace"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:54:13Z"
rotulos: ["#criadoRoger", "#RevisadoGui", "535 Incorrect authentication data", "Could not connect to SMTP host", "Error: authentication failed", "MSD_E00017", "Configuração", "Remetente", "SMTP", "535 5.7.8 Error: authentication failed: UGFzc3dvcmQ6", "Envio de Mensagens", "Erro [MSD_E00017]: Corrigindo Espaços em Branco no Remetente", "Erro"]
---

# Local address contains control or whitespace

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16784138298007) MENSAGEM:**

[MSD\_E00017]:  Local address contains control or whitespace.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16784138315799) CAUSA:**

É provocado quando no campo Remetente possui espaços em branco.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16784110473879) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 4: Acesse: Configurações » Avançado » Envio de Mensagens » Contas SMTP:](https://ajuda.sankhya.com.br/hc/article_attachments/16784110485015) Acesse: Configurações » Avançado » Envio de Mensagens » Contas SMTP:

- No campo **"Remetente"**, retire os espaços em branco caso houver no início ou fim da descrição;
- Salve as alterações.

**![Imagem 5: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16784110488599) OBSERVAÇÃO:**

O campo Remetente da rotina Configurações » Avançado » Envio de Mensagens » Servidor SMTP também pode ser ajustado, caso utilize esta rotina para envio de e-mail.
