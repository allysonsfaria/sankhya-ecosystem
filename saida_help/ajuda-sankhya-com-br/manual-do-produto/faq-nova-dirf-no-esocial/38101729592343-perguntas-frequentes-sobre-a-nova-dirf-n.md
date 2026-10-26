---
id: "38101729592343"
titulo: "Perguntas Frequentes sobre a Nova DIRF no eSocial"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38101729592343-Perguntas-Frequentes-sobre-a-Nova-DIRF-no-eSocial"
trilha: "Manual do Produto > Pessoas+ > Encargos e Obrigações Legais > Nova DIRF e Informe de Rendimentos > FAQ Nova DIRF no eSocial"
atualizado_em: "2026-09-27T18:59:34Z"
rotulos: ["Configuração", "Relatórios", "Fiscal", "Impostos", "DIRF", "eSocial", "Nova DIRF/eSocial", "Informe de Rendimentos", "Relatório S-5012", "IRRF - Períodos Anteriores", "Relatório S-5002"]
---

# Perguntas Frequentes sobre a Nova DIRF no eSocial

**1. Onde é lançada, na nova DIRF, a distribuição de lucros dos sócios?**

A distribuição de lucros é informada por meio do **EFD-Reinf**. No Sankhya, esse lançamento é realizado no **Módulo Fiscal**.

**2.** **Após a conferência dos valores, é necessário enviar algo ao eSocial para "fechar" a DIRF?**

Sim. O fechamento da DIRF ocorre **mensalmente**, por meio do envio do **evento S-1299 (Fechamento dos Eventos Periódicos)**.

**3. É necessário realizar algum fechamento específico no Sankhya para encerrar a DIRF?**

Não. O encerramento acontece automaticamente a cada envio mensal do **S-1299**, com o respectivo retorno do **evento S-5012** pelo eSocial.

**4. É necessário enviar algum evento para obter o S-5012?**

Sim. O **S-5012** somente é retornado pelo eSocial após o envio do **S-1299**.

**5.** **O que fazer quando a folha e o eSocial estão corretos, mas a DIRF apresenta divergência?**

Nessa situação, devem ser considerados os **valores enviados ao eSocial**. Caso a folha e os eventos estejam corretos, eventuais divergências no Extrator da DIRF podem ocorrer até que a base seja atualizada.

**6. Existe relatório comparativo entre Folha, eSocial e Informe de Rendimentos?**

