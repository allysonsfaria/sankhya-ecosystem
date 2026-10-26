---
id: "37226749805207"
titulo: "Fechamento de Caixa no PDV Web: A coluna “Calculado” não apresenta os valores esperados"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37226749805207-Fechamento-de-Caixa-no-PDV-Web-A-coluna-Calculado-n%C3%A3o-apresenta-os-valores-esperados"
trilha: "Melhores Práticas > Varejo"
atualizado_em: "2026-07-22T14:14:40Z"
rotulos: ["Configuração", "Fechamento de Caixa", "PDV Web", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Cartão de Crédito", "Cartão de Débito"]
---

# Fechamento de Caixa no PDV Web: A coluna “Calculado” não apresenta os valores esperados

Durante o fechamento de caixa no PDV Web, alguns usuários podem notar que a coluna **“Calculado”** não apresenta os valores esperados para determinadas formas de pagamento, especialmente **Cartão de Crédito** e **Cartão de Débito**.

Esse comportamento é normal e está relacionado à maneira como o sistema realiza a apuração automática dos valores do caixa.

No fechamento, cada forma de pagamento exibe duas colunas:

- **Informado**: Valor inserido manualmente pelo usuário no momento do fechamento do caixa.
- **Calculado**: Valor apurado automaticamente pelo sistema com base nos lançamentos realizados durante o período do caixa.

![Imagem 1: Calculado : Valor apurado automaticamente pelo sistema com base nos lançamentos realizados durante o período do caixa.](https://ajuda.sankhya.com.br/hc/article_attachments/37242834836631)

#### Por que os valores de pagamento em cartão não aparecem na coluna “Calculado”?

Esse comportamento é esperado. Os valores de **Cartão de Crédito** e **Cartão de Débito** só são exibidos automaticamente na coluna **“Calculado”** quando:

- As vendas foram **baixadas corretamente**
- A baixa foi realizada pelo mesmo usuário do caixa.

Quando essas condições não são atendidas, o sistema não consegue associar os valores ao caixa, mantendo os campos de cartão zerados na coluna **Calculado**.

Nesses casos, apenas a coluna **Informado** deve ser utilizada para o preenchimento manual dos valores.

**OBSERVAÇÃO:** Para que a baixa seja considerada no momento da confirmação, o **Tipo de Título / Tipo de Negociação** deve estar configurado corretamente para esse processo.
