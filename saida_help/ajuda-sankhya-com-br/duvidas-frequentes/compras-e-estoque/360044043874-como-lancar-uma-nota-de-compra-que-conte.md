---
id: "360044043874"
titulo: "Como lançar uma nota de compra que contenha bens e produtos para revenda na mesma nota?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044043874-Como-lan%C3%A7ar-uma-nota-de-compra-que-contenha-bens-e-produtos-para-revenda-na-mesma-nota"
trilha: "Dúvidas Frequentes > Compras e Estoque"
atualizado_em: "2026-07-22T15:55:30Z"
rotulos: ["Configuração", "TOP", "Controle de estoque", "Estoque", "Financeiro", "Lançamento de Nota de Compra com Bens e Produtos para Revenda", "Produtos para revenda"]
---

# Como lançar uma nota de compra que contenha bens e produtos para revenda na mesma nota?

**(1)** Como no sistema o controle de estoque de bens e de produtos para revenda partem do cadastro da TOP, não há a possibilidade de realizar esse lançamento em uma única nota. Caso isso ocorra será apresentada a mensagem:

[[CORE\_E01832] Produto: XX Diferença na quantidade de bens digitados!](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043577734)

**(1)** Isso ocorre devido ao fato do sistema esperar que o bem seja informado para todos os produtos da nota, porém não é possível inserir um bem em um produto que não seja "Imobilizado";

**(1)** Sendo assim é necessário que o lançamento dessa nota de compra se dê em duas TOP's distintas, uma para os imobilizados e outra para os produtos para revenda;

**(1)** Esses dois lançamentos devem ser realizados com os mesmos dados do cabeçalho, número, série, parceiro, chave, etc. Dessa forma, ao gerar as obrigações acessórias (sped e escrituração), o sistema automaticamente irá agrupa-los;

**(1)** Para que o financeiro também seja agrupado, deverá ser realizada a renegociação dos títulos.
