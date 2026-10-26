---
id: "26557530046487"
titulo: "Campo FATURA/DUPLICATA no DANFE com Compensação de Crédito"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26557530046487-Campo-FATURA-DUPLICATA-no-DANFE-com-Compensa%C3%A7%C3%A3o-de-Cr%C3%A9dito"
trilha: "Melhores Práticas > Vendas"
atualizado_em: "2026-07-22T14:41:19Z"
rotulos: ["Configuração", "NF-e", "Movimentação Financeira", "XML", "Crédito", "DANFE", "Passos para resolver", "Razão do erro", "Detalhe do erro", "DANFE com Compensação de Crédito", "Campo FATURA/DUPLICATA"]
---

# Campo FATURA/DUPLICATA no DANFE com Compensação de Crédito

Na impressão do DANFE é possível gerar na sessão **Fatura/Duplicata**informações sobre a compensação de crédito de cliente, com as seguintes alternativas: 

#### **(1)** Cenário 1:

**Parâmetros:**

**FINANCEXMLDANFE** = N
**DESFINPGCOMPDNF** = N

**Comportamento -** sistema irá imprimir no DANFE o financeiro atual da nota: parcelas em aberto e parcelas baixadas por compensação.

**Exemplo:**

TIP NEG A VISTA| OUT=001 Venc=14/12/2023 Valor=497,49 | OUT=002 Venc=30/12/2023 Valor=100,00

#### **(1)** Cenário 2:

**Parâmetros:**

FINANCEXMLDANFE = S
DESFINPGCOMPDNF = N

**Comportamento -** sistema irá imprimir no DANFE o financeiro conforme xml, ou seja, financeiro do momento da aprovação da nota, antes de ocorrer a compensação.

**Exemplo:**

TIP NEG A VISTA| Dup=001 Venc=14/12/2023 Valor=597,49

#### **(1)** Cenário 3:

**Parâmetros:**

FINANCEXMLDANFE = N
DESFINPGCOMPDNF = S

**Comportamento -** sistema irá imprimir no DANFE o financeiro atual da nota: parcelas em aberto e parcelas baixadas por compensação, incluindo a informação [pago] na frente da parcela baixada:

**Exemplo:**

TIP NEG A VISTA| OUT=001 Venc=14/12/2023 Valor=497,49 | OUT=002 Venc=30/12/2023 Valor=100,00 [pago]
