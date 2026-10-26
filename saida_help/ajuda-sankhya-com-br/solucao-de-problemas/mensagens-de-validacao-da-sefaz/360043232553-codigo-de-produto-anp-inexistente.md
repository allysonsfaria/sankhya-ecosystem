---
id: "360043232553"
titulo: "Código de Produto ANP inexistente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043232553-C%C3%B3digo-de-Produto-ANP-inexistente"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:06:00Z"
rotulos: ["ERRONF", "Produtos", "Configuração", "NF-e", "SEFAZ", "Impostos", "761", "Código ANP inexistente", "Preencher \"Código ANP\" em Produtos", "Parâmetro 'COMBUSTÍVEL' ativado", "Erro"]
---

# Código de Produto ANP inexistente

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16452398359191) **MENSAGEM:**

[761 - Rejeição]: Código de Produto ANP inexistente.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16452383335959) SOLUÇÃO:**

Para correção, siga os passos abaixo.

**(1)** Acesse a tela "**[Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113)"** (Caminho de acesso à tela: Configurações » Cadastros » Produtos), vá até a Aba "**Combustível"** e preencha o campo "**Código ANP"** com um código válido.

![Imagem 3: (1) Acesse a tela " Produtos " (Caminho de acesso à tela: Configurações » Cadastros » Produtos), vá até a Aba "…](https://ajuda.sankhya.com.br/hc/article_attachments/14393526733079)

**![Imagem 4: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/16452398372375) IMPORTANTE:**

A aba combustível só será visualizada se o parâmetro 'COMBUSTÍVEL' estiver ligado:

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16452398375063) CAUSA:**

Na emissão de NF-e para Operações com Combustíveis e for informado código do Produto da ANP (cProdANP) que não existe na tabela do sistema de informações de movimentação de produtos (SIMP), será retornada a rejeição.
