---
id: "360045114973"
titulo: "Autorização para cartão de crédito"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114973-Autoriza%C3%A7%C3%A3o-para-cart%C3%A3o-de-cr%C3%A9dito"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-07-29T14:43:29Z"
rotulos: ["AJUDA DO SKW", "manual", "Parceiro", "br.com.sankhya.opcredito.autorizacao.cartao", "Autorização para cartão de crédito manual", "Rotina Específica de Parceiro", "Crédito", "Financeiro", "Autorização de compras com cartão", "Uso para usuários B2B e normais", "Gerenciamento de parcelas e autorizações", "Cartão de Crédito", "Operações de Crédito"]
---

# Autorização para cartão de crédito

| ``` ![Imagem 1: Módulo: Financeiro > Rotinas > Operações de Crédito](https://ajuda.sankhya.com.br/hc/article_attachments/42312467900567) Módulo: Financeiro > Rotinas > Operações de Crédito ``` |
| --- |

---

![Imagem 2: Esta rotina é exclusiva de um Parceiro e habilitada por parâmetro específico.](https://ajuda.sankhya.com.br/hc/article_attachments/16106792056343)  Esta rotina é exclusiva de um Parceiro e habilitada por parâmetro específico.

---

O lojista usará esta tela para registrar/autorizar a compra realizada no cartão, no RG ou no CPF do cliente.

**Observação:** tanto o usuário B2B quanto o usuário normal tem acesso à tela abaixo, podendo informar o cartão de crédito. No caso de usuário B2B, não será visível na grade o campo **"Data Vencimento"**.

![Imagem 3: Observação: tanto o usuário B2B quanto o usuário normal tem acesso à tela abaixo, podendo informar o cartão de crédito.…](https://ajuda.sankhya.com.br/hc/article_attachments/360082178714)

Você deverá pesquisar um cliente através do botão **"Pesquisa de Clientes"**, o qual terá as opções **"CPF/CNPJ"**, **"RG"** e **"Número do Cartão"**.

- Caso você tente realizar uma compra com um cartão que esteja com o status **"Embossamento"** ou **"Bloqueado"**, o sistema não permitirá e emitirá uma mensagem alertando-o que a compra deverá ser realizada com o CPF/CNPJ ou com o RG. Se o cartão estiver ativo, a compra obrigatoriamente deverá ser realizada pelo mesmo e, se estiver nos demais status (Cancelado, Roubado ou Perdido), a compra não poderá ser realizada por nenhuma das opções.
- A data para vencimento será calculada considerando a quantidade de dias informada no campo **"Prazo médio vencimento"**, presente na aba [Crédito](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abacrdito) da tela de [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros).
- O valor da parcela será calculado com taxa, caso o campo **"Taxa mensal de Administradora"** da aba [Características](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abacaractersticas) da tela [Cadastro de Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abacaractersticas) esteja preenchido.
- Se a data de validade do cartão estiver vencida, o sistema não permitirá a autorização e emitirá o seguinte erro:

**"O cartão 'xxxxxxxxxxxxxxxxxxx' está com data de validade expirada".**

Após você confirmar a autorização através do botão **"Confirmar autorização"**, as parcelas geradas entram no financeiro como despesas/receitas confirmadas e relacionadas ao **"Número Único do cartão"**.

Abaixo falaremos sobre os campos desta tela.

O campo **"Lojista"**, refere-se ao parceiro do usuário B2B logado.

O **"Tipo de negociação"** é o utilizado para registrar a venda realizada no cartão ou no CPF do cliente.

Informe o **"Valor total"** e a **"Data da venda"**.

**Notas:**

1. Somente usuário em modo não B2B tem visível o campo Data da venda;
2. A data de negociação (data da venda) não pode ser maior que a data atual;
3. A propriedade de permissão de usuário **"Permite autorizações retroativas"** permitirá ou não lançamentos/autorização retroativos no campo Data da venda, ou seja, se você tiver permissão, poderá alterar a Data da venda; se não tiver permissão, essa data ficará desabilitada e apresentando a Data atual do sistema, não permitindo alteração.

**Botões da tela**

Acionando o botão **![Imagem 4: Acionando o botão "Gerar Parcelas" , o sistema gerará as parcelas de acordo com a quantidade negociada no Tipo de…](https://ajuda.sankhya.com.br/hc/article_attachments/16106821297943) "Gerar Parcelas"**, o sistema gerará as parcelas de acordo com a quantidade negociada no Tipo de Negociação.

O botão ![Imagem 5: O botão "Confirmar autorização" confirma a compra realizada. Ao confirmar, o sistema emitirá a seguinte informação:](https://ajuda.sankhya.com.br/hc/article_attachments/16106851939991) **"Confirmar autorização"**confirma a compra realizada. Ao confirmar, o sistema emitirá a seguinte informação:

**"Autorização realizada com sucesso! O número único da autorização é xxxxxx."**

**Observação:** pode acontecer de, quando você solicitar a confirmação das parcelas, o sistema emitir a seguinte mensagem de erro:

**"Entre em contato com a Administradora".**

Esta mensagem, geralmente é apresentada quando existir as seguintes situações:

- O Parceiro está bloqueado para venda a prazo;
- Parceiro sem limite de crédito para realizar a compra;
- Existência de títulos de receitas em atraso para este parceiro.

**Nota:**verifique também a tolerância para inadimplência do mesmo.
