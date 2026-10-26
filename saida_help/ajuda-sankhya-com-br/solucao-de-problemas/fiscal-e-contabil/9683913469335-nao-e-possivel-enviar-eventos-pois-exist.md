---
id: "9683913469335"
titulo: "Não é possível Enviar Eventos, pois existem registros com status \"Aguardando Correção\" para a sequência atual. É necessário Gerar Eventos novamente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9683913469335-N%C3%A3o-%C3%A9-poss%C3%ADvel-Enviar-Eventos-pois-existem-registros-com-status-Aguardando-Corre%C3%A7%C3%A3o-para-a-sequ%C3%AAncia-atual-%C3%89-necess%C3%A1rio-Gerar-Eventos-novamente"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:06:28Z"
rotulos: ["Parceiro", "Receita Federal", "Impostos", "LIV_E00038", "Registros com status \"Aguardando Correção\" impedem envio de eventos.", "Ajuste notas com % de INSS incorreto e gere eventos novamente.", "Analise eventos enviados para identificar e corrigir erros específicos.", "Erro", "Documentos Eletrônicos", "Reinf"]
---

# Não é possível Enviar Eventos, pois existem registros com status "Aguardando Correção" para a sequência atual. É necessário Gerar Eventos novamente

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16777577228055) MENSAGEM:**

[LIV\_E00038]: Não é possível Enviar Eventos, pois existem registros com status "Aguardando Correção" para a sequência atual. É necessário Gerar Eventos novamente.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16777577232279) SITUAÇÃO:**

Ao tentar transmitir o REINF a mensagem é apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16777555055767) SOLUÇÃO:**

![Imagem 4: Verifique se para o mesmo parceiro e referência existem notas com % de INSS diferentes, fazendo com que o campo indCPRB…](https://ajuda.sankhya.com.br/hc/article_attachments/16777577235863) Verifique se para o mesmo parceiro e referência existem notas com % de INSS diferentes, fazendo com que o campo indCPRB fique diferente;

![Imagem 5: Assim que identificar a nota que está com % de INSS incorreto, realize os devidos ajustes e gere os eventos novamente;](https://ajuda.sankhya.com.br/hc/article_attachments/16777555059863) Assim que identificar a nota que está com % de INSS incorreto, realize os devidos ajustes e gere os eventos novamente;

![Imagem 6: Analise todos os eventos que tiveram seu envio para RFB e analise ponto a ponto, sobre cada erro especificamente, pois…](https://ajuda.sankhya.com.br/hc/article_attachments/16777577240343) Analise todos os eventos que tiveram seu envio para RFB e analise ponto a ponto, sobre cada erro especificamente, pois a causa é genérica, ou seja, pode partir de qualquer evento.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16777555068311)CAUSA:**

Ocorre quando algum evento apresentou erro na validação na receita federal.
