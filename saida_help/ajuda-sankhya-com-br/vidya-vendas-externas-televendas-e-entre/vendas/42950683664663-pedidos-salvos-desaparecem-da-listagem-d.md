---
id: "42950683664663"
titulo: "Pedidos Salvos Desaparecem da Listagem do App"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42950683664663-Pedidos-Salvos-Desaparecem-da-Listagem-do-App"
trilha: "VIDYA: Vendas externas, televendas e entregas > Central de ajuda > Vendas"
atualizado_em: "2026-08-24T16:09:03Z"
rotulos: ["sync_hc", "vidya", "vidya_593602", "sync_hash_18dcda3f5867"]
---

# Pedidos Salvos Desaparecem da Listagem do App

📌 **Sintoma do Erro**
O vendedor redige e salva um pedido (especialmente em cenários sem internet/offline), mas ao retornar para a tela de listagem de pedidos, o documento não aparece na lista, dando a falsa impressão de que a venda foi deletada.

👀 **O que você vê nas Interfaces**

| **Ambiente / Módulo** | **Elementos e Alertas Exibidos na Tela** |
| --- | --- |
| **Listagem de Pedidos** | Histórico de vendas em branco ou ocultando transações recém-concluídas pelo vendedor após a navegação por outras abas do sistema. |

🕵️‍♂️ **Causas Mais Comuns**

- **Filtros de Período Restritivos:** O pedido foi salvo com sucesso, mas a tela de listagem está configurada com um filtro de data muito curto que esconde a venda.
- **Bugs de Exibição Visual:** Falhas de renderização de tela em versões desatualizadas do aplicativo.
- **Retenção Offline:** Os pedidos estão guardados com segurança na memória local, mas ainda não constam na nuvem por falta de rede para transmissão.
- **Inconsistência de Cache:** Arquivos temporários corrompidos impedindo a atualização em tempo real da listagem de cards.

🛠 **Como Corrigir o Problema**

1. **Verificação de Lojas:** Garanta que o aplicativo esteja atualizado na última versão disponível no Google Play ou App Store.
2. **Afrouxar Filtros de Data:** Na tela de listagem de pedidos do app, acesse os filtros de período e amplie a busca (ex: mudar para exibir os últimos 30 dias) para verificar se o card reaparece.
3. **Forçar Varredura (Pull-to-Refresh):** Conecte o aparelho a uma rede estável e, na tela inicial do app, puxe a interface para baixo para forçar a sincronização e reindexar os arquivos locais.
4. **Isolamento de Causa (Troca de Aparelho):** Se o erro persistir com um único funcionário, logue a conta dele em outro celular. Se os pedidos aparecerem, o erro está no smartphone original, exigindo a limpeza de cache ou reinstalação do app.

💡 **Quando abrir chamado para a VidyaCode**

- Se os rascunhos salvos continuarem invisíveis mesmo após a atualização do aplicativo e abertura total dos filtros de data.
- Quando pedidos que já haviam sido sincronizados com sucesso sumirem misteriosamente da listagem de vendas.
- Se a tentativa de abrir a tela de listagem disparar pop-ups com mensagens de erro do sistema.
