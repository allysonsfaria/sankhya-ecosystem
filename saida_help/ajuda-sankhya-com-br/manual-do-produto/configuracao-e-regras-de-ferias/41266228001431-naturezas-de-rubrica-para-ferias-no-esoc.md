---
id: "41266228001431"
titulo: "Naturezas de Rubrica para Férias no eSocial"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/41266228001431-Naturezas-de-Rubrica-para-F%C3%A9rias-no-eSocial"
trilha: "Manual do Produto > Pessoas+ > Férias > Configuração e Regras de Férias"
atualizado_em: "2026-09-25T23:59:42Z"
rotulos: ["Configuração", "Impostos", "eSocial", "Férias", "Pessoal+", "Naturezas de Rubrica para Férias no eSocial", "Natureza de Rubrica"]
---

# Naturezas de Rubrica para Férias no eSocial

**Módulo:** Pessoal+
**Caminho de acesso:** Pessoal+ › Cadastros
**ID da tela:** br.com.sankhya.rh.CadastroEventos

---

### Descrição e Usabilidade

As naturezas de rubrica são utilizadas pelo eSocial para identificar a finalidade de cada verba paga ao trabalhador. No caso das férias, a natureza informada na rubrica determina como o valor será tratado pelos órgãos governamentais, influenciando a composição de demonstrativos, totalizadores e demais obrigações legais.

No Pessoal+, os eventos padrão de férias são configurados de acordo com as orientações do [Manual de Orientação do eSocial (MOS)](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-3-consolidada-ate-a-no-s-1-3-10-2026.pdf), garantindo que as informações enviadas estejam compatíveis com o leiaute vigente.

As principais naturezas utilizadas para férias são:

| Natureza | Descrição |
| --- | --- |
| 1015 | Adiantamento de férias |
| 1016 | Remuneração de Férias |
| 1017 | Terço constitucional de férias |

Para identificar a natureza utilizada nas rubricas, acesse a tela **Eventos** (Pessoal+ > Cadastros), localize o evento utilizado para férias e verifique na aba **eSocial**, o campo **Natureza da Rubrica**.

![Imagem 1: Para identificar a natureza utilizada nas rubricas, acesse a tela Eventos (Pessoal+ > Cadastros), localize o evento…](https://ajuda.sankhya.com.br/hc/article_attachments/41288510359319)

É essa informação que será enviada ao governo por meio do evento S-1010 e posteriormente utilizada nos eventos periódicos.

Os eventos abaixo estão configurados com a **Natureza da Rubrica 1015** por representarem verbas que compõem o Recibo de Férias, ou seja, o pagamento da antecipação das férias e, portanto, não integram a base de apuração do INSS:

- 4410 — FÉRIAS
- 4420 — 1/3 DE FÉRIAS
- 4430 — MÉDIA DE FÉRIAS

Já os eventos abaixo estão com os códigos de **Natureza da Rubrica 1016 e 1017**, pois correspondem às verbas de férias relativas aos dias efetivamente lançados na competência.

Esses eventos representam as férias efetivamente usufruídas na competência e, por isso, participam normalmente da apuração previdenciária e dos totalizadores do eSocial conforme suas incidências configuradas:

- 4150 — FÉRIAS NA COMPETÊNCIA
- 4160 — 1/3 DE FÉRIAS NA COMPETÊNCIA
- 4190 — MÉDIA DE FÉRIAS NA COMPETÊNCIA

**Exemplos Práticos**

**1 – Férias pagas em mês anterior ao gozo**

**Pagamento:** 28/11/2025
**Início das férias:** 01/12/2025

Evento S-1200 - Período de apuração 11/2025

| Rubrica | Natureza | Tipo | {codIncCP} | {codIncFGTS} | {codIncIRRF} |
| --- | --- | --- | --- | --- | --- |
| Adiantamento de Férias | 1015 | Venc. | 00 | 00 | 13 |

Evento S-1200 - Período de apuração 12/2025

| Rubrica | Natureza | Tipo | {codIncCP} | {codIncFGTS} | {codIncIRRF} |
| --- | --- | --- | --- | --- | --- |
| Remuneração de Férias | 1016 | Venc. | 11 | 11 | 13 |
| Terço constitucional de Férias | 1017 | Venc. | 11 | 11 | 13 |
| Adiantamento de Férias | 9221 | Desc. | 00 | 00 | 13 |

**2 – Férias pagas e gozadas na mesmo mês**

**Pagamento:** 07/11/2025
**Início das férias:** 10/11/2025

Evento S-1200 - Período de apuração 11/2025

Opção 1

| Rubrica | Natureza | Tipo | {codIncCP} | {codIncFGTS} | {codIncIRRF} |
| --- | --- | --- | --- | --- | --- |
| Adiantamento de Férias | 1015 | Venc. | 00 | 00 | 13 |
| Remuneração de Férias | 1016 | Venc. | 11 | 11 | 13 |
| Terço constitucional de Férias | 1017 | Venc. | 11 | 11 | 13 |
| Adiantamento de Férias | 9221 | Desc. | 00 | 00 | 13 |

Opção 2

| Rubrica | Natureza | Tipo | {codIncCP} | {codIncFGTS} | {codIncIRRF} |
| --- | --- | --- | --- | --- | --- |
| Remuneração de Férias | 1016 | Venc. | 11 | 11 | 13 |
| Terço constitucional de Férias | 1017 | Venc. | 11 | 11 | 13 |
