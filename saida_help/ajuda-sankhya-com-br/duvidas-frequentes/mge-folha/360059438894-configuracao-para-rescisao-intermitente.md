---
id: "360059438894"
titulo: "Configuração para Rescisão Intermitente - MGE Pessoal"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360059438894-Configura%C3%A7%C3%A3o-para-Rescis%C3%A3o-Intermitente-MGE-Pessoal"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:35:23Z"
rotulos: ["#criadoRoger", "Configuração", "eSocial", "Folha de Pagamento", "Rescisão", "Cálculo rescisão intermitente: folha de rescisão", "Aviso prévio: cálculo diferenciado", "Eventos e fórmulas: Saldo salário DSR férias 13º", "Funcionário Intermitente"]
---

# Configuração para Rescisão Intermitente - MGE Pessoal

A folha responsável pelo cálculo da rescisão definitiva do funcionário intermitente é a folha de Rescisão. Porém, antes do cálculo é necessário cadastrar os eventos e fórmulas abaixo.

## Eventos e fórmulas

### 1.1 Saldo Salário Intermitente

O evento participará do cálculo da folha de rescisão do intermitente caso tenha convocação no mês da Rescisão.

#### Evento

Aba **"Propriedade"**

![Imagem 1: Aba "Propriedade"](https://ajuda.sankhya.com.br/hc/article_attachments/1500001098582)

Aba **"Incidência"**

![Imagem 2: Aba "Incidência"](https://ajuda.sankhya.com.br/hc/article_attachments/360102177033)

Aba **"Bases de Cálculo"**

![Imagem 3: Aba "Bases de Cálculo"](https://ajuda.sankhya.com.br/hc/article_attachments/360102177053)

#### Fórmula

IF((&TIPFOL='R') AND (QueFuncionario.CODCATEGESOCIAL=111), IF((QueFuncionario.TIPSAL=1),(QueFuncionario.SALBASE/ &DiaDivSalBase)\*&DIASTRA,(QueFuncionario.SALBASE \*IF(&HRSNORMAIS>0,&HRSNORMAIS,&DIASTRA))),0)

Índice: IF(&HRSNORMAIS > 0,&HRSNORMAIS, &DIASTRA)

### 1.2. DSR Rescisão

#### Evento

Aba **"Propriedades"**

![Imagem 4: Aba "Propriedades"](https://ajuda.sankhya.com.br/hc/article_attachments/1500001098642)

Aba **"Incidência"**

![Imagem 5: Aba "Incidência"](https://ajuda.sankhya.com.br/hc/article_attachments/1500001098662)

Aba **"Bases de Cálculos"**

![Imagem 6: Aba "Bases de Cálculos"](https://ajuda.sankhya.com.br/hc/article_attachments/1500001098682)

#### Fórmula

IF((QueFuncionario.CODCATEGESOCIAL=111),IF(QueFuncionario.TIPSAL=1,((QueFuncionario.SALBASE /&DiaDivSalBase) \* (&DIASTRA/6)),IF(QueFuncionario.TIPSAL=5,(QueFuncionario.SALBASE\* (&DIASTRA/6)),0)),0)

### 1.3. Férias intermitente rescisão

#### Evento

Aba **"Propriedades"**

![Imagem 7: Aba "Propriedades"](https://ajuda.sankhya.com.br/hc/article_attachments/1500001098702)

Aba **"Incidência"**

![Imagem 8: Aba "Incidência"](https://ajuda.sankhya.com.br/hc/article_attachments/360100000154)

Aba **"Bases de Cálculos"**

![Imagem 9: Aba "Bases de Cálculos"](https://ajuda.sankhya.com.br/hc/article_attachments/360102177133)

#### Fórmula IF((QueFuncionario.CODCATEGESOCIAL = 111),(&E38 + &E39 + &VLRINCORPORA)/12, 0)

&E38: saldo salário intermitente
&E39: DSR

### 1.4. Média férias intermitente rescisão

#### Evento

Aba **"Propriedades"**

![Imagem 10: Aba "Propriedades"](https://ajuda.sankhya.com.br/hc/article_attachments/1500001170001)

Aba **"Incidência"**

![Imagem 11: Aba "Incidência"](https://ajuda.sankhya.com.br/hc/article_attachments/1500001098822)

Aba **"Bases de Cálculo"**

![Imagem 12: Aba "Bases de Cálculo"](https://ajuda.sankhya.com.br/hc/article_attachments/360100000254)

#### Fórmula

IF((QueFuncionario.CODCATEGESOCIAL=111),&VLRINCIDEMEDIAS / 12,0)

###

### 1.5. 1/3 Férias Intermit Resc

#### Evento

Aba **"Propriedades"**

![Imagem 13: Aba "Propriedades"](https://ajuda.sankhya.com.br/hc/article_attachments/360102177173)

Aba **"Incidência"**

![Imagem 14: Aba "Incidência"](https://ajuda.sankhya.com.br/hc/article_attachments/360102177213)

Aba **"Bases de Cálculo"**

![Imagem 15: Aba "Bases de Cálculo"](https://ajuda.sankhya.com.br/hc/article_attachments/360100000314)

#### Fórmula

(&E40 + &E41)/3
&E40: FÉRIAS INTERMITENTE RESC
&E41: MEDIAS FER INTERMIT RESC

### 1.6. 13 Salário intermitente rescisão

#### Evento

Aba **"Propriedades"**

![Imagem 16: Aba "Propriedades"](https://ajuda.sankhya.com.br/hc/article_attachments/1500001099262)

Aba **"Incidência"**

![Imagem 17: Aba "Incidência"](https://ajuda.sankhya.com.br/hc/article_attachments/360100000914)

Aba **"Bases de Cálculo"**

![Imagem 18: Aba "Bases de Cálculo"](https://ajuda.sankhya.com.br/hc/article_attachments/360100000934)

####

#### Fórmula

IF((QueFuncionario.CODCATEGESOCIAL = 111),(&E38 + &E39)/12, 0)
&E38: saldo salário intermitente
&E39: DSR

### 1.7. Média 13º salário intermitente rescisão

#### Evento

Aba **"Propriedades"**

![Imagem 19: Aba "Propriedades"](https://ajuda.sankhya.com.br/hc/article_attachments/1500001170761)

Aba **"Incidência"**

![Imagem 20: Aba "Incidência"](https://ajuda.sankhya.com.br/hc/article_attachments/360100001014)

Aba **"Bases de Cálculo"**

![Imagem 21: Aba "Bases de Cálculo"](https://ajuda.sankhya.com.br/hc/article_attachments/1500001099442)

####

#### Fórmula

IF((QueFuncionario.CODCATEGESOCIAL=111),&VLRINCIDEMEDIAS / 12,0)

### 1.8. Aviso Prévio Indenizado Intermitente

O Aviso Prévio Indenizado para o intermitente tem o cálculo diferenciado utilizando toda a remuneração recebida pelo empregado nos últimos doze meses ou, quando menor que 12 meses, da data de admissão até a rescisão dividindo pelo número de meses trabalhado. O resultado é dividido por 30 e multiplicado pelo número de dias do aviso prévio.
O total das remunerações recebidas nos últimos 12 meses, incluindo os eventos de médias e os proventos do mês da Rescisão, quando há convocação, é apresentado na variável &BaseMediaInterm e a quantidade de meses trabalhados pelo intermitente nos últimos 12 meses é apresentado na variável &MesesMediaInterm.

####

#### Evento

Aba **"Propriedades"**

![Imagem 22: Aba "Propriedades"](https://ajuda.sankhya.com.br/hc/article_attachments/360100001034)

Aba **"Incidência"**

![Imagem 23: Aba "Incidência"](https://ajuda.sankhya.com.br/hc/article_attachments/360102178113)

Aba **"Bases de Cálculo"**

![Imagem 24: Aba "Bases de Cálculo"](https://ajuda.sankhya.com.br/hc/article_attachments/360100001394)

####

#### Fórmula

IF((&Aviso ='S') And (&CAUAFA = 60) AND (&TIPFOL='R') AND (QueFuncionario.CODCATEGESOCIAL=111),((&BaseMediaInterm/&MesesMediaInterm)/30) \* &Diaavi,0)
Índice: &Diaavi

### 1.9. Férias API intermitente

#### Evento

Aba **"Propriedades"**

![Imagem 25: Aba "Propriedades"](https://ajuda.sankhya.com.br/hc/article_attachments/360102178333)

Aba **"Incidência"**

![Imagem 26: Aba "Incidência"](https://ajuda.sankhya.com.br/hc/article_attachments/1500001099822)

Aba **"Bases de Cálculo"**

![Imagem 27: Aba "Bases de Cálculo"](https://ajuda.sankhya.com.br/hc/article_attachments/1500001171041)

####

#### Fórmula

IF((&Aviso ='S') And (&CAUAFA = 60) AND (&TIPFOL='R') AND (QueFuncionario.CODCATEGESOCIAL=111), (&E280/12)\*&MESPROPAPFER,0)

### 1.10. ⅓ Férias API intermitente

#### Evento

Aba **"Propriedades"**

![Imagem 28: Aba "Propriedades"](https://ajuda.sankhya.com.br/hc/article_attachments/360102178413)

Aba **"Incidência"**

![Imagem 29: Aba "Incidência"](https://ajuda.sankhya.com.br/hc/article_attachments/1500001099862)

Aba **"Bases de Cálculo"**

![Imagem 30: Aba "Bases de Cálculo"](https://ajuda.sankhya.com.br/hc/article_attachments/360100001534)

####

#### Fórmula

&E281/3

&E281: FÉRIAS API INTERMITENTE

### 1.11. 13º Sal API intermitente

#### Evento

Aba **"Propriedades"**

![Imagem 31: Aba "Propriedades"](https://ajuda.sankhya.com.br/hc/article_attachments/1500001171061)

Aba **"Incidência"**

![Imagem 32: Aba "Incidência"](https://ajuda.sankhya.com.br/hc/article_attachments/360102178473)

Aba **"Bases de Cálculo"**

![Imagem 33: Aba "Bases de Cálculo"](https://ajuda.sankhya.com.br/hc/article_attachments/360102178493)

####

#### Fórmula

IF((&Aviso ='S') And (&CAUAFA = 60) AND (&TIPFOL='R') AND (QueFuncionario.CODCATEGESOCIAL=111), (&E280/12)\*&MESPROPAP,0)

Índice: &MESPROPAP

### 1.12. Multa FGTS

A única alteração necessária no sistema para o funcionário intermitente é em relação à marcação da regra para cálculo no cadastro do evento, conforme exemplo abaixo:

![Imagem 34: A única alteração necessária no sistema para o funcionário intermitente é em relação à marcação da regra para cálculo…](https://ajuda.sankhya.com.br/hc/article_attachments/360102178513)
