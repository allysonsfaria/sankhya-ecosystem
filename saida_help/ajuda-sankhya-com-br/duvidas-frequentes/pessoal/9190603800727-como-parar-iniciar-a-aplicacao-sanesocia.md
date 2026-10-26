---
id: "9190603800727"
titulo: "Como parar/iniciar a aplicação Sanesocial em sistema operacional Linux"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9190603800727-Como-parar-iniciar-a-aplica%C3%A7%C3%A3o-Sanesocial-em-sistema-operacional-Linux"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-07-29T13:30:21Z"
rotulos: ["Configuração", "Serviços", "não apagar", "Linux", "Parar/iniciar Sanesocial em sistema operacional Linux", "Conecte-se via SSH", "Acesse a pasta \"sanesocial\"", "Sanesocial", "SSH"]
---

# Como parar/iniciar a aplicação Sanesocial em sistema operacional Linux

![Imagem 1: Acesse o servidor em que o sanesocial está instalado com um aplicativo de conexão ssh, aqui, por exemplo, será com o…](https://ajuda.sankhya.com.br/hc/article_attachments/16678133868311) Acesse o servidor em que o sanesocial está instalado com um aplicativo de conexão ssh, aqui, por exemplo, será com o putty:

![Imagem 2: Acesse o servidor em que o sanesocial está instalado com um aplicativo de conexão ssh, aqui, por exemplo, será com o…](https://ajuda.sankhya.com.br/hc/article_attachments/9190051543703)

![Imagem 3: Feito o login com o devido usuário e senha (geralmente o usuário em que foi instalado é o mgeweb, mas pode ser um…](https://ajuda.sankhya.com.br/hc/article_attachments/16678149672727) Feito o login com o devido usuário e senha (geralmente o usuário em que foi instalado é o mgeweb, mas pode ser um usuário diferente), acesse a pasta do sanesocial com o comando cd sanesocial. Antes ainda é possível verificar se o serviço dele está no ar com o comando:  ps aux | grep sanesocial:

![Imagem 4: Feito o login com o devido usuário e senha (geralmente o usuário em que foi instalado é o mgeweb, mas pode ser um…](https://ajuda.sankhya.com.br/hc/article_attachments/9190427547415)

![Imagem 5: Retornando estas linhas, indicam que o processo do sanesocial está em execução. Para reiniciá-lo, a partir da pasta do…](https://ajuda.sankhya.com.br/hc/article_attachments/16678133876119) Retornando estas linhas, indicam que o processo do sanesocial está em execução.
Para reiniciá-lo, a partir da pasta do sanesocial, pare-o antes com o comando **./sanesocial-service stop**
Em seguida para iniciar o serviço do Sanesocial execute **nohup ./sanesocial-service start > /dev/null**
