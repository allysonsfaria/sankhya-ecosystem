---
id: "37227137458839"
titulo: "Registro F500 – Campo 2 VL_REC_CAIXA: Cálculo e Aplicação na EFD-Contribuições"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37227137458839-Registro-F500-Campo-2-VL-REC-CAIXA-C%C3%A1lculo-e-Aplica%C3%A7%C3%A3o-na-EFD-Contribui%C3%A7%C3%B5es"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:14:28Z"
rotulos: ["Impostos", "CFOP", "Financeiro", "EFD Contribuições", "Registro F500", "Nota fiscal", "Campo 2 VL_REC_CAIXA", "PIS e COFINS"]
---

# Registro F500 – Campo 2 VL_REC_CAIXA: Cálculo e Aplicação na EFD-Contribuições

O **Registro F500** da **EFD-Contribuições** é utilizado para informar as receitas apuradas pelo **regime de caixa**.

Nesse registro, o **Campo 2 – VL\_REC\_CAIXA** indica o valor da receita efetivamente recebida no período, sendo essencial para a correta apuração do **PIS e da COFINS**.

Este artigo explica o conceito desse campo e sua aplicação no **Sankhya**, destacando os principais cálculos e procedimentos envolvidos na escrituração.

**Cenário com duas notas fiscais:**

**Nota Fiscal 1**

Possui dois itens, totalizando **R$ 200,00**:

- **Item 1:** Valor de R$100,00, CFOP 5102, CST PIS/COFINS = 01
- **Item 2:** Valor de R$100,00, CFOP 5102, CST PIS/COFINS = 06

**Nota Fiscal 2**

Possui um único item, totalizando **R$ 100,00**:

- **Item 1:** Valor de R$100,00, CFOP 5102, CST PIS/COFINS = 01

No exemplo apresentado, ambos os financeiros das notas foram baixados em sua **integralidade**.

Ao gerar a **EFD PIS/COFINS**, o sistema calcula a **proporção de cada CFOP/CST** para determinar o valor que será totalizado no **Registro F500**. O cálculo é feito da seguinte forma:

**Nota Fiscal 1:**

- Total da nota: R$ 200,00
- Item 1: CFOP 5102, CST 01, valor R$ 100,00
- Item 2: CFOP 5102, CST 06, valor R$ 100,00
- **Índice:** 100 / 200 = 0,50
- Aplicando o índice sobre o valor da baixa (R$200,00), temos: 200 × 0,50 = **R$100,00**
- Esse valor é armazenado como **sub-total** para CFOP 5102 e CST 01

**Nota Fiscal 2:**

- Total da nota: R$ 100,00
- Item 1: CFOP 5102, CST 01, valor R$ 100,00
- **Índice**: 100 / 100 = 1,00
- Aplicando o índice sobre o valor da baixa (R$ 100,00), temos: 100 × 1,00 = R$ 100,00

**Resultado**

No campo **VL\_REC\_CAIXA** do Registro F500, será apresentado o valor total de **R$ 200,00**, refletindo a soma das proporções das notas por CFOP e CST.
