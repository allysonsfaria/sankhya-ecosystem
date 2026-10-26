---
id: "360043180034"
titulo: "Valor da substituição não pode ficar negativo. Produto X"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043180034-Valor-da-substitui%C3%A7%C3%A3o-n%C3%A3o-pode-ficar-negativo-Produto-X"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:02:28Z"
rotulos: ["#PUBLIFER", "CORE_E04483", "Configuração", "NF-e", "ICMS", "Impostos", "Substituição Tributária", "CORE_E04497", "Valor ST negativo não permitido", "ST calculada abaixo de zero", "Marcar \"Zerar valor ST negativo\" e refazer faturamento", "Erro"]
---

# Valor da substituição não pode ficar negativo. Produto X

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16162604723863)MENSAGEM:**

[CORE\_E04483] Valor da substituição não pode ficar negativo. Produto X.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16162604727447) SITUAÇÃO:**

Ao tentar confirmar uma Nota fiscal, ocorre a mensagem.

**![Imagem 3: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/16162604737815) CAUSA**:

Ocorre ao realizar emissão de NF-e e a regra de ICMS calculada irá gerar um valor de ST menor que zero, se a opção Zerar valor da substituição tributária quando negativo estiver desmarcada, será apresentada a mensagem.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16162625439383) SOLUÇÃO:**

![Imagem 5: Primeiro: busque na tela " Alíquotas de ICMS " (Caminho de acesso: Comercial » Arquivo » Cadastros » Alíquotas) a regra…](https://ajuda.sankhya.com.br/hc/article_attachments/16162625439895) Primeiro: busque na tela **"[Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS)"** (Caminho de acesso: Comercial » Arquivo » Cadastros » Alíquotas) a regra que irá incidir sobre a nota fiscal eletrônica gerada e revise os valores configurados na aba **"Substituição Tributária"**.

![Imagem 6: Caso os valores estejam corretos e de fato é provável o cálculo de um valor ST negativo, realize a marcação "Zerar…](https://ajuda.sankhya.com.br/hc/article_attachments/16162604731927) Caso os valores estejam corretos e de fato é provável o cálculo de um valor ST negativo, realize a marcação **"Zerar valor da substituição tributária quando negativo"**, aba 'Substituição Tributária, tela 'Alíquotas de ICMS'.

**(2)** Zerar valor da substituição tributária quando negativo: Se esta opção estiver marcada e o cálculo de ST resultar em menor que zero, o sistema deixará o cálculo zerado.

**(2)** Caso a opção esteja desmarcada e o cálculo de ST venha a ser menor que zero, o sistema emitirá a mensagem: "Valor da substituição não pode ficar negativo. Produto: xxxx".

![Imagem 7: Realizada a marcação, refaça o faturamento.](https://ajuda.sankhya.com.br/hc/article_attachments/16162625446679) Realizada a marcação, refaça o faturamento.
