---
id: "360042575514"
titulo: "CNPJ Destinatário não cadastrado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042575514-CNPJ-Destinat%C3%A1rio-n%C3%A3o-cadastrado"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-08-01T00:46:39Z"
rotulos: ["ERRONF", "Configuração", "Parceiro", "NF-e", "SEFAZ", "246", "Rejeição 246: CNPJ Destinatário não cadastrado", "CNPJ não habilitado na UF destinatária", "Verificar e atualizar CNPJ/CPF e Inscrição Estadual no Cadastro de Parceiros.", "Erro", "Artigo atualizado KCS", "CVE - KCS", "Documentos Eletrônicos"]
---

# CNPJ Destinatário não cadastrado

**MENSAGEM:**

[246 - Rejeição]: CNPJ Destinatário não cadastrado.

**SOLUÇÃO:**

**(1)** Confira, no Cadastro de Parceiros, se o campo **CNPJ/CPF** foi digitado corretamente (erros de digitação são a causa mais frequente).

**(2)** Consulte a situação cadastral do CNPJ diretamente no site da Receita Federal (Consulta Cadastro Nacional da Pessoa Jurídica). A situação deve constar como **"Ativa"**.

**(3)** Se o CNPJ estiver **Baixado, Suspenso, Inapto ou Nulo**, não é possível emitir NF-e para esse parceiro até que ele regularize a situação junto à Receita Federal.

**(4)** Após a regularização (ou correção do CNPJ cadastrado), refaça a nota informando novamente o parceiro.

**CAUSA:**

Essa rejeição ocorre quando o CNPJ do destinatário informado na nota não é encontrado, ou não está com situação cadastral ativa, na base da Receita Federal. A SEFAZ consulta esse cadastro no momento da autorização da NF-e e recusa o documento quando o CNPJ está inválido, inexistente ou baixado.

**OBSERVAÇÃO:**

Se, além dessa rejeição, o sistema também apontar problema na Inscrição Estadual, é necessário verificar separadamente a situação da IE no SINTEGRA ou no site da SEFAZ da UF do destinatário, esse é um cadastro distinto do CNPJ e tratado por outra rejeição.
