---
id: "27537509361943"
titulo: "EFD ICMS/IPI - Registro C100 - Quando campo COD_SIT = 8"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/27537509361943-EFD-ICMS-IPI-Registro-C100-Quando-campo-COD-SIT-8"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-08-18T14:00:22Z"
rotulos: ["IPI", "SEFAZ", "ICMS", "Impostos", "EFD", "EFD ICMS/IPI", "CFOP's 5929 e/ou 6929", "Registro C100", "COD_SIT = 8"]
---

# EFD ICMS/IPI - Registro C100 - Quando campo COD_SIT = 8

Quando se está gerando o EFD ICMS/IPI, na geração do C100, temos o seguinte comportamento:

O sistema realiza as seguintes validações:

- Documento em questão está com o campo **COD\_SIT igual a 8 (Documento Fiscal emitido com base em Regime Especial ou Norma Específica)**

Sendo sim para a validação, os seguintes campos terão seus valores zerados ou deixados sem conteúdo no registro C100:

DT\_E\_S - Data da entrada ou da saída

VL\_DOC - Valor total do documento fiscal

IND\_PGTO - Indicador do tipo de pagamento

VL\_DESC - Valor total do desconto

VL\_ABAT\_NT - Abatimento não tributado e não comercial

VL\_MERC - Valor total das mercadorias e serviços

IND\_FRT - Indicador do tipo do frete

VL\_FRT - Valor do frete indicado no documento fiscal

VL\_SEG - Valor do seguro indicado no documento fiscal

VL\_OUT\_DA - Valor de outras despesas acessórias

VL\_BC\_ICMS - Valor da base de cálculo do ICMS

VL\_ICMS - Valor do ICMS

VL\_BC\_ICMS\_ST - Valor da base de cálculo do ICMS substituição tributária

VL\_ICMS\_ST - Valor do ICMS retido por substituição tributária

VL\_IPI - Valor total do IPI

VL\_PIS - Valor total do PIS

VL\_COFINS - Valor total da COFINS

VL\_PIS\_ST - Valor total do PIS retido por substituição tributária

VL\_COFINS\_ST - Valor total da COFINS retido por substituição tributária
