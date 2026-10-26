---
id: "4403903691799"
titulo: "Tarefas de Serviço com Web Service Interno"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4403903691799-Tarefas-de-Servi%C3%A7o-com-Web-Service-Interno"
trilha: "Manual do Produto > Plataforma e Integrações > Flow"
atualizado_em: "2026-10-01T00:42:14Z"
rotulos: ["Configuração", "Integração", "Estoque", "sankhyaflow", "Tarefas de Serviço com Web Service Interno", "Conecta SankhyaFlow aos serviços do Sankhya Om", "Aprova amostras no Controle de Qualidade", "Usa Web Service Interno sem Java", "Web Service Interno"]
---

# Tarefas de Serviço com Web Service Interno

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42313315342103) Versão disponível: a partir da 4.4
```

---

Esse é um recurso existente em tarefas de serviço do SankhyaFlow, que permite integrar processos de negócios em execução na ferramenta com os demais serviços nativos do Sankhya Om, possibilitando enviar e receber dados.

A utilização de uma tarefa de serviço com Web Service Interno no Flow realiza a integração com recursos nativos de nosso ERP sem a necessidade de desenvolvimento utilizando módulos Java, o que o torna mais simples e rápido, possibilitando aproveitar as rotinas já existentes no Sankhya Om e acrescentar novas funcionalidades no Flow, sem que seja necessário desenvolver rotinas do ERP a partir do zero.

Nesse artigo, você terá acesso aos seguintes tópicos:

---

1. [Caso de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403903691799-Tarefas-de-Servi%C3%A7o-com-Web-Service-Interno#casodeuso)
2. [Configurando tarefa de serviço com Web Service Interno](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403903691799-Tarefas-de-Servi%C3%A7o-com-Web-Service-Interno#configurandotarefadeservi%C3%A7ocomwebserviceinterno)
3. [Resultados](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403903691799-Tarefas-de-Servi%C3%A7o-com-Web-Service-Interno#resultados)

---

#### Caso de Uso

Na imagem abaixo, temos a representação do processo de [Controle de Qualidade de Matérias Primas](https://drive.google.com/drive/folders/1GSZI4NXqBmW_90vwrYt99eyK7CzTbYKt) de uma indústria. Esse processo tem o objetivo de analisar os padrões de qualidades de matérias primas adquiridas de fornecedores antes da disponibilização para a etapa de fabricação. Ocorrem etapas de coletas, validação e revisão de uma amostra e, na sequência, a geração do laudo; assim, havendo aprovação em todas as etapas, a matéria prima é liberada para as áreas de produção da indústria.

![Imagem 2: Na imagem abaixo, temos a representação do processo de Controle de Qualidade de Matérias Primas de uma indústria. Esse…](https://ajuda.sankhya.com.br/hc/article_attachments/4403903985431)

| **Processo de Controle de Qualidade** |
| --- |

Em nosso caso de uso, iremos configurar a tarefa de serviço **"Aprovação da amostra"** (destacada em amarelo na imagem acima) com Web Service Interno para, a partir do Flow, aprovarmos amostras utilizando o serviço nativo do Sankhya Om.

É importante ressaltar que o serviço nativo de aprovação de amostrar, quando acionado, registra diversas operações nos módulos de nosso ERP, dentre elas, a baixa de estoque da amostra que foi coletada.

![Imagem 3: Com o Web Service Interno teremos apenas scripts para chamarmos o serviço de aprovação de amostra. Dessa forma, não…](https://ajuda.sankhya.com.br/hc/article_attachments/16117217120023) Com o Web Service Interno teremos apenas scripts para chamarmos o serviço de aprovação de amostra. Dessa forma, não teremos a necessidade de desenvolver códigos complexos em nosso processo de negócio com finalidade específica de gerar essas baixas, o que torna o desenvolvimento de scripts mais simples.

Também utilizaremos dados de retorno do serviço para registrar o número da requisição de baixa de estoque no formulário do Flow, para visualização em tarefas subsequentes, garantindo melhor rastreabilidade das informações do processo.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403903691799-Tarefas-de-Servi%C3%A7o-com-Web-Service-Interno#top)

#### Configurando tarefa de serviço com Web Service Interno

---

**Identificando o Serviço**

O primeiro passo para configurar uma tarefa de serviço com Web Service é identificar qual serviço nativo do ERP iremos utilizar. Uma maneira prática para identificá-lo é acessar o recurso nativo do ERP e executá-lo.

Em nosso exemplo, para identificar o serviço da tarefa Aprovação de amostra, iremos acessar a tela [Registro de Amostras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611334-Registro-de-Amostras) do Sankhya Om e deixar a amostra no ponto para ser aprovada (preencher os campos **"Dh. Amostragem"** e **"Dh. Verificação"**) ou seja, momento antes da execução do serviço que iremos identificar.

![Imagem 4: Em nosso exemplo, para identificar o serviço da tarefa Aprovação de amostra , iremos acessar a tela Registro de…](https://ajuda.sankhya.com.br/hc/article_attachments/4403910480791)

| **Tela Registro de Amostras** |
| --- |

Antes de clicar no botão ![Imagem 5: Antes de clicar no botão "Aprovar" , abra a ferramenta de desenvolvimento do seu navegador para que possamos localizar…](https://ajuda.sankhya.com.br/hc/article_attachments/4403904285463) **"Aprovar"**, abra a ferramenta de desenvolvimento do seu navegador para que possamos localizar o serviço que será executado quando tentarmos aprovar a amostra.

Nesse exemplo, estamos utilizando o navegador Mozilla Firefox. Assim, após pressionar a tecla **"F12"** (atalho para ferramentas de desenvolvimento), a janela abaixo será aberta. Na sequência, acesse a aba **"Rede"** para consultar o serviço que será utilizado para aprovar a amostra:

![Imagem 6: Nesse exemplo, estamos utilizando o navegador Mozilla Firefox . Assim, após pressionar a tecla "F12" (atalho para…](https://ajuda.sankhya.com.br/hc/article_attachments/4403910579991)

| **Propriedades da Página** |
| --- |

Nesse momento, na tela de Registro de Amostras, clique no botão Aprovar. Então, após a aprovação, será apresentado o registro do serviço que foi utilizado, conforme destacado na imagem abaixo:

![Imagem 7: Nesse momento, na tela de Registro de Amostras , clique no botão Aprovar . Então, após a aprovação, será apresentado o…](https://ajuda.sankhya.com.br/hc/article_attachments/4403910790679)

| **Serviço Identificado** |
| --- |

Ao clicar sobre o serviço, será apresentado o cabeçalho. Nele podemos consultar informações importantes como o nome do serviço apresentado no campo **"serviceName"** (que será utilizado na configuração do Web Service Interno).

Também é possível visualizar no cabeçalho o **"Content-Type"**, que define o formato aceito pelo serviço para gerar a requisição, podendo ser JSON ou XML.

**Observação:** o formato aceito determinará a forma como iremos chamar o serviço. No exemplo da imagem abaixo, temos o formato JSON:

![Imagem 8: Observação: o formato aceito determinará a forma como iremos chamar o serviço. No exemplo da imagem abaixo, temos o…](https://ajuda.sankhya.com.br/hc/article_attachments/4403910840727)

| **Primeira parte do cabeçalho do serviço** |
| --- |

![Imagem 9: Primeira parte do cabeçalho do serviço](https://ajuda.sankhya.com.br/hc/article_attachments/4403910861975)

| **Segunda parte do cabeçalho do serviço** |
| --- |

![Imagem 10: Se o formato fosse XML, em "Content-Type" teríamos: 'text/xml;charset=UFT-8' .](https://ajuda.sankhya.com.br/hc/article_attachments/16117217120023) Se o formato fosse XML, em **"Content-Type"** teríamos: **'text/xml;charset=UFT-8'**.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403903691799-Tarefas-de-Servi%C3%A7o-com-Web-Service-Interno#configurandotarefadeservi%C3%A7ocomwebserviceinterno) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403903691799-Tarefas-de-Servi%C3%A7o-com-Web-Service-Interno#top)

---

**Identificação dos Parâmetros da Requisição do Serviço**

Acessando a aba **"Requisição"**, podemos verificar os parâmetros que foram utilizados para a chamada do serviço.

Conforme podemos visualizar na imagem abaixo, a requisição contém o nome do serviço e seus parâmetros são apresentados em **"requestBody"**. Nesse caso, verificamos que nessa chamada foi requisitada a aprovação da amostra de número 53:

![Imagem 11: Conforme podemos visualizar na imagem abaixo, a requisição contém o nome do serviço e seus parâmetros são apresentados…](https://ajuda.sankhya.com.br/hc/article_attachments/4403911076631)

| **Requisição do Serviço** |
| --- |

**Observação:** o conteúdo contido em **"requestBody"** será utilizado para definirmos o script de requisição na nossa tarefa de serviço **"Aprovação da amostra"**.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403903691799-Tarefas-de-Servi%C3%A7o-com-Web-Service-Interno#configurandotarefadeservi%C3%A7ocomwebserviceinterno) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403903691799-Tarefas-de-Servi%C3%A7o-com-Web-Service-Interno#top)

---

**Identificação de Dados da Resposta do Serviço**

A visualização do retorno de serviço é apresentada na aba **"Resposta"**. No exemplo da imagem abaixo, foi respondido o status = 1. Por padrão do Sankhya Om, quando o status for 1, significa que houve sucesso na tentativa de execução do processo, no caso, a aprovação da amostra:

![Imagem 12: A visualização do retorno de serviço é apresentada na aba "Resposta" . No exemplo da imagem abaixo, foi respondido o…](https://ajuda.sankhya.com.br/hc/article_attachments/4403904988311)

| **Propriedade de Retorno do Serviço** |
| --- |

**Nota:** quando o resultado for diferente de 1, significa que por algum motivo não houve sucesso na requisição solicitada.

**![Imagem 13: Importante: os dados da resposta poderão facilmente serem registrados em campos de formulários do Flow , que será…](https://ajuda.sankhya.com.br/hc/article_attachments/16117217120023) Importante:** os dados da resposta poderão facilmente serem registrados em campos de formulários do Flow, que será apresentado em exemplo no decorrer desse artigo.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403903691799-Tarefas-de-Servi%C3%A7o-com-Web-Service-Interno#configurandotarefadeservi%C3%A7ocomwebserviceinterno) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403903691799-Tarefas-de-Servi%C3%A7o-com-Web-Service-Interno#top)

---

**Configurando a Tarefa de Serviço com Web Service Interno**

Para a tarefa de serviço **"Aprovação da amostra"**, selecione o tipo de serviço **"Web Service Interno"** e, em seguida, clique no botão de configurações. Após isso, procure pelo serviço de aprovação de amostra que identificamos anteriormente (RegistroAmostraSP.aprovarReprovarAmostra). Observe abaixo:

[GIF animado: Imagem 14: Para a tarefa de serviço "Aprovação da amostra" , selecione o tipo de serviço "Web Service Interno" e, em seguida,…](https://ajuda.sankhya.com.br/hc/article_attachments/4403911395095)

| **Configuração do Web Service e Pesquisa do Serviço** |
| --- |

Agora já podemos definir o script de requisição do serviço de aprovação. Em tarefas anteriores do processo, será registrado o número da amostra em campo do formulário. Como esse é o parâmetro que identificamos como necessário para a requisição, vamos definir uma variável (nuAmostra) para registrar esse número e utilizá-la na requisição. Nesse exemplo, a requisição será realizada para o formato JSON que foi identificado anteriormente no cabeçalho:

![Imagem 15: Agora já podemos definir o script de requisição do serviço de aprovação. Em tarefas anteriores do processo, será…](https://ajuda.sankhya.com.br/hc/article_attachments/4403911543959)

| **Script da Requisição** |
| --- |

Script completo contido na imagem acima:

| ``` //Variáveis para registrar o número da amostra inserido em campo de formulário do Flow var buscarFormulario = getLinhasFormulario("AD_TWFTGFRAM"); var nuAmostra = buscarFormulario[0].getCampo("NURAM"); //Parâmetros da requisição var payload = "{\"serviceName\":\"RegistroAmostrasSP.aprovarReprovarAmostra\",\"requestBody\":{\"params\":{\"isAprovacao\":true, \"nuRam\":[{\"$\":"+nuAmostra+"}]},\"clientEventList\":{\"clientEvent\":{\"$\":\"br.com.sankhya.actionbutton.clientconfirm\"}]}}}"; //A função JSON.parse() converte texto para formato JSON var payloadJS = JSON.parse(payload); return payloadJS ``` |
| --- |

