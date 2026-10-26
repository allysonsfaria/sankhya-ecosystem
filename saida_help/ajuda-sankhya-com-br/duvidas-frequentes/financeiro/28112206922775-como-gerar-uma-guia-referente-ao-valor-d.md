---
id: "28112206922775"
titulo: "Como gerar uma guia referente ao 'Valor de Diferencial'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/28112206922775-Como-gerar-uma-guia-referente-ao-Valor-de-Diferencial"
trilha: "Dúvidas Frequentes > Financeiro"
atualizado_em: "2026-07-22T14:38:17Z"
rotulos: ["Configuração", "Fórmulas", "Movimentação Financeira", "Impostos", "Financeiro", "Como gerar uma guia referente ao 'Valor de Diferencial'"]
---

# Como gerar uma guia referente ao 'Valor de Diferencial'

**(1)** Este artigo tem o objetivo de mostrar como se realiza a correta configuração para geração de uma guia referente ao Valor de Diferencial dos impostos dos itens.

![Imagem 1: (1) Este artigo tem o objetivo de mostrar como se realiza a correta configuração para geração de uma guia referente ao…](https://ajuda.sankhya.com.br/hc/article_attachments/28116034527255)

![Imagem 2: (1) Este artigo tem o objetivo de mostrar como se realiza a correta configuração para geração de uma guia referente ao…](https://ajuda.sankhya.com.br/hc/article_attachments/28116012048919)

![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/28112202325143)  **SOLUÇÃO:**

![Imagem 4: Acesse a tela "Tipo de negociação", vá até a aba "Parcelas" e nela inclua uma parcela no título (em questão) com a…](https://ajuda.sankhya.com.br/hc/article_attachments/28112202332439) Acesse a tela **"Tipo de negociação",**vá até a aba **"Parcelas"** e nela inclua uma parcela no título (em questão) com a fórmula abaixo:

**VAL(PDES('sum(valordiferencial)','tgfdin','nunota = '+NUNOTA))**

![Imagem 5: VAL(PDES('sum(valordiferencial)','tgfdin','nunota = '+NUNOTA))](https://ajuda.sankhya.com.br/hc/article_attachments/28112202335255)

Conforme demonstrado abaixo, esse campo refere-se ao 'Valor de Diferencial' da tabela de Imposto/Item/Nota [TGFDIN]:

![Imagem 6: Conforme demonstrado abaixo, esse campo refere-se ao 'Valor de Diferencial' da tabela de Imposto/Item/Nota (TGFDIN):](https://ajuda.sankhya.com.br/hc/article_attachments/28112202336407)

![Imagem 7: Observação:](https://ajuda.sankhya.com.br/hc/article_attachments/28115728764951) **Observação:**

Se houver uma compensação financeira no lançamento da Nota Fiscal feita com Valor de Diferencial, o sistema a reconhecerá como um título. Sendo assim, o valor da referida Nota Fiscal será afetado, logo é necessário realizar esse lançamento através de um projeto adaptativo.
