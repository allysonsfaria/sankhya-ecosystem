---
id: "37221450007447"
titulo: "E0018 Rejeição: A data de competência informada na DPS deve ser igual ou posterior à data de inscrição do CNPJ do emitente no cadastro CNPJ."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37221450007447-E0018-Rejei%C3%A7%C3%A3o-A-data-de-compet%C3%AAncia-informada-na-DPS-deve-ser-igual-ou-posterior-%C3%A0-data-de-inscri%C3%A7%C3%A3o-do-CNPJ-do-emitente-no-cadastro-CNPJ"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:18:40Z"
rotulos: ["Configuração", "Fiscal", "SEFAZ", "Erro", "Declaração de Prestação de Serviços (DPS)", "Data de competência informada é anterior à data de inscrição do CNPJ", "Cadastro da Receita Federal", "Data de inscrição do CNPJ do emitente no cadastro CNPJ"]
---

# E0018 Rejeição: A data de competência informada na DPS deve ser igual ou posterior à data de inscrição do CNPJ do emitente no cadastro CNPJ.

**MENSAGEM**

E0018 Rejeição: A data de competência informada na DPS deve ser igual ou posterior à data de inscrição do CNPJ do emitente no cadastro CNPJ.

**SITUAÇÃO**

Ao emitir uma **Declaração de Prestação de Serviços (DPS)**, o documento é rejeitado pela Sefaz com a mensagem de erro E0018, indicando que a **data de competência informada** é anterior à data de inscrição do CNPJ do emitente no cadastro da Receita Federal.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Verifique a **data de inscrição do CNPJ** do emitente no cadastro da Receita Federal, acessando o site oficial da Receita Federal ou consultando o Cartão CNPJ da empresa.

**(2)** Acesse a tela **''Empresas''** (Configurações » Cadastros » Empresas).

**(3)** Na aba **''Geral''**, verifique se a **data de inscrição do CNPJ** está corretamente registrada.

**(4)** Verifique a **data de competência** informada na DPS que está sendo emitida. Esta data deve ser **igual ou posterior** à data de inscrição do CNPJ do emitente.

**(5)** Caso a data de competência esteja incorreta, ajuste-a para uma data válida (igual ou posterior à data de inscrição do CNPJ).

**(6)** Após realizar os ajustes necessários, reenvie a DPS para a Sefaz.

**CAUSA**

A rejeição ocorre quando a **data de competência informada na DPS** é anterior à **data de inscrição do CNPJ** do emitente no cadastro da Receita Federal. A Sefaz valida se o CNPJ já estava ativo na data de competência declarada, impedindo a emissão de documentos fiscais com datas anteriores à existência legal da empresa.
