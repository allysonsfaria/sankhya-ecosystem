---
id: "9485454562583"
titulo: "O título xxx está em cobrança registrada e a Conta não pode ser alterada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9485454562583-O-t%C3%ADtulo-xxx-est%C3%A1-em-cobran%C3%A7a-registrada-e-a-Conta-n%C3%A3o-pode-ser-alterada"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T15:07:33Z"
rotulos: ["Configuração", "Contas", "Movimentação Financeira", "Preferências", "Financeiro", "não apagar", "Título em cobrança registrada impede alteração", "Renegocie para mudar a conta", "Desligue parâmetro SUBSCONTA para manter conta original"]
---

# O título xxx está em cobrança registrada e a Conta não pode ser alterada

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16747311682071) MENSAGEM:**

O título xxx está em cobrança registrada e a conta não pode ser alterada. Caso haja necessidade este título deve ser renegociado.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16747311683351) SITUAÇÃO:**

Ao tentar baixar um título no financeiro a mensagem é apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16747311684375) SOLUÇÃO:**

![Imagem 4: Títulos gerados em conta monitorada, para que possam ser baixados em outra conta da empresa, precisam passar por uma…](https://ajuda.sankhya.com.br/hc/article_attachments/16747311685655) Títulos gerados em conta monitorada, para que possam ser baixados em outra conta da empresa, precisam passar por uma renegociação de títulos. Com isso, o título antigo é baixado (e depois informado ao banco sobre sua baixa) e é gerado um novo, podendo então informar outra conta na baixa.

![Imagem 5: Títulos gerados em conta monitorada, para que possam ser baixados em outra conta da empresa, precisam passar por uma…](https://ajuda.sankhya.com.br/hc/article_attachments/16747311686807) Existe também um parâmetro que se chama **"SUBSCONTA-Substitui Conta do Financeiro com Conta Baixa"**. 
Quando esse parâmetro está ligado, ele altera a conta do título para a conta da baixa e como a conta é monitorada, ela não pode ser alterada.
Ao desligar esse parâmetro, ele mantém a conta de baixa igual a conta do lançamento na movimentação financeira. Para isso, acesse a tela **"Preferências"** (Caminho de acesso à tela: Configurações » Avançado » Preferências), informe a chave do parâmetro e desligue-o.

![Imagem 6: Títulos gerados em conta monitorada, para que possam ser baixados em outra conta da empresa, precisam passar por uma…](https://ajuda.sankhya.com.br/hc/article_attachments/16747298062615)

![Imagem 7: Títulos gerados em conta monitorada, para que possam ser baixados em outra conta da empresa, precisam passar por uma…](https://ajuda.sankhya.com.br/hc/article_attachments/16747311691671)

![Imagem 8: Títulos gerados em conta monitorada, para que possam ser baixados em outra conta da empresa, precisam passar por uma…](https://ajuda.sankhya.com.br/hc/article_attachments/16747311692311)

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16747298065687) CAUSA:**

Ocorre ao informar a conta de baixa diferente da conta do título e esta é monitorada.
