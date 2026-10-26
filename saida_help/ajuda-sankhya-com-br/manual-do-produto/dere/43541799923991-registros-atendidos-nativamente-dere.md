---
id: "43541799923991"
titulo: "Registros atendidos nativamente - DeRE"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43541799923991-Registros-atendidos-nativamente-DeRE"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Escriturações e Declarações   > DeRE"
atualizado_em: "2026-09-17T13:13:06Z"
---

# Registros atendidos nativamente - DeRE

Este artigo apresenta o **mapa de eventos da DeRE – Declaração de Regimes Específicos**, agrupado por tipo e na mesma ordem em que os eventos são transmitidos. Use-o como referência rápida para identificar a que informação cada evento corresponde, conferir se a declaração do período contém os eventos esperados e localizar a origem de uma inconsistência apontada no retorno do Fisco.

A DeRE é a obrigação acessória da Reforma Tributária (EC 132/2023) destinada aos contribuintes de **regimes específicos** de CBS e IBS, como serviços financeiros, planos de assistência à saúde e concursos de prognósticos. Seus eventos se dividem em três naturezas: **tabela** (série D-1000), com os dados cadastrais e o Plano Geral de Contas Comentado, que devem ser enviados antes dos demais; **periódicos**, de apuração mensal; e de **retorno** (série D-9000), devolvidos pelo ambiente do Fisco.

**Observação:** a DeRE está em implantação por fases e o leiaute segue em evolução. Os eventos marcados como Em construção ainda não estão disponíveis no Sankhya — consulte as notas de versão para acompanhar a liberação.

| Tipo | Evento | Descrição | Considerações |
| --- | --- | --- | --- |
| **Tabela** | **D-1001** | Informações do Contribuinte | Em construção |
| **D-1011** | Plano Geral de Contas Comentado | Em construção |
| **Periódico** | **D-1101** | Balancete Mensal | — |
| **D-1106** | Identificação de Aplicações Financeiras | — |
| **D-1199** | Fechamento Mensal | — |
| **D-2101** | Débito em Operações com Títulos de Dívida com Oferta Pública (exclusivo para Serviços Financeiros) | — |
| **Retorno** | **D-9001** | Retorno – Eventos de Tabela | Estes eventos são gerados pelo Fisco após a transmissão do arquivo. Sendo assim, são recepcionados pela Sankhya para acompanhamento e tratativas do usuário. |
| **D-9101** | Retorno Totalizador – Balancete Mensal |
| **D-9106** | Retorno Totalizador – Identificação de Aplicações Financeiras |
| **D-9121** | Retorno Totalizador – Débito em Operações com Títulos de Dívida com Oferta Pública (exclusivo para Serviços Financeiros) |
| **D-9199** | Retorno Totalizador – Fechamento Mensal |
