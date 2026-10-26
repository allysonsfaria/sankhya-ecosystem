---
id: "4410106481047"
titulo: "Cálculo contribuinte - Individual/Autônomo "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4410106481047-C%C3%A1lculo-contribuinte-Individual-Aut%C3%B4nomo"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:36:17Z"
rotulos: ["Configuração", "Cálculo", "Transporte", "Folha", "INSS", "#validadoAnaLucia", "Autônomo", "Ajuste conforme Sintegra", "Autônomos teto INSS", "Novas fórmulas cálculo"]
---

# Cálculo contribuinte - Individual/Autônomo 

## ![Imagem 1: Cálculo contribuinte - Individual/Autônomo](https://ajuda.sankhya.com.br/hc/article_attachments/42310325081111) Cálculo contribuinte - Individual/Autônomo

Como o autônomo não segue a nova regra de desconto de INSS, a verificação do teto de contribuição será feita através da **tabela de faixa** de código **5 - SALÁRIO MÍNIMO:**

![Imagem 2: Como o autônomo não segue a nova regra de desconto de INSS, a verificação do teto de contribuição será feita através da…](https://ajuda.sankhya.com.br/hc/article_attachments/16110351842583)

**Valor 2:** Valor máximo de desconto. 

**Valor 3:** Teto máximo de contribuição. 

## ![Imagem 3: Novas fórmulas](https://ajuda.sankhya.com.br/hc/article_attachments/42310340953751) Novas fórmulas

**Observação:**

**(1)** As fórmulas que estão adequadas nos pontos 2.1 e 2.2 abaixo, somente irão atender aos parceiros que utilizam a nova folha de autônomos.

**(1)** Parâmetro **‘FPCALAUTONOMOS’**setado.

### 2.1. Prestação de serviço

Fórmula a ser alterada para clientes que utilizam a rotina de autônomo

#### **(1)**9100 - INSS - HONORÁRIOS PREST SERV

| **Fórmula:**  IF((QueFuncionario.VINCULO = 90) AND ((queFuncionario.CODOCORRFGTS = '13') OR (queFuncionario.CODOCORRFGTS = '24')) AND (MemSetVar('BaseINSSfolServ', IF(&FolAutonomo = 'S', &F4101, &E1910 + ABS(FBES(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, &Refere, 'N,R', '505')))) > 0), IF((QueFuncionario.MEI = 'S'), 0, TRUNCFOL(IF(MemGetVar('BaseINSSfolServ') > FTF(5, 3, MemGetVar('BaseINSSfolServ'), &Refere, QueFuncionario.TIPTAB), FTF(5, 2, MemGetVar('BaseINSSfolServ'), &Refere, QueFuncionario.TIPTAB) - IF(&FolAutonomo = 'S', &F4102, 0), (MemGetVar('BaseINSSfolServ') \* 11 / 100) - IF(&FolAutonomo = 'S', &F4102, 0)), 2)), 0)  **Índice:**  11 / 100 |
| --- |

#### **(1)**4101 - RECOMPOSIÇÃO BASE INSS SERVIÇOS

| **Fórmula:**  IF((QueFuncionario.VINCULO = 90) AND ((queFuncionario.CODOCORRFGTS = '13') OR (queFuncionario.CODOCORRFGTS = '24')), IF((QueFuncionario.MEI = 'S'), 0, &E1910 + &E505 + ABS(FBES(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, &Refere, 'N,R', '1910,505'))), 0) |
| --- |

#### **(1)**4102- RECOMPOSIÇÃO INSS RETIDO SERVIÇOS

| **Fórmula:**  IF((QueFuncionario.VINCULO = 90) AND ((queFuncionario.CODOCORRFGTS = '13') OR (queFuncionario.CODOCORRFGTS = '24')), IF((QueFuncionario.MEI = 'S'), 0, &E506 + ABS(FBES(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, &Refere, 'N,R', '9100,506'))), 0) |
| --- |

#### **(1)**4107 - RECOMPOSIÇÃO BASE INSS SERVIÇOS

| **Fórmula:**  IF((QueFuncionario.VINCULO = 90) AND ((queFuncionario.CODOCORRFGTS = '13') OR (queFuncionario.CODOCORRFGTS = '24')), IF((QueFuncionario.MEI = 'S'), 0, &E1913 + &E510 + ABS(FBES(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, &Refere, 'N,R', '1913,510')) + ABS(FBES(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, &Refere, 'N,R', '999'))), 0) |
| --- |

#### **(1)**9130 - IRRF AUTÔNOMO SERVIÇOS

| **Fórmula:**  IF((QueFuncionario.VINCULO = 90) AND ((queFuncionario.CODOCORRFGTS = '13') OR (queFuncionario.CODOCORRFGTS = '24')) AND (MemSetVar('BaseIRRFfolServ', IF(&FolAutonomo = 'S', &F4107, &E1913 + ABS(FBES(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, &Refere, 'N,R', '510')))) > 0), IF((QueFuncionario.MEI = 'S'), 0, IF((MemSetVar('varIRRFServicos', (((MemGetVar('BaseIRRFfolServ') \* FTF(2, 1, MemGetVar('BaseIRRFfolServ'), &REFEREPAGTO, queFuncionario.TIPTAB) / 100) - FTF(2, 2, MemGetVar('BaseIRRFfolServ'), &REFEREPAGTO, queFuncionario.TIPTAB)) - IF(&FolAutonomo = 'S', &F4108, 0))) < queEventos.VLREVENTO), 0, MemGetVar('varIRRFServicos'))), 0)  **Índice:**  FTF(2, 1, IF(&FolAutonomo = 'S', &F4107, &E1913), &REFEREPAGTO, queFuncionario.TIPTAB) |
| --- |

### 2.2. Transporte rodoviário

#### **(1)**9110 -INSS AUTÔNOMO TRANSPORTADOR

| **Fórmula:**  IF((QueFuncionario.VINCULO = 90) AND ((queFuncionario.CODOCORRFGTS = '15') OR (queFuncionario.CODOCORRFGTS = '25')) AND (MemSetVar('BaseINSSfolTrans', IF(&FolAutonomo = 'S', &F4103, &E1850 + ABS(FBES(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, &Refere, 'N,R', '505')))) > 0), TRUNCFOL(IF(MemGetVar('BaseINSSfolTrans') > FTF(5, 3, MemGetVar('BaseINSSfolTrans'), &Refere, QueFuncionario.TIPTAB), FTF(5, 2, MemGetVar('BaseINSSfolTrans'), &Refere, QueFuncionario.TIPTAB) - IF(&FolAutonomo = 'S', &F4104, 0), (MemGetVar('BaseINSSfolTrans') \* 11 / 100) - IF(&FolAutonomo = 'S', &F4104, 0)), 2), 0)  **Índice:**  11 / 100 |
| --- |

#### **(1)**4103 - RECOMPOSIÇÃO BASE INSS TRANSPORTADOR

| **Fórmula:**  IF((QueFuncionario.VINCULO = 90) AND ((queFuncionario.CODOCORRFGTS = '15') OR (queFuncionario.CODOCORRFGTS = '25')), &E1850 + &E505 + ABS(FBES(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, &Refere, 'N,R', '1850,505')), 0) |
| --- |

#### **(1)**4104- RECOMPOSIÇÃO INSS RETIDO TRANSPORTADOR

| **Fórmula:**  IF((QueFuncionario.VINCULO = 90) AND ((queFuncionario.CODOCORRFGTS = '15') OR (queFuncionario.CODOCORRFGTS = '25')), &E506 + ABS(FBES(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, &Refere, 'N,R', '9110,506')), 0) |
| --- |

#### **(1)**1850 - BASE INSS REDUZIDA TRANSPORTE

| **Fórmula:**  IF((QueFuncionario.VINCULO = 90) AND (queFuncionario.CODOCORRFGTS = '15'), (&E5 \* 20 / 100), 0)  **Índice:**  20 / 100 |
| --- |

#### **(1)**1851 - BASE IRRF REDUZIDA TRANSPORTE

| **Fórmula:**  IF((QueFuncionario.VINCULO = 90) AND (queFuncionario.CODOCORRFGTS = '15'), (&E5 \* 10 / 100) - ABS(&E9110) - ABS(&E999), 0)  **Índice:**  10 / 100 |
| --- |

#### **(1)**1852 -PARCELA ISENTA BASE TRANSPORTE

| **Fórmula:**  IF(&FolAutonomo = 'S', 0, &E5 - &E1850 - &E1851)  **Índice:**  10 / 100 |
| --- |

#### **(1)**9310 - ISS AUTÔNOMO

| **Fórmula:**  IF((QueFuncionario.VINCULO = 90), (&E4 + &E5) \* queEventos.INDICE, 0)  **Índice:**  queEventos.INDICE |
| --- |

#### **(1)**9300 - SEST AUTÔNOMO TRANSPORTADOR

| **Fórmula:**  IF((QueFuncionario.VINCULO = 90) AND (queFuncionario.CODOCORRFGTS = '15'), (&E1850  \* queEventos.INDICE), 0)  **Índice:**  queEventos.INDICE |
| --- |

#### **(1)**9320 - SENAT AUTÔNOMO TRANSPORTADOR

| **Fórmula:**  IF((QueFuncionario.VINCULO = 90) AND (queFuncionario.CODOCORRFGTS = '15'), (&E1850  \* queEventos.INDICE), 0)  **Índice:**  queEventos.INDICE |
| --- |

#### **(1)**4105 -RECOMPOSIÇÃO BASE IRRF TRANSPORTE

| **Fórmula:**  IF((QueFuncionario.VINCULO = 90) AND ((queFuncionario.CODOCORRFGTS = '15') OR (queFuncionario.CODOCORRFGTS = '25')), &E1851 + &E510 + ABS(FBES(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, &Refere, 'N,R', '1851,510')) + ABS(FBES(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, &Refere, 'N,R', '999')), 0) |
| --- |

#### **(1)**4106 -RECOMPOSIÇÃO IRRF RETIDO TRANSPORTE

| **Fórmula:**  IF((QueFuncionario.VINCULO = 90) AND ((queFuncionario.CODOCORRFGTS = '15') OR (queFuncionario.CODOCORRFGTS = '25')), &E509 + ABS(FBES(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, &Refere, 'N,R', '9140,509')), 0) |
| --- |

#### **(1)**9140 - IRRF AUTÔNOMO TRANSPORTADOR

| **Fórmula:**  IF((QueFuncionario.VINCULO = 90) AND ((queFuncionario.CODOCORRFGTS = '15') OR (queFuncionario.CODOCORRFGTS = '25')) AND (MemSetVar('BaseIRRFfolTrans', IF(&FolAutonomo = 'S', &F4105, &E1851 + ABS(FBES(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, &Refere, 'N,R', '510')))) > 0), IF((MemSetVar('varIRRFTransporte', (((MemGetVar('BaseIRRFfolTrans') \* FTF(2, 1, MemGetVar('BaseIRRFfolTrans'), &REFEREPAGTO, queFuncionario.TIPTAB) / 100) - FTF(2, 2, MemGetVar('BaseIRRFfolTrans'), &REFEREPAGTO, queFuncionario.TIPTAB)) - IF(&FolAutonomo = 'S', &F4106, 0))) < queEventos.VLREVENTO), 0, MemGetVar('varIRRFTransporte')), 0)  **Índice:**  FTF(2, 1, IF(&FolAutonomo = 'S', &F4105, &E1851), &REFEREPAGTO, queFuncionario.TIPTAB) |
| --- |

####

### 2.3. Expressões para adaptação das fórmulas do desconto INSS para clientes que não utilizam a nova rotina de autônomos

(1)**Valor máximo de desconto:**

FTF(5,2,XXXX,&Refere,QueFuncionario.TIPTAB) 

XXXX - Substituir por &E “CÓDIGO DO EVENTO”. Ex: &E4 

(1)**Teto máximo de contribuição:**

FTF(5,3,XXXX,&Refere,QueFuncionario.TIPTAB) 

XXXX - Substituir por &E “CÓDIGO DO EVENTO”. Ex: &E4
