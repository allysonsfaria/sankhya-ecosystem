---
id: "6278817833239"
titulo: "A TOP só pode ser alterada para outra TOP do mesmo tipo de atualização de BEM"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/6278817833239-A-TOP-s%C3%B3-pode-ser-alterada-para-outra-TOP-do-mesmo-tipo-de-atualiza%C3%A7%C3%A3o-de-BEM"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-08-03T21:19:14Z"
rotulos: ["Configuração", "Atualização", "TOP", "Estoque", "CORE_E01490", "TOP Atualização BEM", "Erro"]
---

# A TOP só pode ser alterada para outra TOP do mesmo tipo de atualização de BEM

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16429657768727) MENSAGEM:**

[CORE\_E01490] A TOP só pode ser alterada para outra TOP do mesmo tipo de atualização de BEM.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16429679146647) CAUSA:**

Ocorre quando a TOP que está tentando alterar, tem a informação incompatível no campo Atualização do Bem da TOP atual que está selecionando na Central para nota/pedido.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16429657774871) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 4: Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP:](https://ajuda.sankhya.com.br/hc/article_attachments/16429679132567) Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP:

- Aba: **"Estoque"**
- Campo: **"Atualização do Bem"**
  Ambas as TOP's (Top 'atual' e top que está tentando inserir) devem estar configuradas com a mesma informação no campo acima.

![Imagem 5: Campo: "Atualização do Bem" Ambas as TOP's (Top 'atual' e top que está tentando inserir) devem estar configuradas com a…](https://ajuda.sankhya.com.br/hc/article_attachments/6278845738135)

![Imagem 6: Após o ajuste, será possível modificar a TOP na nota/pedido.](https://ajuda.sankhya.com.br/hc/article_attachments/16429657786519) Após o ajuste, será possível modificar a TOP na nota/pedido.

![Imagem 7: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17646367503127) **OBSERVAÇÃO:**

Na nova TOP, o campo 'Atualização do Bem' - aba Estoque deverá ser o mesmo da TOP antiga. Caso não seja, realize o ajuste ou gere o lançamento com a TOP desejada para evitar a necessidade de alterar o registro.
