---
id: "42950729988119"
titulo: "Pedido Travado na Aba \"Pendentes\" e não Sobe para o ERP"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42950729988119-Pedido-Travado-na-Aba-Pendentes-e-n%C3%A3o-Sobe-para-o-ERP"
trilha: "VIDYA: Vendas externas, televendas e entregas > Central de ajuda > Vendas"
atualizado_em: "2026-08-24T16:09:21Z"
rotulos: ["sync_hc", "vidya", "vidya_593607", "sync_hash_59f730838ba8"]
---

# Pedido Travado na Aba "Pendentes" e não Sobe para o ERP

📌 **Sintoma do Erro**
O pedido é finalizado pelo vendedor no celular, mas fica permanentemente preso na aba de "Pendentes" ou gera mensagens de erro de envio, impossibilitando a chegada do documento de venda no ERP Sankhya.

👀 **O que você vê nas Interfaces**

| **Ambiente / Módulo** | **Elementos e Alertas Exibidos na Tela** |
| --- | --- |
| **Aba Pendentes / Transmissão** | Cards de pedidos com marcadores de erro ou travados com status pendente mesmo após sucessivos cliques de sincronização. |

🕵️‍♂️ **Causas Mais Comuns**

- **Dados Expirados no ERP:** O pedido utiliza um Centro de Custo ou Centro de Resultado cuja data de validade está vencida nas tabelas do Sankhya.
- **Carga de Cadastros Defasada:** Clientes, produtos ou regras de preço modificados no ERP enquanto o app operava com dados locais desatualizados.
- **Edição Concorrente:** Tentativa de alteração de dados do pedido enquanto o smartphone estava instável ou sem sinal de rede.
- **Permissões de Sistema Revogadas:** O sistema operacional do celular bloqueou o acesso do Vidya Force ao armazenamento ou dados móveis após uma atualização do smartphone.

🛠 **Como Corrigir o Problema**

1. **Forçar Recarga de Sessão:** Peça para o vendedor ir em Perfil, clicar em Sair, realizar um novo login e puxar a tela inicial para baixo para reatar a comunicação com o servidor.
2. **Ajuste de Validade de Centros:** Se o erro acusar problemas de centro de custo/resultado, acesse o cadastro correspondente no Sankhya, estenda a data de validade para um período futuro e peça para o vendedor sincronizar.
3. **Descarte de Rascunho Travado:** Se o pedido continuar preso na aba Pendentes mesmo após as correções, delete o rascunho travado no app e lance a venda do zero (evite tentar editar o rascunho antigo corrompido).
4. **Auditoria de Permissões de OS:** Vá nas configurações de aplicativos do smartphone (Android ou iOS), selecione o Vidya Force e garanta que todas as permissões de armazenamento, rede e localização estejam ativadas.

💡 **Quando abrir chamado para a VidyaCode**

- Se o ciclo de logout, login e sincronização for feito, os cadastros de centros estiverem corretos e o pedido continuar rejeitado.
- Caso as caixas de erro exibam termos genéricos que não façam referência a cadastros ou regras comerciais do ERP.
- Se o problema travar o fluxo de faturamento de múltiplos vendedores ao mesmo tempo.
