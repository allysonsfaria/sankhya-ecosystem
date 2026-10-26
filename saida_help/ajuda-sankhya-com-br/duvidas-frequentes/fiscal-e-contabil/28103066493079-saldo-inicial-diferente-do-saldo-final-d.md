---
id: "28103066493079"
titulo: "Saldo inicial diferente do saldo final do período anterior - ECD"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/28103066493079-Saldo-inicial-diferente-do-saldo-final-do-per%C3%ADodo-anterior-ECD"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:38:20Z"
rotulos: ["Relatórios", "ECD", "Contabilização", "Financeiro", "Saldo inicial diferente do saldo final do período anterior - ECD", "Erro"]
---

# Saldo inicial diferente do saldo final do período anterior - ECD

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/28103104603415) SITUAÇÃO:**

Ao realizar a validação do txt, gerado pela tela **"Geração de Arquivo - ECD"**, no PVA, é apresentada a mensagem de erro no relatório de erros.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/28103066491031) SOLUÇÃO:**

Analise na conta contábil/centro de custo, pelo balancete de verificação, se o saldo final do período anterior ao período que está sendo criticado no PVA bate com o saldo inicial do próximo mês.  Se de fato houver divergências entre os saldos finais de um período, com os iniciais do próximo, realize a **[recomposição de saldos.](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404109742743-Veja-como-fazer-a-recomposi%C3%A7%C3%A3o-de-saldos)**

Vale ressaltar que a recomposição de saldos deve ser realizada partindo sempre do período anterior ao período que foi criticado. Pois, o saldo inicial de um mês só é reconstruído pelo mês anterior ao seu. Então, se o problema foi no mês de janeiro, inicie a recomposição em dezembro do ano anterior; ou se o problema foi em junho, comece a recomposição em maio, e assim sucessivamente.

Caso a recomposição não tenha o efeito esperado, deve-se entender como o sistema chegou no saldo final em questão e como ele chegou no inicial também, analisando os **[Lançamentos Contábeis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116173-Lan%C3%A7amentos-Cont%C3%A1beis)** que compõe tais saldos. Pois, pode ser que alguns lançamentos foram realizados indevidamente, ou de maneira equivocada, causando o problema.
