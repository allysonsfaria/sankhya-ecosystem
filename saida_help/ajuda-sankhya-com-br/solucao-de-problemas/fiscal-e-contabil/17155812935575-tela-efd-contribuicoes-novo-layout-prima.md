---
id: "17155812935575"
titulo: "Tela EFD Contribuições (novo layout): PRIMARY KEY 'PK_XXX'. Não é possível inserir a chave duplicada no objeto 'SANKHYA.XXX'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/17155812935575-Tela-EFD-Contribui%C3%A7%C3%B5es-novo-layout-PRIMARY-KEY-PK-XXX-N%C3%A3o-%C3%A9-poss%C3%ADvel-inserir-a-chave-duplicada-no-objeto-SANKHYA-XXX"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:53:44Z"
rotulos: ["Configuração", "Fiscal", "SEFAZ", "Impostos", "EFD Contribuições", "Erro: Chave duplicada na tela EFD Contribuições.", "Causa: Duplicidade ao cadastrar uma referência já existente.", "Solução: Verifique linhas cadastradas antes de inserir novas.", "Erro"]
---

# Tela EFD Contribuições (novo layout): PRIMARY KEY 'PK_XXX'. Não é possível inserir a chave duplicada no objeto 'SANKHYA.XXX'

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/17155844491415) **MENSAGEM:**

 Violação da restrição PRIMARY KEY 'PK\_TGFEFDC0500'. Não é possível inserir a chave duplicada no objeto 'SANKHYA.TGFEFDC0500'. O valor de chave duplicada é (1, Nov 1 2022 12:00AM, 0001, , 1).

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17155768663319)CAUSA:**

Ocorre na duplicidade ao utilizar a opção "Cadastrar EFD contribuições [F8]".

Essa duplicidade pode ocorrer quando o usuário está tentando cadastrar uma referência que já estava presente.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17155829663127)SOLUÇÃO:**

Ao cadastrar EFD contribuições [F8] observe as linhas cadastradas.

**Exemplo:**

Referência criada em 01/08/2023.

![Imagem 4: Referência criada em 01/08/2023.](https://ajuda.sankhya.com.br/hc/article_attachments/17155637729815)

Caso o usuário crie uma nova linha com uma referência já existente.

![Imagem 5: Caso o usuário crie uma nova linha com uma referência já existente.](https://ajuda.sankhya.com.br/hc/article_attachments/17173897284119)

A restrição de PK é exibida.
