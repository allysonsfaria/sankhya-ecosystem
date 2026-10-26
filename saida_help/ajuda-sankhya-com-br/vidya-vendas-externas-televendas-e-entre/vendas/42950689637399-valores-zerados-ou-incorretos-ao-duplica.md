---
id: "42950689637399"
titulo: "Valores Zerados ou Incorretos ao Duplicar Pedidos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42950689637399-Valores-Zerados-ou-Incorretos-ao-Duplicar-Pedidos"
trilha: "VIDYA: Vendas externas, televendas e entregas > Central de ajuda > Vendas"
atualizado_em: "2026-08-24T16:09:27Z"
rotulos: ["sync_hc", "vidya", "vidya_593608", "sync_hash_fb8d456ff6e7"]
---

# Valores Zerados ou Incorretos ao Duplicar Pedidos

📌 **Sintoma do Erro**
Ao utilizar o comando de clonar/duplicar um pedido existente no aplicativo para agilizar um novo faturamento, as mercadorias são carregadas no novo carrinho com preços zerados ou com valores totalmente diferentes do documento de venda original.

👀 **O que você vê nas Interfaces**

| **Ambiente / Módulo** | **Elementos e Alertas Exibidos na Tela** |
| --- | --- |
| **Carrinho de Duplicação** | Listagem de itens clonados exibindo valores comerciais zerados ou campos de descontos e acréscimos desconfigurados. |

🕵️‍♂️ **Causas Mais Comuns**

- **Origem Faturada:** Tentativa de duplicar pedidos cujo status original já consta como **Faturado** no ERP (esta condição costuma disparar o erro nativamente).
- **Preços Ajustados Manualmente:** O pedido original possuía alterações manuais de preço feitas item por item antes da clonagem.
- **Descontos/Acréscimos Mistos:** Presença de regras comerciais híbridas no mesmo documento (mescla de descontos percentuais com valores em dinheiro fixos).
- **Defasagem de Tabelas locais:** Tabelas de preço locais sem atualização ou aplicativo rodando em builds obsoletas.

🛠 **Como Corrigir o Problema**

1. **Isolamento de Status:** Verifique o status atual do pedido de origem. Caso ele já esteja faturado, teste fazer a duplicação utilizando um pedido em outra fase (ex: liberado ou em separação) para checar o comportamento.
2. **Ajuste Manual Preventivo:** Após executar a duplicação, oriente o vendedor a fazer uma varredura fina no carrinho, inserindo manualmente os valores e descontos caso as regras mistas tenham limpado os campos.
3. **Atualização e Sincronismo:** Force uma atualização completa de dados no menu de sincronização do aplicativo e verifique na aba lateral se o app está operando em sua versão mais recente.

💡 **Quando abrir chamado para a VidyaCode**

- Se o erro de valores zerados se manifestar na duplicação de pedidos que **não estão faturados**.
- Se o problema de distorção de preços na clonagem persistir mesmo com o aplicativo limpo e atualizado na última build de mercado.
- Sempre que conseguir reproduzir o travamento de valores de forma consistente (neste caso, anote o número do pedido original e envie fotos ou vídeos do comportamento no chamado).
