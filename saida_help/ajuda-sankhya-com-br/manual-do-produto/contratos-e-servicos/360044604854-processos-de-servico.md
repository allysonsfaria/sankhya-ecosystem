---
id: "360044604854"
titulo: "Processos de Serviço"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604854-Processos-de-Servi%C3%A7o"
trilha: "Manual do Produto > Contratos e Serviços > Contratos e Serviços"
atualizado_em: "2026-07-29T14:04:36Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Contratos e Serviços", "Executantes", "Fluxo de Trabalho", "Ordem de Serviços", "Processos de Serviço", "transições", "Workflow", "br.com.sankhya.mgeos.cad.processosdeservico", "Processos de Serviço manual", "Ordem de Serviço", "Atividades", "sankhyaflow", "Gerenciamento de Processos de Serviço com Workflow"]
---

# Processos de Serviço

```
![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42311212345239) Módulo: Contratos e Serviços> Arquivos> Cadastros
```

---

Esta tela possibilita a gerência do fluxo de trabalho interno de forma simples e prática.

Configura-se o **"Fluxo de Trabalho"** para os processos que possuam sequências previamente definidas e que serão rigorosamente seguidas pelas Ordens de Serviço.

| [Fluxo do Processo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604854-Processos-de-Servi%C3%A7o#fluxodoprocesso) |  | [Configurações necessárias para uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604854-Processos-de-Servi%C3%A7o#configura%C3%A7%C3%B5esnecess%C3%A1riasparauso) |
| --- | --- | --- |
| [Cadastro das atividades do Processo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604854-Processos-de-Servi%C3%A7o#cadastrodasatividadesdoprocesso) |  | [Botão Substituir OS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604854-Processos-de-Servi%C3%A7o#bot%C3%A3osubstituiros) |
| [Botão Desvincular OS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604854-Processos-de-Servi%C3%A7o#bot%C3%A3odesvincularos) |  | [Processo na Ordem de Serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604854-Processos-de-Servi%C3%A7o#processonaordemdeservi%C3%A7o) |
| [Parâmetros que influenciam nesta tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604854-Processos-de-Servi%C3%A7o#par%C3%A2metrosqueinfluenciamnestatela) |  |  |

![Imagem 2: Parâmetros que influenciam nesta tela](https://ajuda.sankhya.com.br/hc/article_attachments/360095462254)

## Fluxo do Processo

Esta permitirá a automatização de um processo de negócio, de forma que, no final de uma atividade, a próxima a ser executada, seja transmitida para o próximo executante, de acordo com regras que serão pré-definidas de acordo com suas preferências.

Por exemplo, para criar uma solução específica para um cliente em um Processo de Implementação, temos as seguintes atividades:

**1-** Definição escopo

**2-** Implementação

**3-** Teste

**4-** Documentação de Teste

**5-** Compilação

**6-** Validação Versão

**7-** Documentação

**8-** Acompanhamento Implementação, que é a entrega da solução ao cliente.

No processo de implementação, para que a solução seja efetiva para o cliente é necessário que estas atividades sejam executadas nesta sequência. Não é possível **"Testar"** sem ter **"Implementado"**, e por sua vez não é possível **"Implementar"** sem ter **"Definido o escopo"**.

Vejamos a seguir o fluxo desse Processo:

![Imagem 3: Vejamos a seguir o fluxo desse Processo:](https://ajuda.sankhya.com.br/hc/article_attachments/9901905451287)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604854-Processos-de-Servi%C3%A7o#top)

## Configurações necessárias para uso

Inicialmente, para que as funcionalidades estejam disponíveis para utilização, é necessário que estejam configuradas na licença de uso, os opcionais:

- **30618 – WORKFLOW/W**
- **501024 – MÓDULO WORKFLOW SANKHYA /W**

Após a disponibilização do opcional, é necessário cadastrar o Processo como um Serviço. Esse Serviço, será registrado na tela **"Processos de Serviço"**.

Em seguida entre no menu:

Contratos e Serviços > Arquivos > Cadastros > Configurações Ordem de Serviço > Processos de Serviço

Na tela, você terá os campos:

**Serviço:** Informe neste campo o nome do processo.

**Variação:** Este campo será utilizado para criar um processo semelhante a um já existente, considerando que os processos estão sempre evoluindo, alterando assim, a estrutura do processo para as novas Ordens de Serviço a serem lançadas.

**Principal:** Nesse campo especifique se o processo está ou não ativo, ou seja, se existirem dois processos com o mesmo serviço, mas com variação diferente, deve-se informar ao sistema qual deles será utilizado, quando no lançamento de uma ordem de serviço.

**Nota:** se o campo **"Principal"** estiver configurado com a opção **"Não"** ainda que o processo seja único, o sistema não o considerará no lançamento das Ordens de Serviço.

**Observação:** pode-se informar neste campo, detalhes referentes a este processo.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604854-Processos-de-Servi%C3%A7o#top)

## Cadastro das atividades do processo

![Imagem 4: Cadastro das atividades do processo](https://ajuda.sankhya.com.br/hc/article_attachments/360097769053)

**Selecionar próxima atividade?:** Se configurado como **"Sim"** ao finalizar a atividade, o executante poderá encaminhar a OS a um dos executantes configurados para as próximas atividades.

**Pode concluir processo?:** Se marcada, você será liberado para a partir do seu item, concluir o processo fechando a OS sem passar para os outros **"Níveis"**. Contudo, isto só será válido se não existir nenhuma outra atividade em execução.

**Seguir fluxo anterior?:** Estando esta opção marcada, ao executar a atividade pela segunda vez, no caso de um recuo ou transição manual, o sistema automaticamente seguirá o fluxo escolhido anteriormente.

**Máximo de níveis a recuar:** Você deverá informar neste campo quantos **"Níveis"** poderão ser retrocedidos de forma ordenada, se assim o desejar. Se este campo estiver em branco o sistema não permitirá que uma atividade retorne a sua predecessora, a não ser que seja definida uma transição manual na grade localizada na parte inferior da tela **"Transições desta atividade"**.

**Tipo de transição:** Este campo possui três opções de escolha, assim, teremos:

- **Lista:** Pode-se escolher atividades originadas de transições manuais, adicionadas na opção **"Transições desta atividade"**.
- **Próximo Nível:** O sistema só permitirá realizar transições de próximo nível (fluxo normal do processo) e de nível de recuo;
- **Ambos:** Será possível trabalhar com as duas opções.

#### Seção Executantes desta Atividade

Definem-se nesta grade os Executantes de cada Atividade selecionada. Cada atividade poderá ter um ou mais executantes para ela configurados.

Por meio dos botões ![Imagem 5: Por meio dos botões respectivamente, efetua-se a inclusão de executantes para a realização da atividade, ou a retirada…](https://ajuda.sankhya.com.br/hc/article_attachments/9901966041367) respectivamente, efetua-se a inclusão de executantes para a realização da atividade, ou a retirada destes, caso necessário.

[GIF animado: Imagem 6: Por meio dos botões respectivamente, efetua-se a inclusão de executantes para a realização da atividade, ou a retirada…](https://ajuda.sankhya.com.br/hc/article_attachments/360097769413)

#### Seção Transições desta Atividade

![Imagem 7: Seção Transições desta Atividade](https://ajuda.sankhya.com.br/hc/article_attachments/9901969027351)

Na grade **"Transições desta Atividade"**, tem-se a opção de definir também, como será a transição de um nível para outro dentro do processo.

Ao clicar no botão ![Imagem 8: Ao clicar no botão para inclusão, tem-se a tela "Adicionando transições" :](https://ajuda.sankhya.com.br/hc/article_attachments/9902000946199) para inclusão, tem-se a tela **"Adicionando transições"**:

![Imagem 9: Ao clicar no botão para inclusão, tem-se a tela "Adicionando transições" :](https://ajuda.sankhya.com.br/hc/article_attachments/360097770753)

**Nota:** esta opção só será utilizada quando houver a necessidade de saltar ou retroceder alguns níveis dentro do processo.

![Imagem 10: Nota: esta opção só será utilizada quando houver a necessidade de saltar ou retroceder alguns níveis dentro do processo.](https://ajuda.sankhya.com.br/hc/article_attachments/360097772893)

Neste exemplo, a atividade selecionada é a de Nível 4 – Teste da Correção de Erro, se por algum motivo o usuário deseja retornar ao Nível 2 – Identificação do Erro (Debug), ao invés de seguir diretamente para a próxima atividade, que seria a "Documentação da Correção de Erro" no Nível 5, ele utilizará a opção "Transições desta Atividade" para selecionar a atividade de destino.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604854-Processos-de-Servi%C3%A7o#top)

## Botão Substituir OS

O botão Substituir no topo da tela permite realizar a substituição de executantes, no processo selecionado e em todos os outros processos.

[GIF animado: Imagem 11: O botão Substituir no topo da tela permite realizar a substituição de executantes, no processo selecionado e em todos…](https://ajuda.sankhya.com.br/hc/article_attachments/360095464894)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604854-Processos-de-Servi%C3%A7o#top)

## Botão Desvincular OS

Ao clicar no botão Desvincular OS é aberta a tela **"Desvincular OS de Fluxo de Processo"** onde informa-se o número da OS que deseja desvincular o processo de serviço da mesma. Ao preencher-se o número, basta clicar em Desvincular OS para que o Processo de Serviço seja desvinculado da OS, transformando a mesma em uma OS normal.

![Imagem 12: Ao clicar no botão Desvincular OS é aberta a tela "Desvincular OS de Fluxo de Processo" onde informa-se o número da OS…](https://ajuda.sankhya.com.br/hc/article_attachments/360095465454)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604854-Processos-de-Servi%C3%A7o#top)

## Processo na Ordem de Serviço

Para que a abertura de uma Ordem de Serviço seja originada do processo de Workflow, é necessário que o serviço a ser utilizado na primeira sub-OS seja o serviço vinculado ao Cabeçalho do Processo do Serviço.

**Nota:** assim que uma Ordem de Serviço é aberta com o Workflow, o sistema não permite que nenhuma alteração seja feita no processo que o definiu, à exceção de troca de executantes. Uma vez Fechada a OS, pode-se fazer as alterações necessárias no processo, através da tela de Processos de Serviço.

Na OS o processo ocorrerá da mesma forma, modificando-se apenas as opções de **"Salvar"**, **"Encaminhar"** e **"Fechar OS"**. Vejamos um exemplo:

O processo de **"Correção de Erro de Software"** contempla as seguintes atividades:

Nível 1 - Reprodução do Erro (Teste)

Nível 2 - Identificação do Erro (Debug)

Nível 3 - Correção do Erro

Nível 4 - Teste da Correção de Erro

Nível 5 - Documentação da Correção de Erro

Nível 6 - Validação

![Imagem 13: Nível 6 - Validação](https://ajuda.sankhya.com.br/hc/article_attachments/360097774573)

Neste exemplo a OS 110 foi aberta pelo processo **"Correção de Erro de Software"**, sendo assim, o usuário terá duas opções para salvar seu item: **"Salvar"** e **"Salvar e Fechar"**.

**Salvar e Fechar:** Esta opção, realiza o salvamento do item e finaliza a OS, se a configuração feita anteriormente da atividade, permitir que ela conclua o processo.

**Salvar:** Esta opção irá salvar a tarefa atual e caso exista alguma outra Sub-OS em aberto, irá apenas salvar o item em questão. Caso todas as outras Sub-OS's já estejam fechadas, serão apresentadas as opções de **"Salvar e Fechar OS"**, **"Salvar e Abrir Sub-OS"** e **"Encaminhar"**.

![Imagem 14: Salvar: Esta opção irá salvar a tarefa atual e caso exista alguma outra Sub-OS em aberto, irá apenas salvar o item em…](https://ajuda.sankhya.com.br/hc/article_attachments/360097774933)

**Salvar e Fechar OS:** Esta opção, realiza o salvamento do item e finaliza a OS.

**Salvar e Abrir Sub-OS:** Por meio desta opção, é feito o salvamento do item e é aberto uma nova sub-OS com as mesmas configurações (Produto, Serviço, Executante etc) do sub-item que acabou de ser fechado. Esta opção é em muitos casos utilizada, quando a atividade não foi totalmente concluída e precisará ser continuada em outro momento.

![Imagem 15: Salvar e Abrir Sub-OS: Por meio desta opção, é feito o salvamento do item e é aberto uma nova sub-OS com as mesmas…](https://ajuda.sankhya.com.br/hc/article_attachments/360095471014)

**Encaminhar:** O sistema irá salvar a tarefa atual e continuar com o processo Workflow, caminhando para a próxima tarefa como foi definido nos **"Processos de Serviços"**, permitindo ao usuário encaminhar a OS a um dos executantes da próxima atividade.

- Selecione o **"Serviço Previsto"** que será executado na etapa seguinte;
- Em seguida, indique o "Executante" responsável pelo desenvolvimento da próxima atividade;
- Ao clicar no botão ![Imagem 16: Ao clicar no botão , a OS será alocada para o executante definido para o desenvolvimento da atividade em questão.](https://ajuda.sankhya.com.br/hc/article_attachments/360097778793), a OS será alocada para o executante definido para o desenvolvimento da atividade em questão.

O mesmo procedimento de Salvar e direcionar a Sub-OS é válido para todas as atividades, ou seja, no exemplo que está sendo relatado, ao finalizar a atividade, pode-se novamente **"Salvar e Fechar OS"**, **"Salvar e Abrir Sub-OS"** ou **"Encaminhar"** a OS.

**Importante:** Quando duas ou mais atividades estiverem configuradas em um mesmo **"Nível"**, o encaminhamento da OS para estas, será feito de acordo com a configuração do Processo.

Sendo assim, se a opção **"Selecionar próxima atividade?"** estiver assinalada como **"Sim"**, o usuário da atividade anterior poderá selecionar qual das atividades será realizada na próxima etapa.

Se a opção Selecionar próxima atividade? estiver marcada como **"Não"**, no encerramento da atividade anterior, o sistema encaminhará automaticamente as atividades do nível seguinte aos executantes configurados para realizá-las.

Para o fechamento do fluxo do processo, a OS somente poderá ser encerrada, quando a atividade for a última do processo, ou a partir do item cuja atividade possua a opção **"Pode concluir processo?"** assinalada como **"Sim"**. Neste caso, você poderá concluir o processo **"Fechando a OS"** sem passar para os outros níveis, desde que nenhuma atividade anterior esteja pendente.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604854-Processos-de-Servi%C3%A7o#top)

## Parâmetros que influenciam nesta tela

**Filtrar serviços pelo 'Uso produto' - SERVFILUSOPROD:** Com este parâmetro desligado o sistema lista todos os produtos cadastrados independente do que estiver configurado no campo **"Usado Como"** do Cadastro de Produto. Se habilitado trará para o campo Serviço, somente serviços.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604854-Processos-de-Servi%C3%A7o#top)
