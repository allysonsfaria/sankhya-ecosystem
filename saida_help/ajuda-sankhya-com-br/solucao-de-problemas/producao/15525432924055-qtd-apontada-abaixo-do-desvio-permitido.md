---
id: "15525432924055"
titulo: "Qtd. apontada abaixo do desvio permitido (XXXXX menor que XXXXX) para a MP 177 "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/15525432924055-Qtd-apontada-abaixo-do-desvio-permitido-XXXXX-menor-que-XXXXX-para-a-MP-177"
trilha: "Solução de Problemas > Produção"
atualizado_em: "2026-07-22T14:56:38Z"
rotulos: ["Produtos", "Configuração", "Estoque", "PROD_E00062", "Desvio de quantidade fora do permitido", "Ajuste campos de desvio na tela \"Composição do Produto\"", "Apontamento com desvio na composição do produto", "Erro", "MP 177"]
---

# Qtd. apontada abaixo do desvio permitido (XXXXX menor que XXXXX) para a MP 177 

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16536649825943) MENSAGEM:**

[PROD\_E00062] Qtd. apontada abaixo do desvio permitido (XXXXX menor que XXXXX) para a MP 177.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16536611125399) SOLUÇÃO:**

Na tela **"Composição do Produto",** aba **"Matérias-Primas"**, verifique a matéria prima que apresenta na mensagem. A seguir  verifique os campos "**% desvio superior"** e "**% desvio inferior"**, se o produto não trabalhar com o desvio deixe os campos em branco.

![Imagem 3: Na tela "Composição do Produto", aba "Matérias-Primas" , verifique a matéria prima que apresenta na mensagem. A seguir…](https://ajuda.sankhya.com.br/hc/article_attachments/16444010485783) **OBSERVAÇÃO:**

Se o campo estiver como 0 ele considera que o produto não pode ter desvio e será apresentanda a mensagem sempre que houver qualquer desvio no apontamento da matéria prima.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16536649840663) CAUSA:**

Ocorre ao tentar confirmar um apontamento em que a composição do produto possui desvio configurado.
