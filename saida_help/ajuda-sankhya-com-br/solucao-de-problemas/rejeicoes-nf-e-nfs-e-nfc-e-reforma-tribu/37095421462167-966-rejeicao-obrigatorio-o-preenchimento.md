---
id: "37095421462167"
titulo: "966 Rejeição: Obrigatório o preenchimento da origem da mercadoria [nItem:nnn]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37095421462167-966-Rejei%C3%A7%C3%A3o-Obrigat%C3%B3rio-o-preenchimento-da-origem-da-mercadoria-nItem-nnn"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:21:43Z"
rotulos: ["Produtos", "Configuração", "Fiscal", "NF-e", "XML", "SEFAZ", "Nota Fiscal Eletrônica (NF-e)", "Nota Fiscal de Consumidor Eletrônica (NFC-e)", "Origem de Mercadoria", "Legislação fiscal brasileira", "reforma Tributária (Lei Complementar nº 214/2025)", "Origem da mercadoria está vazio ou não foi preenchido"]
---

# 966 Rejeição: Obrigatório o preenchimento da origem da mercadoria [nItem:nnn]

**MENSAGEM**

966 Rejeição: Obrigatório o preenchimento da origem da mercadoria [nItem:nnn]

**SITUAÇÃO**

A NF-e ou NFC-e foi emitida com um ou mais itens do documento fiscal sem a informação da origem da mercadoria devidamente registrada, resultando na rejeição da nota pelo sistema.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela de **"Produtos"** (Configurações » Cadastros » Produtos » Produtos).

**(2)** Localize o produto que está apresentando a rejeição. O número do item com problema é indicado na mensagem de erro [nItem:nnn].

**(3)** Na aba **"Fiscal"**, verifique o campo **"Origem da Mercadoria"** e selecione a opção adequada conforme a procedência do produto:

- **0 – Nacional:** exceto as indicadas nos códigos 3, 4, 5 e 8.
- **1 – Estrangeira – Importação direta:** exceto a indicada no código 6.
- **2 – Estrangeira – Adquirida no mercado interno:** exceto a indicada no código 7.
- **3 – Nacional:** mercadoria ou bem com **Conteúdo de Importação superior a 40% e inferior ou igual a 70%**.
- **4 – Nacional:** produção realizada em conformidade com os **Processos Produtivos Básicos (PPB)**.
- **5 – Nacional:** mercadoria ou bem com **Conteúdo de Importação inferior ou igual a 40%**.
- **6 – Estrangeira – Importação direta:** sem similar nacional, constante em lista da **CAMEX**.
- **7 – Estrangeira – Adquirida no mercado interno:** sem similar nacional, constante em lista da **CAMEX**.
- **8 – Nacional:** mercadoria ou bem com **Conteúdo de Importação superior a 70%**.

**(4)** Salve as alterações no cadastro do produto.

**(5)** Retorne à tela de emissão da nota fiscal e gere um novo lote para transmissão.

**CAUSA**

A rejeição ocorre porque a legislação fiscal brasileira exige que seja informada a origem da mercadoria em todos os itens da nota fiscal.

Esta informação é fundamental para a correta aplicação da tributação, especialmente com a implementação da Reforma Tributária (Lei Complementar nº 214/2025), que estabelece diferentes alíquotas para o IBS (Imposto sobre Bens e Serviços) e CBS (Contribuição sobre Bens e Serviços) de acordo com a origem do produto.

A origem da mercadoria é um campo obrigatório que deve ser preenchido no cadastro do produto e transmitido no XML da nota fiscal. Quando este campo não é informado, a SEFAZ rejeita o documento fiscal, impedindo sua autorização.
