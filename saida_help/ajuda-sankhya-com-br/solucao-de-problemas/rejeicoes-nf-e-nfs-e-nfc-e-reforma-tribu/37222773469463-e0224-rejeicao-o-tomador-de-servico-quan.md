---
id: "37222773469463"
titulo: "E0224 Rejeição: O tomador de serviço, quando emitente da DPS, somente pode ser identificado pelo CNPJ ou CPF."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37222773469463-E0224-Rejei%C3%A7%C3%A3o-O-tomador-de-servi%C3%A7o-quando-emitente-da-DPS-somente-pode-ser-identificado-pelo-CNPJ-ou-CPF"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:17:26Z"
rotulos: ["Configuração", "Parceiro", "SEFAZ", "NFS-e", "Erro", "Documento de Prestação de Serviços (DPS)", "Identificação de Estrangeiro", "Tomador do serviço", "Tomador foi preenchido com informações diferentes de CNPJ ou CPF"]
---

# E0224 Rejeição: O tomador de serviço, quando emitente da DPS, somente pode ser identificado pelo CNPJ ou CPF.

**MENSAGEM**

E0224 Rejeição: O tomador de serviço, quando emitente da DPS, somente pode ser identificado pelo CNPJ ou CPF.

**SITUAÇÃO**

Ao emitir um **Documento de Prestação de Serviços (DPS)** em que a própria empresa é o **tomador do serviço**, o sistema identifica que o tomador foi preenchido com informações diferentes de **CNPJ ou CPF**, como por exemplo, utilizando o campo **"Identificação de Estrangeiro"**. Nesta situação, a Sefaz rejeita o documento com a mensagem E0224.

**SOLUÇÃO**

Para corrigir a rejeição E0224, siga os passos abaixo:

**(1)** Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros).

**(2)** Localize e selecione o **parceiro** que está cadastrado como **tomador do serviço** no DPS rejeitado.

**(3)** Na aba **"Identificação"**, verifique se o campo **"Identificação de Estrangeiro"** está preenchido.

**(4)** Caso o tomador seja uma **pessoa jurídica brasileira**, certifique-se de que o campo **"CNPJ / CPF"** esteja corretamente preenchido e remova qualquer informação do campo "Identificação de Estrangeiro".

**(5)** Caso o tomador seja uma **pessoa física brasileira**, certifique-se de que o campo **"CNPJ / CPF"** esteja corretamente preenchido e remova qualquer informação do campo "Identificação de Estrangeiro".

**(6)** Salve as alterações realizadas no cadastro do parceiro.

**(7)** Retorne ao **DPS** e atualize os dados do tomador, ou exclua o documento e emita novamente com as informações corretas.

**CAUSA**

A rejeição ocorre porque a **Sefaz exige** que, quando a empresa emitente do DPS for também o **tomador do serviço**, este deve ser identificado exclusivamente por **CNPJ ou CPF**. A utilização de outros tipos de identificação, como o campo **"Identificação de Estrangeiro"**, não é permitida neste cenário, resultando na rejeição do documento fiscal.
