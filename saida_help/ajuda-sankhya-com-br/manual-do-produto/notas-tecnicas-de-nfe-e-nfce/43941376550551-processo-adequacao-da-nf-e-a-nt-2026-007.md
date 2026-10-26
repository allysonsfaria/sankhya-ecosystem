---
id: "43941376550551"
titulo: "Processo Adequação da NF-e à NT 2026.007 · v1.10 - (em análise)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43941376550551-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2026-007-v1-10-em-an%C3%A1lise"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Notas Técnicas  > Notas Técnicas de NFe e NFCe"
atualizado_em: "2026-10-14T12:36:07Z"
---

# Processo Adequação da NF-e à NT 2026.007 · v1.10 - (em análise)

![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/44059866606999)

## NT 2026.007 v1.10 – Emissão de NF-e por contribuinte exclusivo do IBS/CBS (sem Inscrição Estadual)

Radar Fiscal NF-e / NFC-e. Nota técnica publicada no Portal Nacional da NF-e em 09/2026. NF-e sem Inscrição Estadual (IE) para quem não é contribuinte do ICMS, com autorização na SVRS, e novas validações cadastrais na Lista Centralizada de Contribuintes da RFB (LCC-RFB). A v1.10 ajusta regras para viabilizar testes em homologação.

### Prazos

- **Homologação (teste): até 26/10/2026 (prorrogada; antes, 05/10/2026).** Ajustes da v1.10 disponíveis no ambiente de teste. As regras da v1.00 estão em teste desde 01/09/2026.
- **Produção: 16/11/2026 (prorrogada; antes, 03/11/2026).** Emissão sem IE e validações na LCC-RFB e no CCC passam a valer para todos os emissores.

### O que muda na v1.10

#### 1. LCC-RFB – Base de produção também em homologação (Rejeições 178 a 180, 187 e 170)

As validações na LCC-RFB passam a usar sempre a base de Produção, mesmo nos Web Services de Homologação.

Para emitente e autor de evento (12C02-10, 12C02-20, 12C21-20, 1P10-30, 1P10-32), a homologação não rejeita quando o CNPJ é de teste no CCC (indContribTeste = 1). Isso permite testes em qualquer UF.

#### 2. 12E02, 12F02 e 12G02 – Destinatário, retirada e entrega (Rejeições 181 a 186)

Em homologação, as regras -10 e -20 de destinatário, local de retirada e local de entrega não rejeitam CNPJ alfanumérico, permitindo testes com UF diferente da que consta na LCC-RFB.

Também foi corrigida a regra 1C17-04 e melhorada a redação da C17-20.

### Escopo da NT

#### 3. emit/IE – Emitente sem IE: contribuinte exclusivo do IBS/CBS (Rejeições 166, 156 e 188)

O campo C17 passa a ser opcional (0-1). É contribuinte exclusivo quem não informa a IE, tem CNPJ ativo na RFB e não possui IE de ICMS habilitada no CCC.

- Autorização somente na SVRS, inclusive dos eventos do emitente.
- Proibido emitir NFC-e até 2033; CNPJ obrigatório e IEST proibida.

#### 4. N01-10, UB12-11 e I08-191 – Tributos e CFOP sem IE (Rejeições 161, 162 e 159)

Na NF-e sem IE, é proibido informar ICMS e ICMSUFDest, o grupo IBSCBS é obrigatório e o CFOP deve estar na tabela de CFOP permitidos (coluna indExcIBSCBS). Devolução e tpNFCredito = 03 ficam fora das regras de ICMS e CFOP.

### Calendário

- **01/09/2026 (homologação, v1.00):** emissão sem IE, autorização na SVRS e validações na LCC-RFB e no CCC.
- **26/10/2026 (homologação, v1.10):** LCC-RFB de produção em homologação; exceções para CNPJ de teste e CNPJ alfanumérico.
- **16/11/2026 (produção, v1.00 e v1.10):** todas as regras da NT valendo para os emissores.

Fonte: NT 2026.007 v1.10 – Portal Nacional da NF-e, publicada em 09/2026.
