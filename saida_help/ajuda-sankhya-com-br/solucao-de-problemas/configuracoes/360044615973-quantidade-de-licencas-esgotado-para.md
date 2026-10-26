---
id: "360044615973"
titulo: "Quantidade de licenças esgotado para ' ' "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044615973-Quantidade-de-licen%C3%A7as-esgotado-para"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-08-24T12:36:26Z"
rotulos: ["#PUBLIFER", "#Revisadoclaudio", "Administração do Servidor", "Licença", "Gerenciando Licenças: Solução e Análise", "Erro", "SankhyaW", "SASConsole"]
---

# Quantidade de licenças esgotado para ' ' 

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18524529290135) MENSAGEM:**

Quantidade de licenças esgotado para 'Módulo X' : 'quantidade'.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18524553484183) SITUAÇÃO:**

Ao tentar acessar determinada rotina no sistema, é apresentada a mensagem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18524529305111) SOLUÇÃO:**

![Imagem 4: Avalie a quantidade de licenças disponíveis para a respectiva rotina através da tela 'Administração do Servidor':](https://ajuda.sankhya.com.br/hc/article_attachments/18524529309847) Avalie a quantidade de licenças disponíveis para a respectiva rotina através da tela 'Administração do Servidor':

Via SankhyaW, em Administração do Servidor, aba: Licença, na guia de 'Grupo', é possível identificar como estão dispostas as licenças, quantidade de licenças adquiridas e quantidade de licença em uso. 

![Imagem 5: Caso consiga identificar internamente os usuários que estão consumindo as respectivas licenças, identificando uma…](https://ajuda.sankhya.com.br/hc/article_attachments/18524553497495) Caso consiga identificar internamente os usuários que estão consumindo as respectivas licenças, identificando uma quantidade em uso igual a quantidade de licenças disponíveis, será necessário que determinado usuário faça logon do sistema, para liberação dessa. Caso tenha alguma dúvida sobre a quantidade de licenças considerada "em uso", siga com as orientações abaixo para análises detalhadas.

**Gerenciamento de licenças através do aplicativo SASConsole:**

- Via SAS Console, é possível gerenciar o uso de licenças do Mitra(Delphi) e/ou SankhyaW(Java).

- **Atenção:** Para conseguir utilizar o SASConsole é necessário que a máquina possua o JAVA instalado. (Caso não possua o Java intalado na máquina, este se encontra disponível  na Central de Downloads >> campo Ferramentas >> JAVA JDK)

![Imagem 6: Realize o download do aplicativo 'SASConsole': Clique aqui](https://ajuda.sankhya.com.br/hc/article_attachments/18524529319319) Realize o download do aplicativo 'SASConsole': [Clique aqui](http://downloads.sankhya.com.br/downloads?app=outros)

![Imagem 7: Instale o aplicativo.](https://ajuda.sankhya.com.br/hc/article_attachments/18524553513239) Instale o aplicativo.

![Imagem 8: Acesse Menu>>Arquivo>>Conexão, informe o IP/Host do servidor onde está instalado o SAS 3.0.](https://ajuda.sankhya.com.br/hc/article_attachments/18524529343639) Acesse Menu>>Arquivo>>Conexão, informe o IP/Host do servidor onde está instalado o SAS 3.0. 

**Atenção:**Verificar no parâmetro IPSERVACESS o IP.

**Como 'derrubar' um usuário do sistema para não consumir licenças desnecessariamente?**

![Imagem 9: Através do SASConsole devidamente instalado, será possível visualizar os usuários responsáveis pelo consumo de licença,…](https://ajuda.sankhya.com.br/hc/article_attachments/18524553520023) Através do SASConsole devidamente instalado, será possível visualizar os usuários responsáveis pelo consumo de licença, conforme exemplo a seguir:

- Acesse o Menu 'Arquivo' >> 'Administração':

![Imagem 10: Para finalizar a sessão de determinado usuário, escolha o usuário desejado na lista mencionada acima, clique com botão…](https://ajuda.sankhya.com.br/hc/article_attachments/18524553525527) Para finalizar a sessão de determinado usuário, escolha o usuário desejado na lista mencionada acima, clique com botão direito e escolha a opção "Parar Usuário":

Ao expandir a "árvore" dentro de Usuários, será possível identificar quais licenças esse está consumindo. 

![Imagem 11: Caso deseje realizar a verificação por grupo, na árvore "Licença" >> Módulos, será possível.](https://ajuda.sankhya.com.br/hc/article_attachments/18524553529495) Caso deseje realizar a verificação por grupo, na árvore "Licença" >> Módulos, será possível.

**Pela opção Gerenciar Sessões da tela Administração do Servidor(SankhyaW) é possível gerenciar licenças?**

Não é possível, a opção 'Gerenciar Sessões', não tem esta finalidade.

Esta opção visualiza os detalhes das sessões dos usuários logados ou não no sistema. Uma sessão de usuário logado é identificada quando a coluna "Nome usuário" está preenchida. Quando essa coluna está em branco é uma sessão não autenticada, isso significa que o sistema foi acessado por algum usuário mas não foi efetuado o login. Sempre que a página de login é acessada uma nova sessão pode ser criada.

Sessões do sistema não consomem licenças, as licenças são consumidas quando alguma tela é aberta, portanto as informações apresentadas aqui nem sempre podem ser utilizadas para identificar consumo de licença.
