---
id: "360044982114"
titulo: "Orientações para configuração  de acesso externo das soluções Sankhya"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044982114-Orienta%C3%A7%C3%B5es-para-configura%C3%A7%C3%A3o-de-acesso-externo-das-solu%C3%A7%C3%B5es-Sankhya"
trilha: "Dúvidas Frequentes > Acessos/Banco de Dados - Sankhya"
atualizado_em: "2026-09-10T16:13:36Z"
rotulos: ["Configuração", "Segurança", "Configuração de rede Acesso externo DNS e NAT", "Guia para Configuração de Acesso Externo nas Soluções Sankhya", "acesso externo configuração rede segurança", "Proxy Reverso", "DNS", "Rede", "NAT"]
---

# Orientações para configuração  de acesso externo das soluções Sankhya

| **Atenção:** As configurações constantes neste manual são geralmente realizadas por profissionais da área de TI ou especialistas em rede/internet. Sua empresa poderá contratar os serviços de um desses profissionais ou empresas, e boa parte do trabalho (senão todo ele) pode ser realizado remotamente. |
| --- |

Este documento visa fornecer orientações a equipe de infra-estrutura para os métodos de configuração das soluções Sankhya para possibilitar o acesso externo à estrutura através, diretamente, da internet.

Para tanto é necessário conhecermos referente ao **NAT**(Network Address Translation) que traduz um endereço vindo da internet(Endereço Público) para um endereço em uma estrutura física e privada. Outra estrutura necessária para configuração é a estrutura de **DNS**(Domain Name System) que traduz uma URL da internet e a converte para um endereço IP.

**Pré-requisitos para o melhor aproveitamento deste manual:**

- Ter noções claras sobre configuração de rede, Linux, Firewall, modems, etc.
- Conseguir executar comandos no terminal de console do Linux ou Windows.

**Informações Importantes:**

- Procure conhecer as melhores práticas relacionadas à segurança quando se expõe um sistema para acesso pela internet. O Grupo Sankhya não se responsabiliza por possíveis falhas de segurança que possam acontecer no ambiente que circunda o sistema, e sugerimos que um profissional especialista seja consultado.
- Esse manual é fornecido seguindo um padrão de configuração amplamente utilizado, porém não é o único possível. Dúvidas sobre o manual ou sobre os procedimentos deverão ser direcionadas para um dos canais de atendimento da Sankhya (chat, e-mail, etc), e só serão atendidas caso estejam sendo seguidos os passos constantes no manual, inclusive utilizando os mesmos software e ferramentas auxiliares.

1- **Configuração de acesso sem SSL:**

Existem 2 métodos para configuração do acesso externo:

- Acesso via IP Dinâmico
- Acesso via IP Fixo

**1.1 Acesso via IP Dinâmico:**

O IP dinâmico é aquele no qual em intervalos de tempo o mesmo muda, não sendo viável neste tipo de situação a utilização de um serviço de DNS devido às trocas constantes que deverão ser realizadas sendo que, na maioria dos casos e excluindo também ambientes de cloud, o DNS aponta para um IP fixo na internet que é o endereço no qual sua aplicação será acessada.

