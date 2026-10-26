---
id: "37827360294295"
titulo: "Como ajustar a incidência de IRRF dos eventos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37827360294295-Como-ajustar-a-incid%C3%AAncia-de-IRRF-dos-eventos"
trilha: "Manual do Produto > Pessoas+ > Encargos e Obrigações Legais > Regras de IRRF e Incidências"
atualizado_em: "2026-10-02T15:53:08Z"
rotulos: ["Configuração", "Impostos", "DIRF", "eSocial", "Folha de Pagamento", "IRRF", "Ajuste de Incidência de IRRF (CODINCIRRF)", "Evento S-5012", "Evento S-5002"]
---

# Como ajustar a incidência de IRRF dos eventos

O **Código de Incidência do IRRF (CODINCIRRF)** de determinadas verbas da folha de pagamento **foi ajustado** para **corrigir o enquadramento tributário dessas rubricas**.

Os ajustes realizados foram:

- a **maior parte das verbas** teve o CODINCIRRF alterado de **79 para 09**;
- a rubrica **MULTA FGTS** teve o CODINCIRRF alterado de **74 para 09**.

A lista completa das rubricas ajustadas está disponível ao final deste artigo.

**Importante**

- A incidência anteriormente utilizada **não gerou impacto financeiro** nem para o colaborador, nem para o empregador.
- Isso ocorreu porque as verbas estavam classificadas com **CODINCIRRF = 79 (Outras isenções)** e, por esse motivo, **não compunham a base de cálculo do IRRF**.

| **Por que esse ajuste foi necessário?** |
| --- |

O ajuste foi realizado porque algumas verbas estavam sendo tratadas como **rendimentos isentos de Imposto de Renda**, quando, na prática, são **verbas que apenas transitam pela folha**, sem natureza de rendimento.

Com a correção da classificação, garante-se que:

- o **Imposto de Renda seja apurado corretamente**;
- as informações enviadas ao **eSocial estejam corretas**;
- a **DIRF 2026** (substituída pelo eSocial) seja gerada **sem inconsistências**;
- o **Informe de Rendimentos do colaborador** apresente os valores de forma clara e correta.

| **O que significa cada código de incidência?** |
| --- |

- **CODINCIRRF = 79 — Outras isenções**

  Utilizado para **rendimentos isentos por lei** que não estão listados na **Tabela 21 do eSocial**, cuja natureza do pagamento deve ser explicitada no nome da rubrica.

  Essas informações:

  - compõem os totalizadores do **evento S-5002**;
  - são apresentadas no **Informe de Rendimentos**, com a descrição da rubrica que compôs as outras isenções.
- **CODINCIRRF = 09 — Verba transitada pela folha de pagamento de natureza diversa de rendimento ou retenção/isenção/dedução de IR.**

  Utilizado para verbas que **transitam pela folha de pagamento**, mas que **não possuem natureza de rendimento, retenção, isenção ou dedução de IR**.

  **Por exemplo:** desconto de convênio farmácia, consignações, adiantamentos e outras verbas sem natureza tributável.
- **CODINCIRRF = 74 — Indenização e rescisão de contrato, inclusive a título de PDV e acidentes de trabalho**

  Utilizado para identificar rubricas de **indenização e rescisão do contrato de trabalho**, incluindo:

  - rescisões contratuais;
  - PDV;
  - indenizações por acidente de trabalho.

| **O que muda na prática?** |
| --- |

Após o ajuste:

- As verbas transitórias **não serão exibidas mais como rendimento isento** no Informe de Rendimentos.
- Os valores enviados ao eSocial ficarão corretos nos eventos:

  - **S-5002** (IRRF do trabalhador);
  - **S-5012** (IRRF do empregador).
- O **Demonstrativo do Informe de Rendimentos** ficará mais claro, diferenciando o que é:

  - rendimentos tributáveis;
  - rendimentos isentos;
  - verbas sem natureza de rendimento.

| **O que o cliente precisa fazer?** |
| --- |

Para que o ajuste reflita corretamente nos **relatórios fiscais, eSocial e Informe de Rendimentos**, é necessário executar os passos abaixo.

**1. Atualizar as rubricas na tela Eventos** (Pessoal+ > Cadastros).

**2. Enviar o evento S-1010 (Tabela de Rubricas) pela Central do eSocial**

- Enviar o **S-1010 das rubricas listadas** neste artigo;
- Utilizar **nova data de início de validade**, **no mínimo a partir de 01/2025, já com o código CODINCIRRF ajustado**;

