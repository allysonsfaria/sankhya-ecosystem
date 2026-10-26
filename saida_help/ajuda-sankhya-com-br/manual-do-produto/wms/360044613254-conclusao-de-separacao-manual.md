---
id: "360044613254"
titulo: "Conclusão de Separação Manual"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613254-Conclus%C3%A3o-de-Separa%C3%A7%C3%A3o-Manual"
trilha: "Manual do Produto > Suprimentos e Estoque > WMS"
atualizado_em: "2026-07-29T14:14:33Z"
rotulos: ["AJUDA DO SKW", "manual", "Conferência", "Configuração", "WMS", "WMSVALCODVOLUSU", "BUSCAMANTARSEP", "Conclusão de Separação Manual", "PROIBEDIGCOLWMS", "UTILDIGCONWMS", "UTILDIGINVENWMS", "WMSOCULTCODBART", "WMSTMINDIG", "WMSVALCHKCONFPD", "br.com.sankhya.wms.conclusaoseparacaomanual", "Conclusão de Separação Manual manual", "Rotinas", "Estoque", "Configurações Iniciais para Separação Manual", "Parâmetros para Execução da Separação", "Validação e Configuração de Parâmetros no WMS"]
---

# Conclusão de Separação Manual

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311547908887) Módulo: WMS > Rotinas
```

---

Neste artigo, trataremos sobre os comportamentos da tela Conclusão de Separação Manual, são eles:

- [Configurações Iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613254-Conclus%C3%A3o-de-Separa%C3%A7%C3%A3o-Manual#configura%C3%A7%C3%B5esiniciais)
- [Pedir confirmação na execução da tarefa de separação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613254-Conclus%C3%A3o-de-Separa%C3%A7%C3%A3o-Manual#pedirconfirma%C3%A7%C3%A3onaexecu%C3%A7%C3%A3odatarefadesepara%C3%A7%C3%A3o)
- [Parâmetros relacionados a esta rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613254-Conclus%C3%A3o-de-Separa%C3%A7%C3%A3o-Manual#par%C3%A2metrosrelacionadosaestarotina)

![Imagem 2: Parâmetros relacionados a esta rotina](https://ajuda.sankhya.com.br/hc/article_attachments/360061028554)

## Configurações Iniciais

Informe nesta tela a Área de Separação (área de conferência), a **"Empresa"**, a **"Ordem de Carga"**, o **"Número do Pedido"** e **"Executante"** que é o usuário que está concluindo a tarefa de separação.

Para concluir a Separação Por Pedido, será necessário informar o **"Endereço de Checkout"**, para onde a separação foi levada. O Endereço de Checkout é onde o pedido será conferido, e deverá ser o mesmo encontrado no campo **"Endereço"** do [Cadastro de Endereços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602274). Desta forma, quando o usuário clicar no botão **"Concluir tarefas"** o sistema substituirá o endereço indefinido, que estava no destino da tarefa, pelo endereço que foi informado na tela.

**Importante:** para conclusão desta tarefa, quando a separação for **"Por Produto"** não será necessário informar a **"Área de Separação"**, mesmo sendo de áreas de separação diferentes, mas para separações **"Por Pedido"** a informação da Área de Separação é obrigatória para conclusão da rotina.

**Nota:** no MGE WMS cada Área de Conferência tem seu intervalo de Endereço de Checkout, que poderá ser verificado em Arquivos/Cadastros/Área de Conferência, a conclusão da separação pelo **"Processo Manual do Sankhya-W"** irá validar se o endereço informado para Checkout realmente faz parte daquela Área de Conferência e, também validará se o endereço está ou não ocupado. Se sim, não será permitido o armazenamento neste.

**Observação:** se houver algum produto com reabastecimento pendente, o sistema indicará qual tarefa (separação) não poderá ser concluída, pois é pendente de outra tarefa (reabastecimento).

Após efetuar os reabastecimentos pendentes e concluir a separação, no WMS a situação da expedição tratada passará para **"Aguardando Conferência"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613254-Conclus%C3%A3o-de-Separa%C3%A7%C3%A3o-Manual#top)

## Pedir confirmação na execução da tarefa de separação

![clip0276](https://ajuda.sankhya.com.br/hc/article_attachments/360061028574)

Quando o parâmetro **"Busca manual de tarefas de separação? - BUSCAMANTARSEP"** estiver ligado, ao executar a tarefa de separação não será realizada a busca da próxima tarefa de forma automática; para executar a próxima tarefa, clique no botão **"Tarefa"**.

**Observação:** caso o referido parâmetro esteja desligado, o botão Tarefas não ficará visível.

![clip0277](https://ajuda.sankhya.com.br/hc/article_attachments/360061028594)

Na tarefa de Separação, ao clicar no botão **"Detalhes Produto"** o campo **"Produto"** possibilita bipar qualquer produto e verificar os detalhes do mesmo.

Ainda nesta rotina, temos o parâmetro **"Ocultar código de barras nos detalhes da tarefa? - WMSOCULTCODBART"** que, quando habilitado, não exibirá o código de barras na opção Detalhes do Produto na tela principal onde existem os dados dos produtos, assim como na mensagem de erro caso seja bipado o código de barras equivocadamente.

Para exemplificação e melhor entendimento desta funcionalidade, foi utilizado o código de barras "cbarras890".

Abaixo, temos a tela principal, na qual você pode notar a Descrição do Produto, com o parâmetro WMSOCULTCODBART desativado e, em seguida, ativado, respectivamente:

![clip0272](https://ajuda.sankhya.com.br/hc/article_attachments/360061944913)

![clip0273](https://ajuda.sankhya.com.br/hc/article_attachments/360061028614)

Abaixo, temos a tela **"Detalhes do produto"**, onde o parâmetro mencionado acima, apresenta desativado:

![clip0270](https://ajuda.sankhya.com.br/hc/article_attachments/360061028634)

Agora a mesma tela de Detalhes do produto, com o referido parâmetro ativado:

![clip0271](https://ajuda.sankhya.com.br/hc/article_attachments/360061028654)

Atualmente, ao solicitar a visualização dos Detalhes dos Produtos, teremos também a informação referente ao **"Agrupamento Mínimo"** do produto. Esta informação é inserida em cada item através da tela **"Cadastro de Produtos"**, aba **"Medidas e estoque"**, sub-aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#sub-abaestoque), campo **"Agrupamento mínimo"**.

![clip2641](https://ajuda.sankhya.com.br/hc/article_attachments/360061028674)

Por fim, note as mensagens que são apresentadas no caso de algum produto ser bipado equivocadamente. Primeiramente, com o parâmetro WMSOCULTCODBART desativado:

![clip0274](https://ajuda.sankhya.com.br/hc/article_attachments/360061028694)

Agora, com o parâmetro ativado:

![clip0275](https://ajuda.sankhya.com.br/hc/article_attachments/360061028714)

Na realização de alguma ação no coletor, se o sistema estiver aguardando a resposta do servidor, será exibida a mensagem:

**"Busca Próxima Tarefa. Tentando Conexão..."**

É verificada pelo sistema a quantidade de segundos que se deve aguardar, sendo que este tempo é configurado no parâmetro **"Tempo em seg. p/ timeout de conexão do coletor WMS - WMSTIMEOUTCON"**; ao final deste tempo, não obtendo resposta, será exibida a seguinte mensagem:

**"O servidor está demorando responder. Em X segundos voltaremos ao processo de espera de resposta."**

**Nota:** a mensagem acima, ficará "X" segundo sendo exibida na tela e, após este tempo, o sistema aguarda a quantidade de segundos configurados no parâmetro WMSTIMEOUTCON.

Após o sistema realizar este procedimento por dez vezes, será apresentada a mensagem:

**"Não foi possível recuperar uma resposta do servidor. Deseja tentar novamente?".**

Ao clicar em **"Sim"** na mensagem, o sistema reexecuta os passos anteriores; clicando em **"Não"**, será exibida a seguinte mensagem:

**"Conexão com problema!"**

No procedimento de **"Conferência"** e **"Conferência por Pedido"**, você pode utilizar o parâmetro **"Emite aviso de qtd. superior na conferência - EMIAVCONFSAIDA**" que, quando desativado, para cada item conferido que contenha a quantidade superior à solicitada, será apresentada uma única mensagem ao final da conferência. Este parâmetro por padrão é apresentado ativado.

![clip2649](https://ajuda.sankhya.com.br/hc/article_attachments/360061028734)

Na realização do processo de Separação no coletor, quando o parâmetro **"Endereço de checkout indefinido - ENDECKTINDEF"** estiver configurado e o parâmetro **"Usa end. de checkout adicional na separação - WMSUSACKADIC"** estiver habilitado, será solicitado que seja informado para cada item de separação, o endereço de destino.

Concluídas as tarefas de separação, ao informar os endereços referentes à conferência no campo solicitado, o valor na coluna **"Informado"** será modificado para **"Sim"**; até que todos os endereços sejam informados, não será possível dar continuidade à rotina de conferência. Uma vez informado o último endereço, tem-se a exibição de uma mensagem concluindo a operação e o consequente redirecionamento para continuidade na conferência.

![clip7395](https://ajuda.sankhya.com.br/hc/article_attachments/360061944953)

**Importante:** caso o parâmetro WMSUSACKADIC esteja habilitado, o parâmetro CKTINDEFAUTOM não poderá estar também ativado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613254-Conclus%C3%A3o-de-Separa%C3%A7%C3%A3o-Manual#top)

## Parâmetros relacionados a esta rotina

O parâmetro **"Exigir cadastro de volume por usuário no WMS? - WMSVALCODVOLUSU"**, por padrão, é apresentado ativado, de modo que faz-se necessário que sejam cadastradas as unidades dos produtos nas configurações por usuário no WMS. Se o parâmetro em questão for desativado, não será necessário efetuar o cadastro, sendo possível que o usuário tenha acesso a qualquer unidade no WMS.

Quando o parâmetro **"Valida endereço específico na conferência pedido? - WMSVALCHKCONFPD"** estiver habilitado, será feita a validação se o endereço bipado na conferência de pedidos é um checkout existente, apresentando no caso, uma mensagem sobre a não localização de um checkout para o endereço. Caso o parâmetro esteja desligado, quando um endereço específico for informado na conferência por pedidos e o mesmo não existe ou não possui conferência em andamento, o sistema procura por padrão a próxima conferência disponível para o usuário logado.

No parâmetro **"Tempo em ms para permitir digitação no coletor - WMSTMINDIG"**, informe o tempo máximo entre uma digitação de uma tecla e outra no coletor. Caso o intervalo de pressionamento seja maior que o tempo determinado neste parâmetro, será exibida uma mensagem de aviso, e o campo de código será limpo.

Quando os parâmetros **"Proibir digitação no coletor do WMS? - PROIBEDIGCOLWMS"** e **"Utilizar a proibição de digitação também nas conferências - UTILDIGCONWMS**" estiverem ativados, o coletor não irá permitir que alguns campos de código de barras sejam digitados manualmente, sendo necessário o uso do leitor de código de barras para tal procedimento. Além disto, com a ativação destes parâmetros, a rotina de **"Contagem de Estoque"** e as seguintes telas e campos de **"Conferência"** serão afetados:

- Conferência de pedido - Endereço Produto;
- Conferência - Endereço e Produto;
- Conferência de Saída - Endereço e Produto;
- Conferência de Entrada - Endereço e Produto;
- Conferência de volumes - Endereço e Volume.

De forma semelhante ao comportamento citado anteriormente, quando os parâmetros PROIBEDIGCOLWMS e **"Utilizar a proibição de digitação também no inventário - UTILDIGINVENWMS"** estiverem ativados, será proibida a digitação nos campos **"código de barras" e "código do endereço"** na função de **"Contagem de estoque (Inventário)"**.

**Nota:** o parâmetro PROIBEDIGCOLWMS foi alterado para tipo ‘Lista’ para que seja adicionada a opção **"Apenas endereços"**. Esta opção bloqueará somente a digitação de endereços nas telas do coletor. Com esta implementação, o parâmetro PROIBEDIGCOLWMS passa a ter as seguintes opções:

- Desligado: Não bloqueia a digitação;
- Endereços e Produtos: Bloqueia a digitação de endereços e produtos;
- Apenas endereços: Bloqueia apenas os endereços.

**Observação:** as telas **"Armazenagem Seletiva" e "Armazenamento Expresso"** não possuem a implementação que valida o bloqueio da digitação do endereço.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613254-Conclus%C3%A3o-de-Separa%C3%A7%C3%A3o-Manual#top)
