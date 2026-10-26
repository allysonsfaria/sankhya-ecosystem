---
id: "4403954451735"
titulo: "Tarefas de Serviço com Web Service Externo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4403954451735-Tarefas-de-Servi%C3%A7o-com-Web-Service-Externo"
trilha: "Manual do Produto > Plataforma e Integrações > Flow"
atualizado_em: "2026-07-29T15:09:11Z"
rotulos: ["Configuração", "Parceiro", "Integração", "sankhyaflow", "Tarefas de Serviço com Web Service Externo", "Cadastro", "Define URL e método de requisição", "Cadastro de fornecedores usando ReceitaWS", "Conecta SankhyaFlow a serviços externos", "Web Service Externo"]
---

# Tarefas de Serviço com Web Service Externo

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42313270596631) Versão disponível: a partir da 4.4
```

---

Esse é um recurso existente em tarefas de serviço do SankhyaFlow, que permite integrar processos de negócios em execução na ferramenta com os serviços externos ao Sankhya Om, possibilitando enviar e receber dados.

A tarefa de serviço com Web Service Externo será utilizada quando houver a necessidade de integrar um processo do SankhyaFlow com serviços externos ao Sankhya Om. Com esse recurso será possível configurar uma integração com serviço externo, sem a necessidade de desenvolvimento utilizando módulos Java, o que torna o desenvolvimento mais simples e rápido.

Nesse artigo, você terá acesso aos seguintes tópicos:

---

1. [Caso de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403954451735-Tarefas-de-Servi%C3%A7o-com-Web-Service-Externo#casodeuso)
2. [Configurando tarefa de serviço com Web Service Externo](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403954451735-Tarefas-de-Servi%C3%A7o-com-Web-Service-Externo#configurandotarefadeservi%C3%A7ocomwebserviceexterno)
3. [Outras configurações de chamada de um Serviço Externo](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403954451735-Tarefas-de-Servi%C3%A7o-com-Web-Service-Externo#outrasconfigura%C3%A7%C3%B5esdechamadadeumservi%C3%A7oexterno)
4. [Resultados](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403954451735-Tarefas-de-Servi%C3%A7o-com-Web-Service-Externo#resultados)

---

#### Caso de Uso

A empresa Beta SA utiliza o SankhyaFlow para realizar o [Cadastro de seus fornecedores](https://drive.google.com/drive/folders/1WxeapXFP8oBi6lP-d7mgtUEUetudV4Ra), conforme o fluxo da imagem abaixo:

![Imagem 2: A empresa Beta SA utiliza o SankhyaFlow para realizar o Cadastro de seus fornecedores , conforme o fluxo da imagem…](https://ajuda.sankhya.com.br/hc/article_attachments/4403954620695)

| **Cadastro de Fornecedor** |
| --- |

Na etapa de **"Abertura da solicitação"**, o solicitante do cadastro informa os dados de identificação do fornecedor e, caso o cadastro seja de um fornecedor Pessoa Jurídica, a empresa integra e recebe automaticamente os dados de um parceiro externo, obtendo a razão social, nome fantasia, endereço completo e o telefone desse fornecedor.

Essa integração é importante para a empresa automatizar o preenchimento desses dados e também para evitar erros no cadastro das informações.

Em seguida, o fluxo segue para o setor fiscal definir regras tributárias e para um gestor revisar todas as informações preenchidas e concluir o processo.

![Imagem 3: A integração servirá somente para fornecedores Pessoa Jurídica .](https://ajuda.sankhya.com.br/hc/article_attachments/16116678005655) A integração servirá somente para fornecedores Pessoa Jurídica.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403954451735-Tarefas-de-Servi%C3%A7o-com-Web-Service-Externo#top)

#### Configurando tarefa de serviço com Web Service Externo

---

**Identificação de características e dados do serviço externo**

O primeiro passo para configurar uma tarefa de serviço com Web Service Externo, é verificar junto ao parceiro externo as características do serviço a ser consumido, como URL para requisição (se houver), método de requisição (GET ou POST), tipo de envio (JSON, XML ou outros) e etc.

O parceiro externo chamado **"ReceitaWS"** disponibilizou as seguintes informações:

- URL para requisição: <https://www.receitaws.com.br/v1/cnpj/[cnpj]>
- Exemplo de requisição: <https://www.receitaws.com.br/v1/cnpj/27865757000102>
- Tipo de envio: JSON
- Campos da matriz JSON do retorno.

Mais informações sobre o serviço podem ser consultadas em: <https://receitaws.com.br/api>

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403954451735-Tarefas-de-Servi%C3%A7o-com-Web-Service-Externo#configurandotarefadeservi%C3%A7ocomwebserviceexterno) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403954451735-Tarefas-de-Servi%C3%A7o-com-Web-Service-Externo#top)

---

**Configurando a tarefa de serviço com Web Service Externo**

Em nosso caso de uso, devemos abrir a solicitação e informar na abertura do processo, o tipo de pessoa (jurídica ou física). Quando informarmos o tipo pessoa jurídica, será apresentado o campo para preenchimento do número do CNPJ.

Após iniciar o processo, iremos executar a tarefa de serviço e apresentar na tela o link para revisar as informações obtidas no site ReceitaWS e complementar o cadastro. Dessa forma, necessitamos configurar a tarefa de serviço **"Busca dados na Receita WS"** para identificar o CNPJ que será consultado, obter os dados na ReceitaWS e retornar as informações no formulário nativo utilizado para cadastrar o parceiro fornecedor.

Inicialmente, devemos configurar o **"Tipo de serviço"** da tarefa com **"Web Service Externo"** e, em seguida, clicar no botão de configuração ![Imagem 4: Inicialmente, devemos configurar o "Tipo de serviço" da tarefa com "Web Service Externo" e, em seguida, clicar no botão…](https://ajuda.sankhya.com.br/hc/article_attachments/4403960487063):

[GIF animado: Imagem 5: Inicialmente, devemos configurar o "Tipo de serviço" da tarefa com "Web Service Externo" e, em seguida, clicar no botão…](https://ajuda.sankhya.com.br/hc/article_attachments/4404173633175)

| **Configuração do Tipo de Serviço da Tarefa de Serviço e botão de Configuração** |
| --- |

Após clicar no botão de configuração, será aberta a tela para configurar a integração (Web Service Externo) com o serviço externo.

Considerando os dados fornecidos pelo parceiro externo, iremos configurar agora como será realizada a requisição (chamada) do serviço externo.

Em nosso caso de uso, o parceiro disponibilizou uma URL para realizar a requisição, então, iremos informá-la no campo URL.

O método da requisição é do tipo **"GET"** e o tipo de envio utiliza o padrão JSON pra enviar e receber dados. Dessa forma, a configuração da requisição será realizada de acordo com a imagem abaixo:

![Imagem 6: O método da requisição é do tipo "GET" e o tipo de envio utiliza o padrão JSON pra enviar e receber dados. Dessa forma,…](https://ajuda.sankhya.com.br/hc/article_attachments/4403960497559)

| **Configuração da Requisição do Serviço** |
| --- |

Note que em **"Variáveis da URL"** temos um script que retorna o número do CNPJ que será utilizado na requisição. Esse dado será informado no campo **"CGC\_CPF"** do formulário nativo utilizado na abertura do processo. O CNPJ obtido será utilizado para complementar a URL para realizar a requisição do serviço.

Script utilizado em Variáveis da URL:

| ``` // A função getLinhasFormularioNativo obtém o CNPJ informado no campo "CGC_CPF" na abertura  do processo e utiliza na requisição var buscarFormulario = getLinhasFormularioNativo("Parceiro"); var cnpj = buscarFormulario[0].getCampo("CGC_CPF"); return cnpj; ``` |
| --- |

