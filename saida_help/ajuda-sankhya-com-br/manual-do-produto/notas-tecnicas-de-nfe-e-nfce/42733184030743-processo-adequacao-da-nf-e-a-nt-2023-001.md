---
id: "42733184030743"
titulo: "Processo Adequação da NF-e à NT 2023.001 (v1.10 e v1.20)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42733184030743-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2023-001-v1-10-e-v1-20"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Notas Técnicas  > Notas Técnicas de NFe e NFCe"
atualizado_em: "2026-10-14T12:36:07Z"
---

# Processo Adequação da NF-e à NT 2023.001 (v1.10 e v1.20)

**Caminhos de Acesso:** Menu Principal › Preferências › Empresa › aba NF-e/NFC-e › sub-aba Nota Técnica NF-e

---

**Você encontra neste artigo:**

| [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/42733184030743-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2023-001-v1-10-e-v1-20#h_01M00ZTH1V37RS1YVCC8AMREDC)  [O que foi alterado](https://ajuda.sankhya.com.br/hc/pt-br/articles/42733184030743-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2023-001-v1-10-e-v1-20#h_01M00ZTH1W4BERKJDSYXGR60GJ)     ↳ [v1.10](https://ajuda.sankhya.com.br/hc/pt-br/articles/42733184030743-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2023-001-v1-10-e-v1-20#h_01M00ZTH1X8D6Y2KSF34BK4B6B)     ↳ [v1.20 — ICMS Monofásico em combustíveis](https://ajuda.sankhya.com.br/hc/pt-br/articles/42733184030743-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2023-001-v1-10-e-v1-20#h_01M00ZTH21WFMC4EPT8FX7CCJV) | [Pontos de atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/42733184030743-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2023-001-v1-10-e-v1-20#h_01M00ZTH218WPMAMQ3WJA5ZQWY) |
| --- | --- |

## O que é e para que serve

A Nota Técnica 2023.001 reúne ajustes fiscais aplicados em duas versões: v1.10 e v1.20. A v1.20 trata do cálculo do ICMS Monofásico em operações com combustíveis; a v1.10 atualiza as regras de validação no regime de tributação monofásico do ICMS (combustíveis e gás) na importação de XML.

## O que foi alterado

### v1.10

A Nota Técnica 2023.001 v.1.10 visa estabelecer e atualizar as regras de validação aplicadas no regime de tributação monofásico do ICMS em operações com combustíveis e gás. Foram realizados ajustes no sistema Sankhya que permitem a inserção efetiva das informações por meio do Portal de Importação de XML para garantir o cálculo preciso dos impostos.

No fluxo de importação de XML, a cada configuração realizada no campo "Cálculo de ICMS, IPI e ISS" da tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114) (aba Impostos), o sistema apresenta comportamentos distintos:

- **Calcula e digita:** Ao definir esta opção e marcar "Usar imposto do arquivo" no [Portal de Importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354), o sistema preenche os campos pertinentes com os valores das tags (ex: <CST>, <qBCMono>, <adRemICMS>, <vICMSMono>, <qBCMonoReten>, <vICMSMonoReten>). Na aba de Impostos, seção "Arquivo", os campos Base ICMS, Valor ICMS, Base ST e Valor ST refletem esses valores originais do XML.
- **Não calcula e digita:** Na importação, os campos da Grade de Itens da nota e os dados de Impostos do Item são apresentados mapeando as tags correspondentes (ex: Base ICMS recebe <qBCMono>, Vlr. ICMS recebe <vICMSMono>, Base substituição recebe <qBCMonoReten>, Vlr. substituição recebe <vICMSMonoReten>).
- **Não calcula e não digita:** Ao abrir o documento processado, os campos (Tributação, Base ICMS, Alíquota ICMS, Valor ICMS, Base substituição, Vlr. substituição) estarão preenchidos com os valores das respectivas tags e bloqueados para edição.
- **Calcula e não digita:** Em casos como o processamento de uma Nota de Devolução de Venda, os campos de Tributação, Base ICMS, Alíq. ICMS e Vlr. ICMS estarão preenchidos tanto na Grade de Itens quanto na consulta de Dados do Imposto do Item.
- **Calcula na confirmação:** Tem comportamento semelhante à opção anterior, porém os campos Tributação, Base ICMS, Alíq. ICMS e Vlr. ICMS da Grade de Itens estarão vazios e bloqueados para digitação na abertura da nota. Os devidos cálculos serão realizados apenas no momento da confirmação da nota.

