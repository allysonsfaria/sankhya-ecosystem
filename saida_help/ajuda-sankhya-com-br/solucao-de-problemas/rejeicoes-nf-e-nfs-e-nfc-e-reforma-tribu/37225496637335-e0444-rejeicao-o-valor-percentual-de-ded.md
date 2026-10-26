---
id: "37225496637335"
titulo: "E0444 Rejeição: O valor percentual de dedução/redução informado na DPS não pode reduzir o valor da BC de forma que resulte no valor do ISSQN a uma alíquota efetiva menor que 2%, exceto para os códigos relativos aos serviços 7.02, 7.05 e 16.01."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37225496637335-E0444-Rejei%C3%A7%C3%A3o-O-valor-percentual-de-dedu%C3%A7%C3%A3o-redu%C3%A7%C3%A3o-informado-na-DPS-n%C3%A3o-pode-reduzir-o-valor-da-BC-de-forma-que-resulte-no-valor-do-ISSQN-a-uma-al%C3%ADquota-efetiva-menor-que-2-exceto-para-os-c%C3%B3digos-relativos-aos-servi%C3%A7os-7-02-7-05-e-16-01"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:15:56Z"
rotulos: ["Configuração", "Alíquota de ISS", "SEFAZ", "Impostos", "ISSQN", "Declaração de Prestação de Serviços (DPS)", "Percentual de dedução ou redução", "Base de Cálculo do ISSQN", "Sefaz valida que a alíquota efetiva do ISSQN", "Arrecadação mínima do imposto municipal"]
---

# E0444 Rejeição: O valor percentual de dedução/redução informado na DPS não pode reduzir o valor da BC de forma que resulte no valor do ISSQN a uma alíquota efetiva menor que 2%, exceto para os códigos relativos aos serviços 7.02, 7.05 e 16.01.

**MENSAGEM**

E0444 Rejeição: O valor percentual de dedução/redução informado na DPS não pode reduzir o valor da BC de forma que resulte no valor do ISSQN a uma alíquota efetiva menor que 2%, exceto para os códigos relativos aos serviços 7.02, 7.05 e 16.01.

**SITUAÇÃO**

Ao emitir uma **Declaração de Prestação de Serviços (DPS)**, o sistema retornou a rejeição **E0444**, relacionada ao **percentual de dedução ou redução da Base de Cálculo do ISSQN** informado no documento.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquota de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

**(2)** Localize o cadastro da alíquota utilizada na operação que gerou a rejeição.

**(3)** Verifique o **percentual de redução da Base de Cálculo do ISSQN** informado no cadastro da alíquota.

**(4)** Calcule a **alíquota efetiva** resultante da aplicação do percentual de redução, utilizando a fórmula:

```
Alíquota Efetiva = (Base de Cálculo Reduzida / Base de Cálculo Original) × Alíquota do ISSQN
```

**(5)** Certifique-se de que a **alíquota efetiva resultante seja igual ou superior a 2%**. Caso contrário, ajuste o percentual de redução da Base de Cálculo para que a alíquota efetiva não fique abaixo deste limite.

**(6)** Se o serviço prestado corresponder aos **códigos 7.02, 7.05 ou 16.01**, verifique se o código de serviço está corretamente informado na DPS, pois estes são exceções à regra e podem ter alíquota efetiva inferior a 2%.

**(7)** Após realizar os ajustes necessários, **reemita a DPS** com as informações corrigidas.

**CAUSA**

A rejeição ocorre porque a **Sefaz valida que a alíquota efetiva do ISSQN**, após a aplicação de deduções ou reduções na Base de Cálculo, **não pode ser inferior a 2%**, conforme estabelecido pela legislação tributária. Esta regra visa garantir uma **arrecadação mínima do imposto municipal** sobre serviços. A exceção aplica-se apenas aos serviços com códigos **7.02, 7.05 e 16.01**, que possuem tratamento tributário diferenciado. Quando o sistema identifica que o percentual de dedução/redução informado resulta em uma alíquota efetiva abaixo do limite estabelecido, e o serviço não está entre as exceções, a DPS é rejeitada com a mensagem **E0444**.
