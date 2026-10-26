---
id: "360044616433"
titulo: "Cannot locate or connect to SQL server. Unable to connect: SQL Server is unavailable or does not exist. Unable to connect: SQL server does not exist or network acces Alias"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616433-Cannot-locate-or-connect-to-SQL-server-Unable-to-connect-SQL-Server-is-unavailable-or-does-not-exist-Unable-to-connect-SQL-server-does-not-exist-or-network-acces-Alias"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:54:02Z"
rotulos: ["Configuração", "SQL Server", "Financeiro", "Erro de Conexão com Servidor SQL", "Erro", "BDE"]
---

# Cannot locate or connect to SQL server. Unable to connect: SQL Server is unavailable or does not exist. Unable to connect: SQL server does not exist or network acces Alias

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16815460636183) MENSAGEM:**

Cannot locate or connect to SQL server. Unable to connect: SQL Server is unavailable or does not exist. Unable to connect: SQL server does not exist or network acces
Alias: DBNSiade.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16815452551703) SOLUÇÃO:**

![Imagem 3: Acesse o aplicativo BDE na máquina local onde está ocorrendo o erro.](https://ajuda.sankhya.com.br/hc/article_attachments/16815452555031) Acesse o aplicativo BDE na máquina local onde está ocorrendo o erro.

![Imagem 4: Acesse o diretório/pasta onde está instalado o BDE: Exemplo: C:\BDE](https://ajuda.sankhya.com.br/hc/article_attachments/16815460641175) Acesse o diretório/pasta onde está instalado o BDE: Exemplo: **C:\BDE**

![Imagem 5: Execute como Administrador o executável bdeadmin.exe](https://ajuda.sankhya.com.br/hc/article_attachments/16815460642711) Execute como Administrador o executável **bdeadmin.exe**

![Imagem 6: No BDE, o campo SERVER NAME que fica em Databases e que está utilizando para acessar o sistema](https://ajuda.sankhya.com.br/hc/article_attachments/16815452566039) No BDE, o campo SERVER NAME que fica em Databases e que está utilizando para acessar o sistema

![Imagem 7: Pesquise no máquina do Servidor ou em outro Computador que está acessando o sistema normalmente, para que seja ajustado…](https://ajuda.sankhya.com.br/hc/article_attachments/16815452567703) Pesquise no máquina do **Servidor** ou em outro Computador que está acessando o sistema normalmente, para que seja ajustado o SERVER NAME, corretamente.

![Imagem 8: Salve as alterações e acesse novamente o sistema.](https://ajuda.sankhya.com.br/hc/article_attachments/16815460646807) Salve as alterações e acesse novamente o sistema.

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16815452576279) CAUSA:**

Ocorre quando o BDE do Computador não está devidamente configurado com o endereço do Servidor do sistema.
