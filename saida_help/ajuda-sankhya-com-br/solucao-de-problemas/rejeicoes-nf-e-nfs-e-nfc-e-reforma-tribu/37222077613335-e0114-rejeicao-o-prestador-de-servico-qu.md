---
id: "37222077613335"
titulo: "E0114 Rejeição: O prestador de serviço, quando emitente da DPS, somente pode ser identificado pelo CNPJ ou CPF."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37222077613335-E0114-Rejei%C3%A7%C3%A3o-O-prestador-de-servi%C3%A7o-quando-emitente-da-DPS-somente-pode-ser-identificado-pelo-CNPJ-ou-CPF"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:18:07Z"
rotulos: ["Configuração", "SEFAZ", "Erro", "Lei Complementar nº 214/2025", "Declaração de Prestação de Serviços (DPS)", "Prestador de serviço identificado como emitente", "CNPJ ou CPF válido informado no cadastro", "Inconsistência nos dados de identificação do emitente", "Prestador de serviço", "CNPJ válido"]
---

# E0114 Rejeição: O prestador de serviço, quando emitente da DPS, somente pode ser identificado pelo CNPJ ou CPF.

**MENSAGEM**

E0114 Rejeição: O prestador de serviço, quando emitente da DPS, somente pode ser identificado pelo CNPJ ou CPF.

**SITUAÇÃO**

Ao emitir uma **Declaração de Prestação de Serviços (DPS)**, o sistema apresenta a rejeição quando o **prestador de serviço identificado como emitente** do documento não possui **CNPJ ou CPF válido** informado no cadastro, ou quando há **inconsistência nos dados de identificação** do emitente.

**SOLUÇÃO**

**(1)** Acesse a tela **"Empresas"** (Configurações » Cadastros » Empresas) e localize o **cadastro da empresa emitente** da DPS.

**(2)**  Verifique se o campo **"CNPJ / CPF''** está **preenchido corretamente** com um número válido:

- Para **Pessoa Jurídica**: certifique-se de que o **CNPJ possui 14 dígitos** e está formatado corretamente.
- Para **Pessoa Física**: certifique-se de que o **CPF possui 11 dígitos** e está formatado corretamente.

**(3)** Caso o campo esteja **vazio, incompleto ou com dados inválidos**, corrija as informações inserindo o **CNPJ ou CPF válido** do prestador de serviço.

**(4)** Salve as alterações realizadas no cadastro da empresa.

**(5)** Retorne à tela de emissão da **DPS** e tente emitir o documento novamente. 

**CAUSA**

A rejeição **E0114** ocorre devido à **validação da SEFAZ** estabelecida pela **Lei Complementar nº 214/2025**, que determina que o **prestador de serviço**, quando atua como **emitente da Declaração de Prestação de Serviços (DPS)**, deve ser **obrigatoriamente identificado** por um **CNPJ válido** (no caso de Pessoa Jurídica) ou **CPF válido** (no caso de Pessoa Física). Quando essas informações estão **ausentes, incompletas ou inválidas** no cadastro do emitente, o documento fiscal é rejeitado pela SEFAZ.