Observe que declaramos a variável **"payload"** com todos os parâmetros de requisição que havíamos identificado anteriormente e, no lugar do número da amostra, inserimos a variável **"nuAmostra"**, que se refere a um valor registrado anteriormente em formulário do Flow.

Caso o serviço identificado no cabeçalho aceitasse apenas o formato XML, a requisição seria realizada nesse formato, conforme o script abaixo:

| ``` //Variáveis para registrar o número da amostra inserido em campo de formulário do Flow var buscarFormulario = getLinhasFormulario("AD_TWFTGFRAM"); var nuAmostra = buscarFormulario[0].getCampo("NURAM"); //Parâmetros da requisição return     "<params isAprovacao=true><nuRam>"+nuAmostra+"</nuRam></params>"; ``` |
| --- |

**Observação:** a **"nuAmostra"** representa a variável que deve ser declarada para obter o valor do campo contido no formulário.

Após definidas as configurações da requisição, podemos também configurar o retorno da requisição, sendo possível obter dados desse retorno e registrar em campos de formulários do Flow.

Em nosso exemplo, quando uma amostra é aprovada, é gerada uma mensagem de aprovação pelo Sankhya Om e um número de requisição da baixa de estoque da amostra. Iremos obter esse número pelo retorno do Web Service e registrar em campo do Flow, para que esse dado possa ser consultado nas tarefas subsequentes do processo.

