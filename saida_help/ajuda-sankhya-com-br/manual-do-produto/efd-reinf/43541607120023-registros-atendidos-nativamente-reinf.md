---
id: "43541607120023"
titulo: "Registros atendidos nativamente - REINF"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43541607120023-Registros-atendidos-nativamente-REINF"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Escriturações e Declarações   > EFD-Reinf"
atualizado_em: "2026-09-16T18:20:39Z"
---

# Registros atendidos nativamente - REINF

Este artigo apresenta o **mapa de eventos da EFD-Reinf**, agrupado por tipo e na mesma ordem em que os eventos são transmitidos. Use-o como referência rápida para identificar a que informação cada evento corresponde, conferir se a escrituração do período contém os eventos esperados e localizar a origem de uma inconsistência apontada no retorno do ambiente nacional.

Os eventos se dividem em quatro naturezas: **tabelas** (série R-1000), que carregam os dados cadastrais e devem ser enviadas antes dos demais; **periódicos** (séries R-2000 e R-4000), de apuração mensal; **não periódicos** (série R-3000), vinculados a um fato específico; e os eventos de **exclusão e de retorno** (série R-9000).

**Observação:** os eventos de retorno (R-9001, R-9005, R-9011 e R-9015) não são transmitidos pelo contribuinte — são gerados pelo ambiente nacional da EFD-Reinf em resposta aos envios e ficam disponíveis para consulta. Os eventos R-9001 e R-9011 substituíram, respectivamente, os antigos R-5001 e R-5011.

| Tipo | Evento | Descrição |
| --- | --- | --- |
| **Tabelas** | **R-1000** | Informações do Contribuinte |
| **R-1050** | Tabela de Entidades Ligadas |
| **R-1070** | Tabela de Processos Adm./Judiciais |
| **Periódicos** | **R-2010** | Retenção CP – Serviços Tomados |
| **R-2020** | Retenção CP – Serviços Prestados |
| **R-2030** | Recursos Recebidos por Assoc. Desportiva |
| **R-2040** | Recursos Repassados para Assoc. Desportiva |
| **R-2050** | Comercialização de Produção Rural |
| **R-2055** | Aquisição de Produção Rural |
| **R-2060** | CPRB |
| **R-2098** | Reabertura da Série R-2000 |
| **R-2099** | Fechamento da Série R-2000 |
| **Não Periódicos** | **R-3010** | Receita de Espetáculo Desportivo |
| **Periódicos** | **R-4010** | Pagamento/Crédito a Beneficiário PF |
| **R-4020** | Pagamento/Crédito a Beneficiário PJ |
| **R-4040** | Pagamento a Beneficiários Não Identificados |
| **R-4080** | Retenção no Recebimento |
| **R-4099** | Fechamento/Reabertura da Série R-4000 |
| **Exclusão** | **R-9000** | Exclusão de Eventos |
| **Retorno** | **R-9001** | Totalização CP (ex-R-5001) |
| **R-9005** | Totalização das Retenções na Fonte |
| **R-9011** | Consolidação CP (ex-R-5011) |
| **R-9015** | Consolidação das Retenções na Fonte |
