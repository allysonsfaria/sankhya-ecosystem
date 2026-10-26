---
id: "26514467862935"
titulo: "Produto não está apresentando as vendas na análise de giro, mesmo fazendo a consolidação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26514467862935-Produto-n%C3%A3o-est%C3%A1-apresentando-as-vendas-na-an%C3%A1lise-de-giro-mesmo-fazendo-a-consolida%C3%A7%C3%A3o"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-22T14:41:42Z"
rotulos: ["Produtos", "Configuração", "Análise de Giro", "Estoque", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Produto não está apresentando as vendas na análise de giro", "Regra de validação"]
---

# Produto não está apresentando as vendas na análise de giro, mesmo fazendo a consolidação

![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26559510790167) **SITUAÇÃO:**

Produto não está apresentando as vendas na análise de giro, conforme imagem abaixo:

![Imagem 2: Produto não está apresentando as vendas na análise de giro, conforme imagem abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/26514484040983)

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26514484046231)SOLUÇÃO:**

O sistema usa diversas regras de validação para executar a análise. Assim, é preciso que todas essas regras sejam obedecidas para que o produto seja apresentado na análise.

Nesse caso, para solução do problema, verifique se todas as regras abaixo estão sendo cumpridas. Caso alguma delas não esteja, faça a devida correção:

**(1)**  Notas devem estar confirmadas; 
**(1)** Notas devem ter um valor maior que zero. Notas de complemento, por exemplo, não são consideradas; 
**(1)** TOP utilizada na nota deve ter configuração de alimentação de giro; 
**(1)** Valor dos itens da nota devem ser maior que zero; 
**(1)** Quantidade negociada do item deve ser maior que zero;
**(1)** Na tela **"Cadastro do produto",** aba**"Medidas e estoque",**sub aba**"Estoque",** o campo **"Calcular giro pelo agendador"** deve estar marcado; 
**(1)** A venda deve estar dentro do período filtrado na análise de giro;

**(1)** O produto deve ter custo.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/26514484051991)CAUSA:**

Problema ocorre quando alguma regra acima não é encontrada.
