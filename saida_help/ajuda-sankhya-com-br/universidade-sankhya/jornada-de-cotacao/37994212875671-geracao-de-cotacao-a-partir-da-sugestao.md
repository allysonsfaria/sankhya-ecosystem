---
id: "37994212875671"
titulo: "Geração de cotação a partir da sugestão de compra da análise do Giro"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37994212875671-Gera%C3%A7%C3%A3o-de-cota%C3%A7%C3%A3o-a-partir-da-sugest%C3%A3o-de-compra-da-an%C3%A1lise-do-Giro"
trilha: "Universidade Sankhya > Jornada de Cotação"
atualizado_em: "2026-07-22T14:03:11Z"
rotulos: ["Produtos", "Configuração", "Cotação", "Análise de Giro", "Estoque"]
---

# Geração de cotação a partir da sugestão de compra da análise do Giro

## Como gerar cotação a partir da sugestão de compra da análise de Giro

#### Introdução

Este guia apresenta o processo de geração de uma cotação de compra, baseado na análise de giro e no cálculo de estoque ideal. A partir da definição dos estoques mínimo e máximo, é possível determinar a quantidade sugerida para compra, utilizando a fórmula que considera acréscimos estratégicos, compras pendentes e vendas em aberto. O objetivo é garantir um planejamento eficiente, evitando excessos ou faltas de produtos, enquanto otimiza os recursos e atende às demandas de forma ágil e precisa.

**Configurações**

- **Produtos:**

  - Acesse a tela de Produtos.
    **Configurações >> Cadastros >> Produtos**

    - Na aba **“Geral”**, no campo **“Usado Como”** deve ser informado com a opção **“Revenda”**.
    - Na aba **“Estoque”**, preencha os campos **“Estoque Mínimo”** e **“Estoque Máximo”.**
- **Análise de Giro:**

  - Acesse a tela de Análise de Giro.
    **Comercial >> Rotinas >> Análise de Giro**

    - Na opção **“Alterar a matriz selecionada”** informe 3 períodos fixos.
    - Na sub aba **“Estoque Mínimo e Sugestão de Compra” realize as seguintes configurações:**
- Marque a opção **“Período sem vendas influencia a média para estoque mínimo”**.
- No campo **“Dias ÚTEIS para Estocagem”** informar a quantidade conforme a necessidade do cliente.
- No campo **“% Acréscimo na Sugestão de Compras”** Informe a quantidade conforme a necessidade do cliente.
- Desmarque a opção **“Não Atualizar Estoque Mínimo quando a sugestão for zero?”**
- Na sub aba **“Outras configurações”** realize as seguintes configurações:
- Marque a opção **“Incluir produtos sem giro”**.
- Marque a opção **“Incluir produtos sem estoque”**.
- No campo **“Considerar custo”** escolha a opção **“Reposição”**.
- No campo **“Detalhar de acordo com”** escolha a opção **“Produto”**.
- Marque a opção **“Listar pedidos na aba Compras/Vendas Pendentes”.**
- No campo **“Apresentar resultado por”** escolha as opções **“Empresa” e “Controle”.**
- Na parte de **“Filtros”** a sugestão é filtrar por produtos de revenda **(Produtos.USOPROD = ‘R’ (Revenda).**

#### Conclusão

As configurações corretas são fundamentais para garantir que a cotação de compra seja gerada de forma eficiente e alinhada às necessidades reais da empresa. A partir da sugestão de compra baseada na análise de giro, é possível planejar a aquisição de produtos de maneira estratégica, equilibrando os estoques e evitando tanto excessos quanto faltas. Isso promove maior controle operacional, otimização dos recursos financeiros e agilidade no atendimento às demandas, fortalecendo a sustentabilidade e a competitividade do negócio.
