---
id: "37665683126039"
titulo: "Como definir tabelas de preço por parceiro"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37665683126039-Como-definir-tabelas-de-pre%C3%A7o-por-parceiro"
trilha: "Universidade Sankhya > Jornada de Precificação"
atualizado_em: "2026-07-22T14:11:32Z"
rotulos: ["Configuração", "Parceiro", "ERP Sankhya", "Comercial", "Tabelas de Preço"]
---

# Como definir tabelas de preço por parceiro

| Categoria |
| --- |
| [Qual é o objetivo de se definir a tabela de preços por parceiro?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37665683126039-Como-definir-tabelas-de-pre%C3%A7o-por-parceiro#h_01KEY8YAXB2P195F3Q0065NGZA) |
| [Quais problemas este recurso resolve?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37665683126039-Como-definir-tabelas-de-pre%C3%A7o-por-parceiro#h_01KEY8YAXEHRQ5XCSASQGH0SXF) |
| [Quais os riscos de não utilizar a tabela de preço por parceiro?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37665683126039-Como-definir-tabelas-de-pre%C3%A7o-por-parceiro#h_01KEY8YAXS4YQS49RM7X3SHFNR) |
| [Vídeo com demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37665683126039-Como-definir-tabelas-de-pre%C3%A7o-por-parceiro#h_01KFBQWR5DKQT0RZH8EXD3ADA4) |
| [Cenário prático e passo a passo para realizar a atividade no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37665683126039-Como-definir-tabelas-de-pre%C3%A7o-por-parceiro#h_01KEY91DQAPS4AJ8V4D20RC12E) |
| [É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37665683126039-Como-definir-tabelas-de-pre%C3%A7o-por-parceiro#h_01KEY8YSZGB1YNT6W8WGNH8YZF) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37665683126039-Como-definir-tabelas-de-pre%C3%A7o-por-parceiro#h_01KEY8YT196N1KPE3ETQ9R6715) |

## Definição de tabela de preço por parceiro

#### Qual é o objetivo de se definir a tabela de preços por parceiro?

Fornecer uma personalização individualizada na precificação, ajustando os preços às necessidades, demandas, histórico de relacionamento e outras particularidades de cada cliente. Essa prática permite alinhar os preços com as expectativas específicas de cada parceiro, promovendo maior competitividade, fidelidade e satisfação. Além disso, ao atender de forma personalizada, a empresa fortalece suas relações comerciais e otimiza as condições de negociação, garantindo margens de lucros ajustadas às particularidades de cada cliente. Por outro lado, será possível que vários clientes compartilhem a mesma tabela, possibilitando o equilíbrio da personalização com eficiência operacional.

#### Quais problemas este recurso resolve?

- Falta de personalização na precificação.
- Insatisfação dos clientes com condições comerciais genéricas.
- Dificuldade em gerenciar condições específicas para clientes estratégicos.
- Inconsistências na aplicação de preços.
- Dificuldade em equilibrar personalização e eficiência operacional.

#### Quais os riscos de não utilizar a tabela de preço por parceiro?

A ausência de tabelas de preços personalizadas por parceiro expõe a empresa a riscos como insatisfação de clientes, especialmente aqueles que esperam condições ajustadas às suas necessidades ou histórico de relacionamento. Isso pode levar à perda de parceiros estratégicos para concorrentes que oferecem maior flexibilidade na precificação. Além disso, a aplicação de condições comerciais genéricas dificulta a fidelização, simplifica a competitividade e limita a capacidade de atender clientes com perfis diferentes. A falta de personalização também aumenta o risco de margens de lucro inconsistentes, prejudicando a sustentabilidade financeira, e dificultando negociações estratégicas, afetando o desempenho comercial da empresa.

##### Vídeo com demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1052318835)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** A **Axis LTDA** atende diversos tipos de clientes, desde pequenos varejistas até grandes redes de supermercados e distribuidores. Durante uma análise de mercado, uma equipe comercial acordos que a aplicação de uma tabela de preços genérica estava dificultando as negociações com clientes estratégicos e gerando insatisfação em alguns parceiros. Grandes redes projetaram preços mais competitivos devido ao alto volume de compras, enquanto pequenos varejistas esperavam condições diferenciadas para volumes menores. Para atender melhor às expectativas de cada parceiro e fortalecer as relações comerciais, a empresa decidiu implementar tabelas de preços personalizadas para o parceiro.

**Tarefa:** Configure tabelas de preços específicas para cada cliente, ou grupo de clientes, na sua base de testes, conforme as orientações indicadas.

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

1. Acesse a tela **Tabelas de Preços**
   Menu: Comercial » Arquivo » Tabelas de preços

- Clique no botão “**+**” (**Cadastrar Cadastro de Tabela de Preço**).
- Informe um número de identificação no campo **Código**.
- Defina um nome para identificação no campo indicado (EX.: PARCEIROS).
- Clique em **Salvar**.

**Aba Histórico de atualizações**

- Informe o código **0** no campo **Tabela de origem**
- Preencha os campos **Dt. Vigor** e **Dt. Atualização** com a data atual.
- Informe **-5,00** no campo **Percentual**. 
  Esse campo definirá a aplicação de acréscimo ou desconto sobre o preço da tabela de origem.
- Clique em **Salvar**.

2. Acesse a tela **Preferências** 
   Menu: Configurações » Avançado » Preferências

- Pesquise a chave **TIPTABPRECO** e tecle ENTER.
- Selecione **Parceiro** no campo **Valor**.
- Clique em **Salvar**.

Após alterar o parâmetro acima, feche a tela de **Tabela de Preço** para que a alteração seja refletida e, em seguida, abra-a novamente.

3. Acesse a tela **Tabelas de Preços**
   Menu: Comercial » Arquivo » Tabelas de Preços

- Localize a tabela de preço do parceiro que foi criada.

Ao lado da aba de **Histórico de atualizações** foi criada uma nova aba.

**Aba Parceiros**

- Clique no botão “**+**” (**Cadastrar Parceiro Tabela de Preço**).
- Informe o **código do parceiro** no campo indicado.
- Clique em **Salvar**.

#### Correção e Repetição

- Revise os registros para confirmar se os passos foram seguidos.
- Caso haja erro no registro refaça a atividade seguindo o passo a passo novamente.
