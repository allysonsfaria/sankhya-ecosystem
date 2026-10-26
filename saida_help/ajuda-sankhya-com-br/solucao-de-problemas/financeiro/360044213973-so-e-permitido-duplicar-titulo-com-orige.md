---
id: "360044213973"
titulo: "Só é permitido duplicar título com origem no financeiro "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044213973-S%C3%B3-%C3%A9-permitido-duplicar-t%C3%ADtulo-com-origem-no-financeiro"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T16:00:46Z"
rotulos: ["#PUBLIFER", "#Revisadoclaudio", "Configuração", "Movimentação Financeira", "Estoque", "Financeiro", "Duplicação bloqueada: Origem não financeira", "Causa: Título com origem 'Estoque'", "Verificar parcelamento: Ajustar tipo na renegociação", "Erro"]
---

# Só é permitido duplicar título com origem no financeiro 

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16199886364823) MENSAGEM:**

Só é permitido duplicar título com origem no financeiro.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16199915206551) SITUAÇÃO:**

Ao tentar efetuar a renegociação de títulos, ocorre a mensagem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16199915207703) SOLUÇÃO:**

A princípio essa validação ocorrerá no cenário abaixo:

![Imagem 4: Verifique pela tela " Renegociação de Títulos " , clicando no botão "Parcelar" , se a seção "Tipo de parcelamento" está…](https://ajuda.sankhya.com.br/hc/article_attachments/16199915208727) Verifique pela tela **"[Renegociação de Títulos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115393)"**, clicando no botão **"Parcelar"**, se a seção **"Tipo de parcelamento"** está definida como **"Duplicação sem juros e sem multas"**. Se for este o caso, não será possível envolver títulos com origem diferente de financeiro. 

![Imagem 5: Caso tenha dúvidas sobre qual opção utilizar, analise o Help da tela ( Renegociação de Títulos ) e escolha a opção mais…](https://ajuda.sankhya.com.br/hc/article_attachments/16199915211543) Caso tenha dúvidas sobre qual opção utilizar, analise o Help da tela [Renegociação de Títulos]  e escolha a opção mais adequada, que seja diferente da opção abaixo:

![Imagem 6: Caso tenha dúvidas sobre qual opção utilizar, analise o Help da tela ( Renegociação de Títulos ) e escolha a opção mais…](https://ajuda.sankhya.com.br/hc/article_attachments/14613465313943)

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16199915213463) CAUSA:**

Ocorre quando a opção Duplicação sem juros e sem multas (fixas) estiver marcada e dentre os títulos parcelados existir pelo menos um título de 'Origem Estoque'.
