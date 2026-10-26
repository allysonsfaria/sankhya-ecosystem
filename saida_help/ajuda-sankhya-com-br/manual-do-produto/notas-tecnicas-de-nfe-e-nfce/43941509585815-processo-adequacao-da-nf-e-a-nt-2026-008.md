---
id: "43941509585815"
titulo: "Processo Adequação da NF-e à NT 2026.008 · v1.00 - (em análise)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43941509585815-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2026-008-v1-00-em-an%C3%A1lise"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Notas Técnicas  > Notas Técnicas de NFe e NFCe"
atualizado_em: "2026-10-14T12:36:07Z"
---

# Processo Adequação da NF-e à NT 2026.008 · v1.00 - (em análise)

![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/44061193611415)

## NT 2026.008-RTC v1.00 – Valor Líquido do Produto na NF-e (IBS, CBS, IS)

Radar Fiscal NF-e / NFC-e. Nota técnica publicada no Portal Nacional da NF-e em 09/2026. Novos campos para o valor do item sem tributos, novo grupo do ICMS previsto no pagamento antecipado e a regra de composição do vProd com IBS e CBS.

### Prazos

- **Homologação (teste): 26/10/2026 (prorrogada; antes, 05/10/2026).** Novos campos e regras de validação disponíveis no ambiente de teste.
- **Produção: 16/11/2026 (prorrogada; antes, 03/11/2026).** Campos de valor líquido e grupo NB01 passam a valer para todos os emissores.

### O que muda na v1.00

#### 1. I11a e W01a – Valor líquido do produto, sem tributos (Rejeições 1279, 1282 e 1283)

Nova sequência I11a no item e novo total no grupo W. Por enquanto opcional, será obrigatória no futuro (I11c-10).

- Valor líquido unitário: vUnComLiq (I11b)
- Valor líquido do item: vProdLiq (I11c)
- Total líquido da nota: vProdLiqTot (W01a)

Na NF-e normal, vProdLiq deve ser igual a vUnComLiq × qCom (tolerância de 0,01) e o total deve bater com a soma dos itens.

#### 2. vProd – IBS e CBS compõem o valor do produto (Rejeição 1105)

A partir de 2027, IBS, CBS e IS passam a compor o vProd (exceto importação), sem entrar na própria base de cálculo e sem somar de novo no total da nota. Os grupos tributários ficam como informativos.

As regras VB01-10 e VB01-20 (vItem) foram ajustadas e a UB16-10 (base de cálculo do IBS/CBS) foi removida.

#### 3. NB01 – ICMS previsto no pagamento antecipado (Rejeições 1280 e 1281)

Novo grupo ICMSPrevistoPagtoAntecip com o campo vICMSPrevisto (NB02): o ICMS que incidirá no fornecimento futuro. Usado só quando tpNFDebito = 06 ou tpOperGov = 4; sem ICMS devido, informe 0.

Na NFC-e ou fora desses cenários, o grupo é rejeitado. A obrigatoriedade (NB01-30) entra depois: em produção a partir de 01/03/2027.

### Calendário

- **26/10/2026 (homologação, v1.00):** campos vUnComLiq, vProdLiq e vProdLiqTot; grupo NB01 e regras I11c, NB01-10/20, W01a, B25-80, VB01.
- **16/11/2026 (produção, v1.00):** mesmo escopo da homologação valendo para todos os emissores.
- **01/03/2027 (produção, NB01-30):** grupo NB01 obrigatório no pagamento antecipado (homologação em 01/02/2027).

Fonte: NT 2026.008-RTC v1.00 – Portal Nacional da NF-e, publicada em 09/2026.
