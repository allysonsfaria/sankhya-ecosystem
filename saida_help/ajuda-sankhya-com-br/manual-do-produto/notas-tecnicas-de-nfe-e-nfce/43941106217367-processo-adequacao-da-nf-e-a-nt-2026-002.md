---
id: "43941106217367"
titulo: "Processo Adequação da NF-e à NT 2026.002 · v1.11 - (em análise)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43941106217367-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2026-002-v1-11-em-an%C3%A1lise"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Notas Técnicas  > Notas Técnicas de NFe e NFCe"
atualizado_em: "2026-10-14T12:36:07Z"
---

# Processo Adequação da NF-e à NT 2026.002 · v1.11 - (em análise)

![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/43948313850647)

## NT 2026.002 v1.11 – DANFE Simplificado Tipo 2, emissão off-line e autorização com alerta

Radar Fiscal NF-e / NFC-e. Nota técnica publicada no Portal Nacional da NF-e em 06/2026. NF-e modelo 55 com DANFE Simplificado Tipo 2 (tpImp = 6) em operações típicas de NFC-e, contingência off-line e autorização com alerta. A v1.11 adia a produção de três regras de referenciamento.

### Prazos

- **Homologação (teste): desde 01/09/2026.** Regras da v1.00/v1.10 (DANFE Simplificado Tipo 2, alertas, referenciamento) disponíveis no ambiente de teste.
- **Produção: 14/12/2026.** Nova data em produção para as RV I08-180, BA02-35 e VC02-40 (antes 05/10/2026).

### O que muda na v1.11

#### 1. BA02-35, VC02-40 e I08-180 – Referenciamento: produção adiada (Rejeições 679 e 375)

Na NF-e de saída (tpNF = 1) que não seja complementar nem devolução, fica proibido referenciar NFC-e (modelo 65), CF-e (modelo 59) ou NF-e com DANFE Simplificado Tipo 2 (tpImp = 6), no grupo refNFe (BA02-35) ou por item em DFeReferenciado (VC02-40).

A I08-180 rejeita NF-e com CFOP 5.929/6.929 (lançamento relativo a cupom fiscal) que referencie NFC-e.

Prazo em produção alterado de 05/10/2026 para 14/12/2026 (mais 2 meses para adequação).

### Escopo da NT

#### 2. tpImp = 6 – NF-e com DANFE Simplificado Tipo 2 (Rejeições 704 a 787 e 750)

Opção para emitir NF-e modelo 55 em operações que normalmente seriam acobertadas por NFC-e (Ajuste SINIEF 13/26). Valem as mesmas restrições da NFC-e:

- Somente saída, operação interna, consumidor final e finalidade 1-Normal.
- Presença indPres = 1, 4 ou 5; em venda não presencial com entrega (4), o destinatário é obrigatório.
- Emissão on-line com tolerância de 5 minutos, QR Code versão 3 obrigatório e sem referenciar outros documentos.
- Acima de R$ 10.000,00 (ou limite da UF), o destinatário deve ser identificado.

#### 3. tpEmis = 9 – Contingência off-line também na NF-e (Rejeição 711)

O tipo de emissão 9 passa a valer para a NFC-e e para a NF-e com DANFE Simplificado Tipo 2, com transmissão posterior para autorização. Fora do tpImp = 6, a contingência off-line é rejeitada. Após 24 h: cStat 150.

#### 4. cStat 120 – Autorização de uso com alerta (Alerta 172)

A nota é autorizada normalmente e o alerta volta no protocolo (grupo PR13: cMsg/xMsg), até 5 alertas. Não precisa retransmitir. Inicialmente só para NFC-e: a regra 5E17-65 alerta quando o destinatário CNPJ está bloqueado ou vedado na UF.

### Calendário em produção

- **15/06/2026 (já vigente, v1.00):** W16-40: limite por UF para NFC-e sem identificação do destinatário (padrão R$ 10.000,00).
- **05/10/2026 (v1.00 e v1.10):** DANFE Simplificado Tipo 2, contingência off-line e autorização com alerta; ajustes nas regras BA e W16; remoção de BA05-10 a BA20-20, I08-184/186 e VC02-50.
- **14/12/2026 (v1.11):** I08-180, BA02-35 e VC02-40 (referenciamento de NFC-e, CF-e e tpImp = 6).

Fonte: NT 2026.002 v1.11 – Portal Nacional da NF-e, publicada em 06/2026.
