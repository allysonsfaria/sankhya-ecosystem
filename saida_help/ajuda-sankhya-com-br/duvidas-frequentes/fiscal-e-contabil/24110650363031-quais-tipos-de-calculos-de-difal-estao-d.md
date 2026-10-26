---
id: "24110650363031"
titulo: "Quais tipos de cálculos de Difal estão disponíveis no sistema?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/24110650363031-Quais-tipos-de-c%C3%A1lculos-de-Difal-est%C3%A3o-dispon%C3%ADveis-no-sistema"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:47:40Z"
rotulos: ["Configuração", "NF-e", "Fórmulas", "SEFAZ", "ICMS", "Impostos", "tipos de cálculos de Difal"]
---

# Quais tipos de cálculos de Difal estão disponíveis no sistema?

Ao emitir uma NF-e com o Valor do ICMS Interestadual para a UF de Destino (vICMSUFDest) diferente do calculado pela Sefaz, é preciso se atentar as configurações para o cáculo do Difal.

Primeiramente, no cadastro de **“Alíquotas de ICMS”,** verifique o campo **“Tipo de Calculo DIFAL”;**

![Imagem 1: Primeiramente, n o cadastro de “Alíquotas de ICMS”, verifique o campo “Tipo de Calculo DIFAL”;](https://ajuda.sankhya.com.br/hc/article_attachments/24110650358935)

Caso este campo esteja marcado com a Opção: **“4- Calculo do DIFAL com ICMS Destino Por dentro”,** deve-se optar por outra fórmula para o calculo do Difal, pois esta opção não é mais aceita pela Sefaz.

#### Seguem abaixo os tipos de cálculos atualmente disponíveis no sistema:

**0 - Sem considerar redução da Base:** Vlr. Operação x (Alíq. Interna Destino - Alíq. Interestadual)

**1 - Com redução da base aplicada na base:** ((Vlr. Operação x (1 - Perc. Redução Base Destino)) x Alíq. Interna Destino) - ICMS Próprio

**2 - Com redução da base aplicada na alíquota:** ((Vlr. Operação x Alíq. Interna Destino x (1 - Perc. Redução Base Destino))) - ICMS Próprio

**3 - ICMS Interestadual calculado sob a BC do DIFAL:** (Vlr. Operação x (1 - Perc. Redução Base Destino)) x Alíq. Interna Destino) - Alíquota Interestadual)

**4 - Cálculo do DIFAL com ICMS Destino por dentro:** (((Vlr. Operação / (1 - Alíq. Interna Destino + Perc. ICMS FCP))) x (1 - Perc. Redução Base Destino)) x Alíq. Interna Destino) - ((Vlr. Operação / (1 - Alíq. Interna Destino + Perc. ICMS FCP))) x Alíq. Interestadual)

**5 - Cálculo do DIFAL Convênio 142/2018:** Vlr. Operação / (1 - Alíq. Interna Destino - Alíq. Interestadual)

**6 - Cálculo do DIFAL com a redução do ICMS Próprio:** ((Vlr.Operação-ICMS próprio)/(1 - Alíq. Interna Destino - Alíquota FCP))

**7 - ICMS difal base dupla UF Sergipe:** (Vlr. Operação x (1 - Perc. Redução Base Destino)) / (1 - Alíq. Interna Destino - Alíq. Interestadual)

**8 - Base de cálculo do DIFAL e do FCP por fórmula:** A Base de cálculo do DIFAL e do FCP será calculada pela fórmula informada.

**9 - Cálculo do DIFAL com ICMS Destino por dentro - Base Dupla:** (((Vlr. Operação / (1 - (Alíq. ICMS Interna Destino + Perc. ICMS FCP))) x (1 - Perc. Redução Base Destino)) x Alíq. Interna Destino) - (Vlr. Operação x Alíq. Interestadual).

**10 - Calculo da base, valor do DIFAL e do FCP por fórmula:** A base de cálculo, o valor do DIFAL e o FCP serão calculados pelas fórmulas informadas.

**Observação:**

Qualquer validação da regra de cálculo deve ser feita pela contabilidade. Caso nenhuma das opções atenda será necessário nos enviar a nova regra de cálculo.

 [Nota Técnica 2015.003 - NF-e, CEST e DIFAL Partilhado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600414-Nota-T%C3%A9cnica-2015-003-NF-e-CEST-e-DIFAL-Partilhado).

#### **(1)**Confira também os outros links relacionados à rotina:

[Alíquota Interna de Destino](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaalquotainternadedestino)

[Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934)

 [Partilha DIFAL](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111373)

[Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)
