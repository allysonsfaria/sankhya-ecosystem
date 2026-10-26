---
id: "360042758594"
titulo: "Valor do ICMS relativo ao Fundo de Combate à Pobreza na UF de destino difere do calculado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042758594-Valor-do-ICMS-relativo-ao-Fundo-de-Combate-%C3%A0-Pobreza-na-UF-de-destino-difere-do-calculado"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:06:03Z"
rotulos: ["ERRONF", "Configuração", "NF-e", "SEFAZ", "ICMS", "Impostos", "793", "Divergência no Valor do ICMS do Fundo de Combate à Pobreza", "Erro"]
---

# Valor do ICMS relativo ao Fundo de Combate à Pobreza na UF de destino difere do calculado

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16086868993431) MENSAGEM:**

793- Rejeição: Valor do ICMS relativo ao Fundo de Combate à Pobreza na UF de destino difere do calculado.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16086868996759) SOLUÇÃO:**

Normalmente estas divergências estão relacionadas a arredondamentos e ou conversões de casas decimais. Vamos utilizar o caso de Uso abaixo para compreender de forma mais clara:

![Imagem 3: Através da Central de Vendas, na linha referente a cada item, botão (...) "Outras Opções" >> Consultar/Alterar dados…](https://ajuda.sankhya.com.br/hc/article_attachments/16086869002391) Através da Central de Vendas, na linha referente a cada item, botão [...] **"Outras Opções"** >> **Consultar/Alterar dados dos impostos do Item**, busque pela linha referente ao Imposto ICMS:

![Imagem 4: Através da Central de Vendas, na linha referente a cada item, botão (...) "Outras Opções" >> Consultar/Alterar dados…](https://ajuda.sankhya.com.br/hc/article_attachments/12154077596311)

![Imagem 5: Anote os valores destacados abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/16086869005335) Anote os valores destacados abaixo:

- Perc.para Fundo Comb. Pobreza
- Vlr. para Fundo Comb. Pobreza
- Base para Fundo Comb. Pobreza

![Imagem 6: Base para Fundo Comb. Pobreza](https://ajuda.sankhya.com.br/hc/article_attachments/12154111386135)

![Imagem 7: Realize o cálculo:](https://ajuda.sankhya.com.br/hc/article_attachments/16086869007767) Realize o cálculo:

**Base para Fundo X Perc.para fundo = Vlr. para Fundo**

Teremos nesse caso:

**100 x 2% = 2**

Contudo, o 'Vlr para fundo com. pobreza' que consta no sistema é =**1,96**

![Imagem 8: Para o caso acima, ajuste o 'Vlr para fundo com. pobreza' para 2,00 .](https://ajuda.sankhya.com.br/hc/article_attachments/16086839779095) Para o caso acima, ajuste o 'Vlr para fundo com. pobreza' para **2,00**.

![Imagem 9: Feito o ajuste, gere um novo lote da respectiva nf-e.](https://ajuda.sankhya.com.br/hc/article_attachments/16086869011991) Feito o ajuste, gere um novo lote da respectiva nf-e.

**![Imagem 10: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16086869023127)CAUSA:**

Quando for emitida uma NF-e e o Valor do ICMS relativo ao Fundo de Combate à Pobreza na UF de Destino (<vFCPUFDest>) informado no produto for diferente da multiplicação entre a Base de Cálculo da UF de Destino (<vBCFCPUFDest>) e o Percentual do Fundo de Combate a Pobreza na UF de Destino (<pFCPUFDest>), será retornada a rejeição.
