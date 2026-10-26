---
id: "43675077284631"
titulo: "Divergência no desconto de eConsignado na rescisão: como proceder?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43675077284631-Diverg%C3%AAncia-no-desconto-de-eConsignado-na-rescis%C3%A3o-como-proceder"
trilha: "Melhores Práticas > Pessoal+"
atualizado_em: "2026-10-03T12:50:11Z"
rotulos: ["Artigo criado KCS", "Sankhya RH - KCS"]
---

# Divergência no desconto de eConsignado na rescisão: como proceder?

O desconto do **eConsignado na rescisão** pode não ocorrer ou apresentar um valor diferente do esperado. Essa situação pode estar relacionada à **margem consignável disponível**, às informações disponibilizadas pela **DATAPREV (Emprega Brasil)** ou às regras aplicáveis ao cálculo rescisório.

Para identificar a causa, é importante verificar se o colaborador possuía **margem suficiente para o desconto** no momento do cálculo da rescisão. Quando a margem disponível não é suficiente, o sistema pode não realizar o desconto integral da parcela ou, conforme o caso, não realizar o desconto. O saldo que não for descontado na rescisão deverá ser tratado conforme as regras do contrato e as orientações da instituição financeira responsável pelo empréstimo.

Também é necessário verificar se a **DATAPREV (Emprega Brasil)** disponibilizou corretamente os dados do empréstimo, como o **saldo devedor e o percentual de desconto**. Essas informações são utilizadas pelo sistema para determinar o valor que poderá ser descontado na rescisão.

Dessa forma, quando o desconto do eConsignado não ocorrer conforme o esperado, deve-se verificar a **margem consignável, o saldo devedor, o percentual de desconto e o cálculo da rescisão**. Essa conferência permite identificar a origem da divergência e evitar ajustes manuais indevidos, garantindo o correto tratamento dos valores e o envio adequado das informações ao eSocial.

### Validações necessárias:

**DATAPREV (Emprega Brasil):** Após realizar a importação do **eConsignado (Crédito do Trabalhador)**, acesse a tela **Lançamento de Movimento** e verifique se os campos **Índice** e **Valor** foram preenchidos corretamente.

Caso algum desses campos não esteja preenchido, acesse o **Emprega Brasil** e verifique se estão disponíveis as informações necessárias para a rescisão: o **percentual de desconto** e o **saldo devedor** do empréstimo.

Caso uma dessas informações não esteja disponível no Emprega Brasil, o sistema não terá os dados necessários para realizar o desconto do **eConsignado (Crédito do Trabalhador)** na rescisão.

Conforme as orientações do **Manual do Crédito do Trabalhador**, o desconto na rescisão somente poderá ser realizado quando **as duas informações — percentual de desconto e saldo devedor — estiverem disponíveis no Emprega Brasil**.

Caso as duas informações estejam disponíveis no **Emprega Brasil**, mas algum dos campos **Índice** ou **Valor** não tenha sido preenchido no **Lançamento de Movimento**, é necessário realizar uma **nova importação do Crédito do Trabalhador** para que os dados sejam atualizados no sistema.

Em caso de dúvidas sobre o processo de importação do **Crédito do Trabalhador**, consulte o artigo [Desconto do Crédito do Trabalhador na rescisão (Portaria MTE nº 1.115/2026)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42166107959319-Desconto-do-Cr%C3%A9dito-do-Trabalhador-na-rescis%C3%A3o-Portaria-MTE-n%C2%BA-1-115-2026)

**Margem consignável:** Para verificar se existe margem disponível para o desconto do **eConsignado (Crédito do Trabalhador)**, acesse o **Cálculo** e, na aba **Base**, localize o evento **"Base Margem Créd. Trabalhador"**.

Esse evento permite verificar se existe **base disponível para o desconto**. Após essa conferência, verifique o **saldo devedor** e o **percentual de desconto** importados para o colaborador.

Com essas informações, é possível avaliar se a margem disponível é suficiente para realizar o desconto do **eConsignado na rescisão** e identificar possíveis divergências no cálculo.

Outra validação importante é verificar se os **eventos que compõem a Base Margem Créd. Trabalhador** estão configurados corretamente. A composição dessa base deve ser conferida conforme as orientações do **Manual do Crédito do Trabalhador**.

### Como proceder no sistema e no eSocial?

Ao realizar o envio do **desligamento ao eSocial**, pode ser apresentada uma **mensagem de advertência** relacionada ao Crédito do Trabalhador. Essa mensagem deve ser analisada para identificar a origem da divergência antes de prosseguir.

Caso a advertência indique **divergência na base do Crédito do Trabalhador**, é necessário verificar o valor apresentado e identificar quais eventos estão causando a diferença. Após localizar o evento, deve-se avaliar se ele **deve ou não compor a Base Margem Créd. Trabalhador**, realizando os ajustes necessários na configuração do evento.

Outra situação que pode ocorrer é a **indisponibilidade das informações do Crédito do Trabalhador no Emprega Brasil no momento do envio do evento**. Nesses casos, é importante comprovar que os dados do empréstimo estavam disponíveis **no momento em que a rescisão foi calculada**.

Para isso, recomenda-se manter **evidências por meio de prints contendo a data e o horário da consulta**, demonstrando que, na ocasião do cálculo da rescisão, as informações do Crédito do Trabalhador estavam disponíveis no Emprega Brasil.

### Boas práticas para evitar e tratar divergências

Para garantir o correto tratamento do **eConsignado na rescisão** e evitar divergências, siga as recomendações abaixo:

- Mantenha atualizados os **eventos que compõem a base de cálculo da margem consignável**, garantindo que todos os eventos que fazem parte da remuneração estejam devidamente vinculados. Para eventos personalizados, realize o vínculo manualmente, quando necessário.

**Importante:** o desconto do **eConsignado na rescisão** somente será realizado quando houver **margem consignável suficiente**. Caso não exista margem disponível, o saldo remanescente deverá ser tratado pelo colaborador diretamente com a **instituição financeira responsável pelo empréstimo**.

Nessa situação, não é necessário realizar ajustes no sistema ou enviar **informações adicionais ao eSocial**.
