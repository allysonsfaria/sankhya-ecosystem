---
id: "360057916054"
titulo: "A instrução INSERT conflitou com a restrição do FOREIGN KEY \"FK_TGFFIN_TSICTA\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360057916054-A-instru%C3%A7%C3%A3o-INSERT-conflitou-com-a-restri%C3%A7%C3%A3o-do-FOREIGN-KEY-FK-TGFFIN-TSICTA"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T15:26:44Z"
rotulos: ["Central de Vendas", "Movimentação Financeira", "Conta Bancária", "Financeiro", "Conflito ao inserir registro", "Verificar e preencher 'Conta Bancária'", "Conta bancária não preenchida", "Erro"]
---

# A instrução INSERT conflitou com a restrição do FOREIGN KEY "FK_TGFFIN_TSICTA"

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16253375684887) MENSAGEM:**

A instrução INSERT conflitou com a restrição do FOREIGN KEY "FK\_TGFFIN\_TSICTA". O conflito ocorreu no bando de dados "SANKHYA\_PRODUCAO", tabela "sankhya.TSICTA", column 'CODCTABCOINT'.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16253375689367) SOLUÇÃO:**

![Imagem 3: Ao realizar qualquer lançamento/movimentação/renegociação financeira, verifique se foi devidamente informado uma 'Conta…](https://ajuda.sankhya.com.br/hc/article_attachments/16253375693335) Ao realizar qualquer lançamento/movimentação/renegociação financeira, verifique se foi devidamente informado uma **'Conta Bancária'** cadastrada e ativa no sistema.

![Imagem 4: Se o financeiro foi gerado a partir de um lançamento de notas (Central de Vendas), é possível identificar através da…](https://ajuda.sankhya.com.br/hc/article_attachments/16253389610135) Se o financeiro foi gerado a partir de um lançamento de notas (Central de Vendas), é possível identificar através da **aba 'Financeiro'** dessa nota, se o campo **"Conta Bancária"** foi devidamente preenchido.

- Caso esteja em branco, acesse o artigo [Quais as regras do sistema para preenchimento da informação 'Conta Bancária' da aba 'Financeiro' das centrais;](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043649134)
- Através dele, será possível compreender quais cadastros do sistema são verificados para que essa informação seja devidamente preenchida.
- Ajustado o cadastro, através do botão "Outras Opções" dentro da Central de Notas, escolha a opção **"Refazer financeiro"**.
- Feito isso, valide se o campo 'Conta Bancária' foi devidamente preenchido e siga com a movimentação desejada.

![Imagem 5: Caso tenha sido um lançamento gerado diretamente nas rotinas financeiras (Movimentação Financeira, Renegociação de…](https://ajuda.sankhya.com.br/hc/article_attachments/16253389615383) Caso tenha sido um lançamento gerado diretamente nas rotinas financeiras (Movimentação Financeira, Renegociação de Títulos), preencha corretamente a 'Conta Bancária' do respectivo título
