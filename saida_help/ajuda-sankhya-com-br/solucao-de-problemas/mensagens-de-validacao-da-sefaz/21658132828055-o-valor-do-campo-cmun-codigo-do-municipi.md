---
id: "21658132828055"
titulo: "O valor do campo cMun (Código do Município de Incidência do Imposto) informado não é valido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/21658132828055-O-valor-do-campo-cMun-C%C3%B3digo-do-Munic%C3%ADpio-de-Incid%C3%AAncia-do-Imposto-informado-n%C3%A3o-%C3%A9-valido"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T14:49:57Z"
rotulos: ["Configuração", "NF-e", "Cidades", "XML", "SEFAZ", "Impostos"]
---

# O valor do campo cMun (Código do Município de Incidência do Imposto) informado não é valido

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/21658136919447) **MENSAGEM:**

 O valor do campo cMun (Código do Município de Incidência do Imposto) informado não é valido.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/21658132819607)CAUSA:**

Quando for emitida uma NF-e e o Código do Município do Fiscal(Mun. domicílio fiscal) informado no cadastro da cidade estiver em branco ou incorreto de acordo com IBGE será retornado à rejeição.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/21658136920855)SOLUÇÃO:**

![Imagem 4: No portal de vendas/compras selecione a nota com a rejeição e gere o XML em conferência igual na imagem abaixo.](https://ajuda.sankhya.com.br/hc/article_attachments/21675505509271) No portal de vendas/compras selecione a nota com a rejeição e gere o XML em conferência igual na imagem abaixo.

![Imagem 5: No portal de vendas/compras selecione a nota com a rejeição e gere o XML em conferência igual na imagem abaixo.](https://ajuda.sankhya.com.br/hc/article_attachments/21675537204759)

![Imagem 6: Feito isso abra o arquivo XML no navegador ou bloco de notas e procure pelo texto cmun conforme print abaixo.](https://ajuda.sankhya.com.br/hc/article_attachments/21675505525271) Feito isso abra o arquivo XML no navegador ou bloco de notas e procure pelo texto cmun conforme print abaixo.

![Imagem 7: Feito isso abra o arquivo XML no navegador ou bloco de notas e procure pelo texto cmun conforme print abaixo.](https://ajuda.sankhya.com.br/hc/article_attachments/21675537217047)

Após identificar a quem se refere o cadastro divergente faça a consulta do código IBGE correspondente e ajuste no cadastro de cidades, redigitar o parceiro/empresa na central  e reenviar o documento.

- Consultas do Código do Município, segue endereço do site do IBGE: [IBGE | Portal do IBGE | IBGE](http://www.ibge.gov.br/home/geociencias/areaterritorial/area.shtm)
