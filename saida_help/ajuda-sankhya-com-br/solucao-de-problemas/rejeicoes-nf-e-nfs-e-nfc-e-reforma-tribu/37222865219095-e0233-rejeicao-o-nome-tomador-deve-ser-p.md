---
id: "37222865219095"
titulo: "E0233 Rejeição: O nome tomador deve ser preenchido obrigatoriamente quando o NIF do tomador for preenchido."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37222865219095-E0233-Rejei%C3%A7%C3%A3o-O-nome-tomador-deve-ser-preenchido-obrigatoriamente-quando-o-NIF-do-tomador-for-preenchido"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:17:19Z"
rotulos: ["Configuração", "Parceiro", "NF-e", "SEFAZ", "NFS-e", "NIF (Número de Identificação Fiscal)", "Identificação de Estrangeiro", "Nome do tomador seja obrigatoriamente preenchido", "NF-e ou NFS-e", "Nome tomador deve ser preenchido obrigatoriamente", "Tomador estrangeiro"]
---

# E0233 Rejeição: O nome tomador deve ser preenchido obrigatoriamente quando o NIF do tomador for preenchido.

**MENSAGEM**

E0233 Rejeição: O nome tomador deve ser preenchido obrigatoriamente quando o NIF do tomador for preenchido.

**SITUAÇÃO**

Ao gerar o lote de uma **NF-e ou NFS-e** com um tomador estrangeiro, o sistema apresenta a mensagem de rejeição informando que o **nome do tomador não foi preenchido**, mesmo que o **NIF (Número de Identificação Fiscal)** tenha sido informado no cadastro.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o parceiro tomador estrangeiro que está sendo utilizado na nota fiscal.

**(2)** Na aba **"Identificação"**, verifique se o campo **"Identificação de Estrangeiro"** está preenchido com o código **"NIF"**.

**(3)** Certifique-se de que o campo **"Nome"** ou **"Razão Social"** do parceiro esteja **devidamente preenchido** com o nome completo do tomador estrangeiro.

**(4)** Salve as alterações realizadas no cadastro do parceiro.

**(5)** Retorne à nota fiscal, **redigite o parceiro tomador** ou **fature novamente** a operação para que o sistema capture as informações atualizadas do cadastro.

**(6)** Gere o lote novamente e transmita a nota fiscal.

**CAUSA**

A rejeição ocorre quando o documento fiscal possui um **tomador estrangeiro** com o campo **"Identificação de Estrangeiro"** preenchido com **"NIF"**, porém o campo **"Nome"** ou **"Razão Social"** do parceiro **não está preenchido** ou está em branco. A Sefaz exige que, ao informar o NIF de um tomador estrangeiro, o **nome do tomador seja obrigatoriamente preenchido** para validação e identificação correta da operação fiscal.
