---
id: "37222603564439"
titulo: "E0190 Rejeição: CNPJ do tomador não encontrado no cadastro CNPJ."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37222603564439-E0190-Rejei%C3%A7%C3%A3o-CNPJ-do-tomador-n%C3%A3o-encontrado-no-cadastro-CNPJ"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-08-25T17:54:58Z"
rotulos: ["CT-e", "Fiscal", "Parceiro", "Receita Federal", "SEFAZ", "Erro", "CNPJ do tomador não foi encontrado no cadastro da Receita Federal", "CNPJ do tomador informado no CT-e", "CT-e (Conhecimento de Transporte Eletrônico)", "CNPJ do tomador não foi encontrado no cadastro", "Documentos Eletrônicos"]
---

# E0190 Rejeição: CNPJ do tomador não encontrado no cadastro CNPJ.

**MENSAGEM**

E0190 Rejeição: CNPJ do tomador não encontrado no cadastro CNPJ.

**SITUAÇÃO**

Ao emitir um **CT-e (Conhecimento de Transporte Eletrônico)**, a nota é rejeitada pela SEFAZ com a mensagem informando que o **CNPJ do tomador não foi encontrado no cadastro** da Receita Federal.

**SOLUÇÃO**

**(1)** Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o cadastro do **tomador do serviço** informado no CT-e.

**(2)** Verifique se o **CNPJ informado no campo "CNPJ/CPF"** está correto e **devidamente cadastrado na Receita Federal**.

**(3)** Consulte o CNPJ do tomador no **SINTEGRA** ou no **Cadastro Centralizado de Contribuintes** para confirmar:

- Se o CNPJ está **ativo e válido**;
- Se o número do CNPJ está **digitado corretamente**, sem erros de digitação;
- Se o CNPJ possui **situação cadastral regular** junto à Receita Federal.

**(4)** Caso identifique que o **CNPJ está incorreto ou inválido**, retorne ao passo 1 e 2 e corrija a informação.

**(5)** Após realizar a correção, **redigite o CT-e** e gere um novo lote para transmissão à SEFAZ.

**(6)** Caso o CNPJ esteja correto mas ainda assim apresente a rejeição, **oriente o tomador a regularizar sua situação cadastral** junto à Receita Federal, pois o CNPJ pode estar **inativo, suspenso ou inexistente** na base de dados. 

**CAUSA**

A rejeição ocorre quando o **CNPJ do tomador informado no CT-e** não consta na base de dados da **Receita Federal**, seja por estar **digitado incorretamente**, por estar **inativo, suspenso, cancelado** ou por **não existir** no cadastro nacional de pessoas jurídicas.
