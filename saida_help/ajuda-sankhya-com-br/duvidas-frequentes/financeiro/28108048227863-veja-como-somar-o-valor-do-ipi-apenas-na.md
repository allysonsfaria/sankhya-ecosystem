---
id: "28108048227863"
titulo: "Veja como somar o valor do IPI apenas na primeira parcela de uma venda parcelada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/28108048227863-Veja-como-somar-o-valor-do-IPI-apenas-na-primeira-parcela-de-uma-venda-parcelada"
trilha: "Dúvidas Frequentes > Financeiro"
atualizado_em: "2026-07-22T14:38:18Z"
rotulos: ["Configuração", "NF-e", "Fórmulas", "Impostos", "Financeiro", "somar o valor do IPI apenas na primeira parcela de uma venda parcelada"]
---

# Veja como somar o valor do IPI apenas na primeira parcela de uma venda parcelada

**(1)** Este artigo tem o objetivo de mostrar como se realiza a correta configuração para somar o valor do IPI apenas na primeira parcela de uma venda usando um tipo de negociação parcelado.

![Imagem 1: Nas fórmulas das parcelas do tipo de negociação, siga o exemplo abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/28108031950743) Nas fórmulas das parcelas do tipo de negociação, siga o exemplo abaixo:

**(2)** Em um tipo de negociação dividido em quatro parcelas, **as fórmulas usadas ficariam da seguinte forma:**

- **Parcela 1:** ((VLRNOTA-VLRIPI) /4)+VLRIPI
- **Parcela 2:** (VLRNOTA-VLRIPI )/4
- **Parcela 3:** (VLRNOTA-VLRIPI  )/4
- **Parcela 4:** (VLRNOTA-VLRIPI   )/4

Antes de dividir pelo número de parcelas, subtraímos o IPI. Pois, em nosso exemplo a variável VLRNOTA (valor total da nota) já vem com o IPI somado, ou seja, o IPI está somando ao total da nota.

**Importante:** **os espaços citados a partir da parcela 2, após o campo 'VLRIPI' devem seguir um padrão**, para que o cálculo ocorra da maneira correta (1 espaço na parcela 2, 2 na parcela 3 e 3 na parcela 4).

**Observação:** normalmente o percentual das parcelas ficaria 25% cada, pois somados totalizam em 100%. Porém, quando se usa fórmulas nas parcelas em que para o mesmo tipo de título uma certa parcela tem uma fórmula **diferente**, é necessário informar 100% em **todas** as parcelas.
