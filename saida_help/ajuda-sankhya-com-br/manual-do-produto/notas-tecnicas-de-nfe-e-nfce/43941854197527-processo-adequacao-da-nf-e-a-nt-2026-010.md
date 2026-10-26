---
id: "43941854197527"
titulo: "Processo Adequação da NF-e à NT 2026.010 · v1.00 - (em análise)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43941854197527-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2026-010-v1-00-em-an%C3%A1lise"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Notas Técnicas  > Notas Técnicas de NFe e NFCe"
atualizado_em: "2026-10-14T12:36:07Z"
---

# Processo Adequação da NF-e à NT 2026.010 · v1.00 - (em análise)

![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/43948437880215)

## NT 2026.010 v1.00 – Novo leiaute do DANFE com IBS, CBS e IS

Radar Fiscal NF-e / NFC-e. Nota técnica publicada no Portal Nacional da NF-e em 10/2026. Alterações no DANFE modelo 55 (retrato e paisagem) para representar os tributos da Reforma Tributária, com mínima ruptura do leiaute atual e sem perder a legibilidade.

### Prazos

- **Homologação (teste): não informada.** A NT não traz data de implantação em ambiente de teste.
- **Produção: 01/12/2026.** Novo leiaute do DANFE passa a valer, nas versões retrato (referência) e paisagem (alternativa).

### O que muda na v1.00

#### 1. Totais – Novo bloco "Total do IBS/CBS/IS"

Inserido logo após o bloco Total do ICMS/IPI, consolida os totais dos novos tributos:

- Valor da CBS: vCBS (W56)
- Valor do IBS UF: vIBSUF (W41)
- Valor do IBS Município: vIBSMun (W46)
- Valor do Imposto Seletivo: vIS (W33)
- IBS / CBS monofásicos: vIBSMono e vCBSMono
- Monofásicos por retenção: vIBSMonoReten e vCBSMonoReten

#### 2. Emitente – Regime tributário no quadro do emitente

O quadro passa a exibir o Código do Regime Tributário (CRT, C21) e reserva área para o Tipo de Regime de Apuração do IBS e da CBS, cuja tag será publicada em NT futura. Até lá, o campo fica sem conteúdo.

#### 3. Itens – Bases, alíquotas e valores por item

O quadro Dados dos Produtos/Serviços traz cClassTrib (UB14), base do IBS/CBS (UB16), alíquotas e valores de IBS UF, IBS Município, CBS e IS.

Com redução de alíquota ou compra governamental (grupo gRed), imprima a alíquota efetiva (pAliqEfet); sem gRed, a alíquota vigente. O novo quadro permite a leitura sem decorar posições.

#### 4. Facultativos – Quadros e campos condicionados ao XML

Canhoto, fatura/duplicatas, FCP, DIFAL, ICMS e IBS/CBS monofásicos, ISSQN, transportador e QR Code podem ser omitidos quando não se aplicam. A exibição não autoriza inferir ou imprimir informação que não esteja no XML.
