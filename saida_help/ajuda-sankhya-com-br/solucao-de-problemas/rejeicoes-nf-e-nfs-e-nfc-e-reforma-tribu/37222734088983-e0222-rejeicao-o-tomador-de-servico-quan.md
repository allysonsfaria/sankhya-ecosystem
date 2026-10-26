---
id: "37222734088983"
titulo: "E0222 Rejeição: O tomador de serviço, quando emitente da DPS, não pode ser identificado pelo NIF."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37222734088983-E0222-Rejei%C3%A7%C3%A3o-O-tomador-de-servi%C3%A7o-quando-emitente-da-DPS-n%C3%A3o-pode-ser-identificado-pelo-NIF"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:17:31Z"
rotulos: ["Configuração", "Parceiro", "SEFAZ", "Erro", "Documento de Prestação de Serviços (DPS)", "Identificação de Estrangeiro", "Emitente da DPS", "Tomador do serviço", "NIF (Número de Identificação Fiscal de estrangeiro)"]
---

# E0222 Rejeição: O tomador de serviço, quando emitente da DPS, não pode ser identificado pelo NIF.

**MENSAGEM**

E0222 Rejeição: O tomador de serviço, quando emitente da DPS, não pode ser identificado pelo NIF.

**SITUAÇÃO**

Ao emitir um **Documento de Prestação de Serviços (DPS)**, o usuário configurou o **tomador do serviço** como sendo a própria **empresa emitente** do documento. No entanto, no **cadastro deste parceiro**, o campo **"Identificação de Estrangeiro"** foi preenchido com a opção **"NIF"** (Número de Identificação Fiscal). Ao tentar transmitir o documento para a SEFAZ, a nota foi **rejeitada** com a mensagem de erro E0222.

**SOLUÇÃO**

Para resolver esta rejeição, é necessário **ajustar o cadastro do parceiro** que está configurado como tomador do serviço. Siga os passos abaixo:

**(1)**  Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros).

**(2)**  Localize e selecione o **parceiro** que está configurado como **tomador do serviço** na DPS rejeitada.

**(3)**  Acesse a aba **"Identificação"** do cadastro do parceiro.

**(4)**  Verifique o preenchimento do campo **"Identificação de Estrangeiro"**:

- Se o tomador for uma **pessoa jurídica brasileira**, certifique-se de que este campo esteja **vazio** ou preenchido com **CNPJ válido**.
- Se o tomador for uma **pessoa física brasileira**, certifique-se de que este campo esteja **vazio** ou preenchido com **CPF válido**.
- **Remova** a identificação **"NIF"** do campo **"Identificação de Estrangeiro"**, pois quando o tomador é o próprio emitente da DPS, não é permitido utilizar identificação de estrangeiro.

**(5)**  Salve as alterações realizadas no cadastro do parceiro.

**(6)**  Retorne ao **documento fiscal** e realize uma nova tentativa de **transmissão** para a SEFAZ.

**CAUSA**

A rejeição ocorre porque a **SEFAZ não permite** que o **tomador do serviço**, quando for o **próprio emitente da DPS**, seja identificado por meio de **NIF (Número de Identificação Fiscal de estrangeiro)**. Esta validação garante que **empresas brasileiras** emitindo documentos fiscais em seu próprio nome utilizem apenas **identificações nacionais válidas**, como CNPJ ou CPF, mantendo a **conformidade fiscal** e a **integridade dos dados** no sistema tributário nacional.
