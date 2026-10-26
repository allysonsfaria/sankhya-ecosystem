---
id: "360044607214"
titulo: "Controle cartão de crédito"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607214-Controle-cart%C3%A3o-de-cr%C3%A9dito"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-07-29T14:41:57Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Parceiro", "Rotina Específica de Parceiro", "br.com.sankhya.opcredito.geracao.controle.cartao", "Controle cartão de crédito manual", "Financeiro", "Geração de Cartões de Crédito", "Detalhes de Vencimento e Segurança", "Consulta e Alteração de Status", "Cartão de Crédito", "Operações de Crédito"]
---

# Controle cartão de crédito

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312409832215) Módulo: Financeiro > Rotinas > Operações de Crédito
```

---

**Importante:** esta rotina é exclusiva de um parceiro e habilitada por um parâmetro específico.

---

Esta tela possui as seguintes finalidades:

![Imagem 2: A Geração de Cartões de Créditos permitirá cadastrar um cartão para o parceiro da proposta.](https://ajuda.sankhya.com.br/hc/article_attachments/16242541587479) A Geração de Cartões de Créditos permitirá cadastrar um cartão para o parceiro da proposta.

![Imagem 3: E a Consulta de cartões já gerados possibilitará também que você realize a alteração do status manualmente.](https://ajuda.sankhya.com.br/hc/article_attachments/16242541590423) E a Consulta de cartões já gerados possibilitará também que você realize a alteração do status manualmente.

![Imagem 4: E a Consulta de cartões já gerados possibilitará também que você realize a alteração do status manualmente.](https://ajuda.sankhya.com.br/hc/article_attachments/4415885463703)

O número do cartão será gerado automaticamente e será composto de 19 dígitos, obedecendo ao seguinte padrão:

- Os 6 primeiros dígitos referem-se ao BIN da administradora. JETPAR CARD (636798) e CREDPAR (636624). O 7º digito é o código do produto.
- Após o BIN a JETPARCARD usa o **"0"** e a CREDPAR o n **"1"**. Este valor deverá estar informado no parâmetro BINDOCARTAO, como por exemplo, 6366241.
- Do 8º ao 18º dígito trata-se de número sequencial. Será utilizado a TGFUM para registrar a sequencia de numeração.
- O 19º dígito é o dígito verificador. Calculado por meio do MÓDULO 11.

Quando você informar os dados para a geração do cartão, o campo **"Status"** ficará desabilitado e o status padrão será **"Embossamento"**.

A alteração do Status só será permitida desde que seja feita da seguinte forma:

- De Embossamento para **"Bloqueado"**.
- De Bloqueado para **"Ativo"**.
- De Ativo para **"Roubado"**.
- De Ativo para **"Perda"**.
- De Ativo para **"Cancelado"**.

A **"Dt. Vencimento"** do cartão será calculada automaticamente de acordo com o parâmetro **"Qtde de anos para vencimento do cartão -** **VENCARTAOANOS"**. O sistema calcula e insere o último dia do mês como vencimento, por exemplo:

**(1)**Se o cartão for gerado no dia 17/01/2021, o vencimento ficará para 31/01/2026, caso no parâmetro esteja informado um período de vencimento de 5 anos.

No campo **"Nome no Cartão"**, informe o nome do parceiro que será impresso no cartão de crédito. A quantidade máxima de caracteres é 22.

Você poderá informar também a **"Dt. Embossamento"**, isto é, a data de plastificação/acabamento do cartão.

---

![Imagem 5: Informações adicionais](https://ajuda.sankhya.com.br/hc/article_attachments/16242541593239) **Informações adicionais**

- O usuário logado será apresentado no campo **"Usuário"** e a **"data de alteração"** e de **"cadastro"** serão preenchidos automaticamente nos seus respectivos campos.
- O sistema não permitirá cadastrar dois ou mais cartões para o mesmo parceiro. Para que isso possa ser feito, o cartão já criado deverá ser cancelado.
- Existe também a possibilidade de gerar um novo cartão, por meio do botão **"Outras Opções"**, opção **"Gerar Novo Cartão"**. Caso você solicite a geração de um novo cartão, o sistema cancelará o cartão atual e gerará um novo com as mesmas informações, solicitando apenas que seja informado o nome que será impresso no cartão, que poderá ser o mesmo ou não.
- O painel do lado esquerdo é composto de filtros para facilitar a busca. Por meio deste, pode-se filtrar pelo **"Número do Cartão"**, pelo **"Nome do Parceiro"** que está no cartão, pelo **"Código do Próprio Parceiro"**, pelo **"Período de vencimento"** do cartão de crédito, pelo **"Status"** (Embossamento, Ativo, Cancelado, Bloqueado ou Roubado), ou ainda realizar algum filtro personalizado.
- Para ativar o cartão que está em Embossamento, é necessário que você altere o status para Bloqueado e posteriormente ative-o.
