---
id: "360043128313"
titulo: " Não informada vBCSTRet, pST, vICMSSubstituto e vICMSSTRet [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043128313--N%C3%A3o-informada-vBCSTRet-pST-vICMSSubstituto-e-vICMSSTRet-nItem-999"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:07:08Z"
rotulos: ["ERRONF", "Configuração", "NF-e", "SEFAZ", "Impostos", "Estoque", "938", "Procedimento de correção: Configurações Atualização Parâmetros", "Causa da rejeição: Tributação NF-e Operações", "Rejeição por dados ausentes: vBCSTRet pST vICMSSubstituto", "Erro"]
---

#  Não informada vBCSTRet, pST, vICMSSubstituto e vICMSSTRet [nItem: 999]

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16487925063575) MENSAGEM:**

[938 - Rejeição]: Não informada vBCSTRet, pST, vICMSSubstituto e vICMSSTRet [nItem: 999]

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16487925065495) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse: Comercial » Preferências » Empresa](https://ajuda.sankhya.com.br/hc/article_attachments/16487925066263) Acesse: Comercial » Preferências » Empresa

Aba: **"NF-e/NFC-e"**

Campo **"Versão NT"**: Última (Nota Técnica 2018.005)

![Imagem 4: Acesse: Configurações » Avançado » Preferências](https://ajuda.sankhya.com.br/hc/article_attachments/16487896838935) Acesse: Configurações » Avançado » Preferências

Parâmetro **"DATINIULTNTNFE-Data Início da última nota técnica da NF-e ":** 06/05/2019

![Imagem 5: Vale destacar que o seu sistema deve estar atualizado em versões iguais ou superiores aos releases abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/16487896849559) Vale destacar que o seu sistema deve estar atualizado em versões iguais ou superiores aos releases abaixo:

- 3.30b58 [Release]
- 3.29b220 [Release]
- 3.28b383 [Release]

Tal atualização evitará a rejeição: 'cvc-complex-type.2.4.a: Invalid content was found starting with element 'vICMSSubstituto'.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16487925077015) CAUSA:**

Quando for emitida uma NF-e (modelo 55) com produto tributado pelo **ICMS 60** ou **CSOSN 500,**para operações que **não** sejam para consumidor final, haverá a rejeição.

**![Imagem 7: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/17874173999511) IMPORTANTE:**

- Alinhe com seu Contador detalhes referente tal rejeição, para que esse lhe oriente à respeito do 'Rastreamento de Estoque' (ST).
- O sistema Sankhya já está preparado para essa rotina, e caso sua empresa enquadre-se nessa necessidade, um consultor de sua Filial poderá ser acionado para configurações e validações.
- Para maiores detalhes: [Rastreamento de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594854)
