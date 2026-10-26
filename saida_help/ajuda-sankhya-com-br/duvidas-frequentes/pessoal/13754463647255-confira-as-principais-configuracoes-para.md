---
id: "13754463647255"
titulo: "Confira as principais configurações para o cálculo de Dissídio no Pessoal + W"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/13754463647255-Confira-as-principais-configura%C3%A7%C3%B5es-para-o-c%C3%A1lculo-de-Diss%C3%ADdio-no-Pessoal-W"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-08-17T12:58:56Z"
rotulos: ["Configuração", "Eventos", "Impostos", "Pessoal", "Folha de Pagamento", "David Macedo", "Configurar eventos de folha", "Marcar base \"Complementar\" para impostos", "Preencher dados da convenção", "Convenção Coletiva"]
---

# Confira as principais configurações para o cálculo de Dissídio no Pessoal + W

O cálculo de **Dissídio** depende de configurações que definem os colaboradores considerados, as regras aplicadas e os valores de reajuste. Por isso, é importante validar previamente essas configurações para evitar inconsistências na apuração dos valores ou na apresentação dos eventos.

Neste artigo, serão apresentadas as principais configurações das telas de **Sindicato, Regra de Cálculo, Eventos e Reajuste Salarial**, destacando os pontos que podem influenciar diretamente o cálculo.

## Sindicato

Acesse **Pessoal+ » Cadastros » Sindicato**, localize o sindicato desejado e acesse a aba correspondente à **Convenção Coletiva, Acordo Coletivo ou Sentença Normativa** para realizar o preenchimento das informações.

