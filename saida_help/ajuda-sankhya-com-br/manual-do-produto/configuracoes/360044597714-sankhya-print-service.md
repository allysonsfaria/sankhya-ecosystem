---
id: "360044597714"
titulo: "Sankhya Print Service"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:46:33Z"
rotulos: ["Configuração", "Impressão", "Servidores de Impressão", "Trabalhos de Impressão", "Mapeamento", "Roteamento", "Sankhya Print Service", "SPSMAXTENTIMP", "SPSMINTMPTENT", "Usando o Componente do Servidor SPS", "Sankhya Print Service manual", "Nomes de Impressoras", "Serviços", "Rede", "Sankhya-Om"]
---

# Sankhya Print Service

Para expandir as capacidades de impressão do Sankhya-Om, foi criado o Sankhya Print Service (SPS), um sistema que permite a disponibilização de impressoras para os usuários do **Sankhya Om** sem a necessidade da configuração dessas impressoras em cada uma das máquinas do cliente.

O SPS é composto de 2 partes, que são, o Servidor SPS e o Componente SPS do Sankhya-Om.

O Servidor SPS registra todas as impressoras instaladas em uma máquina e permite que impressões sejam enviadas diretamente para o servidor via HTTP. Além disso, o servidor SPS oferece outros serviços, tais como listagem de impressoras, listagem de jobs, verificação de status e outros. O servidor SPS pode rodar em uma Linux ou Windows.

O Componente SPS, permite que sistema Sankhya-Om se conecte a um ou mais servidores SPS. Esses servidores são cadastrados no Sankhya-Om, e após esse cadastro, o sistema pode se conectar com qualquer um deles por HTTP. Dessa forma, até mesmo um servidor SPS externo (fora da intranet), pode ser adicionado.

O componente também fornece funcionalidades como:

- Roteamento de usuários, grupos e empresas;
- Controle de acesso a impressoras e servidores, por grupos e usuários;
- Exibição dos trabalhos de impressão;
- Seleção de Impressoras;
- Reimpressão.

