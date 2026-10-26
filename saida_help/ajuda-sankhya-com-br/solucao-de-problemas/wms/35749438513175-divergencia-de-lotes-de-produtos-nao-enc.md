---
id: "35749438513175"
titulo: "Divergência de lotes de produtos não encontrados (Portal de Importação de XML)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35749438513175-Diverg%C3%AAncia-de-lotes-de-produtos-n%C3%A3o-encontrados-Portal-de-Importa%C3%A7%C3%A3o-de-XML"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-10-16T23:21:20Z"
rotulos: ["Produtos", "Configuração", "XML", "Importação", "TOP", "Estoque", "Tipos de Operação - TOP", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Portal de Importação de XML", "Divergência de lotes de produtos", "Atualizar Estoque a partir da Confirmação", "Squad WMS"]
---

# Divergência de lotes de produtos não encontrados (Portal de Importação de XML)

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/35749426259479) **MENSAGEM:**

Divergência de lotes de produtos não encontrados (Portal de Importação de XML)

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/35749426260375)SOLUÇÃO:**

**(1)** Acesse a tela [**''Tipo de Operação - TOP''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP).

**(2)** Na aba **''Estoque''** maque o campo **''Atualizar Estoq.a partir da Confirmação''**.

![Imagem 3: (2) Na aba ''Estoque'' maque o campo ''Atualizar Estoq.a partir da Confirmação'' .](https://ajuda.sankhya.com.br/hc/article_attachments/36625519418391)

**(3)** Após realizar a configuração, exclua o documento gerado na Central.

**(4)** Feche as telas, acesse o sistema e execute um novo processamento no [**''Portal de Importação da XML''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML).

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/35749426260631)CAUSA:**

O erro ocorre no ''Portal de Importação de XML'', quando o campo “Atualizar Estoq. a partir da Confirmação” não está marcado na TOP utilizada para a importação.

Nessa condição, o sistema atualiza o estoque **imediatamente ao gravar cada item da nota**. Como o controle não foi informado nesse momento, o processo fica inconsistente e a mensagem é exibida.
