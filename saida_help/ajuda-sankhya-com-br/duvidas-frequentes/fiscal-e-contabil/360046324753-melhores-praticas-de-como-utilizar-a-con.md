---
id: "360046324753"
titulo: "Melhores práticas de como utilizar a contabilização de custo de produtos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360046324753-Melhores-pr%C3%A1ticas-de-como-utilizar-a-contabiliza%C3%A7%C3%A3o-de-custo-de-produtos"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-08-22T21:36:30Z"
rotulos: ["#criadoRoger", "Produtos", "Custos", "Configuração", "Contabilização", "Financeiro", "TGFCUSITE para custo por item TGFCUS para custo total", "Movimentos de entrada usam TGFCUSITE saída usa TGFCUS", "Não suporta dois critérios de rateio simultâneos"]
---

# Melhores práticas de como utilizar a contabilização de custo de produtos

#### Vejamos aqui, informações pertinentes sobre a utilização de custo e quais seus impactos na contabilização.

![Imagem 1: Diferença dos campos de custo da tabela de custo.](https://ajuda.sankhya.com.br/hc/article_attachments/19196002412695) Diferença dos campos de custo da tabela de **custo.**

- **TGFCUSITE.CUSMEDSEMICM** - Utilizada na contabilização do custo do item, utilização em conjunto com a conta variável do produto, mudando a visão documental de totais da nota para totais do item;
- **TGFCUS**.**CUSMEDSEMICM** - Utilizada na contabilização do custo total dos itens da nota, utilização em conjunto com contas variáveis diferentes do produto ou contas fixas;

Como foi explicado acima as duas variáveis não fazem referência as tabelas de custo da nota (TGFCUSITE) ou de custo do dia (TGFCUS).

Na contabilização dos movimentos de saída os resultados são obtidos na tabela de custo do dia (**TGFCUS**), com exceção dos movimentos de entrada em que os resultados priorizam a tabela de custo da nota (TGFCUSITE) e não existindo utilizam a tabela de custo do dia (TGFCUS).

![Imagem 2: Quanto a contabilização utilizando rateio como fonte para obtenção do CR e/ou Projeto, ou ainda como fonte para…](https://ajuda.sankhya.com.br/hc/article_attachments/19196002422039) Quanto a contabilização utilizando rateio como fonte para obtenção do CR e/ou Projeto, ou ainda como fonte para obtenção da conta contábil a ser utiliza na contabilização, esta configuração é incompatível com a contabilização na conta do produto uma vez que **no sistema não esta previsto** a aplicação de dois critérios de rateio.

**Conclusão:**

A contabilização pode ser; utilizando a conta do produto e o rateio dos valores fica por conta das diferentes contas contábeis dos produtos da nota; ou a contabilização pode ser utilizando a conta contábil, ou CR e Projetos do rateio, e o rateio dos valores fica por conta das diferentes naturezas, CR's e Projetos presentes no rateio;

Não estando então previsto a contabilização considerando dois critérios para rateio de valores.
