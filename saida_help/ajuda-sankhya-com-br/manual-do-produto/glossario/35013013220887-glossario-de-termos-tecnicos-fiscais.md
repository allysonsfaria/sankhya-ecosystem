---
id: "35013013220887"
titulo: "Glossário de Termos Técnicos Fiscais"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35013013220887-Gloss%C3%A1rio-de-Termos-T%C3%A9cnicos-Fiscais"
trilha: "Manual do Produto > Fiscal e Contábil > Reforma Tributária > Glossário"
atualizado_em: "2026-07-29T13:14:10Z"
rotulos: ["Impostos", "br.com.sankhya.mgeliv.cadastros.AliquotaCbs", "br.com.sankhya.mgeliv.cadastros.AliquotaIs", "br.com.sankhya.mgeliv.cadastros.AliquotaIbs", "br.com.sankhya.mgeliv.cadastros.AliquotaMonofasica", "IBS", "CBS", "IS", "Reforma Tributária", "Glossário"]
---

# Glossário de Termos Técnicos Fiscais

Encontre as definições dos campos e siglas introduzidos pela Reforma Tributária e seus novos impostos e modelos de tributação, como o **IS (Imposto Seletivo)**, a **CBS (Contribuição sobre Bens e Serviços)** e o **IBS (Imposto sobre Bens e Serviços)**.

**Você encontra neste artigo:**

