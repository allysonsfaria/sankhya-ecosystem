---
id: "17025796112535"
titulo: "ERRO: cvc-pattern-valid: Value '0' is not facet-valid with respect to pattern '[0-9]{11) for type \"TCpf. cvc-type.3.1.3: The value '0' of element 'CPF' is not valid. Código: CORE_E04895"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/17025796112535-ERRO-cvc-pattern-valid-Value-0-is-not-facet-valid-with-respect-to-pattern-0-9-11-for-type-TCpf-cvc-type-3-1-3-The-value-0-of-element-CPF-is-not-valid-C%C3%B3digo-CORE-E04895"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T14:53:59Z"
rotulos: ["CORE_E04895", "Configuração", "Parceiro", "NF-e", "CPF", "CPF preenchido com '0' no contato de entrega da nota fiscal", "Corrigir o CPF no cadastro de contatos e se necessário ativar CNPJ para contatos jurídicos", "[CORE_E04895] CPF inválido", "Erro"]
---

# ERRO: cvc-pattern-valid: Value '0' is not facet-valid with respect to pattern '[0-9]{11) for type "TCpf. cvc-type.3.1.3: The value '0' of element 'CPF' is not valid. Código: CORE_E04895

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/17025804112279) **MENSAGEM:**

[CORE\_E04895] cvc-pattern-valid: Value '0' is not facet-valid with respect to pattern '[0-9]{11) for type "TCpf. cvc-type.3.1.3: The value '0' of element 'CPF' is not valid.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17025779480983)CAUSA:**

Ocorre ao tentar faturar ou gerar o lote de uma nota cujo a mesma possui um Contato de Entrega preenchido no cabeçalho da nota e no cadastro do mesmo o campo CPF/CNPJ está preenchido com valor '0'.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17025777433623)SOLUÇÃO:**

![Imagem 4: Acesse: Parceiros (Configurações » Cadastros) - aba Contatos e valide o campo CPF no contato cadastrado. Nesse caso o…](https://ajuda.sankhya.com.br/hc/article_attachments/17615095785495) Acesse: Parceiros (Configurações » Cadastros) - aba Contatos e valide o campo CPF no contato cadastrado. Nesse caso o erro informa que o campo CPF está preenchido com valor '0' ou em branco, sendo necessário preenchimento do mesmo.

![Imagem 5: Se o contato for CNPJ, deve-se ativar o parâmetro ''PERMCNPJCONTATO - Permite digitação do CNPJ nos contatos?''](https://ajuda.sankhya.com.br/hc/article_attachments/17615112122135) Se o contato for CNPJ, deve-se ativar o parâmetro ''PERMCNPJCONTATO - Permite digitação do CNPJ nos contatos?''

![Imagem 6: Após ativa-lo, a aba contato atualizará e apresentará a opção para selecionar se o contato se trata de pessoa física ou…](https://ajuda.sankhya.com.br/hc/article_attachments/17615095791255) Após ativa-lo, a aba contato atualizará e apresentará a opção para selecionar se o contato se trata de pessoa física ou jurídica, e o campo CNPJ será apresentado.

![Imagem 7: Após realizar os devidos ajustes, gere o lote novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/17615112140567) Após realizar os devidos ajustes, gere o lote novamente.
