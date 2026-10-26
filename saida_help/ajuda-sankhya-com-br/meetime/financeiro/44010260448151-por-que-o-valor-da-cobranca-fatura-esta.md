---
id: "44010260448151"
titulo: "Por que o valor da cobrança/fatura está diferente da Nota Fiscal?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010260448151-Por-que-o-valor-da-cobran%C3%A7a-fatura-est%C3%A1-diferente-da-Nota-Fiscal"
trilha: "Meetime > Financeiro"
atualizado_em: "2026-10-05T18:33:49Z"
rotulos: ["sync_hc", "meetime", "meetime_424", "sync_hash_93dbcaea002a"]
---

# Por que o valor da cobrança/fatura está diferente da Nota Fiscal?

De acordo com a legislação vigente a partir de Julho de 2015, a retenção dos impostos **CSLL** (1,0%), **PIS** (0,65%), **COFINS** (3,0%) e **IR** (1,5%) se torna obrigação do tomador de Serviços (e portanto deduzida do valor do boleto).

Se você pertence ao **Lucro real ou presumido**, quando a soma dos impostos **CSLL**, **PIS** e **COFINS (CSRF),** é superior a R$ 10,00, ela deve ser descontada do valor do boleto, caso contrário, a responsabilidade de recolhimento é da prestadora e o boleto fica no valor cheio.

A mesma regra se aplica separadamente ao **IR**. Se ele for superior a R$ 10,00, deve ser descontado do valor da fatura.

## EX:

1. Valor NF: R$ 667,00

Valor CSRF: R$ 31,01

Valor IR: R$ 10,00

## Valor da cobrança: 625,99

Valor NF: R$ 500,00
Valor CSRF: R$ 23,25

Valor IR: R$ 7,50

## Valor da cobrança: 476,75

Valor NF: R$ 215,00
Valor CSRF: R$ 9,99

Valor IR: R$ 3,22

## Valor da cobrança: 215,00

Se você pertence ao **Simples Nacional,** irá possuir apenas a incidência do **IR**, e para  ser descontado, ele deve ser superior a R$ 10,00.

Isto porque, de acordo com o art. 647 do Decreto 3.000/99, os serviços prestados pela **Meetime Desenvolvimento de Softwares LTDA**  se enquadram nos CNAEs de pessoas jurídicas que **precisam deduzir o valor do Imposto de Renda diretamente de seu recebimento bruto**, ou seja, as cobranças são emitidas a um valor menor cuja diferença para Nota Fiscal representa exatamente o **valor do imposto a ser retido pelo tomador do serviço**.

## EX:

1. Valor NF: R$ 667,00

Valor IR: R$ 10,00

## Valor da cobrança: 657,00

1. Valor NF: R$ 500,00

Valor IR: R$ 7,50

## Valor da cobrança: 500,00

Todos os valores ficam discriminados no campo "Dados Adicionais" de sua nota fiscal.

Lembrando que em ambos os casos **a obrigação de recolhimento destes imposto é do tomador de serviços**, através da emissão de uma DIRF junto à Receita Federal.

---

Ainda tem dúvidas? Entre em contato com a gente através do 
e-mail [suporte@meetime.com.br](mailto:suporte@meetime.com.br) ou WhatsApp através do número de telefone [(48) 3204-7590](https://wa.me/554832047590).
