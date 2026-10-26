---
id: "4555865028375"
titulo: "Um título de despesa de frete de origem estoque e que atualiza livro fiscal não pode ser baixado com valor inferior"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4555865028375-Um-t%C3%ADtulo-de-despesa-de-frete-de-origem-estoque-e-que-atualiza-livro-fiscal-n%C3%A3o-pode-ser-baixado-com-valor-inferior"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T15:18:56Z"
rotulos: ["Configuração", "Fiscal", "Movimentação Financeira", "Estoque", "Financeiro", "#causaraiz", "CORE_E01730", "Título de despesa de frete não pode ser baixado parcialmente.", "Use a renegociação para ajustar valor e ICMS corretamente", "Validação evita baixa parcial para manter integridade fiscal", "Erro"]
---

# Um título de despesa de frete de origem estoque e que atualiza livro fiscal não pode ser baixado com valor inferior

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16316688917015) MENSAGEM:**

[CORE\_E01730] Um título de despesa de frete de origem estoque e que atualiza livro fiscal não pode ser baixado com valor inferior.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16316691981079) CAUSA:**

O erro ocorre quando tenta-se realizar a baixa parcial de um título.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16316691983639) SOLUÇÃO:**

O processo de baixar parcialmente o título não é correto pois isso faz com que esse título fique errado no livro fiscal. O processo correto **é renegociar o título para que os novos títulos percam a ligação com a nota e fiquem sem o ICMS** (podendo ser baixado até parcialmente ou renegociados). O título original continua ligado à nota e todo o ICMS fica nele.

Dessa forma, a geração do livro fiscal para esses financeiros vai ficar correta porque já trata a configuração do parâmetro **"LIVFRETERENEG"** que determina se vai ser o título original ou os novos títulos gerados na renegociação.

Foi criada uma validação para evitar baixar parcialmente esse tipo de título, emitindo a mensagem: 'Um título de despesa de frete de origem "Estoque" que atualiza livro fiscal, não pode ser baixado com valor inferior. Utilize a renegociação de títulos porque a geração do livro desses títulos já está prevista pelo parâmetro **LIVFRETERENEG.'**

Para que consiga realizar a baixa parcial o ideal será **fazer uma renegociação desse título na tela "Renegociação de título",** sendo um título com valor que pretende baixar hoje e outro com valor restante.