Consulte a documentação: [**Como enviar o evento S-1010 (Tabela de Rubricas) com nova validade no eSocial**](https://ajuda.sankhya.com.br/hc/pt-br/articles/37825585095447).

**2.** Reabrir, por meio do evento S-1298, todas as referências do ano de 2025 em que houve o envio de alguma das rubricas mencionadas ao eSocial.

**3.** Em seguida, bloquear as folhas de pagamento dessas competências e gerar o evento S-1210 (Pagamentos) de exclusão, realizando o respectivo envio ao eSocial.

**4.** Após a exclusão, liberar as folhas, gerar o evento S-1210 (Pagamentos) de inclusão e efetuar o envio.

**5.** Concluído esse processo, realizar o fechamento das competências com o envio do evento S-1299 (Fechamento).

**6.** Após o processamento desses eventos, o eSocial passará a considerar a nova incidência das rubricas, refletindo corretamente nos retornos S-5002 e no consolidado S-5012.

**7.** Por fim, após o envio dos eventos S-1010, repetir os passos 2 a 5 para todas as competências de 2025 em que tenham sido enviadas rubricas com a incidência anterior.

Após esses envios, o eSocial passará a considerar a **nova incidência** nos retornos:

- **S-5002** (IRRF do trabalhador);
- **S-5012** (consolidado do empregador).

Com isso, já será possível emitir os [**Demonstrativos do Informe de Rendimentos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/20941208310167).

[GIF animado: Imagem 1: Com isso, já será possível emitir os Demonstrativos do Informe de Rendimentos .](https://ajuda.sankhya.com.br/hc/article_attachments/37835114254743)

######

### Lista de rubricas ajustadas

Faça a busca pela **descrição do evento ou pela característica**, pois o código pode ser diferente na sua base.

| **Código** | **Descrição do Evento** | **Característica** | **CODINCIRRF ANTIGO** | **CODINCIRRF ATUAL** |
| --- | --- | --- | --- | --- |
| 5 | HONORARIOS TRANSPORTE | HONORARIOSTRANSPORTE | 79 | 9 |
| 16 | DESC. EXCEDENTE ADTO 13º SAL. | DESCADTODECTERMAIOR | 79 | 9 |
| 18 | ANTEC 13ºFERIAS LIC MATERNIDADE COMPET | ANTECIP13FERIASLICGE | 79 | 9 |
| 20 | DESC ANTEC 13 FERIAS LICGE COMP | DESCANTEC13FERIASLICGE | 79 | 9 |
| 301 | 1ª PARCELA DO 13° SALARIO | 1PARCELADO13SALARIO | 79 | 9 |
| 303 | MEDIAS 1ª PARCELA 13° SALARIO | MEDIAS1PARCELADO13SALARIO | 79 | 9 |
| 305 | DESC 1ª PARCELA DO 13° SALARIO | DESCONTO1PARC13SAL | 79 | 9 |
| 306 | DESC ANTECIPACAO 13° SALARIO | DESCANTECIP13SALARIO | 79 | 9 |
| 308 | 1ª PARC 13º LIC MATERNIDADE | 1PARC13SALLICGEST | 79 | 9 |
| 312 | ANTECI 13ºSAL FER LIC MATERNIDADE | ADIANT13SALFERIASLICGE | 79 | 9 |
| 313 | MEDIA 1ª PARC 13º LIC MATERNIDADE | MEDIAS1PARC13SALLICG | 79 | 9 |
| 315 | DESCONTO 1ª PARC 13º RESCISAO | DESCONTO1PARC13SALRESCISA | 79 | 9 |
| 316 | DESC1ªPARC 13ºBASE FGTS MENSAL | DESC1PARC13BASEFGTSMENSAL | 79 | 9 |
| 318 | 1ª PARC 13º ACID TRAB | 1PARC13SACIDTRAB | 79 | 9 |
| 319 | 2ª PARC 13° ACID TRAB | 2PARC13SACIDTRAB | 79 | 9 |
| 320 | DESC 1ª PARC 13º ACID TRAB | DESC1PARC13SACIDTRAB | 79 | 9 |
| 321 | DESC 1ª PARC 13º LIC MATERNIDADE | DESC1PARC13SLICMATER | 79 | 9 |
| 328 | MEDIAS 1ª PARC 13º AC TRAB | MEDIAS1PARC13ACTRAB | 79 | 9 |
| 329 | MEDIAS 2ª PARC 13º AC TRAB | MEDIAS2PARC13ACTRAB | 79 | 9 |
| 330 | 1ª PARC 13º LIC MATERNIDADE CIDADA | 1PAR13SALLICGESTCIDADA | 79 | 9 |
| 331 | MEDIA 1ª PARC 13º LIC MATERNIDADE CIDADA | MEDIAS1PA13SGESTCIDADA | 79 | 9 |
| 334 | DESC 1ª PARC 13º LIC MATERNIDADE CIDADA | DESC1PAR13SAGESTCIDADA | 79 | 9 |
| 542 | ACIDENTE TRABALHO | ACIDENTETRABALHO | 79 | 9 |
| 563 | MEDIAS ACIDENTE TRABALHO | MEDIASACIDENTETRABALHO | 79 | 9 |
| 990 | MULTA FGTS | MULTAFGTS | 74 | 9 |
| 996 | FGTS 13º SALARIO | FGTS13SALARIO | 79 | 9 |
| 997 | FGTS INDENIZACOES | FGTSRESCISORIO | 79 | 9 |
| 1851 | BASE IRRF TRANSPORTE | BASEIRRFREDUZIDATRANSP | 79 | 9 |
| 3000 | ANTECIPACAO 13º SALARIO | ANTECIPACAO13SALARIO | 79 | 9 |
| 4090 | DESCONTO DE ABONO ADIANTADO | DESCONTODEABONOADIANTADO | 79 | 9 |
| 4300 | ANTECIPACAO 13° FERIAS | ANTECIPACAO13SALPGFERIAS | 79 | 9 |
| 4301 | DESC ANTECIPACAO 13° FERIAS | DESCANTEC13SALPGFERIAS | 79 | 9 |
| 9210 | FGTS INTERMITENTE | FGTSINTERMITENTE | 79 | 9 |
| 9220 | FGTS 13° INTERMITENTE | FGTS13INTERMITENTE | 79 | 9 |
| 9367 | DESC ANTEC 13SAL FER LIC MATERNIDADE | DESCANTEC13SALFERLIC | 79 | 9 |
