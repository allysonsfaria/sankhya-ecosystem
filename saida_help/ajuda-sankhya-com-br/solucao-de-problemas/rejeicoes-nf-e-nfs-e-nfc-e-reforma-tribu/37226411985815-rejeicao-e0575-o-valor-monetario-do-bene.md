---
id: "37226411985815"
titulo: "REJEIÇÃO E0575: O valor monetário do benefício municipal informado na DPS não pode reduzir o valor da BC de forma que resulte no valor do ISSQN a uma alíquota efetiva menor que 2%, exceto para os códigos relativos aos serviços 7.02, 7.05 e 16.01"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37226411985815-REJEI%C3%87%C3%83O-E0575-O-valor-monet%C3%A1rio-do-benef%C3%ADcio-municipal-informado-na-DPS-n%C3%A3o-pode-reduzir-o-valor-da-BC-de-forma-que-resulte-no-valor-do-ISSQN-a-uma-al%C3%ADquota-efetiva-menor-que-2-exceto-para-os-c%C3%B3digos-relativos-aos-servi%C3%A7os-7-02-7-05-e-16-01"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:14:59Z"
rotulos: ["Configuração", "Alíquota de ISS", "SEFAZ", "Impostos", "ISSQN", "Declaração de Prestação de Serviços (DPS)", "Benefício fiscal municipal", "Base de cálculo do ISSQN"]
---

# REJEIÇÃO E0575: O valor monetário do benefício municipal informado na DPS não pode reduzir o valor da BC de forma que resulte no valor do ISSQN a uma alíquota efetiva menor que 2%, exceto para os códigos relativos aos serviços 7.02, 7.05 e 16.01

**MENSAGEM**

E0575 Rejeição: O valor monetário do benefício municipal informado na DPS não pode reduzir o valor da BC de forma que resulte no valor do ISSQN a uma alíquota efetiva menor que 2%, exceto para os códigos relativos aos serviços 7.02, 7.05 e 16.01.

**SITUAÇÃO**

A **Declaração de Prestação de Serviços (DPS)** foi emitida com a informação de benefício fiscal municipal que reduz a base de cálculo do ISSQN, resultando em uma alíquota efetiva inferior ao valor aplicado para esse tipo de serviço no documento.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **''Produtos''** (Configurações » Cadastros » Produtos » Produtos) e confirme se o serviço está classificado com um dos códigos de exceção: **7.02**, **7.05** ou **16.01**.

- Se o serviço **não se enquadra** nas exceções, prossiga para o próximo passo.
- Se o serviço **se enquadra** nas exceções, a rejeição não deveria ocorrer. Verifique se o código foi informado corretamente no cadastro.

**(2)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquota de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

**(3)** Na aba **''Tributação''**, verifique o campo **''Código de Classificação Tributária''** informado, e verifique os valores configurados no campo **''% de Redução de Alíquota''**.

- Certifique-se de que o benefício fiscal aplicado **não reduza a Base de Cálculo** de forma que a alíquota efetiva do ISSQN fique abaixo de 2%.

**(4)** Calcule a **alíquota efetiva do ISSQN** após a aplicação do benefício fiscal. A fórmula é:

- Alíquota Efetiva = (Valor do ISSQN / Base de Cálculo Original) x 100
- Se a alíquota efetiva for **menor que 2%**, ajuste o valor do benefício fiscal para que a alíquota efetiva seja igual ou superior a 2%.

**(5)** Retorne ao passo 1 e ajuste o **valor do benefício fiscal municipal**, reduzindo o valor informado no campo **"Valor Monetário do Benefício Municipal"** para que a alíquota efetiva do ISSQN não seja inferior a 2%.

**(6)** Após realizar os ajustes necessários, emita novamente a **DPS** e verifique se a rejeição foi solucionada.

**(7)** Caso a rejeição persista, entre em contato com o **contador responsável** para revisar a aplicação dos benefícios fiscais municipais e garantir que estejam em conformidade com a legislação vigente.

**CAUSA**

A rejeição ocorre porque a **Sefaz valida** que o valor monetário do benefício fiscal municipal informado na DPS **não pode reduzir a Base de Cálculo do ISSQN** de forma que resulte em uma **alíquota efetiva inferior a 2%**. Esta regra visa garantir uma **tributação mínima** sobre os serviços prestados, exceto para os serviços específicos com códigos **7.02**, **7.05** e **16.01**, que possuem tratamento diferenciado conforme a **Lei Complementar nº 214/2025** e a regulamentação da Reforma Tributária.
