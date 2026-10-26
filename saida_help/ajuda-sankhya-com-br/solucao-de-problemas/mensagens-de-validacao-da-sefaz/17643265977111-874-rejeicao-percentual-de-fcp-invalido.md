---
id: "17643265977111"
titulo: "874 Rejeição: Percentual de FCP inválido [nItem: xxxxx]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/17643265977111-874-Rejei%C3%A7%C3%A3o-Percentual-de-FCP-inv%C3%A1lido-nItem-xxxxx"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T14:53:10Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "ICMS", "Impostos", "Rejeição 874", "Percentual de FCP", "NF-e NFC-e", "Regra de validação"]
---

# 874 Rejeição: Percentual de FCP inválido [nItem: xxxxx]

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/17643213023511) **MENSAGEM:**

 [874 - Rejeição: Percentual de FCP inválido [nItem: xxxxx]]

![Imagem 2: (874 - Rejeição: Percentual de FCP inválido (nItem: xxxxx))](https://ajuda.sankhya.com.br/hc/article_attachments/17623554531095)

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17643265966359)SOLUÇÃO:**

Regra de Validação da Sefaz

![Imagem 4: Regra de Validação da Sefaz](https://www.oobj.com.br/bc/assets/Articles/783/RV874_1.60.PNG)

Para emissão de NF-e com FCP (Fundo de Combate à Pobreza)

![Imagem 5: Acesse: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/article_attachments/17643260138263) Acesse: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS

Pesquise pela regra de ICMS que incidiu nos itens da nota e  ajuste o campo "**% ICMS FCP**", de acordo com as orientações do contador, que por sua vez irá alimentar as TAG's <pFCP> e <vFCP>.

Para facilitar a busca pela exceção de ICMS utilizada em cada item/lançamento verifique o conteúdo: [Como identificar qual a alíquota/exceção de ICMS utilizada no lançamento?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043874154-Como-identificar-qual-a-al%C3%ADquota-exce%C3%A7%C3%A3o-de-ICMS-utilizada-no-lan%C3%A7amento-)

[GIF animado: Imagem 6: Para facilitar a busca pela exceção de ICMS utilizada em cada item/lançamento verifique o conteúdo: Como identificar…](https://ajuda.sankhya.com.br/hc/article_attachments/17643586355863)

**![Imagem 7: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17677151744535) OBSERVAÇÃO:**

Para essa Regra de Validação não há exceções. Sempre que preenchido o campo pFCP, a alíquota informada deve ser o percentual igual permitido para o estado emissor, conforme tabela divulgada pela [Sefaz](http://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=Iy/5Qol1YbE=).

Segue a baixo como identificar o percentual correto para a UF da empresa emitente, conforme site da SEFAZ, [clique aqui](http://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=/NJarYc9nus=).

[GIF animado: Imagem 8: Segue a baixo como identificar o percentual correto para a UF da empresa emitente, conforme site da SEFAZ, clique aqui .](https://ajuda.sankhya.com.br/hc/article_attachments/17643213028375)

![Imagem 9: Após os ajustes, inutilize a numeração da NF-e atual e refaça o faturamento.](https://ajuda.sankhya.com.br/hc/article_attachments/17643228418583) Após os ajustes, inutilize a numeração da NF-e atual e refaça o faturamento.

**![Imagem 10: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17643213032599)CAUSA:**

Quando for emitida uma NF-e (modelo 55) ou NFC-e (modelo 65) e no campo referente ao percentual de FCP campo "**% ICMS FCP**", for informado um valor divergente ao percentual correspondente ao permitido no estado emissor, haverá a rejeição.

**![Imagem 11: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17677151744535) OBSERVAÇÃO:**

[**(NT2016.002)**](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=Y6Lj7G0uHwc=) - Nota Técnica - v 1.60
