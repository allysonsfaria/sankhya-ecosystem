---
id: "27484347554711"
titulo: "Os componentes dos kits não estão sendo apresentados no giro de produtos na analise de giro"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/27484347554711-Os-componentes-dos-kits-n%C3%A3o-est%C3%A3o-sendo-apresentados-no-giro-de-produtos-na-analise-de-giro"
trilha: "Dúvidas Frequentes > Compras e Estoque"
atualizado_em: "2026-07-22T14:39:37Z"
rotulos: ["Produtos", "Configuração", "Análise de Giro", "TOP", "Estoque", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Os componentes dos kits não estão sendo apresentados no giro de produtos na analise de giro"]
---

# Os componentes dos kits não estão sendo apresentados no giro de produtos na analise de giro

![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/27543725261335) **SITUAÇÃO:**

Os componentes dos kits não estão sendo apresentados no giro de produtos na análi se de giro.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/27484331201431)SOLUÇÃO:**

Desligue o parâmetro **"JUNVENDTROCA - Junção de pedidos de Venda e Troca"**. Pois, esse parâmetro habilita uma tela de **"Agendador de Junção de pedidos de Venda e Troca"** no Sankhya e, quando essa rotina é utilizada, o sistema insere nos itens da troca **usoprod = 'D'**. Assim, não faz sentido o sistema inserir itens de trocas como giro.

Por outro lado, caso esse rotina (JUNVENDTROCA) tenha que ser utilizada, desmarque nas devidas Top's para não calcular Giro (aba **"Geral",** campo **"Análise de Giro"**).

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/27484347553559)CAUSA:**

Esse problema ocorre porque quando o parâmetro JUNVENDTROCA está ligado na rotina de consolidação de Giro o sistema insere na query de consolidação o filtro  ITE.USOPROD <> 'D'

![Imagem 4: Esse problema ocorre porque quando o parâmetro JUNVENDTROCA está ligado na rotina de consolidação de Giro o sistema…](https://ajuda.sankhya.com.br/hc/article_attachments/27484347553687)
