---
id: "42950651598231"
titulo: "Lentidão Geral e Travamentos no Aplicativo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42950651598231-Lentid%C3%A3o-Geral-e-Travamentos-no-Aplicativo"
trilha: "VIDYA: Vendas externas, televendas e entregas > Central de ajuda > Configurações"
atualizado_em: "2026-08-24T16:08:27Z"
rotulos: ["sync_hc", "vidya", "sync_hash_3c809c1eb35f", "vidya_593588"]
---

# Lentidão Geral e Travamentos no Aplicativo

📌 **Sintoma do Erro**
O vendedor relata que o Vidya Force está operando de forma extremamente lenta na rua, apresentando gargalos de tempo ao registrar check-ins, salvar carrinhos ou tentar gerar PDFs.

👀 **O que você vê nas Interfaces**

| **Ambiente / Módulo** | **Elementos e Alertas Exibidos na Tela** |
| --- | --- |
| **Telas do Aplicativo** | Lentidão acentuada na transição de menus, botões que parecem não responder ao clique imediato e demora excessiva na renderização de documentos. |

🕵️‍♂️ **Causas Mais Comuns**

- **Sobrecarga de Dados Locais:** O vendedor acumulou uma quantidade muito grande de pedidos e orçamentos salvos no modo "Não Enviado" (offline), gerando um gargalo no banco de dados interno do celular.
- **Conexão de Rede Depreciada:** Sinais de internet móvel oscilando ou lentos demais na rota de trabalho, travando as requisições de segundo plano.
- **Saturação de Cache:** Armazenamento temporário do aplicativo sobrecarregado devido ao uso contínuo por longos períodos sem limpeza.
- **Token de Integração Expirado:** Credenciais lógicas de comunicação entre o gateway do sistema e o ERP Sankhya desatualizadas ou falhando.

🛠️ **Como Corrigir o Problema**

1. **Escoar Carga Offline:** Abra a aba de não enviados e certifique-se de escoar todos os pedidos pendentes conectando o aparelho a uma rede Wi-Fi estável para aliviar a memória do app.
2. **Limpeza do Cache Técnico:**

   - **No Android:** Vá em Configurações > Aplicativos > Vidya Force > Armazenamento > clicar em **Limpar Cache**.
   - **No iOS (iPhone):** Sincronize **todas** as vendas pendentes para não perder dados, desinstale o aplicativo e faça uma instalação limpa pela loja.
3. **Análise de Aparelho:** Certifique-se de que o smartphone do colaborador possui memória RAM e espaço em disco livre e que o sistema operacional não está desatualizado.

💡 **Quando abrir chamado para a VidyaCode**

- Se a lentidão operacional persistir mesmo após efetuar as limpezas de cache, escoamento de pedidos e reinstalação total do software.
- Quando o sintoma de lentidão severa atingir vários vendedores simultaneamente, apontando para gargalos no servidor.
- Se a tela acusar avisos contendo os termos técnicos "gateway", "token" ou "falha de comunicação com o servidor", o que exige atualização de credenciais na tela de Configurações Gateway no Sankhya.
