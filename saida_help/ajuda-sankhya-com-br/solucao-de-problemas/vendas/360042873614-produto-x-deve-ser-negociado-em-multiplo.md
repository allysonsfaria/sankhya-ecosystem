---
id: "360042873614"
titulo: "Produto 'X' deve ser negociado em múltiplos de ' '"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042873614-Produto-X-deve-ser-negociado-em-m%C3%BAltiplos-de"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:05:08Z"
rotulos: ["#PUBLIFER", "CORE_E03246", "Produtos", "Configuração", "TOP", "Estoque", "Produto deve ser negociado em múltiplos definidos", "Validação controlada por Tipo de Operação no sistema", "Ajustar \"Agrupamento Mínimo\" no cadastro de produtos", "Erro"]
---

# Produto 'X' deve ser negociado em múltiplos de ' '

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16109575109655) MENSAGEM:**

[CORE\_E03246] Produto 'X' deve ser negociado em múltiplos de ' '.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16109586506519) SOLUÇÃO:**

![Imagem 3: Necessário que o campo "Quantidade" respeite a configuração abaixo, realizada no cadastro do respectivo item:](https://ajuda.sankhya.com.br/hc/article_attachments/16109575114519) Necessário que o campo **"Quantidade"** respeite a configuração abaixo, realizada no cadastro do respectivo item:

**(2)** Tela **"[Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-)"** (Caminho de acesso: Configurações » Cadastros » Produtos)

**(2)** Aba **"Medidas e estoque"** » **"Estoque"** » Campo **"Agrupamento Mínimo"**:

![Imagem 4: (2) Aba "Medidas e estoque" » "Estoque" » Campo "Agrupamento Mínimo" :](https://ajuda.sankhya.com.br/hc/article_attachments/14548961124759)

**(2)** O campo **agrupamento mínimo** comporta os dados pertinentes ao agrupamento mínimo para a venda ou compra do produto, ou seja, a negociação desse produto só poderá ser feita com quantidades múltiplas do valor (4 casas decimais) informado nesse campo.

**(2)** Informando no campo Agrupamento mínimo o valor 0 (zero), será aceita qualquer quantidade na compra;

**Vejamos um exemplo:**

Tem-se o produto Ovo com sua Unidade padrão = unidade, é definido um agrupamento mínimo de 12 para o mesmo. Na inserção do item na nota, o campo "Quantidade" deverá ser preenchido com um múltiplo de 12.

(1)** IMPORTANTE:**

| **(2)** Essa validação pode ser controlada por Tipo de Operação, conforme marcação **"Valida agrupamento mínimo?"** da tela **"Tipos de Operação - TOP"**(Comercial » Arquivo » Cadastros » Tipos de Operação - TOP), aba **"Estoque"**:  Valida agrupamento mínimo?:Por meio deste campo, define-se qual validação será executada de acordo com o agrupamento mínimo definido no **"[Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025389093-Produtos-)"**, aba Medidas e estoque. São apresentadas as seguintes opções:  (2)** Não valida:** Esta opção caracteriza que o agrupamento mínimo não será validado;  (2)** Valida e bloqueia:** Com esta opção selecionada, caso haja algum item negociado com a quantidade que não respeite o agrupamento mínimo e efetuado o bloqueio deste lançamento;  (2)** Valida e exige liberação:** Esta opção funciona de forma semelhante a opção anterior, sendo que ao invés de ocorrer o bloqueio, será solicitada a liberação do evento **"[78 - Liberação de agrupamento mínimo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#78-liberaodeagrupamentomnimo)"** para que um usuário com alçada autorize o lançamento. |
| --- |

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16109575118871) CAUSA:**

Mensagem apresentada ao realizar movimentações no sistema inserindo no campo 'quantidade' um valor que não seja múltiplo do valor definido como agrupamento mínimo.
