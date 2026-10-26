---
id: "360042634594"
titulo: "Data de Saída menor que a Data de Emissão"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042634594-Data-de-Sa%C3%ADda-menor-que-a-Data-de-Emiss%C3%A3o"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:07:55Z"
rotulos: ["ERRONF", "Configuração", "NF-e", "XML", "SEFAZ", "506", "Saída menor que Emissão", "Ajustar data de Saída no XML", "Data de Saída inadequada", "Erro", "Documentos Eletrônicos"]
---

# Data de Saída menor que a Data de Emissão

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16484286670359) **MENSAGEM:**

[506 - Rejeição]: Data de Saída menor que a Data de Emissão.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16484286686359) SOLUÇÃO:**

![Imagem 3: Analise o XML de Conferência (Caminho de acesso: Portal de Vendas » Botão NF-e » Gerar XML de NF-e em arquivo para…](https://ajuda.sankhya.com.br/hc/article_attachments/16484264098583) Analise o XML de Conferência (Caminho de acesso: Portal de Vendas » Botão NF-e » Gerar XML de NF-e em arquivo para Conferência).

**Exemplo:**

- Foi emitida uma NF-e com a data de emissão "11-09-2018" e com a data de Saída ou Entrada "10-09-2018". Nessa situação a NF-e será rejeitada pelo motivo 506.

Indevido:
<dhEmi>2018-09-11T00:00:00-03:00</dhEmi>
<dhSaiEnt>2018-09-10T00:00:00-03:00</dhSaiEnt>

**Informe a Data de Saída igual ou maior a Data de Emissão da NF-e.** A NF-e deverá ser corrigida como no exemplo abaixo:

Correto:
<dhEmi>2018-09-11T00:00:00-03:00</dhEmi>
<dhSaiEnt>2018-09-11T00:00:00-03:00</dhSaiEnt>

![Imagem 4: Ajuste o campo " Dh Saida" , para que fique igual ou maior que a Data de Emissão da NF-e.](https://ajuda.sankhya.com.br/hc/article_attachments/16484286690967) Ajuste o campo "**Dh Saida"**, para que fique igual ou maior que a Data de Emissão da NF-e.

![Imagem 5: Após os ajustes, gerar lote novamente da NF-e.](https://ajuda.sankhya.com.br/hc/article_attachments/16484264108183) Após os ajustes, gerar lote novamente da NF-e.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16484264109975) CAUSA:**

A rejeição retorna quando for emitida uma NF-e e a Data de Saída ou Entrada for menor que a Data de Emissão da NF-e.
