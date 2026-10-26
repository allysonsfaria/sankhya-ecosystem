---
id: "30942995698711"
titulo: "Existe outro processo padrão produzindo o produto Cód.Produto 'X'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30942995698711-Existe-outro-processo-padr%C3%A3o-produzindo-o-produto-C%C3%B3d-Produto-X"
trilha: "Solução de Problemas > Produção"
atualizado_em: "2026-07-22T14:34:15Z"
rotulos: ["Produtos", "Configuração", "Produção", "Composição do Produto", "Passos para resolver", "Razão do erro", "Detalhe do erro", "PROD_E00479", "Só pode haver um processo padrão", "produzindo um determinado produto/controle", "Existe outro processo padrão produzindo", "o produto Cód. Produto 'X'", "Erro"]
---

# Existe outro processo padrão produzindo o produto Cód.Produto 'X'

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/30942995689111) **MENSAGEM:**

[PROD\_E00479] Existe outro processo padrão produzindo o produto Cód. Produto 'X'. Só pode haver um processo padrão produzindo um determinado produto/controle.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30942995689879)SOLUÇÃO:**

Acesse a tela **"Composição do Produto"** (Produção » Cadastros » Composição do Produto), filtre o produto X e valide qual dos processos vinculados ao produto na tela **"Processe Produtivo - Nova"** (Produção » Cadastros » Processo Produtivo - Nova), está com o processo definido como padrão.

Por regra o sistema só permite um processo produtivo padrão por produto definido no sistema.

Caso a necessidade seja esse novo processo produtivo estar definido como padrão para o PA, retire a marcação do processo anterior vinculado ao produto.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/30943012092567)CAUSA:**

Ocorre quando tentamos cadastrar um novo processo produtivo como padrão, porem já temos um ou mais  produto(s) vinculado(s) a esse mesmo processo, cadastrado em outro processo produtivo definido como padrão anteriormente.
