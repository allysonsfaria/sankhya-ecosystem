---
id: "9935217529751"
titulo: "Valor da substituição extra nota não pode ficar negativo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9935217529751-Valor-da-substitui%C3%A7%C3%A3o-extra-nota-n%C3%A3o-pode-ficar-negativo"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T15:05:14Z"
rotulos: ["Configuração", "NF-e", "Impostos", "Alíquotas de ICMS", "CORE E04477", "Valor ST não pode ser negativo", "ST calculada negativa", "Ajustar alíquotas e marcar opção de zerar valor negativo", "Erro"]
---

# Valor da substituição extra nota não pode ficar negativo

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/17318040931351) **MENSAGEM:**

[CORE E04477] Valor da substituição extra nota não pode ficar negativo

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17266512069911) SOLUÇÃO:**

![Imagem 3: Primeiro busque na tela "Alíquotas de ICMS" (Caminho de acesso: Comercial » Arquivo » Cadastros » Alíquotas) a regra…](https://ajuda.sankhya.com.br/hc/article_attachments/17266512072343) Primeiro busque na tela **"Alíquotas de ICMS"** (Caminho de acesso: Comercial » Arquivo » Cadastros » Alíquotas) a regra que irá incidir sobre a nota fiscal eletrônica gerada e revise os valores configurados na aba **"Substituição Tributária"**.

![Imagem 4: Caso os valores estejam corretos e de fato é provável o cálculo de um valor ST negativo, realize a marcação " Zerar…](https://ajuda.sankhya.com.br/hc/article_attachments/17266512074647) Caso os valores estejam corretos e de fato é provável o cálculo de um valor ST negativo, realize a marcação "**Zerar valor da substituição tributária quando negativo**" (Aba Substituição Tributária/ Tela Alíquotas de ICMS).

![Imagem 5: Caso os valores estejam corretos e de fato é provável o cálculo de um valor ST negativo, realize a marcação " Zerar…](https://ajuda.sankhya.com.br/hc/article_attachments/12292716718103)

- Zerar valor da substituição tributária quando negativo: se esta opção estiver marcada e o cálculo de ST resultar em menor que zero, o sistema deixará o cálculo zerado.
- Caso a opção esteja desmarcada e o cálculo de ST venha a ser menor que zero, o sistema emitirá a mensagem: "Valor da substituição não pode ficar negativo. Produto: xxxx".

![Imagem 6: Realizada a marcação, refaça o faturamento.](https://ajuda.sankhya.com.br/hc/article_attachments/17266512077079) Realizada a marcação, refaça o faturamento.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17266512077719)CAUSA:**

Ocorre ao realizar emissão de NF-e e a regra de ICMS calculada irá gerar um valor de ST menor que zero, se a opção Zerar valor da substituição tributária quando negativo estiver desmarcada, será apresentada a mensagem.
