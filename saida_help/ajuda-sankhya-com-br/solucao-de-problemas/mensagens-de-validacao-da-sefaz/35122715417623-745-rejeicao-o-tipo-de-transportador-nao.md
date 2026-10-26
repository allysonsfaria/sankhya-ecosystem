---
id: "35122715417623"
titulo: "745 Rejeição: O tipo de transportador não pode ser informado quando não estiver informado proprietário do veículo de tração"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35122715417623-745-Rejei%C3%A7%C3%A3o-O-tipo-de-transportador-n%C3%A3o-pode-ser-informado-quando-n%C3%A3o-estiver-informado-propriet%C3%A1rio-do-ve%C3%ADculo-de-tra%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T14:25:59Z"
rotulos: ["ERROMDFE", "MDF-e", "Configuração", "Parceiro", "Transporte", "745 Rejeição", "Rejeição 745", "O tipo de transportador não pode ser informado", "quando não estiver informado proprietário do veículo de tração", "Documentos Eletrônicos"]
---

# 745 Rejeição: O tipo de transportador não pode ser informado quando não estiver informado proprietário do veículo de tração

**MENSAGEM**

745 Rejeição: O tipo de transportador não pode ser informado quando não estiver informado proprietário do veículo de tração

**SITUAÇÃO**

Ao emitir um MDF-e (modelo 58) com modal rodoviário, o usuário preencheu o campo **"Tipo de Transportador"** sem informar o grupo **"Proprietário do Veículo de Tração"**. A mensagem de rejeição foi apresentada durante a validação do documento.

**SOLUÇÃO**

**(1)**  Quando for emitido um **MDF-e cujo o veículo informado seja de propriedade da empresa emitente** **do MDF-e**, não poderá ser gerado a TAG: <tpTransp>. Para isso, acesse a tela **"Veículos"** (Configurações » Cadastros » Veículos), na aba **"Propriedades"**, marque a opção **"Veículo da empresa"** se o veículo for de propriedade da empresa emitente.

**(2)**  Caso o **veículo não seja da empresa emitente**, desmarque a opção **"Veículo da empresa"** e preencha o campo **"Parceiro ou Empresa"**.

![Imagem 1: (1) Quando for emitido um MDF-e cujo o veículo informado seja de propriedade da empresa emitente do MDF-e , não poderá…](https://ajuda.sankhya.com.br/hc/article_attachments/35712533179287)

**Observação:** caso seja preciso, para gerar o grupo de Tag **<prop>**, o veículo não pode ser da empresa emitente. Neste caso, desabilite o campo **"Veículo da empresa"** e preencha **"Parceiro ou Empresa"**.

![Imagem 2: Observação: caso seja preciso, para gerar o grupo de Tag <prop> , o veículo não pode ser da empresa emitente. Neste…](https://ajuda.sankhya.com.br/hc/article_attachments/35712533179799)

**CAUSA**

A rejeição ocorre quando, ao emitir um MDF-e (modelo 58) com modal rodoviário, o campo **"Tipo de Transportador"** é preenchido sem informar o grupo **"Proprietário do Veículo de Tração"** (**Tag: prop**). O sistema exige que, para informar o tipo de transportador, o proprietário do veículo de tração também seja informado.