Concluídas as configurações da requisição do serviço, já podemos configurar o retorno do serviço e o registro dos dados obtidos nos respectivos campos do formulário nativo.

No cadastro de parceiro fornecedor, iremos obter vários dados no site ReceitaWS e registrá-los no formulário nativo.

Para os dados de endereço (logradouro, bairro e cidade) haverão validações para verificar se já existe o cadastro no Sankhya Om. Se existir será aproveitado o registro já existente e, caso não exista, será realizado o registro do dado no ERP e sua utilização do formulário nativo.

Na imagem abaixo, temos a tela de configuração do retorno do serviço:

![Imagem 7: Na imagem abaixo, temos a tela de configuração do retorno do serviço:](https://ajuda.sankhya.com.br/hc/article_attachments/4403955041175)

| **Configuração do Retorno do Serviço** |
| --- |

Os dados do Retorno do Serviço sempre serão obtidos por meio da variável **"retornoWSE"**. A seguir temos o script utilizado para obter os dados, cadastrar dados relacionados a endereços no ERP e registrar nos campos do formulário nativo.

Script acima completo:

| ``` // A variável 'retornoWSE' armazena todo o conteúdo do retorno. A função JSON.parse() converte texto para formato JSON. var retornoJS = JSON.parse(retornoWSE); // Declaração de variáveis para armazenar o status e mensagem do retorno. var status = retornoJS.status; var mensagemStatus = retornoJS.message; // Se o serviço retornar erro para o CNPJ informado é emitida uma mensagem na abertura do processo. if (status === "ERROR" ) {     throw new Error (mensagemStatus); } //Se não houve erro declara variáveis para cada para cada propriedade do retorno e registra no formulário. else{     var nome = retornoJS.nome;     //O método substring() retorna a parte da string entre os índices inicial e final, ou até o final da string.       Utilizamos para obter os primeiros 40 caracteres aceitos pelo campo.     var nometrunc = nome.substr(0, 40);     var fantasia = retornoJS.fantasia;     var fantasiatrunc = fantasia.substr(0, 40);     var numero = retornoJS.numero;     var complemento = retornoJS.complemento;     var complementotrunc = complemento.substr(0, 30);     var cep = retornoJS.cep;     //O “método replace(), que retorna uma nova string com algumas ou todas as correspondências de um padrão         substituídas por um determinado caractere (ou caracteres)”, no caso estamos retirando o ponto e traço do CEP.    cep = cep.replace(/\.|\-/g, '');     var uf = retornoJS.uf;     var email = retornoJS.email;     var telefone = retornoJS.telefone;     telefone = telefone.replace(/\.|\-/g, '');     telefonetrunc = telefone.substr(0, 13);     //cria uma nova linha no formulário nativo para armazenado dos dados das variáveis     var registrarDados = novaLinhaFormularioNativo("Parceiro");     //registra os dados armazenados nas variáveis nos campos do formulário nativo     registrarDados.setCampo('RAZAOSOCIAL', nometrunc);     registrarDados.setCampo('NOMEPARC', fantasiatrunc);     registrarDados.setCampo('NUMEND', numero); registrarDados.setCampo('COMPLEMENTO', complementotrunc);     registrarDados.setCampo('CEP', cep);     registrarDados.setCampo('INSCESTADNAUF', uf);     registrarDados.setCampo('EMAIL', email);     registrarDados.setCampo('TELEFONE', telefone);     //Tratativa do nome da rua retornado no JSON (ex. de retorno: Av Rondon Pacheco),        utilizamos a função split para quebrar o texto em array e obter somente o nome da rua     var enderecoJson v retornoJS.logradouro;     var enderecoArray = enderecoJson.split(" ");     endereco = "";      if(enderecoArray.length > 1){         tipo = enderecoArray[0];         for (i=1; i<enderecoArray.length; i++){             endereco += enderecoArray[i] += ' ';         }         endereco = endereco.substring(0,endereco.length -1);     }     //Verifica se já existe o nome do endereço (logradouro) informado no retorno cadastrado no SankhyaOm     var buscaCodEnd = buscarDado(['CODEND'],'TSIEND','NOMEEND = :NOMEEND',[endereco]);     //Se já existir registra o código da rua no formulário nativo     if  (buscaCodEnd != undefined || buscaCodEnd != null) {          registrarDados.setCampo('CODEND', buscaCodEnd);          }     else {         //Caso o logradouro ainda não exista no SankhyaOm, registra o logradouro,           data da alteração no formulário nativo e registra no SankhyaOm         var novoEndereco = novaLinha("TSIEND");         novoEndereco.setCampo("NOMEEND", endereco);           var TipoLogradArray = enderecoJson.split(" ");         tipoLogradouro = TipoLogradArray[0];         novoEndereco.setCampo("TIPO", tipoLogradouro);         novoEndereco.save();          //Obtém o código do novo logradouro e registra no formulário nativo         var codigo = novoEndereco.getCampo("CODEND");         registrarDados.setCampo('CODEND', codigo);     }          //Verifica se já existe o nome do bairro informado no retorno no SankhyaOm var bairro = retornoJS.bairro;     var buscaCodBai = buscarDado(['CODBAI'],'TSIBAI','NOMEBAI = :NOMEBAI',[bairro]);     if  (buscaCodBai != undefined || buscaCodBai != null) {         //Encontrou bairro no sistema e registra no formulário do Flow         registrarDados.setCampo('CODBAI', buscaCodBai);      }      else {         //Não encontrou bairro no sistema e realiza cadastro         var novoBairro = novaLinha("TSIBAI");           novoBairro.setCampo("NOMEBAI", bairro);           novoBairro.save();         //Obtém o código do novo bairro e registra no formulário nativo         var codigoBairro = novoBairro.getCampo("CODBAI");         registrarDados.setCampo('CODBAI', codigoBairro);     }              //Verifica se já existe o nome da cidade informada no retorno no SankhyaOm, considerando nome da cidade UF        informados no retorno     var cidade = retornoJS.municipio;     var buscaCodCid = buscarDado(['CODCID'],'TSICID','NOMECID = :NOMECID',[cidade] ,'AND UF = :UF',[uf]);     //Se existe a cidade cadastrada no SankhyaOm, registra no formulário do Flow.     if  (buscaCodCid != undefined || buscaCodCid != null) {         //Encontrou cidade no sistema         registrarDados.setCampo('CODCID', buscaCodCid);        }      else {         //Não encontrou cidade no sistema e vai cadastra no SankhyaOm         var novaCidade = novaLinha("TSICID");           novaCidade.setCampo("NOMECID", cidade);         var buscaCodUf = buscarDado(['CODUF'],'TSIUFS','UF = :UF',[uf]);        novaCidade.setCampo("UF", buscaCodUf);         novaCidade.save();         //Obtém o código da nova cidade e registra no formulário nativo         var codigoCidade = novaCidade.getCampo("CODCID");         registrarDados.setCampo('CODCID', codigoCidade);     }   } ``` |
| --- |

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403954451735-Tarefas-de-Servi%C3%A7o-com-Web-Service-Externo#configurandotarefadeservi%C3%A7ocomwebserviceexterno) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403954451735-Tarefas-de-Servi%C3%A7o-com-Web-Service-Externo#top)

#### Outras configurações de chamada de um Serviço Externo

A aba **"Envio"** será utilizada quando o serviço aceitar somente a URL contendo o payload, então nessa aba o modelador deverá descrever esse payload de chamada do serviço, conforme as imagens abaixo:

![Imagem 8: A aba "Envio" será utilizada quando o serviço aceitar somente a URL contendo o payload, então nessa aba o modelador…](https://ajuda.sankhya.com.br/hc/article_attachments/4403955264663)

| **Configuração do Retorno do Serviço** |
| --- |

![Imagem 9: Configuração do Retorno do Serviço](https://ajuda.sankhya.com.br/hc/article_attachments/4403955326103)

| **Configuração do Retorno do Serviço** |
| --- |

Na aba **"Requisição"** temos o botão **"Cabeçalho" ![Imagem 10: Na aba "Requisição" temos o botão "Cabeçalho" , que possibilita definir propriedades que serão utilizadas para…](https://ajuda.sankhya.com.br/hc/article_attachments/4403955347991)**, que possibilita definir propriedades que serão utilizadas para configurações adicionais na chamada da requisição, como por exemplo, tokens de validações, tipos de dados e etc.

Caso seja selecionada em **"Tipo de envio"** a opção **"Outros"**, seria necessário cadastrar através do botão Cabeçalho o **"Content-Type"** referente aos tipos de dados a serem enviados.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403954451735-Tarefas-de-Servi%C3%A7o-com-Web-Service-Externo#top)

#### Resultados

Após o término das configurações de requisição e retorno da tarefa de Web Service Externo, podemos executar o processo e verificar o resultado da integração.

Na tela de abertura do processo, iremos informar um CNPJ e clicar em iniciar:

![Imagem 11: Na tela de abertura do processo, iremos informar um CNPJ e clicar em iniciar:](https://ajuda.sankhya.com.br/hc/article_attachments/4403955402775)

| **Abertura do Processo do Cadastro do Fornecedor** |
| --- |

Após clicar em iniciar, a tarefa de serviço de Web Service Externo **"Busca dados na ReceitaWS"** é executada pelo sistema e disponibilizada pelo link para complementarmos os dados da solicitação:

![Imagem 12: Após clicar em iniciar, a tarefa de serviço de Web Service Externo "Busca dados na ReceitaWS" é executada pelo sistema…](https://ajuda.sankhya.com.br/hc/article_attachments/4404173503895)

| **Processo Iniciado** |
| --- |

Ao clicar em **"Complementar solicitação"**, a tarefa é aberta para o solicitante, conforme o exemplo da imagem abaixo:

![Imagem 13: Ao clicar em "Complementar solicitação" , a tarefa é aberta para o solicitante, conforme o exemplo da imagem abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/4404173524887)

| **Tarefa "Complementar solicitação"** |
| --- |

Na imagem acima, podemos visualizar que os campos de identificação e endereço foram preenchidos automaticamente após a execução da tarefa de Web Service Externo, restando para preenchimento apenas a **"Insc. Estadual / Identidade"** e o **"Celular/Fax"**, visto que esses dados não são fornecidos pelo parceiro externo.

Essa integração e automação agiliza o processo de cadastro de fornecedores, diminui a probabilidade de erros operacionais na execução desses cadastros, bem como melhora a experiência dos executores de processos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403954451735-Tarefas-de-Servi%C3%A7o-com-Web-Service-Externo#top)