- [Imposto Seletivo (IS)](https://ajuda.sankhya.com.br/hc/pt-br/articles/35013013220887-Gloss%C3%A1rio-de-Termos-T%C3%A9cnicos-Fiscais#is)
- [IBS e CBS Monofásico](https://ajuda.sankhya.com.br/hc/pt-br/articles/35013013220887-Gloss%C3%A1rio-de-Termos-T%C3%A9cnicos-Fiscais#mono)
- [Contribuição sobre Bens e Serviços (CBS)](https://ajuda.sankhya.com.br/hc/pt-br/articles/35013013220887-Gloss%C3%A1rio-de-Termos-T%C3%A9cnicos-Fiscais#cbs)
- [Imposto sobre Bens e Serviços (IBS)](https://ajuda.sankhya.com.br/hc/pt-br/articles/35013013220887-Gloss%C3%A1rio-de-Termos-T%C3%A9cnicos-Fiscais#ibs)
- [Siglas gerais](https://ajuda.sankhya.com.br/hc/pt-br/articles/35013013220887-Gloss%C3%A1rio-de-Termos-T%C3%A9cnicos-Fiscais#siglas)

---

### Imposto Seletivo (IS)

O Imposto Seletivo (IS) é um tributo de competência federal que incide sobre a produção, comercialização ou importação de bens e serviços que podem ser prejudiciais à saúde ou ao meio ambiente.

| Sigla/Campo | Descrição |
| --- | --- |
| `CodClassTribIS` | Código de Classificação Tributária do Imposto Seletivo. |
| `vProd` | Valor Total Bruto dos Produtos ou Serviços. |
| `vServ` | Valor total dos Serviços sob não incidência ou não tributados pelo ICMS. |
| `vFrete` | Valor Total do Frete. |
| `vSeg` | Valor Total do Seguro. |
| `vOutro` | Outras despesas acessórias. |
| `vII` | Valor do Imposto de Importação. |
| `vDesc` | Valor do Desconto. |
| `vPis` | Valor do PIS (Programa de Integração Social). |
| `vCofins` | Valor da COFINS (Contribuição para o Financiamento da Seguridade Social). |
| `vICMS` | Valor do ICMS (Imposto sobre Circulação de Mercadorias e Serviços). |
| `vICMSUFDest` | Valor do ICMS Interestadual para a Unidade da Federação de destino. |
| `vFCP` | Valor do Fundo de Combate à Pobreza. |
| `vFCPUFDest` | Valor do ICMS relativo ao Fundo de Combate à Pobreza (FCP) da UF de destino. |
| `vICMSMono` | Valor do ICMS próprio em regime monofásico. |
| `vISSQN` | Valor do ISSQN (Imposto Sobre Serviços de Qualquer Natureza). |
| `vBC` | Base de Cálculo do Imposto Seletivo. |
| `pIS` | Percentual de alíquota ad valorem (sobre o valor) do IS. |
| `pISEspec` | Alíquota específica do IS (valor fixo por unidade de medida). |
| `qTrib` | Quantidade tributável, utilizada para o cálculo com alíquota específica. |
| `vIS` | Valor do Imposto Seletivo. |

---

### IBS e CBS Monofásico

Regime de tributação em que o imposto é cobrado uma única vez em toda a cadeia de produção e circulação de um produto ou serviço.

#### Nível do item da nota fiscal

| Sigla/Campo | Descrição |
| --- | --- |
| `gIBSCBSMono` | Grupo de Informações do IBS e CBS em operações com imposto monofásico. |
| `qBCMono` | Quantidade tributada na monofasia. |
| `qBCMonoReten` | Quantidade tributada sujeita à retenção na monofasia. |
| `qBCMonoRet` | Quantidade tributada que já foi retida anteriormente na cadeia. |
| `adRemIBS` | Alíquota ad rem (valor fixo por unidade) do IBS. |
| `adRemIBSReten` | Alíquota ad rem do IBS sujeito a retenção. |
| `adRemIBSRet` | Alíquota ad rem do IBS que foi retido anteriormente. |
| `adRemCBS` | Alíquota ad rem da CBS. |
| `adRemCBSReten` | Alíquota ad rem da CBS sujeita a retenção. |
| `adRemCBSRet` | Alíquota ad rem da CBS que foi retida anteriormente. |
| `vIBSMono` | Valor do IBS monofásico. |
| `vIBSMonoReten` | Valor do IBS monofásico sujeito a retenção. |
| `vIBSMonoRet` | Valor do IBS que foi retido anteriormente. |
| `vCBSMono` | Valor da CBS monofásica. |
| `vCBSMonoReten` | Valor da CBS monofásica sujeita a retenção. |
| `vCBSMonoRet` | Valor da CBS que foi retida anteriormente. |
| `qTrib` | Quantidade Tributável (quantidade comercial convertida na unidade de tributação). |
| `vIBSMonoDif` | Valor do IBS monofásico diferido (postergado). |
| `pDifIBS` | Percentual do diferimento do IBS monofásico. |
| `vCBSMonoDif` | Valor da CBS monofásica diferida. |
| `pDifCBS` | Percentual do diferimento da CBS monofásica. |
| `vTotIBSMonoItem` | Valor total de IBS monofásico do item. |
| `vTotCBSMonoItem` | Valor total da CBS monofásica do item. |

#### Nível do rodapé (totais da nota fiscal)

| Sigla/Campo | Descrição |
| --- | --- |
| `IBSCBSTot` | Grupo de totais da NF-e referentes ao IBS e CBS. |
| `vIBSMono` | Total do IBS monofásico da nota. |
| `vCBSMono` | Total da CBS monofásica da nota. |
| `vIBSMonoReten` | Total do IBS monofásico sujeito a retenção. |
| `vCBSMonoReten` | Total da CBS monofásica sujeita a retenção. |
| `vIBSMonoRet` | Total do IBS monofásico retido anteriormente. |
| `vCBSMonoRet` | Total da CBS monofásica retida anteriormente. |

---

### CBS (Contribuição sobre Bens e Serviços)

Contribuição federal que unifica o PIS e a COFINS, incidindo sobre o valor agregado em operações com bens e serviços.

| Sigla/Campo | Descrição |
| --- | --- |
| `vBC` | Base de Cálculo da CBS. |
| `pCBS` | Percentual da alíquota da CBS. |
| `pDif` | Percentual do diferimento da CBS. |
| `vDif` | Valor do diferimento (postergado) da CBS. |
| `vDevTrib` | Valor do tributo devolvido da CBS. |
| `pRedAliq` | Percentual da Redução da Alíquota da CBS. |
| `AlíqEfet` | Alíquota Efetiva da CBS (considerando reduções ou benefícios). |
| `cCredPres` | Código de Classificação do Crédito Presumido da CBS. |
| `pCredPres` | Percentual do Crédito Presumido da CBS a ser aplicado sobre a base de cálculo. |
| `vCredPres` | Valor do Crédito Presumido da CBS. |
| `vCredPresCondSus` | Valor do Crédito Presumido da CBS que se encontra em condição suspensiva. |
| `vCBS` | Valor da CBS. |
| `pAliqEfet` | Alíquota Efetiva da CBS que será aplicada à Base de Cálculo. |
| `pRedutor` | Percentual de redução de alíquota em compra governamental. |

---

### IBS (Imposto sobre Bens e Serviços)

Imposto de competência estadual e municipal que unifica o ICMS e o ISS, incidindo sobre o valor agregado em operações com bens e serviços.

| Sigla/Campo | Descrição |
| --- | --- |
| `vBC` | Base de Cálculo do IBS. |
| `pIBSUF` | Percentual da alíquota do IBS de competência das Unidades da Federação (Estados). |
| `pIBSMun` | Percentual da alíquota do IBS de competência do Município. |
| `pDif` | Percentual do diferimento do IBS. |
| `vDif` | Valor do Diferimento (postergado) do IBS. |
| `vDevTrib` | Valor do tributo devolvido do IBS. |
| `pRedAliq` | Percentual da redução de alíquota do IBS. |
| `AlíqEfet` | Alíquota Efetiva do IBS a ser aplicada sobre a base de cálculo. |
| `cCredPres` | Código de Classificação do Crédito Presumido do IBS. |
| `pCredPres` | Percentual do Crédito Presumido do IBS a ser aplicado sobre a base de cálculo. |
| `vCredPres` | Valor do Crédito Presumido do IBS. |
| `vCredPresCondSus` | Valor do Crédito Presumido em condição suspensiva do IBS. |
| `vIBSUF` | Valor do IBS de competência da Unidade da Federação. |
| `vIBSMun` | Valor do IBS de competência do Município. |
| `pAliqEfet` (Município) | Alíquota Efetiva do IBS de competência do Município que será aplicada à Base de Cálculo. |
| `pAliqEfet` (UF) | Alíquota Efetiva do IBS de competência das UF que será aplicada à Base de Cálculo. |
| `pRedutor` | Percentual de redução de alíquota em compra governamental. |

---

### Siglas gerais

| Sigla/Campo | Descrição |
| --- | --- |
| `gCompraGov` | Grupo de Compra Governamental. |
| `gTribCompraGov` | Grupo de informações da composição do valor do IBS e da CBS em compras governamentais. |
| `tpOperGov` | Tipo de operação com o ente governamental. |
