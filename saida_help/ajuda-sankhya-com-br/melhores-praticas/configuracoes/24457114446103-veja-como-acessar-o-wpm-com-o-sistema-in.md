---
id: "24457114446103"
titulo: "Veja como acessar o WPM com o sistema indisponível"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/24457114446103-Veja-como-acessar-o-WPM-com-o-sistema-indispon%C3%ADvel"
trilha: "Melhores Práticas > Configurações"
atualizado_em: "2026-07-22T14:46:45Z"
rotulos: ["Configuração", "WMS", "Servidor", "Como acessar o WPM com o sistema indisponível", "WildFly", "Navegador Sankhya"]
---

# Veja como acessar o WPM com o sistema indisponível

**Para acessar o WPM mesmo quando o sistema estiver indisponível, siga os passos abaixo:**

### Servidores Linux (WildFly):

![Imagem 1: Acesse o servidor de aplicações no qual o serviço Sankhya/WildFly está instalado;](https://ajuda.sankhya.com.br/hc/article_attachments/25168374693399) Acesse o servidor de aplicações no qual o serviço Sankhya/WildFly está instalado;

![Imagem 2: Pare o serviço do WildFly;](https://ajuda.sankhya.com.br/hc/article_attachments/25168374697495) Pare o serviço do WildFly;

![Imagem 3: Se o servidor tiver os aliás configurados, execute os seguintes comandos para parar e iniciar o serviço do WildFly…](https://ajuda.sankhya.com.br/hc/article_attachments/25168383106327) Se o servidor tiver os aliás configurados, execute os seguintes comandos para parar e iniciar o serviço do WildFly utilizando o usuário mgeweb:

- - Para parar a base de produção: killprod
  - Para parar a base de teste: killteste
  - Para parar a base de treinamento: killtreina
  - Para iniciar a base de produção: jb\_startprod
  - Para iniciar a base de teste: jb\_startteste
  - Para iniciar a base de treinamento: jb\_starttreina

(O start do serviço deve ser realizado apenas quando os arquivos sankhyaw.ear forem excluídos)

![Imagem 4: Navegue até o diretório padrão de instalação do WildFly: /home/mgeweb/wildfly_producao/standalone/deployments (esse…](https://ajuda.sankhya.com.br/hc/article_attachments/25168389020183) Navegue até o diretório padrão de instalação do WildFly: /home/mgeweb/wildfly\_producao/standalone/deployments (esse diretório pode variar dependendo de como foi feita a instalação do WildFly no servidor).

![Imagem 5: Exclua os arquivos que contêm o nome sankhyaw.ear . No Linux, para excluir os arquivos, utilize o comando rm -rf…](https://ajuda.sankhya.com.br/hc/article_attachments/25168380623511) Exclua os arquivos que contêm o nome sankhyaw.ear. No Linux, para excluir os arquivos, utilize o comando rm -rf juntamente com o nome dos arquivos. Exemplo: rm -rf sankhyaw.ear sankhya.ear.deployed

![Imagem 6: Exclua os arquivos que contêm o nome sankhyaw.ear . No Linux, para excluir os arquivos, utilize o comando rm -rf…](https://ajuda.sankhya.com.br/hc/article_attachments/25169590043287)

![Imagem 7: Após a exclusão dos arquivos, inicie novamente o serviço do WildFly.](https://ajuda.sankhya.com.br/hc/article_attachments/25169188807831)Após a exclusão dos arquivos, inicie novamente o serviço do WildFly.

### Servidores Windows (WildFly):

![Imagem 8: Acesse a tela “Serviços” do Windows;](https://ajuda.sankhya.com.br/hc/article_attachments/25168374693399) Acesse a tela “Serviços” do Windows;

![Imagem 9: Localize o serviço do WildFly;](https://ajuda.sankhya.com.br/hc/article_attachments/25168374697495) Localize o serviço do WildFly;

![Imagem 10: Pare o serviço do WildFly;](https://ajuda.sankhya.com.br/hc/article_attachments/25168383106327) Pare o serviço do WildFly;

![Imagem 11: Clique com o botão direito do mouse sobre o serviço e selecione “Propriedades”;](https://ajuda.sankhya.com.br/hc/article_attachments/25168389020183) Clique com o botão direito do mouse sobre o serviço e selecione “Propriedades”;

![Imagem 12: Identifique o diretório de instalação do WildFly;](https://ajuda.sankhya.com.br/hc/article_attachments/25168380623511) Identifique o diretório de instalação do WildFly;

![Imagem 13: Realize a exclusão dos arquivos sankhyaw.ear que constam no diretório deployments ;](https://ajuda.sankhya.com.br/hc/article_attachments/25169188807831) Realize a exclusão dos arquivos `sankhyaw.ear` que constam no diretório `deployments`;

![Imagem 14: Realize a exclusão dos arquivos sankhyaw.ear que constam no diretório deployments ;](https://ajuda.sankhya.com.br/hc/article_attachments/25169581471767)

**![Imagem 15: Após excluir esses arquivos, inicie novamente o serviço do Wildfly na tela "Serviços".](https://ajuda.sankhya.com.br/hc/article_attachments/25169581475863)
 
 ![Imagem 16: Após excluir esses arquivos, inicie novamente o serviço do Wildfly na tela "Serviços".](https://ajuda.sankhya.com.br/hc/article_attachments/25169188828055) Após excluir esses arquivos, inicie novamente o serviço do Wildfly na tela "Serviços".**

### Registro de Novo Servidor (WPM) no Navegador Sankhya:

![Imagem 17: Abra o Navegador Sankhya e faça o registro de um novo servidor através botão "Configurações" no canto superior direito…](https://ajuda.sankhya.com.br/hc/article_attachments/25168374693399) Abra o Navegador Sankhya e faça o registro de um novo servidor através botão **"Configurações"** no canto superior direito do Navegador Sankhya, e informe o IP/Link de Acesso ao sistema e adicione `/wpm` ao final. Exemplo:

- - Para acessar o sistema: `localhost:8180/mge`
  - Para acessar o WPM: `localhost:8180/wpm`

**![Imagem 18: Após cadastrar o novo servidor do WPM ( localhost:8180/wpm ) no Navegador Sankhya, selecione o mesmo após os…](https://ajuda.sankhya.com.br/hc/article_attachments/25169590071063)
 
Após cadastrar o novo servidor do WPM (`localhost:8180/wpm`) no Navegador Sankhya, selecione o mesmo após os procedimentos terem sido realizados e, assim, conseguirá acessar o WPM normalmente, mesmo que o sistema esteja indisponível.
 
![Imagem 19: Após cadastrar o novo servidor do WPM ( localhost:8180/wpm ) no Navegador Sankhya, selecione o mesmo após os…](https://ajuda.sankhya.com.br/attachments/token/B8LNqb1JSbb3Zui1iyYKC1Lit/?name=image.png)
 
Observação: O link localhost é apenas um exemplo. Em sua base, o link de acesso e IP provavelmente serão diferentes.**

Se mesmo seguindo essa orientações você não conseguir acessar o WPM, por favor, entre em contato com o Service Desk Sankhya para assistência adicional.
