---
id: "360043195373"
titulo: "Operação interestadual para Consumidor Final e valor do FCP informado em campo diferente de vFCPUFDest [nItem:nnn]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043195373-Opera%C3%A7%C3%A3o-interestadual-para-Consumidor-Final-e-valor-do-FCP-informado-em-campo-diferente-de-vFCPUFDest-nItem-nnn"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:06:51Z"
rotulos: ["ERRONF", "#criadoRoger", "Configuração", "NF-e", "SEFAZ", "ICMS", "Impostos", "876", "Rejeição por Valor FCP Incorreto", "Documentos Eletrônicos"]
---

# Operação interestadual para Consumidor Final e valor do FCP informado em campo diferente de vFCPUFDest [nItem:nnn]

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16511832333719) MENSAGEM:**

[876 - Rejeição]: Operação interestadual para Consumidor Final e valor do FCP informado em campo diferente de vFCPUFDest [nItem:nnn]

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16511856856727) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/article_attachments/16511832338071) Acesse: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS

Pesquise pela regra de ICMS que incidiu nos itens da nota e  ajuste o campo "**Aliq. Interna Destino"**, de acordo com as orientações do Contador.

Para facilitar a busca pela exceção de ICMS utilizada em cada item/lançamento verifique o conteúdo [Como identificar qual a alíquota/exceção de ICMS utilizada no lançamento?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043874154-Como-identificar-qual-a-al%C3%ADquota-exce%C3%A7%C3%A3o-de-ICMS-utilizada-no-lan%C3%A7amento-)

![Imagem 4: Após os ajustes, inutilize a numeração da NF-e atual e refaça o faturamento.](https://ajuda.sankhya.com.br/hc/article_attachments/16511856879767) Após os ajustes, inutilize a numeração da NF-e atual e refaça o faturamento.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16511832344599) CAUSA:**

Quando for emitida uma NF-e (modelo 55) interestadual (Campo: idDest = 2) para Consumidor Final (Campo: indFinal = 1) não contribuinte (Campo: indIEDest = 9) e o valor do FCP for informado em um campo diferente de vFCPUFDest, haverá a rejeição
