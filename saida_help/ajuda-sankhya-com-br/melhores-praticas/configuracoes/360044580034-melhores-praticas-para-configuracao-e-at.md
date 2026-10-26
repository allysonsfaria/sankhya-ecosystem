---
id: "360044580034"
titulo: "Melhores práticas para configuração e atualização via Gerenciador de Pacotes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044580034-Melhores-pr%C3%A1ticas-para-configura%C3%A7%C3%A3o-e-atualiza%C3%A7%C3%A3o-via-Gerenciador-de-Pacotes"
trilha: "Melhores Práticas > Configurações"
atualizado_em: "2026-07-22T15:51:17Z"
rotulos: ["#criadoporUEDER", "Configuração", "Atualização", "Sankhya-W", "Atualização com Gerenciador de Pacotes", "Gerenciador de Pacotes", "Manutenção"]
---

# Melhores práticas para configuração e atualização via Gerenciador de Pacotes

O Gerenciador de Pacotes é uma ferramenta que realiza os trabalhos de manutenção e atualização do Sankhya-W em ambientes Windows ou Linux. É executada através de um console e que possui passos intuitivos para realizar estas tarefas. Nesse material iremos abordar o processo de atualização do sistema.

Assim como o WPM (Web Package Manager), o Gerenciador de Pacotes executa os pacotes de atualização do Sankhya-W. A principal diferença entre eles é que o Gerenciador de Pacotes realiza esta tarefa com o sistema fora do ar. Isto serve para que possam ser realizados ajustes na estrutura do Wildfly (JBoss), e este pode ser solicitado na atualização via WPM, de acordo com as alterações contidas no pacote.

O primeiro passo para a atualização do sistema é ter certeza de que o Gerenciador de Pacotes encontra-se em sua versão mais recente.

Para verificar a versão do gerenciador de pacotes, basta executá-lo.

No Linux: Digite o comando pkg no console, conectado como usuário mgeweb.

Observação.: Caso você não possua conhecimento em SO Linux, solicite apoio à sua equipe de TI.

No Windows: Localize a pasta do gerenciador de pacotes, e execute o arquivo <Pasta do gerenciador>\bin\**sankhyaw-package-manager.exe**.

Ao abrir, compare com a versão do Gerenciador de Pacotes disponibilizada em <http://downloads.sankhya.com.br/>.

**Exemplo:**

![Imagem 1: Exemplo:](https://ajuda.sankhya.com.br/hc/article_attachments/16996346256919)

[Versão mais recente do Gerenciador]

Gerenciador de pacotes:

![Imagem 2: Gerenciador de pacotes:](https://ajuda.sankhya.com.br/hc/article_attachments/16996417628055)

[Versão do Gerenciador de Pacotes]

Caso esteja em versões diferentes, é necessário baixar a versão do aplicativo referente ao seu sistema operacional e realizar a instalação.

Lembre-se de copiar os arquivos das pastas **conf** e **extensions** da versão anterior do Gerenciador para a nova.

Após realizar a atualização do Gerenciador de Pacotes, é necessário baixar o pacote da versão que deseja atualizar. O download também é feito através do endereço [http://downloads.sankhya.com.br/.](http://downloads.sankhya.com.br/)

![Imagem 3: Após realizar a atualização do Gerenciador de Pacotes, é necessário baixar o pacote da versão que deseja atualizar. O…](https://ajuda.sankhya.com.br/hc/article_attachments/16996346256919)

[Versões disponíveis no site]

Após baixar o pacote que deseja atualizar, você deverá colocá-lo em <Pasta do gerenciador>\pkgs.

Caso o servidor seja Linux, é recomendado que utilize um aplicativo como [WinSCP](https://winscp.net/eng/download.php) para realizar a transferência do pacote. Esta operação deve ser realizada com o usuário mgeweb.

Com o pacote no diretório, o próximo passo é realizar a instalação do pacote. Para isto, no menu inicial do Gerenciador, selecione a opção “[1] Instalação/atualização expressa do Sistema”. Será apresentada a mensagem conforme imagem abaixo a seguir informando sobre o que irá ser feito. Também será recomendado realizar um backup da base de dados antes de efetuar o procedimento:

[Informações sobre o procedimento]

Estando ciente, informe a opção “S” e dê ENTER para que seja dado prosseguimento na atualização.

Após confirmar esta opção, será apresentada a lista com os servidores (instâncias), para que informe o número correspondente à instância do Wildfly que deseja atualizar.

Após definir a instância que deseja atualizar, será necessário selecionar o pacote de atualização que deseja executar. Estes pacotes estão salvos na pasta pkgs do Gerenciador de Pacotes que realizamos no passo anterior.

[Seleção do pacote de atualização]

Após selecionar o pacote e teclar ENTER, será dado início ao processo de atualização.

Neste processo serão executados automaticamente os passos abaixo:

- Informações da atualização:

- Atualização dos scripts de banco de dados:

- Atualização de metadados do sistema:

- Compilação dos objetos inválidos, atualização de binários e extensões (caso existam):

Após finalizar o processo de atualização, é necessário inicializar o sistema.
