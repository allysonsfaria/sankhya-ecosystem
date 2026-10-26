---
id: "44012780178327"
titulo: "[TMS] Resolução de Erro \"Produto Não Atendido\" no Cálculo de Pré-Conhecimento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012780178327--TMS-Resolu%C3%A7%C3%A3o-de-Erro-Produto-N%C3%A3o-Atendido-no-C%C3%A1lculo-de-Pr%C3%A9-Conhecimento"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T19:38:06Z"
rotulos: ["sync_hc", "lincros", "lincros_13433263", "sync_hash_7bd875a46f0c"]
---

# [TMS] Resolução de Erro "Produto Não Atendido" no Cálculo de Pré-Conhecimento

## 1. Problema Relatado pelo Cliente:

O cliente informou que, ao realizar o cálculo de um pré-conhecimento, o sistema apresenta a mensagem de erro "Produto Não Atendido" e não exibe a tabela de frete correspondente. Além disso, o cálculo do pré-conhecimento não é concluído com sucesso.

## 2. Passo a Passo para Resolver o Problema:

Passo 1: Identificar a Tabela de Frete

No pré-conhecimento, verifique as seguintes informações:

- Transportadora
- Peso
- Cubagem
- Origem e Destino

Essas informações determinam qual tabela de frete deve ser utilizada.

Passo 2: Verificar o Produto no Pré-Conhecimento

Acesse a aba Mercadoria no pré-conhecimento.

Localize o Produto listado.

Clique no ícone de edição (lápis) ao lado do produto.

Na tela de Edição de Produto, anote o código do produto.

Passo 3: Validar o Produto com a Nota Fiscal

Acesse a Nota Fiscal correspondente.

Vá até a aba Itens e localize o código do produto.

Compare se o código do produto na nota fiscal é o mesmo que aparece no pré-conhecimento.

Se os códigos não coincidirem, pode haver um erro no cadastro do produto.

Passo 4: Acessar a Tabela de Frete

Acesse a "Tabela de Frete" no seguinte caminho: Cadastros gerais > Transportadoras > Negociações > Tabelas de frete

Passo 5: Verificar Restrições de Busca

Na Tabela de Frete, acesse a aba Restrições de Busca.

Selecione a opção Produtos.

Busque pelo produto cadastrado no pré-conhecimento.

Se o produto não estiver listado, o sistema pode não vinculá-lo corretamente à tabela de frete, gerando o erro "Produto Não Atendido".

Passo 6: Verificar se o Produto está Restrito

Ainda na aba Restrições de Busca, acesse a opção Produtos.

Verifique se o produto está configurado como "Produto Restrito".

Se o produto estiver como restrito, a tabela de frete será ignorada e o cálculo não será concluído.

Passo 7: Corrigir o Status do Produto

Se o produto estiver marcado como "Produto Restrito", remova-o da lista.

Adicione o produto novamente, desta vez configurando-o como "Atendido".

Isso permitirá que o sistema reconheça o produto corretamente e aplique a tabela de frete.

Passo 8: Recalcular o Pré-Conhecimento

Após as alterações, refaça o cálculo do pré-conhecimento.

O sistema deve concluir o cálculo com sucesso e exibir a tabela de frete correta.
