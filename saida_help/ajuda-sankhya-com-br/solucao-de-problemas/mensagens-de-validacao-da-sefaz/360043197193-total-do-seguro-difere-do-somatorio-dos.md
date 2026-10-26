---
id: "360043197193"
titulo: "Total do Seguro difere do somatório dos itens"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043197193-Total-do-Seguro-difere-do-somat%C3%B3rio-dos-itens"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:06:44Z"
rotulos: ["ERRONF", "Configuração", "NF-e", "SEFAZ", "Impostos", "TOP", "536", "Divergência no Total do Seguro", "Erro"]
---

# Total do Seguro difere do somatório dos itens

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16451904036759) MENSAGEM:**

[536-Rejeição]: Total do Seguro difere do somatório dos itens.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16451904041879) SOLUÇÃO:**

Para correção siga os passos abaixo:

![Imagem 3: Acesse: " Tipos de Operação - TOP " (Caminho de acesso: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP )](https://ajuda.sankhya.com.br/hc/article_attachments/16451919071511) Acesse: "**[Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)"** (Caminho de acesso: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP)

- Aba: "**Despesas Acessórias"**

**"ICMS proporcional ao ICMS dos itens"**
Marque todas as opções

**"PIS proporcional ao PIS dos itens"**
Marque todas as opções

**"IPI proporcional ao IPI dos itens"**
Marque todas as opções

**"COFINS proporcional ao COFINS dos itens"**
Marque todas as opções

**"S.T. proporcional ao S.T. dos itens"**
Marque todas as opções

![Imagem 4: Realizados os ajustes acima inutilize a NF-e rejeitada, proceda com sua exclusão e realize um novo lançamento.](https://ajuda.sankhya.com.br/hc/article_attachments/16451919075863) Realizados os ajustes acima inutilize a NF-e rejeitada, proceda com sua exclusão e realize um novo lançamento.

![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16451904057495) **CAUSA:**

Quando for emitida uma NF-e ou NFC-e com o Total do Seguro da NF-e  diferente do somatório do Valor do Seguro  de cada item, será retornado a rejeição.
