---
id: "42950684701975"
titulo: "Desconto Embutido no Preço Unitário do Item"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42950684701975-Desconto-Embutido-no-Pre%C3%A7o-Unit%C3%A1rio-do-Item"
trilha: "VIDYA: Vendas externas, televendas e entregas > Central de ajuda > Produtos"
atualizado_em: "2026-08-24T17:00:57Z"
rotulos: ["sync_hc", "vidya", "vidya_593605", "sync_hash_dcb49d9368bc"]
---

# Desconto Embutido no Preço Unitário do Item

📌 **Sintoma do Erro**
Ao fechar uma venda, o desconto concedido abate diretamente o valor unitário do produto na nota, em vez de aparecer destacado de forma separada no campo de descontos do total do pedido, mascarando a tabela de preços oficial da empresa.

👀 **O que você vê nas Interfaces**

| **Ambiente / Módulo** | **Elementos e Alertas Exibidos na Tela** |
| --- | --- |
| **Resumo Financeiro / Totais** | O valor total do pedido bate com o esperado, mas o campo de desconto geral fica zerado e o preço de custo unitário do item aparece reduzido. |

🕵️‍♂️ **Causas Mais Comuns**

- **Regra de Desconto Promocional:** Existe uma promoção ativa vinculada à tabela de preços do cliente direto no ERP Sankhya (descontos promocionais de tabela sempre vêm embutidos no preço de custo enviado ao app).
- **Cadastro de Vendedor Incompleto:** Ausência de preenchimento dos parâmetros obrigatórios de "Desconto Máximo" e "Acréscimo Máximo" no usuário do vendedor no ERP, impossibilitando o app de calcular taxas manuais destacadas.
- **Incompatibilidade de Sincronização:** Aplicação de descontos em modo offline que sofrem recálculo estrutural automático ao conectar com o servidor.

🛠 **Como Corrigir o Problema**

1. **Auditoria de Promoções:** No Sankhya, cheque o cadastro do produto e da tabela de preços usada pelo cliente para verificar se o desconto não está embutido de fábrica como promocional.
2. **Completar Cadastro do Vendedor:** No ERP, acesse o usuário do vendedor e garanta o preenchimento exato dos limites permitidos nos campos de **Desconto Máximo** e **Acréscimo Máximo**.
3. **Uso de Inserção Manual:** Instrua o vendedor a aplicar o abatimento diretamente no campo específico de desconto manual dentro do item no aplicativo, garantindo o destaque visual separado no fechamento do pedido.

💡 **Quando abrir chamado para a VidyaCode**

- Se os parâmetros do vendedor estiverem preenchidos no Sankhya, mas as caixas de desconto manual sumirem ou continuarem inativas no aplicativo.
- Se houver divergências matemáticas superiores a 1% entre o desconto fixado no app e o valor que o pedido assume após sincronizar com o ERP.
- Caso o preço do item apareça reduzido sem que nenhuma regra de desconto promocional ou tabela especial esteja ativa no ERP.
