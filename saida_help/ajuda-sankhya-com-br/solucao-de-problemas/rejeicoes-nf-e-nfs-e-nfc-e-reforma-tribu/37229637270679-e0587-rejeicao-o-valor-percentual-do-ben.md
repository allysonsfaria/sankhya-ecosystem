---
id: "37229637270679"
titulo: "E0587 Rejeição: O valor percentual do benefício municipal informado na DPS não pode reduzir o valor da BC de forma que resulte no valor do ISSQN a uma alíquota efetiva menor que 2%, exceto para os códigos relativos aos serviços 7.02, 7.05 e 16.01."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37229637270679-E0587-Rejei%C3%A7%C3%A3o-O-valor-percentual-do-benef%C3%ADcio-municipal-informado-na-DPS-n%C3%A3o-pode-reduzir-o-valor-da-BC-de-forma-que-resulte-no-valor-do-ISSQN-a-uma-al%C3%ADquota-efetiva-menor-que-2-exceto-para-os-c%C3%B3digos-relativos-aos-servi%C3%A7os-7-02-7-05-e-16-01"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:13:48Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "ISSQN", "Legislação tributária", "Alíquota Efetiva", "NF-e ou NFC-e com tributação de IBS Municipal", "Percentual de redução da base de cálculo", "Alíquota efetiva do ISSQN"]
---

# E0587 Rejeição: O valor percentual do benefício municipal informado na DPS não pode reduzir o valor da BC de forma que resulte no valor do ISSQN a uma alíquota efetiva menor que 2%, exceto para os códigos relativos aos serviços 7.02, 7.05 e 16.01.

**MENSAGEM**

E0587 Rejeição: O valor percentual do benefício municipal informado na DPS não pode reduzir o valor da BC de forma que resulte no valor do ISSQN a uma alíquota efetiva menor que 2%, exceto para os códigos relativos aos serviços 7.02, 7.05 e 16.01.

**SITUAÇÃO**

Ao emitir uma NF-e ou NFC-e com tributação de IBS Municipal, a nota é **rejeitada pela Sefaz** quando a alíquota efetiva do ISSQN calculada fica abaixo de 2%, exceto para os serviços com códigos 7.02, 7.05 ou 16.01.

**SOLUÇÃO**

**(1)** Acesse as telas **''Aliquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Aliquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

**(2)** Localize a alíquota configurada para o produto/serviço que está gerando a rejeição.

**(3)** Na aba **''Tributação''** no campo **"Código de situação tributária - CST"**, verifique o código configurado e identifique se há **benefício fiscal municipal** aplicado.

**(3)** Ainda na mesma aba revise os seguintes campos:

- **"Percentual de Redução (Gov)":** pRedAliqIbsMun
- **"Alíquota do IBS do Município":** pIBSMun
- ##### "Percentual da Alíquota Efetiva": pAliqEfet

**(4)** Calcule a **alíquota efetiva** após aplicar o benefício fiscal municipal utilizando a seguinte fórmula:

```
Alíquota Efetiva = (Base de Cálculo × Alíquota Municipal × (1 - Percentual de Redução)) / Base de Cálculo
```

**(5)** Certifique-se de que a **alíquota efetiva calculada** não seja inferior a **2%**, **exceto** se o serviço prestado estiver classificado com os códigos **7.02, 7.05 ou 16.01**.

**(6)** Se a **alíquota efetiva** estiver abaixo de 2% e o serviço **não se enquadrar nas exceções**, ajuste o campo **Percentual de Redução (Gov)** para garantir que a alíquota efetiva fique **igual ou superior a 2%**.

**(7)** Salve todas as alterações.

**(8)** Reemita o documento fiscal para que as novas configurações sejam aplicadas e a validação da SEFAZ seja atendida.

**CAUSA**

A rejeição ocorre porque a **legislação tributária estabelece um limite mínimo de 2%** para a alíquota efetiva do ISSQN após a aplicação de benefícios fiscais municipais. Quando o **percentual de redução da base de cálculo** configurado no sistema resulta em uma alíquota efetiva inferior a este limite, a Sefaz rejeita o documento fiscal para garantir o cumprimento da norma. As exceções previstas para os serviços com códigos 7.02, 7.05 e 16.01 permitem alíquotas efetivas menores, conforme regulamentação específica.
