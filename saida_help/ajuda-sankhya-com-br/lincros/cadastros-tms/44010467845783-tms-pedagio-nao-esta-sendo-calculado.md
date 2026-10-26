---
id: "44010467845783"
titulo: "[TMS] - Pedágio não está sendo calculado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010467845783--TMS-Ped%C3%A1gio-n%C3%A3o-est%C3%A1-sendo-calculado"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T18:39:32Z"
rotulos: ["sync_hc", "lincros", "sync_hash_1960b96f73ae", "lincros_13432481"]
---

# [TMS] - Pedágio não está sendo calculado

## 1 - Problema Relatado pelo Cliente:

O cliente informou que, ao calcular o frete no pré-conhecimento, mesmo o componente de pedágio estando devidamente incluído dentro da referida tabela de frete, o valor do pedágio não estava sendo calculado, resultando em um valor total do frete incorreto porque faltou o valor do pedágio.

## 2 - Passo a Passo para Resolver o Problema:

Siga as etapas abaixo para corrigir o cálculo do pedágio:

Acesse a tabela de frete utilizada no pré-conhecimento, seguindo o caminho:
**Cadastros Gerais > Transportadoras > Negociações > Tabelas de Frete.**

Na tela seguinte, pesquise e acesse a tabela de frete que está sendo utilizada no pré-conhecimento.

![Imagem 1: Na tela seguinte, pesquise e acesse a tabela de frete que está sendo utilizada no pré-conhecimento.](https://ajuda.sankhya.com.br/hc/article_attachments/44010468084375)

Dentro da tabela de frete, localize a rota utilizada e clique no ícone de lápis para editar.

![Imagem 2: Dentro da tabela de frete, localize a rota utilizada e clique no ícone de lápis para editar.](https://ajuda.sankhya.com.br/hc/article_attachments/44010468202263)

Na tela de edição, marque a flag de pedágio para ativar o cálculo do pedágio.

Após marcar a flag de pedágio, salve as alterações realizadas.

![Imagem 3: Após marcar a flag de pedágio, salve as alterações realizadas.](https://ajuda.sankhya.com.br/hc/article_attachments/44010486058903)

Volte ao pré-conhecimento, exclua a tabela de frete e recalcule o frete para verificar se o pedágio foi corretamente incluído.

![Imagem 4: Volte ao pré-conhecimento, exclua a tabela de frete e recalcule o frete para verificar se o pedágio foi corretamente…](https://ajuda.sankhya.com.br/hc/article_attachments/44010486190103)

## 3 - Pedágio calcula, mas com valor incorreto (Mínimo x Fixo):

Se a flag de pedágio já está marcada e o componente aparece no movimento, mas o **valor calculado não confere** com o acordado (geralmente aparece sempre o mesmo valor "mínimo", independente da rota ou peso), o motivo costuma ser a forma de cadastro do componente na tabela de frete.

Um equívoco comum é confundir os campos **Valor Fixo** e **Valor Mínimo**:

- Use **Valor Mínimo** quando o pedágio negociado é um valor fixo por faixa/rota (não multiplica por peso ou distância).
- Use **Valor Fixo** quando o pedágio deve ser multiplicado por uma variável (ex: peso, KM ou fração).

Para corrigir: acesse Cadastros Gerais > Transportadoras > Negociações > Tabelas de Frete, edite o componente de pedágio na rota em questão e confirme em qual desses dois campos o valor foi informado. Após ajustar, recalcule o pré-conhecimento.

Consulte também: [TMS] - Componente de frete 'Forma de Cálculo do Pedágio' por fração KG.
