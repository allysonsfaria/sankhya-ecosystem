---
id: "20026120604567"
titulo: "ORA-20101: Código Barra REPETIDO na unidade alternativa para o produto XXXX ORA-06512: em \"SANKHYA.TRG_INC_UPT_TGFVOA_CODBARRA\", line XX ORA-04088: erro durante a execução do gatilho 'SANKHYA.TRG_INC_UPT_TGFVOA_CODBARRA'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/20026120604567-ORA-20101-C%C3%B3digo-Barra-REPETIDO-na-unidade-alternativa-para-o-produto-XXXX-ORA-06512-em-SANKHYA-TRG-INC-UPT-TGFVOA-CODBARRA-line-XX-ORA-04088-erro-durante-a-execu%C3%A7%C3%A3o-do-gatilho-SANKHYA-TRG-INC-UPT-TGFVOA-CODBARRA"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T14:51:19Z"
rotulos: ["Produtos", "Configuração", "ORA-20101", "ORA-06512", "Código de barras duplicado", "Unidade alternativa com código repetido", "Desmarcar 'Unidades Alternativas' ao duplicar", "Erro"]
---

# ORA-20101: Código Barra REPETIDO na unidade alternativa para o produto XXXX ORA-06512: em "SANKHYA.TRG_INC_UPT_TGFVOA_CODBARRA", line XX ORA-04088: erro durante a execução do gatilho 'SANKHYA.TRG_INC_UPT_TGFVOA_CODBARRA'

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/20026115007511) **MENSAGEM:**

ORA-20101: Código Barra REPETIDO na unidade alternativa para o produto XXXX
ORA-06512: em "SANKHYA.TRG\_INC\_UPT\_TGFVOA\_CODBARRA", line XX
ORA-04088: erro durante a execução do gatilho 'SANKHYA.TRG\_INC\_UPT\_TGFVOA\_CODBARRA'.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/20026120603287)CAUSA:**

Quando o produto que deseja duplicar, trabalha com unidade alternativa, já existe o código de barras da unidade alternativa na tabela TGFVOA (Volume alternativa) e não há como alterá-lo antes de salvar a cópia do novo produto.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/20026120602391)SOLUÇÃO:**

Clique no botão duplicar na rotina Cadastro de **Produtos** (Configurações » Cadastros » Produtos) será aberto o pop-up 'Copiar Também' desmarque a opção 'Unidades Alternativas' e salve.

![Imagem 4: Clique no botão duplicar na rotina Cadastro de Produtos (Configurações » Cadastros » Produtos) será aberto o pop-up…](https://ajuda.sankhya.com.br/hc/article_attachments/20054229290007)