![Imagem 1: Reimpressão.](https://ajuda.sankhya.com.br/hc/article_attachments/1500001302382)

Neste artigo, trataremos das funcionalidades, bem como das configurações necessárias para utilizar o SPS. Clique nos links abaixo para facilitar sua navegação:

| [Requisitos de Máquina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#:~:text=Rotinas%20do%20Sistema-,Requisitos%20de%20m%C3%A1quina,-Para%20garantir%20o) |
| --- |
| [Instalação do SPS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#instalaodosps) |
| [Verificando a Instalação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#verificandoainstalao) |
| [Configurando o Servidor SPS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#configurandooservidorsps) |
| [Utilizando o Console do Servidor SPS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#utilizandooconsoledoservidorsps) |
| [Utilizando o SPS no Sankhya-Om](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#utilizandoospsnosankhya-om) |
| [Roteamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#roteamento) |
| [Cadastros e Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#cadastroseconfigura%C3%A7%C3%B5es) |
| [Tipos de Roteamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#tiposderoteamento) |
| [Controle de Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#controledeacessos) |
| [Rotinas do Sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#rotinasdosistema) |

## Requisitos de Máquina

Para garantir o bom funcionamento do SPS, a máquina que servirá como servidor (seja física ou virtual) precisa ser dimensionada corretamente. É essencial levar em conta o volume total de impressões e o número de impressões simultâneas, que se refere à quantidade de impressoras conectadas ao servidor. Segue tabela de referência:  

![Imagem 2: Para garantir o bom funcionamento do SPS, a máquina que servirá como servidor (seja física ou virtual) precisa ser…](https://ajuda.sankhya.com.br/hc/article_attachments/34378209408535)

## Instalação do SPS

A instalação não requer nenhum tipo de configuração especial, para fazê-la, você deve seguir o procedimento padrão descrito abaixo:

**1.** Execute o instalador do **"Sankhya Print Service"**.

![Imagem 3: 1. Execute o instalador do "Sankhya Print Service" .](https://ajuda.sankhya.com.br/hc/article_attachments/4929930400919)

![Imagem 4: 1. Execute o instalador do "Sankhya Print Service" .](https://ajuda.sankhya.com.br/hc/article_attachments/4929930790935)

![Imagem 5: 1. Execute o instalador do "Sankhya Print Service" .](https://ajuda.sankhya.com.br/hc/article_attachments/4929930791191)

**2.** Clique em **"Avançar"**.

![Imagem 6: 2. Clique em "Avançar" .](https://ajuda.sankhya.com.br/hc/article_attachments/4929930824215)

**3.** Selecione uma pasta, ou mantenha a pasta padrão. 

![Imagem 7: 3. Selecione uma pasta, ou mantenha a pasta padrão.](https://ajuda.sankhya.com.br/hc/article_attachments/4929925951255)

**4.** Em seguida, clique em **"Avançar"**.

![Imagem 8: 4. Em seguida, clique em "Avançar" .](https://ajuda.sankhya.com.br/hc/article_attachments/4929951856151)

**5.** Nesta etapa, mantenha os campos **"Instalar o serviço sps-service"** e **"Iniciar arranque"** selecionados. 

![Imagem 9: 5. Nesta etapa, mantenha os campos "Instalar o serviço sps-service" e "Iniciar arranque" selecionados.](https://ajuda.sankhya.com.br/hc/article_attachments/4929930853143)

**6.** Clique em **"Avançar"**.

![Imagem 10: 6. Clique em "Avançar" .](https://ajuda.sankhya.com.br/hc/article_attachments/4929926008727)

![Imagem 11: 6. Clique em "Avançar" .](https://ajuda.sankhya.com.br/hc/article_attachments/4929930876439)

**7.** Para finalizar a instalação, clique em **"Terminar"**.

**Observação:** para tornar uma máquina local visível em nuvem, certifique-se de escolher a opção de instalação local e selecione o endereço adequado para a instalação do SPS. Além disso, realize as seguintes configurações:

- Configuração do Firewell:
  - No cliente onde a máquina local está localizada, acesse as configurações do firewall;
  - Certifique-se de que o firewall esteja configurado para permitir a comunicação através da porta 9091;
  - Verifique se o firewall está configurado para permitir o acesso externo ao endereço IP fixo da máquina local.
- Redirecionamento da porta 9091:
  - Acesse as configurações do roteador ou do dispositivo de rede responsável pela conexão da máquina local com a internet e procure pelas opções de redirecionamento de porta ou **"port forwarding"**;
  - Crie uma regra para direcionar a porta 9091 para o endereço IP local da máquina onde o SPS está instalado, certificando-se de salvar as configurações do roteador ou dispositivo de rede para que o redirecionamento de porta seja aplicado.
- Configuração do **Sankhya-Om**:
  - Acesse o sistema no navegador web e siga as instruções dele para entrar na área de configuração do SPS;
  - Insira as informações necessárias, como, o endereço IP fixo da máquina local e a porta 9091, de acordo com as configurações feitas anteriormente e finalize o processo seguindo as orientações específicas do **Sankhya-Om**.

Após concluir essas etapas, a máquina local estará visível para o sistema em nuvem, permitindo a integração e comunicação corretas com o **Sankhya-Om**. Lembre-se de realizar testes para garantir que a configuração esteja funcionando conforme o esperado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#top)

## Verificando a Instalação

Para verificar se o sistema foi instalado e iniciado corretamente, basta acessar no navegador, o endereço http://localhost:9091/index.html.

![Imagem 12: Para verificar se o sistema foi instalado e iniciado corretamente, basta acessar no navegador, o endereço…](https://ajuda.sankhya.com.br/hc/article_attachments/4905868593559)

Se a tela de login for exibida, o sistema está sendo executado corretamente.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#top)

## Configurando o Servidor SPS

A configuração do Sankhya Print Service pode ser realizada através de dois arquivos de configuração:

- config.properties
- log4j.conf

Esses arquivos estão localizados na pasta **"INSTALL\_DIR\conf"**, na qual INSTALL\_DIR é a pasta onde o servidor SPS foi instalado. Por exemplo:

![Imagem 13: Esses arquivos estão localizados na pasta "INSTALL_DIR\conf" , na qual INSTALL_DIR é a pasta onde o servidor SPS foi…](https://ajuda.sankhya.com.br/hc/article_attachments/4930026332311)

A edição destes arquivos, pode ser realizada através de qualquer editor de textos.

O arquivo **"config.properties"**, contém as configurações gerais da aplicação. Ele possui as seguintes especificações:

- **crypto.hmac.salt:** Salt é utilizado na autenticação dos clientes do SPS. Se um novo valor for definido para essa configuração, o mesmo valor deve ser inserido na configuração equivalente no Sankhya-Om. Por exemplo: crypto.hmac.salt=MzM2Yzg5YWYtZDAyYS00ODEwLWFjMzAtZWE3M2M2ZjA0MTU4
- **crypto.hmac.secretkey:** Secret Key é utilizada na autenticação dos clientes do SPS. Se um novo valor for definido para essa configuração, o mesmo valor deve ser inserido na configuração equivalente no Sankhya-Om. Exemplo: crypto.hmac.secretkey=ZmMyZWFjOTMtN2I3Ny00N2VmLWFkNGUtMmU4ZmRmYzJkYTIy

**Importante:** você não deve alterar nenhuma dessas configurações, a não ser que isso seja especificamente definido pela Sankhya. A versão atual não permite a alteração dessa configuração no componente SPS, portanto, não altere. Futuramente, o componente SPS permitirá a modificação dessa configuração.

- **server.http.port:** Porta do servidor do Sankhya Print Service. A aplicação de administração também é acessada nessa porta. Se alterado, o valor do parâmetro **"Porta do servidor de impressão - SPSSERVERPORT"** deve ser ajustado no Sankhya-W. Exemplo: server.http.port=9091
- **system.shutdown.time:** Tempo em segundos, que cada componente do SPS deve levar para terminar seu trabalho, em caso de desligamento. Se o componente não encerrar seu trabalho nesse tempo, o sistema forçará o desligamento imediato do componente. Exemplo: system.shutdown.time=60
- **job.timeout:** Tempo máximo em segundos, que cada Job tem para continuar voltando à fila, em caso de erro. Esse tempo começa a ser contado a partir do momento em que o job for enviado. Cada vez que um erro ocorrer, esse tempo é verificado. Se o tempo desde a criação do job for menor que este intervalo, o job é enviado para a fila imediatamente. Após esse tempo, se o job não processar corretamente, será sinalizado com um erro e retirado da fila de impressão. Seu status poderá ser consultado na página de administração.Exemplo: job.timeout=3600
- **dir.uploaded:** Diz respeito a pasta de arquivos enviados para impressão. Toda vez que um documento é impresso, seu conteúdo é enviado a esta pasta. A configuração padrão é **"./sps-print-files"** e indica que a pasta **"sps-print-files"** é criada dentro da pasta de instalação do SPS. Considere os exemplos: dir.uploaded=./sps-print-files e dir.uploaded=c:\upload.
- **log4j.conf:** Este arquivo configura as preferências de log da aplicação. Sempre que possível, deve ser manipulado por pessoal especializado, que poderá configurá-lo de forma a permitir a identificação e resolução de problemas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#top)

---

## Utilizando o Console do Servidor SPS

Acesse os links abaixo para saber mais sobre o Console do Servidor SPS:

| [Acessando o Console de Administração](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#acessandooconsoledeadministrao) |
| --- |
| [Tela de Login](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#teladelogin) |
| [Tela Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#telaprincipal) |
| [Lista de Jobs (Trabalhos de Impressão)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#listadejobstrabalhosdeimpresso) |
| [Configuração de Impressora](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#configuraodeimpressora) |
| [Alterar Senha](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#alterarsenha) |

 Acessando o Console de Administração

O console de administração do servidor SPS pode ser acessado através da url: <http://SPSSERVERURL:SPSPRINTSERVERPORT/index.html>

A URL, com os valores padrão da instalação, é: <http://localhost:9091/index.html> ou <http://ip_do_servidor:9091/index.html>

Se o SPS estiver ativo, a tela de login será exibida. Verificar parâmetros **"URL do servidor de impressão - SPSSERVERURL"** e **"Porta do servidor de impressão - SPSSERVERPORT"**.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#utilizandooconsoledoservidorsps) 

## Tela de Login

A tela de login permite acesso ao console de administração do servidor SPS. O login da aplicação de administração é **"admin"** e a senha padrão é **"tecsis"**.

![Imagem 14: A tela de login permite acesso ao console de administração do servidor SPS. O login da aplicação de administração é…](https://ajuda.sankhya.com.br/hc/article_attachments/4905471609623)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#utilizandooconsoledoservidorsps) 

## Tela Principal

![Imagem 15: Tela Principal](https://ajuda.sankhya.com.br/hc/article_attachments/4906050697239)

A tela principal do console do Servidor SPS é composta inicialmente pelos seguintes elementos:

**Botão Sair:** O botão  quando acionado, executará o encerramento da sessão retornando para tela de login.

**Aba Lista de Impressoras:** Esta aba contém a lista de impressoras cadastradas no Sankhya Print Service e os dados relativos a cada uma delas.

**Aba Alterar Senha:** Nesta aba, temos o formulário de alterações de senhas.

**Recarregar Lista de Impressoras:** Ao clicar no botão , a lista de impressoras é atualizada.

**Lista de Impressoras:** Essa lista contém todas as impressoras cadastradas no Sankhya Print Service. Cada item dessa lista mostra o ícone de status da impressora, o nome da impressora e um botão de configuração. A lista de impressoras pode ser recarregada ao clicar no botão Recarregar Lista de Impressoras.

**Status da Impressora:** Cada item da lista de impressoras, apresenta um ícone que indica o seu status atual, se disponível, processando, parada ou desconhecido. Esse status não é atualizado automaticamente. Para isso, deve-se recarregar a lista de impressoras no botão Recarregar lista de impressoras. A impressora pode apresentar os seguintes status:

![Imagem 16: Status da Impressora: Cada item da lista de impressoras, apresenta um ícone que indica o seu status atual, se…](https://ajuda.sankhya.com.br/hc/article_attachments/4930678665367)

**Botão Configurar Impressora:** O botão  permite que cada impressora seja configurada individualmente.

**Botão Apagar:** Após realizar a remoção de uma impressora do sistema operacional, a mesma apresentará o seu status como **"Desconhecido"** no Sankhya Print Service. Deste modo, é necessário acionar o botão ![Imagem 17: Botão Apagar: Após realizar a remoção de uma impressora do sistema operacional, a mesma apresentará o seu status como "…](https://ajuda.sankhya.com.br/hc/article_attachments/4930099203607) para que a mesma seja eliminada da Lista de Impressoras.

**Nota:** somente quando a impressora for removida do sistema operacional que o referido botão efetuará a exclusão de impressoras.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#utilizandooconsoledoservidorsps) 

## Lista de Jobs (Trabalhos de Impressão)

![Imagem 18: Lista de Jobs (Trabalhos de Impressão)](https://ajuda.sankhya.com.br/hc/article_attachments/9527457310231)

Um job é um trabalho de impressão, enviado pelo sistema Sankhya-Om para o Sankhya Print Service. Ele tem duração máxima de 24 horas e após esse tempo, tanto o registro, como o arquivo com o documento a ser impresso, são removidos do sistema.

Ao clicar em uma impressora, na Lista de Impressoras, o sistema mostra um painel do lado direito, com dois elementos. Esta lista possui os dados de cada job enviado para esta impressora e tem duas finalidades:

1. **Tabela de jobs da impressora:** Permitir a visualização dos dados de cada job enviado para a impressora;
2. **Botão reimprimir jobs:** Permitir a reimpressão de um conjunto de jobs.

#### Tabela de Jobs

A Tabela de Jobs possui as seguintes colunas:

**ID:** Identificador numérico do job;

**Descrição:** Descrição do job, normalmente contendo o tipo de documento que está sendo impresso;

**Cópias**: Número de cópias a serem impressas;

**ID do usuário** : Identificador do usuário que enviou a impressão;

**Usuário:** Nome do usuário que enviou a impressão;

**MimeType:** Tipo de dados do documento enviado para impressão. Por enquanto, podem ser:

- PDF: Qualquer documento PDF;
- TEXT : Qualquer documento do tipo texto puro;
- JASPER: Um documento gerado através de um relatório Jasper Reports;
- FILE: O conteúdo do documento enviado será salvo em uma pasta do disco. Um documento do tipo file, não é deletado quando o job expira e é apagado da lista de jobs.

**Tipo de documentos:** Natureza do documento a ser impresso. Podem ser:

- Nota;
- Pedido;
- Boleto;
- Cheque;
- Relatório;
- Outro.

**Status:** Se refere ao status do job. Este pode ser:

- Pronto para impressão;
- Enviando para a impressora;
- Imprimindo;
- Aguardando impressora;
- Requisitando atenção;
- Impressão terminada;
- Erro na impressão;
- Impressão cancelada;
- Status desconhecido.

**Mensagem de status :** Mensagem exibida de acordo com o status da impressão. Útil para identificar causas de problemas com o job;

**Criação:** Data e hora de envio do job;

**Atualização:** Data e hora de atualização do job (sempre que o status do job é alterado, por exemplo).

#### Reimpressão de Jobs

A Tabela de jobs, permite que um ou mais jobs sejam selecionados para a reimpressão. Para isso, basta selecionar os jobs e clicar no botão de **"Reimpressão**".

O job deve estar em um dos seguintes estados, para ser reimpresso:

- Aguardando impressora;
- Impressão terminada;
- Erro na impressão;
- Impressão cancelada.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#utilizandooconsoledoservidorsps) 

## Configuração de Impressora

**Importante:** essa sessão é destinada a operadores avançados do Sankhya Print Service. Não altere as configurações de impressora, sem conhecer exatamente o que ocorre no Sankhya-Om. A manipulação incorreta dessas configurações pode acarretar em diversos problemas na impressão.

#### O DocFlavor

Um documento pode assumir diversas formas diferentes, incluindo, um arquivo PDF, uma imagem de uma câmera digital, um e-mail, um documento de processador de texto ou uma página web. Antes de imprimir um documento de um formato específico, é necessário garantir que a impressora consiga entender este formato.

Às vezes, uma impressora pode imprimir diretamente os documentos de um determinado formato, impressoras fotográficas podem imprimir diretamente imagens de vários formatos e impressoras **"PostScript"** podem imprimir diretamente documentos **"PostScript"**. No entanto, apesar de existirem algumas impressoras que podem imprimir diretamente uma ampla variedade de formatos, a maioria das impressoras requer algum suporte de software de alto nível para traduzir o documento de origem em um formato que se pode imprimir.

O Sankhya Print Service utiliza a **"Java Print Service API"**. Essa API fornece uma maneira de descrever os tipos de documentos de forma que:

- A impressora pode informar quais formatos ela é capaz de imprimir;
- Pode informar o formato dos dados que se deseja imprimir;
- Pode descrever a codificação de dados de texto.

A Java Print Service API descreve os tipos de documentos utilizando a classe DocFlavor, sendo este composto por: 

- Um tipo de MIME, que informa à impressora como interpretar os dados;
- Um nome de classe de representação, que indica a classe Java que descreve como os dados são enviados para a impressora.

#### O DocFlavor no Sankhya Print Service

Quando se envia um documento para o SPS, o tipo de dado enviado deve ser informado utilizando o parâmetro MymeType.

O Sankhya-Om por exemplo, envia o valor JASPER quando o modelo da nota é um relatório jasper reports ou TEXT quando o modelo é texto. Utilizando este parâmetro, o SPS pode determinar qual o tipo de DocFlavor deve ser usado para imprimir o documento. Algumas impressoras podem aceitar tipos diferentes de DocFlavor e portanto, é necessário que exista um mapeamento entre o DocFlavor e o Mimetype. Esse mapeamento é feito na tela de configuração de impressora.

Ao clicar no botão **"Configurar Impressora"** de uma impressora, será aberto uma tela na qual, temos uma lista dos tipos de dados suportados pela impressora e os DocFlavor's utilizados para cada tipo de dado.

![Imagem 19: Ao clicar no botão "Configurar Impressora" de uma impressora, será aberto uma tela na qual, temos uma lista dos tipos…](https://ajuda.sankhya.com.br/hc/article_attachments/4931758069783)

Para cada tipo de dado (coluna **"Tipo de Documento"**), você escolherá um DocFlavor (coluna localizada à direita). Após todos os pares estarem configurados, você pode salvar as configurações.

![Imagem 20: Para cada tipo de dado (coluna "Tipo de Documento" ), você escolherá um DocFlavor (coluna localizada à direita). Após…](https://ajuda.sankhya.com.br/hc/article_attachments/4931817675415)

A coluna DocFlavor permite a seleção através de um combobox, conforme apresentado na imagem acima.

![Imagem 21: A coluna DocFlavor permite a seleção através de um combobox, conforme apresentado na imagem acima.](https://ajuda.sankhya.com.br/hc/article_attachments/4931874105367)

Se o combobox for acionado e nenhum valor for escolhido, o campo exibe o valor **"null"**. 

Assim, se as configurações forem salvas com valores **"null"**, uma mensagem de erro é exibida, indicando que um DocFlavor deve ser selecionado para cada tipo de documento citado na mensagem.

**Mensagem: Erro de validação. O valor da configuração PDF é inválido. O valor da configuração TEXT é inválido.**

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#utilizandooconsoledoservidorsps) 

## Alterar Senha

Na aba Alterar Senha, você pode alterar a senha do usuário admin. Este é o único usuário do SPS.

![Imagem 22: Na aba Alterar Senha , você pode alterar a senha do usuário admin. Este é o único usuário do SPS .](https://ajuda.sankhya.com.br/hc/article_attachments/4913112541591)

Depois de informadas a **"Senha atual"**, e a **"Nova senha"** e confirmá-la, clique em **"Salvar"**. No próximo login, a senha será exigida.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#utilizandooconsoledoservidorsps) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#top) 

## Utilizando o SPS no Sankhya-Om

Saiba como utilizar o SPS no Sankhya-Om, acesse os links abaixo para facilitar sua navegação:

| [Como funciona o SPS?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#comofuncionaosps) |
| --- |
| [Como o SPS localiza uma Impressora?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#comoospslocalizaumaimpressora) |
| [Localização de uma Impressora no SPS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#localizaodeumaimpressoranosps) |
| [Impressora Substituta](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#impressorasubstituta) |

## Como Funciona o SPS?

O Componente SPS é responsável por controlar todos os processos ligados à impressão. Ele mantém o cadastro dos Servidores SPS (um servidor Sankhya-Om pode se comunicar com vários servidores SPS), envia impressões para os servidores, controla o acesso às impressoras cadastradas, faz o roteamento de impressoras e permite o controle dos trabalhos de impressão.

De todos esses processos, o mais importante é o processo de impressão.

#### Execução da Impressão

O processo de impressão é iniciado quando você solicita uma impressão. O sistema então gera um imprimível (atualmente, nota ou boleto) e decide qual o nome da impressora a ser utilizada. Essa solicitação é passada ao Componente SPS, que procede com a impressão.

A geração do imprimível e resolução do nome da impressora são particulares a cada processo e suas respectivas documentações devem ser consultadas.

Quando a solicitação de impressão é recebida pelo Componente SPS, a primeira coisa a ser verificada é se o Sankhya-Om irá utilizar a impressão tradicional (com o applet) ou a impressão com o SPS.

Se o parâmetro **"Usar o PrintService para impressão? - USASERVIMP"** estiver ativado, então será utilizada a impressão com o SPS. Neste caso, o sistema pesquisa por uma localização de impressora. Se uma impressora não for localizada, o job é registrado sem impressora.

No caso de uma localização ser encontrada, o sistema verifica se você tem acesso a essa impressora. Se o você não possuir acesso, o job é registrado sem impressora. Se possuir acesso, o job é registrado em uma fila de jobs.

Futuramente, o sistema irá oferecer a configuração de uma nova impressora para jobs sem uma impressora.

Uma vez que o job é colocado na fila, ele fica aguardando até ser retirado dessa fila e ser enviado para o servidor SPS da impressora escolhida. Dessa forma, o sistema não fica travado aguardando a impressão, permitindo que você possa continuar suas tarefas.

Você pode acompanhar o andamento de suas impressões na tela **"Trabalhos de Impressão".**

Futuramente, o sistema irá oferecer impressão local (na máquina do usuário) como parte do SPS (jobs locais serão registrados na tabela de jobs).

O processo de impressão pode ser visto no fluxograma representado na imagem abaixo:

![Imagem 23: O processo de impressão pode ser visto no fluxograma representado na imagem abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/4912716996759)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#utilizandoospsnosankhya-om)

## Como o SPS localiza uma impressora?

Um passo importante da impressão, é a localização da impressora a ser utilizada. A determinação dessa localização permite uma grande flexibilidade de configurações, de forma a atender as mais diversas necessidades. Para descobrir qual impressora deve ser utilizada, o Componente SPS se baseia em três conceitos:

- [Nome da Impressora](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#nomedaimpressora)
- [Localização de Impressora](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#localizaodeimpressora)
- [Mapeamento de Impressora](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#mapeamentodeimpressora)

#### Nome da Impressora

Quando o Componente SPS recebe uma solicitação de impressão, essa solicitação traz consigo o nome da impressora a ser utilizada. Esse nome é decidido em cada processo solicitante. Por exemplo, na impressão de boletos, o nome da impressora pode ser configurado na tela [Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113), aba [Boleto(s)/Duplicatas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas#ababoletosduplicatas), campo **"Impressora"**.

Esse nome não representa uma impressora física, mas sim um nome lógico que pode ser mapeado para uma impressora ou outra, levando em consideração:

- Configurações de Localização de Impressora encontradas no SPS;
- Roteamento de impressoras;
- Controle de acessos;
- Impressoras substitutas.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#comoospslocalizaumaimpressora)

#### Localização de Impressora

Em algumas telas do SPS, é possível visualizar o caminho de uma impressora. Geralmente ele aparece na forma, servidor:porta/impressora. Por exemplo: 127.0.0.1:9091/CutePDF Writer.

Esse caminho indica qual o IP ou nome do servidor SPS, a porta desse servidor e o nome da impressora. É através deste caminho que o Componente SPS pode enviar uma requisição de impressão para essa impressora.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#comoospslocalizaumaimpressora)

#### Mapeamento de Impressora

O Mapeamento de Impressora é a configuração que associa um Nome de impressora a uma Localização de impressora, de forma que o sistema possa, através do nome de impressora, encontrar a localização de impressora. O componente SPS utiliza de quatro formas de mapear as impressoras. São elas:

- Mapeamento por parâmetro;
- Mapeamento por nomes de impressoras;
- Mapeamento por impressoras e servidores de impressão;
- Mapeamento de impressoras substituídas.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#utilizandoospsnosankhya-om)

## Localização de uma impressora no SPS

Uma vez que o componente SPS é solicitado, ele recebe o nome da impressora e busca em seus mapeamentos, por uma localização de impressora equivalente a este nome. Quando uma localização é encontrada, o sistema para a busca e usa essa localização no restante do processo.

O primeiro passo da pesquisa por uma localização de impressora, é a verificação se existe no sistema alguma localização da mesma. Não existindo nenhuma, o sistema considera que o job não possui impressora, ainda que a solicitação de impressão contenha um nome de impressora.

Se existir ao menos uma localização no sistema, o próximo passo é o roteamento de usuários. Feito isso, o nome de roteamento é utilizado para buscar uma localização de impressora na tabela Impressoras (TSIPRN). Essa busca usa o campo **"Nome Local"** (ALIASLOCAL) para encontrar a impressora.

Se não for encontrada uma localização compatível, a busca passa a verificar a tabela **"Nomes de Impressoras"** (TSIPRP). Essa busca utiliza o campo **"Nome local da impressora"** (NOMEIMPLOCAL).

Se não for encontrada uma localização, a busca usa os mapeamentos existentes no parâmetro **"Mapeamento de impressoras locais e remotas SPSPRINTMAP"**.

O processo pode ser visualizado no fluxograma representado na imagem abaixo:

![Imagem 24: O processo pode ser visualizado no fluxograma representado na imagem abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/4912659481495)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#utilizandoospsnosankhya-om)

## Impressora Substituta

Uma Impressora Substituta é aquela que é marcada como disponível para ser utilizada por um grupo de impressão (jobs que possuem os mesmos nomes de impressora e tipos de documento).

Sempre que o sistema procura por uma impressora para um documento, ele utiliza um nome de impressora. Se uma impressora não for encontrada, o Componente SPS tenta localizar uma impressora substituta. Se uma substituta não for encontrada, o sistema exibe a tela de seleção de impressora substituta.

![Imagem 25: Sempre que o sistema procura por uma impressora para um documento, ele utiliza um nome de impressora. Se uma impressora…](https://ajuda.sankhya.com.br/hc/article_attachments/4913057123991)

As Impressoras PDFs só podem ser utilizadas como impressoras locais, se o sistema estiver configurado para utilizar o SPS e possuir um servidor cadastrado na tela [Servidores de impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600774), ao efetuar uma impressão o sistema poderá apresentar o pop-up **"Impressora Substituta"**. No referido pou-up, você pode efetuar as seguintes seleções:

- Ao selecionar na aba Impressoras locais a impressora PDFCreator, será a impressora na máquina que está efetuando a impressão e nela será apresentada a caixa de diálogo do windows para salvar o PDF.
- Caso selecione uma impressora na aba Impressoras remotas a impressão não é feita localmente, sendo assim, ao selecionar a impressora PDFCreator e imprimir, a caixa de diálogo do windows será apresentada na máquina remota que está rodando o SPS, onde, de fato será executada a impressão.

Para impressão remota não se pode utilizar PDFCreator ou qualquer outro tipo de geração de documentos em uma impressora que tenha interação com o usuário, pois, essa interação será feita no servidor e não na máquina local.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#utilizandoospsnosankhya-om) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#top)

## Roteamento

Trataremos nos tópicos a seguir do Roteamento de impressora:

| [O que é Roteamento de Impressora? Qual a sua finalidade?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#oqueroteamentodeimpressoraqualasuafinalidade) |
| --- |
| [Localização de Roteamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#localizaoderoteamento) |
| [Localização de Configuração de Impressora](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#localizaodeconfiguraodeimpressora) |
| [Comportamento do Sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#comportamentodosistema) |
| [Como é feito o Controle de Acessos?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#comofeitoocontroledeacessos) |

## O que é Roteamento de Impressora? Qual a sua finalidade?

O nome de uma impressora definido em um processo, é utilizado para todos os usuários. Por exemplo, na impressão de um boleto, é sempre o nome cadastrado na conta vinculada ao boleto. Em alguns casos, isso pode não ser desejável. Pode-se ter por exemplo, todas as filiais de uma empresa imprimindo seus boletos em uma conta apenas. Dessa forma, sem o processo de roteamento, todos os boletos seriam impressos na mesma impressora, o que poderia gerar situações em que uma empresa no Rio de Janeiro, pode enviar uma impressão para uma empresa em Manaus.

Em outros casos, deseja-se que nesse mesmo processo, um determinado usuário ou grupo possa realizar a impressão em outra impressora. Para resolver este tipo de situação, foi criado o **"Roteamento de Impressora"**.

O roteamento consiste em desviar o usuário, grupo ou empresa para uma outra impressora. O componente SPS recebe como nome de entrada o nome da impressora, e verifica se para aquele usuário, grupo ou empresa, existe um roteamento. Se um roteamento for encontrado, o nome de roteamento (campo **"Nome de saída"**), é utilizado como nome de impressora. Caso contrário, o próprio nome da impressora será usado como identificador.

O resultado desse processo, é utilizado na localização de impressora. Dessa forma, pode-se ter toda uma empresa utilizando a impressora **"PDFCreator"** para impressão de boletos, e o usuário "João Teixeira", por exemplo, utilizando a impressora **"PDF995"**.

![Imagem 26: O resultado desse processo, é utilizado na localização de impressora. Dessa forma, pode-se ter toda uma empresa…](https://ajuda.sankhya.com.br/hc/article_attachments/4912596236695)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#roteamento)

## Localização de Roteamento

O roteamento pode ocorrer em 3 (três) níveis, do mais específico para o mais geral:

1. Roteamento por usuário (Tela - Usuários)
2. Roteamento por grupo de usuário (Tela – Grupo de Usuários)
3. Roteamento por empresa (Tela - Empresa)

Ou seja, o sistema pesquisa primeiro nos roteamentos do usuário que solicitou a impressão. Se não encontrar nenhum, pesquisa nos roteamentos do grupo do usuário. Caso também não encontre nenhum, busca nos roteamentos da empresa do documento que está sendo impresso.

Cada nível de roteamento é definido uma tela diferente. Caso o sistema não encontre nenhum roteamento, será pego o nome de entrada, e verificado se há alguma configuração para esta impressora, e caso tenha, o sistema realiza a impressão por esta impressora.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#roteamento)

## Localização de Configuração de Impressora

Quando o sistema encontra um roteamento em um dos níveis, é pego o nome de saída e verificado se existe configuração pra essa impressora em 3 (três) locais seguindo a ordem:

1. Tela - **"Servidor de Impressão"**;
2. Tela - **"Nome de Impressoras"**;
3. Parâmetro **"Mapeamento de impressoras locais e remotas - SPSPRINTMAP"**.

Quando o sistema encontra configuração em um dos níveis, realiza a impressão utilizando a configuração encontrada.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#roteamento)

## Comportamento do Sistema

O sistema pega o nome de entrada, e verifica se há algum roteamento cadastrado para o  mesmo, seguindo a ordem de verificação conforme descrita no item Localização de Roteamento.

Ao encontrar um roteamento cadastrado, o sistema pega o nome de saída e verifica se existe configuração para o mesmo, conforme o item Localização de Configuração de Impressora.

Caso o sistema não encontre um roteamento, será pego o nome de entrada e verificado se há configuração para o mesmo; caso tenha, será realizada a impressão conforme a configuração; caso não tenha, o sistema tenta imprimir pela impressora de entrada, e caso essa impressora não seja uma impressora válida, a impressão e enviada para o Applet.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#roteamento)

## Como é feito o Controle de Acessos?

Se o sistema encontrar uma localização de impressora, o sistema verifica se o usuário possui acesso a essa impressora. A configuração desses acessos é descrita no item [Controle de Acesso](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#controledeacessos), mais adiante nesta documentação.

Para que o usuário tenha acesso à impressora, uma das seguintes condições deve ser satisfeita:

- A localização da impressora foi definida na tela Servidores de impressão e o usuário possui acesso ao servidor de impressão;
- A localização da impressora foi definida na tela Servidores de impressão e o grupo do usuário possui acesso ao servidor de impressão;
- A localização da impressora foi definida na tela Servidores de impressão e o usuário dispõe acesso a impressora;
- A localização da impressora foi definida na tela Servidores de impressão e o grupo do usuário possui acesso a impressora;
- A localização da impressora foi definida na tela Nomes de impressora;
- A localização da impressora foi definida no parâmetro Mapeamento de impressoras locais e remotas - SPSPRINTMAP.

Se nenhuma dessas condições for satisfeita, o usuário não tem acesso a impressora, e o job é cadastrado sem impressora.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#roteamento) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#top)

## Cadastros e Configurações

Trataremos a seguir dos cadastros e das configurações do SPS:

| [Ativando a impressão pelo SPS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#ativandoaimpressopelosps) |
| --- |
| [Método de Config. de Impressoras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#escolhendoummtododeconfiguraodeimpressoras) |
| [Remoção de Impressoras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#remoodeimpressoras) |
| [Remoção de Servidor de Impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#remoodeservidordeimpresso) |

## Ativando a impressão pelo SPS

Para ativar a impressão pelo SPS, é necessário ativar o parâmetro **"Usar o PrintService para impressão? - USASERVIMP"**. Sem este parâmetro, o Sankhya-Om utilizará a impressão tradicional, via applet.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#cadastroseconfigura%C3%A7%C3%B5es)

## Escolhendo um método de Configuração de Impressoras

Atualmente, no componente SPS, existem 3 (três) métodos para configurar impressoras. Esses métodos **não podem ser utilizados ao mesmo tempo** e devem ser aplicados de forma individual, ou seja, apenas um deles deve ser escolhido por vez:

1. [Configurando por Parâmetros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#configurandoporparmetros)
2. [Configurando por Nome de Impressora](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#configurandopornomedeimpressora)
3. [Configurando por Impressoras e Servidor de impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#configurandoporimpressoraseservidordeimpresso)

Como visto anteriormente, existe uma ordem de pesquisa por um nome de impressora. Se a mesma impressora for configurada utilizando os 3 (três) métodos, a impressora que estiver usando o método 3 (três) será utilizada.

Se ela não for encontrada no método 3 (três), a do método 2 (dois) será utilizada. Somente se nenhuma impressora for encontrada nos métodos anteriores, o sistema irá utilizar a impressora cadastrada no método 1 (um).

A configuração por parâmetros deve ser utilizada, apenas se for bem compreendida a utilização do mapeamento padrão e o mapeamento completo. Ela é flexível, pois permite dar vários nomes a uma mesma impressora e utilizar a sintaxe padrão, que é uma versão resumida da sintaxe de mapeamento. Contudo, é complexa de administrar e não possui controle de acessos. Essa foi a primeira forma de configurar o componente SPS, e é mantida devido à retrocompatibilidade.

A configuração por nomes de impressoras mapeia um nome de impressora diretamente para uma localização de impressora. Ela é um meio termo entre a configuração por parâmetros e a configuração por impressoras e servidores de impressão. Também é mantida devido à retrocompatibilidade.

A configuração por impressoras e servidores de impressão é a melhor forma de configurar os servidores SPS. Ela permite que se tenha controle de acessos, e é mais simples de administrar e gerenciar.

Sempre que possível, aconselhamos a utilização da configuração por impressoras e servidores de impressão. Sendo exequível, aconselhamos a migração das configurações antigas para esta forma.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#escolhendoummtododeconfiguraodeimpressoras)

## Configurando por Parâmetros

Para configurar o componente SPS utilizando parâmetros, é necessário alterar 3 (três) parâmetros de sistema:

O parâmetro **"URL do servidor de impressão - SPSSERVERURL",** armazena o nome ou IP do servidor SPS padrão. Ele é utilizado sempre que uma operação exige um servidor SPS, mas não especifica qual servidor. Este endereço deve ser informado pelo nome ou pelo IP, e não deve possuir **"HTTP://"** ou **"HTTPS://"** em seu início.

Exemplos válidos:

- localhost (Servidor local)
- printserver (Nome da máquina onde está instalado o SPS)
- 192.168.0.158 (IP da máquina onde está instalado o SPS)

Exemplos inválidos:

- http://localhost
- http://printserver
- https://192.168.0.158

O parâmetro **"Porta do servidor de impressão - SPSSERVERPORT"** armazena a porta utilizada pelo servidor SPS padrão. O Sankhya-Om usa essa porta para enviar impressões ao servidor SPS. O valor padrão é **"9091"**.

Essa porta só deve ser modificada, se o valor correspondente for modificado no servidor.

Por fim, o parâmetro **"Mapeamento de impressoras locais e remotas - SPSPRINTMAP"** armazena o mapeamento entre nomes de impressoras cadastrados no Sankhya-Om e impressoras do SPS. Este parâmetro obedece a uma sintaxe muito rígida e qualquer erro na interpretação do parâmetro, pode levar ao cancelamento do processo de impressão pelo servidor SPS e uso da impressão tradicional.

Esse parâmetro contém uma sequência de 0 ou mais mapeamentos, onde cada mapeamento é separado do outro por ponto e vírgula (;).Considere o exemplo:

mapeamento1;mapeamento2;mapeamento3;mapeamento4;

O parâmetro também pode ser cadastrado com quebras de linha:

mapeamento1;
mapeamento2;
mapeamento3;
mapeamento4;

Cada mapeamento pode ser definido utilizando uma das duas sintaxes, são elas:

- [Mapeamento Completo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#mapeamentocompleto);
- [Mapeamento Padrão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#mapeamentopadr%C3%A3o).

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#cadastroseconfigura%C3%A7%C3%B5es)

#### Mapeamento Completo

O Mapeamento completo é a forma plena de definir um mapeamento por parâmetro. Ele tem o seguinte formato:

nomeDeImpressora#servidor:porta/nomeDeImpressoraRemota

ou como podemos notar:

nomeDeImpressora#localizaçãoDeImpressora

Onde:

- **nomeDeImpressora:** Nome da impressora local, como definido na seção Nome de impressora;
- **localizaçãoDeImpressora:** Localização da impressora, como definida na seção Localização de impressora.

Note que o símbolo # (cerquilha), é o responsável pela separação do nome de impressora do restante do mapeamento.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#configurandoporparmetros)

#### Mapeamento Padrão

O mapeamento padrão é uma forma resumida de descrever um mapeamento, permitindo que um nome de impressora seja mapeado para uma localização de impressora do servidor SPS padrão. O servidor SPS padrão, é aquele que definido nos parâmetros SPSSERVERURL e SPSSERVERPORT mencionados logo acima.

Como o servidor já está definido, é necessário apenas informar o nome local e o nome da impressora no servidor SPS. O mapeamento padrão tem o seguinte formato:

nomeDeImpressora@impressoraRemota;

Onde:

- **nomeDeImpressora:** Nome da impressora local, como definido na seção Nome de impressora.
- **impressoraRemota:** É o nome de uma impressora cadastrada no SPS padrão. Não é preciso informar o nome ou IP do servidor SPS, nem a porta.

Note que o símbolo @ (arroba), é o responsável pela separação do nome de impressora e o resto do mapeamento.

O componente SPS transforma internamente, o mapeamento padrão em um mapeamento completo, utilizando os parâmetros SPSSERVERURL e SPSSERVERPORT mencionados acima, para completar o mapeamento. Dessa forma:

nomeDeImpressora@impressoraRemota;

se transforma em:

nomeDeImpressora@SPSSERVERURL:SPSSERVERPORT/impressoraRemota;

Você deve atentar para os seguintes nomes especiais de impressoras locais:

- Padrão;
- Outras;
- ?;
- Sem impressora.

Por exemplo:

- PADRAO@PDFCreator;
- OUTRA@CutePDF Writer;
- ?@Canon iR1020/1024/1025 UFRII LT ADM;
- SEM IMPRESSORA@Canon iR1020/1024/1025 UFRII LT ADM;
- PDFCreator@PDFCreator;
- CutePDF Writer@Canon iR1020/1024/1025 UFRII LT ADM;
- Canon iR1020/1024/1025 UFRII LT ADM@Canon iR1020/1024/1025 UFRII LT ADM

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#escolhendoummtododeconfiguraodeimpressoras)

## Configurando por Nome de Impressora

Para configurar o componente SPS, utilizando nomes de impressoras, utilize a tela [Nomes de Impressoras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598834).

![Imagem 27: Para configurar o componente SPS, utilizando nomes de impressoras, utilize a tela Nomes de Impressoras .](https://ajuda.sankhya.com.br/hc/article_attachments/4932002420119)

Nessa tela, temos os seguintes campos:

- **Nome local de impressora:** Este campo recebe um Nome de Impressora, conforme definido na seção Nome de impressora.
- **Caminho da impressora no servidor de impressão:** Campo que recebe uma localização de impressora, conforme definido na seção Localização de impressora.

No modo grade, você pode visualizar os mapeamentos de impressora já cadastrados.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#escolhendoummtododeconfiguraodeimpressoras)

## Configurando por Impressoras e Servidor de Impressão

Para configurar o componente SPS utilizando a tela de servidores de impressão, utilize a tela [Servidores de Impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600774).

![Imagem 28: Para configurar o componente SPS utilizando a tela de servidores de impressão, utilize a tela Servidores de Impressão .](https://ajuda.sankhya.com.br/hc/article_attachments/4932055524375)

Nesta tela são realizados os cadastros de servidores de impressão de suas impressões. Caso já tenha sido realizado algum registro, ao abrir a tela, será visualizada a lista de servidores já cadastrados no sistema.

Ao ser acionado o sinal de **(+)** para inclusão de um novo servidor, será aberta o pop-up **"Cadastrando um servidor de impressão"**.

![Imagem 29: Ao ser acionado o sinal de ( +) para inclusão de um novo servidor, será aberta o pop-up "Cadastrando um servidor de…](https://ajuda.sankhya.com.br/hc/article_attachments/4932094770967)

No primeiro passo do assistente, informe a **"URL"** e a **"Porta do Servidor"** de impressão. O preenchimento do campo **"Descrição"** é opcional. O botão **"Próximo"** será habilitado, após os campos obrigatórios estarem devidamente preenchidos.

Preenchidos os dados e clicando em **"Próximo"**, será solicitada ao servidor informado, a sua lista de impressoras.

![Imagem 30: Preenchidos os dados e clicando em "Próximo" , será solicitada ao servidor informado, a sua lista de impressoras.](https://ajuda.sankhya.com.br/hc/article_attachments/4932199622167)

Caso algum problema ocorra durante a busca de informações, a tela irá retornar ao primeiro passo, e a mensagem de erro será exibida.

Se o servidor informado for encontrado e a lista for retornada com sucesso, esta será exibida no seguinte passo, na tela de escolha de impressoras. Feita a escolha, o servidor de impressão e as impressoras escolhidas são salvos.

Feita a seleção de algumas impressoras, o botão **"Concluir"** é habilitado, ao acioná-lo o procedimento de cadastro é finalizado.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#cadastroseconfigura%C3%A7%C3%B5es)

## Remoção de Impressoras

Quando é solicitada a remoção de uma impressora, o componente SPS deve verificar se essa impressora possui algum job na tabela de trabalhos de impressão. Se houver algum job, essa remoção não será autorizada.

Para verificar se existe algum job para a impressora, basta acessar a tela [Trabalhos de Impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600374) e filtrar pelo campo **"Endereço da impressora"**. Esse campo contém o endereço completo da impressora, que são, o servidor, a porta do serviço de impressão e o nome da impressora.

![Imagem 31: Para verificar se existe algum job para a impressora, basta acessar a tela Trabalhos de Impressão e filtrar pelo campo…](https://ajuda.sankhya.com.br/hc/article_attachments/4932373840279)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#cadastroseconfigura%C3%A7%C3%B5es)

## Remoção de Servidor de Impressão

Quando é solicitada a remoção de um servidor de impressão, o componente SPS verifica se alguma das impressoras desse servidor possui algum job na tabela de trabalhos de impressão. Se houver algum job, essa remoção não é autorizada.

Para verificar se existe algum job para este servidor, basta acessar na tela Trabalhos de Impressão e filtrar pelo campo **"Endereço do servidor de impressão"**. Esse campo contém o endereço completo do servidor, ou seja, o servidor e a porta do serviço de impressão.

![Imagem 32: Para verificar se existe algum job para este servidor, basta acessar na tela Trabalhos de Impressão e filtrar pelo…](https://ajuda.sankhya.com.br/hc/article_attachments/4932316547607)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#cadastroseconfigura%C3%A7%C3%B5es) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#top)

## Tipos de Roteamento

Trataremos aqui, sobre os tipos de Roteamento, sendo eles:

| [Roteamento por Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#roteamentoporusurios) |
| --- |
| [Roteamento por Grupo de Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#roteamentoporgrupodeusurios) |
| [Roteamento por Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#roteamentoporempresa) |

  Roteamento por Usuários

Esse roteamento é configurado na tela [Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874), aba [Roteamento de impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abaroteamentodeimpresso). Esse é o roteamento de maior precedência, ou seja, que antecede aos demais tipos.

![Imagem 33: Esse roteamento é configurado na tela Usuários , aba Roteamento de impressão . Esse é o roteamento de maior…](https://ajuda.sankhya.com.br/hc/article_attachments/4932437545495)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#tiposderoteamento) 

## Roteamento por Grupo de Usuários

Esse roteamento é configurado na tela [Grupo de Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596134), aba **"Roteamento de impressão"**. Este roteamento é utilizado se um roteamento de usuários não for encontrado para o usuário que solicitou a impressão.

![Imagem 34: Esse roteamento é configurado na tela Grupo de Usuários , aba "Roteamento de impressão" . Este roteamento é utilizado…](https://ajuda.sankhya.com.br/hc/article_attachments/4932591926423)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#tiposderoteamento) 

## Roteamento por Empresa

Esse roteamento é definido na tela [Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893), aba [Roteamento de impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaroteamentodeimpresso). Ele só é utilizado se não for localizado nenhum roteamento por usuário e nenhum roteamento por grupo de usuários.

![Imagem 35: Esse roteamento é definido na tela Empresa , aba Roteamento de impressão . Ele só é utilizado se não for localizado…](https://ajuda.sankhya.com.br/hc/article_attachments/4932725654807)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#tiposderoteamento) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#top)

## Controle de Acessos

Nesta seção, trataremos dos seguintes tópicos:

| [Servidores de Impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#servidoresdeimpresso) |
| --- |
| [Acesso a Impressora](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#acessoaimpressora) |
| [Verificando o Status da Impressora](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#verificandoostatusdaimpressora) |

 Servidores de Impressão

O acesso ao servidor de impressão pode ser definido na tela [Servidores de Impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600774). Esta tela quando alternada para o modo formulário, irá exibir a aba [Controle de acesso](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600774-Servidores-de-Impress%C3%A3o#abacontroledeacesso).

![Imagem 36: O acesso ao servidor de impressão pode ser definido na tela Servidores de Impressão . Esta tela quando alternada para o…](https://ajuda.sankhya.com.br/hc/article_attachments/4932756683799)

Nessa aba, você pode configurar o acesso de um grupo de usuários, ou de um usuário, ao servidor de impressão selecionado. Sendo selecionado um grupo, qualquer usuário daquele grupo poderá imprimir em qualquer impressora do servidor. Sendo selecionado um usuário, este usuário poderá imprimir em qualquer impressora deste servidor.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#controledeacessos)

## Acesso a Impressora

Ainda na tela Servidores de Impressão, para definir o acesso a uma impressora, realiza-se o acesso a aba [Impressoras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600774-Servidores-de-Impress%C3%A3o#abaimpressoras), onde serão exibidas as impressoras disponíveis e indisponíveis em modo grade.

![Imagem 37: Ainda na tela Servidores de Impressão , para definir o acesso a uma impressora, realiza-se o acesso a aba Impressoras ,…](https://ajuda.sankhya.com.br/hc/article_attachments/4933041890711)

Primeiramente, efetue a seleção da respectiva impressora através de um duplo clique, de modo que esta passe a ser apresentada em modo formulário.

Na aba Controle de acesso, realize a configuração do acesso de um grupo ou de um usuário à impressora selecionada. Sendo selecionado um grupo, qualquer usuário daquele grupo poderá imprimir nessa impressora. Se selecionado um usuário, esse usuário poderá imprimir nessa impressora.

![Imagem 38: Na aba Controle de acesso , realize a configuração do acesso de um grupo ou de um usuário à impressora selecionada.…](https://ajuda.sankhya.com.br/hc/article_attachments/4933403636119)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#controledeacessos)

## Verificando o Status da Impressora

Ao cadastrar uma impressora, a localização desta é armazenada no banco de dados do Sankhya-Om. O processo de atualização automática de status, visa manter o status dessa localização de impressora, sincronizado com o status da impressora no servidor SPS apropriado.

Essa atualização ocorre a cada 1 (um) minuto e pode ser visualizada também na tela Servidores de impressão, aba Impressoras, através da coluna "Status". A tela não é atualizada automaticamente. O Sankhya-Om atualiza o status da impressora internamente, e é necessário que o usuário atualize a tela para visualizar o novo status. Para isso, acione o botão **"Atualizar status"**.

![Imagem 39: Essa atualização ocorre a cada 1 (um) minuto e pode ser visualizada também na tela Servidores de impressão , aba…](https://ajuda.sankhya.com.br/hc/article_attachments/4933490553239)

Ao clicar neste botão, o sistema verifica o console do SPS, e identifica o status de cada impressora para realizar sua atualização.

É possível que a impressora se encontre em dois status **"Disponível"** e **"Indisponível"**; quando o sistema não consegue identificar o status da impressora ou esta por algum motivo não aceita a impressão, o equipamento fica com o status Indisponível; se a impressora estiver recebendo impressão, o status da mesma fica como Disponível.

Na tela [Trabalhos de Impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600374), você pode identificar o botão **"Atualizar status"**, na qual o sistema verifica no SPS o status de cada Job (impressão) e realiza a atualização do mesmo na tela.

Uma impressora pode assumir os seguintes estados:

- **Pronta:** Indica que a impressora está pronta para receber novas impressões, sem espera;
- **Processando:** Demonstra que a impressora está processando um documento e que novos trabalhos serão colocados na fila. A atualização para esse estado, depende da notificação pela impressora ao sistema operacional, de seu status e de que esse notifique a JPS. Em muitos casos, uma impressora que está imprimindo um documento pode aparecer como Pronta. Este estado é utilizado para manter a compatibilidade com a JPS.
- **Parada:** Significa que a impressora está parada por algum motivo e uma intervenção direta na mesma é requisitada. A atualização para esse estado, depende da notificação pela impressora ao sistema operacional, de seu status e de que esse notifique a JPS. Em muitos casos, uma impressora que está imprimindo um documento pode aparecer como "Pronta". Este estado é utilizado para manter a compatibilidade com a JPS.
- **Desconhecido:** Indica que o componente SPS não foi capaz de determinar o estado da impressora.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#controledeacessos) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#top)

## Rotinas do Sistema

Nessa seção, trataremos dos seguintes tópicos relacionados as rotinas do sistema:

| [Impressã](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#impressodeboleto)[o](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#impressodeboleto) [de Boleto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#impressodeboleto) |
| --- |
| [Impressão de Cheques](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#impressodecheques) |
| [Impressão de Relatórios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#impressoderelatrios) |
| [Verificando os Trabalhos de Impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#verificandoostrabalhosdeimpresso) |
| [O processo de Reenvio](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#oprocessodereenvio) |
| [Verificando o status de um Job](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#verificandoostatusdeumjob) |
| [Reimprimindo trabalhos de Impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#reimprimindotrabalhosdeimpresso) |
| [Selecionando Impressora substituta](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#selecionandoumaimpressorasubstituta) |
| [Como salvar uma Impressora Substituta?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#comosalvarumaimpressorasubstituta) |
| [Tela Impressora Substituta](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#telaimpressorasubstituta) |
| [Quando a tela de seleção de Impressora Substituta é exibida?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#quandoateladeseleodeimpressorasubstitutaexibida) |

Impressão de Boleto

Na Impressão de boleto, o sistema sempre utiliza o nome da impressora como **"Padrão"**. Sendo assim, para realizar um roteamento ou imprimir em uma impressora, você deve usar este nome.

Para acompanhar a impressão do boleto acesse a tela Trabalhos de Impressão.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#rotinasdosistema) 

## Impressão de Cheques

Se o parâmetro **"Usar o PrintService para impressão? - USASERVIMP"** estiver ativado, ou seja, o Sankhya-Om irá utilizar o SPS, e a impressão de cheques é realizada utilizando este componente.

Na tela [Impressão de cheques](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115313), ao clicar em imprimir cheque, o sistema exibirá um pop-up de mesmo nome.

![Imagem 40: Na tela Impressão de cheques , ao clicar em imprimir cheque, o sistema exibirá um pop-up de mesmo nome.](https://ajuda.sankhya.com.br/hc/article_attachments/4940482526615)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#rotinasdosistema) 

## Impressão de Relatórios

A partir das configurações mencionadas abaixo, será possível efetuar a impressão de qualquer relatório utilizando o SPS. Esta rotina será acionada através de uma Rotina Java ou por meio de um Script (JavaScript), criados para utilização de um botão de ação.

Cria-se uma Rotina Java ou um Script (JavaScript) para o botão de ação, passando alguns parâmetros necessários. Em seguida, é feita a chamada da rotina do sistema passando estes parâmetros. O sistema irá processar esta solicitação e realizar a impressão do relatório através do SPS, ou seja, o sistema irá buscar a impressora informada para efetuar tal impressão. Abaixo trataremos dos passos para utilização desta rotina:

#### Criação de uma classe no Java (Rotina Java)

Crie uma classe no Java que será utilizada pelo botão de ação do sistema. Nesta classe, você deve pegar os parâmetros do usuário e chamar o serviço criado passando tais parâmetros. Desta forma, o sistema conseguirá imprimir o relatório. Considere o exemplo  abaixo de uma classe criada:

```
import java.math.BigDecimal;

public class AcaoTesteImpressaoJava implements AcaoRotinaJava {
      @Override
  public void doAction(ContextoAcao contexto) throws Exception {
if (contexto.confirmarSimNao ("Confirmar Sim Não", "Deseja confirmar a ação?", 1)) {
                  BigDecimal nuRfe = new BigDecimal ((String) contexto.getParam ("NURFE"));
                  BigDecimal codEmp = new BigDecimal ((String) contexto.getParam ("CODEMP"));
                  String localPrinterName = (String) contexto.getParam ("NOMEIMPRESSORA");

                  //Parâmetros que o relatório que usamos no teste está esperando, nesse caso
estamos imprimindo um DANFE
                  Map<String, Object> params = new HashMap<String, Object>();
                  params.put("ARQUIVO_LOGO", null);
                  params.put("PDHSIS", null);
                  params.put("PNOMEUSULOGADO", "SUP");
                  params.put("PDATSIS", null);
                  params.put("NUNOTA", new BigDecimal (68748));
                  params.put("IMPITENSNFE", new BigDecimal (1));
                  params.put("PCODUSULOGADO", 0);
                  params.put("PDIR_MODELO", "D:\'Modelos\'");

                  //A linha abaixo irá imprimir no console as descrições relacionadas ao serviço.
                  System.out.println (PlatformServiceFactory.getInstance().listServices());

                  //Criando a instancia da classe para chamar o serviço
                  PlatformService report = PlatformServiceFactory.getInstance().lookupService
("@core:report.service");

                  //Passando os parametros necessários para utilização do serviço
                  report.set("nurfe", nuRfe);
                  report.set("codemp", codEmp);
                  report.set("report.params", params);
                  report.set("printer.name", localPrinterName);

                  //Chamando a execução do serviço
                  report.execute();
       } else {
                  contexto.confirmar("Testando Confirmar", "Testando Confirmar!", 2);
                   contexto.mostraErro("Testando mensagem de erro!");
       }
}
```

Depois de criada a classe, realize sua exportação para um "arquivo.jar" e inicie o serviço do SPS. Em seguida, acesse a tela [Módulo Java](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110573) e crie um registro com o arquivo.jar referente a classe elaborada.

#### Criação de um Script (JavaScript)

Caso você não queira fazer uso da Rotina Java, você pode criar um Script passando os parâmetros necessários assim como no caso anterior, que o sistema conseguirá imprimir o relatório corretamente. Abaixo, temos um exemplo do Script criado:

```
if (confirmarSimNao (“Confirmar Sim Não”, “Deseja confirmar a ação?”, 1)) {
   var factory = javaStaticMethod(‘br.com.sankhya.modelcore.PlatformServiceFactory’,
   ’getInstance’, null, null);
   var reportService = factory.lookupService('@core:report.service');

   reportService.set('nurfe', getParam("NURFE"));
   reportService.set('codemp', getParam("CODEMP"));

   var params = ();
   params['ARQUIVO_LOGO'] = null;
   params['PDHSIS'] = null;
   params[PNOMEUSULOGADO'] = 'SUP';
   params['PDATSIS'] = null;
   params['NUNOTA'] = 68748;
   params['IMPITENSNFE'] = 1;
   params['PCODUSULOGADO'] = 0;
   params['PDIR_MODELO'] = 'D:\\Modelos\\'

   reportService.set('report.params',t);
   reportService.set('printer.name', getParam("NOMEIMPRESSORA"));

   reportService.execute();
} else {
   confirmar("Testando Confirmar", "Testando Confirmar!", 2);
   mostraErro("Testando mensagem de erro!")
}
```

O passo seguinte, de grande importância para sucesso na impressão, é a criação do Botão de Ação, que deve ser feito através da tela [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294), configurando corretamente a aba [Ações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados#abaaes) de acordo com a instância na qual será criada o Botão de ação.

Acionando o Botão de ação criado em sua tela correspondente, será apresentada um pop-up para que sejam informados os parâmetros necessários. Considere um exemplo de um Botão de ação criado no Portal de Vendas:

![Imagem 41: Acionando o Botão de ação criado em sua tela correspondente, será apresentada um pop-up para que sejam informados os…](https://ajuda.sankhya.com.br/hc/article_attachments/4935166072471)

No exemplo da imagem acima, preenchendo os campos (parâmetros) solicitados e clicando no botão **"Ok"** será acionada a rotina de impressão.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#rotinasdosistema) 

## Verificando os Trabalhos de Impressão

Quando solicitado um trabalho de impressão, esse trabalho pode ser visto na tela [Trabalhos de Impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600374). Essa tela pode ser acessada de duas maneiras:

**1.** Pelo campo de busca, informando o nome da tela, chegando-se ao caminho Trabalhos de Impressão:

![Imagem 42: 1. Pelo campo de busca, informando o nome da tela, chegando-se ao caminho Trabalhos de Impressão :](https://ajuda.sankhya.com.br/hc/article_attachments/4934823575703)

**2.** Pelo menu de contexto:

![Imagem 43: 2. Pelo menu de contexto:](https://ajuda.sankhya.com.br/hc/article_attachments/4934825066391)

A tela Trabalhos de Impressão exibe os trabalhos de impressão do usuário. Esses trabalhos são mantidos por 2 (dois) dias.

Em modo grade, você pode visualizar a lista de trabalhos, com seus respectivos dados. Já em modo formulário, você pode ver que todos os campos são desabilitados, pois esta tela destina-se apenas a apresentar os dados do trabalho.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#rotinasdosistema) 

## O processo de Reenvio

Se um erro ocorrer ao enviar o trabalho para o Servidor SPS, o componente irá tentar reenviar o trabalho após um tempo. O número de tentativas de envio e o tempo entre os envios é definido por dois parâmetros, que são:

- **Máximo tentativas de reenvio da impressão. - SPSMAXTENTIMP**: Este parâmetro define o número máximo de tentativas de envio. Após esse número ser atingido, o status do trabalho é considerado como erro de envio. O valor padrão são de 30 (trinta) tentativas.
- **Tempo mínimo entre as tentativas, em segundos. - SPSMINTMPTENT**: Neste parâmetro define-se o tempo mínimo entre cada tentativa de envio, em segundos. O valor padrão são 30 (trinta) segundos.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#rotinasdosistema) 

## Verificando o status de um Job

Após o trabalho de impressão ser enviado para o servidor SPS (status Enviado), o sistema passa a atualizar o status do job a cada 1 (um) minuto. Os status do job podem assumir os seguintes valores:

- **Pendente:** Indica que o job foi criado e aguarda ser processado;
- **Enfileirado:** Indica que o job foi colocado na fila de impressão do componente SPS;
- **Enviando:** Indica que o job está sendo enviado para o servidor SPS;
- **Enviado:** Indica que o job foi enviado para o servidor SPS e aguarda ser processado;
- **Imprimindo:** Indica que o job está sendo impresso no servidor SPS;
- **Impressora requisitando atenção:** Indica que a impressão parou e a impressora requisita a atenção do usuário, devido a ocorrência de algum problema;
- **Impresso com sucesso:** Indica que o job foi impresso com sucesso;
- **Cancelado:** Indica que o job foi cancelado no servidor SPS (normalmente, na impressora);
- **Erro de envio:** Indica que ocorreu um erro durante o envio do job para o servidor SPS;
- **Erro de impressão:** Indica que ocorreu um erro ao imprimir o job no servidor SPS;
- **Tentando enviar:** Indica que um erro ocorreu durante o envio, mas que o componente está tentando reenviar o job;
- **Desconhecido:** Indica que é possível determinar o status do job.

Você pode visualizar o status do Job na tela Trabalhos de Impressão. Essa tela não é atualizada automaticamente. O Sankhya-Om atualiza o status dos jobs internamente e você precisa atualizar a tela para visualizar o novo status.

O processo de atualização de trabalhos de impressão pode ser executado manualmente, clicando no botão **"Atualizar status"**. Esse processo atualiza somente os trabalhos de impressão do usuário.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#rotinasdosistema) 

## Reimprimindo trabalhos de Impressão

Na tela Trabalho de Impressão, um job que já foi impresso pode ser reimpresso. Esta reimpressão para ser possível, é preciso que o job esteja em um dos seguintes estados:

- Enviado;
- Imprimindo;
- Sucesso;
- Requisitando atenção;
- Erro de envio;
- Erro de impressão;

**Observação:** o estado Requisitando atenção existe por uma compatibilidade com a Java Print Service API, porém é dependente da comunicação entre a impressora e o sistema operacional. Em muitos casos, o sistema operacional não é notificado pela impressora sobre esse estado.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#rotinasdosistema) 

## Selecionando uma impressora substituta

Quando é solicitada uma impressão, o componente SPS utiliza o nome da impressora para pesquisar por uma impressora adequada. Caso não consiga localizar uma impressora, o sistema apresenta ao usuário a tela de Seleção de impressora substituta.

Essa tela permite que você escolha uma nova impressora para realizar as impressões de um grupo de impressão. Um grupo de impressão é definido por um **"Nome de Impressora"** e um **"Tipo de Documento"**. Por exemplo:

1. Tem-se um boleto enviado para a impressora de nome **"Padrão**" (grupo de impressão);
2. Nenhuma impressora com o nome de impressora Padrão foi encontrada;
3. O sistema mostra a tela de seleção de impressoras substitutas;
4. Você escolhe uma impressora, local ou remota, para imprimir o boleto destinado à impressora Padrão.

Para um grupo de impressão, você pode escolher dois tipos de impressora como substitutas, sendo uma impressora remota ou uma impressora local.

A impressora remota, é uma impressora cadastrada em um dos diversos repositórios do componente SPS. Uma impressora local, é uma impressora da máquina do usuário.

Quando a tela de Seleção de Impressora Substituta é exibida, ela pode exibir duas configurações:

#### Seleção única

A seleção única, permite que você  selecione uma impressora para um único grupo de impressão. Esse grupo pode ter um ou mais trabalhos de impressão. Neste caso, ele pode imprimir ao dar um duplo clique no ícone da impressora que deseja utilizar.

#### Seleção múltipla

A seleção múltipla é usada quando existem vários grupos de impressão, com um ou mais trabalhos de impressão em cada um. Indique uma impressora para cada grupo, mas não é obrigatório que todos os grupos tenham uma impressora selecionada. Se algum grupo de impressão ficar sem uma impressora, seus trabalhos de impressão continuam pendentes.

Em qualquer uma das opções, só é possível imprimir após selecionar ao menos 1 impressora. Se o usuário cancelar a operação, todos os jobs dos grupos de impressão continuam como pendentes.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#rotinasdosistema) 

## Quando a tela de seleção de Impressora Substituta é exibida?

A tela de seleção de impressoras pode ser exibida em duas situações:

1. Quando uma impressora não é encontrada;
2. Quando você seleciona trabalhos de impressão pendentes e clica no botão **"Impressora Substituta"**, na tela Trabalhos de Impressão.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#rotinasdosistema) 

## Como salvar uma Impressora Substituta?

Quando você indica uma ou mais impressoras substitutas, ele pode optar por salvar essa seleção de impressoras. Para isso, marque a opção **"Usar sempre esta seleção?"**, na tela de Seleção de impressão substituta.

Uma vez que ele tenha selecionado essa opção, o sistema salva a impressora escolhida, para o grupo de impressão. Assim, sempre que o sistema procurar por uma impressora chamada **"Nome da Impressora"**, se ela não for encontrada em nenhum dos repositórios de impressora, o sistema procura por um endereço de impressora, utilizando o grupo de impressão na tabela de impressoras substitutas.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#rotinasdosistema) 

## Tela Impressora Substituta

As impressoras substitutas podem ser visualizadas na tela acessada através do menu **"Configurações > Avançado > Impressão > Impressoras Substitutas"**. Essa apresenta o tipo de documento, o nome da impressora e o endereço da impressora selecionada.

Não se pode criar novas associações, nem editar as já existentes, mas você pode remover ou desvincular uma impressora. Se for utilizada a opção **"Desvincular impressoras"**, no menu de contexto, todas as impressoras substitutas serão removidas.

A tela Impressora Substituta também pode ser acessada através do menu de contexto.

![Imagem 44: A tela Impressora Substituta também pode ser acessada através do menu de contexto.](https://ajuda.sankhya.com.br/hc/article_attachments/4934982851863)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#rotinasdosistema) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#top)
