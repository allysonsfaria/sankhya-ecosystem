---
id: "24901861538967"
titulo: "Erro na geração do financeiro para a nota. O sistema não está preparado para gerar financeiro para o tipo de negociação que possui o campo número de parcelas diferente de zero e tipo de movimento (TIPMOV) diferente de \"P ou V\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/24901861538967-Erro-na-gera%C3%A7%C3%A3o-do-financeiro-para-a-nota-O-sistema-n%C3%A3o-est%C3%A1-preparado-para-gerar-financeiro-para-o-tipo-de-negocia%C3%A7%C3%A3o-que-possui-o-campo-n%C3%BAmero-de-parcelas-diferente-de-zero-e-tipo-de-movimento-TIPMOV-diferente-de-P-ou-V"
trilha: "Dúvidas Frequentes > Financeiro"
atualizado_em: "2026-07-22T14:46:25Z"
rotulos: ["Configuração", "Movimentação Financeira", "Nota Fiscal", "TOP", "Financeiro"]
---

# Erro na geração do financeiro para a nota. O sistema não está preparado para gerar financeiro para o tipo de negociação que possui o campo número de parcelas diferente de zero e tipo de movimento (TIPMOV) diferente de "P ou V"

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/24901861528215) **MENSAGEM:**

Erro na geração do financeiro para a nota. O sistema não está preparado para gerar financeiro para o tipo de negociação que possui o campo número de parcelas diferente de zero e tipo de movimento (TIPMOV) diferente de "P ou V".

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/24901868288151)SOLUÇÃO:**

Quando o erro for apresentado ao tentar devolver uma nota é necessário utilizar uma TOP que não recalcule financeiro, cadastro da TOP, aba Financeiro, campo 'Tipo de Alteração da Data de Vencimento', deve estar com a opção: Manter.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/24901861534359)CAUSA:**

O erro é apresentado quando utiliza um Tipo de Negociação com o campo 'Número de Parcelas' preenchido com uma TOP com o tipo de movimento diferente de 'P' (Pedido de Venda) e 'V' (Nota de Venda).
