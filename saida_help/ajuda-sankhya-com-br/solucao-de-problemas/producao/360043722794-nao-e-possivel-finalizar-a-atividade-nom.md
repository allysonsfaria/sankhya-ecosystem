---
id: "360043722794"
titulo: "Não é possível finalizar a atividade (nome da atividade) pois existem execuções dessa atividade em aberto"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043722794-N%C3%A3o-%C3%A9-poss%C3%ADvel-finalizar-a-atividade-nome-da-atividade-pois-existem-execu%C3%A7%C3%B5es-dessa-atividade-em-aberto"
trilha: "Solução de Problemas > Produção"
atualizado_em: "2026-07-22T16:00:14Z"
rotulos: ["PROD_E00278", "Ordem de Produção", "Produção", "Apontamento de Produção", "Preencha \"Dh Final\" em Apontamento de Produção", "Atividade não pode ser finalizada", "Execução em aberto ou usuário diferente finalizando", "Erro", "Atividade"]
---

# Não é possível finalizar a atividade (nome da atividade) pois existem execuções dessa atividade em aberto

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/17292895738263) MENSAGEM:**

[PROD\_E00278] Não é possível finalizar a atividade (nome da atividade) pois existem execuções dessa atividade em aberto.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17292925010455) SITUAÇÃO:**

Ao tentar finalizar alguma atividade no processo de Produção retorna a mensagem de aviso

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17292895769751) SOLUÇÃO:**

![Imagem 4: Acesse: Produção » Rotinas » Apontamento de Produção / Aba: "Execução"](https://ajuda.sankhya.com.br/hc/article_attachments/17292895784983) Acesse: Produção » Rotinas » Apontamento de Produção / Aba: **"Execução"**

Com o usuário que iniciou o Apontamento, acesse a rotina e preencha o campo **"Dh Final"**. A produção pode ser encerrada pela rotina Apontamento de Produção.

![Imagem 5: Acesse: Produção » Rotinas » Ordens de Produção - Nova / Aba: "Atividades"](https://ajuda.sankhya.com.br/hc/article_attachments/30892195641367) Acesse: Produção » Rotinas » Ordens de Produção - Nova / Aba: **"Atividades"**

Nos três pontos do Card da atividade, selecione **"Execuções"**, duplo clique no campo **"Dh. Final"** e preencha a informação. A produção pode ser encerrada pela rotina de Operações de Produção.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17292895791767) CAUSA:**

Ocorre quando foi iniciado apontamento pela tela de Apontamento de Produção por algum executante e este confirmou o apontamento, porém não preencheu o campo Dh. Final da aba Execuções.
Ocorre também quando o usuário que iniciou a atividade pela tela de Operações de Produção não é o mesmo que está finalizando a atividade.
