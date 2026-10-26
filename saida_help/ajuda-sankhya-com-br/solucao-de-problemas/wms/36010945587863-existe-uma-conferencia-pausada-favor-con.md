---
id: "36010945587863"
titulo: "Existe uma conferência pausada. Favor conclui-la antes de prosseguir."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36010945587863-Existe-uma-confer%C3%AAncia-pausada-Favor-conclui-la-antes-de-prosseguir"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T14:24:09Z"
rotulos: ["Conferência", "Configuração", "WMS", "Preferências", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Erro", "Conferência pausada", "Squad WMS"]
---

# Existe uma conferência pausada. Favor conclui-la antes de prosseguir.

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/36010945579543) **MENSAGEM:**

Existe uma conferência pausada. Favor conclui-la antes de prosseguir.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/36010945580951)SOLUÇÃO:**

**(1)** Acesse a tela [**''Preferências''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias) (Configurações » Avançado » Preferências).

**(2)** Ative o parâmetro **'PERMCONTCONFPED'**, que oferece maior flexibilidade no processo de conferência.

Ao habilitar esse parâmetro, torna-se possível iniciar e finalizar a conferência em momentos distintos, permitindo, por exemplo que o processo seja iniciado pela manhã e concluído no período da tarde ou em outro momento.

![Imagem 3: Ao habilitar esse parâmetro, torna-se possível iniciar e finalizar a conferência em momentos distintos, permitindo, por…](https://ajuda.sankhya.com.br/hc/article_attachments/36623548001559)

**OBSERVAÇÃO:**
Quando a conferência por pedido é retomada posteriormente, **somente o mesmo usuário que a iniciou poderá concluí-la**. Outro usuário não conseguirá continuar o processo.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/36010897063319)CAUSA:**

##### A mensagem ocorre no coletor TotalCross/Superwaba durante as tarefas de conferência quando o parâmetro `PERMCONTCONFPED` está desativado. Nessa condição, o sistema não permite que o mesmo usuário inicie uma nova conferência antes de finalizar a anterior. Isso normalmente acontece quando o usuário inicia a conferência, sai do coletor sem concluir o processo, e depois tenta iniciar outra conferência — o que é bloqueado pelo sistema até que a conferência anterior seja finalizada.
