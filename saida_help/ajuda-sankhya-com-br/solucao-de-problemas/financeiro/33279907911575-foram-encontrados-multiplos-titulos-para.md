---
id: "33279907911575"
titulo: "Foram encontrados múltiplos títulos para o NSU XXX"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33279907911575-Foram-encontrados-m%C3%BAltiplos-t%C3%ADtulos-para-o-NSU-XXX"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T14:29:08Z"
rotulos: ["Configuração", "Movimentação Financeira", "Financeiro", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Foram encontrados múltiplos", "Layout de Processamento de Arquivo", "Campos do Registro", "NRO_PARCELA", "títulos para o NSU XXX.", "Desdobramento", "Erro", "Documentos Eletrônicos"]
---

# Foram encontrados múltiplos títulos para o NSU XXX

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/33279845753879) **MENSAGEM:**

Foram encontrados múltiplos títulos para o NSU XXX.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/33279845754263)SOLUÇÃO:**

Para que o sistema reconheça os registros de maneira adequada, é importante que, no parcelamento, cada título tenha sua parcela correspondente de forma individual.

(1)** Para validar as duas situações, siga os passos a seguir:**

**(1)** Acesse a tela **"Layout de Processamento de Arquivo"** (Financeiro>> Rotinas >>Layout de Processamento de Arquivo)

- Selecione o layout utilizado;
- Verifique na grade ''**Campos do Registro''**, se a variável ''**NRO\_PARCELA''** está presente e se está posicionada corretamente na sequência esperada.

![Imagem 3: Verifique na grade '' Campos do Registro'' , se a variável '' NRO_PARCELA'' está presente e se está posicionada…](https://ajuda.sankhya.com.br/hc/article_attachments/33347278024983)

**(2)** Acesse a tela **"Movimentação Financeira"** (Financeiro >> Rotinas >> Movimentação Financeira)

- Consulte o NSU em questão;
- Verifique se o campo **''Desdobramento''** está sendo repetido em outras parcelas com o mesmo NSU.

![Imagem 4: Verifique se o campo ''Desdobramento'' está sendo repetido em outras parcelas com o mesmo NSU.](https://ajuda.sankhya.com.br/hc/article_attachments/33347278025623)

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/33279845755031)CAUSA:**

Esse erro acontece quando, na configuração do Layout de Processamento de Arquivo, a variável NRO\_PARCELA não foi definida, ou se há mais de um registro com o mesmo NSU e o mesmo Desdobramento (Parcela).
