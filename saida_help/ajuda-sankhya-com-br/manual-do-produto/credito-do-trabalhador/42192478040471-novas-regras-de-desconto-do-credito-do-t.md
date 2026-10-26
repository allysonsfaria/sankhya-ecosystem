---
id: "42192478040471"
titulo: "Novas Regras de Desconto do Crédito do Trabalhador em Caso de Rescisão Contratual (MGE Folha)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42192478040471-Novas-Regras-de-Desconto-do-Cr%C3%A9dito-do-Trabalhador-em-Caso-de-Rescis%C3%A3o-Contratual-MGE-Folha"
trilha: "Manual do Produto > Pessoas+ > Crédito do Trabalhador"
atualizado_em: "2026-09-02T14:01:37Z"
rotulos: ["Crédito do Trabalhador: Novas Regras para Desconto em Rescisões Contratuais (Portaria MTE nº 1.115/2026)", "Novas Regras de Desconto do Crédito do Trabalhador em Caso de Rescisão Contratual (MGE Folha)", "Cálculo Individual > Rescisão", "30309 - Pessoal/G", "Importação Crédito do Trabalhador"]
---

# Novas Regras de Desconto do Crédito do Trabalhador em Caso de Rescisão Contratual (MGE Folha)

**Módulo:** Pessoal+ **|** MGEFolha (30309 - Pessoal/G)
**Versão mínima:** Pessoal+ 5.113 **|** MGE - Controle Pessoal 4.67.0.15 **|** Sankhya OM 4.35826
**Caminhos de acesso:**

- Pessoal+> Rotinas Folha > Importação Crédito do Trabalhador
- MGEFolha > Arquivo > Fórmulas
- MGEFolha > Arquivo > Eventos
- MGEFolha > Arquivo > Bases de Cálculo
- MGEFolha > Cálculo Individual > Rescisão

---

### Sumário

