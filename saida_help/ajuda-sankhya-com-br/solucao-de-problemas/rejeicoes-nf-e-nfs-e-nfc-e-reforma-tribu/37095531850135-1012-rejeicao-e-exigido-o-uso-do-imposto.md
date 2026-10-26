---
id: "37095531850135"
titulo: "1012 Rejeição: É exigido o uso do Imposto Seletivo para esta classificação da operação [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37095531850135-1012-Rejei%C3%A7%C3%A3o-%C3%89-exigido-o-uso-do-Imposto-Seletivo-para-esta-classifica%C3%A7%C3%A3o-da-opera%C3%A7%C3%A3o-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:21:40Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "TOP", "Código de Situação Tributária", "Assistente de Configuração da Tributação integral IBS e CBS (Reforma Tributária)", "Classificação tributária do Imposto Seletivo (cClassTribIS)", "(cClassTribIS)", "Imposto Seletivo (IS)", "Ausência do grupo de Imposto Seletivo (IS)"]
---

# 1012 Rejeição: É exigido o uso do Imposto Seletivo para esta classificação da operação [nItem: 999]

**MENSAGEM**

1012 Rejeição: É exigido o uso do Imposto Seletivo para esta classificação da operação [nItem: 999]

**SITUAÇÃO**

O documento fiscal foi emitido com uma classificação tributária do Imposto Seletivo que prevê o preenchimento do grupo de Imposto Seletivo, sem que esse grupo tenha sido informado no documento.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela [**"Tipos de Operação - TOP"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e selecione o TOP utilizado na operação que gerou a rejeição.

**(2)** Na aba **"NF-e/NFC-e/CF-e"**, verifique se a classificação tributária do Imposto Seletivo (cClassTribIS) está configurada corretamente para a operação.

**(3)** Acesse a tela **"Produtos"** (Configurações » Cadastros » Produtos » Produtos) e verifique se o produto possui configuração adequada para o Imposto Seletivo.

**(4)** Acesse o **"Assistente de Configuração da Tributação integral IBS e CBS (Reforma Tributária)"** (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária) e configure as alíquotas do Imposto Seletivo para o produto e operação em questão.

**(5)** Certifique-se de que o **"Código de Situação Tributária - CST"** do Imposto Seletivo esteja configurado corretamente para a operação.

**(6)** Verifique se a **"Base de Cálculo"** e a **"Alíquota"** do Imposto Seletivo estão preenchidas corretamente.

**(7)** Após realizar as configurações necessárias, tente emitir o documento fiscal novamente. 

**CAUSA**

A rejeição 1012 ocorre devido à **ausência do grupo de Imposto Seletivo** (IS) no documento fiscal, quando este é obrigatório para a classificação tributária informada. De acordo com a regra de validação UB01-20 da Sefaz, determinadas classificações tributárias do Imposto Seletivo (cClassTribIS) exigem obrigatoriamente a informação do grupo IS no documento fiscal.

Esta exigência está relacionada à implementação da Reforma Tributária, conforme a Lei Complementar nº 214 de 16 de janeiro de 2025, que estabelece o Imposto Seletivo como um dos novos tributos do sistema tributário brasileiro. O Imposto Seletivo incide sobre produtos específicos, como aqueles prejudiciais à saúde e ao meio ambiente, e sua correta informação no documento fiscal é obrigatória para determinadas classificações tributárias.
