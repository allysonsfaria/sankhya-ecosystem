---
id: "42733552101271"
titulo: "Processo Adequação da NF-e à NT 2020.006"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42733552101271-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2020-006"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Notas Técnicas  > Notas Técnicas de NFe e NFCe"
atualizado_em: "2026-10-14T12:36:07Z"
rotulos: ["Nota Técnica 2020.006"]
---

# Processo Adequação da NF-e à NT 2020.006

**Caminhos de Acesso:**

- Menu Principal › Preferências › Empresa › aba NF-e/NFC-e
- Menu Principal › Tipo de Operação - TOP › aba NF-e/NFC-e/CF-e

---

## O que é e para que serve

A **Nota Técnica 2020.006** gera no XML da NF-e as tags de intermediador e presença do comprador, a partir de campos já configurados no Tipo de Operação (TOP). Ela não cadastra essas informações — apenas transporta para o XML o que está preenchido na TOP.

## O que foi alterado

Quando a opção **Última (Nota Técnica 2020.006)** é selecionada no campo **Versão da nota técnica**, as tags <indIntermed>, <indPres> e <idCadIntTran> são geradas no XML.

**Parametrizações no sistema:**

Tela **"Empresa"** (Caminho de acesso: Comercial » Preferência » Empresa):

- Aba 'NF-e' » **Campo 'Versão NT':** foi criada a opção **“(Nota Técnica 2020.006)”** que quando selecionada, trará as novas informações das tags a serem utilizadas.

Tela **"Tipos de Operação - TOP"** (Caminho de acesso: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP)

Aba **"NF-e/NFC-e"**: foi criado um campo **“Indicador de Intermediador/Marketplace"** com as seguintes opções:

- Em branco (null)
- 0 = Operação sem intermediador
- 1 = Operação em site ou plataforma de terceiros (intermediadores/marketplace)

 Esse campo tem preenchimento obrigatório quando o Indicador de presença for:

- 1 = Operação presencial;
- 2 = Operação não presencial, pela internet;
- 3 = Operação não presencial, teleatendimento;
- 4 = NFC-e em operação com entrega a domicílio;
- 9 = Operação não presencial, outros.

Aba NF-e/NFC-e : foi criado um campo **“Intermediador da Transação”** onde o usuário irá informar qual o parceiro responsável pela intermediação.

- Através do código informado, o sistema irá alimentar as novas TAGs criadas no XML: CNPJ do Intermediador da Transação e Identificador Cadastrado no Intermediador.

Esse campo tem preenchimento obrigatório quando o Indicador de Intermediador/Marketplace for igual a 1 = Operação em site ou plataforma de terceiros.

Tela **"Tipos de Títulos"** (Caminho de acesso: Financeiro » Arquivos » Cadastros » Tipos de Títulos):

**Aba Geral:** foi acrescentado no campo **“Tipo de pgto para NFC-e/NF-e/CF-e”** os seguintes códigos:

- 16 = Depósito Bancário
- 17 = Pagamento Instantâneo (PIX)
- 18 = Transferência bancária, Carteira Digital
- 19 = Programa de fidelidade, Cashback, Crédito Virtual

## Pontos de atenção

As tags são preenchidas de acordo com as informações dos campos **Indicador de Intermediador/Marketplace**, **Indicador de Presença para NF-e/NFC-e** e **Intermediador da transação**, disponíveis na tela [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114), aba NF-e/NFC-e/CF-e. Sem esses campos preenchidos na TOP, as tags saem vazias mesmo com a NT ativa.
