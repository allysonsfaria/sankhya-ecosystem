---
id: "360043119993"
titulo: "The value '' of element 'nro' is not valid"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043119993-The-value-of-element-nro-is-not-valid"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:07:24Z"
rotulos: ["ERRONF", "#RevisadoBernardo", "Configuração", "Parceiro", "NF-e", "SEFAZ", "Valor Inválido de Endereço", "Erro", "Documentos Eletrônicos"]
---

# The value '' of element 'nro' is not valid

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16487820896535) MENSAGEM:**

cvc-pattern-valid: Value ' SEM ENDERECO' is not facet-valid with respect to pattern '[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}' for type '#AnonType\_xLgrTEndereco'.
cvc-type.3.1.3: The value ' SEM ENDERECO' of element 'xLgr' is not valid.
cvc-pattern-valid: Value '' is not facet-valid with respect to pattern '[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}' for type '#AnonType\_nroTEndereco'.
cvc-type.3.1.3: The value '' of element 'nro' is not valid.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16487793129495) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse o cadastro do Parceiro ou Transportadora da Nota ( quando houver )](https://ajuda.sankhya.com.br/hc/article_attachments/16487820900503) Acesse o cadastro do Parceiro ou Transportadora da Nota (quando houver)

1.1- Acesse: Configurações » Cadastros » Parceiros

Aba: **"Endereço ou Endereço de Entrega"**

- Efetue o ajuste no campo do  **"Endereço"** para resolver o erro: The value ' SEM ENDERECO' of element 'xLgr' is not valid.
- Efetue o ajuste no campo **"Número"**, para resolver o erro The value '' of element 'nro' is not valid.

**![Imagem 4: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16487820902295) OBSERVAÇÃO:**

Em alguns casos podem ocorrer o erro **The value '200 ' of element 'nro' is not valid.**Isso significa que após o número 200 existe um espaço em branco, que ocasiona erro na validação da SEFAZ.

![Imagem 5: Se o erro for no cadastro do emitente, acesse o cadastro de empresa.](https://ajuda.sankhya.com.br/hc/article_attachments/16487793134999) Se o erro for no cadastro do emitente, acesse o cadastro de empresa.

2.1- Configurações » Cadastros » Empresas

- Aba **"Endereço":** efetue os ajustes como indicado no item anterior.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16487820908311) CAUSA:**

Ocorre quando no cadastro do emitente, destinatário ou transportadora, o endereço e número estão inválidos, incorretos ou em branco.
