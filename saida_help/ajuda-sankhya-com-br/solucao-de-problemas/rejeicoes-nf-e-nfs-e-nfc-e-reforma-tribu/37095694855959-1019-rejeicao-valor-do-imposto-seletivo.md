---
id: "37095694855959"
titulo: "1019 Rejeição: Valor do Imposto Seletivo difere do calculado [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37095694855959-1019-Rejei%C3%A7%C3%A3o-Valor-do-Imposto-Seletivo-difere-do-calculado-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-08-24T16:48:40Z"
rotulos: ["Produtos", "Configuração", "NF-e", "SEFAZ", "Impostos", "Artigo atualizado KCS", "Alíquotas de IBS", "Assistente de Configuração Integral da Reforma Tributária", "Valor do Imposto Seletivo", "Inconsistência no cálculo do Imposto Seletivo", "Alíquota (pIS) do Imposto Seletivo"]
---

# 1019 Rejeição: Valor do Imposto Seletivo difere do calculado [nItem: 999]

**MENSAGEM**

1019 Rejeição: Valor do Imposto Seletivo difere do calculado [nItem: 999]

**SITUAÇÃO**

A nota fiscal foi emitida com divergência no valor do Imposto Seletivo informado no documento, em relação ao valor esperado para o enquadramento aplicado, resultando na rejeição pelo sistema.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **''Produtos''** (Configurações » Cadastros » Produtos » Produtos) e verifique se o NCM está cadastrado corretamente, especialmente se o produto pertencer aos grupos sujeitos ao Imposto Seletivo (códigos 2401, 2402, 2403, 2404, 2203, 2204, 2205, 2206, 2208).

**(2)** Acesse a tela **''Assistente de Configuração Integral da Reforma Tributária''** (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária) e verifique as configurações do Imposto Seletivo para o produto em questão.

**(3)** Confira se o **"Código de situação tributária - CST"** do Imposto Seletivo está corretamente configurado para o produto e operação.

**(4)** Verifique se a **"Base de Cálculo"** (vBCIS) e a **"Alíquota"** (pIS) do Imposto Seletivo estão corretamente informadas.

**(5)** Certifique-se de que o cálculo do valor do Imposto Seletivo está seguindo a fórmula: **vIS = vBCIS \* (pIS / 100)**.

**(6)** Após realizar as correções necessárias, tente emitir a nota fiscal novamente.

**CAUSA**

A causa desta rejeição está relacionada à **inconsistência no cálculo do Imposto Seletivo**. De acordo com a regra de validação UB11-10 para os modelos 55/65, o valor do Imposto Seletivo (vIS) deve ser igual à Base de Cálculo (vBCIS) multiplicada pela Alíquota (pIS) dividida por 100.

Esta inconsistência pode ocorrer devido a:

- Erro na configuração da alíquota do Imposto Seletivo
- Erro no cálculo da base de cálculo do Imposto Seletivo
- Arredondamento incorreto dos valores
- Configuração inadequada do CST do Imposto Seletivo
- Falha na aplicação da fórmula de cálculo do Imposto Seletivo

A Lei Complementar 214 de 16 de janeiro de 2025, que implementa a Reforma Tributária, estabelece novas regras para o Imposto Seletivo, e o sistema precisa estar corretamente configurado para calcular este imposto de acordo com as normas vigentes.
