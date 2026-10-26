---
id: "37222592721559"
titulo: "E0188 Rejeição: CNPJ do tomador informado na DPS é inválido."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37222592721559-E0188-Rejei%C3%A7%C3%A3o-CNPJ-do-tomador-informado-na-DPS-%C3%A9-inv%C3%A1lido"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:17:40Z"
rotulos: ["Configuração", "Parceiro", "SEFAZ", "Erro", "Reforma Tributária", "Lei Complementar nº 214/2025", "Documento Fiscal Eletrônico (DPS)", "CNPJ do tomador do serviço", "CNPJ do tomador informado no Documento Fiscal Eletrônico"]
---

# E0188 Rejeição: CNPJ do tomador informado na DPS é inválido.

**MENSAGEM**

E0188 Rejeição: CNPJ do tomador informado na DPS é inválido.

**SITUAÇÃO**

Ao emitir um **Documento Fiscal Eletrônico (DPS)** no contexto da **Reforma Tributária**, o usuário informou o **CNPJ do tomador** do serviço ou da operação com **dados inválidos**. A SEFAZ validou o documento e identificou que o CNPJ apresenta **zeros, está nulo ou possui dígito verificador (DV) incorreto**, resultando na rejeição do documento.

**SOLUÇÃO**

Para corrigir a rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o **cadastro do tomador** informado no documento fiscal.

**(2)** Verifique o campo **"CNPJ"** do parceiro e certifique-se de que:

- O CNPJ **não está preenchido com zeros** (exemplo: 00000000000000);
- O CNPJ **não está vazio ou nulo**;
- O **dígito verificador (DV) está correto**.

**(3)** Caso o CNPJ esteja incorreto, **consulte o CNPJ correto** do tomador no site da **Receita Federal** ou no **SINTEGRA** do estado correspondente.

**(4)** Atualize o campo **"CNPJ"** no cadastro do parceiro com as **informações corretas** e salve as alterações.

**(5)** Certifique-se de que a **situação cadastral do parceiro** está **Ativa/Habilitada** na Receita Federal.

**(6)** Retorne ao **documento fiscal rejeitado**, redigite o cabeçalho da nota e **gere um novo lote** para transmissão à SEFAZ.

**OBSERVAÇÃO:** Para parceiros **estrangeiros**, certifique-se de preencher corretamente o parâmetro **"Código do País Brasil" [CODPAISBRASIL]** com o valor **[55]**.

**CAUSA**

A rejeição ocorre quando o **CNPJ do tomador** informado no **Documento Fiscal Eletrônico (DPS)** apresenta uma das seguintes situações:

- CNPJ preenchido com **zeros** (exemplo: 00000000000000);
- CNPJ **nulo ou vazio**;
- **Dígito verificador (DV) inválido**, indicando erro de digitação ou inconsistência cadastral.

Conforme as **regras de validação da SEFAZ** estabelecidas pela **Lei Complementar nº 214/2025** no contexto da **Reforma Tributária**, o CNPJ do tomador deve ser **válido e estar corretamente cadastrado** para que o documento fiscal seja aceito.
