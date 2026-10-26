---
id: "37226421941143"
titulo: "E0574 Rejeição: O valor monetário do benefício municipal informado na DPS não pode ser superior ao valor do serviço."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37226421941143-E0574-Rejei%C3%A7%C3%A3o-O-valor-monet%C3%A1rio-do-benef%C3%ADcio-municipal-informado-na-DPS-n%C3%A3o-pode-ser-superior-ao-valor-do-servi%C3%A7o"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:15:00Z"
rotulos: ["Configuração", "SEFAZ", "Prefeituras", "NFS-e", "Valor do serviço", "valor total do serviço prestado", "Benefício Municipal", "DPS (Declaração de Prestação de Serviços)", "valor de benefício fiscal municipal", "Valor monetário do benefício municipal", "Valor Monetário"]
---

# E0574 Rejeição: O valor monetário do benefício municipal informado na DPS não pode ser superior ao valor do serviço.

**MENSAGEM**

E0574 Rejeição: O valor monetário do benefício municipal informado na DPS não pode ser superior ao valor do serviço.

**SITUAÇÃO**

Rejeição apresentada na emissão de uma NFS-e quando a DPS é informada com um benefício fiscal municipal cujo valor monetário é maior que o valor total do serviço declarado.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **''Portal de Vendas''** (Comercial » Consulta » Portal de Vendas) e localize a nota fiscal que está sendo rejeitada.

- Ao selecionar a nota fiscal, ela será aberta automaticamente, direcionando o usuário para a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas).

**(2)** Na grade **''Rodapé''**, na aba **''Totais''**, verifique o campo **''Valor do serviço''** informando o valor total do serviço na nota fiscal.

**(3)** Verifique o **valor monetário do benefício municipal** que está sendo informado na DPS e certifique-se de que este valor **não seja superior ao valor do serviço**.

**(4)** Caso o valor do benefício esteja incorreto, ajuste-o para um valor **igual ou inferior ao valor do serviço** prestado.

**(5)** Revise as **configurações de benefícios fiscais municipais** cadastradas no sistema para garantir que estejam corretas e de acordo com a legislação municipal vigente.

**(6)** Após realizar os ajustes necessários, tente **emitir novamente a NFS-e**.

**CAUSA**

A rejeição ocorre porque foi informado um **valor de benefício fiscal municipal** que **excede o valor total do serviço** prestado. A Sefaz possui uma regra de validação que impede que o benefício fiscal seja maior do que a base de cálculo sobre a qual ele incide, garantindo a **consistência tributária** e evitando inconsistências nos valores declarados na DPS.
