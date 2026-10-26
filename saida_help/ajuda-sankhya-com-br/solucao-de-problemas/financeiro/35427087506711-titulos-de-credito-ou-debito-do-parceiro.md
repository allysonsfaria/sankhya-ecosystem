---
id: "35427087506711"
titulo: "Títulos de crédito ou débito do parceiro não estão sendo utilizados na compensação? Saiba como resolver."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35427087506711-T%C3%ADtulos-de-cr%C3%A9dito-ou-d%C3%A9bito-do-parceiro-n%C3%A3o-est%C3%A3o-sendo-utilizados-na-compensa%C3%A7%C3%A3o-Saiba-como-resolver"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T14:25:10Z"
rotulos: ["Configuração", "Parceiro", "Movimentação Financeira", "crédito", "Financeiro", "Títulos", "Passos para resolver", "Razão do erro", "Detalhe do erro", "do parceiro", "não estão sendo", "utilizados", "como resolver", "débito", "compensação"]
---

# Títulos de crédito ou débito do parceiro não estão sendo utilizados na compensação? Saiba como resolver.

**SITUAÇÃO:**

Ao realizar o lançamento da nota de venda ou de compra, o sistema identifica que existem títulos de crédito ou débito vinculados ao parceiro, porém esses valores não estão sendo compensados automaticamente no processo.

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/35427147831063) SOLUÇÃO:**

**(1)** Valide se o crédito ou débito está disponível:

- Acesse a tela “**Configurador de Layout da Nota”** (Comercial» Configuração), selecione o layout em uso e adicione o campo **“Valor Crédito”**. Dessa forma, será possível visualizar se o parceiro possui créditos disponíveis no momento do lançamento.

![Imagem 2: Acesse a tela “ Configurador de Layout da Nota” (Comercial» Configuração), selecione o layout em uso e adicione o campo…](https://ajuda.sankhya.com.br/hc/article_attachments/36321371782039)

**(2)** Confira os títulos na Movimentação Financeira:

Acesse a tela ''**Movimentação Financeira''** (Financeiro» Rotinas) e aplique os filtros conforme o tipo de operação:

(1)** Crédito de cliente:**

- Despesas
- Real
- Pendentes
- Informe o **código do parceiro** em questão

(1)** Débito de fornecedor:**

- Receitas
- Real
- Pendentes
- Informe o **código do parceiro** em questão

**(3)** Valide a configuração dos parâmetros e tipos de título:

- Verifique se as configurações estão conforme a documentação [**Compensação de Crédito ou Débito em Compra ou Venda**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601914-Compensa%C3%A7%C3%A3o-de-Cr%C3%A9dito-ou-D%C3%A9bito-em-Compra-ou-Venda);
- Revise o uso dos tipos de título configurados nos parâmetros:

  `TIPTITCREDCLI` → Tipo de título utilizado para **crédito de cliente**

  `TIPTITDEBFOR` → Tipo de título utilizado para **débito de fornecedor**

**Observação:**
Se, por exemplo, houver um título de receita utilizando o mesmo tipo de título definido no parâmetro **TIPTITCREDCLI** (que deveria ser destinado a despesas), isso poderá impactar diretamente o processo de compensação. Portanto, é essencial garantir que cada tipo de título esteja corretamente classificado conforme o parâmetro correspondente.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/35427087505303)CAUSA:**

Ocorre quando há inconsistências nas configurações do tipo de título financeiro ou na parametrização da compensação de créditos e débitos. Em determinados casos, os títulos podem estar classificados de forma incorreta, por exemplo, como receita em vez de despesa, o que impede que o sistema realize a compensação automática durante o faturamento.
