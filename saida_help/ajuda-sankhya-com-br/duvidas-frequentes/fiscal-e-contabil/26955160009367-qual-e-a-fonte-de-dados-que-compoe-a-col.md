---
id: "26955160009367"
titulo: "Qual é a fonte de dados que compõe a coluna 'Vlr ICMS+ST Inicial' no R1050 da tela de Geração do Arquivo Cat42?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26955160009367-Qual-%C3%A9-a-fonte-de-dados-que-comp%C3%B5e-a-coluna-Vlr-ICMS-ST-Inicial-no-R1050-da-tela-de-Gera%C3%A7%C3%A3o-do-Arquivo-Cat42"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:40:27Z"
rotulos: ["Relatórios", "Fiscal", "NF-e", "ICMS", "Estoque", "Passos para resolver", "Razão do erro", "Detalhe do erro"]
---

# Qual é a fonte de dados que compõe a coluna 'Vlr ICMS+ST Inicial' no R1050 da tela de Geração do Arquivo Cat42?

![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/29451601145239) **SITUAÇÃO:**

Qual é a fonte de dados que compõe a coluna 'Vlr ICMS+ST Inicial' no R1050 da tela de Geração do Arquivo Cat42?

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26955159989655)SOLUÇÃO:**

Segue abaixo como cada campo R1050 é alimentado:

Em outras opções da tela temos a opção "Descartar movimentação negativa/produtos em estoque não amparados," essa opção retira todos os produtos que estejam com o valor negativo quando tem divergência.
 
Cat 42 
Evento R1020
 
Quantidade inicial = É com base no rastreamento de estoque conforme (conforme o tipo de apuração definido)
Pode avaliar a movimentação na tela de análise de movimentação do rastreamento ST
 
Valor ICMS + ST Inicial = Vai ser a soma da coluna VLR ICMS+ST, da aba notas q/amparam estoque, de notas puxadas de base do mês anterior, para compor o valor inicial.
 
Quantidade final = O campo de quantidade inicial do mês anterior + os lançamentos do mês que o cat está sendo gerado
 
Valor ICMS + ST Final = Valor inicial calculado com base nas notas anteriores mais os valores das notas do mês em que o valor está sendo gerado.
 
BASE DO ST = Ele pega a base de ST divide pela quantidade negociada na nota e multiplica pela quantidade que foi usada, informada na coluna quantidade.
 
VLR ICMS+ST = Soma da coluna VLR ICMS + VLR ST
VLR ICMS = A coluna ICMS Unitário \* A coluna quantidade
VLR ST = coluna do VLR ST unitário \* Coluna Quantidade
VLR ST UNITÁRIO = Valor calculado de ST na nota / Pela quantidade negociada na nota
QUANTIDADE=

![Imagem 3: Para as notas do mês anterior o sistema utiliza a forma UEPS primeiro que entra primeiro que sai, proporcionalizando…](https://ajuda.sankhya.com.br/hc/article_attachments/29451617578775)   Para as notas do mês anterior o sistema utiliza a forma UEPS primeiro que entra primeiro que sai, proporcionalizando ate chegar na quantidade inicial da cópia de estoque.

![Imagem 4: Notas referente ao mês em que o CAT esta sendo gerado ele pega a quantidade que foi negociada na nota BASE ST UNITÁRIO…](https://ajuda.sankhya.com.br/hc/article_attachments/29451617581719) Notas referente ao mês em que o CAT esta sendo gerado ele pega a quantidade que foi negociada na nota
 
BASE ST UNITÁRIO = Coluna Base ST / QTD Inicial;
 
VLR ICMS + ST UNITÁRIO = soma das colunas VLR ICMS Unitário + ST Unitário;
 
VLR ICMS UNITÁRIO = Coluna VLR ICMS / pela Coluna quantidade.
