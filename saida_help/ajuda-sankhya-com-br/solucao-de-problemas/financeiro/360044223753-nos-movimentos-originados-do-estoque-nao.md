---
id: "360044223753"
titulo: "Nos movimentos originados do estoque não é possível alterar os campos: Valor do Desdobramento, TOP, Data de Negociação, Receita/Despesa, Empresa, Provisão, Cód. e Valor da Moeda"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044223753-Nos-movimentos-originados-do-estoque-n%C3%A3o-%C3%A9-poss%C3%ADvel-alterar-os-campos-Valor-do-Desdobramento-TOP-Data-de-Negocia%C3%A7%C3%A3o-Receita-Despesa-Empresa-Provis%C3%A3o-C%C3%B3d-e-Valor-da-Moeda"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T16:00:19Z"
rotulos: ["#criadoRoger", "CORE_E02409", "Configuração", "Movimentação Financeira", "SEFAZ", "Estoque", "Preferências", "Financeiro", "Campos de estoque não podem ser alterados", "Restrição para manter integridade dos dados", "Use \"Renegociação de Títulos\" para ajustes"]
---

# Nos movimentos originados do estoque não é possível alterar os campos: Valor do Desdobramento, TOP, Data de Negociação, Receita/Despesa, Empresa, Provisão, Cód. e Valor da Moeda

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/17294004238103) MENSAGEM:**

[CORE\_E02409]: Nos movimentos originados do estoque não é possível alterar os campos: Valor do Desdobramento, TOP, Data de Negociação, Receita/Despesa, Empresa, Provisão, Cód. e Valor da Moeda.

**![Imagem 2: SITUAÇÃO](https://ajuda.sankhya.com.br/hc/article_attachments/17294038727831) SITUAÇÃO**

Ao tentar alterar os campos de títulos financeiros é apresentada a mensagem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17294004255511) SOLUÇÃO:**

![Imagem 4: Em algumas situações podem ser necessárias modificações nos títulos na "Movimentação Financeira" , mesmo que estes…](https://ajuda.sankhya.com.br/hc/article_attachments/17294004263063) Em algumas situações podem ser necessárias modificações nos títulos na **"Movimentação Financeira"**, mesmo que estes tenham sido originados das centrais (campo Origem = Estoque).

Lembre-se que a alteração de determinadas informações são bloqueadas, visto que são dados enviados à SEFAZ e precisam de sua integridade. Para ajustes relacionados a valores, por exemplo, opte por utilizar a rotina "[Renegociação de Títulos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115393)".

![Imagem 5: Tal comportamento é controlado pelos parâmetros abaixo (Tela "Preferências" ):](https://ajuda.sankhya.com.br/hc/article_attachments/17294004264983) Tal comportamento é controlado pelos parâmetros abaixo (Tela **"Preferências"**):

**"ALTERAFIN - Qdo originado da Central não permitir alterar nada"** e **"PROIBTRCPARFIN" - "Proíbe a troca de parceiro em financeiro de nota?"** -  da seguinte maneira:

(1)** CASO¹:**

Se o parâmetro de chave ALTERAFIN estiver ativado, será feito **o bloqueio de qualquer alteração** nos títulos que tiveram origem nas Centrais.

(1)** CASO²:**

Caso o parâmetro de chave ALTERAFIN esteja desligado e o parâmetro PROIBTRCPARFIN ativado, será **feito o bloqueio de modificações** nos títulos de origem nas Centrais, nos seguintes campos:

- Vlr do Desdobramento;
- Tipo Operação;
- Dt. Negociação;
- Receita/Despesa;
- Empresa;
- Provisão;
- Moeda;
- Vlr Moeda;
- Parceiro.

(1)** CASO³:**

Com o parâmetro de chave ALTERAFIN desligado e o parâmetro PROIBTRCPARFIN também desligado, tem-se **o bloqueio de alterações nos títulos originados** das Centrais, nos seguintes campos:

- Vlr do Desdobramento;
- Tipo Operação;
- Dt. Negociação;
- Receita/Despesa;
- Empresa;
- Provisão;
- Moeda;
- Vlr Moeda.

**![Imagem 6: CAUSA](https://ajuda.sankhya.com.br/hc/article_attachments/17294038752663) CAUSA**

Ocorre ao tentar alterar os campos: Valor do Desdobramento, TOP, Data de Negociação, Receita/Despesa, Empresa, Provisão ou  Cód. e Valor da Moeda, em um título na tela de Movimentação Financeira, de origem **estoque**.
