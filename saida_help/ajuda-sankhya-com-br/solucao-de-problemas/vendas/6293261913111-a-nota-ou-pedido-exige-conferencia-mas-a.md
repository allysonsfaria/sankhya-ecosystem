---
id: "6293261913111"
titulo: "A nota ou pedido exige conferência, mas ainda não foi liberada para conferência"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/6293261913111-A-nota-ou-pedido-exige-confer%C3%AAncia-mas-ainda-n%C3%A3o-foi-liberada-para-confer%C3%AAncia"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-09-17T13:05:51Z"
rotulos: ["Conferência", "Configuração", "TOP", "Estoque", "#publifercausaraiz", "CORE_E01878", "CORE_E01880", "Verificar configurações", "Falta de conferência", "Nota exige conferência", "Erro"]
---

# A nota ou pedido exige conferência, mas ainda não foi liberada para conferência

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16446994786711) MENSAGEM:**

[CORE\_E01878]  A nota ou pedido XXXX exige conferência, mas ainda não houve conferência.

[CORE\_E01880] A nota ou pedido XXXX exige conferência, mas ainda não houve conferência.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16446979062167)CAUSA:**

Quando vinculado ao lançamento configurações que exigem conferência e essa não for executada, a mensagem será apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16446979067671) SOLUÇÃO:**

Entenda a exigência de conferência solicitada para o seu lançamento, conforme abaixo:

![Imagem 4: Acesse a Tela "Tipos de Operação-TOP" e selecione a TOP utilizada:](https://ajuda.sankhya.com.br/hc/article_attachments/16446994803351) Acesse a Tela **"Tipos de Operação-TOP"** e selecione a TOP utilizada:

**(1)** Aba: **"Estoque";**

**(1)** Verifique a informação que consta no Campo **"Configuração p/Conferência";**

![Imagem 5: (1) Verifique a informação que consta no Campo "Configuração p/Conferência";](https://ajuda.sankhya.com.br/hc/article_attachments/14367289512599)

![Imagem 6: Na tela "Configuração de Conferência" , certifique-se do momento em que a conferência estará sendo executada:](https://ajuda.sankhya.com.br/hc/article_attachments/16446994809623) Na tela **"Configuração de Conferência"**, certifique-se do momento em que a conferência estará sendo executada:

**(1)** Busque pelo modelo vinculado na TOP
**(1)** Verifique o campo **"Momento da conferência":**

- **Antes de faturar:** será exigida a conferência dos itens somente ao **"Faturar"** o Pedido, ou seja, o Pedido só poderá ser faturado se a conferência dos itens estiver finalizada.
- **Antes da confirmação:** se configurada será exigida a conferência dos itens ao **"Confirmar"** o pedido/nota. Isto é, a confirmação da nota ou pedido somente poderá ser feita se a conferência estiver finalizada.

![Imagem 7: Antes da confirmação: se configurada será exigida a conferência dos itens ao "Confirmar" o pedido/nota. Isto é, a…](https://ajuda.sankhya.com.br/hc/article_attachments/14367329539863)

**OBSERVAÇÃO:** Não existe, nativamente, uma opção de ''Momento da conferência" para depois do faturamento, apenas os dois cenários acima (antes de faturar ou antes da confirmação).

![Imagem 8: Caso as configuração acima não estejam adequadas ao processo, ajuste as mesmas para seguir com o faturamento sem essa…](https://ajuda.sankhya.com.br/hc/article_attachments/16446994814743) Caso as configuração acima não estejam adequadas ao processo, ajuste as mesmas para seguir com o faturamento sem essa exigência. Caso a exigência seja pertinente, finalize o processo de conferência.
