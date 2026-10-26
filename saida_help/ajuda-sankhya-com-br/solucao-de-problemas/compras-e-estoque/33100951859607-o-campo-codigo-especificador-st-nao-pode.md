---
id: "33100951859607"
titulo: "O campo 'Código Especificador ST' não pode possuir mais que 7 dígitos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33100951859607-O-campo-C%C3%B3digo-Especificador-ST-n%C3%A3o-pode-possuir-mais-que-7-d%C3%ADgitos"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T14:29:42Z"
rotulos: ["Produtos", "Configuração", "NF-e", "XML", "Impostos", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Erro"]
---

# O campo 'Código Especificador ST' não pode possuir mais que 7 dígitos

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/33100951839383) **MENSAGEM:**

[CORE\_E03869] Ao importar um XML no portal de importação de XML apresenta o erro 'O campo 'Código Especificador ST' não pode possuir mais que 7 dígitos.

**SITUAÇÃO:**

Esse comportamento ocorre quando o sistema está configurado para "Exigir Liberação e Alterar o Cadastro" na tela Importação de XML Comercial > Rotinas > Outras Opções > Configuração de Liberação de Divergência.

**CAUSA:**
O campo CEST no XML contém mais de 7 dígitos, e o sistema tenta inserir essa informação no cadastro do produto.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/33100964371863)SOLUÇÃO:**

Nessa situação, o XML será importado normalmente, porém o código CEST não será atualizado no cadastro do produto.

![Imagem 3: Nessa situação, o XML será importado normalmente, porém o código CEST não será atualizado no cadastro do produto.](https://ajuda.sankhya.com.br/hc/article_attachments/33100951846935)![Imagem 4: Nessa situação, o XML será importado normalmente, porém o código CEST não será atualizado no cadastro do produto.](https://ajuda.sankhya.com.br/hc/article_attachments/33100951846423)
