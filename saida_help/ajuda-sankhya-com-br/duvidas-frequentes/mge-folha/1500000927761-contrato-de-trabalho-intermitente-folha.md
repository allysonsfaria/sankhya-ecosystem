---
id: "1500000927761"
titulo: "Contrato de Trabalho Intermitente - Folha Mensal - MGE Pessoal"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/1500000927761-Contrato-de-Trabalho-Intermitente-Folha-Mensal-MGE-Pessoal"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:31:08Z"
rotulos: ["#criadoRoger", "Configuração", "Contrato", "Fórmulas", "eSocial", "Folha de Pagamento", "alário intermitente: fórmula cálculo dias convocação DSR incluído", "Férias intermitente: cálculo proporcional médias terço", "13º salário intermitente: fórmula proporcional INSS IRRF", "Trabalho Intermitente"]
---

# Contrato de Trabalho Intermitente - Folha Mensal - MGE Pessoal

Veja aqui as principais configurações para o contrato de trabalho Intermitente.

**![Imagem 1: Cadastro dos eventos e fórmulas](https://ajuda.sankhya.com.br/hc/article_attachments/16282195446551) Cadastro dos eventos e fórmulas**

**1.1. Salário intermitente**

**Evento**

**(2)**Aba **"Propriedade"**

![Imagem 2: (2) Aba "Propriedade"](https://ajuda.sankhya.com.br/hc/article_attachments/1500001113462)

**(2)** Aba **"Incidência"**

![Imagem 3: (2) Aba "Incidência"](https://ajuda.sankhya.com.br/hc/article_attachments/1500001113582)

**(2)** Aba **"Bases de Cálculo"**

![Imagem 4: (2) Aba "Bases de Cálculo"](https://ajuda.sankhya.com.br/hc/article_attachments/360102193793)

(1)** Fórmula salário intermitente**

IF((QueFuncionario.CODCATEGESOCIAL <> 111),0, IF(QueFuncionario.TIPSAL=1, (QueFuncionario.SALBASE / &DiaDivSalBase) \* &DIASTRA, QueFuncionario.SALBASE \* IF(&HRSNORMAIS > 0,&HRSNORMAIS, &DIASTRA)))

Índice: IF((&HRSNORMAIS<>0),&HRSNORMAIS,&DIASTRA)

**![Imagem 5: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16282211937175) OBSERVAÇÃO:**

A fórmula do salário do intermitente remunera todos os dias da convocação, desde a data início até a data fim da convocação. Há empresas na quais o intermitente trabalha todos os dias da convocação, quando isso ocorrer a empresa deverá pagar a verba de DSR para o funcionário, porque a cada 6 dias trabalhados um dia será pago a título de DSR.
Porém há também empresas nas quais o funcionário intermitente trabalha de segunda a sábado e folga no domingo, nesse caso não há necessidade de calcular a verba de DSR, pois o evento de salário do intermitente já incluirá esse dia não trabalhado.

**1.2. DSR intermitente**

**Evento**

**(2)** Aba **"Propriedades"**

![Imagem 6: (2) Aba "Propriedades"](https://ajuda.sankhya.com.br/hc/article_attachments/1500001114282)

**(2)** Aba **"Incidência"**

![Imagem 7: (2) Aba "Incidência"](https://ajuda.sankhya.com.br/hc/article_attachments/360100013794)

**(2)** Aba **"Bases de Cálculos"**

![Imagem 8: (2) Aba "Bases de Cálculos"](https://ajuda.sankhya.com.br/hc/article_attachments/1500001114342)

(1)** Fórmula- DSR intermitente**

IF((QueFuncionario.CODCATEGESOCIAL=111),IF(QueFuncionario.TIPSAL=1,((QueFuncio nario.SALBASE /&DiaDivSalBase) \*

(&DIASTRA/6)),IF(QueFuncionario.TIPSAL=5,(QueFuncionario.SALBASE\* (&DIASTRA/6)),0)),0)

**![Imagem 9: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16282211937175) OBSERVAÇÃO:**

A fórmula divide por 6 a &DIASTRA, utilizando a regra disposta na Lei 605/49 que dispõe que a cada 6 dias trabalhados o funcionário possui um dia não trabalhado remunerado.

**1.3. Férias intermitente**

**Evento**

**(2)** Aba **"Propriedades"**

![Imagem 10: (2) Aba "Propriedades"](https://ajuda.sankhya.com.br/hc/article_attachments/1500001115122)

**(2)** Aba **"Incidência"**

![Imagem 11: (2) Aba "Incidência"](https://ajuda.sankhya.com.br/hc/article_attachments/360102195033)

**(2)** Aba **"Bases de Cálculo"**

![Imagem 12: (2) Aba "Bases de Cálculo"](https://ajuda.sankhya.com.br/hc/article_attachments/360100014754)

(1)** Fórmula- Férias intermitente**

IF((QueFuncionario.CODCATEGESOCIAL = 111),(&E30 + &E31 + &VLRINCORPORA)/12,0)
&E30 : EVENTO DE SALÁRIO INTERMITENTE
&E31: EVENTO DE DSR INTERMITENTE

**1.4. Médias de férias intermitente**

**Evento**

**(2)** Aba **"Propriedades"**

![Imagem 13: (2) Aba "Propriedades"](https://ajuda.sankhya.com.br/hc/article_attachments/1500001311722)

**(2)** Aba **"Incidência"**

![Imagem 14: (2) Aba "Incidência"](https://ajuda.sankhya.com.br/hc/article_attachments/1500001376181)

**(2)** Aba **"Bases de Cálculo"**

![Imagem 15: (2) Aba "Bases de Cálculo"](https://ajuda.sankhya.com.br/hc/article_attachments/1500001376281)

(1)** Fórmula - Média férias intermitente**

IF((QueFuncionario.CODCATEGESOCIAL=111),&VLRINCIDEMEDIAS / 12,0)

**1.5. Terço de férias intermitente**

**Evento**

**(2)** Aba **"Propriedades"**

![Imagem 16: (2) Aba "Propriedades"](https://ajuda.sankhya.com.br/hc/article_attachments/360102386293)

**(2)** Aba **"Incidência"**

![Imagem 17: (2) Aba "Incidência"](https://ajuda.sankhya.com.br/hc/article_attachments/360100211254)

**(2)** Aba **"Bases de Cálculo"**

![Imagem 18: (2) Aba "Bases de Cálculo"](https://ajuda.sankhya.com.br/hc/article_attachments/1500001311822)

(1)** Fórmula - ⅓ Férias intermitente**

(&E33 + &E34)/3
&E33: FÉRIAS INTERMITENTE
&E34: MÉDIA DE FÉRIAS INTERMITENTE

**1.6 13º Salário intermitente**

**Evento**

**(2)** Aba **"Propriedades"**

![Imagem 19: (2) Aba "Propriedades"](https://ajuda.sankhya.com.br/hc/article_attachments/1500001311922)

**(2)** Aba **"Incidência"**

![Imagem 20: (2) Aba "Incidência"](https://ajuda.sankhya.com.br/hc/article_attachments/1500001312002)

**(2)** Aba **"Bases de Cálculo"**

![Imagem 21: (2) Aba "Bases de Cálculo"](https://ajuda.sankhya.com.br/hc/article_attachments/360100211514)

(1)** Fórmula - 13º Salário intermitente**

IF((QueFuncionario.CODCATEGESOCIAL = 111),(&E30 + &E31)/12, 0)
&E30 : EVENTO DE SALÁRIO INTERMITENTE
&E31: EVENTO DE DSR INTERMITENTE

**1.7 Médias 13º salário intermitente**

**Eventos**

**(2)** Aba **"Propriedades"**

![Imagem 22: (2) Aba "Propriedades"](https://ajuda.sankhya.com.br/hc/article_attachments/1500001376821)

**(2)** Aba **"Incidência"**

![Imagem 23: (2) Aba "Incidência"](https://ajuda.sankhya.com.br/hc/article_attachments/360102386873)

**(2)** Aba **"Bases de Cálculo"**

![Imagem 24: (2) Aba "Bases de Cálculo"](https://ajuda.sankhya.com.br/hc/article_attachments/360102387133)

(1)** Fórmula - Médias 13º salário intermitente**

IF((QueFuncionario.CODCATEGESOCIAL=111),&VLRINCIDEMEDIAS / 12,0)

**1.8 Fórmulas auxiliares para cálculo do INSS**

**![Imagem 25: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16282211937175) OBSERVAÇÃO:**

Na parametrização do sistema, o usuário deverá colocar os códigos das fórmulas, conforme criado na base do cliente. Os códigos abaixo foram utilizados na base de teste. Veja:

(1)** Fórmula 5030: Base INSS intermitente**

IF(QueFuncionario.CODCATEGESOCIAL = 111,FBES(queFuncionario.CODEMP, queFuncionario.CODFUNC, &REFERE, 'N', '1901'), 0)
**Observação:** Esta fórmula deverá ser somada no final da fórmula 5008. + &F5030

(1)** Fórmula 5008: Base INSS FCOMPL/NORMAL/FERIAS**

&E1901 + &E505 + IF((&TIPFOL = 'O') AND (&INSSMESAMES = 'N'), &E1900 + &E1902 + &E1922,IF(&FOLHACPL = 'S',
FBECPL(QueFuncionario.CODEMP,QueFuncionario.CODFUNC,&Refere,'F','1902') +
FBECPL(QueFuncionario.CODEMP,QueFuncionario.CODFUNC,&Refere,'F','1922'),
FBE(QueFuncionario.CODEMP,QueFuncionario.CODFUNC,&Refere,'F','1902') +
FBE(QueFuncionario.CODEMP,QueFuncionario.CODFUNC,&Refere,'N','1921'))) +
IF((&RecompoeCompl =
'S'),FBE(QueFuncionario.CODEMP,QueFuncionario.CODFUNC,&Refere,'F,N,O','1901,1902
,1922'),0) + &F5030

(1)** Fórmula 5031: INSS intermitente**

IF(QueFuncionario.CODCATEGESOCIAL = 111, Abs(FBES(queFuncionario.CODEMP,
queFuncionario.CODFUNC, &REFERE, 'N', '901')), 0)
**Observação:** Esta fórmula deverá ser somada no final da fórmula 5009. + &F5031

(1)** Fórmula 5009: INSS RETIDO FCOMPL/NORMAL/FERIAS**

IF((&TIPFOL = 'O') AND (&INSSMESAMES = 'N'), &E900 + &E902 + &E922, &E506 +
ABS(IF(&FOLHACPL = 'S',
FBECPL(QueFuncionario.CODEMP,QueFuncionario.CODFUNC,&Refere,'F','902') +
FBECPL(QueFuncionario.CODEMP,QueFuncionario.CODFUNC,&Refere,'F','922'),
FBE(QueFuncionario.CODEMP,QueFuncionario.CODFUNC,&Refere,'F','902') +
FBE(QueFuncionario.CODEMP,QueFuncionario.CODFUNC,&Refere,'N','921')) +
FBE(QueFuncionario.CODEMP,QueFuncionario.CODFUNC,&Refere,'F','506'))) +
IF((&RecompoeCompl =
'S'),ABS(FBE(QueFuncionario.CODEMP,QueFuncionario.CODFUNC,&Refere,'F,N,O','901,9
02,922')),0) + ABS(&E921)+ &F5031

(1)** Fórmula: INSS décimo terceiro**

**5033: BASE INSS 13 INTERMITENTE**

IF(QueFuncionario.CODCATEGESOCIAL = 111,FBES(queFuncionario.CODEMP,
queFuncionario.CODFUNC, &REFERE, 'N', '1903'), 0)
**Observação:** Esta fórmula deverá ser somada no final da fórmula 5003. + &F5033

(1)** Fórmula 5003: Base INSS 13º COMPL/RESCISAO**

&E1903 + &E503 +
FBE(QueFuncionario.CODEMP,QueFuncionario.CODFUNC,&Refere,'DS','1903,735') +
IF(&TIPFOL = 'O', 0, IF(&TIPFOL =
'C',FBE(QueFuncionario.CODEMP,QueFuncionario.CODFUNC,&Refere,'R','1903,735'),0) +
IF(((&TIPFOL = 'R') AND
(FBE(QueFuncionario.CODEMP,QueFuncionario.CODFUNC,&Refere,'R','307') > 0)) OR
((&TIPFOL = 'N') AND
(FBE(QueFuncionario.CODEMP,QueFuncionario.CODFUNC,&Refere,'N','307') > 0)) OR
(&TIPFOL =
'C'),FBE(QueFuncionario.CODEMP,QueFuncionario.CODFUNC,&Refere,'DS','1903,735'),0)
+ IF(&RecompoeCompl =
'S',FBE(QueFuncionario.CODEMP,QueFuncionario.CODFUNC,&Refere,'O','1903'),0))+
&F5033

(1)** Fórmula 5034: INSS 13 INTERMITENTE**

IF(QueFuncionario.CODCATEGESOCIAL = 111, Abs(FBES(queFuncionario.CODEMP,
queFuncionario.CODFUNC, &REFERE, 'N', '903')), 0)
Obs.: Esta fórmula deverá ser somada no final da fórmula 5004. + &F5034

(1)** Fórmula 5004: INSS retido FCOMPL/RESCISÃO/13º**

IF(&TIPFOL <> 'O',&E502 + IF(&RecompoeCompl =
'S',ABS(FBE(QueFuncionario.CODEMP,QueFuncionario.CODFUNC,&Refere,'O','903')),0) +
IF(&TIPFOL =
'C',ABS(FBE(QueFuncionario.CODEMP,QueFuncionario.CODFUNC,&Refere,'R','903,502')),
0) +
ABS(FBE(QueFuncionario.CODEMP,QueFuncionario.CODFUNC,&Refere,'DS','903,502')),0
)+ &F5034

**1.9 Fórmulas auxiliares IRRF**

(1)** Fórmula 5035: Base IRRF intermitente**

IF(QueFuncionario.CODCATEGESOCIAL = 111,FBES(queFuncionario.CODEMP,
queFuncionario.CODFUNC, &REFERE, 'N', '1904'), 0)

**![Imagem 26: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16282211937175) OBSERVAÇÃO:**

Essa fórmula deve ser incluída na FÓRMULA 9002.

(1)** Fórmula 9002 - Base 1904 data de pagamento**

IF((&FOLHACPL = 'S') AND (&TIPFOL <> 'O'),0,IF((&DataPagamento >= &REFERE) AND
(&DataPagamento <= (FSOMAMES(&REFERE,1) -1)) AND
((MES(DTOC(&DataPagamento)) = MES(DTOC(&REFERE))) AND (&TIPFOL = 'N')),
IF(&TIPFOL = 'A',&E1916, &E1904 + &E1907 +&F5035 +&E510 +
FBEDTPAG(queFuncionario.CODEMP, queFuncionario.CODFUNC, &DataPagamento,
'650,1904') + MemSetVar('varTransfIRRF',FBEDTPAG(QueFuncionario.CODEMPORIG,
QueFuncionario.CODFUNCORIG, &DataPagamento, '1904') +
FBEDTPAG(QueFuncionario.CODEMPORIG, QueFuncionario.CODFUNCORIG,
&DataPagamento, '1907'))), IF(&TIPFOL = 'A',
IF((FBE(QueFuncionario.CODEMP,QueFuncionario.CODFUNC,Fsomames(&Refere,-1),'A','
650') <= 0) AND
(FBE(QueFuncionario.CODEMPORIG,QueFuncionario.CODFUNCORIG,Fsomames(&Refer
e,-1),'A','650') <= 0),FBEDTPAG(queFuncionario.CODEMP, queFuncionario.CODFUNC,
&DataPagamento, '1904'), FBEDTPAG(queFuncionario.CODEMP,
queFuncionario.CODFUNC, &DataPagamento, '1904') +
FBEDTPAG(queFuncionario.CODEMP, queFuncionario.CODFUNC, &DataPagamento,
'650')+ FBEDTPAG(QueFuncionario.CODEMPORIG, QueFuncionario.CODFUNCORIG,
&DataPagamento, '1904')) + &E1916, &E1904 + &E1907 + &E510 +
MemGetVar('varTransfIRRF') + FBEDTPAG(queFuncionario.CODEMP,
queFuncionario.CODFUNC, &DataPagamento, '1916'))))

**![Imagem 27: Cálculo individual da folha mensal](https://ajuda.sankhya.com.br/hc/article_attachments/16282195456407) Cálculo individual da folha mensal**

**a) Informações importantes antes do cálculo**

**(2)** Cadastro do período de convocação na rotina ‘Convocação de Trabalho Intermitente’;
**(2)** Os períodos cadastrados devem estar dentro da mesma referência, conforme exemplo abaixo
REFERÊNCIA:07/2020

(3)**Convocação 1**

![Imagem 28: (3) Convocação 1](https://ajuda.sankhya.com.br/hc/article_attachments/1500001313262)

(3)**Convocação 2**

![Imagem 29: (3) Convocação 2](https://ajuda.sankhya.com.br/hc/article_attachments/360100213694)

**![Imagem 30: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16282211937175) OBSERVAÇÃO:**

Se houver dias de convocação na próxima referência, o usuário deverá lançar outra convocação com os dias de convocação da próxima referência, para que os tributos respeitem a regra de competência.

**b) Cálculo por período trabalhado**
Caminho: **MGE PESSOAL » CÁLCULOS » INTERMITENTE**
O usuário terá a opção de calcular por período de convocação ou calcular todas as convocações da referência (Folha Mensal), porém cabe esclarecer que uma vez calculado por período na referência o cálculo deverá ser feito apenas por período.
Se o usuário optar por pagar por período convocado, deverá escolher na tela do Cálculo de Intermitentes>> Convocação a convocação que deseja pagar, conforme print abaixo:

Cálculo da convocação 1 da referência 07/2020- código da convocação=4

![Imagem 31: Cálculo da convocação 1 da referência 07/2020- código da convocação=4](https://ajuda.sankhya.com.br/hc/article_attachments/360100215114)

![Imagem 32: Cálculo da convocação 1 da referência 07/2020- código da convocação=4](https://ajuda.sankhya.com.br/hc/article_attachments/1500001315722)

Cálculo da convocação 2 da referência 07/2020- código convocação 5

![Imagem 33: Cálculo da convocação 2 da referência 07/2020- código convocação 5](https://ajuda.sankhya.com.br/hc/article_attachments/360100215174)

O último cálculo da referência fará recomposição das bases, calculará o INSS da folha normal e descontará o que já foi pago na folha anterior. Já para o IRRF, o valor da base da folha da convocação anterior que não atingia o mínimo será somada com a base da última convocação da referência e descontará o IRRF

**![Imagem 34: IMPORTANTE: Após o cálculo da folha do intermitente, é necessário que o usuário faça novamente o cálculo da folha do…](https://ajuda.sankhya.com.br/hc/article_attachments/16282195466263) IMPORTANTE:**
Após o cálculo da folha do intermitente, é necessário que o usuário faça novamente o cálculo da folha do intermitente na folha mensal, para que o sistema possa liberar a folha para envio ao eSocial e confirme no cadastro da Convocação do Intermitente que a folha foi calculada.

**![Imagem 35: Resumo da Folha](https://ajuda.sankhya.com.br/hc/article_attachments/16282211943063) Resumo da Folha**

Para o usuário ter acesso ao resumo da folha do funcionário intermitente deve acessar o Resumo da Folha e escolher a opção Folha Suplementar, conforme print abaixo:

![Imagem 36: Para o usuário ter acesso ao resumo da folha do funcionário intermitente deve acessar o Resumo da Folha e escolher a…](https://ajuda.sankhya.com.br/hc/article_attachments/1500001379681)

**![Imagem 37: Integração com o Financeiro](https://ajuda.sankhya.com.br/hc/article_attachments/16282211946007) Integração com o Financeiro**

O usuário terá a opção de integrar com o financeiro a folha do intermitente por convocação marcando a opção Folha Suplementar e escolhendo a sequência ou integrar de uma única vez marcando apenas a opção Normal, conforme print abaixo:

![Imagem 38: O usuário terá a opção de integrar com o financeiro a folha do intermitente por convocação marcando a opção Folha…](https://ajuda.sankhya.com.br/hc/article_attachments/360102390013)
