---
id: "38435817397783"
titulo: "Funcionamento do parâmetro VLRLIQBOL no Boleto Rápido por API"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38435817397783-Funcionamento-do-par%C3%A2metro-VLRLIQBOL-no-Boleto-R%C3%A1pido-por-API"
trilha: "Dúvidas Frequentes > Financeiro"
atualizado_em: "2026-07-22T14:01:33Z"
rotulos: ["Configuração", "Contas", "Movimentação Financeira", "Boleto", "Financeiro", "Boleto Rápido API", "API", "Parâmetro VLRLIQBOL", "Valor líquido do título", "Valor bruto"]
---

# Funcionamento do parâmetro VLRLIQBOL no Boleto Rápido por API

Ao utilizar contas com **Boleto Rápido por API** ativo, o registro do boleto é definido pela configuração do parâmetro **VLRLIQBOL**, que determina a forma de composição do valor enviado na integração com o banco.

- Quando o parâmetro está **ligado**, é transmitido apenas o **valor líquido do título**.
- Quando está **desligado**, são enviados o **valor bruto e o desconto separadamente**.

A alteração desse parâmetro após o registro de boletos pode gerar divergências na baixa e na Movimentação Financeira, pois o título foi registrado sob regra distinta daquela aplicada no momento da liquidação.

**Parâmetro Ligado**

O sistema envia ao banco o **valor líquido do título** (já com desconto deduzido).

Exemplo:

- Valor do desdobramento: R$ 100,00
- Desconto: R$ 10,00
- Valor enviado para registro: **R$ 90,00**

Nesse cenário:

- O desconto não é enviado separadamente;
- Não é compatível com inserção ou alteração de desconto após o registro;
- Pode gerar divergência se o parâmetro for alterado após o registro do boleto.

**Parâmetro Desligado**

O sistema envia:

- Valor do título: R$ 100,00
- Desconto informado: R$ 10,00 de forma separada.

Nesse cenário:

- O banco registra o valor bruto;
- É possível inserir ou alterar desconto após o registro sem gerar inconsistências;
- Mantém o comportamento financeiro convencional.

![Imagem 1: Mantém o comportamento financeiro convencional.](https://ajuda.sankhya.com.br/hc/article_attachments/38435827116951)
