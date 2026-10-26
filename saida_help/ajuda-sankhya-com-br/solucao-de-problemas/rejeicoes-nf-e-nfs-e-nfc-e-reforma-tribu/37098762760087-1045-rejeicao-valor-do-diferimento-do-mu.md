---
id: "37098762760087"
titulo: "1045 Rejeição: Valor do Diferimento do Município difere do calculado [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37098762760087-1045-Rejei%C3%A7%C3%A3o-Valor-do-Diferimento-do-Munic%C3%ADpio-difere-do-calculado-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:20:10Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "TOP", "Código de Situação Tributária", "Alíquotas de CBS", "Alíquotas de IBS", "Assistente de Configuração Integral da Reforma Tributária", "Divergência no cálculo do valor do diferimento municipal"]
---

# 1045 Rejeição: Valor do Diferimento do Município difere do calculado [nItem: 999]

**MENSAGEM**

1045 Rejeição: Valor do Diferimento do Município difere do calculado [nItem: 999]

**SITUAÇÃO**

A nota fiscal eletrônica foi emitida com divergência no valor do diferimento do imposto municipal informado no documento, resultando na rejeição durante o processamento fiscal.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

**(2)** Verifique se o tipo de operação utilizado na nota está configurado corretamente para o cálculo do diferimento municipal.

**(3)** Na aba **"NF-e/NFC-e/CF-e"**, verifique se as configurações de tributação estão de acordo com as regras da Reforma Tributária para o diferimento municipal.

**(4)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

**(5)** Verifique se o percentual de diferimento municipal está configurado corretamente para o item que apresentou a rejeição.

**(6)** Verifique se o **"Código de Situação Tributária" (CST)** utilizado é compatível com a operação de diferimento municipal. Certifique-se de que o CST selecionado permite o diferimento do imposto municipal.

**(7)** Acesse a tela **''Assistente de Configuração Integral da Reforma Tributária''** (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária), revise e ajuste as configurações de tributação relacionadas ao diferimento municipal.

**(8)** Após realizar as correções necessárias, emita novamente a nota fiscal para verificar se a rejeição foi solucionada.

 **CAUSA**

A rejeição ocorre devido a uma **divergência no cálculo do valor do diferimento municipal** entre o informado na nota fiscal e o calculado pela Sefaz. Esta divergência pode ser causada por:

- Configuração incorreta das alíquotas de IBS e CBS relacionadas ao diferimento municipal;
- Utilização de CST incompatível com operações de diferimento;
- Erro na fórmula de cálculo do diferimento municipal aplicada pelo sistema;
- Alterações nas regras de cálculo conforme a NT 2020.005, que modificou a forma de calcular o diferimento, passando a utilizar o cálculo por dentro e com base dupla.
