---
id: "360063774353"
titulo: "Cupom Fiscal só pode ser cancelado pelo FastService"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360063774353-Cupom-Fiscal-s%C3%B3-pode-ser-cancelado-pelo-FastService"
trilha: "Solução de Problemas > Varejo"
atualizado_em: "2026-07-22T15:25:07Z"
rotulos: ["Configuração", "Fast Service", "TOP", "#validadoSilvio", "SAT", "CF-e só pode ser cancelado pelo FastService", "Altere a série se for NFC-e", "Use FastService para cancelamento", "Cupom Fiscal"]
---

# Cupom Fiscal só pode ser cancelado pelo FastService

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16334673448087) MENSAGEM:**

Cupom Fiscal só pode ser cancelado pelo FastService.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16334673449495) SOLUÇÃO:**

Para a resolução do incidente, siga os passos abaixo:

![Imagem 3: Acesse a configuração da TOP e verifique o controle de numeração;](https://ajuda.sankhya.com.br/hc/article_attachments/16334712060055) Acesse a configuração da TOP e verifique o controle de numeração;

![Imagem 4: Se estiver com série = CF, somente poderá ser cancelada pelo FastService, pois esta série é exclusiva de Cupom Fiscal.](https://ajuda.sankhya.com.br/hc/article_attachments/16334673451799) Se estiver com série = CF,  somente poderá ser cancelada pelo FastService, pois esta série é exclusiva de Cupom Fiscal.

![Imagem 5: Se for uma NFC-e, altere a série para a adequada.](https://ajuda.sankhya.com.br/hc/article_attachments/16334673452439) Se for uma NFC-e, altere a série para a adequada.

![Imagem 6: Verifique também se o cod.mod.doc esta = '59 - Cupom Fiscal Eletrônico'. Sendo que este modelo somente deverá ser usado…](https://ajuda.sankhya.com.br/hc/article_attachments/16334712065047) Verifique também se o cod.mod.doc esta = '59 - Cupom Fiscal Eletrônico'. Sendo que este modelo somente deverá ser usado em localidades que utilizam SAT e, com isso, somente será cancelado pelo Fast Service.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16334712065815) CAUSA:**

Esta validação ocorre em duas situações, se a série utilizada no lançamento for 'CF' ou for lançamento SAT onde na configuração da TOP o cod.mod.doc = 59.
