---
id: "37229576686743"
titulo: "Rejeição E0488: CPF do fornecedor informado na DPS não encontrado no cadastro CPF"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37229576686743-Rejei%C3%A7%C3%A3o-E0488-CPF-do-fornecedor-informado-na-DPS-n%C3%A3o-encontrado-no-cadastro-CPF"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:13:51Z"
rotulos: ["Configuração", "Parceiro", "Receita Federal", "SEFAZ", "Erro", "CPF do fornecedor informado na DPS", "CPF não encontrado na DPS", "Declaração Prévia de Serviços (DPS)", "CPF do fornecedor", "DPS", "E0488 Rejeição", "Rejeição E0488"]
---

# Rejeição E0488: CPF do fornecedor informado na DPS não encontrado no cadastro CPF

**MENSAGEM**

Rejeição E0488: CPF do fornecedor informado na DPS não encontrado no cadastro CPF.

**SITUAÇÃO**

Ao transmitir uma **Declaração Prévia de Serviços (DPS)**, o sistema retorna a rejeição informando que o **CPF do parceiro** indicado no documento **não foi localizado** na base de dados do cadastro de CPF da Receita Federal. Esta validação ocorre no momento da transmissão do documento fiscal eletrônico.

**SOLUÇÃO**

**(1)** Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros).

**(2)** Localize o cadastro do **parceiro** informado na DPS.

**(2)** Na aba **"Identificação"**, verifique se o **CPF** do fornecedor está **correto e completo**, sem caracteres especiais (pontos, hífens ou traços).

**(3)** Consulte o CPF do fornecedor diretamente no site da [**''Receita Federal''**](https://servicos.receita.fazenda.gov.br/servicos/cpf/consultasituacao/consultapublica.asp) e confirme se o número está **ativo e regular**:

**(4)** Caso o CPF esteja **incorreto ou inválido**, corrija a informação no cadastro do parceiro com o **número correto** conforme a consulta realizada.

**(5)** Salve as alterações realizadas no cadastro do fornecedor.

**(6)** Retorne à tela de emissão da **DPS** e realize novamente a **transmissão do documento** fiscal eletrônico.

**CAUSA**

A rejeição é retornada pela **SEFAZ** quando o **CPF do parceiro** informado na Declaração Prévia de Serviços está **incorreto, inválido ou não consta** na base de dados do cadastro de CPF da Receita Federal. Isso pode ocorrer devido a **erros de digitação**, CPF **cancelado ou suspenso**, ou ainda pela **ausência de cadastro** do fornecedor como parceiro no sistema.
