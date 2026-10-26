---
id: "13850663928087"
titulo: "Usa dias fixos para pagamentos, com problemas relacionados aos meses de 31 dias"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/13850663928087-Usa-dias-fixos-para-pagamentos-com-problemas-relacionados-aos-meses-de-31-dias"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:59:45Z"
rotulos: ["Configuração", "Parceiro", "Vencimento", "Financeiro", "Pagamento", "Configurações de Sistema", "Cálculo de Vencimento", "Dias Fixos"]
---

# Usa dias fixos para pagamentos, com problemas relacionados aos meses de 31 dias

**![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/16913052841879) SITUAÇÃO:**

Cliente possui dias fixos para pagamento. No tipo de negociação foi determinado a condição de 30 dias para pagamento. Entretanto, ao emitir um faturamento cujo o o mês possui 31 dias, foi observado que o sistema se perde no calculo. Considera-se que o cliente utiliza a data de entrada/saída como base dos vencimentos.

**Exemplo:** Quando emitido um faturamento no dia 01/03/2023, o sistema automaticamente calcula o vencimento para o dia 01/03/2023, ignorando a regra do sistema, que deveria somar 30 dias ou a data prox. de pagamento.

**![Imagem 2](https://ajuda.sankhya.com.br/hc/article_attachments/16913036178967) SOLUÇÃO:**

![Imagem 3](https://ajuda.sankhya.com.br/hc/article_attachments/16970559174423) Para esta situação, observe em especifico se o parâmetro: **"Posterga vencimento com dia fixo (CALDIAFIXOVCT)? - POSVENCDIAFIX"**, está ativado.

Caso não, ative o mesmo e ser fique atento as seguintes configurações:

- Tipo negociação > Características > Campo Prazo mínimo = 30
- Tipo negociação > Parcelas > Prazo: 30
- Tipo negociação > Características > Base do prazo: A partir do dia
- Tipo negociação > Parcelas > Vencimento não útil: Vencimento original
- Parceiro > Crédito > Campo prazo médio pagamento = 30

**(1)** Entretanto, vale destacar que que além deste, outros parâmetros impactam o funcionamento dos "Dias Fixos" e devem estar devidamente configurados para seu correto funcionamento.

- **POSVENCDIAFIX** - Ligado
- **DIASMAXPRAZEXTR** - 0
- **RECALVENCFAT** - Ligado
- **DTCALCVENC** - saída
- **TRANSFVENC** - Desligado
- **USARDIAFIXOVCT** - Ligado
- **POSVENCDIAFIX** - Desligado
- **ACVENDIAFIXOVCT** - Ligado
- **CALDIAFIXOVCT** - Ligado
- **HABTIPALTDTVENC** - Desligado
- **FP\_FOLGADOM** e **FOLGADOM** - Ligado
- **DIASMAXPRAZEXTR** - 0

**![Imagem 4: DIASMAXPRAZEXTR - 0](https://ajuda.sankhya.com.br/hc/article_attachments/16913052848535) CAUSA:**

Problemas relacionados ao cálculo de vencimento utilizando dias fixos para meses com 31 dias.
