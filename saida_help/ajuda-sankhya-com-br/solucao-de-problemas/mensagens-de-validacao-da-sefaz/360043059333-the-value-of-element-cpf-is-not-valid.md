---
id: "360043059333"
titulo: "The value '' of element 'CPF' is not valid"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043059333-The-value-of-element-CPF-is-not-valid"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:09:34Z"
rotulos: ["ERRONF", "Configuração", "Parceiro", "NF-e", "XML", "SEFAZ", "Valor Inválido de 'CPF'", "Erro"]
---

# The value '' of element 'CPF' is not valid

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16460040684695) MENSAGEM:**

ERRO NA VALIDAÇÃO. Número Único:
Validação básica Sefaz: Erros encontrados:
cvc-pattern-valid: Value '' is not facet-valid with respect to pattern '[0-9]{11}' for type 'TCpf'.
cvc-type.3.1.3: The value '' of element 'CPF' is not valid.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16460008827671) SOLUÇÃO:**

Acesse o cadastro de todos os parceiros envolvidos no lançamento e valide se o campo CPF foi inserido corretamente [Destinatário, Transportador]:

- Tela "**Parceiros"** » Aba "**Identificação"** » Campo "**CNPJ/CPF"**

![Imagem 3: Tela " Parceiros" » Aba " Identificação" » Campo " CNPJ/CPF"](https://ajuda.sankhya.com.br/hc/article_attachments/14474553926167)

Acesse também a aba Acesso ao XML da NF-e/CTe e certifique não tem nenhuma linha cadastrada sem CPF/CNPJ..

![Imagem 4: Acesse também a aba Acesso ao XML da NF-e/CTe e certifique não tem nenhuma linha cadastrada sem CPF/CNPJ..](https://ajuda.sankhya.com.br/hc/article_attachments/19652981177111)

**![Imagem 5: IMPORTANTE :](https://ajuda.sankhya.com.br/hc/article_attachments/16460008832535) IMPORTANTE:**

Caso seja um parceiro padrão 'Consumidor Final', onde não seja possível identificar com um CPF válido, inserir a sequência de zeros [0].

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16460008840343) CAUSA:**

Mensagem é apresentada devido à ausência ou informação inválida para CPF/CNPJ em tag de CPF do XML, exemplos de cadastros que podem estar incompleto/inválido:

- CPF/CNPJ do Parceiro
- CPF/CNPJ do Parceiro transportador
- CFP/CNPJ do contato do parceiro
- Configuração da aba 'Acesso ao XML da NF-e/CT-e'
- Preferências da empresa » Aba 'Contador'
