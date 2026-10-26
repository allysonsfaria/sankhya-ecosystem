---
id: "37097644139159"
titulo: "1118 Rejeição: Total de IBS e CBS informado indevidamente [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37097644139159-1118-Rejei%C3%A7%C3%A3o-Total-de-IBS-e-CBS-informado-indevidamente-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-23T13:11:54Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Passos para resolver", "Erro", "Como Resolver", "Reforma Tributária", "Tipo de Nota Fiscal de Débito", "Total de IBS e CBS", "NF-e e NFC-e", "IBS e CBS foi informado indevidamente para o CST"]
---

# 1118 Rejeição: Total de IBS e CBS informado indevidamente [nItem: 999]

**MENSAGEM**

1118 Rejeição: Total de IBS e CBS informado indevidamente [nItem: 999]

**SITUAÇÃO**

Ao tentar emitir uma Nota Fiscal Eletrônica (NF-e) ou Nota Fiscal de Consumidor Eletrônica (NFC-e), o sistema apresenta erro indicando que o total de IBS e CBS foi informado indevidamente para o CST utilizado.

**SOLUÇÃO**

**(1)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e verifique o CST do IBS/CBS utilizado na nota fiscal e confirme se ele permite a informação dos grupos de IBS e CBS.

**(2)** Caso o CST utilizado não permita a informação dos grupos de IBS e CBS, selecione um CST adequado para a operação:

- Escolha um CST que possua o indicador **"ind\_gIBSCBS = 1"** para permitir a informação dos grupos de IBS e CBS.

**(3)** Acesse a tela **''Tipos de Operação - TOP''** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

**(4)** Na aba **"NF-e/NFC-e/CF-e"**, verifique se a finalidade do campo **''NF-e''** está configurada corretamente. Caso a nota seja de débito, verifique o campo **''Tipo de Nota Fiscal de Débito''**.

**(5)** Acesse a tela **"Assistente de Configuração Integral da Reforma Tributária"** (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária) para configurar corretamente a tributação de IBS e CBS de acordo com o CST selecionado. 

**CAUSA**

Esta rejeição ocorre quando o CST do IBS/CBS informado na nota fiscal possui um indicador que **não permite** a informação dos grupos de IBS e CBS (ind\_gIBSCBS = 0), mas estes grupos foram indevidamente informados no documento fiscal.

Cada CST do IBS/CBS possui indicadores específicos que determinam quais grupos de informações podem ou devem ser preenchidos. Quando um CST com indicador ind\_gIBSCBS = 0 é utilizado, o sistema não deve informar os grupos de IBS e CBS no documento fiscal. Se estes grupos forem informados, a Sefaz rejeitará o documento com a mensagem 1118.

Esta validação faz parte das regras implementadas para a Reforma Tributária, conforme a Lei Complementar nº 214 de 16 de janeiro de 2025, que estabelece os novos impostos IBS (Imposto sobre Bens e Serviços) e CBS (Contribuição sobre Bens e Serviços).
