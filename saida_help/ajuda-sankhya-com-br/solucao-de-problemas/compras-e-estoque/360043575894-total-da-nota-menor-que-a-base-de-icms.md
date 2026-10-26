---
id: "360043575894"
titulo: "Total da nota menor que a base de ICMS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043575894-Total-da-nota-menor-que-a-base-de-ICMS"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T16:02:16Z"
rotulos: ["CORE_E03081", "Configuração", "NF-e", "ICMS", "Impostos", "Preferências", "Divergência entre Valor da Nota e Base de ICMS"]
---

# Total da nota menor que a base de ICMS

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16092900391703) MENSAGEM:**

[CORE\_E03081] Total da nota menor que a base de ICMS.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16092854224535) SOLUÇÃO:**

![Imagem 3: Valide se os valores apresentados para a Base de ICMS estão coerentes com o esperado. Em caso negativo, revalide as…](https://ajuda.sankhya.com.br/hc/article_attachments/16092854227479) Valide se os valores apresentados para a Base de ICMS estão coerentes com o esperado. Em caso negativo, revalide as configurações da exceção de ICMS desse lançamento, de acordo com o recomendado pela Contabilidade. Após ajustes, testes uma nova confirmação do lançamento.

![Imagem 4: Caso essa divergência seja válida, para permitir sua confirmação no sistema é necessário que o parâmetro abaixo seja…](https://ajuda.sankhya.com.br/hc/article_attachments/16092854233367) Caso essa divergência seja válida, para permitir sua confirmação no sistema é necessário que o parâmetro abaixo seja ligado:

**(2)** Tela **"Preferências"** (Configurações >> Avançado)

**(2)** Chave **"ACEITARVLRMEICM - Aceitar valor da nota menor que a base de ICMS"**

![Imagem 5: (2) Chave "ACEITARVLRMEICM - Aceitar valor da nota menor que a base de ICMS"](https://ajuda.sankhya.com.br/hc/article_attachments/12290562356759)

![Imagem 6: Após ligar o parâmetro teste a confirmação novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16092854243607) Após ligar o parâmetro teste a confirmação novamente.

**(1)** **IMPORTANTE:**

**(2)** Manter esse parâmetro como **Ligado** pode propiciar lançamentos indevidos, visto que esse valor a maior não é algo comum.

**(2)** Caso alinhe que para essa nota em específico de fato ele precise ser ajustado, aconselhamos retorná-lo para **Desligado** em seguida.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16092900418711) CAUSA:**

Ao tentar confirmar lançamentos, onde a informação Base de ICMS possuir um valor maior que o Vlr.Nota será apresentada a mensagem.
