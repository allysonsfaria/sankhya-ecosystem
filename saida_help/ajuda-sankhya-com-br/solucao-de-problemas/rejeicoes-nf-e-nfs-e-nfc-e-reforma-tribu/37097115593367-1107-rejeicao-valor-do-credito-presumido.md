---
id: "37097115593367"
titulo: "1107 Rejeição: Valor do Crédito Presumido do IBS não pode ser superior a vProd [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37097115593367-1107-Rejei%C3%A7%C3%A3o-Valor-do-Cr%C3%A9dito-Presumido-do-IBS-n%C3%A3o-pode-ser-superior-a-vProd-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:20:54Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Crédito", "Impostos", "Passos para resolver", "Erro", "Como Resolver", "Alíquotas de CBS", "Alíquotas de IBS", "Valor do Crédito Presumido", "Crédito Presumido do IBS", "Código de classificação do crédito presumido"]
---

# 1107 Rejeição: Valor do Crédito Presumido do IBS não pode ser superior a vProd [nItem: 999]

**MENSAGEM**

1107 Rejeição: Valor do Crédito Presumido do IBS não pode ser superior a vProd [nItem: 999]

**SITUAÇÃO**

Ao emitr a nota fiscal o valor do Crédito Presumido do IBS informado na NF-e é superior ao valor do produto (**vProd**) no item correspondente, em operação de aquisição de bens móveis de pessoa física não contribuinte para revenda.

**SOLUÇÃO**

**(1)** Acesse a tela de **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e verifique se o tipo de operação utilizado está configurado corretamente para operações com bens móveis usados de pessoa física não contribuinte.

**(2)** Na aba **"NF-e/NFC-e/CF-e"**, verifique se o campo **"NF-e''** está configurado como **"Normal"** (para emissão de nota de entrada própria, visto que a Pessoa Física não contribuinte não emite NF-e) ou **"Terceiros"** (caso a entrada seja apenas escritural).

**(3)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e verifique se o percentual do crédito presumido está configurado corretamente para a operação.

**(4)** Ao emitir a nota fiscal, certifique-se de que o valor do crédito presumido do IBS (**vCredPres**) não ultrapasse o valor do produto (**vProd**). Ajuste o valor do crédito presumido para que seja igual ou inferior ao valor do produto.

**(5)** Caso esteja utilizando o **"Assistente de Configuração da Tributação integral IBS e CBS"** (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária), verifique se as configurações para crédito presumido estão corretas para operações com bens móveis usados.

**CAUSA**

A rejeição ocorre devido à regra de validação UB76-20 (para o IBS) e UB129-10 (para a CBS) da Sefaz, que estabelece que, quando o código de classificação do crédito presumido for **"4-Aquisição de bens móveis de PF não contrib. para revenda"**, o valor do crédito presumido não pode ser superior ao valor do produto (vProd).

Esta regra é específica para operações de aquisição de bens móveis usados de pessoa física não contribuinte para revenda, como veículos usados ou itens de brechó, onde o crédito presumido tem um tratamento diferenciado em relação às demais operações, conforme previsto na Lei Complementar 214/2025.
