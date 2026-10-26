---
id: "37225536255255"
titulo: "E0447 Rejeição: O valor de dedução/redução informado na DPS não pode reduzir o valor da BC de forma que resulte no valor do ISSQN a uma alíquota efetiva menor que 2%, exceto para os códigos relativos aos serviços 7.02, 7.05 e 16.01."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37225536255255-E0447-Rejei%C3%A7%C3%A3o-O-valor-de-dedu%C3%A7%C3%A3o-redu%C3%A7%C3%A3o-informado-na-DPS-n%C3%A3o-pode-reduzir-o-valor-da-BC-de-forma-que-resulte-no-valor-do-ISSQN-a-uma-al%C3%ADquota-efetiva-menor-que-2-exceto-para-os-c%C3%B3digos-relativos-aos-servi%C3%A7os-7-02-7-05-e-16-01"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:15:54Z"
rotulos: ["Configuração", "Alíquota de ISS", "SEFAZ", "Impostos", "ISSQN", "Declaração de Prestação de Serviços (DPS)", "Valores de dedução ou redução", "Valor de dedução/redução informado na DPS", "Alíquota mínima de 2% para o ISSQN", "Base de cálculo do ISSQN", "Legislação tributária"]
---

# E0447 Rejeição: O valor de dedução/redução informado na DPS não pode reduzir o valor da BC de forma que resulte no valor do ISSQN a uma alíquota efetiva menor que 2%, exceto para os códigos relativos aos serviços 7.02, 7.05 e 16.01.

**MENSAGEM**

E0447 Rejeição: O valor de dedução/redução informado na DPS não pode reduzir o valor da BC de forma que resulte no valor do ISSQN a uma alíquota efetiva menor que 2%, exceto para os códigos relativos aos serviços 7.02, 7.05 e 16.01.

**SITUAÇÃO**

Ao emitir uma **Declaração de Prestação de Serviços (DPS)**, o sistema retornou uma rejeição relacionada aos **valores de dedução ou redução da base de cálculo do ISSQN** informados no documento.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

**(2)** Localize a alíquota configurada para o serviço que está sendo prestado.

**(3)** Verifique se o serviço prestado está enquadrado nos **códigos 7.02, 7.05 ou 16.01**.

- Caso esteja, a dedução/redução pode resultar em alíquota efetiva inferior a 2%.

**(4)** Caso o serviço **não esteja enquadrado** nos códigos de exceção, revise os valores informados nos campos de **dedução ou redução da base de cálculo do ISSQN** na DPS.

**(5)** Recalcule a **alíquota efetiva** aplicando a seguinte fórmula:

```
Alíquota Efetiva = (Valor do ISSQN / Base de Cálculo após deduções) × 100
```

**(6)** Certifique-se de que a **alíquota efetiva resultante seja igual ou superior a 2%**. Caso seja inferior, ajuste os valores de dedução/redução para que a alíquota mínima seja respeitada.

**(6)** Após realizar os ajustes necessários, **reemita a DPS** com os valores corrigidos.

**CAUSA**

A rejeição ocorre porque a **legislação tributária estabelece uma alíquota mínima de 2% para o ISSQN**, visando garantir uma arrecadação mínima aos municípios. Quando são aplicadas **deduções ou reduções excessivas na base de cálculo**, a alíquota efetiva pode ficar abaixo deste patamar, violando a regra de validação da Sefaz. As exceções previstas para os **serviços 7.02, 7.05 e 16.01** são estabelecidas por legislação específica que permite tratamento diferenciado para essas atividades.
