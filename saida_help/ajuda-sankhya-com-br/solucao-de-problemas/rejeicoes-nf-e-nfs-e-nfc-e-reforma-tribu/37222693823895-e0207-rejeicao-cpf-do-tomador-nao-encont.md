---
id: "37222693823895"
titulo: "E0207 Rejeição: CPF do tomador não encontrado no cadastro CPF."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37222693823895-E0207-Rejei%C3%A7%C3%A3o-CPF-do-tomador-n%C3%A3o-encontrado-no-cadastro-CPF"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:17:33Z"
rotulos: ["Configuração", "Fiscal", "Parceiro", "NF-e", "Receita Federal", "SEFAZ", "Erro", "CPF do tomador/destinatário", "Autenticidade e regularidade fiscal", "CPF do tomador/destinatário não foi encontrado", "Não foi encontrado no cadastro da Receita Federal"]
---

# E0207 Rejeição: CPF do tomador não encontrado no cadastro CPF.

**MENSAGEM**

E0207 Rejeição: CPF do tomador não encontrado no cadastro CPF.

**SITUAÇÃO**

Ao emitir um **documento fiscal eletrônico** (NF-e, NFS-e ou NFC-e), o sistema retorna a rejeição informando que o **CPF do tomador/destinatário** não foi encontrado no cadastro da Receita Federal. A rejeição ocorre no momento da **transmissão do documento** para a SEFAZ.

**SOLUÇÃO**

**(1)** Acesse o site da [**''Receita Federal''**](https://servicos.receita.fazenda.gov.br/servicos/cpf/consultasituacao/consultapublica.asp) e consulte a situação cadastral do CPF do tomador/destinatário.

**(2)** Verifique se o **CPF está ativo e regular** na base da Receita Federal.

- Caso o CPF esteja **inativo, suspenso ou cancelado**, solicite ao cliente que regularize sua situação cadastral junto à Receita Federal.

**(3)** Confirme se o **CPF informado no cadastro** está correto e sem erros de digitação.

**(4)** Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o cadastro do tomador/destinatário.

**(5)** Corrija o **número do CPF** no campo **"CNPJ / CPF"** do cadastro do parceiro, caso identifique alguma inconsistência.

**(6)** Salve as alterações realizadas no cadastro.

**(7)** Reemita o **documento fiscal eletrônico** para o tomador/destinatário com os dados corrigidos. 

**CAUSA**

A rejeição é retornada pela **SEFAZ** quando o **CPF do tomador/destinatário** informado no documento fiscal não consta na base de dados da **Receita Federal**, está **inativo, cancelado ou digitado incorretamente** no cadastro do parceiro. A validação é realizada para garantir a **autenticidade e regularidade fiscal** das partes envolvidas na operação.
