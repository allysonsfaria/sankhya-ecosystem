---
id: "10624259857815"
titulo: "Colaborador(a) não tem pensionista e ao gerar cálculo de folha normal está gerando base 1997 - BASE PENSÃO SL, saiba como proceder"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10624259857815-Colaborador-a-n%C3%A3o-tem-pensionista-e-ao-gerar-c%C3%A1lculo-de-folha-normal-est%C3%A1-gerando-base-1997-BASE-PENS%C3%83O-SL-saiba-como-proceder"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:16:27Z"
rotulos: ["Configuração", "Eventos", "Funcionários", "Folha", "#folha", "Base de Cálculo", "Base 1997 informativa", "Não imprime/visualiza", "Desmarcar regra cálculo"]
---

# Colaborador(a) não tem pensionista e ao gerar cálculo de folha normal está gerando base 1997 - BASE PENSÃO SL, saiba como proceder

![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18849052546583) **SOLUÇÃO:**

A base 1997 - \*\*\*BASE PENSAO SL\*\*\* está sendo apresentada na base de cálculo da folha do colaborador somente como informativa. Isso acontece mesmo não tendo o evento de pensão calculado.
Essa situação ocorre em função da configuração da base 1997 estar marcada como regra em cálculo de Folha Normal e tem os eventos 1 e 901 vinculados nela. Essa base está apenas sendo demonstrada na Folha, mas não influencia no cálculo nem no Resumo da Folha.

Caso entenda que a base não deve ser demonstrada no cálculo, siga os seguintes passos:

**No MGE Pessoal,** acesse o menu Arquivos>> Bases de Cálculo, selecione a base 1997 e desmarque o campo 'Normal' da **Base como regra de cálculo de:**O campo **Imprime** pode marcar **"Não Imprime".**Pode marcar o box **"Não Visualizar na tela do cálculo.**

![Imagem 2: No MGE Pessoal, acesse o menu Arquivos>> Bases de Cálculo, selecione a base 1997 e desmarque o campo 'Normal' da Base…](https://ajuda.sankhya.com.br/hc/article_attachments/18849033246743)

**Já no Pessoal+,** acesse o Pessoal+ » Cadastros » Eventos, pesquise pelo 1997 e desmarque o campo 'Normal' da **Base como regra de cálculo;**

**E deixe o box do "Imprime em Documentos" desmarcado.**

![Imagem 3: E deixe o box do "Imprime em Documentos" desmarcado.](https://ajuda.sankhya.com.br/hc/article_attachments/18849052552599)

**Importante:**

Vale ressaltar que ambos sistema, se em algum momento houver pensionista em folha e estes campos citados acima estiverem desmarcados, a base não será informada.
