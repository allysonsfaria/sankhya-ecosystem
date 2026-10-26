---
id: "37225909194391"
titulo: "E0492 Rejeição: O grupo de informações de endereço nacional deve ser informado obrigatoriamente quando o fornecedor for identificado pelo CPF ou CNPJ."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37225909194391-E0492-Rejei%C3%A7%C3%A3o-O-grupo-de-informa%C3%A7%C3%B5es-de-endere%C3%A7o-nacional-deve-ser-informado-obrigatoriamente-quando-o-fornecedor-for-identificado-pelo-CPF-ou-CNPJ"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:15:31Z"
rotulos: ["Configuração", "Parceiro", "NF-e", "SEFAZ", "Erro", "CPF ou CNPJ", "Dados de endereço incompletos ou ausentes", "Grupo de informações de endereço nacional", "nota fiscal rejeitada", "Endereço nacional", "Documentos Eletrônicos"]
---

# E0492 Rejeição: O grupo de informações de endereço nacional deve ser informado obrigatoriamente quando o fornecedor for identificado pelo CPF ou CNPJ.

**MENSAGEM**

E0492 Rejeição: O grupo de informações de endereço nacional deve ser informado obrigatoriamente quando o fornecedor for identificado pelo CPF ou CNPJ.

**SITUAÇÃO**

Ao emitir uma NF-e ou NFC-e, o documento foi rejeitado porque o fornecedor (destinatário ou emitente) possui CPF ou CNPJ cadastrado, mas o endereço nacional não foi informado.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros).

**(2)** Localize o cadastro do **fornecedor** que está sendo utilizado na nota fiscal rejeitada.

**(3)** Acesse a aba **"Identificação"** e verifique se os campos **"CNPJ"** ou **"CPF"** estão preenchidos corretamente.

**(3)** Acesse a aba **"Endereço"** e preencha **obrigatoriamente** as seguintes informações do endereço nacional:

- **"Logradouro"**: informe o nome da rua, avenida ou logradouro.
- **"Número"**: informe o número do endereço.
- **"Bairro"**: informe o bairro.
- **"Município"**: selecione o município.
- **"UF"**: selecione a Unidade Federativa (Estado).
- **"CEP"**: informe o Código de Endereçamento Postal.

**(4)** Caso o endereço possua **complemento**, preencha também o campo **"Complemento"** com informações adicionais (apartamento, sala, bloco, etc.).

**(5)** Salve as alterações.

**(6)** Retorne à **nota fiscal rejeitada** e tente realizar a **transmissão novamente** para a SEFAZ.

**CAUSA**

A rejeição ocorre porque a **SEFAZ exige que o grupo de informações de endereço nacional seja preenchido obrigatoriamente** quando o fornecedor (destinatário ou emitente) for identificado por **CPF ou CNPJ**. Caso o cadastro do parceiro esteja com **dados de endereço incompletos ou ausentes**, o documento fiscal não será aceito pela SEFAZ, resultando na rejeição E0492.
