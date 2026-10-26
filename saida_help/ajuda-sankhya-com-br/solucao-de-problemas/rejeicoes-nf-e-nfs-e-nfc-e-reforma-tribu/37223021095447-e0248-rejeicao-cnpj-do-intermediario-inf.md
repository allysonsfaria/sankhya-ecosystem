---
id: "37223021095447"
titulo: "E0248 Rejeição: CNPJ do intermediário informado na DPS é inválido."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37223021095447-E0248-Rejei%C3%A7%C3%A3o-CNPJ-do-intermedi%C3%A1rio-informado-na-DPS-%C3%A9-inv%C3%A1lido"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:17:08Z"
rotulos: ["Configuração", "Fiscal", "Parceiro", "SEFAZ", "Erro", "CNPJ do intermediário informado na DPS está preenchido incorretamente", "CNPJ do intermediário informado na DPS", "Transmissão da DPS (Documento Preliminar de Serviços)", "Documento fiscal está preenchido com zeros nulo ou com dígito verificador (DV) inválido"]
---

# E0248 Rejeição: CNPJ do intermediário informado na DPS é inválido.

**MENSAGEM**

E0248 Rejeição: CNPJ do intermediário informado na DPS é inválido.

**SITUAÇÃO**

A mensagem de rejeição é apresentada durante a **transmissão da DPS** (Documento Preliminar de Serviços) quando o **CNPJ do intermediário** informado no documento fiscal está **preenchido com zeros, nulo ou com dígito verificador (DV) inválido**.

**SOLUÇÃO**

**(1)** Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros).

**(2)** Localize o **cadastro do intermediário** vinculado à operação.

**(3)** Na aba **"Identificação"**, verifique o campo **"CNPJ / CPF"** e certifique-se de que:

- O CNPJ está **preenchido corretamente**, sem zeros;
- O **dígito verificador (DV) está válido**;
- O CNPJ está **ativo e habilitado** na Receita Federal.

**(4)** Caso necessário, **consulte o CNPJ correto** do intermediário no site da Receita Federal ou no SINTEGRA e ajuste o cadastro do parceiro.

**(5)** Salve as alterações realizadas no cadastro do parceiro.

**(6)** Retorne ao documento fiscal (DPS), **redigite o cabeçalho** para atualizar as informações do intermediário e **transmita novamente** o lote. 

**CAUSA**

A rejeição ocorre quando o **CNPJ do intermediário** informado na DPS está **preenchido incorretamente** no cadastro de parceiros, seja com **zeros, nulo ou com dígito verificador inválido**. A SEFAZ valida o CNPJ durante a transmissão do documento e, ao identificar inconsistências, retorna a mensagem de rejeição **E0248**.
