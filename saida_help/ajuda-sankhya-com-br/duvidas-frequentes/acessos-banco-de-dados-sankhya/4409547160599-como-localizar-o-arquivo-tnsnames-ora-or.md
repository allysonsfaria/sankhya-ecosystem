---
id: "4409547160599"
titulo: "Como localizar o arquivo TNSNAMES.ORA - Oracle"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4409547160599-Como-localizar-o-arquivo-TNSNAMES-ORA-Oracle"
trilha: "Dúvidas Frequentes > Acessos/Banco de Dados - Sankhya"
atualizado_em: "2026-07-22T15:21:35Z"
rotulos: ["Configuração", "oracle", "tnsnames.ora", "listener", "Localizando o Arquivo TNSNAMES.ORA no Oracle", "Arquivo TNSNAMES.ORA Localização padrão Passos de busca", "Oracle TNSNAMES.ORA Conexão", "Banco de Dados", "Rede"]
---

# Como localizar o arquivo TNSNAMES.ORA - Oracle

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30249014463895) SOLUÇÃO:**

O arquivo tnsnames.ora é utilizado para armazenar os nomes de serviço de rede para que a estação de trabalho (cliente) consiga conectar-se ao servidor Oracle.

A localização padrão onde este arquivo fica gravado é:

 Em ambiente Windows: %ORACLE\_HOME%\network\admin;

 Em ambiente LINUX: $ORACLE\_HOME/network/admin;

**![Atenção](https://ajuda.sankhya.com.br/hc/article_attachments/16033615135383) DÚVIDA:**

Como localizar o arquivo TNSNAMES.ORA?

Para localizar o arquivo de configuração TNSNAMES.ORA, realize os passos a seguir no servidor de instalação do banco de dados Oracle:

![Imagem 3: Clique em Iniciar/Executar do Windows (Atalho Win + R);](https://ajuda.sankhya.com.br/hc/article_attachments/16033636848023) Clique em **Iniciar/Executar** do Windows (Atalho Win + R);

![Imagem 4: Digite CMD e clique em OK;](https://ajuda.sankhya.com.br/hc/article_attachments/16033615138199) Digite CMD e clique em OK;

![Imagem 5: Na tela de comandos, digite o comando TNSPING NOME_DA_BASE, conforme imagem:](https://ajuda.sankhya.com.br/hc/article_attachments/16033636856087) Na tela de comandos, digite o comando TNSPING NOME\_DA\_BASE, conforme imagem:

![Imagem 6: Na tela de comandos, digite o comando TNSPING NOME_DA_BASE, conforme imagem:](https://ajuda.sankhya.com.br/hc/article_attachments/4409546601111)

![Imagem 7: Será exibido a mensagem conforme a imagem abaixo, o caminho está indicado pela seta:](https://ajuda.sankhya.com.br/hc/article_attachments/16033636857751) Será exibido a mensagem conforme a imagem abaixo, o caminho está indicado pela seta:

![Como](https://ajuda.sankhya.com.br/hc/article_attachments/16033636860951)

![Imagem 9: Copie esse caminho até admin\ no Executar do Windows e clique em OK:](https://ajuda.sankhya.com.br/hc/article_attachments/16033636863127) Copie esse caminho até admin\ no Executar do Windows e clique em OK:

![Imagem 10: Copie esse caminho até admin\ no Executar do Windows e clique em OK:](https://ajuda.sankhya.com.br/hc/article_attachments/4409546702615)

**Importante:**note que somente o caminho foi copiado, não o **sqlnet.ora**. Outra informação importante é que o caminho pode variar de um servidor para outro.

![Imagem 11: Os arquivos serão listados nessa pasta, conforme imagem abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/16033636864919) Os arquivos serão listados nessa pasta, conforme imagem abaixo:

![Como](https://ajuda.sankhya.com.br/hc/article_attachments/16033636866327)

**Observação:** Este arquivo é responsável pela configuração da forma de comunicação entre client Oracle e banco de dados.
