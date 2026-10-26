---
id: "10112746179351"
titulo: "A nota XXX não pode gerar nota de compra. Para usar essa funcionalidade a TOP da nota deve ter uma TOP de compra como destino"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10112746179351-A-nota-XXX-n%C3%A3o-pode-gerar-nota-de-compra-Para-usar-essa-funcionalidade-a-TOP-da-nota-deve-ter-uma-TOP-de-compra-como-destino"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T15:04:33Z"
rotulos: ["Configuração", "Portal de Vendas", "TOP", "Estoque", "COM_E00151", "Nota de Compra", "Incapacidade de gerar nota de compra", "Tentativa de gerar nota de compra no portal de vendas", "Vincular TOP de compra na TOP de venda", "Nota de Venda"]
---

# A nota XXX não pode gerar nota de compra. Para usar essa funcionalidade a TOP da nota deve ter uma TOP de compra como destino

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18697109160471) MENSAGEM:**

[COM\_E00151]  A nota XXX não pode gerar nota de compra. Para usar essa funcionalidade a TOP da nota deve ter uma TOP de compra como destino.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18697096943255) SITUAÇÃO:**

Ao tentar gerar uma nota de compra através de uma nota no portal de vendas a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18697096944407) CAUSA:**

Ocorre quando é usada a opção de gerar nota de compra pelo portal de vendas e a TOP de compra não está vinculada na TOP de venda.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18697096948119) SOLUÇÃO:**

Logo após a geração de uma nota de venda, de acordo com o processo adotado por cada empresa, pode ser necessário o lançamento imediato de uma nota de compra dos produtos que saíram do estoque, de modo a realimentá-lo.

Para configurar essa opção de ação, acesse a tela do **Tipo de Operação - TOP** (Caminho de acesso à tela: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP), vá até a aba Geral e no campo TOP p/Devolução informe a TOP que dará seguimento ao processo, ou seja, neste caso uma TOP de Compra que efetue as atualizações pertinentes a esta operação (atualizações de financeiro, estoque etc).

![Imagem 5: Para configurar essa opção de ação, acesse a tela do Tipo de Operação - TOP (Caminho de acesso à tela: Comercial »…](https://ajuda.sankhya.com.br/hc/article_attachments/18697109186711)

![Imagem 6: Para configurar essa opção de ação, acesse a tela do Tipo de Operação - TOP (Caminho de acesso à tela: Comercial »…](https://ajuda.sankhya.com.br/hc/article_attachments/18697109191191)

Além disso, no cabeçalho da nota de Venda, alimente o campo **"Empresa de negociação"** com a empresa que será gerada na nota de compra.

![Imagem 7: Além disso, no cabeçalho da nota de Venda, alimente o campo "Empresa de negociação" com a empresa que será gerada na…](https://ajuda.sankhya.com.br/hc/article_attachments/18697109192599)
