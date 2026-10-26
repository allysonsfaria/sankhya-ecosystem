---
id: "360044213893"
titulo: "O título de número único XXXXXX possui ligação com remessa. Para continuar com a exclusão do título será necessário desvinculá-lo da remessa, pela tela Movimentação Financeira"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044213893-O-t%C3%ADtulo-de-n%C3%BAmero-%C3%BAnico-XXXXXX-possui-liga%C3%A7%C3%A3o-com-remessa-Para-continuar-com-a-exclus%C3%A3o-do-t%C3%ADtulo-ser%C3%A1-necess%C3%A1rio-desvincul%C3%A1-lo-da-remessa-pela-tela-Movimenta%C3%A7%C3%A3o-Financeira"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T16:00:51Z"
rotulos: ["#RevisadoBernardo", "CORE_E02441", "Configuração", "Movimentação Financeira", "Preferências", "Financeiro", "ORA-20101", "Título vinculado a remessa não pode ser excluído", "Desvincule título da remessa na tela Movimentação Financeira", "Certifique-se de que o parâmetro 'PERDESVFINREM' está ativado", "Erro"]
---

# O título de número único XXXXXX possui ligação com remessa. Para continuar com a exclusão do título será necessário desvinculá-lo da remessa, pela tela Movimentação Financeira

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/17292496797591) MENSAGEM:**

[CORE\_E02441] Erro ao remover entidade: ORA-20101: O titulo de número único XXXXXX possui ligação com remessa. Para continuar com a exclusão do título será necessário desvinculá-lo da remessa, pela tela Movimentação Financeira.
[ORA-06512]: em "SANKHYA.TRG\_DLT\_TGFFIN", line 300
[ORA-04088]: erro durante a execução do gatilho 'SANKHYA.TRG\_DLT\_TGFFIN'

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17292496811031) SOLUÇÃO:**

![Imagem 3: Acesse: Configurações » Avançado » Preferências](https://ajuda.sankhya.com.br/hc/article_attachments/17292496825367) Acesse: Configurações » Avançado » Preferências

Parâmetro **"PERDESVFINREM - Permite desvincular financeiro de remessa?":**ligado

![Imagem 4: Acesse: Financeiro » Rotinas » Movimentação Financeira](https://ajuda.sankhya.com.br/hc/article_attachments/17292496828311) Acesse: Financeiro » Rotinas » Movimentação Financeira

Selecione na tela **"Movimentação financeira"** os financeiros da respectiva nota.

Clique no botão: Outras Opções...>>Desvincular Remessa

![Imagem 5: Realizado os procedimentos acima, proceda com a exclusão/cancelamento desejado.](https://ajuda.sankhya.com.br/hc/article_attachments/17292508259735) Realizado os procedimentos acima, proceda com a exclusão/cancelamento desejado.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17292496859031) CAUSA:**

Ocorre quando um ou vários títulos participaram de um arquivo de remessa para o banco, afim de geração de boletos para pagamentos.
