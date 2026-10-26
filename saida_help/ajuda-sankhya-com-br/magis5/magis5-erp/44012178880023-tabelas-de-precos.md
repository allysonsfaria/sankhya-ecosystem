---
id: "44012178880023"
titulo: "Tabelas de preços"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012178880023-Tabelas-de-pre%C3%A7os"
trilha: "Magis5 > Magis5 ERP"
atualizado_em: "2026-10-05T19:21:55Z"
rotulos: ["sync_hc", "magis5", "magis5_204055193495", "sync_hash_3c74d94f0769"]
---

# Tabelas de preços

## As tabelas de preço permitem que o empreendimento trabalhe com até quatro tipos de preços para diferentes perfis de clientes.

- **Modo de Preço:** É a forma que será controlado o preço do produto, sendo:
  - Tabela: É possível utilizar até quatro tabelas (Atacado, Intermediário 1, Intermediário 2 e Varejo), sendo que cada tabela pode ser associada a um perfil de cliente específico. Além dessas quatro tabelas, há também a tabela “Parceiro”, onde o preço dos produtos utilizados é o preço de custo. Essa tabela não é editável. 
    A ordenação da tabela de preço são: Parceiro, Atacado, Intermediário 1, Intermediário 2 e Varejo. 
    Por padrão, a tabela principal é a “Varejo”.
  - Plataforma: Utilizado em integrações, onde cada integração utiliza um preço diferenciado.

- **Ao Alterar o custo, variar “Percentual” ou “Venda”:** Utilizado ao realizar entradas de Notas Fiscais, onde o custo dos produtos ou o lucro poderá ser alterado. Consequentemente, há duas situações:
  - Ao selecionar “Percentual”: Altera o percentual e mantém o valor da venda ou,
  - Ao selecionar “Venda”: Altera o valor da venda e mantém o percentual de lucro.

- **Atualizar custo de produtos compostos apenas no empreendimento atual?** Utilizado em situações onde o preço de custo dos produtos é atualizado. Esta configuração habilita que o empreendimento atual atualize o preço de custo em outros empreendimentos, seja a matriz atualizando as filiais ou as filiais atualizando a matriz. Por padrão, o preço de custo, se atualizado em uma filial, não deve atualizar a matriz, porém, a matriz deve atualizar a filial. 

  Logo, 

  Quando configurado na Matriz: Marcar “Não”, para o preço ser replicado para as filiais; 
  Quando configurado nas filiais: Marcar “Sim” para o preço ser atualizado apenas no empreendimento atual e não ser replicado para a matriz e outras filiais.

- **Atualizar custo de produtos compostos ao alterar o custo de insumos?** Essa configuração informa se o preço de custo de um insumo deverá ser atualizado caso tenha alguma alteração ao editar seu cadastro ou dar entrada no estoque através da nota fiscal

- **Permitir outro empreendimento atualizar preço de custo?** Utilizado para permitir ou não permitir que outro empreendimento atualize o preço de custo dos produtos (utilizado em conjunto com a configuração “Atualizar custo de produtos compostos apenas no empreendimento atual?)

  Logo, 

  Na Matriz, deve-se marcar “Não” para que nenhum outro empreendimento possa atualizar seu preço de custo e,
  Nas filiais, marcar “Sim” para que a matriz possa atualizar o preço de custo dos produtos.
