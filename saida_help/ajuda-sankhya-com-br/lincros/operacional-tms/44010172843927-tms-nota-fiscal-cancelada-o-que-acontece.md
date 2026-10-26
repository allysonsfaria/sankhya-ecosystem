---
id: "44010172843927"
titulo: "[TMS] - Nota fiscal cancelada: o que acontece no sistema e como identificar automaticamente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010172843927--TMS-Nota-fiscal-cancelada-o-que-acontece-no-sistema-e-como-identificar-automaticamente"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T18:31:05Z"
rotulos: ["sync_hc", "lincros", "lincros_17153881", "sync_hash_ba4888c3de06"]
---

# [TMS] - Nota fiscal cancelada: o que acontece no sistema e como identificar automaticamente

**Menu**: Operacional > Documentos de despacho > Notas Fiscais

**Objetivo**: Entender o que acontece no sistema quando uma nota fiscal é cancelada, por que ela não pode ser excluída, e como identificar o cancelamento sem depender de auditoria manual.

## Por que a NF cancelada não pode ser excluída

Notas fiscais, mesmo canceladas, precisam permanecer registradas no sistema por questão de rastreabilidade fiscal e de auditoria. A exclusão física do registro removeria esse histórico, o que não é uma opção disponível nem desejável para a conformidade da operação — isso vale mesmo quando o cancelamento já foi confirmado na SEFAZ.

O caminho correto para uma NF que não deve mais ser considerada é o cancelamento. Uma vez cancelada, ela permanece no sistema com a situação "Cancelada" claramente identificada, sem poder ser removida.

## Como registrar o cancelamento no sistema

Existem duas formas:

## 1. Importação manual do XML de evento de cancelamento

Caminho: Operacional > Importação > Importação Eventos Nota Fiscal. Basta importar o arquivo XML de cancelamento, disponível no portal da SEFAZ ou com o emissor da nota.

## 2. Botão "Recuperar Sefaz" (tela de Notas Fiscais)

Na tela de Notas Fiscais (Operacional > Documentos de despacho > Notas fiscais), existe o botão **"Recuperar Sefaz"**. Com ele, ao selecionar a nota, o próprio sistema busca o evento de cancelamento diretamente na SEFAZ, atualizando a situação para "Cancelada" sem a necessidade de baixar e subir o arquivo XML manualmente.

Para esse botão funcionar, é necessário que o **Certificado Digital A1** da empresa esteja configurado no TMS, em: Cadastros gerais > Configurações da empresa > Gerais > Certificado digital.

## Impacto em relatórios e dashboards

Como o cancelamento não pode ser resolvido por exclusão, quando uma NF cancelada continua aparecendo como pendente em relatórios ou dashboards próprios do cliente, a recomendação é ajustar o filtro do relatório para desconsiderar notas fiscais com situação "Cancelada" na consulta de pendentes — em vez de tentar removê-las do sistema.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
