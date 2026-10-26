---
id: "360044510933"
titulo: "Folha anterior ao período de obrigatoriedade não envia pensão no S-1210?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044510933-Folha-anterior-ao-per%C3%ADodo-de-obrigatoriedade-n%C3%A3o-envia-pens%C3%A3o-no-S-1210"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-08-11T14:16:14Z"
rotulos: ["XML", "Dependentes", "eSocial", "Folha de Pagamento", "Pensão Alimentícia", "Evento S-1210", "Informações ausentes", "Comportamento do sistema", "S-1210"]
---

# Folha anterior ao período de obrigatoriedade não envia pensão no S-1210?

Evento S-1210 não apresenta no XML de envio as informações de dependentes pensionistas quando a folha é anterior ao início da obrigatoriedade do eSocial.

Conforme possível analisar no manual do eSocial, temos as tags de envio de pensionistas ao eSocial por meio do evento S-1210.

No entanto, é de se observar que para pagamentos onde **não** ocorre envio de **S-1200** (onde as rubricas são declaradas no grupo detPgtoAnt) não existe a declaração da tag **penAlim.** Sendo assim, o comportamento do sistema ao gerar o evento S-1210 está correto.
