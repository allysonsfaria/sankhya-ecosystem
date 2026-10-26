---
id: "43937293192087"
titulo: "É necessário utilizar a opção de Processar Recebimento para liberação da doca, quando o parâmetro de liberação automática de doca está ligado em fluxo de Registro de Conferência."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43937293192087-%C3%89-necess%C3%A1rio-utilizar-a-op%C3%A7%C3%A3o-de-Processar-Recebimento-para-libera%C3%A7%C3%A3o-da-doca-quando-o-par%C3%A2metro-de-libera%C3%A7%C3%A3o-autom%C3%A1tica-de-doca-est%C3%A1-ligado-em-fluxo-de-Registro-de-Confer%C3%AAncia"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-10-02T12:50:05Z"
rotulos: ["Recebimento de Mercadorias", "registro de conferência", "WMS - KCS", "Processar Recebimento", "liberação da doca", "liberação automática de doca"]
---

# É necessário utilizar a opção de Processar Recebimento para liberação da doca, quando o parâmetro de liberação automática de doca está ligado em fluxo de Registro de Conferência.

**MENSAGEM**

É necessário utilizar a opção de Processar Recebimento para liberação da doca, quando o parâmetro de liberação automática de doca está ligado em fluxo de Registro de Conferência.

**SITUAÇÃO**

Quando a conferência de entrada é realizada pela tarefa **Registro de Conferência**.

**SOLUÇÃO**

**(1)** Acesse a tela **''Recebimento de Mercadorias''** (WMS » Rotinas » Recebimento de Mercadorias).

**(2)** No botão  **''Outras opções''**, selecione **''Processar recebimento''** para liberar a doca.

**CAUSA**

O sistema bloqueia intencionalmente a liberação manual da doca nesse cenário, pois o fluxo de **Registro de Conferência em uso** exige que a doca de entrada seja liberada pela opção **Processar Recebimento**.