**Nota:** o retorno de dados do Web Service sempre é obtido utilizando a variável **"retornoWSI"**.

Como já vimos anteriormente, o retorno do Web Service de aprovação contém os seguintes dados:

![Imagem 16: Como já vimos anteriormente, o retorno do Web Service de aprovação contém os seguintes dados:](https://ajuda.sankhya.com.br/hc/article_attachments/4403911664407)

| **Retorno do Serviço** |
| --- |

No script, iremos armazenar na variável **"retornoJS"** todo o conteúdo do retorno. Na variável **"retornoString"** vamos obter o conteúdo do objeto **"{msg'.$}"** e, por fim, registramos a variável **"retornoString"** no campo **"NUMREQ"**, que pertence ao formulário do Flow, utilizando funções para selecionar apenas os números:

![Imagem 17: No script, iremos armazenar na variável "retornoJS" todo o conteúdo do retorno. Na variável "retornoString" vamos obter…](https://ajuda.sankhya.com.br/hc/article_attachments/4403911710231)

| **Configuração do script de Retorno** |
| --- |

Script completo de retorno:

| ``` //JSON.parse() realiza a conversão do conteúdo para string var retornoJS = JSON.parse(retornoWSI); //Obtém o conteúdo específico do objeto  var retornoString = retornoJS.msg.$; //Identifica na mensagem o número da requisição e registra no campo do formulário do Flow o número da requisição, utilizando  o “método replace(), que retorna uma nova string com algumas ou todas as correspondências de um padrão substituídas por um  determinado caractere (ou caracteres)”. var buscarFormulario = getLinhasFormulario("AD_TWFTGFRAM"); buscarFormulario[0].setCampo("NUMREQ",retornoString.replace(/\D/g, '')); ``` |
| --- |

Realizadas as configurações de requisição e retorno do Web Service, basta salvar e publicar o processo.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403903691799-Tarefas-de-Servi%C3%A7o-com-Web-Service-Interno#configurandotarefadeservi%C3%A7ocomwebserviceinterno) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403903691799-Tarefas-de-Servi%C3%A7o-com-Web-Service-Interno#top)

#### Resultados

Para visualizar o resultado das configurações, acesse a [Lista de Tarefas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595434-Lista-de-Tarefas) e inicie o processo **"Controle de Qualidade de Matérias Primas"**. Em seguida, finalize as atividades **"Coletar amostra"** e **"Validar amostra colhida"**, e aprove a tarefa **"Analisar amostra"**.

Na sequência, o fluxo irá executar a tarefa de serviço com Web Service Interno **"Aprovação da amostra"** que configuramos anteriormente.

O Web Service realiza a aprovação da amostra e a mesma é direcionada para a tarefa de usuário seguinte (Gerar laudo), em que podemos verificar que o número da requisição de baixa foi identificado no retorno do Web Service e inserido no campo específico que determinamos no script de retorno:

![Imagem 18: O Web Service realiza a aprovação da amostra e a mesma é direcionada para a tarefa de usuário seguinte ( Gerar laudo ),…](https://ajuda.sankhya.com.br/hc/article_attachments/4403905591575)

| **Tela do processo no Flow após execução da Tarefa de Serviço** |
| --- |

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403903691799-Tarefas-de-Servi%C3%A7o-com-Web-Service-Interno#top)
