---
id: "39011143271447"
titulo: "Como efetuar a atualização da JDK em servidor Windows?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39011143271447-Como-efetuar-a-atualiza%C3%A7%C3%A3o-da-JDK-em-servidor-Windows"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-07-22T14:00:39Z"
rotulos: ["Configuração", "Servidor", "Atualização", "JDK", "Variaveis de ambiente do sistema", "Servidor Windows", "Atualização da JDK", "Atualização da JDK no Windows", "Java", "Java Development Kit", "Windows"]
---

# Como efetuar a atualização da JDK em servidor Windows?

##### IMPORTANTE: O procedimento de atualização deve ser executado exclusivamente por um SysAdmin ou pela equipe da Cloud caso o ambiente esteja hospedado em nuvem. A JDK é um pacote de software que você pode usar para desenvolver aplicativos baseados em Java. Este pacote é imprescindível para o uso das aplicações Sankhya Web (Sankhya OM e JivaEvo).

| Recomendamos que solicite a equipe de TI da Empresa, que execute o procedimento abaixo. Também, deve-se programar um horário que não irá interromper a operação da empresa, ou avisar aos usuários sobre a manutenção e que o sistema ficará fora do ar, por alguns instantes. |
| --- |

#### Procedimento

##### **(1)** Acesse o ''Gerenciador de Tarefas'', localize o processo Java que está executando o WildFly e finalize-o.

![Imagem 1: (1) Acesse o ''Gerenciador de Tarefas'' , localize o processo Java que está executando o WildFly e finalize-o.](https://ajuda.sankhya.com.br/hc/article_attachments/39011143237783)![Imagem 2: (1) Acesse o ''Gerenciador de Tarefas'' , localize o processo Java que está executando o WildFly e finalize-o.](https://ajuda.sankhya.com.br/hc/article_attachments/39011143238039)

**(2)** Acesse a **''Central de Downloads''** da Sankhya e realize o download da última versão disponível da JDK do Java para Windows.

![Imagem 3: (2) Acesse a ''Central de Downloads'' da Sankhya e realize o download da última versão disponível da JDK do Java para…](https://ajuda.sankhya.com.br/hc/article_attachments/39011179762071)

**(3)** Execute o JDK como administrador para evitar futuros erros de permissão.

![Imagem 4: (3) Execute o JDK como administrador para evitar futuros erros de permissão.](https://ajuda.sankhya.com.br/hc/article_attachments/39011143246871)

**(4)** Será apresentada a tela de setup de instalação do **Java Development Kit**, clique em **''Next''** para iniciar.

![Imagem 5: (4) Será apresentada a tela de setup de instalação do Java Development Kit , clique em ''Next'' para iniciar.](https://ajuda.sankhya.com.br/hc/article_attachments/39123417125527)

**(5)** Na próxima página, valide o diretório onde o Java será instalado. Por padrão, será utilizado o caminho `C:\Program Files\Java\jdk-1.8`. Caso seja necessário alterar o diretório padrão, clique em **"Change"**.

![Imagem 6: (5) Na próxima página, valide o diretório onde o Java será instalado. Por padrão, será utilizado o caminho C:\Program…](https://ajuda.sankhya.com.br/hc/article_attachments/39011143249559)

**(6)** Clique em "Next" para prosseguir.

**(7)** Copie o caminho que foi efetuado e acesse as **"Variáveis de ambiente do sistema"**.

![Imagem 7: (7) Copie o caminho que foi efetuado e acesse as "Variáveis de ambiente do sistema" .](https://ajuda.sankhya.com.br/hc/article_attachments/39011179768471)

**(7)** Clique em **"Variáveis de ambiente"**.

![Imagem 8: (7) Clique em "Variáveis de ambiente" .](https://ajuda.sankhya.com.br/hc/article_attachments/39011179769879)

**(8)** Nas variáveis do sistema, localize a variável **"JAVA\_HOME"** e altere seu valor para o caminho copiado anteriormente, conforme o exemplo abaixo:

![Imagem 9: (8) Nas variáveis do sistema, localize a variável "JAVA_HOME" e altere seu valor para o caminho copiado anteriormente,…](https://ajuda.sankhya.com.br/hc/article_attachments/39011179770903)![Imagem 10: (8) Nas variáveis do sistema, localize a variável "JAVA_HOME" e altere seu valor para o caminho copiado anteriormente,…](https://ajuda.sankhya.com.br/hc/article_attachments/39011143254295)

**(9)** Clique em **"OK"** para confirmar e feche a janela de variáveis.

**(10)** Acesse os serviços do Windows (atalho: **Win + R → services.msc**) e ative novamente o serviço do WildFly.

![Imagem 11: (10) Acesse os serviços do Windows (atalho: Win + R → services.msc ) e ative novamente o serviço do WildFly.](https://ajuda.sankhya.com.br/hc/article_attachments/39011179772311)
