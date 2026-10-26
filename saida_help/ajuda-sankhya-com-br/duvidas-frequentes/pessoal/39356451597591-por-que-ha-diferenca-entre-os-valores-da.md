---
id: "39356451597591"
titulo: "Por que há diferença entre os valores da GRRF no sistema e no FGTS Digital em rescisões?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39356451597591-Por-que-h%C3%A1-diferen%C3%A7a-entre-os-valores-da-GRRF-no-sistema-e-no-FGTS-Digital-em-rescis%C3%B5es"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-07-29T13:28:55Z"
rotulos: ["Impostos", "eSocial", "Folha de Pagamento", "Rescisão", "Central do eSocial", "FGTS", "Artigo criado KCS", "Sankhya RH - KCS"]
---

# Por que há diferença entre os valores da GRRF no sistema e no FGTS Digital em rescisões?

Em situações de **"Rescisão de contrato de experiência"**, é comum que os usuários identifiquem divergências entre os valores de FGTS apresentados no **"Resumo de Folha"** do sistema Sankhya e os valores exibidos no portal **"FGTS Digital"**. Essa diferença pode ocorrer por diversos motivos, incluindo a forma como o sistema processa rescisões complementares, pagamentos de 13º salário e a data de competência versus data de pagamento dos encargos.

Este artigo explica as principais causas dessas divergências e orienta sobre como validar se os valores estão corretos, além de apresentar os procedimentos adequados para cada situação.

### Validação dos valores no eSocial

Antes de considerar que há um erro no sistema, é fundamental validar os valores no portal do eSocial. O eSocial é a fonte oficial de informações e serve como referência para o **"FGTS Digital"**.

Acesse o **Portal do eSocial** e verifique se os valores de base de cálculo do FGTS e valor de recolhimento do FGTS estão idênticos aos apresentados no **Resumo de Folha** do sistema Sankhya. Se os valores estiverem corretos no eSocial, mas divergentes no **FGTS Digital**, a inconsistência está no processamento da plataforma, e não no sistema Sankhya.

Neste caso, abra um chamado diretamente com o suporte do FGTS Digital para que eles identifiquem a causa da divergência em seu portal.

### Diferença causada por 13º salário na rescisão

Uma das causas mais comuns de divergência ocorre quando o funcionário possui 13º salário calculado na mesma referência da rescisão. Neste cenário, a **"GRRF"** irá consolidar os valores da rescisão e do 13º salário, resultando em um montante maior do que o apresentado apenas na folha de rescisão.

Além disso, se o funcionário recebeu adiantamento de 13º salário em uma competência anterior (por exemplo, durante as férias), mas o pagamento dos encargos ocorreu em uma competência posterior, o eSocial considera a data de pagamento dos encargos para apresentar os valores no **FGTS Digital**. Isso pode gerar diferenças na visualização entre o **Resumo de Folha** (que considera a competência de cálculo) e o **FGTS Digital** (que considera a data de pagamento).

**Exemplo prático**: um funcionário teve adiantamento de 13º salário calculado em fevereiro/2025, mas o pagamento ocorreu em janeiro/2026. O FGTS referente ao 13º salário será exibido no **FGTS Digital** na competência janeiro/2026, enquanto no **Resumo de Folha** aparecerá em fevereiro/2025.

### Indenização compensatória complementar em rescisões

Outro cenário que gera dúvidas é quando aparece um valor de **Indenização compensatória complementar** no **FGTS Digital**. Esse valor refere-se aos **40% de multa rescisória** calculados sobre o FGTS do 13º salário, quando este foi pago em parcelas.

O **FGTS Digital** entende que deve calcular os 40% sobre o recolhimento da remuneração do 13º salário, gerando esse valor complementar. Por exemplo, se a remuneração do 13º salário foi de R$ 1.344,09, aplicando a alíquota de 8% temos R$ 107,52 de FGTS. Sobre esse montante, incide o percentual de 40%, resultando em R$ 43,00 de indenização compensatória complementar.

Esse cálculo está correto e segue as regras do governo. Caso haja dúvidas sobre o comportamento do cálculo, entre em contato com o **FGTS Digital** para validação.

### Rescisão complementar e referência de origem

Em casos de **Rescisão complementar**, é fundamental que os eventos lançados como **"Verba de meses anteriores"** tenham a **"Referência de origem correta"**. A referência deve ser sempre o mês da rescisão original, e não o mês em que a verba foi gerada.

Se a referência de origem for preenchida incorretamente, o FGTS subirá ao **FGTS Digital** como **"Mensal"**, e não como **"FGTS Rescisório"**. Isso causará divergência entre o **Resumo de Folha** (que mostra na aba GRRF) e o **FGTS Digital** (que mostra como mensal).

**Procedimento correto**: ao lançar verbas em rescisão complementar, sempre utilize como referência de origem o mês da rescisão original do colaborador, garantindo que a informação suba corretamente ao **FGTS Digital** como FGTS Rescisório.

### Atualização do Console eSocial

Divergências nos valores também podem ocorrer devido a versões desatualizadas do Console eSocial. Certifique-se de que o console esteja sempre na versão mais recente disponível.

Caso identifique que o console está desatualizado, realize a atualização e, em seguida, exclua os eventos **"S-1210"** e **"S-1200"** no eSocial. Após a exclusão, efetue o reenvio dos eventos. Esse procedimento pode corrigir inconsistências na transmissão dos dados.

### Resumo das principais causas

As divergências entre o **"Resumo de Folha"** e o **"FGTS Digital"** geralmente ocorrem devido a:

- Consolidação de valores de rescisão e 13º salário na GRRF;
- Diferença entre competência de cálculo e data de pagamento dos encargos;
- Indenização compensatória complementar sobre 13º salário parcelado;
- Referência de origem incorreta em rescisões complementares;
- Console eSocial desatualizado.

Sempre valide os valores no **Portal do eSocial** antes de considerar que há erro no sistema. Se os valores estiverem corretos no eSocial, mas divergentes no **FGTS Digital**, o problema está no processamento do portal governamental.
