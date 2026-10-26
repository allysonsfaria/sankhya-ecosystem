---
id: "9629930831383"
titulo: "ORA-20101: O nro único desta operação é inferior do último registrado no cad. Bens. Ultimo Nunota: XXXX"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9629930831383-ORA-20101-O-nro-%C3%BAnico-desta-opera%C3%A7%C3%A3o-%C3%A9-inferior-do-%C3%BAltimo-registrado-no-cad-Bens-Ultimo-Nunota-XXXX"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:07:07Z"
rotulos: ["Movimentação Financeira", "TOP", "Estoque", "ORA-20101", "Cadastro", "Problema de Número Único na Operação", "Erro"]
---

# ORA-20101: O nro único desta operação é inferior do último registrado no cad. Bens. Ultimo Nunota: XXXX

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16363639917591) MENSAGEM:**

[ORA-20101]: O nro único desta operação é inferior do último registrado no cad. Bens. Ultimo Nunota: XXXX.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16363650701207)CAUSA:**

O erro é apresentado pois o último nro. único com registro de movimentação do Bem (TCIIBE) não pode ser maior que o nro. único da Nota Atual, desde que a operação em questão não seja um desmembramento do bem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16363639920663)SOLUÇÃO:**

Identifique a nota com a última movimentação do Bem, a mesma está sendo citada na própria mensagem de erro.

Após a identificação, avalie qual a melhor tratativa para a mesma, pois esse é o último registro no qual consta a movimentação do bem.

Caso seja necessário a exclusão, só é recomendado se existir a possibilidade de cancelamento da nota; não sendo necessária a exclusão, pode ser revisto o lançamento de origem e realizado o devido ajuste.

Após validar a melhor tratativa e realizá-la será possível movimentar o bem assim como desejar, pois o bem terá seu último nro. nota vinculado ao lançamento.
