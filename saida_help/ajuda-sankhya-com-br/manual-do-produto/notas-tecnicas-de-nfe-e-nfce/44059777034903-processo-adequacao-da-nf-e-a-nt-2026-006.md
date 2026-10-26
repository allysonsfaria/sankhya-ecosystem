---
id: "44059777034903"
titulo: "Processo Adequação da NF-e à NT 2026.006 · v1.00 - (em análise)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44059777034903-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2026-006-v1-00-em-an%C3%A1lise"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Notas Técnicas  > Notas Técnicas de NFe e NFCe"
atualizado_em: "2026-10-14T12:36:07Z"
---

# Processo Adequação da NF-e à NT 2026.006 · v1.00 - (em análise)

![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/44059793347863)

## NT 2026.006-RTC v1.00 – Vinculação do pagamento ao DF-e (Split Payment)

Radar Fiscal NF-e / NFC-e. Nota técnica publicada no Portal Nacional da NF-e em 06/2026. Novo grupo YC (gPgtoVinc) na NF-e/NFC-e e novo evento 110300 para vincular a nota à transação financeira (boleto, Pix, TED). Os campos são preparatórios: o split payment está previsto para 2027.

### Prazos

- **Homologação (teste): desde 03/08/2026.** Grupo YC, regras de validação e evento 110300 disponíveis no ambiente de teste.
- **Produção: 05/10/2026.** Campos e evento disponíveis para todos os emissores, sem obrigatoriedade de preenchimento em 2026.

### O que muda na v1.00

#### 1. YC (gPgtoVinc) – Vinculação do pagamento na própria nota (Rejeições 215, 1273 e 1274)

Informar sempre que a transação de pagamento começar antes da emissão do DF-e (ex.: boleto ou QR Code Pix dinâmico gerado antes da nota), mesmo que ainda não esteja paga. Até 99 pagamentos por nota (grupo gPgto).

- Nº do pagamento: nPag (YC03)
- ID da transação, de 2 a 35 caracteres: idTransacao (YC04)
- Meio de pagamento: tpMeioPgto (YC05)
- CNPJ do recebedor: CNPJReceb (YC06)
- CNPJ base do PSP: CNPJBasePSP (YC07)

O recebedor pode ser diferente do fornecedor da nota (ex.: plataforma). O meio de pagamento segue a Tabela Nacional do Informe Técnico 2026.001. A rejeição 215 ocorre quando nPag ou idTransacao estão duplicados.

#### 2. Evento 110300 – Vinculação Pagamento após a autorização (Rejeições 466, 1273 e 1274)

Gerado pelo emitente para vincular uma transação financeira a uma nota já autorizada. Leva o protocolo da nota (nProt) e os mesmos dados do pagamento: idTransacao, tpMeioPgto, CNPJReceb e CNPJBasePSP.

Autor diferente de 1 = Empresa Emitente é rejeitado. O cancelamento usa o evento genérico 110001 (NT 2025.002-RTC).

### Quando usar cada um

- **Boleto antes da nota:** o boleto foi emitido sem a chave do DF-e. A nota sai depois já com os dados da transação. Use o grupo YC.
- **Pix depois da nota:** o QR Code Pix dinâmico foi gerado sem a chave da nota já emitida. Use o evento 110300.
- **TED com chave errada:** o adquirente pagou informando a chave do DF-e incorretamente. Use o evento 110300.

Quanto antes o vínculo for informado, maior a chance do split superinteligente. Sem ele, roda o split inteligente offline, com devolução do valor retido a maior em até 3 dias úteis.

### O que não muda

- O vínculo indica uma expectativa de pagamento, não um pagamento liquidado (ex.: boleto emitido e não pago).
- Os grupos YA (Pagamento) e YB (Intermediador) continuam obrigatórios conforme a legislação estadual.
- O evento 110300 não substitui o evento de Conciliação Financeira (ECONF, NT 2024.002).

### Calendário

- **03/08/2026 (homologação, v1.00):** grupo YC, regras YC03 a YC06 e evento 110300 em teste.
- **05/10/2026 (produção, v1.00):** campos e evento disponíveis, de uso opcional em 2026.
- **2027 (split payment):** ativação efetiva dos campos com a vigência do split payment. Cronograma a ser divulgado pelo CGIBS e pela RFB.

Fonte: NT 2026.006-RTC v1.00 – Portal Nacional da NF-e, publicada em 06/2026.
