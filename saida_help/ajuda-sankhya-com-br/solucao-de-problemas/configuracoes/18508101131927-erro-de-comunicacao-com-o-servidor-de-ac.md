---
id: "18508101131927"
titulo: "Erro de comunicação com o servidor de acessos. Verifique se o SaaS está iniciado e se o parâmetro IPSERVACESS está configurado com o IP correto da máquina onde se encontra o SAS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/18508101131927-Erro-de-comunica%C3%A7%C3%A3o-com-o-servidor-de-acessos-Verifique-se-o-SaaS-est%C3%A1-iniciado-e-se-o-par%C3%A2metro-IPSERVACESS-est%C3%A1-configurado-com-o-IP-correto-da-m%C3%A1quina-onde-se-encontra-o-SAS"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-08-18T19:38:52Z"
rotulos: ["Configuração", "Segurança", "Preferências", "Financeiro", "resuma esse texto com um titulo e um conjunto de 3 palavras chaves :", "Erro"]
---

# Erro de comunicação com o servidor de acessos. Verifique se o SaaS está iniciado e se o parâmetro IPSERVACESS está configurado com o IP correto da máquina onde se encontra o SAS

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18508058047767) **MENSAGEM:**

Erro de comunicação com o servidor de acessos. Verifique se o SAS está iniciado e se o parâmetro IPSERVACESS está configurado com o IP correto da máquina onde se encontra o SAS.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18508116169495)CAUSA:**

Esse erro geralmente ocorre quando o IP do servidor do SAS configurado no parâmetro IPSERVACESS é inacessível ou bloqueado na máquina em que está o MGE/Mitra.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18508072138775)SOLUÇÃO:**

![Imagem 4: Verifique se na pasta configuração do SAS o arquivo sas.cfg está com a nova string de conexão com o banco de dados.…](https://ajuda.sankhya.com.br/hc/article_attachments/19477594050583) Verifique se na pasta configuração do SAS o arquivo sas.cfg está com a nova string de conexão com o banco de dados. Caso haja algum problema nesta configuração, não será possível a conexão ao banco de dados e o serviço ficará indisponível.

![Imagem 5: Acesse o MGE CONFIGURAÇÕES, vá no menu AVANÇADO > PREFERÊNCIAS > TODAS PREFERÊNCIAS...](https://ajuda.sankhya.com.br/hc/article_attachments/19477594054551) Acesse o MGE CONFIGURAÇÕES, vá no menu AVANÇADO > PREFERÊNCIAS > TODAS PREFERÊNCIAS...

Pesquise pelo parâmetro **IP do servidor de acessos -IPSERVACESS** e verifique se o IP configurado lá de fato corresponde ao IP em do servidor em que o SAS está instalado.

![Imagem 6: Pesquise pelo parâmetro IP do servidor de acessos -IPSERVACESS e verifique se o IP configurado lá de fato corresponde…](https://ajuda.sankhya.com.br/attachments/token/IVeqE2dQwqMfgHPWrk531T3OR/?name=image.png)

Caso não esteja, altere e faça um teste. Verifique também se a porta 10050 está liberada neste servidor e caso não esteja altere a porta no arquivo de configuração do SAS: sas.cfg ou libere a porta padrão do SAS dentro do servidor.

Caso o caminho já esteja correto verifique o artigo disponibilizado abaixo para ajustes:

[Conexão com o serviço de autenticação (SAS) não estabelecida](https://ajuda.sankhya.com.br/hc/pt-br/articles/360054489734)
