---
id: "26924758196375"
titulo: "LINE 25 - Nao é possível inserir NULL em (\"TFXADE\".\"ID\") ORA-06512: em \"TRG_FX_TFXPRC\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26924758196375-LINE-25-Nao-%C3%A9-poss%C3%ADvel-inserir-NULL-em-TFXADE-ID-ORA-06512-em-TRG-FX-TFXPRC"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:40:33Z"
rotulos: ["Produtos", "Atualização", "ORA-06512", "ORA-04088", "ORA-01400", "Passos para resolver", "Razão do erro", "Detalhe do erro", "nao é possível inserir NULL em (\"TFXADE\".\"ID\")", "erro durante a execução do gatilho ‘TRG_FX_TFXPRC'", "Erro"]
---

# LINE 25 - Nao é possível inserir NULL em ("TFXADE"."ID") ORA-06512: em "TRG_FX_TFXPRC"

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/26924758145687) **MENSAGEM:**

Ao realizar alguma alteração no cadastro de produtos, é apresentada a mensagem abaixo.

**ORA-01400: nao é possível inserir NULL em ("TFXADE"."ID") ORA-06512: em "TRG\_FX\_TFXPRC", line 25 ORA-04088: erro durante a execução do gatilho ‘TRG\_FX\_TFXPRC'**

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26924758152983)SOLUÇÃO:**

![Imagem 3: O erro ocorre quando a Trigger 'TRG_FX_TFXADE' não existe no banco de dados.](https://ajuda.sankhya.com.br/hc/article_attachments/26924758157207) O erro ocorre quando a Trigger 'TRG\_FX\_TFXADE' não existe no banco de dados.

**(1)** Para recriar esse objeto, faça a atualização do sistema para que os Scripts do banco sejam executados novamente. Ou, entre em contato com o Service Desk da Sankhya para obter o Script a ser executado, visto que pode sofrer alterações conforme novos releases do sistema.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/26924758165911)CAUSA:**

Ocorre quando uma Trigger nativa do sistema não existe na base de dados.
