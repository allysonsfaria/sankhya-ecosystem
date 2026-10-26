---
id: "9853206300311"
titulo: "Valor do campo nro. único [XXXX] maior que o número permitido: 999999"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9853206300311-Valor-do-campo-nro-%C3%BAnico-XXXX-maior-que-o-n%C3%BAmero-permitido-999999"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T15:05:42Z"
rotulos: ["Configuração", "Contas", "Boleto", "Financeiro", "CORE_E01416", "Valor nro. único > 999999", "Convênio > 6 dígitos carteira inválida", "Ajustar \"Carteira\" e \"Convênio\" conforme regras", "Erro"]
---

# Valor do campo nro. único [XXXX] maior que o número permitido: 999999

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16779161972759) MENSAGEM:**

[CORE\_E01416]: Valor do campo nro. único [XXXX] maior que o número permitido: 999999.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16779181261847) SITUAÇÃO:**

Ao tentar emitir um boleto a mensagem é apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16779161979927)SOLUÇÃO:**

![Imagem 4: Para solução dessa mensagem, revise (com apoio do gerente e/ou manual do banco) os seguintes campos :](https://ajuda.sankhya.com.br/hc/article_attachments/16779161982359) Para solução dessa mensagem, revise (com apoio do gerente e/ou manual do banco) os seguintes campos :

Tela **"Contas"** (Caminho de acesso à tela: Configurações » Cadastros » Bancários » Contas)

- Campo : "**Carteira"**
- Campo : "**Convênio"**

Considerando as seguintes regras :

Se o Convênio for maior que 999999 (seis dígitos) o campo Carteira deve ser: 12, 17, 18, 19.

![Imagem 5: Se o Convênio for maior que 999999 (seis dígitos) o campo Carteira deve ser: 12, 17, 18, 19.](https://ajuda.sankhya.com.br/hc/article_attachments/16779181270167)

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16779181273367)CAUSA:**

Quando o campo convênio possui mais de seis dígitos e o campo carteira é diferente de 12, 17, 18, 19..
