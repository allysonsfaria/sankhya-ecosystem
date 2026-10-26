---
id: "42950674870295"
titulo: "Problemas com Check-in e Check-out de Visitas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42950674870295-Problemas-com-Check-in-e-Check-out-de-Visitas"
trilha: "VIDYA: Vendas externas, televendas e entregas > Central de ajuda > Parceiros"
atualizado_em: "2026-08-24T16:59:57Z"
rotulos: ["sync_hc", "vidya", "vidya_593586", "sync_hash_a146ad7703b7"]
---

# Problemas com Check-in e Check-out de Visitas

📌 **Sintoma do Erro**
O vendedor não consegue iniciar o atendimento a um cliente na rota, fica impedido de lançar pedidos ou encontra o aplicativo bloqueado devido a pendências de marcações geográficas anteriores.

👀 **O que você vê nas Interfaces**

| **Ambiente / Módulo** | **Elementos e Alertas Exibidos na Tela** |
| --- | --- |
| **Painel de Visitas** | Alertas avisando sobre a existência de checkouts pendentes ou erros de validação de coordenadas geográficas (GPS). |

🕵️‍♂️ **Causas Mais Comuns**

- **Esquecimento de Saída:** O vendedor foi embora do cliente anterior sem clicar no botão de encerramento (check-out), bloqueando a abertura do próximo cliente.
- **Falta de Cadastro de Atividades:** Ausência de uma tabela de "Atividade" configurada e vinculada dentro do ERP Sankhya, o que impossibilita o app de computar o encerramento da visita.
- **Dessincronização de Tabelas:** Dados de visitas travados na memória cache local do aparelho do funcionário.

🛠️ **Como Corrigir o Problema**

1. **Regularizar Pendência:** Caso o app avise sobre um check-out pendente, oriente o vendedor a concluir a marcação de saída da visita anterior para liberar o novo check-in.
2. **Parametrização no ERP:** Acesse o Sankhya e certifique-se de que existe pelo menos uma "Atividade" cadastrada (mesmo que configurada como inativa), pois o app exige essa referência estrutural.
3. **Reset de Conexão Local:** Se o erro de check-out persistir mesmo com a atividade cadastrada, peça para o vendedor fazer logout (Sair) da sua conta no app e realizar um novo login para recarregar as tabelas lógicas.

💡 **Quando abrir chamado para a VidyaCode**

- Se o aplicativo falhar na validação de raio geográfico, aceitando marcações fora do perímetro real do estabelecimento.
- Caso os registros de entrada e saída feitos com sucesso no celular sumam ou não integrem nos relatórios gerenciais do Sankhya.
- Se houver a necessidade de incluir campos customizados obrigatórios (ex: caixa de texto para motivo da visita) no fluxo de check-in/out.
