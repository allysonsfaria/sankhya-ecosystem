---
id: "360042637734"
titulo: "The value '0.00' of element 'pICMSInter' is not valid"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042637734-The-value-0-00-of-element-pICMSInter-is-not-valid"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:07:49Z"
rotulos: ["ERRONF", "CORE_E04895", "Alíquotas", "Configuração", "NF-e", "XML", "SEFAZ", "Impostos", "Valor '0.00' no Campo 'pICMSInter' Inválido"]
---

# The value '0.00' of element 'pICMSInter' is not valid

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16510625339927) MENSAGEM:**

[CORE\_E04895]  cvc-enumeration-valid: value '0.00' is not facet-valid with respect to enumeration '[4.00, 7.00, 12.00]'. it must be a value from the enumeration. cvc-type.3.1.3: the value '0.00' of element 'picmsinter' is not valid.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16510649167511) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse: Configurações » Avançado » Preferências](https://ajuda.sankhya.com.br/hc/article_attachments/16510649169815) Acesse: Configurações » Avançado » Preferências

Parâmetro: **"UFDESTNFEBENFIS - UFs destino NF-e com benefício fiscal para DIFAL"**

- No parâmetro **"UFDESTNFEBENFIS"** que por padrão é vazio, informe a sigla de cada UF da SEFAZ de destino (separada por vírgula); caso a SEFAZ de origem/destino estejam amparadas por benefícios fiscais, ou seja, a alíquota interestadual é igual a zero.

![Imagem 4: Acesse: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/article_attachments/16510649174423) Acesse: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS

Aba: **"Geral"**

- Campo "**Aliq. Interna Destino":** Alíquota interestadual deve ser igual a zero
- Campo "**Tributação**": CST's deverão estar configurados igual a 40, 41, 50, 51, ou 60.

Desta forma, o valor do DIFAL e do Fundo de Combate à Pobreza, não serão calculados quando o produto estiver com a alíquota interestadual igual a zero, e o "**Cód.Tributação(CST)**" for igual a 40, 41, 50, 51 ou 60, e a UF destino esteja no parâmetro **"UFDESTNFEBENFIS"**.

Não existindo o cálculo do DIFAL, o grupo <ICMSUFDest> não será gerado.

A geração do grupo <ICMSUFDest> no XML não foi alterada e sua premissa continua sendo a existência de valor em algum dos campos referentes ao DIFAL ou ao Fundo de Combate à Pobreza.

![Imagem 5: Após os ajustes, exclua a nota e fature ou crie uma nova nota, e posteriormente gere lote.](https://ajuda.sankhya.com.br/hc/article_attachments/16510649178391) Após os ajustes, exclua a nota e fature ou crie uma nova nota, e posteriormente gere lote.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16510649187863) CAUSA:**

SEFAZ que não exigir o DIFAL (grupo <ICMSUFDest>), devido às UF's origem/destino participarem de Protocolos ou Convênios que definem os benefícios fiscais tais como Isenção, por exemplo.