### v1.20 — ICMS Monofásico em combustíveis

Para realizar o cálculo do ICMS Monofásico aplicado nas operações com combustíveis, é necessário considerar as regras da Nota Técnica 2023.001 - v.1.20 e mantê-la ativa na sub-aba Nota Técnica NF-e.

Inclusão do campo de índice de mistura do biodiesel do diesel B (tag: <pBio>)  

Criação de campo específico no Grupo de Combustíveis para a indicação do índice de Mistura do Biodiesel no Óleo Diesel B. Esse campo irá auxiliar no cálculo do volume do Biodiesel B100 a ser misturado com Óleo Diesel A ou do volume do Biodiesel B100 misturado nas operações com Óleo Diesel B.

**Incluída a tag <pBio> no grupo "encerrante"**

As informações desse grupo é disponibilizado por hardware específico acoplado à bomba de Combustível definido no controle da venda do Posto Revendedor de Combustível. Nele, existem informações do número de identificação do bico utilizado no abastecimento, número da bomba, tanque, valor da leitura do contador do início do abastecimento e no térmico.

**Inclusão do Grupo Indicador da origem do combustível (tag: <origComb>)**

Esse grupo deve ser preenchido para as operações com Biodiesel B100, Óleo Diesel B e GLP/GLGN. Será utilizado para identificar as UF's do produtor, do importador de B100 ou GLGN utilizado na mistura. Além da identificação da UF de Origem, da qual há a necessidade de informar se o produto é nacional ou importado.

**Criação do grupo N02a - Grupo Tributação do ICMS = 02 (tag: <ICMS02>)**

Esse grupo trata do regime de tributação monofásica própria do ICMS nas operações com combustíveis nos termos da Lei Complementar nº 192/2022 e Convênio ICMS 199/2022.

Assim sendo, o novo código de Situação Tributária (CST = 02) é criado pelo Ajuste SINIEF Nº 1/2023.

Observe abaixo como cada tag desse grupo é preenchida:

