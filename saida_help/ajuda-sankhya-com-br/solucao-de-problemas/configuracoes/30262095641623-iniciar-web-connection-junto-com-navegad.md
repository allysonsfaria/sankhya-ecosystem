---
id: "30262095641623"
titulo: "Iniciar Web Connection junto com navegador se desmarcando"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30262095641623-Iniciar-Web-Connection-junto-com-navegador-se-desmarcando"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:36:22Z"
rotulos: ["Configuração", "Preferências", "Web Connection", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Desmarcando", "Desmarca", "Desconecta", "Erro", "Navegador Sankhya"]
---

# Iniciar Web Connection junto com navegador se desmarcando

![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30262111744023) **SITUAÇÃO:**

Navegador Sankhya desmarca sozinho a opção **'Iniciar Web Connection junto com navegador'**.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30262111747735)SOLUÇÃO:**

![Imagem 3: Feche o Navegador Sankhya completamente.](https://ajuda.sankhya.com.br/hc/article_attachments/30275546946199) **Feche** o **Navegador Sankhya** completamente.

![52a3f95f-f5a6-4c32-a7dd-1bd3735f408b](https://ajuda.sankhya.com.br/hc/article_attachments/30277518139799) Acesse o **Explorador de Arquivos** do computador e navegue até o seguinte caminho:

`C:\Users\NOME_DO_USUARIO_LOGADO\AppData\Roaming\Navegador\Sankhya\db\`

**![Imagem 5: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30275546946839)OBSERVAÇÃO:**

Se a pasta **AppData** não estiver visível, ative a exibição de itens ocultos:

- No **Explorador de Arquivos**, clique em **Exibir** (ou **Visualizar**).
- Em seguida, selecione **Mostrar > Itens Ocultos**.

![Imagem 6: Em seguida, selecione Mostrar > Itens Ocultos .](https://ajuda.sankhya.com.br/hc/article_attachments/30262111755287)

![Imagem 7: Dentro da pasta "db" , exclua o arquivo chamado "config.db" .](https://ajuda.sankhya.com.br/hc/article_attachments/30275554656151) Dentro da pasta **"db"**, **exclua** o arquivo chamado **"config.db"**.

- Esse arquivo armazena as configurações do **Navegador Sankhya** e, ao removê-lo, as configurações serão redefinidas.

![Imagem 8: Reabra o Navegador Sankhya .](https://ajuda.sankhya.com.br/hc/article_attachments/30275546951319)  **Reabra** o **Navegador Sankhya**.

![Imagem 9: Ative novamente a opção:](https://ajuda.sankhya.com.br/hc/article_attachments/30275554657175) **Ative novamente** a opção:

- Acesse as configurações e marque **"Iniciar Web Connection junto com navegador"**.

6 **Feche e abra** o navegador mais uma vez para validar a correção.

 Após seguir esses passos, a opção **"Iniciar Web Connection junto com navegador"** deverá permanecer ativada de forma permanente.
