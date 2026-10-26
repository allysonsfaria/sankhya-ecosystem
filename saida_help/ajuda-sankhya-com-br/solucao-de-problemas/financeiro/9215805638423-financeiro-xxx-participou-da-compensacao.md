---
id: "9215805638423"
titulo: "Financeiro xxx participou da Compensação xxx após a compensação que está sendo desfeita, neste caso a compensação null deve ser desfeita primeiro pois ela foi uma compensação total, ou seja, o título foi baixado por ela"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9215805638423-Financeiro-xxx-participou-da-Compensa%C3%A7%C3%A3o-xxx-ap%C3%B3s-a-compensa%C3%A7%C3%A3o-que-est%C3%A1-sendo-desfeita-neste-caso-a-compensa%C3%A7%C3%A3o-null-deve-ser-desfeita-primeiro-pois-ela-foi-uma-compensa%C3%A7%C3%A3o-total-ou-seja-o-t%C3%ADtulo-foi-baixado-por-ela"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T15:09:24Z"
rotulos: ["Movimentação Financeira", "Compensação", "Financeiro", "FIN_E00298", "Desfaça compensação total primeiro título baixado", "Desfaça compensação total; estorne título. Verifique contabilização e comissão", "Tentativa de desfazer compensação com anterior existente", "Passos para resolver", "Razão do erro", "Erro", "Artigo atualizado KCS", "Financeiro - KCS"]
---

# Financeiro xxx participou da Compensação xxx após a compensação que está sendo desfeita, neste caso a compensação null deve ser desfeita primeiro pois ela foi uma compensação total, ou seja, o título foi baixado por ela

**Mensagem**

[FIN\_E00298]: Financeiro XXX participou da Compensação xxx após a compensação que está sendo desfeita, neste caso a compensação xxx deve ser desfeita primeiro pois ela foi uma compensação total, ou seja, o título foi baixado por ela.

**Situação**

Ao tentar desfazer uma compensação financeira na tela **"Compensação Financeira"** (Financeiro >> Rotinas >> Compensação Financeira), o sistema apresenta a mensagem informando que existe outra compensação posterior que precisa ser desfeita primeiro. Porém, ao tentar desfazer a compensação indicada, o sistema retorna uma mensagem similar apontando para a compensação anterior, criando um **"loop de dependência"** entre as compensações.

**Solução**

Para resolver o erro de dependência circular entre compensações, siga o procedimento abaixo:

**(1)** Acesse a tela **"Movimentação Financeira"** (Financeiro » Rotinas » Movimentação Financeira) e localize os títulos envolvidos nas compensações.

**(2)** Identifique no campo **"Nro Compensação/Acerto"** os números das compensações vinculadas a cada título financeiro.

![Imagem 1: (2) Identifique no campo "Nro Compensação/Acerto" os números das compensações vinculadas a cada título financeiro.](https://ajuda.sankhya.com.br/hc/article_attachments/39596507255191)

**(3)** Verifique a **"ordem cronológica"** das compensações realizadas, identificando qual foi executada primeiro e qual foi executada posteriormente.

**(4)** Acesse a tela **"Compensação Financeira"** (Financeiro >> Rotinas >> Compensação Financeira).

**(5)** No campo **"Acerto"**, clique na **"lupa"** e pesquise pela última compensação realizada (a mais recente cronologicamente).
 
![Imagem 2: (5) No campo "Acerto" , clique na "lupa" e pesquise pela última compensação realizada (a mais recente cronologicamente).](https://ajuda.sankhya.com.br/hc/article_attachments/39596528474135)

**(6)** Selecione a compensação e clique no **"Botão Desfazer"** para reverter a operação.

**(7)** Após desfazer a compensação mais recente, retorne à tela e localize a compensação anterior.

**(8)** Clique novamente no **"Botão Desfazer"** para reverter a compensação anterior.

**(9)** Verifique na tela **"Movimentação Financeira"** se os títulos retornaram aos seus valores e parcelas originais.

**Observações adicionais para casos específicos:**

Se o título já tiver sido contabilizado, será necessário avaliar o estorno junto à contabilidade.

**Causa**

O erro ocorre quando um mesmo título financeiro participa de múltiplas compensações em sequência. O sistema exige que as compensações sejam desfeitas respeitando a ordem cronológica inversa, ou seja, a última compensação realizada deve ser desfeita primeiro.

Quando existe uma compensação posterior vinculada à compensação que se tenta estornar, o sistema bloqueia a operação para preservar a integridade dos dados financeiros. Isso é especialmente importante quando a compensação posterior foi uma compensação total, que baixou completamente o título.

Além disso, o problema pode ser agravado quando as compensações são realizadas de forma inadequada, como compensar múltiplos títulos de despesa simultaneamente contra múltiplos títulos de receita. Esse procedimento pode gerar parcelas adicionais indevidas e causar divergências entre os valores de receita e despesa, resultando em erros contábeis e dificuldades no estorno das operações.
