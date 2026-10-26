---
id: "35837175655447"
titulo: "Códigos de resposta do eSocial: envio e processamento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35837175655447-C%C3%B3digos-de-resposta-do-eSocial-envio-e-processamento"
trilha: "Manual do Produto > Pessoas+ > eSocial > Retornos e Erros do eSocial"
atualizado_em: "2026-10-14T18:22:21Z"
rotulos: ["Eventos", "Central de Vendas", "XML", "SEFAZ", "eSocial", "Central do eSocial", "Erro", "Códigos de resposta do processamento do Evento", "Processamento do Lote", "Códigos e Mensagens de retorno do envio"]
---

# Códigos de resposta do eSocial: envio e processamento

Ao enviar e processar lotes de eventos para o eSocial, o sistema pode retornar diferentes códigos de resposta, indicando o status do envio ou eventuais inconsistências encontradas.

Abaixo estão listados os principais códigos e mensagens de retorno conforme o [Manual de Orientação do Desenvolvedor do eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/manualorientacaodesenvolvedoresocialv1-15.pdf).

#### Códigos e Mensagens de retorno do envio e Processamento do Lote

| **Código** | **Descrição** |
| --- | --- |
| 101 | Lote aguardando processamento |
| 201 | Lote processado com sucesso |
| 202 | Lote processado com advertências |
| 301 | Erro no servidor do eSocial |
| 401 | Lote incorreto – erro de preenchimento |
| 402 | Lote incorreto – schema inválido |
| 403 | Leiaute incorreto – versão do schema não permitida |
| 404 | Lote incorreto – erro no certificado digital |
| 405 | Lote incorreto – lote nulo ou vazio |
| 501 | Solicitação de consulta incorreta – erro de preenchimento |
| 502 | Solicitação de consulta incorreta – schema inválido |
| 503 | Solicitação de consulta incorreta – versão do schema não permitida |
| 504 | Solicitação de consulta incorreta – erro no certificado digital |
| 505 | Solicitação de consulta incorreta – consulta nula ou vazia |

#### Códigos de resposta do processamento do Evento

| **Categoria** | **Código** | **Descrição** |
| --- | --- | --- |
| **Sucesso** | 201 | Sucesso - lote recebido com sucesso. |
| 202 | Sucesso com advertência - lote recebido com advertência. |
| **Erro eSocial** | 301 | Erro no servidor do eSocial. |
| **Erro do usuário** | 401 | Erro no conteúdo do evento – lote incorreto ou erro de preenchimento. |
| 402 | Schema inválido - lote incorreto. |
| 403 | Leiaute inválido – versão do schema não permitida. |
| 404 | Erro no certificado digital da assinatura do evento. |
| 405 | Erro na assinatura do evento – lote nulo ou vazio. |
| 406 | Evento não pertence ao grupo especificado no lote de eventos. |
