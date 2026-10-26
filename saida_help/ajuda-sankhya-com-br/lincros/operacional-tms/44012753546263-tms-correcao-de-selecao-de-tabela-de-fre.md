---
id: "44012753546263"
titulo: "[TMS] - Correção de Seleção de Tabela de Frete em Carga Fracionada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012753546263--TMS-Corre%C3%A7%C3%A3o-de-Sele%C3%A7%C3%A3o-de-Tabela-de-Frete-em-Carga-Fracionada"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T19:37:40Z"
rotulos: ["sync_hc", "lincros", "sync_hash_b253f57f358d", "lincros_13433283"]
---

# [TMS] - Correção de Seleção de Tabela de Frete em Carga Fracionada

## 1º Problema Relatado pelo Cliente:

O cliente informou que, ao processar determinadas cargas fracionadas, o sistema está atribuindo a tabela de frete errada. A tabela "Transportadora 1" está sendo selecionada quando, na verdade, a tabela correta seria "Transportadora 2". Este erro foi identificado em várias cargas fracionadas, e o cliente solicitou orientações sobre como corrigir a seleção da tabela de frete.

## 2° Passo a Passo para Resolver o Problema:

- Identificação do Problema:

O sistema está selecionando automaticamente a tabela de frete "Transportadora 1" devido a uma restrição de grupo de veículo associada a ela.

A tabela "Transportadora 2" deveria ser utilizada, mas essa tabela não possui a restrição de grupo de veículo necessária para a seleção correta.

- Verificação dos Dados das Cargas:

Acesse a tela de cargas fracionadas no sistema TMS.

Caminho: Operacional > Cargas > Cargas Fracionadas

Pesquise o número da carga fracionada afetada.

Selecione a carga fracionada e verifique a aba de pré-conhecimentos para identificar qual tabela de frete foi atribuída erroneamente.

- Análise das Tabelas de Frete:

Acesse a tela de tabelas de frete no TMS.

Caminho: Cadastros Gerais > Transportadoras > Negociações > Tabelas de Frete

Pesquise o nome da tabela de frete, como "Transportadora 1" e "Transportadora 2 ".

Selecione a tabela "Transportadora 1" e verifique a aba de restrições de busca.

Nessa aba, selecione a opção "Grupo de Veículos" e observe que a restrição de grupo de veículo está associada a esta tabela.

A tabela "Transportadora 2" precisa ser configurada para aceitar o grupo de veículo também, permitindo sua utilização nas cargas fracionadas.

- Solução:

Acesse a tela de tabelas de frete no TMS.

Caminho: Cadastros Gerais > Transportadoras > Negociações > Tabelas de Frete

Pesquise e selecione a tabela "Transportadora 2".

Na aba de restrições de busca, selecione a opção "Grupo de Veículos", pesquise pelo grupo de veículo correto e adicione essa restrição à tabela "Transportadora 2".

Após adicionar a restrição, vá para a tela de carga fracionada.

Caminho: Operacional > Cargas > Cargas Fracionadas

Pesquise e selecione a carga fracionada afetada.

Clique no botão Recalcular para que o sistema atualize os dados e atribua a tabela de frete correta às cargas fracionadas.

- Verificação Final:

Após o recalculo, retorne à tela de carga fracionada e confirme se a tabela correta, "Transportadora 2", foi atribuída às cargas fracionadas que apresentavam o erro.
