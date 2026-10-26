---
id: "360043111813"
titulo: "NFC-e com contingência off-line para a UF"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043111813-NFC-e-com-conting%C3%AAncia-off-line-para-a-UF"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:07:57Z"
rotulos: ["ERRONF", "Configuração", "Fast Service", "SEFAZ", "Contingência", "Preferências", "NFC-e", "712", "Rejeição 712: NFC-e com Contingência Off-line Não Aceita pela UF"]
---

# NFC-e com contingência off-line para a UF

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16482905813015) MENSAGEM:**

[712-Rejeição]: NFC-e com contingência off-line para a UF.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16482928023575) SOLUÇÃO:**

Considere o Comportamento da Aplicação, conforme abaixo:

Algumas Secretarias (SEFAZ) estaduais não aceitam esse tipo de contingência. A Sefaz de São Paulo é um exemplo, a UF não aceita a contingência off-line.

Para que não ocorra a mensagem, siga as instruções abaixo:

![Imagem 3: Acesse: Comercial » Preferências » Empresa](https://ajuda.sankhya.com.br/hc/article_attachments/16482905818647) Acesse: Comercial » Preferências » Empresa

- Aba: **"NF-e/NFC-e"**
- NFC-e Campo **"Envio em Contingência":** Não usar contingência

![Imagem 4: NFC-e Campo "Envio em Contingência": Não usar contingência](https://ajuda.sankhya.com.br/hc/article_attachments/14536890184855)

![Imagem 5: Após o ajuste, inutilize a numeração das notas emitidas que estão com a rejeição acima e efetue um novo lançamento no…](https://ajuda.sankhya.com.br/hc/article_attachments/16482928027159) Após o ajuste, inutilize a numeração das notas emitidas que estão com a rejeição acima e efetue um novo lançamento no ambiente, fora da contingência.

**![Imagem 6: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16482928029591) OBSERVAÇÃO:**

Para emitir NFC-e em modo contingência para essas UFs que rejeitam, somente se faz através do FastService (PDV) com a integração do SAT.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16482905826199) CAUSA:**

Quando for emitida uma NFC-e em contingência "9 - off-line" e a UF autorizadora não aceitar esse tipo de contingência, será retornado a rejeição.
