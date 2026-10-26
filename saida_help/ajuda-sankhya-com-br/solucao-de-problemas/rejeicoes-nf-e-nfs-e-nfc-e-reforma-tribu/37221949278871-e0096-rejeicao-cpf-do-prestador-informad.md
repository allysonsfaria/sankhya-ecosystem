---
id: "37221949278871"
titulo: "E0096 Rejeição: CPF do prestador informado na DPS é inválido."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37221949278871-E0096-Rejei%C3%A7%C3%A3o-CPF-do-prestador-informado-na-DPS-%C3%A9-inv%C3%A1lido"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:18:14Z"
rotulos: ["Configuração", "Fiscal", "Parceiro", "SEFAZ", "Erro", "Transmissão da DPS (Declaração de Prestação de Serviços)", "CPF do prestador de serviços", "Transmissão do documento fiscal eletrônico", "CPF do prestador de serviços inválido", "Inválido zerado ou com dígito verificador incorreto"]
---

# E0096 Rejeição: CPF do prestador informado na DPS é inválido.

**MENSAGEM**

E0096 Rejeição: CPF do prestador informado na DPS é inválido.

**SITUAÇÃO**

A mensagem de rejeição aparece durante o processo de **transmissão da DPS** (Declaração de Prestação de Serviços) quando o **CPF do prestador de serviços** cadastrado no sistema está **inválido, zerado ou com dígito verificador incorreto**. Esta validação é realizada pela SEFAZ no momento da transmissão do documento fiscal eletrônico.

**SOLUÇÃO**

Para corrigir a rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o cadastro do **prestador de serviços** vinculado à DPS rejeitada.

**(2)** Na aba **"Identificação"**, localize o campo **"CNPJ / CPF"** e verifique se o CPF informado está correto:

- Certifique-se de que o CPF possui **11 dígitos numéricos**;
- Verifique se o CPF está **sem pontos, traços ou espaços em branco**;
- Confirme se o **dígito verificador** (últimos dois números do CPF) está correto;
- Assegure-se de que o CPF **não está zerado** (00000000000).

**(3)** Caso o CPF esteja incorreto, **corrija a informação** inserindo um CPF válido e ativo na Receita Federal do Brasil.

**(4)** Salve as alterações realizadas no cadastro do parceiro.

**(5)** Retorne ao documento fiscal e **redigite as informações** do prestador para que o sistema atualize os dados cadastrais.

**(6)** Gere um **novo lote de transmissão** da DPS com as informações corrigidas. 

**OBSERVAÇÃO:** Caso o problema persista após as correções, inutilize a numeração do documento, exclua a DPS e gere uma nova com os dados atualizados.

**CAUSA**

A rejeição ocorre quando a DPS é transmitida com o **CPF do prestador de serviços inválido**. Isso acontece quando o CPF informado no cadastro do parceiro está **zerado, com sequência numérica incorreta, com dígito verificador inválido ou não está ativo** na base da Receita Federal. A SEFAZ valida a autenticidade do CPF no momento da transmissão e, caso identifique inconsistências, retorna a rejeição E0096.