Sim. O [**relatório S-5002 – Conferência IRRF**](https://ajuda.sankhya.com.br/hc/pt-br/articles/37202771074071) consolida:

- valores apurados na folha de pagamento;
- retornos do eSocial (evento S-5002);
- informações utilizadas na composição do informe de rendimentos.

**7. Existe relatório no Sankhya com totalizadores comparando sistema x eSocial?**

Sim. Essa conferência pode ser realizada por meio do [**relatório S-5002 – Conferência IRRF**](https://ajuda.sankhya.com.br/hc/pt-br/articles/37202771074071).

**8. Haverá um totalizador por funcionário semelhante à antiga ficha financeira?**

Sim. O [**relatório S-5002 – Conferência IRRF**](https://ajuda.sankhya.com.br/hc/pt-br/articles/37202771074071) cumpre esse papel.

**9. No S-5012 os valores conferem no resumo, mas divergem no detalhamento. Como tratar?**

Na primeira página do [**relatório do S-5012**](https://ajuda.sankhya.com.br/hc/pt-br/articles/37497561502231) é apresentada apenas a soma dos valores de IRRF. No segundo nível, é exibido o detalhamento por tipo de rendimento que impacta o imposto.

Nesses casos, o usuário deve:

1. Identificar os pontos divergentes;
2. Conferir as incidências na folha de pagamento e no eSocial;
3. Caso necessário, corrigir a incidência no sistema;
4. Enviar o **S-1010**, reabrir as referências e realizar nova apuração com o envio do **S-1210**.

**10.** **No S-5002 aparecem valores elevados em** "**Rendimentos não tributáveis/isentos" sem detalhamento. Como conferir?**

Para conferência, devem ser considerados no relatório **S-5002** todos os eventos que possuam:

- Incidência **75 – Abono pecuniário**;
- Incidência **79 – Outras isenções**.

Esses eventos podem ser verificados na **tela de Eventos → aba eSocial**, desde que tenham sido calculados na folha no período em análise.

É importante também observar a **regra de provento e desconto** no cálculo.

⚠️ Nas próximas versões, será disponibilizada a **descrição detalhada de todos os eventos** que compõem essa linha no informe de rendimentos, tanto para geração via eSocial quanto via folha.

**11. Ao gerar a DIRF pelo Sankhya, ela já é oficial ou pode ser corrigida?**

As informações podem ser corrigidas:

- Até a entrega do **informe de rendimentos** ao colaborador; ou
- Caso seja utilizada a tela [**IRRF – Períodos Anteriores**](https://ajuda.sankhya.com.br/hc/pt-br/articles/37272130595223), até o fechamento do **evento S-1210 de janeiro**.

**12. Qual é o prazo para retificação das informações da DIRF?**

O prazo de retificação segue as regras do eSocial, sendo permitido até o envio do **evento S-1210 de janeiro**.

Importante destacar que as correções precisam ser realizadas antes da geração e envio das informações do Informe de Rendimentos aos trabalhadores.

**13. Qual é o prazo de envio dos eventos do eSocial relacionados à DIRF?**

Conforme regra disposta no evento S-1210, os eventos devem ser enviados até o **dia 15 do mês subsequente** ao mês de referência. Caso a data caia em dia não útil, o prazo é prorrogado para o próximo dia útil.

No caso dos Períodos Anteriores essa regra se aplica ao envio do fechamento de janeiro/2026.

**14.** **Em qual tela realizo a retificação de períodos anteriores?**

A retificação é realizada na tela [**IRRF – Períodos Anteriores eSocial**](https://ajuda.sankhya.com.br/hc/pt-br/articles/37272130595223), disponível em:
**Pessoal+ > Rotinas Folha > IRRF – Períodos Anteriores eSocial**

⚠️Caso a tela não esteja disponível automaticamente após a atualização, é necessário solicitar ao **TI a liberação de acesso**, por meio da tela: **Configurações > Controle de Acesso > Acessos**.

**15. Por que não tenho acesso à tela IRRF – Períodos Anteriores eSocial?**

Verifique os seguintes pontos:

1. Se o **Sankhya Om**, **Módulo Pessoal** e **San eSocial** estão atualizados para as versões mais recentes;
2. Se a tela está disponível no caminho indicado: **Pessoal+ > Rotinas Folha > IRRF – Períodos Anteriores eSocial;**
3. Caso não esteja visível, solicite ao **TI a liberação de acesso** na tela **Acessos**.

**16. Na tela IRRF – Períodos Anteriores, posso filtrar colaborador por empresa filial/matriz?**

Sim, essa correção já está disponível nas **últimas versões publicadas** do sistema.

**17. Após corrigir uma rubrica/incidência e reenviar o S-1010, é necessário reabrir folhas e retificar o S-1210?**

Sim. É necessário **reabrir as folhas** e **retificar o S-1210**, para que a apuração correta seja refletida no eSocial.

**18. Alterei a incidência de Previdência Privada. Preciso recalcular todos os meses de 2025?**

Somente se a alteração **impactar valores**. Caso contrário, basta reenviar o **S-1210**.

⚠️Para eventos de **plano de saúde** que tiverem a **natureza da rubrica alterada**, será necessário reenviar os eventos **S-1200 / S-2299 / S-2399**, além do **S-1210**, para atender às validações do eSocial.

**19.** **Preciso alterar a incidência de coparticipação do plano de saúde. É necessário reabrir folhas e retificar o S-1210?**

Sim. Sempre que houver **alteração na natureza da rubrica** de eventos de plano de saúde, é necessário reenviar os eventos **S-1200 / S-2299 / S-2399**, além do **S-1210**.

**20. Qual a diferença entre as incidências 51 e 79 (pensão alimentícia)?**

O **tipo de rendimento** informado depende da **base de cálculo sobre a qual a pensão alimentícia é descontada**.

Exemplos:

- **11 – Remuneração Mensal**: quando o desconto ocorre sobre as verbas da folha mensal;
- **79 – Rendimentos Isentos ou Não Tributáveis**: quando o desconto incide sobre verbas indenizadas, como em rescisões.

**21.** **Por que a incidência 79 precisou de ajuste?**

Anteriormente, quando o trabalhador não possuía retenção de IRRF, mas tinha desconto de pensão alimentícia, o sistema levava essa informação de forma equivocada como **tipo de rendimento 79**.

Esse comportamento foi corrigido. Para os casos impactados, o sistema ajustará automaticamente o tipo de rendimento, sendo necessária a **retificação do S-1210** para correção da apuração na DIRF/eSocial.

Para isso, é indispensável que o sistema esteja atualizado nas **últimas versões do Módulo Pessoal e San eSocial**.

**22. Por que o desconto de pensão nas férias está indo como 51 e não 53?**

O desconto de pensão sobre férias deve utilizar a **incidência 53**.

Como as rubricas de pensão alimentícia são **parametrizadas pelo próprio cliente**, a correção da incidência, o envio do **S-1010** e a retificação do **S-1210** são de responsabilidade do usuário.

**23. No informe de rendimentos, o campo "Outros" representa o quê?**

O campo **Outros**, localizado na linha 9 do quadro 4 – Rendimentos Isentos e Não Tributáveis, apresenta a soma dos eventos com incidência **75 - Abono pecuniário** e **incidência 79 – Outras isenções considerando também os descontos**, bem como suas descrições, conforme o leiaute do eSocial e a **IN RFB n.º 2.060/2021**.

**24. Os valores de plano de saúde estão indo todos para o titular. Isso será ajustado?**

O primeiro ponto a verificar é se, no lançamento dos eventos de desconto para dependentes, a **vinculação no campo "Optante"** foi realizada corretamente.

Como boa prática, recomenda-se utilizar:

- Um evento de desconto para o **titular**;
- Outro evento específico para **dependentes**, evitando vinculações incorretas.

**25. O cadastro de plano de saúde será preenchido automaticamente para quem não possui?**

Sim. Será liberada uma funcionalidade que **preenche automaticamente o cadastro de plano de saúde** para funcionários e dependentes que não possuam cadastro, mas que tenham eventos de desconto calculados e enviados ao eSocial.

As novidades devem ser acompanhadas pelo [**Loopedin**.](https://ajuda.sankhya.com.br/hc/pt-br/articles/37089461685783-Fique-por-dentro-da-evolu%C3%A7%C3%A3o-do-Pessoas-em-tempo-real)

**26. Qual versão contempla todas as correções de plano de saúde e DIRF?**

Todas as funcionalidades relacionadas à DIRF já estão disponíveis nas versões atuais. Por isso, é **fundamental manter o sistema sempre atualizado**.

**27.** **É possível enviar o informe de rendimentos por e-mail ao colaborador?**

Sim. O envio do informe por e-mail mantém o **mesmo comportamento já existente** no sistema.

⚠️ O e-mail com o informe de rendimentos deve ser enviado aos trabalhadores apenas quando não houver mais alterações a serem realizadas. Caso seja necessário alterar qualquer informação no informe, é necessário realizar uma nova geração para que o sistema atualize as informações do informe que será enviado.

**28. Como gerar o informe considerando dados do sistema anterior?**

Atualmente, o informe de rendimentos pode ser gerado apenas com as informações existentes no Sankhya após a implantação.

Estamos estudando melhorias para que, no próximo ano-calendário, seja possível gerar o informe considerando **todas as informações do eSocial ao longo do ano**.

**29. Como realizar a conferência das Informações de Plano de Saúde no Informe de Rendimentos (Quadro 7- Informações Complementares)?**

Para validar as informações de Plano de Saúde, siga as etapas abaixo:

✅ 1. Verifique se a informação foi enviada na origem:

- Primeiramente, confirme se a informação foi enviada no período de apuração do ano anterior por meio do evento S-1210, no grupo: planSaude >> infoIRCompl (para titular e/ou dependentes).

  ✔️ Se a informação foi enviada corretamente:
  - Realize a conferência pelo Relatório de Conferência do S-5002, validando:
    - primeiro nível (visão consolidada);
    - segundo nível (visão individualizada por trabalhador).
  - Verifique também no Informe de Rendimentos – Quadro 7 se todas as informações estão sendo apresentadas corretamente.

⚠️ 2. Caso a informação NÃO tenha sido enviada no período correspondente:

- Se as informações não constarem no período de apuração do ano-calendário em que o Informe está sendo gerado, realize as seguintes validações:
  - Etapa 1 – Vínculo do Plano de Saúde:
    - verifique se o plano de saúde está vinculado corretamente ao titular e/ou dependentes;
    - confirme se a Referência Inicial (início de validade) do plano corresponde ao período de apuração analisado.

      **Solução**:
    - Realize o vínculo na tela Configuração Funcionário > Plano de Saúde (titular) ou tela Configuração Funcionário > Dependentes > Plano de Saúde (dependente);
    - Ajuste o campo Referência Inicial (aba Plano de Saúde), garantindo que esteja igual ou anterior ao período de apuração. Após o ajuste, gere e envie novamente o S-1210.
  - Etapa 2 – Vínculo do Evento de Desconto:
    - verifique se o evento de desconto do plano de saúde está corretamente vinculado ao plano cadastrado para o titular e/ou dependente.

      **Solução**:
    - Ajuste o vínculo na tela Plano de Saúde, no campo Evento.
    - Gere e envie novamente o S-1210.
  - Etapa 3 – Conferência de Sequências:
    - para o titular, a sequência deve ser 0 (zero).
    - para dependentes, a sequência deve corresponder exatamente à sequência cadastrada para cada dependente.

      **Solução**:
    - Caso haja divergência, o ajuste deve ser realizado na tela Lançamento de Movimento.
    - Após a correção, gere e envie novamente o S-1210.
  - Etapa 4 – Configuração da Rubrica:
    - verifique se o evento de plano de saúde possui:

      - Natureza de Rubrica 9219
      - Código de incidência igual a:
        - 09, ou
        - 67, ou
        - 9067

      **Solução**:
    - Reenvie o evento S-1010 com as novas configurações.
    - Após o envio, gere e transmita novamente os eventos S-1200 e S-1210 para cada período de apuração impactado.

📌 **Importante**

Todas as validações acima são essenciais para que a informação:

- seja enviada corretamente ao eSocial;
- seja consolidada adequadamente no S-5002;
- seja apresentada corretamente no Informe de Rendimentos.

Caso alguma configuração esteja divergente, será necessário realizar os ajustes indicados e reenviar os eventos correspondentes para nova apuração.

---

**Caso ainda tenha alguma dúvida, descreva-a no campo de Comentários aqui abaixo.**
