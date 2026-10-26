---
id: "9357846850327"
titulo: "Programa não está preparado para juntar TOP Destino diferentes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9357846850327-Programa-n%C3%A3o-est%C3%A1-preparado-para-juntar-TOP-Destino-diferentes"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:08:31Z"
rotulos: ["Configuração", "Faturamento", "TOP", "CORE_E04630", "Gerenciamento de TOPs para Faturamento", "Erro", "Documentos Eletrônicos"]
---

# Programa não está preparado para juntar TOP Destino diferentes

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16975771393559) MENSAGEM:**

[CORE\_E04630] Programa não está preparado para juntar TOP Destino diferentes.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16975771395735) SOLUÇÃO:**

![Imagem 3: Verifique quais os 'Tipo de Operação' utilizados no lançamento dos documentos de origem (orçamentos/pedidos) a serem…](https://ajuda.sankhya.com.br/hc/article_attachments/16975771397143) Verifique quais os 'Tipo de Operação' utilizados no lançamento dos documentos de **origem**(orçamentos/pedidos) a serem faturados.

![Imagem 4: Acesse a tela "Tipos de Operação - TOP" e para as TOP'S identificadas no item 1, verifique a informação inserida no…](https://ajuda.sankhya.com.br/hc/article_attachments/16975771398679) Acesse a tela **"Tipos de Operação - TOP"** e para as TOP'S identificadas no item 1, verifique a informação inserida no campo abaixo:

- Aba **"Geral"**, campo **"TOP p/faturamento":**

![Imagem 5: Aba "Geral" , campo "TOP p/faturamento":](https://ajuda.sankhya.com.br/hc/article_attachments/16975743904535)

- A informação acima deve ser a mesma nas TOP'S utilizadas no lançamentos dos documentos de origem.  Nesse caso, realize o ajuste e o faturamento será permitido.
- Caso o **campo citado esteja em branco**, a TOP de faturamento poderá ser definida no momento do faturamento, solucionando a mensagem de validação tratada nesse artigo.
- Caso o ajuste não seja realizado, o faturamento deve ocorrer de forma "separada" considerando os pedidos com mesma TOP para faturamento. A marcação **"Uma nota para cada"**, no momento do faturamento, também permitirá essa condição.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16975771402519) CAUSA:**

O sistema não está preparado para junção de pedidos com TOP de destino diferentes, uma vez que a TOP é responsável pela caracterização dos movimentos do sistema. Nela são definidos os principais passos de um lançamento, tais como atualiza ou não estoque ou financeiro, cálculo de imposto, impressão de notas, TOP p/Faturamento etc. Qualquer marcação diferente de uma TOP para outra TOP, o sistema não consegue processar essas informações, que se tornam "conflitantes" para mesma operação.
