---
id: "39376713327767"
titulo: "Estoque não retorna após cancelamento de NF de Devolução"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39376713327767-Estoque-n%C3%A3o-retorna-ap%C3%B3s-cancelamento-de-NF-de-Devolu%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-08-01T02:53:00Z"
rotulos: ["NF-e", "Movimentação Financeira", "SEFAZ", "Estoque", "Aba WMS", "Erro", "Artigo criado KCS", "CVE - KCS"]
---

# Estoque não retorna após cancelamento de NF de Devolução

**Mensagem**

Após o cancelamento de uma Nota Fiscal de Devolução, o estoque do produto não retorna ao sistema, impedindo a emissão de uma nova nota de devolução correta.

**Situação**

Após o cancelamento de uma Nota Fiscal de Devolução, o estoque do produto não retorna ao sistema, impedindo a emissão de uma nova nota de devolução correta.

**Solução**

Para resolver esta situação, avalie as seguintes alternativas:

**Opção 1: Concluir o cancelamento extemporâneo no Sankhya**

**(1)** Consulte a Contabilidade sobre a possibilidade de solicitar o Cancelamento Extemporâneo junto à Sefaz.
**(2)** Com a aprovação da Sefaz em mãos, informe o número e a data do protocolo de cancelamento na tela específica do Sankhya para cancelamentos fora do prazo.

**(3)** Ao concluir esse passo, o sistema reverte automaticamente o estoque da nota cancelada.

**Opção 2: Ajuste de Estoque de Entrada (se o cancelamento não puder ser concluído no sistema)**

Caso não seja possível realizar o cancelamento extemporâneo, siga as orientações abaixo:

**(1)** Acesse a tela **"Ajuste de Estoque"**.
**(2)** Registre um Ajuste de Estoque de Entrada com os mesmos produtos, quantidades e local de estoque da nota cancelada.

**Causa**

O cancelamento de uma nota fiscal no Sankhya sempre estorna o estoque automaticamente, pois o processo exclui o registro da nota do sistema. Isso vale tanto para o cancelamento dentro do prazo quanto para o extemporâneo.

O estoque só deixa de retornar quando o cancelamento não é concluído de fato no Sankhya. Isso costuma acontecer quando:

- A nota está fora do prazo de cancelamento (regular + tolerância, parametrizados na empresa) e o usuário obteve aprovação diretamente com a Sefaz, mas **não informou o protocolo do cancelamento extemporâneo na tela do Sankhya,** sem esse passo, o sistema não reconhece a nota como cancelada.
- Houve falha de comunicação com a Sefaz e a nota ficou em status pendente.
