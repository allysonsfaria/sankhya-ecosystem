---
id: "37141359895063"
titulo: "1013 Rejeição: É exigido o uso do Imposto Seletivo para esta classificação da operação para este NCM [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37141359895063-1013-Rejei%C3%A7%C3%A3o-%C3%89-exigido-o-uso-do-Imposto-Seletivo-para-esta-classifica%C3%A7%C3%A3o-da-opera%C3%A7%C3%A3o-para-este-NCM-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:19:36Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "NCM", "Reforma Tributária", "Imposto Seletivo (IS)", "Tributação do Imposto Seletivo", "NCMs específicos"]
---

# 1013 Rejeição: É exigido o uso do Imposto Seletivo para esta classificação da operação para este NCM [nItem: 999]

**MENSAGEM**

1013 Rejeição: É exigido o uso do Imposto Seletivo para esta classificação da operação para este NCM [nItem: 999]

**SITUAÇÃO**

Ao tentar emitir uma Nota Fiscal Eletrônica (NF-e) ou Nota Fiscal de Consumidor Eletrônica (NFC-e) contendo produtos com NCM específicos que exigem a tributação do Imposto Seletivo, o documento foi rejeitado pela SEFAZ porque não foi informado o grupo de tributação do Imposto Seletivo para o item.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **''Produtos''** (Configurações » Cadastros » Produtos » Produtos) e verifique se o NCM do produto está correto. Alguns NCMs específicos exigem obrigatoriamente a tributação do Imposto Seletivo.

**(2)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e verifique se existe uma alíquota configurada para o Imposto Seletivo (IS) para o NCM do produto em questão.

**(3)** Caso não exista, crie uma nova alíquota clicando no botão **"Incluir"** e preencha os seguintes campos:

- Selecione o **"Tipo de Imposto"** como **"IS - Imposto Seletivo"**
- Informe o **"NCM"** do produto
- Selecione o **"CST do IS"** adequado para a operação
- Informe a **"Classificação Tributária do IS"** (cClassTribIS) apropriada
- Preencha a **"Alíquota do IS"** (pIS) conforme a legislação
- Se aplicável, preencha a **"Alíquota Específica do IS"** (pISEspec)
- Informe a **"Unidade Tributável"** (uTrib) e **"Quantidade Tributável"** (qTrib) quando necessário

**(4)** Acesse a tela **"Tipo de Operação"** (Fiscal » Cadastros » Tipo de Operação) e verifique se o tipo de operação utilizado está configurado corretamente para calcular o Imposto Seletivo.

**(5)** Na aba **"Impostos"** do tipo de operação, certifique-se de que a opção **"Calcular IS"** esteja habilitada.

**(6)** Gere novamente a nota fiscal para que o sistema calcule automaticamente o Imposto Seletivo com base nas configurações realizadas.

**CAUSA**

Esta rejeição ocorre devido à implementação da Reforma Tributária (Lei Complementar nº 214/2025), que criou o Imposto Seletivo (IS). Determinados produtos, identificados por NCMs específicos (como bebidas alcoólicas, tabaco e seus derivados), exigem obrigatoriamente a tributação do Imposto Seletivo. Quando um documento fiscal é emitido contendo um produto com NCM que exige o IS, mas o grupo de tributação do Imposto Seletivo não é informado, a SEFAZ rejeita o documento.

A regra de validação UB01-30 da SEFAZ determina que é exigido o uso do Imposto Seletivo (grupo: imposto/IS) para determinados NCMs, conforme estabelecido na legislação da Reforma Tributária. Os NCMs que geralmente exigem o Imposto Seletivo incluem produtos como tabaco (2401, 2402, 2403, 2404) e bebidas alcoólicas (2203, 2204, 2205, 2206, 2208), entre outros.
