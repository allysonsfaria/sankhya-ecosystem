---
id: "360043129093"
titulo: "Valor total do ICMS Interestadual da UF de destino difere do somatório dos itens"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043129093-Valor-total-do-ICMS-Interestadual-da-UF-de-destino-difere-do-somat%C3%B3rio-dos-itens"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:07:05Z"
rotulos: ["ERRONF", "Configuração", "NF-e", "XML", "SEFAZ", "ICMS", "Impostos", "TOP", "799", "Diferença no Valor Total do ICMS Interestadual", "Artigo atualizado KCS", "Docs Eletrônicos - KCS"]
---

# Valor total do ICMS Interestadual da UF de destino difere do somatório dos itens

**Mensagem**

799 - Rejeição: Valor total do ICMS interestadual da uf de destino difere do somatório dos itens.

**Situação**

Esta rejeição ocorre ao tentar emitir uma **"Nota Fiscal Eletrônica (NF-e)"** em operações interestaduais, especialmente em notas de devolução ou vendas para consumidor final não contribuinte de outro estado. O sistema identifica que a tag **"vICMSUFDest"** no XML da nota está ausente, sem valor, ou que o valor total do difal não corresponde ao somatório dos itens.

**Solução**

Para resolver a rejeição 799, siga os passos abaixo:

**(1)** Acesse a tela **"Tipos de Operação"** (Comercial >> Arquivo >> Cadastros).

**(2)** Localize e selecione a **"TOP"** utilizada na nota fiscal que está sendo rejeitada e acesse a aba **"Impostos"**.

**(3)** Marque a opção **"Calcular DIFAL Partilhado"** para que o sistema preencha corretamente a tag **"vICMSUFDest"** no XML.

![Imagem 1: (1) Acesse a tela "Tipos de Operação" (Comercial >> Arquivo >> Cadastros). (2) Localize e selecione a "TOP" utilizada…](https://ajuda.sankhya.com.br/hc/article_attachments/12120275876631)

**(4)** Salve as alterações, inutilize e exclua a nota fiscal rejeitada e realize uma nova emissão.

**Análise detalhada (se o problema persistir):**

Caso a configuração esteja correta e a divergência persista, verifique a integridade dos valores:

**(1)** No Portal de Vendas, clique no botão **"NF-e"** e selecione **"Gerar XML da NF-e em arquivo para conferência"**.

**(2)** Abra o XML em um editor de texto.

**(3)** Some o valor da tag **"vICMSUFDest"** de cada item (nItem).

**(4)** Verifique se a soma é igual ao valor da tag **"vICMSUFDest"** contida no grupo **"total"**.

![Exemplo XML](https://ajuda.sankhya.com.br/hc/article_attachments/360059969754)

Se houver divergência entre o total e a soma dos itens, revise os valores de difal da nota com apoio de seu contador.

**Observações importantes:**

• Esta configuração é essencial para operações interestaduais quando o parceiro destinatário está classificado como **"Consumidor Final Não Contribuinte"**.
• Em notas de devolução, certifique-se de que a **"TOP"** de devolução também esteja com a opção **"Calcular DIFAL Partilhado"** marcada, caso a nota de origem possuísse a tag preenchida.

**Causa**

A rejeição 799 ocorre porque a tag **"vICMSUFDest"** não está sendo enviada ou apresenta um valor divergente do somatório dos itens no XML. Isso acontece geralmente pela ausência da parametrização **"Calcular DIFAL Partilhado"** na **"TOP"**, ou por inconsistências nos cálculos dos itens da nota fiscal.
