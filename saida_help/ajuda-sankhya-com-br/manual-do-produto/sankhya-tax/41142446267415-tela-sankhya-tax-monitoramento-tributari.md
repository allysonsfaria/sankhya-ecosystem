---
id: "41142446267415"
titulo: "Tela Sankhya Tax - Monitoramento Tributário"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/41142446267415-Tela-Sankhya-Tax-Monitoramento-Tribut%C3%A1rio"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Sankhya TAX"
atualizado_em: "2026-07-29T16:13:11Z"
rotulos: ["Configuração", "Fiscal", "UF", "Impostos", "NCM", "Sankhya Tax", "Monitoramento Tributário"]
---

# Tela Sankhya Tax - Monitoramento Tributário

**Módulo:** Sankhya Tax
**Caminho de acesso:** Menu Principal › Sankhya Tax - Monitoramento Tributário

---

## O que é e para que serve

O Monitoramento Tributário centraliza as alterações tributárias dos produtos cadastrados no Sankhya Om, exibindo diagnósticos, alertas e benefícios identificados pela inteligência tributária do Sankhya Tax com base nas regras tributárias vigentes para cada NCM e UF. A tela é atualizada diariamente (processamento às 02h) e apresenta um snapshot das ocorrências do dia, permitindo que você acompanhe, filtre e registre o status de cada monitoramento de forma centralizada. Ela **não** aplica automaticamente as alterações tributárias — você indica manualmente se a regra foi aplicada nos registros do ERP.

![Imagem 1: O Monitoramento Tributário centraliza as alterações tributárias dos produtos cadastrados no Sankhya Om, exibindo…](https://ajuda.sankhya.com.br/hc/article_attachments/41142474707607)

## Como usar a tela

Ao acessar a tela, você vê imediatamente seis cards com um panorama consolidado do monitoramento, seguido pelos filtros e a grade de ocorrências. Comece pela leitura dos cards para entender o cenário geral e, se necessário, refine a visualização usando os filtros.

## Cards de resumo

Os seis cards apresentam um snapshot das ocorrências identificadas no último processamento:

| Card | O que exibe |
| --- | --- |
| **Produtos monitorados** | Quantidade de produtos do Sankhya Om incluídos no monitoramento, com o total de NCMs distintos identificados no snapshot. |
| **Atenção** | Ocorrências com diagnóstico crítico que requerem ação imediata. |
| **Advertência** | Ocorrências que requerem análise, mas sem criticidade imediata. |
| **Benefícios** | Oportunidades de benefícios fiscais identificadas. |
| **UF mais recorrente** | Estado com maior número de ocorrências no período. |
| **Vigência futura – 30 dias** | Regras tributárias com início de vigência nos próximos 30 dias. |

## Filtros disponíveis

Use os filtros na barra superior para refinar a visualização da grade:

- **NCM** — filtra por código NCM específico.
- **UF** — filtra pelo estado de origem ou destino da operação.
- **Status de Aplicação** — filtra por Pendente, Ciente ou Descartado.
- **Grupo** — filtra pelo grupo tributário (ex: ICMS/ST Interno Simples).
- **Vigência** — filtra por intervalo de datas, limitado a 30 dias.

**💡 Dica**

Use o filtro **Status de Aplicação** para acompanhar o andamento: filtre por **Pendente** para ver o que ainda precisa de ação, por **Ciente** para revisar o que já foi analisado, ou por **Descartado** para visualizar ocorrências desconsideradas.

## Grade de monitoramentos

A grade exibe as ocorrências identificadas no snapshot com as seguintes colunas:

| Coluna | Descrição |
| --- | --- |
| **NCM** | Código NCM do produto monitorado. |
| **UF** | Estado ao qual a regra se aplica. |
| **Grupo** | Grupo tributário da ocorrência. |
| **Diagnóstico** | Classificação da ocorrência: Atenção, Advertência, Benefício ou Relatório. |
| **Itens** | Quantidade de itens do Sankhya Om associados ao NCM. |
| **Estoque** | Valor de estoque vinculado ao NCM. |
| **Vigência (30d)** | Indica se há regra com vigência iniciando nos próximos 30 dias. |
| **Próx. vigência** | Data de início da próxima vigência identificada. |

## Tipos de diagnóstico

Cada ocorrência recebe uma classificação que indica seu nível de prioridade:

| Diagnóstico | Significado |
| --- | --- |
| **Atenção** (vermelho) | Divergência crítica que requer revisão imediata. |
| **Advertência** (amarelo) | Ponto de atenção que requer análise. |
| **Benefício** (verde) | Oportunidade de benefício fiscal identificada. |
| **Relatório** (azul) | Informação de contexto sobre a regra tributária. |

## Ações em lote

Selecione uma ou mais linhas na grade usando as marcações à esquerda para acionar os botões da barra de ações:

### Marcar como pendente

Registra a ocorrência como pendente de análise. Use quando você identificou a ocorrência mas ainda precisa investigar ou tomar uma decisão.

### Marcar como aplicado

Registra que a regra foi aplicada ao produto no Sankhya Om. Este processo não é automatizado — você indica manualmente se fez o ajuste nas configurações tributárias do ERP.

### Marcar como descartado

Registra que a ocorrência foi descartada intencionalmente. Use quando a alteração não se aplica ao seu cenário operacional ou foi resolvida por outro meio.

**⚠️ Atenção**

O status registrado (**Pendente**, **Ciente** ou **Descartado**) é exibido na coluna **Status de Aplicação** e pode ser usado como filtro nas próximas consultas. Esses dados ficam armazenados para auditoria e rastreabilidade das decisões tributárias.

## Modal de detalhes

Clique em qualquer linha da grade para abrir um modal com informações detalhadas da ocorrência, incluindo:

- Dados do diagnóstico e do grupo tributário.
- Tabela de produtos vinculados ao NCM (produto, descrição, estoque).
- Detalhamento do alerta gerado pelo Sankhya Tax no campo **Detalhe**.
- MVA (Markup de Valor Agregado) aplicável, quando disponível para o grupo tributário.
- Embasamento legal da regra.

## Perguntas frequentes

#### Com que frequência a tela é atualizada?

O processamento ocorre uma vez ao dia, às 02h. O timestamp da última atualização é exibido no topo da tela.

#### O campo "Produtos monitorados" reflete quantos produtos?

Reflete a quantidade de produtos cadastrados no Sankhya Om incluídos no monitoramento tributário do Sankhya Tax.

#### O filtro de vigência tem alguma limitação?

Sim. O intervalo selecionável é limitado a 30 dias por consulta para manter a performance da tela.

#### O MVA aparece para todas as ocorrências?

Não. O MVA é exibido apenas no modal de detalhes e somente para os grupos tributários que retornam essa informação.

#### Posso desfazer um status que registrei?

Sim. Selecione a linha novamente e escolha o novo status desejado. O sistema atualiza o registro com a última ação registrada.

#### Onde os dados de monitoramento são armazenados?

Os dados do monitoramento tributário são guardados na tabela `TAIMONITORIA`. Todas as ocorrências, diagnósticos, status de aplicação e informações de vigência registradas nesta tela ficam armazenados nessa tabela para auditoria e consultas posteriores.
