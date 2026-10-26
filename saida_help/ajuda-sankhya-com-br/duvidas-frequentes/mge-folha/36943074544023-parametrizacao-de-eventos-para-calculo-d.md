---
id: "36943074544023"
titulo: "Parametrização de eventos para cálculo da Isenção do IRRF 2026 - MGE Pessoal"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36943074544023-Parametriza%C3%A7%C3%A3o-de-eventos-para-c%C3%A1lculo-da-Isen%C3%A7%C3%A3o-do-IRRF-2026-MGE-Pessoal"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:35:41Z"
rotulos: ["Configuração", "Fórmulas", "Atualização", "Impostos", "Lei n.º 15.270/2025", "IRRF", "Cálculo do IRRF 2026", "ISENÇÃO DE IRRF", "MGE Pessoal"]
---

# Parametrização de eventos para cálculo da Isenção do IRRF 2026 - MGE Pessoal

**Módulo:** MGE Pessoal

**Versão:** 4.66.0.32

A [Lei n.º 15.270/2025](https://www.in.gov.br/web/dou/-/lei-n-15.270-de-26-de-novembro-de-2025-671614220) traz novas regras de isenção do IRRF a partir de janeiro de 2026. Para atender a essas mudanças no **MGEPessoal**, é necessário atualizar o sistema para a versão **4.66.0.32** ou superior e **criar manualmente** a tabela de faixas, os eventos de isenção e as fórmulas.

Verifique especialmente os **eventos personalizados de IRRF** para garantir que estejam configurados corretamente e sigam o fluxo de cálculo adequado.

**(1)** **Atualize** o MGE Pessoal para a **versão: 4.66.0.32** ou superior.

**(2)** Crie a **tabela de faixa** com o código: 7542 - ISENÇÃO DE IRRF:

![Imagem 1: (2) Crie a tabela de faixa com o código: 7542 - ISENÇÃO DE IRRF:](https://ajuda.sankhya.com.br/hc/article_attachments/36943424060695)

**(3)** Configure as **fórmulas** para isenção do IRRF:

**Os códigos** informados nas fórmulas abaixo **devem ser adaptados pelos códigos da sua base de dados**.

| **9381 - ISENÇÃO IRRF PL 1087/2025** | |
| --- | --- |
| **Fórmula** | IF((ANO(DTOC(&Referepagto)) > 2025) AND (&F9102 > 0), IF(MemSetVar('RendTrib', &F9102 + IF(isBaseSimplificadaMP1171(12), &VLRSIMPLIRRF, ABS(fValorEventosFolha(getEventosIdentificados('101, 107, 166, 167,176'))+FBEDTPAG(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, &DataPagamento, getEventosIdentificados('101, 107, 166, 167'))+IF(&TIPFOL = 'A',FBEDTPAG(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, &DataPagamento, getEventosIdentificados('176')),0)))) <= FTF(7542, 1, 0, &Referepagto, QueFuncionario.TIPTAB), FTF(7542, 2, 0, &Referepagto, QueFuncionario.TIPTAB), ROUND((FTF(7542, 1, MemGetVar('RendTrib'), &Referepagto, QueFuncionario.TIPTAB) \* FTF(7542, 2, MemGetVar('RendTrib'), &Referepagto, QueFuncionario.TIPTAB)) - (MemGetVar('RendTrib') \* FTF(7542, 2, MemGetVar('RendTrib'), &Referepagto, QueFuncionario.TIPTAB)), 2)), 0) |

**DE / PARA:**

**&F9102** / Fórmula auxiliar: RECOMPOSICAO BASE IRRF

####

| **9382 - ISENÇÃO IRRF PL 1087/2025 FERIAS** | |
| --- | --- |
| **Fórmula** | IF((ANO(DTOC(&Referepagto)) > 2025) AND (&F9103 > 0), IF(MemSetVar('RendTrib', &F9103 + IF(isBaseSimplificadaMP1171(22), &VLRSIMPLIRRF, ABS(fValorEventosFolha(getEventosIdentificados('148, 151, 201'))))) <= FTF(7542, 1, 0, &Referepagto, QueFuncionario.TIPTAB), FTF(7542, 2, 0, &Referepagto, QueFuncionario.TIPTAB), ROUND((FTF(7542, 1, MemGetVar('RendTrib'), &Referepagto, QueFuncionario.TIPTAB) \* FTF(7542, 2, MemGetVar('RendTrib'), &Referepagto, QueFuncionario.TIPTAB)) - (MemGetVar('RendTrib') \* FTF(7542, 2, MemGetVar('RendTrib'), &Referepagto, QueFuncionario.TIPTAB)), 2)), 0) |

**DE / PARA:**

**&F9103** / Fórmula auxiliar: RECOMPOSICAO BASE IRRF FERIAS

####

| **9383 - ISENÇÃO IRRF PL 1087/2025 13º** | |
| --- | --- |
| **Fórmula** | IF((ANO(DTOC(&Referepagto)) > 2025) AND (&F5060 > 0), IF(MemSetVar('RendTrib', &F5060 + IF(isBaseSimplificadaMP1171(13), &VLRSIMPLIRRF, ABS(fValorEventosFolha(getEventosIdentificados('104, 168, 177'))))) <= FTF(7542, 1, 0, &Referepagto, QueFuncionario.TIPTAB), FTF(7542, 2, 0, &Referepagto, QueFuncionario.TIPTAB), ROUND((FTF(7542, 1, MemGetVar('RendTrib'), &Referepagto, QueFuncionario.TIPTAB) \* FTF(7542, 2, MemGetVar('RendTrib'), &Referepagto, QueFuncionario.TIPTAB)) - (MemGetVar('RendTrib') \* FTF(7542, 2, MemGetVar('RendTrib'), &Referepagto, QueFuncionario.TIPTAB)), 2)), 0) |

**DE / PARA:**

&F**5060** / Fórmula auxiliar: RECOMPOSICAO BASE IRRF 13

####

| **9384 - ISENÇÃO IRRF PL 1087/2025 SERVICOS** | |
| --- | --- |
| **Fórmula** | IF((ANO(DTOC(&Referepagto)) > 2025) AND (&F4107 > 0), IF(MemSetVar('RendTrib', &F4107 + IF(isBaseSimplificadaMP1171(15), &VLRSIMPLIRRF, ABS(fValorEventosFolha(getEventosIdentificados('109, 176'))))) <= FTF(7542, 1, 0, &Referepagto, QueFuncionario.TIPTAB), FTF(7542, 2, 0, &Referepagto, QueFuncionario.TIPTAB), ROUND((FTF(7542, 1, MemGetVar('RendTrib'), &Referepagto, QueFuncionario.TIPTAB) \* FTF(7542, 2, MemGetVar('RendTrib'), &Referepagto, QueFuncionario.TIPTAB)) - (MemGetVar('RendTrib') \* FTF(7542, 2, MemGetVar('RendTrib'), &Referepagto, QueFuncionario.TIPTAB)), 2)), 0) |

**DE / PARA:**

&F**4107** / Fórmula auxiliar: RECOMPOSICAO BASE IRRF SERVICOS

####

| **9385 - ISENÇÃO IRRF PL 1087/2025 TRANSPORTE** | |
| --- | --- |
| **Fórmula** | IF((ANO(DTOC(&Referepagto)) > 2025) AND (&F4105 > 0), IF(MemSetVar('RendTrib', &F4105 + IF(isBaseSimplificadaMP1171(16), &VLRSIMPLIRRF, ABS(fValorEventosFolha(getEventosIdentificados('111, 176'))))) <= FTF(7542, 1, 0, &Referepagto, QueFuncionario.TIPTAB), FTF(7542, 2, 0, &Referepagto, QueFuncionario.TIPTAB), ROUND((FTF(7542, 1, MemGetVar('RendTrib'), &Referepagto, QueFuncionario.TIPTAB) \* FTF(7542, 2, MemGetVar('RendTrib'), &Referepagto, QueFuncionario.TIPTAB)) - (MemGetVar('RendTrib') \* FTF(7542, 2, MemGetVar('RendTrib'), &Referepagto, QueFuncionario.TIPTAB)), 2)), 0) |

**DE / PARA:**

&F**4105** / Fórmula auxiliar: RECOMPOSICAO BASE IRRF TRANSPORTE

####

| **9386 - ISENÇÃO IRRF PL 1087/2025 INTERMITENTE** | |
| --- | --- |
| **Fórmula** | IF((ANO(DTOC(&Referepagto)) > 2025) AND (&F5160 > 0), IF(MemSetVar('RendTrib', &F5160 + IF(isBaseSimplificadaMP1171(12), &VLRSIMPLIRRF, ABS(fValorEventosFolha(getEventosIdentificados('101, 107, 166, 167,176'))))) <= FTF(7542, 1, 0, &Referepagto, QueFuncionario.TIPTAB), FTF(7542, 2, 0, &Referepagto, QueFuncionario.TIPTAB), ROUND((FTF(7542, 1, MemGetVar('RendTrib'), &Referepagto, QueFuncionario.TIPTAB) \* FTF(7542, 2, MemGetVar('RendTrib'), &Referepagto, QueFuncionario.TIPTAB)) - (MemGetVar('RendTrib') \* FTF(7542, 2, MemGetVar('RendTrib'), &Referepagto, QueFuncionario.TIPTAB)), 2)), 0) |

**DE / PARA:**

&F**5160** / Fórmula auxiliar: RECOMPOSICAO BASE IRRF INTERMITENTE

| **9387 - ISENÇÃO IRRF PL 1087/2025 S/ 13° INTERMITENTE** | |
| --- | --- |
| **Fórmula** | IF((ANO(DTOC(&Referepagto)) > 2025) AND (&F5160 > 0), IF(MemSetVar('RendTrib', &F5160 + IF(isBaseSimplificadaMP1171(12), &VLRSIMPLIRRF, ABS(fValorEventosFolha(getEventosIdentificados('101, 107, 166, 167,176'))))) <= FTF(7542, 1, 0, &Referepagto, QueFuncionario.TIPTAB), FTF(7542, 2, 0, &Referepagto, QueFuncionario.TIPTAB), ROUND((FTF(7542, 1, MemGetVar('RendTrib'), &Referepagto, QueFuncionario.TIPTAB) \* FTF(7542, 2, MemGetVar('RendTrib'), &Referepagto, QueFuncionario.TIPTAB)) - (MemGetVar('RendTrib') \* FTF(7542, 2, MemGetVar('RendTrib'), &Referepagto, QueFuncionario.TIPTAB)), 2)), 0) |

**DE / PARA:**

&F**5160** / Fórmula auxiliar: RECOMPOSICAO BASE IRRF INTERMITENTE

####

| **9388 - ISENÇÃO IRRF PL 1087/2025 PRO LABORE** | |
| --- | --- |
| **Fórmula** | IF((ANO(DTOC(&Referepagto)) > 2025), IF(MemSetVar('RendTrib', (@E\_BASEINSSPROLABORE + @E\_BASEINSSOUTRASFONTES)) <= FTF(7542, 1, 0, &Referepagto, QueFuncionario.TIPTAB), FTF(7542, 2, 0, &Referepagto, QueFuncionario.TIPTAB), ROUND((FTF(7542, 1, MemGetVar('RendTrib'), &Referepagto, QueFuncionario.TIPTAB) \* FTF(7542, 2, MemGetVar('RendTrib'), &Referepagto, QueFuncionario.TIPTAB)) - (MemGetVar('RendTrib') \* FTF(7542, 2, MemGetVar('RendTrib'), &Referepagto, QueFuncionario.TIPTAB)), 2)), 0) |

**DE / PARA:**

**@E\_BASEINSSPROLABORE** / Evento BASE INSS PRO LABORE. **Exemplo:** &E1902
**@E\_BASEINSSOUTRASFONTES** / Evento BASE INSS OUTRAS FONTES. **Exemplo:** &E505

**(1)** Ajuste as fórmulas de desconto do IRRF para prever a isenção:

| **9040 - IRRF** | |
| --- | --- |
| **Fórmula** | IF(MemSetVar('DIRRF',IF((QueFuncionario.CODCATEGESOCIAL = 111) OR (QueFuncionario.VINCULO = 90) OR ((&TIPFOL = 'A') AND (&REGIMEIRRFCAIXA = 'N')) OR (CTOI(PDESPARAM('1', 'TFPFUN', 'CODEMP = :INT\_CODEMP AND CODFUNC = :INT\_CODFUNC AND DTLAUDORRA IS NOT NULL', STR(QueFuncionario.CODEMP), STR(QueFuncionario.CODFUNC))) = 1), 0, (((&F9102 \* FTF(2, 1, &F9102, &DataPagamento, QueFuncionario.TIPTAB)) / 100) - FTF(2, 2, &F9102, &DataPagamento, QueFuncionario.TIPTAB)) - &F9101) - &F9381) >= queEventos.VLREVENTO, MemGetVar('DIRRF'), 0) |

**DE / PARA:**

&F**9102** / Fórmula auxiliar: RECOMPOSICAO BASE IRRF
&F**9101** / Fórmula auxiliar: RECOMPOSICAO IRRF RETIDO
&F**9381** / Fórmula auxiliar: ISENÇÃO IRRF PL 1087/2025

####

| **9050 IRRF - FERIAS** | |
| --- | --- |
| **Fórmula** | IF(MemSetVar('DIRRF',IF((QueFuncionario.CODCATEGESOCIAL = 111) OR (QueFuncionario.VINCULO = 90) OR (CTOI(PDESPARAM('1', 'TFPFUN', 'CODEMP = :INT\_CODEMP AND CODFUNC = :INT\_CODFUNC AND DTLAUDORRA IS NOT NULL', STR(QueFuncionario.CODEMP), STR(QueFuncionario.CODFUNC))) = 1), 0, (((&F9103 \* FTF(2, 1, &F9103, &DataPagamento, QueFuncionario.TIPTAB)) / 100) - FTF(2, 2, &F9103, &DataPagamento, QueFuncionario.TIPTAB)) - &F9104) - &F9382) >= queEventos.VLREVENTO, MemGetVar('DIRRF'), 0) |

**DE / PARA:**

&F**9103** / Fórmula auxiliar: RECOMPOSICAO BASE IRRF FERIAS
&F**9104** / Fórmula auxiliar: RECOMPOSICAO IRRF RETIDO FERIAS
&F**9382** / Fórmula auxiliar: ISENÇÃO IRRF PL 1087/2025 FÉRIAS

####

| **9060 - IRRF - 13 SALARIO** | |
| --- | --- |
| **Fórmula** | IF(MemSetVar('DIRRF',IF((QueFuncionario.CODCATEGESOCIAL = 111) OR (QueFuncionario.VINCULO = 90) OR (CTOI(PDESPARAM('1', 'TFPFUN', 'CODEMP = :INT\_CODEMP AND CODFUNC = :INT\_CODFUNC AND DTLAUDORRA IS NOT NULL', STR(QueFuncionario.CODEMP), STR(QueFuncionario.CODFUNC))) = 1), 0, (((&F5060 \* FTF(2, 1, &F5060, &DataPagamento, QueFuncionario.TIPTAB)) / 100) - FTF(2, 2, &F5060, &DataPagamento, QueFuncionario.TIPTAB)) - &F5070) - &F9383) >= queEventos.VLREVENTO, MemGetVar('DIRRF'), 0) |

**DE / PARA:**

&F**5060** / Fórmula auxiliar: RECOMPOSICAO BASE IRRF 13
&F**5070** / Fórmula auxiliar: RECOMPOSICAO IRRF RETIDO 13
&F**9383** / Fórmula auxiliar: ISENÇÃO IRRF PL 1087/2025 13º

####

| **9130 - IRRF AUTONOMO SERVICOS** | |
| --- | --- |
| **Fórmula** | IF((QueFuncionario.VINCULO = 90) AND ((queFuncionario.CODOCORRFGTS = '13') OR (queFuncionario.CODOCORRFGTS = '24')) AND (QueFuncionario.MEI = 'N'), IF((MemSetVar('varIRRFServicos', (((&F4107 \* FTF(2, 1, &F4107, &DataPagamento, queFuncionario.TIPTAB) / 100) - FTF(2, 2, &F4107, &DataPagamento, queFuncionario.TIPTAB)) - &F4108) - &F9384) < queEventos.VLREVENTO), 0, MemGetVar('varIRRFServicos')), 0) |

**DE / PARA:**

&F**4107** / Fórmula auxiliar: RECOMPOSICAO BASE IRRF SERVICOS
&F**4108** / Fórmula auxiliar: RECOMPOSICAO IRRF RETIDO SERVICOS
&F**9384** / Fórmula auxiliar: ISENÇÃO IRRF PL 1087/2025 SERVICOS

####

| **9140 - IRRF AUTONOMO TRANSPORTADOR** | |
| --- | --- |
| **Fórmula** | IF((QueFuncionario.VINCULO = 90) AND ((queFuncionario.CODOCORRFGTS = '15') OR (queFuncionario.CODOCORRFGTS = '25')), IF((MemSetVar('varIRRFTransporte', (((&F4105 \* FTF(2, 1, &F4105, &DataPagamento, queFuncionario.TIPTAB) / 100) - FTF(2, 2, &F4105, &DataPagamento, queFuncionario.TIPTAB)) - &F4106) - &F9385) < queEventos.VLREVENTO), 0, MemGetVar('varIRRFTransporte')), 0) |

**DE / PARA:**

&F**4105** / Fórmula auxiliar: RECOMPOSICAO BASE IRRF TRANSPORTE
&F**4106** / Fórmula auxiliar: RECOMPOSICAO IRRF RETIDO TRANSPORTE
&F**9385** / Fórmula auxiliar: ISENÇÃO IRRF PL 1087/2025 TRANSPORTE

####

| **9180 - IRRF INTERMITENTE** | |
| --- | --- |
| **Fórmula** | IF((QueFuncionario.CODCATEGESOCIAL = 111), IF((MemSetVar('varIRRFintermitente', (((&F5160 \* FTF(2, 1, &F5160, &DataPagamento, queFuncionario.TIPTAB) / 100) - FTF(2, 2, &F5160, &DataPagamento, queFuncionario.TIPTAB)) - &F5170) - &F9386) < queEventos.VLREVENTO), 0, MemGetVar('varIRRFintermitente')), 0) |

**DE / PARA:**

&F**5160** / Fórmula auxiliar: RECOMPOSICAO BASE IRRF INTERMITENTE
&F**5170** / Fórmula auxiliar: RECOMPOSICAO IRRF RETIDO INTERMITENTE
&F**9386** / Fórmula auxiliar: ISENÇÃO IRRF PL 1087/2025 INTERMITENTE

####

| **9200 - IRRF 13° INTERMITENTE** | |
| --- | --- |
| **Fórmula** | IF((QueFuncionario.CODCATEGESOCIAL = 111), IF((MemSetVar('varIRRFintermitente13', (((&F5220 \* FTF(2, 1, &F5220, &DataPagamento, queFuncionario.TIPTAB) / 100) - FTF(2, 2, &F5220, &DataPagamento, queFuncionario.TIPTAB)) - &F5230) - &F9387) < queEventos.VLREVENTO), 0, MemGetVar('varIRRFintermitente13')), 0) |

**DE / PARA:**

&F**5220** / Fórmula auxiliar: RECOMPOSICAO BASE IRRF 13° INTERMITENTE
&F**5230** / Fórmula auxiliar: RECOMPOSICAO IRRF 13º RETIDO INTERMITENTE
&F**9387** / Fórmula auxiliar: ISENÇÃO IRRF PL 1087/2025 S/ 13º INTERMITENTE

####

| **9150 - IRRF - PRO LABORE** | |
| --- | --- |
| **Fórmula** | IF(QueFuncionario.VINCULO = 80, IF(MemSetVar('varBaseIRprolab', &E1915 + &E510 + ABS(FBEDTPAG(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, &DataPagamento, '1915')) + ABS(FBEDTPAG(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, &DataPagamento, '999'))) > 0, IF(MemSetVar('varIRRFprolab', (MemGetVar('varBaseIRprolab') \* FTF(2, 1, MemGetVar('varBaseIRprolab'), &DataPagamento, QueFuncionario.TIPTAB) / 100) - FTF(2, 2, MemGetVar('varBaseIRprolab'), &DataPagamento, QueFuncionario.TIPTAB) + &E509 - ABS(FBEDTPAG(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, &DataPagamento, '9150')) - &F9388) < queEventos.VLREVENTO, 0, MemGetVar('varIRRFprolab')), 0), 0) |

**DE / PARA:**

&E**1915** / Evento: BASE IRRF PRO LABORE
&E**510** / Evento: BASE IRRF OUTRAS FONTES
'**1915'** / Evento: BASE IRRF PRO LABORE
'**999'** / Evento: DEPENDENTES - IRRF
&E**509** / Evento: IRRF RETIDO OUTRAS FONTES
'**9150'** / Evento: IRRF - PRO LABORE
&F**9388** / Fórmula auxiliar: ISENÇÃO IRRF PL 1087/2025 PRO LABORE

**(4)** Configure os **eventos** demonstrativos para associar às fórmulas de isenção:

**(1)** **Folha Normal**

| **Folha Normal** | |
| --- | --- |
| **Código** | 9381 |
| **Descrição** | ISENÇÃO IRRF PL 1087/2025 |
| **Regra de** | NORMAL, RESCISÃO, RESCISÃO COMPLEMENTAR, ADIANTAMENTO, DISSIDIO |
| **Tipo** | Demonstrativo |
| **É base?** | Não |
| **Compõe eSocial** | Não |
| **Integra Contabilidade** | Não |

**(1)** **Folha Férias**

| **Folha Férias** | |
| --- | --- |
| **Código** | 9382 |
| **Descrição** | ISENÇÃO IRRF PL 1087/2025 FÉRIAS |
| **Regra de** | FÉRIAS |
| **Tipo** | Demonstrativo |
| **É base?** | Não |
| **Compõe eSocial** | Não |
| **Integra Contabilidade** | Não |

**(1)** **Folha Décimo Terceiro**

| **Folha Décimo Terceiro** | |
| --- | --- |
| **Código** | 9383 |
| **Descrição** | ISENÇÃO IRRF PL 1087/2025 13º |
| **Regra de** | NORMAL, RESCISÃO, RESCISÃO COMPLEMENTAR, ADIANTAMENTO, DISSIDIO |
| **Tipo** | Demonstrativo |
| **É base?** | Não |
| **Compõe eSocial** | Não |
| **Integra Contabilidade** | Não |

**(1)** **Folhas Suplementares**

**(2)** **Eventos** **Autônomos**

| **AUTONOMO SERVIÇOS** | |
| --- | --- |
| **Código** | 9384 |
| **Descrição** | ISENÇÃO IRRF PL 1087/2025 SERVICOS |
| **Regra de** | NORMAL, RESCISÃO |
| **Tipo** | Demonstrativo |
| **É base?** | Não |
| **Compõe eSocial** | Não |
| **Integra Contabilidade** | Não |

####

| **AUTONOMO TRANSPORTE** | |
| --- | --- |
| **Código** | 9385 |
| **Descrição** | ISENÇÃO IRRF PL 1087/2025 TRANSPORTE |
| **Regra de** | NORMAL, RESCISÃO |
| **Tipo** | Demonstrativo |
| **É base?** | Não |
| **Compõe eSocial** | Não |
| **Integra Contabilidade** | Não |

**(2)** **Eventos Intermitente**

| **INTERMITENTE NORMAL** | |
| --- | --- |
| **Código** | 9386 |
| **Descrição** | ISENÇÃO IRRF PL 1087/2025 INTERMITENTE |
| **Regra de** | NORMAL, RESCISÃO, INTERMITENTE |
| **Tipo** | Demonstrativo |
| **É base?** | Não |
| **Compõe eSocial** | Não |
| **Integra Contabilidade** | Não |

####

| **INTERMITENTE 13º** | |
| --- | --- |
| **Código** | 9387 |
| **Descrição** | ISENÇÃO IRRF PL 1087/2025 S/ 13º INTERMITENTE |
| **Regra de** | NORMAL, RESCISÃO, INTERMITENTE |
| **Tipo** | Demonstrativo |
| **É base?** | Não |
| **Compõe eSocial** | Não |
| **Integra Contabilidade** | Não |

**(1)** **Folha Pró Labore**

| **Folha Pró Labore** | |
| --- | --- |
| **Código** | 9381 |
| **Descrição** | ISENÇÃO IRRF PL 1087/2025 |
| **Regra de** | NORMAL |
| **Tipo** | Demonstrativo |
| **É base?** | Não |
| **Compõe eSocial** | Não |
| **Integra Contabilidade** | Não |
