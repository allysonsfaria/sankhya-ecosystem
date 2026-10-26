---
id: "27337065080727"
titulo: "Proporcionalização das Despesas Acessórias para cálculo de impostos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/27337065080727-Proporcionaliza%C3%A7%C3%A3o-das-Despesas-Acess%C3%B3rias-para-c%C3%A1lculo-de-impostos"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:39:47Z"
rotulos: ["Configuração", "NF-e", "ICMS", "Impostos", "TOP", "Despesas Acessórias", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Proporcionalização das Despesas Acessórias para cálculo de impostos", "Cálculo de Impostos"]
---

# Proporcionalização das Despesas Acessórias para cálculo de impostos

(1)**O que é a Proporcionalização das Despesas Acessórias no Cálculo de Impostos?**

A proporcionalização das despesas acessórias consiste em calcular os impostos (ICMS, IPI e Substituição Tributária - ST) aplicados sobre os valores de frete, seguro, destaque, embalagem e juros, quando presentes na nota fiscal.

(1)** Como configurar a incidência de impostos sobre despesas acessórias?**

Se os impostos já estão configurados para incidir sobre os produtos, acesse a aba de **"Despesas Acessórias"** na TOP (Comercial » Arquivo » Cadastros) e defina quais impostos devem incidir sobre cada tipo de despesa acessória.

Atualmente, na TOP, essa configuração é feita por imposto, permitindo especificar individualmente as despesas sobre as quais cada imposto deve ser calculado.

![Imagem 1: Atualmente, na TOP, essa configuração é feita por imposto, permitindo especificar individualmente as despesas sobre as…](https://ajuda.sankhya.com.br/hc/article_attachments/27493031774743)

(1)**Caso de Uso:**

Tenho uma nota fiscal com 3 itens, detalhados a seguir com seus respectivos valores totais:

1. **Produto 1020:** R$ 150,00
2. **Produto 1030:**R$ 890,00
3. **Produto 1040:**R$ 260,00

Nesta nota, incidem valores de ICMS sobre o valor do frete, que está incluso, no valor de R$ 95,00.

Exemplificação de cálculo:

| **Produto** | **Vlr. Total Item** | **Proprocio-nalização  Frete** | **Vlr. Proprocio-nalização** | **Bc. ICMS** | **Aliq. ICMS** | **Vlr. ICMS** | **Bc. ICMS Frete** | **Aliq. ICMS  Frete** | **Vlr. ICMS  Frete** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1020 | R$ 150,00 | 11,54% | R$ 10,96 | R$ 150,00 | 12,00% | R$ 18,00 | R$ 10,96 | 12,00% | R$ 1,32 |
| 1030 | R$ 890,00 | 68,46% | R$ 65,04 | R$ 890,00 | 12,00% | R$ 106,80 | R$ 65,04 | 12,00% | R$ 7,80 |
| 1040 | R$ 260,00 | 20,00% | R$ 19,00 | R$ 260,00 | 12,00% | R$ 31,20 | R$ 19,00 | 12,00% | R$ 2,28 |
|  |  |  |  |  |  |  |  |  |  |
| **TOTAL** | R$ 1.300,00 | 100,00% | R$ 95,00 | R$ 1.300,00 | - | R$ 156,00 | R$ 95,00 | - | R$ 11,40 |

No cálculo, o sistema aplicará a seguinte fórmula: o valor total de cada item será dividido pela soma dos valores de todos os itens, determinando assim a proporção do valor de cada produto em relação ao total da nota. Dessa forma, o sistema distribuirá o valor do frete proporcionalmente entre os produtos da nota.
