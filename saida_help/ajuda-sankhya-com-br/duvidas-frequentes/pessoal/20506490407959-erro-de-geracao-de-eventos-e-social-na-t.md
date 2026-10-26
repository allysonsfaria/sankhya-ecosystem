---
id: "20506490407959"
titulo: "Erro de geração de eventos  e-Social na TFPS1210_INFODEP"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/20506490407959-Erro-de-gera%C3%A7%C3%A3o-de-eventos-e-Social-na-TFPS1210-INFODEP"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-07-29T13:25:47Z"
rotulos: ["Eventos", "Fiscal", "eSocial", "Configuração Funcionários", "Campo CPF de dependentes não preenchido", "Inserir CPF dos dependentes", "Requisito do e-Social 1.2", "Erro"]
---

# Erro de geração de eventos  e-Social na TFPS1210_INFODEP

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/20506456943383) **MENSAGEM:**

Caused by: java.sql.SQLIntegrityConstraintViolationException: ORA-01400: não possível inserir NULL em ("SANKHYA"."TFPS1210\_INFODEP"."CHAVE").

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/20506456947991)CAUSA:**

Com a atualização do leiaute 1.2 do e-Social as informações dos dependentes são obrigatórios.
Esse erro de geração de eventos na TFPS1210\_INFODEP ocorre quando há dependentes com o campo de CPF não preenchido, ou seja, é necessário incluir o CPF do dependente corretamente para que o envio dos eventos ocorram sem apresentar erro.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/20506490396311)SOLUÇÃO:**

É **obrigatório** preencher o campo de CPF de todos os dependentes existentes no cadastro do funcionário.
