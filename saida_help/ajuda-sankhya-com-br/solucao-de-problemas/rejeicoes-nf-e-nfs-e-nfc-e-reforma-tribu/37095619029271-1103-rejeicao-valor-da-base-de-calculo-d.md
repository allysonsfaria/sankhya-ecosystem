---
id: "37095619029271"
titulo: "1103 Rejeição: Valor da Base de cálculo do Imposto Seletivo difere do somatório dos valores que a compõem [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37095619029271-1103-Rejei%C3%A7%C3%A3o-Valor-da-Base-de-c%C3%A1lculo-do-Imposto-Seletivo-difere-do-somat%C3%B3rio-dos-valores-que-a-comp%C3%B5em-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:21:39Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Erro", "Alíquotas de IBS", "Imposto Seletivo", "Base de cáculo do Imposto Seletivo", "Alíquotas do Imposto Seletivo", "CST do Imposto Seletivo"]
---

# 1103 Rejeição: Valor da Base de cálculo do Imposto Seletivo difere do somatório dos valores que a compõem [nItem: 999]

**MENSAGEM**

1103 Rejeição: Valor da Base de cálculo do Imposto Seletivo difere do somatório dos valores que a compõem [nItem: 999]

**SITUAÇÃO**

Ao emitir uma nota o **valor total da Base de Cálculo do Imposto Seletivo (IS) informado no documento fiscal não corresponde ao somatório correto dos valores que compõem esta base de cálculo**, conforme as regras estabelecidas pela Lei Complementar 214/2025. O sistema identifica uma inconsistência entre o valor total da base de cálculo do IS declarado e o valor que deveria ser calculado com base nos componentes individuais dos itens.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Verifique a configuração do **"Imposto Seletivo"** nos cadastros de produtos afetados, certificando-se que a **"Classificação Tributária do Imposto Seletivo"** está corretamente definida para cada item.

**(2)** Acesse a tela **"Produtos"** (Configurações » Cadastros » Produtos » Produtos) e verifique se os produtos sujeitos ao Imposto Seletivo estão com a classificação correta.

**(3)** Acesse a tela **''Alíquotas de IS''** (Livros Fiscais » Cadastros » Aliquotas de IS) e certifique-se que as configurações estão de acordo com a legislação vigente.

**(4)** Verifique se o **"CST do Imposto Seletivo"** está configurado corretamente para cada item da nota fiscal, conforme a operação realizada.

**(5)** Revise os valores que compõem a base de cálculo do Imposto Seletivo, considerando:

- Valor do produto Valor do frete
- Valor do seguro
- Valor de outras despesas
- Descontos aplicados.

**(6)** Recalcule manualmente a base de cálculo do Imposto Seletivo para cada item e compare com o valor total informado no documento fiscal.

**(7)** Corrija os valores divergentes e reenvie o documento fiscal para processamento.

**CAUSA**

Esta rejeição ocorre devido à implementação das novas regras tributárias estabelecidas pela Lei Complementar 214/2025, que institui o Imposto Seletivo como parte da Reforma Tributária. Quando o sistema da Sefaz verifica o documento fiscal, ele realiza uma validação (regra UB05-10) que compara o valor total da Base de Cálculo do Imposto Seletivo informado com o somatório dos valores que devem compor esta base conforme a legislação.

A divergência pode ocorrer por diversos motivos, como:

- Erro no cálculo automático do sistema
- Configuração incorreta das alíquotas do Imposto Seletivo
- Classificação tributária do Imposto Seletivo inadequada para o produto Inconsistência nos valores que compõem a base de cálculo
- Arredondamentos incorretos nos cálculos dos valores

É importante ressaltar que esta validação está marcada como "Implementação Futura" nos documentos da Sefaz, o que indica que entrará em vigor conforme o cronograma de implementação da Reforma Tributária.
