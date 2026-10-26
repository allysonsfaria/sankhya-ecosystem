---
id: "13976871754647"
titulo: "Pedido de Compra continua pendente após faturado totalmente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/13976871754647-Pedido-de-Compra-continua-pendente-ap%C3%B3s-faturado-totalmente"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T14:59:44Z"
rotulos: ["DUVIDANF", "Configuração", "NF-e", "Faturamento", "Pedido de Compra", "Estoque", "Correção de Trigger", "Erro"]
---

# Pedido de Compra continua pendente após faturado totalmente

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16912115788823) SITUAÇÃO:**

Pedido de Compra ao ser faturado integralmente utilizando botão **"Faturar"**, mantém o pedido como Pendente: Sim

Possibilitando novos faturamentos e geração de novas notas sem a mudança do situação do pedido.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16912103397783) SOLUÇÃO:**

![Imagem 3: Acesse a tela "DBExplorer" (Caminho de acesso: Configurações » Avançado » DBExplorer Opção Triggers)](https://ajuda.sankhya.com.br/hc/article_attachments/16912103400343) Acesse a tela  **"DBExplorer"** (Caminho de acesso: Configurações » Avançado » DBExplorer Opção Triggers)

![Imagem 4: Acesse a tela "DBExplorer" (Caminho de acesso: Configurações » Avançado » DBExplorer Opção Triggers)](https://ajuda.sankhya.com.br/hc/article_attachments/15137074396183)

![Imagem 5: Verifique se Trigger TRG_INC_UPD_TGFVAR existe no sistema;](https://ajuda.sankhya.com.br/hc/article_attachments/16912103402647) Verifique se Trigger TRG\_INC\_UPD\_TGFVAR existe no sistema;

![Imagem 6: Verifique se Trigger TRG_INC_UPD_TGFVAR existe no sistema;](https://ajuda.sankhya.com.br/hc/article_attachments/13976790559895)

![Imagem 7: Na inexistência da trigger, atualize o release, observe se trigger será incluída automaticamente no sistema.](https://ajuda.sankhya.com.br/hc/article_attachments/16912115796631) Na inexistência da trigger, atualize o release, observe se trigger será incluída automaticamente no sistema.

![Imagem 8: Se a inclusão não for bem sucedida, entre em contato com o suporte para análise.](https://ajuda.sankhya.com.br/hc/article_attachments/16912138620183) Se a inclusão não for bem sucedida, entre em contato com o suporte para análise.
