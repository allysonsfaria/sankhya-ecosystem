---
id: "42950678142231"
titulo: "Pedido Duplicado no ERP Sankhya"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42950678142231-Pedido-Duplicado-no-ERP-Sankhya"
trilha: "VIDYA: Vendas externas, televendas e entregas > Central de ajuda > Vendas"
atualizado_em: "2026-08-24T16:08:57Z"
rotulos: ["sync_hc", "vidya", "vidya_593600", "sync_hash_f8627c8a0f87"]
---

# Pedido Duplicado no ERP Sankhya

📌 **Sintoma do Erro**
O vendedor realiza a transmissão de uma venda pelo aplicativo e, ao checar o painel do ERP Sankhya, o sistema apresenta **dois registros idênticos** (mesmos itens, valores e cliente) com números únicos diferentes, mas gravados exatamente com o mesmo minuto de entrada.

👀 **O que você vê nas Interfaces**

| **Ambiente / Módulo** | **Elementos e Alertas Exibidos na Tela** |
| --- | --- |
| **Painel do ERP Sankhya** | Exibição de duas linhas de pedidos gêmeos geradas em lote para a mesma transação móvel. |

🕵️‍♂️ **Causas Mais Comuns**

- **Bug de Versões Obsoletas:** O smartphone está rodando uma versão desatualizada do aplicativo (versões de iOS inferiores à **864** possuíam essa falha de concorrência, já corrigida).
- **Ansiedade no Clique:** Conexões lentas de internet fazem o app demorar para responder, levando o vendedor a clicar repetidas vezes no botão de envio achando que o comando falhou.
- **Concorrência de Filas:** O envio manual de um pedido conflitando simultaneamente com a fila automática de transmissão de dados offline acumulados.

🛠 **Como Corrigir o Problema**

1. **Verificação de Versão:** No celular do vendedor, acesse **Menu > Configurações > Sobre** e verifique o número da build do aplicativo.
2. **Atualização Mandatória:** Caso esteja abaixo da versão **864** (iOS) ou equivalente (Android), faça a atualização imediata do app pelas lojas oficiais ou TestFlight.
3. **Treinamento de Campo (Clique Único):** Oriente a equipe técnica de vendas a clicar **apenas uma vez** no botão de envio e aguardar pacientemente a mensagem de sucesso ou erro gerada pelo próprio sistema, sem forçar cliques adicionais.
4. **Mapeamento de Reincidência:** Se o erro persistir após a atualização, anote o código do cliente (CODPARC), o código do vendedor, o horário exato e os números únicos gerados em duplicidade para fins de análise de banco de dados.

💡 **Quando abrir chamado para a VidyaCode**

- Se a duplicidade de pedidos continuar ocorrendo mesmo com toda a equipe utilizando as versões mais recentes e atualizadas do aplicativo.
- Se você possuir evidências claras (como gravações de tela ou logs) de que o vendedor realizou apenas um único clique e o app efetuou o disparo duplo.
- Caso ocorram mais de duas duplicidades documentadas na mesma semana após as orientações de uso terem sido repassadas.
