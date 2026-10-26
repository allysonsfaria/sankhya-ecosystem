---
id: "26401921523863"
titulo: "Qtd. apontada acima do desvio permitido (XXXXX maior que XXXXX) para a MP XXX"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26401921523863-Qtd-apontada-acima-do-desvio-permitido-XXXXX-maior-que-XXXXX-para-a-MP-XXX"
trilha: "Solução de Problemas > Produção"
atualizado_em: "2026-07-22T14:42:21Z"
rotulos: ["Produtos", "Configuração", "Desvios de Produção", "Matéria-Prima", "Apontamento", "Produção", "Desvio de quantidade fora do permitido", "Passos para resolver", "Razão do erro", "Detalhe do erro", "[PROD_E00062]", "Desvio"]
---

# Qtd. apontada acima do desvio permitido (XXXXX maior que XXXXX) para a MP XXX

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/26401908419863) **MENSAGEM:**

[PROD\_E00062] Qtd. apontada acima do desvio permitido (XXXXX maior que XXXXX) para a MP XXX.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26401921509399)SOLUÇÃO:**

Na tela **Composição do Produto** (Produção > Cadastros > Composição do Produto), aba **"Matérias-Primas"**, verifique a matéria prima que apresenta na mensagem.

A seguir, verifique a marcação **"Solicitar Liberação ao Exceder Desvio"**, se essa marcação estiver desmarcada, e o produto tiver configuração de desvio nos campos **"% desvio superior" e "% desvio inferior"** (mesmo sendo 0), o sistema valida que não pode ter nenhum desvio para a Matéria Prima. Essa configuração também vale para o Desvio de PA.

Para prosseguir, ligue a marcação citada anteriormente e realize novamente o apontamento. Com isso, será apresentado o pop-up para definir o liberador e prosseguir com a liberação.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/26401921511191)CAUSA:**

Ocorre ao tentar confirmar um apontamento em que a composição do produto possui desvio configurado e não foi realizada a marcação Solicitar Liberação ao Exceder Desvio.
