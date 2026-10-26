---
id: "37666122735511"
titulo: "Como definir tabelas de preço por local"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37666122735511-Como-definir-tabelas-de-pre%C3%A7o-por-local"
trilha: "Universidade Sankhya > Jornada de Precificação"
atualizado_em: "2026-07-22T14:11:31Z"
rotulos: ["Produtos", "Configuração", "Estoque", "Preferências", "Comercial"]
---

# Como definir tabelas de preço por local

| Categoria |
| --- |
| [Qual é o objetivo de usar tabela de preços por local?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37666122735511-Como-definir-tabelas-de-pre%C3%A7o-por-local#h_01KEY9JN46JNKF51R6M7P19CJ6) |
| [Quais problemas este recurso resolve?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37666122735511-Como-definir-tabelas-de-pre%C3%A7o-por-local#h_01KEY9JN4A0934ADMFEQKCKTG1) |
| [Quais os riscos de não utilizar uma tabela de preço por local?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37666122735511-Como-definir-tabelas-de-pre%C3%A7o-por-local#h_01KEY9JN4M8GZWVNXMA0DAPZMV) |
| [Vídeo com demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37666122735511-Como-definir-tabelas-de-pre%C3%A7o-por-local#h_01KFBRCH63PBJB31FDTB8V75FA) |
| [Cenário prático e passo a passo para realizar a atividade no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37666122735511-Como-definir-tabelas-de-pre%C3%A7o-por-local#h_01KEYAAVX7EP0XY96QQH5FE9NC) |
| [É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37666122735511-Como-definir-tabelas-de-pre%C3%A7o-por-local#h_01KEY9K4KGGPQYAA4641NTFD6A) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37666122735511-Como-definir-tabelas-de-pre%C3%A7o-por-local#h_01KEY9K4N5T8Y847J7SW5NZPZC) |

## Definição de tabela de preço por local

#### Qual é o objetivo de usar tabela de preços por local?

O objetivo de usar a tabela de preços por local é adaptar a precificação às características de cada ponto físico de estoque, considerando variações logísticas, operacionais e comerciais. Essa prática permite definir preços mais alinhados à realidade de cada centro de distribuição ou filial, ajustando-se a fatores como custos de transporte, tributos regionais ou estratégias de vendas específicas. Além de apoiar a atuação comercial, essa abordagem contribui para uma visão mais estratégica da operação, otimizando recursos e fortalecendo o posicionamento da empresa em diferentes regiões.

#### Quais problemas este recurso resolve?

- Desalinhamento entre preços e custos regionais.
- Falta de competitividade em mercados regionais.
- Dificuldade em gerenciar estoques segmentados.
- Problemas com clientes regionais.
- Falta de controle sobre variações logísticas.

#### Quais os riscos de não utilizar uma tabela de preço por local?

A ausência de tabelas de preços por local pode levar à aplicação de preços inadequados em regiões com custos logísticos e operacionais distintos, o que compromete as margens de lucro e pode gerar prejuízos localizados. Sem essa personalização, a empresa perde capacidade de adaptação às particularidades de cada área, o que dificulta a gestão de estoque, a precificação coerente e a análise de rentabilidade regional. Isso também aumenta o risco de distorções comerciais, insatisfação de clientes e decisões estratégicas mal fundamentadas.

##### Vídeo com demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1052311651)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** A empresa Axis LTDA possui três centros de distribuição localizados em São Paulo, Rio de Janeiro e Minas Gerais. Cada local apresenta características peculiares, como custos logísticos, tributos e demandas específicas. Durante uma análise operacional, a equipe de gestão acordos que os preços uniformes para todos os locais geram margens de lucro inconsistentes. Por exemplo, em São Paulo, os altos custos de transporte reduziram a rentabilidade, enquanto em Minas Gerais, os incentivos fiscais locais não foram refletidos nos preços, o que poderia aumentar a competitividade. Para corrigir essas discrepâncias, a empresa decidiu implementar fórmulas de preço específicas para o local, ajustando a precificação às condições regionais.

**Tarefa:** Configure tabelas específicas para cada centro de distribuição, de acordo com as informações cadastradas em sua base de testes, seguindo as orientações indicadas.

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

1. Acesse a tela **Tabelas de Preços**
   Menu: Comercial » Arquivo » Tabelas de Preços

- Clique no botão “**+**” (**Cadastrar Cadastro de Tabela de Preço**).
- Informe um número de identificação no campo **Código**.
- Defina um nome para identificação no campo indicado (EX.:  LOCAL PADRÃO).
- Clique em **Salvar**.

  **Aba Histórico de atualizações**
- Informe o código **0** no campo **Tabela de origem**
- Preencha os campos **Dt. Vigor** e **Dt. Atualização** com a data atual.
- Informe **-5,00** no campo **Percentual**. 
  Esse campo definirá a aplicação de acréscimo ou desconto sobre o preço da tabela de origem.
- Clique em **Salvar**.
  Na sub aba **Exceções** pode-se criar exceções para produtos específicos, adicionando mais descontos ou acréscimos, ou também informando preços fixos diferenciados.

2. Acesse a tela **Preferências**
   Menu: Configurações » Avançado » Preferências

- Pesquise a chave **TIPTABPRECO** e tecle ENTER.
- Selecione **Local** no campo **Valor**.
- Clique em **Salvar**.

  Após alterar o parâmetro acima, feche a tela de **Tabela de Preço** para que a alteração seja refletida e, em seguida, abra-a novamente.

3. Acesse a tela **Tabelas de Preços**
   Menu: Comercial » Arquivo » Tabelas de Preços.

- Localize a tabela de preço que foi criada.
  Ao lado da aba de **Histórico de atualizações** foi criada uma nova aba.

**Aba Locais**

- Clique no botão “**+**” (**Cadastrar Locais Tabela de Preço**).
- Informe o código dos locais para aplicação da tabela, no campo **Cód. Local**.
- Clique em **Salvar**.

#### Correção e Repetição

- Revise os registros para confirmar se os passos foram seguidos.
- Caso haja erro no registro refaça a atividade seguindo o passo a passo novamente.
