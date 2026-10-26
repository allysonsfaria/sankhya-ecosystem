---
id: "37096416738199"
titulo: "1062 Rejeição: Valor do Diferimento da CBS difere do calculado [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37096416738199-1062-Rejei%C3%A7%C3%A3o-Valor-do-Diferimento-da-CBS-difere-do-calculado-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:21:22Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Erro", "Alíquotas de CBS", "Diferimento da CBS (vDif) não corresponde ao valor calculado", "Percentual do Diferimento", "Valor do Diferimento da CBS", "Cálculo do valor do diferimento da CBS", "Regra de validação UB61-10", "Base de Cálculo pelo Percentual da CBS"]
---

# 1062 Rejeição: Valor do Diferimento da CBS difere do calculado [nItem: 999]

**MENSAGEM**

1062 Rejeição: Valor do Diferimento da CBS difere do calculado [nItem: 999]

**SITUAÇÃO**

O documento fiscal foi emitido com divergência no valor do diferimento da CBS informado, em relação ao valor esperado para esse enquadramento no documento, resultando na rejeição pelo sistema.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e verifique se o CST configurado para a CBS exige diferimento.

**(2)** Acesse as telas **''Assistente de Configuração Integral da Reforma Tributária''** (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária) e verifique se o CST configurado para o CBS possui o indicador que exige o uso de diferimento (ind\_gDif = 1).

**(3)** Verifique os valores informados nos seguintes campos:

- Base de Cálculo da CBS (vBC);
- Percentual da CBS (pCBS);
- Percentual do Diferimento (pDif);
- Valor do Diferimento (vDif).

**(4)** Recalcule o valor do diferimento utilizando a fórmula:

```
vDif = vBC x (pCBS / 100) x (pDif / 100).
```

**(5)** Corrija o valor do diferimento (vDif) no documento fiscal para que corresponda exatamente ao resultado da fórmula, considerando as regras de arredondamento estabelecidas pela legislação.

**(6)** Verifique se o sistema está calculando corretamente o valor do diferimento conforme a fórmula estabelecida pela Sefaz.

**(7)** Após realizar as correções necessárias, tente emitir o documento fiscal novamente.

**CAUSA**

A rejeição ocorre devido a uma **inconsistência no cálculo do valor do diferimento da CBS**. Conforme a regra de validação UB61-10, quando informado o grupo do Diferimento (gCBS/gDif), o valor do diferimento (vDif) deve ser calculado pela fórmula: vDif = vBC x (pCBS / 100) x (pDif / 100).

Esta validação é aplicada quando o CST da CBS possui indicador que exige o uso de diferimento (ind\_gDif = 1) e o grupo de diferimento foi informado. O erro pode ocorrer por diversos motivos, como:

- Erro no cálculo manual do valor do diferimento
- Problemas na configuração do sistema para o cálculo automático
- Arredondamento incorreto dos valores Inconsistência entre os valores da base de cálculo, percentual da CBS ou percentual do diferimento

É importante ressaltar que esta validação faz parte das regras estabelecidas para a implementação da Reforma Tributária, conforme a Lei Complementar 214/2025, que institui a Contribuição sobre Bens e Serviços (CBS).
