---
id: "43940813048343"
titulo: "Processo Adequação da NF-e à NT 2025.002  · v1.50 - (em análise)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43940813048343-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2025-002-v1-50-em-an%C3%A1lise"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Notas Técnicas  > Notas Técnicas de NFe e NFCe"
atualizado_em: "2026-10-14T12:36:07Z"
---

# Processo Adequação da NF-e à NT 2025.002  · v1.50 - (em análise)

![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/43948468633879)

## NT 2025.002-RTC v1.50 – Tributação monofásica de combustíveis (IBS, CBS)

Radar Fiscal NF-e / NFC-e. Nota técnica publicada no Portal Nacional da NF-e em 06/2026. Reformulação do leiaute da tributação monofásica de combustíveis no grupo gIBSCBSMono, com separação entre Ad Rem e Ad Valorem para IBS e CBS, e novas regras de validação.

### Prazos

- **Homologação (teste): até 01/09/2026.** Novo leiaute e regras de validação disponíveis no ambiente de teste. Pode variar por UF.
- **Produção: 03/11/2026.** Leiaute reformulado da monofasia passa a valer para todos os emissores.

### O que muda na v1.50

#### 1. UB84 – Ad Rem e Ad Valorem em grupos separados (Rejeições 1219 a 1272)

O grupo gIBSCBSMono passa a ter quatro grupos, um por tributo e modalidade:

- IBS Monofásico Ad Rem: gIBSMonoAdRem (UB85a)
- IBS Monofásico Ad Valorem: gIBSMonoAdValorem (UB90)
- CBS Monofásica Ad Rem: gCBSMonoAdRem (UB95a)
- CBS Monofásica Ad Valorem: gCBSMonoAdValorem (UB100)

Cada grupo traz as situações padrão (gMonoPadrao), sujeita à retenção (gMonoReten) e retida anteriormente (gMonoRet), conforme os indicadores do cClassTrib.

#### 2. dhEmi – Qual modalidade usar em cada ano (Rejeições 1219, 1220, 1228 e 1229)

O grupo exigido depende do ano da data de emissão (dhEmi). Informar a modalidade fora do período gera rejeição (UB85a-10/20, UB90-10/20).

- 2026: IBS Ad Valorem e CBS Ad Valorem.
- 2027 e 2028: IBS Ad Valorem e CBS Ad Rem.
- A partir de 2029: IBS Ad Rem e CBS Ad Rem.

#### 3. Base de cálculo – Quantidade × alíquota ou valor tributado

No Ad Rem, o imposto vem da quantidade tributada (qBCMono) multiplicada pela alíquota ad rem (adRemIBS, adRemCBS).

No Ad Valorem, a base é o valor tributado (vBCMono) e o IBS é separado em vIBSMonoUF e vIBSMonoMun, com vIBSMono igual à soma das duas parcelas.

#### 4. gpBioDiferenca – Mistura de EAC fora do percentual obrigatório (LC 214/2025, art. 179)

Novo grupo para quando o percentual de etanol anidro combustível (EAC) misturado à gasolina A difere do obrigatório (pBio ≠ pBioObrigatório). Informa a quantidade de EAC (qBCBioComb) e o valor de IBS ou CBS da diferença.

- cClassTrib 620004: valor a recolher.
- cClassTrib 620005: valor a ressarcir.

A tabela vRefBioComb ainda será publicada.

### Calendário em produção

- **03/08/2026 (já vigente, v1.36 e v1.40):** IBS/CBS obrigatórios na NF-e/NFC-e (RV UB12-10) para Regime Normal; novos campos cIndOp, ISUFemit e gALCZFMCBS.
- **01/09/2026 (homologação, v1.50):** leiaute reformulado da tributação monofásica disponível para teste.
- **03/11/2026 (produção, v1.50):** grupos Ad Rem e Ad Valorem do IBS e da CBS; novas regras de validação da monofasia.

Fonte: NT 2025.002-RTC v1.50 – Portal Nacional da NF-e, publicada em 06/2026.
