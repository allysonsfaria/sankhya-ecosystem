---
id: "26611540727831"
titulo: "Sistema não está considerando corretamente dos dados Dias ÚTEIS para Estocagem na análise de giro"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26611540727831-Sistema-n%C3%A3o-est%C3%A1-considerando-corretamente-dos-dados-Dias-%C3%9ATEIS-para-Estocagem-na-an%C3%A1lise-de-giro"
trilha: "Dúvidas Frequentes > Compras e Estoque"
atualizado_em: "2026-07-22T14:41:04Z"
rotulos: ["Configuração", "Cálculo", "Análise de Giro", "Parâmetros", "Estoque", "Passos para resolver", "Razão do erro", "Detalhe do erro", "não está considerando corretamente dos dados Dias ÚTEIS"]
---

# Sistema não está considerando corretamente dos dados Dias ÚTEIS para Estocagem na análise de giro

![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26668763432215) **SITUAÇÃO:**

Sistema não está considerando corretamente dos dados Dias ÚTEIS para Estocagem na analise de giro.

![Imagem 2: Sistema não está considerando corretamente dos dados Dias ÚTEIS para Estocagem na analise de giro.](https://ajuda.sankhya.com.br/hc/article_attachments/26611551818263)

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26611551819287)SOLUÇÃO:**

Quando o parâmetro **"CONSDIASUTEIS"** está ligado, o sistema tem o seguinte comportamento, se for informado o valor de 10 dias no campo Dias ÚTEIS para Estocagem, o sistema vai verificar quais os dias úteis dentro desses 10 para fazer o cálculo da sugestão de compras do giro. **Ex:** Considerando 10 dias dentro do mês sendo que o dia 01 cairia no dia 10, nesse caso tem 7 dias úteis, a conta seria Qt.Vnd/Dia útil  \* 7 no cálculo. Já com Parâmetro desligado, o sistema vai fazer o cálculo multiplicando a Qt.Vnd/Dia útil pelos 10 dias.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/26611540725911)CAUSA:**

Acontece essa situação quando o parâmetro CONSDIASUTEIS  está ligado.

Além disso, quando o parâmetro **"Somar o Lead Time aos dias úteis de estocagem - SOMALEADTIME"** for ligado, o campo Est. Mín. Sug. será calculado pela Qtd. Vnd/Dia Útil multiplicado pela soma do Lead Time com os Dias Úteis para Estocagem, ou seja:

Sug.Compra Giro= (Qt. Vnd/Dia útil" \* SNK\_QTD\_DIAS\_UTEIS (Data de hoje, Dias ÚTEIS pra Estocagem) \* % Acréscimo na Sugestão de Compras) - Estoque - Compra Pendente + Venda Pendente
