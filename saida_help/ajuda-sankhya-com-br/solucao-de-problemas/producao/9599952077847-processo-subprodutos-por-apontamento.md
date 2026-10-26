---
id: "9599952077847"
titulo: "Processo Subprodutos por apontamento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9599952077847-Processo-Subprodutos-por-apontamento"
trilha: "Solução de Problemas > Produção"
atualizado_em: "2026-07-29T13:59:15Z"
rotulos: ["Produtos", "Configuração", "TOP", "Estoque", "Produção", "não apagar", "Permite registrar subproduto sem apontar perda", "Adicione TOP para compra e novo modelo de nota", "Configure entrada de subproduto no roteiro e na composição do produto", "Subproduto"]
---

# Processo Subprodutos por apontamento

**(1)** Esse processo permite que o subproduto seja apontado manualmente pelo usuário, sem a necessidade de apontar a perda para dar entrada no subproduto.

**![Imagem 1: CONFIGURAÇÕES: Tipos de Operações - TOP (Caminho de acesso: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP)](https://ajuda.sankhya.com.br/hc/article_attachments/16749290887191) CONFIGURAÇÕES:**

**![Imagem 2: CONFIGURAÇÕES: Tipos de Operações - TOP (Caminho de acesso: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP)](https://ajuda.sankhya.com.br/hc/article_attachments/16749290891159) Tipos de Operações - TOP** (Caminho de acesso: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP)

- Inclua uma TOP com o tipo de movimento C-Compra.

![Imagem 3: Inclua uma TOP com o tipo de movimento C-Compra.](https://ajuda.sankhya.com.br/hc/article_attachments/16749274142743)

![Imagem 4: Modelos de Notas e Pedidos (Caminho de acesso: Comercial » Consulta » Modelo de Notas e Pedidos)](https://ajuda.sankhya.com.br/hc/article_attachments/16749290898839) **Modelos de Notas e Pedidos** (Caminho de acesso: Comercial » Consulta » Modelo de Notas e Pedidos)

- Inclua um novo modelo de nota pedido, usando a TOP de compra criada anteriormente.

![Imagem 5: Inclua um novo modelo de nota pedido, usando a TOP de compra criada anteriormente.](https://ajuda.sankhya.com.br/hc/article_attachments/16749274152983)

**![Imagem 6: Processo Produtivo - nova (Caminho de acesso: Produção » Cadastros » Processo Produtivo - Nova)](https://ajuda.sankhya.com.br/hc/article_attachments/16749290907287) Processo Produtivo - nova** (Caminho de acesso: Produção » Cadastros » Processo Produtivo - Nova)

- No processo que deseja adicionar o apontamento de subproduto acesse o roteiro;

![Imagem 7: No processo que deseja adicionar o apontamento de subproduto acesse o roteiro;](https://ajuda.sankhya.com.br/hc/article_attachments/16749290911127)

- Selecione a atividade que fará o apontamento e na aba **"Operações de estoque"** inclua uma nova;
- Crie uma nova operação de estoque:

![Imagem 8: Crie uma nova operação de estoque:](https://ajuda.sankhya.com.br/hc/article_attachments/16749290917015)

**Modelo:** Entrada de Sucata

**Tipo dos Itens:** Subproduto da Atividade

**Quando:** Ao apontar PA

**Modelo de nota:** Incluir o modelo criado com tipo de movimento C-compra.

**Local Origem:** Informe o local onde o Subproduto vai entrar.

**![Imagem 9: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/16749290922263) IMPORTANTE:**

As seleções acima são importantes para o funcionamento da rotina com subproduto, demais campos devem ser analisados pelo próprio usuário, se faz ou não sentido em seu processo utilizá-los.

![Imagem 10: Composição do Produto (Caminho de acesso: Produção » Cadastros » Composição do Produto)](https://ajuda.sankhya.com.br/hc/article_attachments/16749274177303) **Composição do Produto** (Caminho de acesso: Produção » Cadastros » Composição do Produto)

- Na aba Sub-Produtos ver adicionado o produto que vai dar entrada no estoque:

**Subproduto:** informe  o código do produto;

**Quantidade:** informe a quantidade de subproduto gerado para cada produto acabado.

**Exige Apontamento:** caso necessário, deixe o apontamento como obrigatório e marque essa opção.

**Subproduto por perda/refugo:** não use essa opção para apontamento de subproduto.

![Imagem 11: Subproduto por perda/refugo: não use essa opção para apontamento de subproduto.](https://ajuda.sankhya.com.br/hc/article_attachments/9606628792727)

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/9599952077847-Processo-Subprodutos-por-apontamento#top)
