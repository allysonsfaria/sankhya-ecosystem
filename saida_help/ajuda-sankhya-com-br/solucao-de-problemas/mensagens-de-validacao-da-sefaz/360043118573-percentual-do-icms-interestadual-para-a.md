---
id: "360043118573"
titulo: "Percentual do ICMS Interestadual para a UF de destino difere do previsto para o ano da Data de Emissão [nItem:999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043118573-Percentual-do-ICMS-Interestadual-para-a-UF-de-destino-difere-do-previsto-para-o-ano-da-Data-de-Emiss%C3%A3o-nItem-999"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:07:34Z"
rotulos: ["ERRONF", "Alíquotas", "Configuração", "NF-e", "SEFAZ", "ICMS", "Impostos", "699", "Percentual ICMS Interestadual Divergente"]
---

# Percentual do ICMS Interestadual para a UF de destino difere do previsto para o ano da Data de Emissão [nItem:999]

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16085859414935) MENSAGEM:**

699-Rejeição: Percentual do ICMS Interestadual para a UF de destino difere do previsto para o ano da Data de Emissão [nItem:999]

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16085859420439) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse: Configurações » Cadastros » Partilhas DIFAL](https://ajuda.sankhya.com.br/hc/article_attachments/16085859421591) Acesse: Configurações » Cadastros » Partilhas DIFAL

Crie um novo registro para NF-e's, considerando o ano base atual. Considere o exemplo abaixo:

- Data Inicio Partilha = 01/01/2019
- Percentual de Partilha DIFAL = 100%

![Imagem 4: Percentual de Partilha DIFAL = 100%](https://ajuda.sankhya.com.br/hc/article_attachments/12099641779863)

![Imagem 5: Após os ajustes, exclua a nota e fature a novamente, ou redigite o item na nota e gere novo lote.](https://ajuda.sankhya.com.br/hc/article_attachments/16085874240791) Após os ajustes, exclua a nota e fature a novamente, ou redigite o item na nota e gere novo lote.

**Importante:**

Valide o percentual correto junto ao seu Contador, visto que trata-se de um percentual Nacional, não levando em consideração possíveis especificações do seu Estado/Empresa.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16085859430807) CAUSA:**

Quando for emitida uma NF-e com o Percentual do ICMS Interestadual para a UF de Destino (pICMSInterPart) diferente do previsto para o Ano da Data de Emissão do documento, será retornada a rejeição.

Os percentuais de ICMS Interestadual para a UF de destino serão:

- 40% em 2016;
- 60% em 2017;
- 80% em 2018;
- 100% a partir de **2019**.

**![Imagem 7: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16085874259735) OBSERVAÇÃO:**

**1-Nota Técnica (NT2017.002)**

<http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=Yy9URkJxo5s=>
