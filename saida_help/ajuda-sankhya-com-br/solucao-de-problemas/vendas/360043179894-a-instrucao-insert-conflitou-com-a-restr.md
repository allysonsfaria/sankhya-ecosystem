---
id: "360043179894"
titulo: "A instrução INSERT conflitou com a restrição do FOREIGN KEY \"FK_TGFCAB_CODNAT_TGFNAT\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043179894-A-instru%C3%A7%C3%A3o-INSERT-conflitou-com-a-restri%C3%A7%C3%A3o-do-FOREIGN-KEY-FK-TGFCAB-CODNAT-TGFNAT"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:02:31Z"
rotulos: ["Configuração", "Preferências", "Financeiro", "Natureza", "Conflito ao inserir registro", "Natureza padrão inadequada", "Ajustar parâmetro NATPADDEV", "Erro"]
---

# A instrução INSERT conflitou com a restrição do FOREIGN KEY "FK_TGFCAB_CODNAT_TGFNAT"

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16161210380311) MENSAGEM:**

A instrução INSERT conflitou com a restrição do FOREIGN KEY "FK\_TGFCAB\_CODNAT\_TGFNAT". O conflito ocorreu no banco de dados "NOMEDOBANCO", tabela "sankhya.TGFNAT", column 'CODNAT'.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16161196086039) SITUAÇÃO:**

Ao tentar efetuar qualquer devolução de vendas, ocorre a mensagem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16161196086679) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 4: Acesse: Configurações » Avançado » Preferências](https://ajuda.sankhya.com.br/hc/article_attachments/16161210382231) Acesse:  Configurações » Avançado » Preferências

- Parâmetro:  **"NATPADDEV-Natureza padrão p/Devolução de Vendas"**
- Identifique o valor no campo INTEIRO.

![Imagem 5: Identifique o valor no campo INTEIRO.](https://ajuda.sankhya.com.br/hc/article_attachments/14706416983959)

![Imagem 6: Acesse: Configurações » Cadastros » Gerencial » Natureza de Receitas e Despesas](https://ajuda.sankhya.com.br/hc/article_attachments/16161210382615) Acesse: Configurações » Cadastros » Gerencial » Natureza de Receitas e Despesas

- Pesquise pelo código e, caso não encontre, escolha outro código de natureza que esteja ativo e informe no parâmetro ou limpe o valor informado no parâmetro.

![Imagem 7: Execute a devolução novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16161196093847) Execute a devolução novamente.

**![Imagem 8: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16161196094615) OBSERVAÇÃO:**

Parâmetro: "**NATPADDEV-Natureza padrão p/Devolução de Vendas".**

Descrição: Ao efetuar uma devolução, se o Tipo de Negociação não conter uma natureza informada ou estiver diferente do parâmetro no ato da devolução, irá assumir a natureza informada no parâmetro.

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16161196095767) CAUSA:**

Ocorre quando não está definido adequadamente o valor inserido no parâmetro "**NATPADDEV-Natureza padrão p/Devolução de Vendas".** Em determinados processos a Devolução requer uma natureza diferente da venda, então neste caso é usado o parâmetro.
