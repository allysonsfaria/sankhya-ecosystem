---
id: "360043863494"
titulo: "Como somar o FCP ao total da nota?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043863494-Como-somar-o-FCP-ao-total-da-nota"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-22T15:58:35Z"
rotulos: ["#PUBLIFER", "#revisadohugo", "O.S1457161", "Configuração", "NF-e", "ICMS", "Impostos", "Alíquota ICMS-ST: Inclui FCP", "Exemplo de Cálculo: ST + FCP", "Configurações Necessárias: Somar ST à nota calcular FCP", "FCP"]
---

# Como somar o FCP ao total da nota?

**(1)** Conforme norma técnica NT 2018.005\_v1\_10:

"N10b N 1-1 3v2-4 Deve ser informada a alíquota do cálculo do ICMS-ST,  já incluso o FCP caso incida sobre a mercadoria. Exemplo: alíquota da mercadoria na venda ao consumidor final = 18% e 2% de FCP. A alíquota a ser informada no campo pST deve ser 20%."

Dessa forma, com as devidas configurações, o valor do FCP é**somado ao valor do ST**. Considere o seguinte exemplo:

- Vlr. total do item = 100,00
- % FCP: 2%
- Vlr. FCP = 2,00
- % ST: 14%
- Vlr. ST será 14,00 + 2,00 = 16,00 [Vlr.ST + Vlr. FCP]

Para o comportamento acima, atente-se as seguintes configurações:

- TOP marcada para SOMAR ST ao total da nota: aba **"Impostos", "Somar ST ao total da nota"**
- TOP marcada para 'Calcular FCP': aba **"Impostos",** **"Calcular FCP (ICMS/ST) Interno?"**
