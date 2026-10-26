---
id: "360042625734"
titulo: "Total do Frete difere do somatório dos itens (NT2009/005)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042625734-Total-do-Frete-difere-do-somat%C3%B3rio-dos-itens-NT2009-005"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-09-10T19:05:03Z"
rotulos: ["ERRONF", "Configuração", "NF-e", "SEFAZ", "Impostos", "TOP", "535", "Divergência no Total do Frete"]
---

# Total do Frete difere do somatório dos itens (NT2009/005)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16484807188375) MENSAGEM:**

[535 - Rejeição]: Total do Frete difere do somatório dos itens. (NT2009/005).

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16484807192983) SOLUÇÃO:**

![Imagem 3: Acesse a tela " Tipos de Operação - TOP " ( Comercial » Arquivo » Cadastros )](https://ajuda.sankhya.com.br/hc/article_attachments/16484768003991) Acesse a tela **"[Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)"**  (Comercial » Arquivo » Cadastros)

![Imagem 4: Selecione a TOP que está sendo utilizada na emissão e verifique as configurações da aba "Despesas Acessórias" , que…](https://ajuda.sankhya.com.br/hc/article_attachments/16484807203223) Selecione a TOP que está sendo utilizada na emissão e verifique as configurações da aba **"Despesas Acessórias"**, que deverão seguir as seguintes configurações:

- **ICMS proporcional ao ICMS dos itens :**ICMS proporcional para frete [MARCADO]
- **PIS proporcional ao PIS dos itens:** PIS proporcional para frete [MARCADO]
- **IPI proporcional ao IPI dos itens:** IPI proporcional para frete [MARCADO]
- **COFINS proporcional ao COFINS dos itens:** COFINS proporcional para frete [MARCADO]
- **S.T. proporcional ao S.T. dos itens:**ST proporcional para frete [MARCADO]

![Imagem 5: Os ajustes nesta aba são históricos, então inutilize a nota rejeitada e realize um novo faturamento.](https://ajuda.sankhya.com.br/hc/article_attachments/16484768009879) Os ajustes nesta aba são históricos, então inutilize a nota rejeitada e realize um novo faturamento.

**![Imagem 6: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16484807209239) OBSERVAÇÃO:**

| Para clientes que utilizam MGE/G1 a marcação deverá ser realizada utilizando a opção:   - Calcular ICMS dos itens ? Para FRETE : **"Somente para os itens com ICMS"** - Calcular IPI dos itens ? Para FRETE:  **"Somente para os itens com IPI"** - Calcular PIS dos itens ? Para FRETE: **"Somente para os itens com PIS"** - Calcular COFINS dos itens? Para FRETE: **"Somente para os itens com COFINS"** - Calcular Substituição Tributária dos itens: **"Somente para os itens com S.T"** |
| --- |

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16484807217559)CAUSA:**

Quando for emitida uma NF-e (modelo 55) ou NFC-e (modelo 65) com o Total do Frete da NF-e  diferente do somatório do Valor do Frete de cada item, será retornada a rejeição.

**![Imagem 8: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16484807209239) OBSERVAÇÃO:**

([NT2009/005](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=EZA0oy86tPY=)) - Nota Técnica.
