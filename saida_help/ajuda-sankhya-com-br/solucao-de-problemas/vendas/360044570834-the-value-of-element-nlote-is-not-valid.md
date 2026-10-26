---
id: "360044570834"
titulo: "The value '' of element 'nLote' is not valid"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044570834-The-value-of-element-nLote-is-not-valid"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T15:51:38Z"
rotulos: ["Produtos", "Configuração", "NF-e", "Estoque", "Lote vazio com dados preenchidos", "Ajuste cadastro de lote; exclua dados incorretos", "Valor vazio para 'nLote' inválido", "Erro"]
---

# The value '' of element 'nLote' is not valid

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18602756226583) MENSAGEM:**

cvc-type.3.1.3: The value '' of element 'nLote' is not valid.
cvc-minLength-valid: Value '' with length = '0' is not facet-valid with respect to minLength '1' for type.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18602756232343)CAUSA:**

Essa mensagem será apresentada quando determinado produto inserido na nota, possui a marcação "Tem Rastro do Lote", as informações de data de validade e fabricação preenchidas, porém a informação de lote está vazia.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18602756234263) SOLUÇÃO:**

Essa mensagem será apresentada quando determinado produto inserido na nota, possui a marcação "Tem Rastro do Lote", as informações de data de validade e fabricação preenchidas, porém a informação de lote está vazia.

![Imagem 4: Será necessário alinhar com os responsáveis pelas configurações de controle de lote dos produtos, qual medida cabe ao…](https://ajuda.sankhya.com.br/hc/article_attachments/18602730081943) Será necessário alinhar com os responsáveis pelas configurações de controle de lote dos produtos, qual medida cabe ao processo da empresa:

- No cadastro do produto, aba 'Estoque' verifique se existe uma linha com o campo 'Controle' em branco e 'Data de Validade' e 'Data de Fabricação' preenchidos, caso essa seja indevida, proceda com sua exclusão.

![Imagem 5: Após esse ajuste, realize um novo lançamento da nota. Caso a nota anterior tenha gerado 'Número Nota', realize sua…](https://ajuda.sankhya.com.br/hc/article_attachments/18602724746391) Após esse ajuste, realize um novo lançamento da nota. Caso a nota anterior tenha gerado 'Número Nota', realize sua inutilização/exclusão.
