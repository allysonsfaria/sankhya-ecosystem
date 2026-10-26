---
id: "360043576414"
titulo: "Já existe venda posterior a esta data de vigor"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043576414-J%C3%A1-existe-venda-posterior-a-esta-data-de-vigor"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T16:02:10Z"
rotulos: ["#PUBLIFER", "#RevisadoGilmar", "Configuração", "Atualização", "Atualização de Preço de Venda", "TOP", "ORA-20101", "ORA-06512", "ORA-04088", "Tipo de Operação (TOP)", "Data de Vigor", "Erro", "Preço de Venda"]
---

# Já existe venda posterior a esta data de vigor

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16106779437591) **MENSAGEM:**

ORA-20101: (0) Já existe venda posterior a esta data de vigor.
ORA-06512: em "SANKHYA.TRG\_INC\_TGFTAB\_AFTER", line 105
ORA-04088: erro durante a execução do gatilho 'SANKHYA.TRG\_INC\_TGFTAB\_AFTER'

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16106779440023) SITUAÇÃO:**

Essa mensagem será apresentada quando o Tipo de Operação - TOP utilizado possuir a marcação **"Precificação"** configurada para atualização do preço de venda e já existir uma venda posterior a data de vigor da atualização de preço que será gerada por esse lançamento.

![Imagem 3: Certifique-se que a TOP utilizada de fato deverá atualizar preço de venda, em caso negativo ajuste o campo mencionado e…](https://ajuda.sankhya.com.br/hc/article_attachments/16106779441175) Certifique-se que a TOP utilizada de fato deverá atualizar preço de venda, em caso negativo ajuste o campo mencionado e refaça o lançamento:

**(2)** Tela **"[Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)"** (Caminho de acesso: Comercial » Arquivo » Cadastros)

**(2)** Aba **"Geral"**, campo **"Precifica"**:

![Imagem 4: (2) Aba "Geral" , campo "Precifica" :](https://ajuda.sankhya.com.br/hc/article_attachments/14522007249943)

![Imagem 5: Caso a atualização de preço de venda seja necessária, a primeira etapa é compreender qual data está sendo considerada…](https://ajuda.sankhya.com.br/hc/article_attachments/16106807647127) Caso a atualização de preço de venda seja necessária, a primeira etapa é compreender qual data está sendo considerada em seu processo de precificação. Para tal acesse a tela **"[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias)"** e verifique como está configurado o parâmetro **"DTPDTVIGOR - Data de entrada para Data de Vigor da tab.de Preço"**:

![Imagem 6: Caso a atualização de preço de venda seja necessária, a primeira etapa é compreender qual data está sendo considerada…](https://ajuda.sankhya.com.br/hc/article_attachments/12298557953303)

![Imagem 7: No lançamento realizado verifique se a data apontada no parâmetro está correta, pois se a mensagem ocorreu, quer dizer…](https://ajuda.sankhya.com.br/hc/article_attachments/16106779449623) No lançamento realizado verifique se a data apontada no parâmetro está correta, pois se a mensagem ocorreu, quer dizer que foi informada uma data retroativa. Dessa forma, ajuste essa data para a data atual e confirme o lançamento. Esse ajuste de data será necessário pois não será permitida a atualização do preço de venda quando já existir venda posterior a essa data de vigor. Caso necessário manter no lançamento a data antiga, ajuste após a confirmação.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16106779451031) CAUSA:**

Essa mensagem será apresentada quando o Tipo de Operação - TOP utilizado possuir a marcação **"Precificação"** configurada para atualização do preço de venda e já existir uma venda posterior a data de vigor da atualização de preço que será gerada por esse lançamento.
