---
id: "9757679656599"
titulo: "Não foi possível ler dados do relatório"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9757679656599-N%C3%A3o-foi-poss%C3%ADvel-ler-dados-do-relat%C3%B3rio"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T15:06:23Z"
rotulos: ["Produtos", "Configuração", "Relatórios", "TOP", "Estoque", "INV_E00016", "Não foi possível ler dados do relatório", "Produto sem Custo de Reposição compatível", "[INV_E00016] Dados do relatório não lidos", "Erro"]
---

# Não foi possível ler dados do relatório

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19277438966551) MENSAGEM:**

[INV\_E00016] Não foi possível ler dados do relatório.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19277414848151) SITUAÇÃO:**

Ao gerar o registro de inventário a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19277414851351) CAUSA:**

Ocorre quando um produto ou mais não possui Custo de Reposição em sua tabela que seja compatível ao filtro utilizado na tela Registro de Inventário.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19277414855831) SOLUÇÃO:**

Esse comportamento costuma ocorrer quando um produto ou mais não possui Custo de Reposição, em sua tabela, que seja compatível ao filtro utilizado na tela Registro de Inventário.

Confira no cadastro do **Tipo de Operação TOP** (Caminho de acesso à tela: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) como está configurado o campo Usar como Preço:

![Imagem 5: Confira no cadastro do Tipo de Operação TOP (Caminho de acesso à tela: Comercial » Arquivo » Cadastros » Tipos de…](https://ajuda.sankhya.com.br/hc/article_attachments/19277414859415)

Defina no campo **"Usar como Preço"** qual valor que será atribuído aos itens lançados na central; o preço utilizado para o produto. Confira abaixo as opções que podem ser escolhidas:

- Valor Líquido da origem;
- Último Custo Médio Gerencial;
- Preço em Moeda;
- Último Custo Médio Sem ICMS;
- Último Custo de Entrada Com ICMS;
- Último Custo Variável;
- Último Custo Gerencial;
- Último Custo de Reposição;
- Preço de Venda;
- Nenhum;
- Último Custo Médio Com ICMS;
- Último Custo de Entrada Sem ICMS;
- Média das notas de origem.

Para mais informações sobre o cadastro do Tipo de Operação acesse o link abaixo:

[Tipos de Operação - TOP – Sankhya Gestão de Negócios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)

Também segue abaixo o manual da tela 'Registro de Inventário', que informa em detalhes a funcionalidade de cada opção disponível.

[Registro de Inventário – Sankhya Gestão de Negócios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116253-Registro-de-Invent%C3%A1rio)
