---
id: "43939811332887"
titulo: "Processo Adequação da NF-e à NT 2025.002 · v1.52 - (em análise)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43939811332887-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2025-002-v1-52-em-an%C3%A1lise"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Notas Técnicas  > Notas Técnicas de NFe e NFCe"
atualizado_em: "2026-10-14T12:36:07Z"
---

# Processo Adequação da NF-e à NT 2025.002 · v1.52 - (em análise)

![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/44061244516887)

## NT 2025.002-RTC v1.52 – Reforma Tributária do Consumo (IBS, CBS, IS)

Radar Fiscal NF-e / NFC-e. Nota técnica publicada no Portal Nacional da NF-e em 01/10/2026. Ajuste pontual nas regras de validação de notas de devolução (finNFe = 4) e novo prazo em produção para o referenciamento por item.

### Prazos

- **Homologação (teste): até 26/10/2026 (prorrogada; antes, 05/10/2026).** Correção da RV VC02-50 disponível no ambiente de teste. Pode variar por UF.
- **Produção: 16/11/2026 (prorrogada; antes, 03/11/2026).** VC02-50 corrigida e VC02-14 passam a valer para todos os emissores.

### O que muda na v1.52

#### 1. VC02-50 – Regra de devolução com escopo ajustado (Rejeição 1194)

Na NF-e de devolução de saída (finNFe = 4 e tpNF = 1), a exigência de que o emitente da nota referenciada seja igual ao destinatário da devolução agora só se aplica quando o DF-e referenciado também for de saída (tpNF = 1).

Devoluções que referenciam nota de entrada emitida pelo próprio contribuinte deixam de cair na rejeição 1194. Resultado: menos rejeições indevidas.

#### 2. VC02-14 – Referência por item na devolução: novo prazo (Rejeição 321)

Na devolução de mercadoria, a nota de origem deve ser referenciada por item no grupo DFeReferenciado (chaveAcesso). Fica proibido usar a tag refNFe para isso.

Prazo em produção alterado de 05/10/2026 para 03/11/2026 e, depois, para 16/11/2026 (+6 semanas para adequação).

### Calendário em produção

- **03/08/2026 (já vigente, v1.51):** IBS/CBS obrigatórios na NF-e/NFC-e (RV UB12-10) para Regime Normal.
- **05/10/2026 (v1.51):** alterações em regras de validação de IBS/CBS (UB13, UB22, UB26, UB45, UB56, UB64, I08-140/144, B25-80 e outras).
- **16/11/2026 (v1.50 e v1.52):** VC02-14 e VC02-50 (devolução); novo leiaute da tributação monofásica de combustíveis.

Fonte: NT 2025.002-RTC v1.52 – Portal Nacional da NF-e, publicada em 01/10/2026.
