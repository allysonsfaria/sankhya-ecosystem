---
id: "28948282766871"
titulo: "Possível conflito no cálculo da OP - Botão Ver Custos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/28948282766871-Poss%C3%ADvel-conflito-no-c%C3%A1lculo-da-OP-Bot%C3%A3o-Ver-Custos"
trilha: "Dúvidas Frequentes > Produção"
atualizado_em: "2026-07-22T14:37:30Z"
rotulos: ["Produtos", "Custos", "Configuração", "Estoque", "Preferências", "Passos para resolver", "Razão do erro", "Detalhe do erro"]
---

# Possível conflito no cálculo da OP - Botão Ver Custos

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/28948251571095) **MENSAGEM:**

Possível conflito no cálculo - Possui um item de custo na mesma data da nota de produção, pode existir divergência no valor apresentado por questões cronológicas.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/28948251574551)CAUSA:**

O sistema deixa a linha em vermelho mostrando que após o lançamento da nota de produção houve atualização de custo de determinada MP/PI. Isso se dá devido a compras de MP após a produção (se a MP trabalhar com controle, será apresentado quando houver entrada daquele controle utilizado, é necessário trabalhar com a preferência ligada CUSTOPORCONT (Custo por Controle, onde cada controle pode ter um custo diferente) e/ou produção de PI após aquela nota de produção, pois com entradas poderá haver uma atualização do custo.

Caso haja diversas entradas em um dia, o sistema gera um custo médio de acordo com o estoque anterior e o atual (daquela nota de compra ou produção do PI), nesse help explica o cálculo do custo médio ([Como é realizado o cálculo do custo médio](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051314174)).
