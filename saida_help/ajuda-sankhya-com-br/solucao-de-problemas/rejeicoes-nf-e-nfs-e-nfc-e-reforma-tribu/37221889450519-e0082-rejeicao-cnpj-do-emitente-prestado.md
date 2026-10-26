---
id: "37221889450519"
titulo: "E0082 Rejeição: CNPJ do emitente prestador não encontrado no cadastro CNPJ na data de competência."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37221889450519-E0082-Rejei%C3%A7%C3%A3o-CNPJ-do-emitente-prestador-n%C3%A3o-encontrado-no-cadastro-CNPJ-na-data-de-compet%C3%AAncia"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:18:16Z"
rotulos: ["Configuração", "Fiscal", "NF-e", "SEFAZ", "Erro", "NF-e ou NFC-e", "Base de dados da Receita Federal", "Não consta na base de dados da Receita Federal", "CNPJ da empresa emitente não está cadastrado ou não estava ativo", "CNPJ do emitente prestador informado no documento fiscal"]
---

# E0082 Rejeição: CNPJ do emitente prestador não encontrado no cadastro CNPJ na data de competência.

**MENSAGEM**

E0082 Rejeição: CNPJ do emitente prestador não encontrado no cadastro CNPJ na data de competência.

**SITUAÇÃO**

Mensagem apresentada ao emitir uma **NF-e** ou **NFC-e** quando o **CNPJ da empresa emitente** não está cadastrado ou não estava ativo na base de dados da Receita Federal na data de competência informada no documento fiscal.

**SOLUÇÃO**

**(1)** Acesse a tela **"Empresas"** (Configurações » Cadastros » Empresas) e localize o **cadastro da empresa emitente**.

**(2)** Na aba **“Geral”**, verifique se o campo **“CNPJ/CPF”** está corretamente preenchido e se a informação informada **corresponde ao cadastro oficial da empresa**.

**(3)** Consulte o CNPJ no site da **Receita Federal** ou no **SINTEGRA** para validar:

- Se o **CNPJ está correto**;
- Se a **situação cadastral** está **ATIVA**;
- Se o cadastro estava **ativo na data de competência** do documento fiscal que está sendo emitido.

**(4)** Caso identifique que o **CNPJ** esteja incorreto no cadastro, **retorne aos passos 1 e 2** e corrija a informação no campo “CNPJ/CPF”.

**(5)** Se o **CNPJ** estiver correto, mas a **situação cadastral** estiver **inativa** ou **não estiver ativa na data de competência**, entre em contato com o **contador da empresa** para regularizar a situação junto à **Receita Federal**.

**(6)** Após realizar as correções necessárias, **redigite os dados do cabeçalho da nota fiscal** ou, se preferir, **exclua a nota e refaça o faturamento**.

**(7)** Em seguida, **gere um novo lote** e tente **autorizar novamente o documento fiscal**.

**CAUSA**

A rejeição ocorre quando o **CNPJ do emitente prestador** informado no documento fiscal **não consta na base de dados da Receita Federal** ou não estava **ativo na data de competência** do documento. Isso pode acontecer por:

- CNPJ digitado incorretamente no cadastro da empresa;
- Empresa com situação cadastral **inativa, suspensa ou baixada** na Receita Federal;
- Cadastro da empresa não estava ativo na data de competência informada no documento fiscal;
- Divergência entre o CNPJ cadastrado no sistema e o CNPJ oficial da empresa.
