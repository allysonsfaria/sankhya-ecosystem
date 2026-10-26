---
id: "37217695821719"
titulo: "Saldo Devedor na Folha: Desconto  do Crédito do Trabalhador"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37217695821719-Saldo-Devedor-na-Folha-Desconto-do-Cr%C3%A9dito-do-Trabalhador"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-08-25T20:21:48Z"
rotulos: ["Configuração", "Financeiro", "Folha", "eSocial", "Saldo Devedor na Folha", "Desconto do Crédito do Trabalhador", "Desconto da parcela", "Manual do Crédito do Trabalhador", "Folha mensal negativa", "Crédito Consignado"]
---

# Saldo Devedor na Folha: Desconto  do Crédito do Trabalhador

O **desconto do crédito consignado** está fazendo com que a **folha mensal do colaborador fique negativa**. Como o colaborador possui outros descontos vinculados à empresa, como convênios, planos, entre outros, o valor do consignado deveria ser descontado de forma proporcional ao saldo disponível na folha, evitando a geração de saldo negativo.

Conforme o **Manual do Crédito do Trabalhador – eConsignado**, **o desconto da parcela considera exclusivamente os eventos que compõem a base da margem consignável do trabalhador**.

O manual define que rubricas como plano de saúde, por exemplo, não integram essa base de cálculo. Dessa forma, para a aplicação do desconto do eConsignado, não são considerados eventos que não façam parte da margem consignável, ainda que impactem o valor líquido da folha de pagamento.

Inclusive, o próprio manual apresenta um exemplo específico envolvendo plano de saúde (coparticipação), reforçando que esse evento não compõe a margem consignável e que não há previsão de desconto prévio do plano de saúde para a aplicação do eConsignado.

![Imagem 1: Inclusive, o próprio manual apresenta um exemplo específico envolvendo plano de saúde (coparticipação), reforçando que…](https://ajuda.sankhya.com.br/hc/article_attachments/37226492443159)

Manual do Crédito do Trabalhador: <https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/manual-e-documentacao-tecnica-old>

**CAUSA:**

O desconto do eConsignado é **calculado com base exclusivamente na margem consignável**, conforme **definido no Manual do Crédito do Trabalhador – eConsignado**. Eventos como plano de saúde, convênios e coparticipações não compõem essa base, o sistema não os considera no cálculo da parcela do consignado.

Dessa forma, quando o colaborador possui diversos descontos que reduzem o valor líquido da folha, o sistema não realiza o desconto parcial do consignado, o que pode resultar na geração de saldo devedor.