![Imagem 1: Acesse Pessoal+ » Cadastros » Sindicato , localize o sindicato desejado e acesse a aba correspondente à Convenção…](https://ajuda.sankhya.com.br/hc/article_attachments/42775574763671)

Confira atentamente os seguintes campos:

- **Data Base:** influencia quais funcionários serão considerados para o reajuste. Funcionários admitidos na data-base ou após essa data não serão considerados, exceto quando o salário estiver abaixo do mínimo estabelecido para a classe.
- **Data Assinatura:** influencia o reajuste de funcionários desligados. Caso o desligamento ocorra após a data de assinatura, o funcionário não será considerado, pois o sistema entende que o reajuste ocorreu antes do desligamento. Para considerar os desligados no mês da assinatura, informe como data de assinatura o **último dia do mês**.
- **Percentual:** informe o percentual total do reajuste, mesmo quando já tiver sido realizada uma antecipação.
- **Reaj. Sindical:** deve estar marcado para que o cadastro seja identificado como reajuste sindical e fique disponível no processo de reajuste salarial.
- **Perc. Antecipação, Data Ref. Antecipação e Cód. Hist. Antecipação:** devem ser preenchidos quando houver antecipação do reajuste. Essas informações são utilizadas pelo sistema para calcular o percentual restante e as respectivas diferenças.

> **Importante:** para orientações sobre antecipação de reajuste, consulte o artigo [**Veja como realizar a antecipação de reajuste salarial CCT**](https://ajuda.sankhya.com.br/hc/pt-br/articles/30948418365975-Veja-como-realizar-a-antecipa%C3%A7%C3%A3o-de-reajuste-salarial-CCT)

## Regra de Cálculo

Acesse **Pessoal+ » Cadastros » Regras de Cálculo**, localize a regra vinculada ao sindicato e confira as configurações disponíveis na seção **Reajuste Sindical**.

![Imagem 2: Acesse Pessoal+ » Cadastros » Regras de Cálculo , localize a regra vinculada ao sindicato e confira as configurações…](https://ajuda.sankhya.com.br/hc/article_attachments/42775574765079)

Os principais campos são:

- **Reajuste Sindical Proporcional ao Tempo de Serviço:** deve ser utilizado quando a convenção determinar que o reajuste será proporcional ao tempo de serviço. Nesse caso, funcionários com menos de um ano de admissão até a data-base receberão o reajuste de forma proporcional.
- **Considerar % cheio no recálculo de eventos:** deve ser marcado quando o percentual integral do reajuste precisar ser considerado no recálculo dos eventos.
- **Aplicar percentual em todos os eventos da folha complementar (mensalistas):** deve ser marcado para funcionários mensalistas quando essa regra se aplicar ao cálculo.
- **Aplicar percentual em todos os eventos da folha complementar (não mensalistas):** deve ser marcado para funcionários não mensalistas quando essa regra se aplicar ao cálculo.

## Eventos

Na aba **Avançado**, verifique se os eventos que devem participar do cálculo possuem a marcação **“Tem seus valores recalculados”**. Essa configuração determina que o evento seja **recalculado durante o cálculo do Dissídio**.

![Imagem 3: Na aba Avançado , verifique se os eventos que devem participar do cálculo possuem a marcação “Tem seus valores…](https://ajuda.sankhya.com.br/hc/article_attachments/42775604022423)

**Evento de indenização integrante do Aviso Prévio Indenizado:** deve ser marcado quando o evento precisar ser considerado no recálculo de rescisões para pagamento de diferenças de verbas indenizadas.

![Imagem 4: Evento de indenização integrante do Aviso Prévio Indenizado: deve ser marcado quando o evento precisar ser considerado…](https://ajuda.sankhya.com.br/hc/article_attachments/42775604024727)

- **É evento da folha Recibo de Férias?:** deve ser utilizado quando o evento for exclusivo da folha de recibo de férias e não deverá participar do cálculo de Dissídio.

  **Ponto de atenção:** caso um evento que deveria participar do cálculo de Dissídio não esteja sendo apresentado, verifique se o campo “É evento da folha Recibo de Férias?” está marcado. Quando essa opção estiver marcada indevidamente, o evento poderá não ser apresentado no cálculo.

![Imagem 5: Ponto de atenção: caso um evento que deveria participar do cálculo de Dissídio não esteja sendo apresentado, verifique…](https://ajuda.sankhya.com.br/hc/article_attachments/42775604025623)

Também é importante conferir as **bases de cálculo dos impostos**, verificando se estão configuradas com a opção **“Dissídio”** como regra de cálculo. Essa validação é especialmente importante para eventos de base configurados como personalizados, pois os eventos padrões já possuem a configuração adequada para o cálculo em folha de Dissídio.

![Imagem 6: Também é importante conferir as bases de cálculo dos impostos , verificando se estão configuradas com a opção…](https://ajuda.sankhya.com.br/hc/article_attachments/42775604026775)

## Reajuste Salarial

Após validar as configurações anteriores, realize o reajuste salarial conforme as informações da Convenção Coletiva, Acordo Coletivo ou Sentença Normativa.

Para consultar o passo a passo, acesse o artigo: [Como efetuar o reajuste salarial em decorrência de Convenção Coletiva para todos os Funcionários no Pessoal +?](https://ajuda.sankhya.com.br/hc/pt-br/articles/Como%20efetuar%20o%20reajuste%20salarial%20em%20decorr%C3%AAncia%20de%20Conven%C3%A7%C3%A3o%20Coletiva%20para%20todos%20os%20Funcion%C3%A1rios%20no%20Pessoal%20+)

Após realizar o reajuste, calcule a folha  de dissídio em **Cálculo** (individual ou coletivo) e preencha as informações referentes ao cálculo e prossiga com o mesmo.

![Imagem 7: Após realizar o reajuste, calcule a folha de dissídio em Cálculo (individual ou coletivo) e preencha as informações…](https://ajuda.sankhya.com.br/hc/article_attachments/24445071731863)

![Imagem 8: Após realizar o reajuste, calcule a folha de dissídio em Cálculo (individual ou coletivo) e preencha as informações…](https://ajuda.sankhya.com.br/hc/article_attachments/24445057920279)

![Imagem 9: Após realizar o reajuste, calcule a folha de dissídio em Cálculo (individual ou coletivo) e preencha as informações…](https://ajuda.sankhya.com.br/hc/article_attachments/24445057922583)

Pronto! O cálculo foi concluído, agora é só realizar as conferências!
