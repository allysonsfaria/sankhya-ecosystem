---
id: "19839261105943"
titulo: "Registro só pode ser manifestado como 'Operação confirmada' se a nota estiver confirmada no sistema, sendo possível visualizá-la na Central de notas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/19839261105943-Registro-s%C3%B3-pode-ser-manifestado-como-Opera%C3%A7%C3%A3o-confirmada-se-a-nota-estiver-confirmada-no-sistema-sendo-poss%C3%ADvel-visualiz%C3%A1-la-na-Central-de-notas"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:51:25Z"
rotulos: ["Configuração", "NF-e", "XML", "SEFAZ", "Preferências", "Operação Confirmada Restrita a Notas Confirmadas", "Erro"]
---

# Registro só pode ser manifestado como 'Operação confirmada' se a nota estiver confirmada no sistema, sendo possível visualizá-la na Central de notas

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19839267917975) **MENSAGEM:**

Registro só pode ser manifestado como 'Operação confirmada' se a nota estiver confirmada no sistema, sendo possível visualizá-la na Central de notas.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19839267926295)CAUSA:**

Ocorre quando a marcação no campo Validar confirmação da operação para notas não confirmadas na central?' esta ativada no Portal de Importação de XML > Botão MD-e > Preferências do MD-e.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19839276598167)SOLUÇÃO:**

Acesse o **Portal de Importação de XML** (Comercial » Rotinas » Portal de importação de XML)  Botão MD-e  Preferências do MD-e, no campo 'Validar confirmação da operação para notas não confirmadas na central?', se a marcação estiver realizada, desmarque-a.

**Observação:** Esta marcação é por usuário, portanto é necessário verificar usuário por usuário.

Se desmarcar a opção nas Preferências DF-e e a mensagem de erro persistir, verifique o parâmetro **VALCONFOPDFE  -'Validar Confirmação Op. DF-e em Nota Confirmada?'**, que, para não validar se a nota está confirmada, deve permanecer desligado. Para validar, deve permanecer ligado.