| **TAG** | **INFORMAÇÃO** |
| --- | --- |
| <orig> | campo Origem do Produto do [Item](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradedeitens) Nota |
| <CST> | campo CST/CSOSN do [Imposto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#abaimpostos) Item Nota |
| <qBCMono> | campo Base de Cálculo do Imposto Item Nota |
| <adRemICMS> | campo Alíquota do Imposto Item Nota |
| <vICMSMono> | campo Valor do Imposto Item Nota |

**Criação do Grupo N03 - Grupo do ICMS = 15 (tag: ICMS15)**

Este grupo refere-se ao Regime de Tributação monofásica própria e com responsabilidade pela retenção do ICMS nas operações com combustíveis nos termos da Lei Complementar nº 192/2022 e Convênio ICMS 199/2022.

O novo Código de Situação Tributária (CST = 15) é criado pelo Ajuste SINIEF Nº 1/2023.

Observe abaixo como cada tag desse grupo é preenchida:

| **TAG** | **INFORMAÇÃO** |
| --- | --- |
| <orig> | campo Origem do Produto do [Item](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradedeitens) Nota |
| <CST> | campo CST/CSOSN do [Imposto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#abaimpostos) Item Nota |
| <qBCMono> | campo Base de Cálculo do Imposto Item Nota |
| <adRemICMS> | campo Alíquota do Imposto Item Nota |
| <vICMSMono> | campo Valor do Imposto Item Nota |
| <qBCMonoReten> | campo Base de Cálculo do Imposto Item Nota, correspondente   ao campo Imposto igual a ST |
| <adRemICMSReten> | campo Alíquota do Imposto Item Nota, correspondente ao   campo Imposto igual a ST |
| <vICMSMonoReten> | campo Valor do Imposto Item Nota, correspondente ao campo     Imposto igual a ST |
| <pRedAdRem> | campo Valor do Imposto Item Nota |
| <motRedAdRem> | campo Motivo Redução do adrem da [Alíquota de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934) |

**Criação do Grupo N07a - Grupo Tributação do ICMS = 53 (tag: <ICMS53>)**

Esse grupo aborda o Regime de Tributação monofásica com recolhimento diferido do ICMS nas operações com combustíveis nos termos da Lei Complementar nº 192/2022 e Convênio ICMS 199/2022.

Desse modo, o novo Código de Situação Tributária (CST = 53) é criado pelo Ajuste SINIEF Nº1/2023.

Observe abaixo como cada tag desse grupo é preenchida:

| **TAG** | **INFORMAÇÃO** |
| --- | --- |
| <orig> | campo Origem do Produto do [Item](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradedeitens) Nota |
| <CST> | campo CST/CSOSN do [Imposto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#abaimpostos) Item Nota |
| <qBCMono> | campo Base de Cálculo do Imposto Item Nota |
| <adRemICMS> | campo Alíquota do Imposto Item Nota |
| <vICMSMonoOp> | resultado da multiplicação do campo Base ICMS (Item Nota /     Itens) pelo campo Alíq. ICMS (Item Nota/Itens) |
| <pDif> | campo % de Outorga/Diferimento da Alíquota de ICMS |
| <vICMSMonoDif> | resultado da multiplicação do campo Base ICMS (Item Nota /     Itens) pelo campo Alíq. ICMS (Item Nota/Itens), multiplicado   pelo percentual de diferimento |
| <vICMSMono> | campo Valor do Imposto Item Nota |

**Criação do Grupo N08a - Grupo Tributação do ICMS = 61 (tag: <ICMS61>)**

O referido grupo abrange o Regime de Tributação monofásica sobre combustíveis com ICMS cobrado anteriormente nos Termos da Lei Complementar Nº 192/2022 e Convênio ICMS 199/2022.

Assim, o novo Código de Situação Tributária (CST = 61) é criado pelo Ajuste SINIEF Nº 1/2023.

Observe abaixo como cada tag desse grupo é preenchida:

| **TAG** | **INFORMAÇÃO** |
| --- | --- |
| <orig> | campo Origem do Produto do [Item](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradedeitens) Nota |
| <CST> | campo CST/CSOSN do [Imposto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#abaimpostos) Item Nota, do qual apenas o   valor 61 será válido |
| <qBCMonoRet> | campo Base de Cálculo do Imposto Item Nota, quando a CST   for igual a 61 |
| <adRemICMSRet | campo Alíquota do Imposto Item Nota, quando CST igual a 61 |

**Criação dos campos Valor Total do ICMS monofásico próprio (tag: <vICMSMono>)**

Este tópico refere-se ao Valor Total monofásico sujeito a retenção (tag: <**vICMSMono**>) e Valor total do ICMS monofásico retido anteriormente (tag: <**vICMSMonoRet**>) criados no grupo de Total da NF-e (tag: <**total**>).

**Criação dos campos indicadores da Base de Cálculo do ICMS monofásico (Campos: qBCMono, qBCMonoReten e qBCMonoRet)**

Os campos aqui informados visam permitir a indicação da Base de Cálculo do ICMS monofásico para cada uma das situações tributárias existentes.

**Criação dos campos totalizadores das Bases de Cálculos do ICMS monofásico (Campos: qBCMono, qBCMonoReten e qBCMonoRet) no Grupo W. Total da NF-e**

Os referidos campos aqui mencionados irão permitir a indicação da Base de Cálculo do ICMS monofásico para cada uma das situações tributárias existentes.

**Criação dos campos pRedAdRem e motRedAdRem (id: N48)**

Esses campos devem ser preenchidos quando houver algum percentual de redução do valor da alíquota ad rem junto ao indicador do motivo desta redução.

O cálculo realizado no campo **"% Redução Alíquota ad rem ICMS"** da tela [Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934) (aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#abageral)) irá preencher a tag <**pRedAdRem**>. Assim, este será executa da seguinte maneira:

```
  <qBCMono> x ( <adRemICMS> - <pRedAdRem> ) = <vICMSMono>
```

**Criação dos campos qBCMono, adRemICMS, vICMSMonoOp, pDif e vICMSMono**

Os campos criados acima visam atender à previsão de diferimento parcial, conforme previsto no Convênio ICMS 10/23 que altera o Convênio ICMS 199/22.

## Pontos de atenção

A NT 2023.001 também interage com a NT 2024.003: com as duas ativas juntas, o limite de defensivos agrícolas enviados no XML sobe de 1 para até 20.
