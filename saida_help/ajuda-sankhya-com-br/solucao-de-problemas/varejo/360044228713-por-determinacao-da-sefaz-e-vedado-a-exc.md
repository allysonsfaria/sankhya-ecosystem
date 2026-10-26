---
id: "360044228713"
titulo: "Por determinação da SEFAZ é vedado a exclusão da nota 'X', pois ela é uma Pré-Venda"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044228713-Por-determina%C3%A7%C3%A3o-da-SEFAZ-%C3%A9-vedado-a-exclus%C3%A3o-da-nota-X-pois-ela-%C3%A9-uma-Pr%C3%A9-Venda"
trilha: "Solução de Problemas > Varejo"
atualizado_em: "2026-07-22T15:59:49Z"
rotulos: ["#PUBLIFER", "#revisadojunior", "CORE_E00893", "Configuração", "NF-e", "SEFAZ", "TOP", "Solução: marcar como não pendente", "Exclusão de pré-venda vedada", "SEFAZ impede exclusão", "Erro"]
---

# Por determinação da SEFAZ é vedado a exclusão da nota 'X', pois ela é uma Pré-Venda

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16198384554263) MENSAGEM:**

[CORE\_E00893] Por determinação da SEFAZ é vedado a exclusão da nota 'X', pois ela é uma Pré-Venda.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16198371719831) SOLUÇÃO:**

Caso o documento tenha sido lançado com o Tipo de Operação - TOP vinculado como 'TOP de Pré-Venda', a validação acontecerá:

- Avançado » Preferências,  aba **Parâmetros de Telas,** campo "**Código da TOP para Pré-Venda"**:

![Imagem 3: Avançado » Preferências , aba Parâmetros de Telas, campo " Código da TOP para Pré-Venda" :](https://ajuda.sankhya.com.br/hc/article_attachments/14532970879511)

Esse documento, por determinações da SEFAZ, não poderá ser excluído. Caso a venda tenha sido cancelada e/ou lançada de forma equivocada, a prática recomendada é marcá-lo como não pendente:

- SankhyaW : Selecione o pedido na tela **"[Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654)"**, botão **"Outras Opções"** : Marcar como não pendente.

![Imagem 4: SankhyaW : Selecione o pedido na tela " Portal de Vendas " , botão "Outras Opções" : Marcar como não pendente.](https://ajuda.sankhya.com.br/hc/article_attachments/14532942621463)

- Mitra : Selecionar o pedido na CAC, botão direito e marcar a opção "**Marcar como não pendente".**

![Imagem 5: Mitra : Selecionar o pedido na CAC, botão direito e marcar a opção " Marcar como não pendente".](https://ajuda.sankhya.com.br/hc/article_attachments/14532975415575)

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16198384567575) CAUSA:**

Mensagem apresentada na tentativa de exclusão de documento "pré-venda" lançado no sistema, visto que a exclusão desse tipo de documento é vedada pela SEFAZ.
