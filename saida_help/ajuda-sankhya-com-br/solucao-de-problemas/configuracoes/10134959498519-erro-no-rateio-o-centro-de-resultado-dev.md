---
id: "10134959498519"
titulo: "Erro no rateio. O Centro de Resultado deve ser informado. O parâmetro 'EXIGCRCFR' está ligado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10134959498519-Erro-no-rateio-O-Centro-de-Resultado-deve-ser-informado-O-par%C3%A2metro-EXIGCRCFR-est%C3%A1-ligado"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:04:28Z"
rotulos: ["Configuração", "Movimentação Financeira", "Centro de Resultado", "Financeiro", "CORE_E05389", "CORE_E03357", "Erro de Rateio: Centro de Resultado Necessário", "Erro"]
---

# Erro no rateio. O Centro de Resultado deve ser informado. O parâmetro 'EXIGCRCFR' está ligado

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19033693744791) MENSAGEM:**

Erro no rateio. O Centro de Resultado deve ser informado. O parâmetro **'EXIGCRCFR'** está ligado.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19033678364311) SITUAÇÃO:**

Ao processar um arquivo OFX ou realizar um lançamento a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19033693750807) CAUSA:**

Ocorre quando o parâmetro **"Exigir CR na central/financeiro/rateio? - EXIGCRCFR"** está ligado e o centro de resultado não é informado.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19033693757719) SOLUÇÃO:**

Quando o parâmetro **"Exigir CR na central/financeiro/rateio? - EXIGCRCFR"** estiver ligado, o sistema irá exigir que o usuário indique o centro de resultado nas seguintes telas:
- Movimentos da CAC e CAF (pedido e nota);
- Tela de rateio ("Rateio de Receitas e Despesas");
- Financeiros das centrais;
- Movimentação financeira.

![Imagem 5: Quando o parâmetro "Exigir CR na central/financeiro/rateio? - EXIGCRCFR" estiver ligado, o sistema irá exigir que o…](https://ajuda.sankhya.com.br/hc/article_attachments/19033693760023)

Caso não deseje informar o centro de resultado, desligue o parâmetro.