Para solução deste problema existem alguns players de mercado que entregam um DNS fixo mesmo o IP alterando coletando esses dados de um roteador ou client interno, como é o caso dos serviços ofertados pelo DynDNS(<https://dyn.com/>) ou pelo No-IP(<https://www.noip.com/>).

![Imagem 1: Para solução deste problema existem alguns players de mercado que entregam um DNS fixo mesmo o IP alterando coletando…](https://ajuda.sankhya.com.br/hc/article_attachments/360062188034)

Figura 1.

Após configurado o DynDns ou outra ferramenta de DDNS ele irá te ofertar um endereço que é através deste que será utilizado para acessar a plataforma da Sankhya.

Feito isto, no roteador ou no firewall que entrega a solução é necessário fazer um roteamento que vai direcionar o fluxo de dados recebidos da internet e direcionar para o servidor do SankhyaOM. Quando se faz um nat você pode direcionar uma porta qualquer recebido daquele endereço e direcionando para o outro endereço na porta que está o seu SankhyaOM, como por exemplo, se o seu SankhyaOM estiver no endereço <http://sankhyaom.sankhya.com.br:8180> a porta de destino será a 8180.

O último ponto a ser liberado são as regras do firewall(caso possua) para as portas configuradas anteriormente.

![Imagem 2: O último ponto a ser liberado são as regras do firewall(caso possua) para as portas configuradas anteriormente.](https://ajuda.sankhya.com.br/hc/article_attachments/360062188274)

Figura 2.

Após essas configurações o servidor já poderá ser acessado externamente através do endereço gerado pelo serviço de DDNS.

2- **Configuração de acesso com SSL:**

Além das configurações mais simplificadas abordadas acima, podemos realizá-las adicionando uma camada de segurança a mais que permite a criptografia dos dados trafegados. Os certificados digitais são documentos eletrônicos que comprovam que uma pessoa física ou pessoa jurídica realmente é proprietário daquele site no qual está navegando através de uma cadeia de certificados, um exemplo de uma certificadora com raízes confiáveis é a Site Blindado (<https://www.siteblindado.com/>). Existem também alguns certificados criados gratuitamente porém estes não comprovam a identidade deste site, apenas criptografa o tráfego do site.

Outro ponto do SSL é que o Wildfly, atual servidor de aplicações utilizados pelo SankhyaOm, não trabalha bem com o protocolo, por isto não recomendamos a configuração diretamente no serviço. Para tal pode-se criar um serviço chamado **Proxy Reverso**, utilizando o **NGinx** ou **Apache** para essa função. Desta forma é possível aplicar o certificado e ainda garantir uma maior segurança na aplicação.

![Imagem 3: Outro ponto do SSL é que o Wildfly, atual servidor de aplicações utilizados pelo SankhyaOm, não trabalha bem com o…](https://ajuda.sankhya.com.br/hc/article_attachments/360063074473)

Figura 3.

Como apresentado na figura 3, todo tráfego chega com HTTPS(SSL) e vai para os servidores internos na porta desejada. Ainda é necessário o Nat pois como o tráfego virá de uma rede pública e irá para uma rede privada será necessário a configuração do roteador, no caso da figura 3 o ModemDSL.

**2.1 Proxy Reverso Nginx:**

Abaixo segue um exemplo do NGinx configurado como proxy-reverso no qual os campos em vermelho deverão ser alterados de acordo com a realidade da estrutura do cliente:

server  {

  listen  443 ssl http2;   

  listen [::]:443 ssl http2;

  # Endereço externo do site

   server\_name  teste.sankhya.com.br;   

  

# Logs de acesso e de erro

  access\_log /var/log/nginx/teste/access.log  main;

  error\_log /var/log/nginx/teste/error.log;

 

  # Configurações de timeout

  ssl\_session\_timeout 60m;

  ssl\_session\_cache shared:SSL:30m;

  ssl\_session\_tickets off;

 

 client\_max\_body\_size 500M;

  client\_header\_buffer\_size 64k;

  large\_client\_header\_buffers 4 64k;

 

  proxy\_connect\_timeout       600;

  proxy\_send\_timeout          600;

  proxy\_read\_timeout          600;

  send\_timeout                600;

 

  # Habilita certificado digital

  ssl  on;

  ssl\_certificate  ssl/ssl-bundle.crt;   # Replace with your cert info (I generate my own self-signed certs with openssl)

  ssl\_certificate\_key  ssl/sankhya.key; # Replace with your cert info (I generate my own self-signed certs with openssl)

  ssl\_prefer\_server\_ciphers  on;

  ssl\_protocols  TLSv1 TLSv1.1 TLSv1.2;

  ssl\_ciphers 'EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH';

 

  # URL do SankhyaOm interno, o mesmo que utiliza para acessar internamente o Sistema

  location  / {

    proxy\_pass  http://10.10.10.1:8180/;

  }

}

**2.2 Proxy Reverso Apache:**

Abaixo, de forma equivalente ao do NGinx, segue a configuração de proxy reverso para o apache:

SSLCertificateKeyFile /etc/httpd/certs/teste.key

SSLCertificateFile /etc/httpd/certs/teste.crt

SSLCertificateChainFile /etc/httpd/certs/intermediario.crt

 

<VirtualHost 192.168.1.170:443>

        ServerName teste.sankhya.com.br

        ServerAlias teste.sankhya.com.br

 

        ErrorLog /logs/teste/teste\_error\_log

        LogLevel error

        LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-agent}i\"" combined

        CustomLog /logs/teste/teste\_access\_log combined

        LogLevel error

 

        ProxyRequests Off

        ProxyVia Off

        

        <Proxy \*>

                Require all granted

                #Order Deny,Allow

                #Allow from all

        </Proxy>

 

        ProxyPass / http://10.10.10.1:8180/

        ProxyPassReverse / http://10.10.10.1:8180/

 

        ProxyTimeout 600

 

        RedirectMatch ^/$ https://skw-bia.sankhya.com.br/mge

 

        SSLEngine on

</VirtualHost>

3- **Configuração do NoIP:**

O NoIP é um serviço de DNS que converte seu IP dinâmico para um nome. Este serviço é muito útil quando precisamos ter uma aplicação disponibilizada via internet sem ter necessidade de um IP fixo para o mesmo. O serviço funciona tanto em sistemas operacionais Windows quanto em Linux além de estar disponível também para alguns modens.

**3.1 Realizando registro do NoIP:**

Para realizar a inscrição no site do NoIP acesse o link<http://www.noip.com/pt-BR> e escolha a opção inscrever-se.

![Imagem 4: Para realizar a inscrição no site do NoIP acesse o link http://www.noip.com/pt-BR e escolha a opção inscrever-se.](https://ajuda.sankhya.com.br/hc/article_attachments/360062190354)

Figura 4.

Feito isto preencha os seus dados e no campo nome do host informe o endereço que deseja cadastrar para acessar o SankhyaOm externamente e escolha a opção Cadastre Gratuitamente. Um email de confirmação será enviado para sua conta de email informada no momento do cadastro. Ao finalizar o cadastro clique em **Entrar** e digite os dados cadastrados anteriormente.

A tela abaixo será aberta para completar o cadastro:

![Imagem 5: A tela abaixo será aberta para completar o cadastro:](https://ajuda.sankhya.com.br/hc/article_attachments/360062190494)

Figura 5.

- Clique sobre o botão **Adicione agora** para completar o seu cadastro.
- Escolha um nome de usuário e complete os campos para finalizar o cadastro.

**3.2 Instalação do NoIP em ambiente Windows:**

Para efetuar o download do aplicativo do No-IP clique sobre o link abaixo e selecione **Faça Download Agora**. 

<https://www.noip.com/pt-BR/download?page=win>

- Execute o aplicativo baixado anteriormente e selecione a opção **I Agree.**
- Na próxima tela escolha o local de instalação e clique em **Install**.
- Deixe marcado a opção Launch DUC e clique em **Finish**.
- Depois de instalado o aplicativo ele será aberto solicitando o email e a senha do cadastro do NoIP.

![Imagem 6: Depois de instalado o aplicativo ele será aberto solicitando o email e a senha do cadastro do NoIP.](https://ajuda.sankhya.com.br/hc/article_attachments/360062190694)

Figura 6.

Efetuado o login clique em **Edit Hosts**, nesta tela será marcado o host que criou no momento do cadastro no site do NoIP. Após selecionado clique em **Save**.

![Imagem 7: Efetuado o login clique em Edit Hosts , nesta tela será marcado o host que criou no momento do cadastro no site do…](https://ajuda.sankhya.com.br/hc/article_attachments/360063075953)

Figura 7.

Após efetuado os procedimentos o No-IP estará configurado e pronto para uso:

![Imagem 8: Após efetuado os procedimentos o No-IP estará configurado e pronto para uso:](https://ajuda.sankhya.com.br/hc/article_attachments/360063076033)

Figura 8.
