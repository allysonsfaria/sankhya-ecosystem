---
id: "360043652854"
titulo: "Adiantamento/Empréstimo não pode ser excluído por esta tela"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043652854-Adiantamento-Empr%C3%A9stimo-n%C3%A3o-pode-ser-exclu%C3%ADdo-por-esta-tela"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T16:00:59Z"
rotulos: ["#PUBLIFER", "CORE_E02382", "Movimentação Financeira", "Financeiro", "Adiantamento/Empréstimo", "Exclusão indisponível", "Acesso à tela correta", "Verificação necessária", "Detalhe do erro", "Erro"]
---

# Adiantamento/Empréstimo não pode ser excluído por esta tela

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16191245259159) MENSAGEM:**

[CORE\_E02382] Adiantamento/Empréstimo não pode ser excluído por esta tela!

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16191245260311) SOLUÇÃO:**

![Imagem 3: Na tela " Movimentação Financeira " localize o campo "Nro Compensação/Acerto" :](https://ajuda.sankhya.com.br/hc/article_attachments/16191247788823) Na tela **"[Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753)"** localize o campo **"Nro Compensação/Acerto"**:

![Imagem 4: Na tela " Movimentação Financeira " localize o campo "Nro Compensação/Acerto" :](https://ajuda.sankhya.com.br/hc/article_attachments/9978994098711)

![Imagem 5: Localizada a informação acima, acesse a tela " Adiantamento/Empréstimo ", clique no Campo "Buscar" , insira o código em…](https://ajuda.sankhya.com.br/hc/article_attachments/16191245263895) Localizada a informação acima, acesse a tela **"[Adiantamento/Empréstimo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598534)",** clique no Campo **"Buscar"**, insira o código em **"Adiant./Emp"** e clique em **"aplicar"**.

![Imagem 6: Localizada a informação acima, acesse a tela " Adiantamento/Empréstimo ", clique no Campo "Buscar" , insira o código em…](https://ajuda.sankhya.com.br/hc/article_attachments/9978948510231)

![Imagem 7: Localizada a informação acima, acesse a tela " Adiantamento/Empréstimo ", clique no Campo "Buscar" , insira o código em…](https://ajuda.sankhya.com.br/hc/article_attachments/9978971946775)

![Imagem 8: Localizado o adiantamento selecione a opção "Desfazer" ':](https://ajuda.sankhya.com.br/hc/article_attachments/16191245265431) Localizado o adiantamento selecione a opção **"Desfazer"**':

![Imagem 9: Localizado o adiantamento selecione a opção "Desfazer" ':](https://ajuda.sankhya.com.br/hc/article_attachments/14605807109271)

![Imagem 10: Executado o procedimento acima, retorne a tela Movimentação Financeira e valide se a exclusão do título ocorreu…](https://ajuda.sankhya.com.br/hc/article_attachments/16191247792535) Executado o procedimento acima, retorne a tela Movimentação Financeira e valide se a exclusão do título ocorreu conforme desejado.

Se caso por algum motivo esse adiantamento/empréstimo não for localizado na tela Adiantamento/Empréstimo**,** acesse o título na movimentação financeira, localize o campo **"Desdob. Duplicata"**:.

Se esse campo estiver preenchido com "**ZZ**", limpe o manualmente e, em seguida, será permitido excluir o lançamento.

![Imagem 11: Se esse campo estiver preenchido com " ZZ ", limpe o manualmente e, em seguida, será permitido excluir o lançamento.](https://ajuda.sankhya.com.br/hc/article_attachments/14605861534487)

**![Imagem 12: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16191247793175) CAUSA:**

Ocorre ao tentar excluir um lançamento diretamente na rotina Movimentação Financeira, sendo que esse possui um Nro Compensação/Acerto.