[Descrição e Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/42192478040471-Novas-Regras-de-Desconto-do-Cr%C3%A9dito-do-Trabalhador-em-Caso-de-Rescis%C3%A3o-Contratual-MGE-Folha#h_01KYM6ABTRA97JFG373Y42C4RQ)

[1. Descrição da Funcionalidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/42192478040471-Novas-Regras-de-Desconto-do-Cr%C3%A9dito-do-Trabalhador-em-Caso-de-Rescis%C3%A3o-Contratual-MGE-Folha#h_01KYM6ABTRGMPMDEMB30C7TQF2)
[2. Pré-requisitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/42192478040471-Novas-Regras-de-Desconto-do-Cr%C3%A9dito-do-Trabalhador-em-Caso-de-Rescis%C3%A3o-Contratual-MGE-Folha#h_01KYM6ABTR8EYJ563WC69ZM6HE)
[3. Jornada de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/42192478040471-Novas-Regras-de-Desconto-do-Cr%C3%A9dito-do-Trabalhador-em-Caso-de-Rescis%C3%A3o-Contratual-MGE-Folha#h_01KYM6ABTR1CXXDNJBVK614AVA)

[3.1 Configurar Fómulas, Eventos e Base da Margem do Crédito do Trabalhador no MGEFolha](https://ajuda.sankhya.com.br/hc/pt-br/articles/42192478040471-Novas-Regras-de-Desconto-do-Cr%C3%A9dito-do-Trabalhador-em-Caso-de-Rescis%C3%A3o-Contratual-MGE-Folha#h_01KYME20H2JJQN54BXG5ZXEP5Y)
[3.2 Importar os dados do contrato no Pessoal+](https://ajuda.sankhya.com.br/hc/pt-br/articles/42192478040471-Novas-Regras-de-Desconto-do-Cr%C3%A9dito-do-Trabalhador-em-Caso-de-Rescis%C3%A3o-Contratual-MGE-Folha#h_01KYM6ABTRMA3B9G730KH6M41S)
[3.3 Calcular a rescisão no MGEFolha](https://ajuda.sankhya.com.br/hc/pt-br/articles/42192478040471-Novas-Regras-de-Desconto-do-Cr%C3%A9dito-do-Trabalhador-em-Caso-de-Rescis%C3%A3o-Contratual-MGE-Folha#h_01KYM6ABTR6ZRMQJ37K193J1A6)
[3.4 Emitir o TRCT no MGEFolha](https://ajuda.sankhya.com.br/hc/pt-br/articles/42192478040471-Novas-Regras-de-Desconto-do-Cr%C3%A9dito-do-Trabalhador-em-Caso-de-Rescis%C3%A3o-Contratual-MGE-Folha#h_01KYM6ABTRD1XYKSEZRARKTZCY)

[4. Pontos de Atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/42192478040471-Novas-Regras-de-Desconto-do-Cr%C3%A9dito-do-Trabalhador-em-Caso-de-Rescis%C3%A3o-Contratual-MGE-Folha#h_01KYM6ABTREXN2XY5FNJC9DF66)

[Perguntas Frequentes (FAQ)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42192478040471-Novas-Regras-de-Desconto-do-Cr%C3%A9dito-do-Trabalhador-em-Caso-de-Rescis%C3%A3o-Contratual-MGE-Folha#h_01KYM6ABTS0D6BNWBV2RW0636K)

---

## Descrição e Usabilidade

A [**Portaria MTE nº 1.115/2026**](https://www.in.gov.br/web/dou/-/portaria-mte-n-1.115-de-25-de-junho-de-2026-714711070) alterou as regras de desconto do Crédito do Trabalhador (eConsignado) nas rescisões contratuais.

Para atender às novas exigências legais, o **MGEFolha** disponibiliza uma rotina de importação automática dos dados do contrato diretamente da **Dataprev**, permitindo que o cálculo da rescisão utilize as informações mais recentes do empréstimo consignado.

As novas regras são aplicadas às rescisões com data de desligamento a partir de **23/07/2026**.

📚 Acesse o [**Manual do Crédito do Trabalhador**](https://www.gov.br/trabalho-e-emprego/pt-br/assuntos/credito-do-trabalhador/empregador/manual-operacional-do-empregador) e confira todo o fluxo operacional para desligamento do trabalhador (item 5.7).

### 1. Descrição da Funcionalidade

Para clientes que utilizam **MGEFolha**, o processamento da rescisão passa a envolver dois sistemas:

| Etapa | Sistema |
| --- | --- |
| Configuração de Fórmulas, Eventos e Base da Margem do Crédito do Trabalhador | **MGEFolha** |
| Importação dos dados do contrato de Crédito do Trabalhador junto à Dataprev | **Pessoal+** |
| Armazenamento das informações retornadas pela API | **Pessoal+** |
| Cálculo da rescisão utilizando os dados importados | **MGEFolha** |
| Geração do TRCT com as informações do Crédito do Trabalhador | **MGEFolha** |

| **⚠️** **Atenção**   **Data de corte da legislação**  Todo o processamento do Crédito do Trabalhador na rescisão é definido pela **data de desligamento do colaborador**.   - Desligamentos até **22/07/2026: regras anteriores do Crédito do Trabalhador**; - Desligamentos a partir de **23/07/2026: novas regras da Portaria MTE nº 1.115/2026**.   Essa data define:   - qual serviço da API será utilizado; - quais informações serão importadas; - quais verbas compõem a margem consignável; - como será calculado o desconto da rescisão; - quais informações serão demonstradas no TRCT. |
| --- |

####

### 2. Pré-requisitos

Antes de iniciar a rescisão, verifique se:

- a empresa possui integração configurada com a API da Dataprev;
- o certificado digital está válido;
- o colaborador possui contrato ativo do Crédito do Trabalhador  registrado junto ao governo;
- o cálculo da rescisão ainda não foi realizado.

### 3. Jornada de Uso

#### 3.1 Configurar Fórmulas, Eventos e Base da Margem do Crédito do Trabalhador no MGEFolha

Antes de importar os dados do Crédito do Trabalhador e realizar o cálculo da rescisão, é necessário configurar Fórmulas, Eventos e base utilizados para o cálculo da margem consignável.

Para isso:

1. Acesse as telas de cadastros de Eventos, Fórmulas e Bases de Cálculo no MGEFolha;

##### 🔹Avançado > Fórmulas

1. Atualize as fórmulas abaixo considerando a seguinte legenda:

   **MMMM** = Código do evento crédito do trabalhador informado no Lançamento de Movimento.
   **BBBB** = Código do evento de Base da Margem Crédito Trabalhador

   - **DESCONTO CREDITO TRABALHADOR**

   | (MemSetVar('MargemCredAcum', IF(&EMMMM = 0, 0, MemGetVar('MargemCredAcum'))) \* 0) + IF(QUEMOVIMENTO.VLRMOV > 0, IF(MemSetVar('MargemCred', (&EBBBB \* IF(MemSetVar('Garantia',IF((&TIPFOL = 'R') AND (&DTDEMISSAO > CTOD('22/07/2026')), ABS(FBM(QueFuncionario.CODEMP, QueFuncionario.CODFUNC,&REFERE, 'R', 'MMMM', 'I'))/100,(35/100))) > 0, MemGetVar('Garantia'), 0)))> 0, IF((MemGetVar('MargemCred') - MemGetVar('MargemCredAcum') < MemSetVar('ValorDesconto',IF(&TIPFOL = 'R', IF(MemSetVar('MargemGarantia',&EBBBB \* IF(&DTDEMISSAO < CTOD('23/07/2026'), MemGetVar('Garantia'), QUEMOVIMENTO.INDICE/100)) < QUEMOVIMENTO.VLRMOV, MemGetVar('MargemGarantia'),QUEMOVIMENTO.VLRMOV), QUEMOVIMENTO.VLRMOV))), MemGetVar('MargemCred') - MemGetVar('MargemCredAcum'), MemGetVar('ValorDesconto') + (MemIncVar('MargemCredAcum', MemGetVar('ValorDesconto')) \* 0)), 0), 0) |
   | --- |

   - **PARCELA NÃO DESCONTO CREDITO TRABALHADOR**

   | IF((ABS(FBE(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, &Refere, 'R', '**MMMM**')) = 0) AND (MemSetVar('Credtrab', ABS(FBM(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, &REFERE, 'M', '**MMMM**', 'V') + FBM(QueFuncionario.CODEMP, QueFuncionario.CODFUNC,&REFERE, 'R', '**MMMM**', 'V'))) > 0), IF(MemSetVar('MargemCred', &E**BBBB** \* IF(&TIPFOL = 'R', ABS(FBM(QueFuncionario.CODEMP, QueFuncionario.CODFUNC,&REFERE, 'R', '**MMMM**', 'I'))/100,(35/100))) > 0, IF(MemGetVar('MargemCred') < MemGetVar('Credtrab'), MemGetVar('Credtrab') - MemGetVar('MargemCred'), 0), MemGetVar('Credtrab')), 0) |
   | --- |

##### 🔹Arquivos > Eventos

1. Cadastre os eventos abaixo:

   | Código do Evento | Descrição do Evento | Natureza da Rubrica | Característica | Cod Incidencia INSS (CODINCCP) | Cod Incidencia IRRF (CODINCIRRF) |
   | --- | --- | --- | --- | --- | --- |
   | 1 | Salário Base | 1000 | SALARIOBASE | 11 | 11 |
   | 2 | Salário Horas - Fixo | 1000 | SALARIOHORASFIXO | 11 | 11 |
   | 9 | Salário Hora Variável | 1000 | SALARIOHORAVARIAVEL | 11 | 11 |
   | 11 | Periculosidade | 1203 | PERICULOSIDADE | 11 | 11 |
   | 13 | Insalubridade | 1202 | INSALUBRIDADE | 11 | 11 |
   | 19 | Periculosidade em Dias | 1203 | PERICULOSIDADEEMDIAS | 11 | 11 |
   | 26 | DSR Salário Horas | 1012 | DSRSALARIOHORAS | 11 | 11 |
   | 28 | Intervalo Intrajornada | 1006 | INTERVALOINTRAJORNADA | 11 | 11 |
   | 29 | Desconto DSR Ponto | 9210 | DESCONTODSRPONTO | 11 | 11 |
   | 50 | Hora Extra 50% | 1003 | HORAEXTRA50 | 11 | 11 |
   | 51 | Hora Extra 60% | 1003 | HORAEXTRA60 | 11 | 11 |
   | 52 | Hora Extra 80% | 1003 | HORAEXTRA80 | 11 | 11 |
   | 53 | Hora Extra 100% | 1003 | HORAEXTRA100 | 11 | 11 |
   | 54 | Hora Extra 1200% | 1003 | HORAEXTRA200 | 11 | 11 |
   | 55 | Hora Extra Noturna 50% | 1003 | HORAEXTRANOT50 | 11 | 11 |
   | 56 | Hora Extra Noturna 60% | 1003 | HORAEXTRANOT60 | 11 | 11 |
   | 57 | Hora Extra Noturna 80% | 1003 | HORAEXTRANOT80 | 11 | 11 |
   | 58 | Hora Extra Noturna 100% | 1003 | HORAEXTRANOT100 | 11 | 11 |
   | 59 | Hora Extra Noturna 200% | 1003 | HORAEXTRANOT200 | 11 | 11 |
   | 60 | Horas de Sobreaviso | 1011 | HORASDESOBREAVISO | 11 | 11 |
   | 61 | Adicional Noturno Urbano | 1205 | ADICNOTURNOURB | 11 | 11 |
   | 62 | Adicional Noturno Rural Lavoura | 1205 | ADICNOTURNORURLAV | 11 | 11 |
   | 63 | Adicional Noturno Rural Pecuária | 1004 | ADICNOTURNORURPEC | 11 | 11 |
   | 64 | Hora Extra 50% Banco de Horas | 1004 | HORAEXTRA50BANCODEHORAS | 11 | 11 |
   | 65 | Hora Extra 60% Banco de Horas | 1004 | HORAEXTRA60BANCODEHORAS | 11 | 11 |
   | 66 | Hora Extra 80% Banco de Horas | 1004 | HORAEXTRA80BANCODEHORAS | 11 | 11 |
   | 67 | Hora Extra 100% Banco de Horas | 1004 | HORAEXTRA100BANCODEHORAS | 11 | 11 |
   | 68 | Hora Extra 200% Banco de Horas | 1004 | HORAEXTRA200BANCODEHORAS | 11 | 11 |
   | 72 | DSR Intrajornada | 1006 | DSRINTRAJORNADA | 11 | 11 |
   | 73 | Intervalo Interjornada | 1006 | INTERVALOINTERJORNADA | 11 | 11 |
   | 74 | DSR Interjornada | 1006 | DSRINTERJORNADA | 11 | 11 |
   | 81 | DSR Horas Extras 50% Banco de Horas | 1012 | DSRHORASEXTRAS50BCOHORAS | 11 | 11 |
   | 82 | DSR Horas Extras 60% Banco de Horas | 1012 | DSRHORASEXTRAS60BCOHORAS | 11 | 11 |
   | 83 | DSR Horas Extras 80% Banco de Horas | 1012 | DSRHORASEXTRAS80BCOHORAS | 11 | 11 |
   | 84 | DSR Horas Extras 100% Banco de Horas | 1012 | DSRHORASEXTRAS100BCOHORAS | 11 | 11 |
   | 85 | DSR Horas Extras 200% Banco de Horas | 1012 | DSRHORASEXTRAS200BCOHORAS | 11 | 11 |
   | 86 | DSR - Horas de Sobreaviso | 1012 | DSRHORASDESOBREAVISO | 11 | 11 |
   | 87 | DSR - Adicional Noturno Urbano | 1012 | DSRADICNOTURNOURB | 11 | 11 |
   | 88 | DSR - Adicional Noturno Rural Lavoura | 1012 | DSRADICNOTURNORURLAV | 11 | 11 |
   | 89 | DSR - Adicional Noturno Rural Pecuária | 1012 | DSRADICNOTURNORURPEC | 11 | 11 |
   | 90 | DSR - Horas Extras 50% | 1012 | DSRHORASEXTRAS50 | 11 | 11 |
   | 91 | DSR - Horas Extras 60% | 1012 | DSRHORASEXTRAS60 | 11 | 11 |
   | 92 | DSR - Horas Extras 80% | 1012 | DSRHORASEXTRAS80 | 11 | 11 |
   | 93 | DSR - Horas Extras 100% | 1012 | DSRHORASEXTRAS100 | 11 | 11 |
   | 94 | DSR - Horas Extras 200% | 1012 | DSRHORASEXTRAS200 | 11 | 11 |
   | 95 | DSR - Horas Extras Noturna 50% | 1012 | DSRHORASEXTRASNOT50 | 11 | 11 |
   | 96 | DSR - Horas Extras Noturna 60% | 1012 | DSRHORASEXTRASNOT60 | 11 | 11 |
   | 97 | DSR - Horas Extras Noturna 80% | 1012 | DSRHORASEXTRASNOT80 | 11 | 11 |
   | 98 | DSR - Horas Extras Noturna 100% | 1012 | DSRHORASEXTRASNOT100 | 11 | 11 |
   | 99 | DSR - Horas Extras Noturna 200% | 1012 | DSRHORASEXTRASNOT200 | 11 | 11 |
   | 102 | Faltas | 9207 | FALTAS | 11 | 11 |
   | 103 | Atrasos/Saídas Antecipadas | 9209 | ATRASOSSAIDASANTECIPADAS | 11 | 11 |
   | 104 | Suspensão Disciplinar | 9209 | SUSPENSAODISCIPLINAR | 11 | 11 |
   | 105 | Restituição Faltas Indevidas | 9207 | RESTITUICAOFALTASINDEV | 11 | 11 |
   | 106 | Restituição Atrasos/Saídas Indevidas | 1099 | RESTITATRASOSSAIDASINDEV | 11 | 11 |
   | 107 | Desconto de DSR | 9210 | DESCONTODEDSR | 11 | 11 |
   | 200 | Saldo de Salário Rescisão | 6000 | SALDODESALARIORESCISAO | 11 | 11 |
   | 201 | Aviso Prévio Indenizado | 6003 | AVISOPREVIOINDENIZADO | 0 | 74 |
   | 202 | 13º Salário Proporcional Rescisão | 6002 | 13SALPROPRESCISAO | 12 | 12 |
   | 203 | 13º Salário Aviso Prévio Indenizado | 6001 | 13SALARIOAPI | 12 | 74 |
   | 204 | Férias Vencidas Indenizadas na Rescisão | 6007 | FERIASVENCINDENRESC | 0 | 74 |
   | 205 | Férias Proporcionais - Rescisões | 6006 | FERIASPROPRESCISOES | 0 | 74 |
   | 206 | 1/3 de Férias Proporcionais | 6006 | 13FERIASPROPORCIONAIS | 0 | 74 |
   | 207 | 1/3 de Férias Vencidas | 6007 | 13FERIASVENCIDAS | 0 | 74 |
   | 208 | Médias de Aviso Prévio Indenizado | 6003 | MEDIASAVISOPREVIOIND | 0 | 74 |
   | 209 | Médias 13º Salário Proporcional Rescisão | 6002 | MEDIAS13PROPRESC | 12 | 12 |
   | 210 | Médias de Férias Proporcionais - Rescisão | 6006 | MEDIASFERIASPROPRESCISAO | 0 | 74 |
   | 211 | Médias das Férias Vencidas Indenizadas - Rescisão | 6007 | MEDIASFERIASVENCINDRESC | 0 | 74 |
   | 212 | Médias 13º Salário Aviso Prévio Indenizado | 6001 | MEDIAS13SALARIOAPI | 12 | 74 |
   | 214 | Art. 480 Contrato Experiência | 6904 | ART480CONTRATOEXPERIENCIA | 0 | 9 |
   | 216 | Art. 480 Contrato Determinado | 6904 | ART480CONTRATODETERMINADO | 0 | 9 |
   | 217 | Aviso Prévio Descontado | 6901 | AVISOPREVIODESCONTADO | 0 | 9 |
   | 219 | Férias Dobradas - Rescisão | 6004 | FERIASDOBRADASRESCISAO | 0 | 74 |
   | 220 | 1/3 de Férias Dobradas - Rescisão | 6004 | 13FERIASDOBRADASRESCISAO | 0 | 74 |
   | 222 | Desconto Art. 130 sobre Férias Vencidas | 6007 | DESART130FERVENCIDAS | 0 | 74 |
   | 224 | Médias Art. 480 Contrato Experiência | 6904 | MEDIASART480CONTRATOEXP | 0 | 9 |
   | 225 | Férias Proporcionais Indenizadas (API) | 6006 | FERIASPROPINDENIZADASAPI | 0 | 74 |
   | 226 | Médias de Férias Proporcionais Indenizadas (API) | 6006 | MEDIASFERIASPROPINDENAPI | 0 | 74 |
   | 227 | Médias de Férias Dobradas - Rescisão | 6004 | MEDIAFERIASDOBRADASRESC | 0 | 74 |
   | 228 | Desconto Art. 130 sobre Férias Proporcionais | 6006 | DESART130FERPROPORCIONAIS | 0 | 74 |
   | 231 | Sábado Compensado | 1099 | SABADOCOMPENSADO | 11 | 11 |
   | 232 | DSR Projetado Aviso Prévio Indenizado | 1012 | DSRPROJAVISOPREVIOIND | 0 | 74 |
   | 236 | Desconto de Licença sem Remuneração - Férias Proporcionais | 6006 | DESCLICSEMREMFERPROPORC | 0 | 74 |
   | 237 | Desconto de Licença sem Remuneração - Férias Vencidas | 6007 | DESCLICSEMREMFERVENCIDA | 0 | 74 |
   | 239 | Médias Art. 480 Contrato Determinado | 6904 | MEDIAART480CONTRATODETERM | 0 | 9 |
   | 240 | Aviso Prévio - Lei nº 12.506 | 6003 | AVISOPREVIOLEI12506 | 0 | 74 |
   | 241 | 13º Salário Lei nº 12.506 | 6001 | 13SALARIOLEI12506 | 12 | 74 |
   | 242 | Férias Proporcionais - Lei nº 12.506 | 6003 | FERIASPROPLEI12506 | 0 | 74 |
   | 243 | DSR Rescisão | 1012 | DSRRESCISAO | 11 | 11 |
   | 244 | Médias de Aviso Prévio - Lei nº 12.506 | 6003 | MEDIAAVISOPREVIOLEI12506 | 0 | 74 |
   | 245 | Médias de Férias Proporcionais - Lei nº 12.506 | 6006 | MEDIAFERIASPROPLEI12506 | 0 | 74 |
   | 246 | Médias de 13º Salário - Lei nº 12.506 | 6001 | MEDIA13SALARIOLEI12506 | 12 | 74 |
   | 247 | 1/3 de Férias (API) | 6006 | 13FERIASAPI | 0 | 74 |
   | 251 | Descumprimento de Aviso Prévio pelo Empregador | 6003 | DESCUMPAVIEMPREGADOR | 0 | 74 |
   | 252 | Descumprimento de Aviso Prévio pelo Empregado | 6901 | DESCUMPAVIEMPREGADO | 0 | 9 |
   | 257 | Férias Proporcionais - Contrato Intermitente | 6006 | FERIASPROPINTERMITENTE | 11 | 74 |
   | 258 | Médias das Férias Proporcionais - Contrato Intermitente | 6006 | MEDIASFERIASPROPINTERMIT | 11 | 74 |
   | 259 | 1/3 de Férias Proporcionais - Contrato Intermitente | 6006 | 13FERIASPROPINTERMITENTE | 11 | 74 |
   | 262 | Aviso Indenizado - Contrato Intermitente | 6003 | AVISOINDENIZADOINTERMIT | 0 | 74 |
   | 263 | Férias (API) - Contrato Intermitente | 6003 | FERIASAPIINTERMITENTE | 0 | 74 |
   | 265 | 1/3 de Férias (API) - Contrato Intermitente | 6003 | 13FERIASAPIINTERMITENTE | 0 | 74 |
   | 540 | Licença Maternidade | 4050 | LICENCAGESTANTE | 21 | 11 |
   | 541 | Médias Licença Maternidade | 4050 | MEDIASLICGESTANTE | 21 | 11 |
   | 546 | Licença Remunerada Afastamento | 1050 | LICENCAREMUNERADAAFAST | 11 | 11 |
   | 547 | Licença Paternidade | 1050 | LICENCAPATERNIDADE | 11 | 11 |
   | 549 | Licença Paternidade Cidadã | 1050 | LICENCAPATERNIDADECIDADA | 11 | 11 |
   | 552 | Atestado Médico em Dias | 1050 | ATESTADOMEDICODIAS | 11 | 11 |
   | 558 | Licença Óbito | 1050 | LICENCAOBITO | 11 | 11 |
   | 560 | Licença Maternidade Cidadã | 4050 | LICENCAGESTANTECIDADA | 21 | 11 |
   | 561 | Médias Licença Maternidade Cidadã | 4050 | MEDIALICENCAGESTCIDADA | 21 | 11 |
   | 650 | Adiantamento Quinzenal - Percentual | 5501 | ADIANTQUINZENALPERCENTUAL | 0 | 11 |
   | 652 | Adiantamento Quinzenal - Valor | 5501 | ADIANTQUINZENALVALOR | 0 | 11 |
   | 2003 | Férias Proporcionais - Contrato Verde e Amarelo | 6006 | FERIASPROPCONTVERDEEAMAR | 11 | 11 |
   | 2004 | Médias de Férias Proporcionais - Contrato Verde e Amarelo | 6006 | MEDIASFERIASPROPVERDEAMAR | 11 | 11 |
   | 2005 | 1/3 Férias Proporcionais - Contrato Verde e Amarelo | 6006 | 13FERPROPCONTVERDAMAR | 11 | 11 |
   | 4150 | Férias na Competência | 1016 | FERIASNACOMPETENCIA | 11 | 9 |
   | 4160 | 1/3 de Férias na Competência | 1017 | 13DEFERIASNACOMPETENCIA | 11 | 9 |
   | 4190 | Médias de Férias na Competência | 1016 | MEDIAFERIASNACOMPETENCIA | 11 | 9 |
   | 4200 | Diferença de Férias | 1016 | DIFERENCADEFERIAS | 11 | 11 |
   | 4230 | Diferença de Médias de Férias | 1016 | DIFERENCADEMEDIADEFERIAS | 11 | 11 |
   | 4410 | Férias | 1015 | FERIAS | 0 | 13 |
   | 4420 | 1/3 de Férias | 1015 | 13DEFERIAS | 0 | 13 |
   | 4430 | Médias de Férias | 1015 | MEDIADEFERIAS | 0 | 13 |
   | 9010 | INSS | 9201 | INSS | 31 | 41 |
   | 9030 | INSS - 13º Salário | 9201 | INSS13SALARIO | 32 | 42 |
   | 9040 | IRRF | 9203 | IRRF | 0 | 31 |
   | 9050 | IRRF - Férias | 9203 | IRRFFERIAS | 0 | 33 |
   | 9060 | IRRF - 13º Salário | 9203 | IRRF13SALARIO | 0 | 32 |
   | 9120 | INSS - Pró Labore | 9201 | INSSPROLABORE | 31 | 41 |
   | 9150 | IRRF - Pró Labore | 9203 | IRRFPROLABORE | 0 | 31 |
   | 9160 | INSS - Intermitente | 9201 | INSSINTERMITENTE | 31 | 41 |
   | 9180 | IRRF - Intermitente | 9203 | IRRFINTERMITENTE | 0 | 31 |
   | 9341 | INSS Descontado nas Férias | 9201 | INSSDESCONTADONASFERIAS | 31 | 9 |

##### 🔹Arquivos > Bases de Cálculo

1. Localize ou cadastre a base com a identificação **34 - Base Margem Cred. Trabalhador** (BASEMARGEMCREDTRAB);
2. Inclua manualmente **todos os eventos cadastrados acima** para compor essa base.

   | **⚠️** **Atenção**   A presença dos eventos na base não significa que seus valores serão sempre considerados no cálculo. O sistema verifica automaticamente a data de desligamento do colaborador para definir a regra aplicável:  - **Até 22/07/2026:** os eventos permanecem vinculados à base, porém os valores incluídos pelas novas regras **não compõem a margem consignável**; - **A partir de 23/07/2026:** os eventos **passam a compor automaticamente a base de cálculo da margem consignável**, conforme a Portaria MTE nº 1.115/2026. |
   | --- |

#### 3.2 Importar os dados do contrato no Pessoal+

| **⚠️** **Atenção**   **A importação dos dados deve ser realizada antes do cálculo da rescisão no MGEFolha.** Caso contrário, o cálculo utilizará as informações já existentes no sistema. |
| --- |

1. Acesse a tela **Importação Crédito do Trabalhador** (Pessoal+ >  Rotinas Folha) no **Pessoal+**;
2. Informe:
   - Empresa;
   - Referência;
   - Funcionário.
3. Clique em **Importar**.

   O sistema realiza automaticamente a consulta à API da Dataprev utilizando o CPF do colaborador. Ao término da importação será apresentada a mensagem:

   **"Importação concluída.**
   Os dados do Crédito do Trabalhador foram importados com sucesso. Acesse o **MGEFolha** para prosseguir com o cálculo da rescisão."

   | **⚠️** **Atenção**   A rescisão não pode ser calculada enquanto essas informações não forem disponibilizadas pela Dataprev, conforme as [Orientações adicionais sobre a funcionalidade de garantias no crédito do trabalhador](https://www.gov.br/trabalho-e-emprego/pt-br/assuntos/credito-do-trabalhador/empregador/comunicado-aos-empregadores/orientacoes-adicionais-sobre-a-funcionalidade-de-garantias-no-credito-do-trabalhador.pdf). |
   | --- |

#### 3.3 Calcular a rescisão no MGEFolha

Após concluir a importação:

1. Acesse o **MGEFolha** para calcular a rescisão;
2. Execute normalmente o **Cálculo Individual > Rescisão**.

   O sistema utilizará automaticamente os dados importados no Pessoal+ para realizar o cálculo do desconto do Crédito do Trabalhador.

   Para desligamentos ocorridos a partir de **23/07/2026**, passam a integrar automaticamente a base da margem consignável as verbas rescisórias previstas na Portaria MTE nº 1.115/2026, quando existentes no cálculo.

   Entre elas:

   - 6003 - Aviso prévio indenizado;
   - 6004 - Férias em dobro indenizadas na rescisão;
   - 6006 - Férias proporcionais;
   - 6007 - Férias vencidas.

     | **⚠️** **Atenção**   Essas verbas são consideradas exclusivamente nas rescisões. |
     | --- |

   Para determinar o desconto, o sistema sempre aplica o menor valor entre:

   - o limite calculado pela garantia rescisória;
   - o saldo devedor atualizado do contrato.

   Caso o limite calculado seja inferior ao saldo devedor, será realizado desconto parcial e o saldo remanescente permanecerá sob responsabilidade do trabalhador perante a instituição financeira.

   | Exemplo | Situação | Resultado |
   | --- | --- | --- |
   | 1 | - Base: R$ 10.000,00 - Garantia: 10% - Saldo devedor: R$ 1.000,00 | Limite da garantia = R$ 1.000,00.  Como é igual ao saldo devedor, o desconto será de **R$ 1.000,00**, quitando integralmente o contrato. |
   | 2 | - Base: R$ 10.000,00 - Garantia: 10% - Saldo devedor: R$ 500,00 | Limite da garantia = R$ 1.000,00.  Como o saldo devedor é menor, o desconto será de **R$ 500,00**, quitando integralmente o contrato. |
   | 3 | - Base: R$ 10.000,00 - Garantia: 10% - Saldo devedor: R$ 2.000,00 | Limite da garantia = R$ 1.000,00.  Como esse é o menor valor, o desconto será de **R$ 1.000,00** e permanecerá saldo devedor de **R$ 1.000,00** junto à instituição financeira. |

#### 3.4 Emitir o TRCT no MGEFolha

1. Após concluir o cálculo, gere normalmente o TRCT no MGEFolha.

   O relatório apresenta automaticamente:

   - instituição financeira;
   - número do contrato;
   - saldo devedor;
   - percentual de garantia;
   - valor descontado;
   - saldo não descontado.

   Além dessas informações, o documento exibirá uma mensagem explicativa conforme o resultado do cálculo:

   - desconto integral;
   - desconto parcial;
   - ausência de garantia rescisória.

   Quando houver mais de um contrato de empréstimo, cada contrato será apresentado individualmente.

### 4. Pontos de Atenção

- As regras anteriores permanecem válidas para desligamentos ocorridos até 22/07/2026.
- As novas regras aplicam-se apenas às rescisões com desligamento a partir de 23/07/2026.
- A importação dos dados do Crédito do Trabalhador é realizada exclusivamente no **Pessoal+**.
- O cálculo da rescisão e a emissão do TRCT são realizados no **MGEFolha**.
- A importação deve ser concluída antes da execução do cálculo da rescisão.
- As verbas rescisórias previstas na Portaria MTE nº 1.115/2026 passam a compor automaticamente a margem consignável.
- Essas verbas não alteram o cálculo da folha mensal.
- Caso o governo não retorne saldo devedor ou percentual de garantia, os valores serão considerados iguais a zero.
- Em caso de indisponibilidade da API, a importação não será realizada até que uma nova consulta seja efetuada.
- Caso novos dados sejam disponibilizados pela Dataprev, execute uma nova importação antes de recalcular a rescisão.

## Perguntas Frequentes (FAQ)

**1. Preciso consultar o Portal Emprega Brasil antes da rescisão?**

Não. O MGEFolha consulta automaticamente a API da Dataprev durante a importação.

**2. Posso importar apenas um colaborador?**

Sim. A rotina realiza a consulta individual utilizando o CPF do colaborador selecionado.

**3. O que acontece se não houver contrato ativo?**

O sistema informa que não foram encontrados contratos e nenhuma informação é importada.

**4. O que acontece se a API estiver indisponível?**

O sistema informa a falha de comunicação e permite uma nova tentativa posteriormente.

**5. Como o desconto é calculado?**

O sistema aplica sempre o menor valor entre o limite calculado pela garantia rescisória e o saldo devedor atualizado do contrato.

**6. As novas verbas rescisórias também entram na folha mensal?**

Não. Elas compõem a margem consignável apenas nas rescisões enquadradas na Portaria MTE nº 1.115/2026.
