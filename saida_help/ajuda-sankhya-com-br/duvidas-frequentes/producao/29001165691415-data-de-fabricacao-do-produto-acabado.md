---
id: "29001165691415"
titulo: "Data de fabricação do produto acabado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/29001165691415-Data-de-fabrica%C3%A7%C3%A3o-do-produto-acabado"
trilha: "Dúvidas Frequentes > Produção"
atualizado_em: "2026-07-22T14:37:26Z"
rotulos: ["Produtos", "Configuração", "Estoque", "Produção", "Validade", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Data de fabricação do produto acabado", "Base para cálculo da Dt.Validade", "Prazo validade/tolerância", "Squad WMS"]
---

# Data de fabricação do produto acabado

##### Este documento descreve as funcionalidades relacionadas à definição e ao cálculo da data de validade para produtos acabados no sistema, detalhando os parâmetros disponíveis na tela ''Composição do Produto'' (Produção » Cadastros » Composição do Produto), na aba ''Geral''.

##### Abaixo, detalhamos o campo "Base para cálculo da Dt.Validade" e suas configurações:

#### Campo "Base para cálculo da Dt.Validade"

O campo **''Base para cálculo da Dt. Validade''** tem a finalidade de **parametrizar a base utilizada para calcular a data de validade do produto acabado**. As opções disponíveis são:

**1. Não calcula:**

- A data de validade do produto acabado não será calculada automaticamente.

**2. Data da primeira nota de produção do lote:**

- A data de validade do PA será baseada na **data da primeira nota de produção do lote**.

Configuração no sistema:

- Acesse a tela **''Produtos''** (Configurações » Cadastros » Produtos » Produtos).
- Localize a aba **''Medidas e Estoque''**, sub-aba **''Estoque''.**
- Verifique o campo **''Prazo validade/tolerância''**, que será utilizado no cálculo da validade.

![Imagem 1: Verifique o campo ''Prazo validade/tolerância'' , que será utilizado no cálculo da validade.](https://ajuda.sankhya.com.br/hc/article_attachments/36857722755991)

**3. Menor Dt.Validade das Matérias-Primas (MPs):**

- A data de validade do PA será determinada pela **menor data de validade entre as MPs** que compuseram o produto acabado.

**4. Data de Inicialização da Ordem de Produção (OP):**

- A data de validade do PA será calculada com base na **data de inicialização da OP**.
- Para o cálculo, utiliza-se o campo ''Prazo validade/tolerência'', conforme o **procedimento detalhado no item 2.**

**INFORMAÇÕES ADICIONAIS:**

- A **data de fabricação do produto** acabado é sempre registrado como a data de entrada no sistema, corresponde á data da nota de produção de produção que originou o produto.
- O preenchimento correto do campo "Prazo validade/tolerância" no cadastro do produto é essencial para o cálculo automático da validade.
- Certifique-se de configurar a "Base para cálculo da Dt.Validade" de acordo com as necessidades operacionais, garantindo **precisão das datas de validade**.
