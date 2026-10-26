---
id: "39388748986775"
titulo: "Como funciona o cálculo do INSS quando há férias e folha mensal na mesma competência?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39388748986775-Como-funciona-o-c%C3%A1lculo-do-INSS-quando-h%C3%A1-f%C3%A9rias-e-folha-mensal-na-mesma-compet%C3%AAncia"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-08-27T18:25:50Z"
rotulos: ["Cálculo", "Impostos", "Folha", "INSS", "eSocial", "Férias", "Artigo criado KCS", "Sankhya RH - KCS"]
---

# Como funciona o cálculo do INSS quando há férias e folha mensal na mesma competência?

Quando um colaborador possui **cálculo de férias e folha mensal na mesma competência**, o sistema realiza automaticamente o **cálculo proporcional do INSS descontado nas férias** em relação à quantidade de dias. Esse processo pode gerar diferenças aparentes entre os valores da folha de pagamento e do eSocial, mas que na verdade estão corretos quando analisados em conjunto.

Este artigo explica o **funcionamento do cálculo proporcional** e como interpretar corretamente os valores apresentados no sistema e no eSocial, evitando confusões sobre possíveis divergências.

### Cálculo do INSS nas Férias

No cálculo de férias, o sistema considera a **"base 1926"** para apurar o desconto de INSS. Por exemplo, se a base for de **"R$ 7.871,87"**, o desconto de INSS apurado será de **"R$ 911,64"**.

Este valor é calculado normalmente conforme as **faixas progressivas da tabela de INSS** vigente e enviado ao eSocial através do evento **"S-1200"** referente às férias.

### Cálculo Proporcional na Folha Mensal

Ao calcular a **"folha mensal"** (Pessoal+ » Rotinas Folha » Cálculos) do mesmo colaborador, o sistema realiza o **cálculo proporcional do INSS descontado nas férias** em relação à quantidade de dias de férias na competência.

**Exemplo de cálculo proporcional:**

Se o INSS das férias foi de **"R$ 911,64"** e o colaborador teve **"14 dias de férias"** na competência, o cálculo será:

- R$ 911,64 ÷ 30 dias = **"R$ 30,388"** (valor diário)
- R$ 30,388 × 14 dias = **"R$ 425,43"** (valor proporcional)

Este valor de **"R$ 425,43"** representa o INSS proporcional das férias que deve ser considerado na folha mensal.

### Ajuste de INSS na Folha Mensal

Na folha mensal, o sistema calcula o INSS considerando a **"base 1901"**. Seguindo o exemplo anterior, se a base for de **"R$ 3.673,54"**, o valor do INSS a ser retido corresponde a **"R$ 334,24"**.

Como o INSS proporcional das férias foi de **"R$ 425,43"** e o INSS da folha mensal é de **"R$ 334,24"**, torna-se necessária a **restituição do valor de R$ 91,21** ao colaborador na competência.

- Os valores totais estarão corretos quando analisados em conjunto, pois o sistema garante que o **desconto total de INSS** respeite as faixas progressivas da tabela, considerando todos os rendimentos do colaborador na competência.
