---
id: "42950650289431"
titulo: "Erro ao Enviar ou Finalizar Pedidos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42950650289431-Erro-ao-Enviar-ou-Finalizar-Pedidos"
trilha: "VIDYA: Vendas externas, televendas e entregas > Central de ajuda > Vendas"
atualizado_em: "2026-08-24T16:08:09Z"
rotulos: ["sync_hc", "vidya", "sync_hash_fec414cc8106", "vidya_593585"]
---

# Erro ao Enviar ou Finalizar Pedidos

📌 **Sintoma do Erro**
Ao tentar fechar uma venda ou orçamento no carrinho de compras, o aplicativo exibe um erro, travando o pedido no aparelho e impedindo o envio do documento para faturamento no Sankhya.

👀 **O que você vê nas Interfaces**

| **Ambiente / Módulo** | **Elementos e Alertas Exibidos na Tela** |
| --- | --- |
| **Fechamento de Pedido** | Alertas vermelhos de erro com códigos técnicos, botões de envio travados ou o pedido desaparecendo temporariamente após a tentativa de transmissão. |

🕵️‍♂️ **Causas Mais Comuns**

- **Quebra de Regras do ERP:** Um ou mais produtos inseridos violam regras de quantidade mínima de venda estabelecidas no Sankhya ou restrições cadastrais do cliente.
- **Caracteres Proibidos:** Uso de emojis, símbolos especiais ou pontuações fora do padrão dentro do campo de observações gerais do pedido.
- **Dessincronização:** Falha de comunicação ou interrupção de pacotes de dados após a última modificação no carrinho.

🛠️ **Como Corrigir o Problema**

1. **Ciclo de Sincronização:** Feche o aplicativo por completo (mate o processo no gerenciador do celular), abra-o novamente e aguarde a sincronização automática de rotina finalizar antes de tentar reenviar.
2. **Ajustar Mínimos de Estoque:** Avalie se o erro detalha restrições de quantidade (ex: "produto X precisa ser >= 5"). Oriente o vendedor a adequar a quantidade ou remover o item.
3. **Higienizar Observações:** Delete quaisquer emojis, caracteres especiais ou acentuações complexas inseridas nas caixas de texto de observação do pedido e tente transmitir.
4. **Refazer em Contingência:** Como último recurso em casos de rascunhos corrompidos localmente, delete o pedido travado e lance a venda do zero (não tente editar o rascunho antigo).

💡 **Quando abrir chamado para a VidyaCode**

- Se o erro de transmissão persistir após fechar e reabrir o aplicativo por 3 vezes consecutivas.
- Se o alerta trouxer termos puramente sistêmicos como "null", "timeout" ou "Erro 500".
- Se você checar todas as regras e travas de quantidade no Sankhya e constatar que não há impedimentos comerciais no ERP.
