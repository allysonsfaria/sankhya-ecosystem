---
id: "360044085053"
titulo: "Base de ICMS maior que o total da nota"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044085053-Base-de-ICMS-maior-que-o-total-da-nota"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T16:02:15Z"
rotulos: ["#PUBLIFER", "CORE_E00345", "Configuração", "Fiscal", "NF-e", "ICMS", "Impostos", "Nota Fiscal", "Preferências", "Erro de Base de ICMS"]
---

# Base de ICMS maior que o total da nota

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16108066856087) MENSAGEM:**

[CORE\_E00345] Base de ICMS maior que o total da nota.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16108099168151) SOLUÇÃO:**

![Imagem 3: Revise os valores de impostos apresentados em seu lançamento, preferencialmente com o apoio de seu Contador. Dessa…](https://ajuda.sankhya.com.br/hc/article_attachments/16108066863383) Revise os valores de impostos apresentados em seu lançamento, preferencialmente com o apoio de seu Contador. Dessa forma, conseguirá compreender se essa diferença de valor entre a 'Base de ICMS' e o 'Valor Total da Nota' é coerente. Caso seja incoerente, realize os devidos ajustes.

Caso seja coerente, realize a análise abaixo:

![Imagem 4: Verifique na tela " Preferências " (Configurações » Avançado) o parâmetro " ACEITARVLRMEICM - Aceitar valor da nota…](https://ajuda.sankhya.com.br/hc/article_attachments/16108066864791) Verifique na tela **"[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias)"** (Configurações » Avançado) o parâmetro **"ACEITARVLRMEICM - Aceitar valor da nota menor que a base de ICMS":**

Se estiver **"Sim"**, permitirá que a nota tenha base de ICMS com valor maior que o total da nota.

Se estiver **"Não"**, caso o valor da base de ICMS superior ao total da nota o sistema barrará a inclusão.

![Imagem 5: Se estiver "Não" , caso o valor da base de ICMS superior ao total da nota o sistema barrará a inclusão.](https://ajuda.sankhya.com.br/hc/article_attachments/12300027001879)

(1)** IMPORTANTE:**

**(2)** Manter esse parâmetro como 'Ligado' pode propiciar lançamentos indevidos, visto que esse valor a maior não é algo comum.

**(2)** Caso alinhe que para essa nota em específico de fato ele precise ser ajustado, retorne-o para 'Desligado' em seguida.

**![Imagem 6: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/16108099181975) CAUSA**:

Ao tentar confirmar lançamentos, onde a informação 'Base de ICMS' possuir um valor maior que o Vlr.Nota será apresentada a mensagem.
