---
id: "37229430990359"
titulo: "E0004 Rejeição: Conteúdo do identificador informado na DPS difere da concatenação dos campos correspondentes."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37229430990359-E0004-Rejei%C3%A7%C3%A3o-Conte%C3%BAdo-do-identificador-informado-na-DPS-difere-da-concatena%C3%A7%C3%A3o-dos-campos-correspondentes"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:14:03Z"
rotulos: ["Fiscal", "SEFAZ", "Rejeição", "Erro", "Declaração de Prestação de Serviços (DPS)", "identificador (chave de acesso)", "identificador informado na DPS difere da concatenação", "Conteúdo do identificador informado na DPS"]
---

# E0004 Rejeição: Conteúdo do identificador informado na DPS difere da concatenação dos campos correspondentes.

**MENSAGEM:**

E0004 Rejeição: Conteúdo do identificador informado na DPS difere da concatenação dos campos correspondentes.

**SITUAÇÃO:**

Ao emitir uma **Declaração de Prestação de Serviços (DPS)**, o sistema gerou um **identificador (chave de acesso)** que não corresponde à concatenação correta dos campos que compõem essa chave. Ao tentar transmitir o documento para a SEFAZ, a validação identificou essa **inconsistência entre o identificador informado e os dados do documento**, resultando na rejeição E0004.

**SOLUÇÃO**

Para corrigir a rejeição E0004, siga os passos abaixo:

**(1)** Realize a **consulta da chave da DPS** gerada nos **Portais Nacional e Estadual da SEFAZ**, certificando-se de que o documento não foi recebido ou autorizado:

- **SEFAZ Nacional:** Acesse o portal nacional da SEFAZ e selecione a opção **''Serviços Consultar DPS''**.
- **SEFAZ Estadual:** Acesse o portal estadual da SEFAZ, selecione **"Portais Estaduais"**, escolha o **estado da empresa emissora** e busque pelo serviço de ''**Consulta de documentos/chave''**.

**(2)** Caso a consulta retorne a chave como **"Inexistente"** em ambos os portais e o status da DPS esteja como **"Aguardando Correção"**, proceda com a **inutilização e exclusão** do documento rejeitado.

**(3)** Emita uma **nova DPS**, onde a chave de acesso será gerada automaticamente conforme os **dados atuais e corretos** do documento.

**CAUSA:**

Esta rejeição ocorre quando o **identificador (chave de acesso) informado na DPS** não corresponde à **concatenação correta dos campos** que compõem essa chave, como código da UF, data de emissão, CNPJ do emitente, modelo do documento, série, número, tipo de emissão e código numérico. Essa divergência pode ser causada por **inconsistências nos dados cadastrais**, **erros no momento da geração da chave** ou **alterações nos campos após a geração do identificador**.
