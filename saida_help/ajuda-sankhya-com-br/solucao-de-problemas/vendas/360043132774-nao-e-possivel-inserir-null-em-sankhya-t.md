---
id: "360043132774"
titulo: "Não é possível inserir NULL em (SANKHYA.TGFITE.CODCFO)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043132774-N%C3%A3o-%C3%A9-poss%C3%ADvel-inserir-NULL-em-SANKHYA-TGFITE-CODCFO"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:04:48Z"
rotulos: ["#PUBLIFER", "Configuração", "Fiscal", "TOP", "CFOP", "ORA-01400", "Erro ao inserir NULL em campo obrigatório", "CFOP do item está em branco ou zero", "Ajustar CFOP no Tipo de Operação e refazer o lançamento", "Erro"]
---

# Não é possível inserir NULL em (SANKHYA.TGFITE.CODCFO)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16145105993111) MENSAGEM:**

ORA-01400: não é possível inserir NULL em (SANKHYA.TGFITE.CODCFO)
ORA-06512: em "SANKHYA.TRG\_INC\_TGFITE\_AFTER", line 27
ORA-04088: erro durante a execução do gatilho 'SANKHYA.TRG\_INC\_TGFITE\_AFTER'

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16145122100119) SOLUÇÃO:**

![Imagem 3: Acesse a tela " Tipos de Operação " (Caminho de acesso: Comercial » Arquivo » Cadastros) e localize o tipo de operação…](https://ajuda.sankhya.com.br/hc/article_attachments/16145122101399) Acesse a tela **"[Tipos de Operação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)"** (Caminho de acesso: Comercial » Arquivo » Cadastros) e localize o tipo de operação utilizado no respectivo lançamento.

![Imagem 4: Na aba " Livro Fiscal" preencha de acordo com orientações contábil/fiscal os campos destacados abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/16145106001559) Na aba "**Livro Fiscal"** preencha de acordo com orientações contábil/fiscal os campos destacados abaixo:

![Imagem 5: Na aba " Livro Fiscal" preencha de acordo com orientações contábil/fiscal os campos destacados abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/14690180907415)

![Imagem 6: Realizado o ajuste acima, refaça o lançamento da nota.](https://ajuda.sankhya.com.br/hc/article_attachments/16145122103575) Realizado o ajuste acima, refaça o lançamento da nota.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16145122106519) CAUSA:**

Mensagem apresentada quando as informações de CFOP de determinado item constam em branco ou zero.
