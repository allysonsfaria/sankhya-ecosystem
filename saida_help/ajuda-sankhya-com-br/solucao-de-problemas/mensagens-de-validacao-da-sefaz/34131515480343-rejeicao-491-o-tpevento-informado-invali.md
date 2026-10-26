---
id: "34131515480343"
titulo: "Rejeição 491: O tpEvento informado inválido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34131515480343-Rejei%C3%A7%C3%A3o-491-O-tpEvento-informado-inv%C3%A1lido"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T14:27:38Z"
rotulos: ["Eventos", "EPEC", "NF-e", "XML", "SEFAZ", "Cancelamento", "Manifestação do Destinatário", "Rejeição", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Rejeição 491: O tpEvento informado inválido", "O tpEvento informado inválido", "tpEvento", "layout definido pela Sefaz", "110110 – Carta de Correção Eletrônica (CC-e)", "210200 – Confirmação da Operação (Manifestação do Destinatário)", "210210 – Ciência da Operação", "210220 – Desconhecimento da Operação", "Rejeição 491", "tentar enviar um evento relacionado à NF-e", "Carta de Correção", "110111 – Cancelamento da NF-e", "110140 – EPEC (Evento Prévio de Emissão em Contingência)", "210240 – Operação não Realizada"]
---

# Rejeição 491: O tpEvento informado inválido

**MENSAGEM**

Rejeição 491: O tpEvento informado inválido.

**SITUAÇÃO**

A mensagem ocorre ao tentar enviar um evento relacionado à NF-e, como **"Carta de Correção"**, **"Cancelamento"**, **"EPEC"** ou **"Manifestação do Destinatário"**, quando o campo **"tpEvento"** informado no XML não é reconhecido ou não corresponde a nenhum código válido segundo o layout definido pela Sefaz.

**SOLUÇÃO**

**(1)**  Verifique o código informado no campo **"tpEvento"** no XML do evento.

**(2)**  Consulte a tabela oficial de códigos de evento da Sefaz e confirme se o código utilizado é válido.

- **110110** – Carta de Correção Eletrônica (CC-e)
- **110111** – Cancelamento da NF-e
- **110140** – EPEC (Evento Prévio de Emissão em Contingência)
- **210200** – Confirmação da Operação (Manifestação do Destinatário)
- **210210** – Ciência da Operação
- **210220** – Desconhecimento da Operação
- **210240** – Operação não Realizada

**(3)**  Se necessário, corrija o código do evento no XML e tente reenviar o evento.

**(4)**  Caso a rejeição persista, entre em contato com o suporte **"Sankhya"** para orientações adicionais.

**CAUSA**

A rejeição 491 é causada pelo envio de um código de evento (**tpEvento**) inválido ou incompatível com a tabela oficial da Sefaz.
