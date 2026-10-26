---
id: "30708180844823"
titulo: "Na Consulta de Produtos pela Central de Vendas não apresenta os mesmos produtos da Consulta de Produtos fora da Central de Vendas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30708180844823-Na-Consulta-de-Produtos-pela-Central-de-Vendas-n%C3%A3o-apresenta-os-mesmos-produtos-da-Consulta-de-Produtos-fora-da-Central-de-Vendas"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-09-01T12:02:33Z"
rotulos: ["Produtos", "Configuração", "Consulta", "Central de Vendas", "Portal de Vendas", "acessando pela Central de Vendas", "retorna uma quantidade diferente", "de produtos ou não apresenta produtos", "Consulta de Produtos fora da Central de Vendas", "pesquisa na Consulta de Produtos", "quando comparado"]
---

# Na Consulta de Produtos pela Central de Vendas não apresenta os mesmos produtos da Consulta de Produtos fora da Central de Vendas

![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30708180834711) **SITUAÇÃO:**

Ao fazer uma pesquisa na Consulta de Produtos acessando pela Central de Vendas retorna uma quantidade diferente de produtos (ou não apresenta produtos específicos) quando comparado à Consulta de Produtos fora da Central de Vendas.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30708176907543)SOLUÇÃO:**

Pela **"Central de Vendas"** é possível acrescentar um critério adicional que permitirá filtrar os produtos da consulta de acordo com a Nota/Pedido selecionados através do parâmetro **"Critério adicional para catálogo de produtos - QRYCONSPROD"**. A informação desse parâmetro deve ser configurada em linguagem SQL como parte da cláusula "WHERE" que irá filtrar os produtos. Nesse WHERE estará disponível o parâmetro **"NUNOTA"** que representa a nota selecionada na Central.

**Exemplo:**

![Imagem 3: Exemplo:](https://ajuda.sankhya.com.br/hc/article_attachments/30708180838551)

Caso este parâmetro esteja configurado e os produtos desejados não estejam retornando na busca será necessário rever esta configuração.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/30708176910871)CAUSA:**

A divergência de produtos apresentados na Consulta de Produtos dentro e fora da Central de Vendas pode ocorrer quando há uma expressão no parâmetro QRYCONSPROD e as condições dessa configuração não contemplam os produtos em questão.
