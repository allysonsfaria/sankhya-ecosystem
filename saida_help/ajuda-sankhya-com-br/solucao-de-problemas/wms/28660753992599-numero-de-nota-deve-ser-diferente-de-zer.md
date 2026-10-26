---
id: "28660753992599"
titulo: "Número de nota deve ser diferente de zero (WMS)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/28660753992599-N%C3%BAmero-de-nota-deve-ser-diferente-de-zero-WMS"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T14:37:42Z"
rotulos: ["Configuração", "WMS", "Nota Fiscal", "TOP", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Número de nota deve ser diferente de zero (WMS)", "Erro"]
---

# Número de nota deve ser diferente de zero (WMS)

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/28660753976727) **MENSAGEM:**

Número de nota deve ser diferente de zero (WMS).

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/28660742701975)SOLUÇÃO:**

Verifique no campo **"TOP diferença a maior (peso variavel)"** e/ou campo **"TOP diferença a menor(peso variavel)"** aba **"WMS"** (Comercial > Preferências > Empresa) , a top que está configurada.

Depois, observe no cadastro desta TOP, na tela **"Tipo de operação TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP)  se o campo **"numeração automática"** está marcado. Caso não esteja, defina como automática para que o próprio sistema crie o número da nota na geração da mesma.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/28660742704791)CAUSA:**

A numeração para a Top de diferença a maior ou menor (Sobra ou perda), obrigatoriamente precisa ser automática, pois, se trata de notas criadas de forma automática pelo sistema.
