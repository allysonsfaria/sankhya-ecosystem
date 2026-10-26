---
id: "44011556112791"
titulo: "[TMS] Pedágio calculado em dobro"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011556112791--TMS-Ped%C3%A1gio-calculado-em-dobro"
trilha: "Lincros > TMS"
atualizado_em: "2026-10-05T19:06:26Z"
rotulos: ["sync_hc", "lincros", "sync_hash_9de99c3bac6c", "lincros_13438145"]
---

# [TMS] Pedágio calculado em dobro

**Menu:** Cadastros Gerais > Negociações > Tabela de Frete

**Objetivo:** Auxiliar no entendimento e resolução do cálculo “duplicado” no componente pedágio.

**Considerações:** O TMS permite o agrupamento de Pré-Notas, Notas, e Pré-Conhecimentos no embarque.

Estes agrupamentos têm por objetivo facilitar e agilizar o dia a dia, como por exemplo para uma cotação SPOT.

Entretanto, se a unificação não for realizada corretamente, ou a forma de cobrança do componente pedágio for realizada por CTRC, haverá uma cobrança “duplicada”.

Neste exemplo podemos observar que o valor original do pedágio é R$928,80.

![Imagem 1: Neste exemplo podemos observar que o valor original do pedágio é R$928,80.](https://ajuda.sankhya.com.br/hc/article_attachments/44011567835927)

Porém, na cotação o mesmo está sendo calculado em R$1857,60.

![Imagem 2: Porém, na cotação o mesmo está sendo calculado em R$1857,60.](https://ajuda.sankhya.com.br/hc/article_attachments/44011568062103)

Isso ocorre porque o componente de cálculo do pedágio “Fórmula de Cálculo do Pedágio” está configurado para somar por CTRC(Pré-Conhecimento).

A correção neste caso é bem simples, basta agrupar os Pré-Conhecimentos em um único, e posteriormente recalcular. 

**Conclusão**: Após o agrupamento dos Pré-Conhecimentos, o pedágio foi calculado apenas uma vez, conforme o esperado.

![Imagem 3: Conclusão : Após o agrupamento dos Pré-Conhecimentos, o pedágio foi calculado apenas uma vez, conforme o esperado.](https://ajuda.sankhya.com.br/hc/article_attachments/44011575005335)
