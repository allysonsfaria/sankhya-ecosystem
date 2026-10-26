---
id: "34184825143063"
titulo: "Erro em Reclassificação de produtos para Movimentações Próprias"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34184825143063-Erro-em-Reclassifica%C3%A7%C3%A3o-de-produtos-para-Movimenta%C3%A7%C3%B5es-Pr%C3%B3prias"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:27:25Z"
rotulos: ["Produtos", "Configuração", "TOP", "Estoque", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Erro", "Erro em Reclassificação", "de produtos para Movimentações Próprias", "de Saída de estoque não", "foi configurado", "Verifique o cadastro da empresa", "O modelo para o ajuste", "Artigo atualizado KCS", "WMS - KCS"]
---

# Erro em Reclassificação de produtos para Movimentações Próprias

**MENSAGEM:**

"O modelo para o ajuste de Saída de estoque não foi configurado.
Verifique o cadastro da empresa."

![Imagem 1: "O modelo para o ajuste de Saída de estoque não foi configurado. Verifique o cadastro da empresa."](https://ajuda.sankhya.com.br/hc/article_attachments/35010264046359)

**SITUAÇÃO:**

Ao realizar a cópia de estoque, quando há produtos com movimentações de terceiros e a Top utilizada é para movimentações próprias, com o campo **"Atualização de Estoque"** diferente de **"Nenhum"** na aba **"Estoque"**, o sistema apresenta esta mensagem de erro.

Para validar as movimentações dos produtos, consulte a tabela **TGFCTE** filtrando pelo código do produto. No campo **CODPARC**:

- **0** → movimentações próprias
- **diferente de 0** → movimentações de terceiros

`SELECT *`
`FROM TGFCTE`
`WHERE CODPROD = (Código do Produto);`

![Imagem 2: SELECT * FROM TGFCTE WHERE CODPROD = (Código do Produto);](https://ajuda.sankhya.com.br/hc/article_attachments/35010264049175)

**SOLUÇÃO:**

**(1)**  Acesse a tela **"Cópia de Estoque"** (Inventário > Arquivo >Cópia de Estoque); 

**(2)**  Crie um filtro utilizando **CODPARC = 0** para considerar apenas movimentações próprias; 

**(3)**  Execute a cópia de estoque novamente. A validação é feita pela primeira linha retornada na consulta (última contagem); 

**(4)**  Se a cópia já foi refeita com **CODPARC = 0**, não é necessário refazê-la, a menos que o erro volte a ocorrer.

**Ajuda oficial:** [**AQUI**](https://ajuda.sankhya.com.br/hc/pt-br/articles/6024489775895-Reclassifica%C3%A7%C3%A3o-do-Produto)
**Movimentação com terceiros:** [**AQUI**](https://ajuda.sankhya.com.br/hc/pt-br/articles/10117649858583-O-modelo-para-o-ajuste-de-Sa%C3%ADda-de-estoque-COM-TERCEIROS-n%C3%A3o-foi-configurado-Verifique-o-cadastro-da-empresa)

**CAUSA:**

O erro ocorre porque, ao tentar copiar o estoque de produtos com movimentações de terceiros utilizando uma Top configurada para movimentações próprias, o sistema não encontra o modelo de ajuste adequado, devido ao campo **"Atualização de Estoque"** estar diferente de **"Nenhum"** na aba **"Estoque"**.
