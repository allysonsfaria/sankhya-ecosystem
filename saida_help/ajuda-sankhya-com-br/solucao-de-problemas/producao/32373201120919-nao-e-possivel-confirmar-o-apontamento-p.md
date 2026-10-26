---
id: "32373201120919"
titulo: "Não é possível confirmar o apontamento pois existem itens (Recursos CT) com quantidade apontada igual ou menor que zero"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32373201120919-N%C3%A3o-%C3%A9-poss%C3%ADvel-confirmar-o-apontamento-pois-existem-itens-Recursos-CT-com-quantidade-apontada-igual-ou-menor-que-zero"
trilha: "Solução de Problemas > Produção"
atualizado_em: "2026-07-22T14:31:41Z"
rotulos: ["Configuração", "Centro de Trabalho", "Apontamento", "Produção", "Passos para resolver", "Razão do erro", "Detalhe do erro", "PROD_E00058", "Não é possível confirmar o apontamento", "existem itens (Recursos CT)", "com quantidade apontada igual ou menor que zero", "Erro"]
---

# Não é possível confirmar o apontamento pois existem itens (Recursos CT) com quantidade apontada igual ou menor que zero

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/32373201114391) **MENSAGEM:**

[PROD\_E00058] Não é possível confirmar o apontamento pois existem itens (Recursos CT) com quantidade apontada igual ou menor que zero.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/32373216703383)SOLUÇÃO:**

Acesse a tela **"Operações de produção"** (Produção > Rotinas > Operações de Produção), selecione a operação em questão. Vá até a aba **"Apontamentos",**selecione o devido apontamento. Em seguida, selecione a sub aba **"Itens"**e, na sub aba **"Recursos CT"**, informe os recursos de Centro de Trabalho utilizados na OP.

![Imagem 3: Acesse a tela "Operações de produção" (Produção > Rotinas > Operações de Produção) , selecione a operação em questão.…](https://ajuda.sankhya.com.br/hc/article_attachments/32532791373591)

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/32373216705303)CAUSA:**

O erro acontece quando no processo produtivo está definido que aponta recursos do centro de trabalho, no entanto, os recursos do CT não foram informados e é feita a tentativa de confirmar um apontamento na tela Operações de produção.
