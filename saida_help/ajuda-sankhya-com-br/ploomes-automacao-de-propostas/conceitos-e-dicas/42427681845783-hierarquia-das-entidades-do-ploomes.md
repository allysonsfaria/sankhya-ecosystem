---
id: "42427681845783"
titulo: "Hierarquia das entidades do Ploomes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427681845783-Hierarquia-das-entidades-do-Ploomes"
trilha: "PLOOMES: Automação de propostas  > Conceitos e dicas"
atualizado_em: "2026-08-10T18:08:20Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452310", "sync_hash_6de654bc5ad3"]
---

# Hierarquia das entidades do Ploomes

## Nesse artigo você entenderá de forma aprofundada a hierarquia das entidades do Ploomes.

O Ploomes possui diversas entidades como: Clientes, Negócios, Documentos, Produtos, Propostas, entre outras. Essas entidades estão diretamente relacionadas umas às outras e entender esta relação é fundamental para estruturar: Filtros, Abas, Relatórios, Fórmulas, e mais.

Exemplo: Imagine que seja necessário montar uma visualização de todos os produtos que foram orçados para clientes do segmento **"Distribuidora"**. Para isso, é preciso percorrer as estruturas do Ploomes desde o Produto da Proposta até o Segmento do Cliente:

![Imagem 1: Exemplo: Imagine que seja necessário montar uma visualização de todos os produtos que foram orçados para clientes do…](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369329863/6fe9070df90faef91966e090/mceclip1.png?expires=1786536000&signature=75307b065911b54014c597e293410e14b9285bbccb038d3a6fd5c09890e092b7&req=dyYuFct3lYdcFb4V1XW4gW1voU5L7urxan9LS6b%2FcsPSlRC05ZeFIRNnLXJl%0AlOtZszeIfRSmHtIWOLyvjP7LjA%3D%3D%0A)

**Observação:** "Workflow" seria o "Negócio" mas, nesta conta o módulo foi customizado.

O exemplo mostra a necessidade de entender que um **Produto** faz parte de uma **Proposta**, que por sua vez faz parte de um **Negócio** que está relacionado a um **Cliente**, para então buscar os campos referentes ao cliente (segmento).

Seguindo esta lógica, se fosse necessário buscar por produtos que façam parte de propostas que valham mais do que um certo valor, o caminho seria:

"Produto da proposta > Proposta > Negócio" e ao atingir o nível de Negócio, buscar pelo campo "Valor".

Existem relações mais complexas e elas podem se intercalar em alguns momentos mas, este exemplo cobre os principais casos de uso:

![Imagem 2: Existem relações mais complexas e elas podem se intercalar em alguns momentos mas, este exemplo cobre os principais…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369329867/24bacf0a911e355c2f4f8970/hierarquia_ploomes.png-expires%3D1619280000-signature%3Dc79ae80e509c2ae0b4fef3167e6a8c4ccccda39219c9be7c1b5cf2dbdb18aea5?expires=1786536000&signature=50179df534135db3548f9b6f8a8f9618e2fb13ca064b0234feafc0b4aa499aab&req=dyYuFct3lYdYFb4V1XW4gf6jJf0by809HY1wkJ%2F8%2Bds%2Bi0v8q69j%2FMcLFkK0%0AumAKCXLMWSnmzRNyRhv4%2F5c8ZQ%3D%3D%0A)
