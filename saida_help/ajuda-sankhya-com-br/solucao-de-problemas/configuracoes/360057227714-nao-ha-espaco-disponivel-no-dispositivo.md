---
id: "360057227714"
titulo: "Não há espaço disponível no dispositivo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360057227714-N%C3%A3o-h%C3%A1-espa%C3%A7o-dispon%C3%ADvel-no-dispositivo"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:26:54Z"
rotulos: ["Configuração", "Atualização", "não apagar", "Linux", "COM_E00510", "Falha de Espaço em Disco", "Erro", "Windows"]
---

# Não há espaço disponível no dispositivo

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16251883616919) MENSAGEM**:

[COM\_E00510] Não há espaço disponível no dispositivo.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16251883633559) CAUSA:**

Mensagem apresentada devido a partição do HD em que o SankhyaOm está instalado ter chegado a 100% de ocupação.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16251854187671) SOLUÇÃO:**

Mensagem apresentada devido a partição do HD em que o SankhyaOm está instalado ter chegado a 100% de ocupação. Para solução, o tópico 1 citado abaixo poderá ser seguido para LINUX e os tópicos 2 e 3 para ambos (Linux e Windows):

![Imagem 4: Verifique no /home/mgeweb/ se existe um arquivo 'nohup.out' e se utiliza o sanesocial. Acesse a pasta dele e localize…](https://ajuda.sankhya.com.br/hc/article_attachments/16251883624215) Verifique no /home/mgeweb/ se existe um arquivo 'nohup.out' e se utiliza o sanesocial. Acesse a pasta dele e localize este arquivo. É possível apagar em ambos os locais (**análise específica para sistema operacional Linux)**

**(1)** Ainda sobre este arquivo para o sanesocial e para o wildfly, para não gerá-lo, é importante que se tenha no aliás de configuração de start do SankhyaOm e do Sanesocial o comando /dev/null;

**(1)** Por exemplo, se o Sanesocial estiver instalado em: /home/mgeweb ao iniciá-lo com: home/mgeweb/sanesocial/./sanesocial-service start > /dev/null;

**(1)** Então, o arquivo nohup.out não vai ser gerado;

**(1)** Para facilitar o trabalho, pode-se criar um aliás para que o comando de start seja executado sem ter que decorar isso.

Portanto, crie no .bash\_profile do linux os comandos de start e stop e, dessa forma, ele utilizará sempre estes para não gerar o arquivo. Para abrir o .bash\_profile, faça login no servidor com o usuário mgeweb e no /home/mgeweb execute vi .bash\_profile

Neste arquivo observa-se que os comandos de start e stop do Sankhya-W estão lá já listados, então vá até o fim deste arquivo e coloque as configurações abaixo. Feito isso, saia do terminal, entre novamente e reinicie o sanesocial com os novos comandos, para parar: stopsan e iniciar: startsan

**#CONFIGURACAO START STOP SANESOCIAL**

alias startsan='/home/mgeweb/sanesocial/./sanesocial-service start > /dev/null'

alias stopsan='/home/mgeweb/sanesocial/./sanesocial-service stop'

Observe também se neste mesmo arquivo .bash\_profile tem a configuração para start do Sankhya, está também com o dev/null. Ficando assim:

alias jb\_startprod=' killprod; rmltwprod; nohup /home/mgeweb/wildfly\_producao/bin/standalone.sh -bmanagement 0.0.0.0 >& /dev/null &'

![Imagem 5: Além deste arquivo, é possível apagar os pacotes de atualização antigos do sistema que podem estar na pasta…](https://ajuda.sankhya.com.br/hc/article_attachments/16251854193815) Além deste arquivo, é possível apagar os pacotes de atualização antigos do sistema que podem estar na pasta /home/hde/sankhyaw-wpm/pkgs, diretamente nesta pasta ou pelo atualizador do sistema (WPM) acessando as opções: Exibir todas as versões > aba Disponíveis localmente > Deletar todos arquivos de atualização.

![Imagem 6: Os logs antigos do SankhyaOm também podem ser apagados na pasta do wildfly: Wildfly > standalone > log.](https://ajuda.sankhya.com.br/hc/article_attachments/16251883631127) Os logs antigos do SankhyaOm também podem ser apagados na pasta do wildfly: Wildfly > standalone > log.
