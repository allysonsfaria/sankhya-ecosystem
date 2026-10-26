---
id: "360043658673"
titulo: "'193785' is not a valid value of union type 'tpDDDNulo'. cvc-type.3.1.3"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043658673--193785-is-not-a-valid-value-of-union-type-tpDDDNulo-cvc-type-3-1-3"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:04:27Z"
rotulos: ["ERRONF", "Configuração", "Empresa", "SEFAZ", "NFS-e", "Ajuste necessário", "Rejeição da NFS-e", "DDD inválido", "Erro"]
---

# '193785' is not a valid value of union type 'tpDDDNulo'. cvc-type.3.1.3

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16453892932503) MENSAGEM:**

cvc-datatype-valid.1.2.3: '193785' is not a valid value of union type 'tpDDDNulo'.
cvc-type.3.1.3: The value '193785' of element 'DDDPrestador' is not valid.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16453908154007) SITUAÇÃO:**

Ao gerar lote de uma NFS-e, é apresentada a mensagem de rejeição.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16453908165655) SOLUÇÃO:**

Para correção siga os passos abaixo:

**(1)** Acesse: "[Empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913)" (Caminho de acesso: Configurações » Cadastros » Empresas)

- Aba: '**Endereços"**
- Campo "**Telefone":** ajuste para que o DDD seja de apenas 3 números.

![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16453892964503) **CAUSA:**

Ocorre quando o número de DDD está com 4 casas decimais no cadastro da Empresa emitente da NFS-e.
