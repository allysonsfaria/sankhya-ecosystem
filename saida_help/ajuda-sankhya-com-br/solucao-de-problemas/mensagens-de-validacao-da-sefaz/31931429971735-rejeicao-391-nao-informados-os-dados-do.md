---
id: "31931429971735"
titulo: "Rejeição 391: não informados os dados do cartão de crédito/débito nas formas de pagamento da nota fiscal"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31931429971735-Rejei%C3%A7%C3%A3o-391-n%C3%A3o-informados-os-dados-do-cart%C3%A3o-de-cr%C3%A9dito-d%C3%A9bito-nas-formas-de-pagamento-da-nota-fiscal"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-10-02T12:21:16Z"
rotulos: ["Configuração", "NF-e", "XML", "SEFAZ", "Financeiro", "Pagamento", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Rejeição 391", "não informados os dados do cartão de crédito", "débito nas Formas de Pagamento da Nota Fiscal", "Artigo atualizado KCS", "Docs Eletrônicos - KCS"]
---

# Rejeição 391: não informados os dados do cartão de crédito/débito nas formas de pagamento da nota fiscal

Rejeição 391: não informados os dados do cartão de crédito / débito nas formas de pagamento da nota fiscal.

**Situação:**

A Rejeição 391 ocorre quando uma NFC-e ou NF-e é transmitida com forma de pagamento configurada como cartão de crédito ou débito, mas os dados complementares não foram informados corretamente no XML. Esta validação segue a Nota Técnica 2015.002.

### SOLUÇÃO

Para resolver esta rejeição, siga os passos abaixo:

### Configurar corretamente os tipos de título

**(1)** Acesse a tela **"Tipos de título"** (Financeiro >> Arquivos >> Cadastros >> Tipos de Título) e localize o tipo de título utilizado nas vendas.

**(2)** No campo **"Tipo de pgto para NFC-e / NF-e / CF-e"**, selecione uma das seguintes opções:

- 03 – Cartão de crédito
- 04 – Cartão de débito
- 17 – PIX (Pagamento instantâneo)

**Importante:** ao inserir ou alterar um tipo de título com subtipo **"Cartão de débito"** ou **"Cartão de crédito"**, o campo **"Parc. Administradora"** deverá ser preenchido com o código do parceiro responsável pela administração dos pagamentos com cartão.
Esse parceiro deve:

- Estar cadastrado no sistema;
- Ter um **"CNPJ válido"** correspondente à empresa administradora (exemplos: **"Cielo"**, **"Redecard"**, **"Hipercard"**).

**Observação:** Para o caso de **“PIX POS”**, não é necessário preencher o campo **“Parc. Administradora”**. Além disso, é necessário marcar a opção **“Utiliza POS”** para que o sistema identifique que não há integração direta com o Sankhya e, assim, gere a tag `<tpIntegra>` com o valor 2.

![Imagem 1: Observação: Para o caso de “PIX POS” , não é necessário preencher o campo “Parc. Administradora” . Além disso, é…](https://ajuda.sankhya.com.br/hc/article_attachments/39889544952727)

### Ativar a Nota Técnica 2023.004

**(1)** Acesse a tela **"Empresa"** (Comercial >> Preferências >> Empresa), vá até a aba **"Documentos Fiscais Eletrônicos"**, depois à sub-aba **"NF-e/NFC-e"**, em seguida à sub-aba **"Nota Técnica NF-e"** e ative as opções  **de Notas Técnicas**.

- Nota Técnica 2023.004 - v.1.11

**Informações Técnicas Adicionais:**

Conforme a NT 2015.002, deve ser informado o tipo de integração (tag <tpIntegra>): 1 (integrado) ou 2 (não integrado). Se for do tipo 1, devem ser informados o CNPJ da credenciadora e o código de autenticação (<cAut>).

Após realizar essas configurações, a emissão da NF-e ou NFC-e com pagamento via cartão deverá ser processada corretamente, sem gerar rejeições.
