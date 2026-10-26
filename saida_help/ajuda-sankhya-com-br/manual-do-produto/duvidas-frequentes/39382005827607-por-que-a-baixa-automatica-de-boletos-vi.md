---
id: "39382005827607"
titulo: "Por que a baixa automática de boletos via API ocorre em data diferente do crédito em conta?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39382005827607-Por-que-a-baixa-autom%C3%A1tica-de-boletos-via-API-ocorre-em-data-diferente-do-cr%C3%A9dito-em-conta"
trilha: "Manual do Produto > Financeiro e Patrimônio > Sankhya Fintech > Dúvidas frequentes "
atualizado_em: "2026-07-29T13:13:05Z"
rotulos: ["Configuração", "Contas", "Boletos", "Financeiro", "API", "Artigo criado KCS", "Financeiro - KCS"]
---

# Por que a baixa automática de boletos via API ocorre em data diferente do crédito em conta?

A baixa automática de boletos via API pode apresentar divergências entre a **"data de crédito em conta"** e a **"data de baixa"** no sistema. Esse comportamento está relacionado à forma como cada banco disponibiliza as informações através da API e às configurações estabelecidas na conta bancária do ERP Sankhya.

Quando um boleto é pago e o valor é creditado na conta bancária, o banco processa essa informação e a disponibiliza via API. No entanto, nem todos os bancos retornam a data efetiva de crédito em conta, o que pode resultar em baixas automáticas realizadas em datas posteriores ao crédito real.

### Comportamento específico por banco

Cada instituição bancária possui particularidades no retorno de informações via API:

**Banco Itaú:** Não retorna via API a data efetiva de crédito em conta. O banco disponibiliza essa informação em D+1, e a baixa é permitida apenas no próximo dia útil. Por exemplo, um boleto creditado na sexta-feira (dia 06) pode ter sua baixa processada apenas na segunda-feira (dia 09), pois o banco não envia a data do crédito em conta (liquidação).

**Bancos Itaú, Santander, Sicoob e Sicredi:** Atualmente, não retorna via API a informação da data de crédito em conta. Quando configurada a baixa para ocorrer com base no crédito em conta, podem ocorrer divergências com relação ao crédito em conta com a data de baixa do título no sistema.

**Banco Sicoob e Sicredi:** Não disponibiliza o canal de pagamento, o que impossibilita a distinção entre pagamentos feitos via linha digitável e QR code.

### Configuração recomendada para baixa automática

Para evitar divergências nas datas de baixa, configure corretamente a conta bancária na tela **"Contas"** (Financeiro Cadastros Contas):

**(1)** Acesse a tela **"Contas"** e localize a conta bancária integrada via API.

**(2)** No campo **"Baixa Automática"**, revise a melhor opção conforme a regra de negócio e convênio com o banco.

- Não realizar;
- Realizar na data de pagamento;
- Realizar na data do crédito em conta.

**(3)** Salve as alterações realizadas na conta bancária.

### Quando usar "Realizar na data de crédito em conta"

A opção **"Realizar na data de crédito em conta"** deve ser utilizada apenas quando o prazo de recebimento seja 0 ou 1 dia, visto que o banco não retorna via API a data de crédito em conta.

Se o banco mudou o comportamento de liquidação para D+0 (crédito no mesmo dia do pagamento), configure a baixa automática para **"Realizar na data de pagamento"**.

### Monitoramento das baixas automáticas

Após realizar os ajustes de configuração, acompanhe os próximos boletos liquidados através da tela **"Acompanhamento de Boletos API"** (Financeiro >> Consultas >> Acompanhamento de Boletos API) para validar se a baixa está ocorrendo na data correta.

### Observações importantes

A API de Boleto Rápido realiza a comunicação automática com o banco, e quando o cliente efetua o pagamento, o banco informa ao sistema que a liquidação foi realizada. O processamento da baixa automática segue a configuração estabelecida na conta bancária.

O sistema não possui controle sobre a forma como o banco envia as informações via API. Em alguns títulos, o banco retorna a data de determinada forma e, em outros, de maneira diferente, conforme critérios internos da própria instituição financeira.

Para situações específicas relacionadas ao comportamento da API de determinado banco, entre em contato com o suporte do produto API para avaliar possíveis melhorias ou correções junto à instituição financeira.
