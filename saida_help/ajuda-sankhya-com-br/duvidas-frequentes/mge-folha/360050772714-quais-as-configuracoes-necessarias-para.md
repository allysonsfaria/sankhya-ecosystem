---
id: "360050772714"
titulo: "Quais as configurações necessárias para \"Demissão comum acordo\"?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360050772714-Quais-as-configura%C3%A7%C3%B5es-necess%C3%A1rias-para-Demiss%C3%A3o-comum-acordo"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:35:01Z"
rotulos: ["Configuração", "Atualização", "eSocial", "Folha de Pagamento", "Configurações para Demissão por Acordo", "FGTS"]
---

# Quais as configurações necessárias para "Demissão comum acordo"?

**(1)**  Criar um novo código de afastamento contemplando os novos códigos do governo criados para atender à lei:

Tela 'Códigos de Afastamento':

- Código de movimentação: I5 - Rescisão do Contrato por motivo de acordo.

![Imagem 1: Código de movimentação: I5 - Rescisão do Contrato por motivo de acordo.](https://ajuda.sankhya.com.br/hc/article_attachments/360087443553)

![Imagem 2: Código de movimentação: I5 - Rescisão do Contrato por motivo de acordo.](https://ajuda.sankhya.com.br/hc/article_attachments/360087443653)

![Imagem 3: Código de movimentação: I5 - Rescisão do Contrato por motivo de acordo.](https://ajuda.sankhya.com.br/hc/article_attachments/360087443733)

**(2)**  Criar um novo tipo de rescisão considerando os códigos de afastamento criados:

- Código de saque: 7 - RESCISÃO DO CONTRATO DE TRABALHO POR ACORDO ENTRE TRABALHADOR E EMPREGADOR – FORMALIZADA A PARTIR DE 11/11/2017 – LEI 13.467/2017

![Imagem 4: Código de saque: 7 - RESCISÃO DO CONTRATO DE TRABALHO POR ACORDO ENTRE TRABALHADOR E EMPREGADOR – FORMALIZADA A PARTIR…](https://ajuda.sankhya.com.br/hc/article_attachments/360087443813)

**(3)**  Alterar as fórmulas para realização do cálculo correto;

**201 - AVISO PRÉVIO INDENIZADO**

Fórmula:

IF((&Aviso ='S') And (&CAUAFA = 60) or (&CAUAFA = 82) AND (QueFuncionario.COMPSALARIO <> 2),((((queFuncionario.SALBASE \* IF(queFuncionario.TIPSAL = 5, queFuncionario.HORASSEM \* 5, 1)) + &VLRINCORPORA) / 30) \* &Diaavi) \* IF(QuelTFPafaF.CODGOVERNO = 'I5', 0.5, 1),0)

 Índice:

IF(QuelTFPafaF.CODGOVERNO = 'I5', &DIAAVI/2, &DIAAVI)

**990 - MULTA FGTS**

Fórmula:

TRUNCFOL(IF((QuelTFPafaF.DIRMULTAFGTS='S') And ((&CAUAFA = 60) OR (&CAUAFA =65) OR (QuelTFPafaF.CODGOVERNO = 'I5')), (((IF((&TIPFOL='R'),(&FGTSSALDO +(TRUNCFOL(((&E1826 \* IF((queFuncionario.CODCATEGESOCIAL = 107) OR (queFuncionario.CODCATEGESOCIAL = 108),queRegFiscal.PERFGTSCVA,queRegFiscal.PERPAGTOFGTS))/100),2) + TRUNCFOL(((&E1827 \*IF((queFuncionario.CODCATEGESOCIAL = 107) OR (queFuncionario.CODCATEGESOCIAL = 108),queRegFiscal.PERFGTSCVA,queRegFiscal.PERPAGTOFGTS))/100),2))), TRUNCFOL(((&E1826 \*IF((queFuncionario.CODCATEGESOCIAL = 107) OR (queFuncionario.CODCATEGESOCIAL = 108),queRegFiscal.PERFGTSCVA,queRegFiscal.PERPAGTOFGTS))/100),2) + TRUNCFOL(((&E1827 \*IF((queFuncionario.CODCATEGESOCIAL = 107) OR (queFuncionario.CODCATEGESOCIAL = 108),queRegFiscal.PERFGTSCVA,queRegFiscal.PERPAGTOFGTS))/100),2))) + IF(&FGTSMESANT='S',FSOMAEVE(queFuncionario.CODEMP, queFuncionario.CODFUNC, FSOMAMES(&REFERE, (-1)), 'N','1810') \* (IF((queFuncionario.CODCATEGESOCIAL = 107) OR (queFuncionario.CODCATEGESOCIAL = 108),queRegFiscal.PERFGTSCVA,queRegFiscal.PERPAGTOFGTS)/100), 0)) \* IF((&CAUAFA = 76),0.25,IF((QuelTFPafaF.CODGOVERNO ='I5') OR (queFuncionario.CODCATEGESOCIAL = 108),0.20,0.40))),0),2)

Índice: Sem fórmula

**(4)** Importar novo modelo de GRRF disponível no [Sankhya Place](http://place.sankhya.com.br/).

**(5)**  Atualizar a GRRF da caixa.
