---
id: "35384537690903"
titulo: "853 Rejeição: Dados de cobrança não devem ser informados para pagamento à vista"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35384537690903-853-Rejei%C3%A7%C3%A3o-Dados-de-cobran%C3%A7a-n%C3%A3o-devem-ser-informados-para-pagamento-%C3%A0-vista"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T14:25:13Z"
rotulos: ["Configuração", "NF-e", "XML", "SEFAZ", "TOP", "Financeiro", "853 Rejeição", "Rejeição 853", "pagamento à vista", "\"Tipo Negociação\" está como \"A vista\"", "pagamento à vista como Dinheiro ou Pix", "Tipo de título\" selecione uma condição que seja condizente com pagamento à vista", "853 Rejeição: Dados de cobrança não devem ser informados para pagamento à vista", "Dados de cobrança não devem ser informados para pagamento à vista", "Dados de cobrança não devem ser informados"]
---

# 853 Rejeição: Dados de cobrança não devem ser informados para pagamento à vista

**MENSAGEM:**

853 Rejeição: Dados de cobrança não devem ser informados para pagamento à vista

**SOLUÇÃO:**

### Identifique o Tipo de Operação:

**(1)** Acesse o **Portal de Vendas ou Compras**, selecione a **nota que recebeu a rejeição**.

**(2)** Na nota rejeitada, veja no cabeçalho o **"Tipo de operação"** que está sendo usado.

**(3)** Em seguida, acesse a tela **'Tipos de Operação"** e verifique se a TOP usada na nota está adequada para operação em questão. Caso não esteja, faça o devido ajuste.

### Configure a condição de pagamento:

**(1)** Ainda na nota rejeitada, veja se o campo **"Tipo Negociação"** está como **"A vista".** Caso esteja e o **pagamento realmente seja à vista, realize os ajustes abaixo:**

![Imagem 1: (1) Ainda na nota rejeitada, veja se o campo "Tipo Negociação" está como "A vista". Caso esteja e o pagamento realmente…](https://ajuda.sankhya.com.br/hc/article_attachments/35391907929495)

**(2)** Vá até a aba **"Financeiro"** e, no campo **"Tipo de título",** selecione uma condição que seja condizente com pagamento à vista como, **Dinheiro ou Pix;**

![Imagem 2: (2) Vá até a aba "Financeiro" e, no campo "Tipo de título", selecione uma condição que seja condizente com pagamento à…](https://ajuda.sankhya.com.br/hc/article_attachments/35391907934743)

**(3)** **Também na aba Financeiro garanta que:**

- a operação tenha apenas **uma parcela;**

![Imagem 3: a operação tenha apenas uma parcela;](https://ajuda.sankhya.com.br/hc/article_attachments/35391923362327)

- e a data de **vencimento esteja igual** a data de **emissão.**

![Imagem 4: e a data de vencimento esteja igual a data de emissão.](https://ajuda.sankhya.com.br/hc/article_attachments/35391923367063)

### Configure a condição de pagamento:

**(1)** Ainda nota rejeitada, na aba Financeiro, acesse a **"Movimentação financeira"** dela e garanta que o campo **"Nro Duplicata"** esteja vazio. Não informe um número de duplicata para operações à vista.

![Imagem 5: (1) Ainda nota rejeitada, na aba Financeiro, acesse a "Movimentação financeira" dela e garanta que o campo "Nro…](https://ajuda.sankhya.com.br/hc/article_attachments/35392051176471)![Imagem 6: (1) Ainda nota rejeitada, na aba Financeiro, acesse a "Movimentação financeira" dela e garanta que o campo "Nro…](https://ajuda.sankhya.com.br/hc/article_attachments/35392066735255)

**(2)**  E caso haja duplicatas ligadas a nota, remova todas elas.

### Ajuste de parâmetro

**(1)** Por fim, acesse a tela **"Preferências"** e desabilite o parâmetro **"ESCDETDUPLNFE - Esconder detalhes do campo Fatura/Duplicata na NFE".**

**Observação:** o **parâmetro** foi **criado como paliativo até que fosse concluída a entrada da nota técnica**. No entanto, **ao utilizá-lo, o sistema deixa de levar para o XML e para o DANFE informações de operações a prazo**, nas quais esses dados são obrigatórios.

Por isso, é fundamental **manter o sistema atualizado** para as **versões** que já **contemplam as implementações da NT 2025.001**, **eliminando** a necessidade de **usar o parâmetro ESCDETDUPLNFE.**

**As versões adequadas são:**

- 4.31b179
- 4.32b160
- 4.33b159
- 4.34b193
- 4.35B159

**CAUSA:**

Essa rejeição ocorre quando a NF-e está configurada com pagamento à vista (campo <indPag> = 0). No entanto, o **XML enviado contém o grupo de cobrança (<cobr>, <dup>), ou duplicatas com vencimento igual à data de emissão.**

A Sefaz considera que, **para pagamento à vista, não se deve informar dados de parcelamento, duplicatas ou vencimentos.**

**Ou seja**: se a nota é “à vista”, não se pode misturar com dados de cobrança (duplicatas, vencimentos, etc.).
