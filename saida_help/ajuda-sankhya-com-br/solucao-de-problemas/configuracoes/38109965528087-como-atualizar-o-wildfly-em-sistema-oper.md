---
id: "38109965528087"
titulo: "Como atualizar o Wildfly em sistema operacional Windows"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38109965528087-Como-atualizar-o-Wildfly-em-sistema-operacional-Windows"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:02:03Z"
rotulos: ["Configuração", "Atualização", "Sankhya ID", "WildFly", "Serviço do Windows", "Servidor de Aplicação wildfly_producao", "atualizar o Wildfly", "Wildfly - Windows", "23 mod_03", "Wildfly Produção", "Windows"]
---

# Como atualizar o Wildfly em sistema operacional Windows

É fundamental manter o **Wildfly sempre atualizado** para a versão mais recente (**23 mod\_03**). Isso garante a compatibilidade do ambiente Sankhya com as últimas versões do **JDK** e demais componentes de infraestrutura, além de proporcionar **ganhos de desempenho, estabilidade e segurança**, reduzindo o risco de falhas em produção.

**OBSERVAÇÃO:** O procedimento de atualização deve ser realizado **apenas por Administradores de Sistemas** com conhecimento em Windows, ou pela equipe da **Cloud**, caso o ambiente esteja hospedado em nuvem. Antes de iniciar, é obrigatório **validar a versão do JDK** em uso. O Wildfly 23 é compatível com **JDK 8u421** (preferencialmente) até **JDK 11**. Essa versão deve estar **instalada e ativada no servidor** para garantir o correto funcionamento do ambiente.

#### Procedimento de Instalação

(1)** Acesse o servidor** onde o Wildfly atual está instalado e pare o serviço da aplicação Sankhya.

**(2)**  Logue-se como `administrador` e acesse a pasta aonde está instalado o wildfly.

**(3)**  Crie um backup do diretório atual do Wildfly:

```
windows + R >> services.msc
```

![Imagem 1: (3) Crie um backup do diretório atual do Wildfly:](https://ajuda.sankhya.com.br/hc/article_attachments/38141407556631)![Imagem 2: (3) Crie um backup do diretório atual do Wildfly:](https://ajuda.sankhya.com.br/hc/article_attachments/38141407561367)

**(4)** Acesse o portal **“Downloads Sankhya Wildfly”** utilizando o seu **Sankhya ID**.

![Imagem 3: (4) Acesse o portal “Downloads Sankhya Wildfly” utilizando o seu Sankhya ID .](https://ajuda.sankhya.com.br/hc/article_attachments/38141368150551)

**(5)** Faça o download do pacote correspondente ao seu banco de dados:

- [**''Wildfly 23.0''**](https://downloads.sankhya.com.br/downloads?app=WildFly&c=1)

![Imagem 4: ''Wildfly 23.0''](https://ajuda.sankhya.com.br/hc/article_attachments/38109965490327)

**(6)** Descompactação do pacote:

- Extraia o pacote **wildfly\_producao** utilizando o **WinRAR** ou qualquer outro gerenciador de arquivos compatível.
- Após a descompactação, o diretório resultante deverá conter:

![Imagem 5: Após a descompactação, o diretório resultante deverá conter:](https://ajuda.sankhya.com.br/hc/article_attachments/38141407565591)

**(7)** Configure o servidor no **PKG (SankhyaW Package Manager)**:

- Acesse o diretório: `c:\sankhya\sankhyaW_gerenciador_de_pacotes\bin\`
- Execute o comando: `sankhyaw-package-manager.bat`
- No menu do PKG:

Selecione a **opção 2: Selecionar servidor**

Em seguida, selecione a **opção 2: Configurar arranjo de portas**

- Escolha o servidor **wildfly\_producao** (agora com Wildfly 23).

![Imagem 6: Escolha o servidor wildfly_producao (agora com Wildfly 23).](https://ajuda.sankhya.com.br/hc/article_attachments/38109965493527)

![Imagem 7: Escolha o servidor wildfly_producao (agora com Wildfly 23).](https://ajuda.sankhya.com.br/hc/article_attachments/38110010383895)

##### IMPORTANTE: O Wildfly altera a porta padrão para 8080. Ajuste para a porta correta de produção (geralmente 8180).

**(8)** Acesse o diretório `c:/sankhya/wildfly_producao` e abra o arquivo `standalone.conf.bat` do novo Wildfly.

**(9)** Em seguida, copie as configurações de **memória** e **argumentos** do arquivo `standalone.conf.bat` do Wildfly antigo (`wildfly_producao_old`) e cole no novo, replicando todas as definições necessárias.

![Imagem 8: (9) Em seguida, copie as configurações de memória e argumentos do arquivo standalone.conf.bat do Wildfly antigo (…](https://ajuda.sankhya.com.br/hc/article_attachments/38109965495703)

**(10)** Ajuste os dados de conexão do banco de dados conforme instruções do DBA.

![Imagem 9: (10) Ajuste os dados de conexão do banco de dados conforme instruções do DBA.](https://ajuda.sankhya.com.br/hc/article_attachments/38110010386583)

##### IMPORTANTE: Os dados informados acima são individuais. Verifique também a porta HTTP: o padrão é 8080, mas se estiver configurada como 8180, ajuste-a no PKG em Configurar arranjo de portas.

![Imagem 10: IMPORTANTE: Os dados informados acima são individuais. Verifique também a porta HTTP : o padrão é 8080 , mas se estiver…](https://ajuda.sankhya.com.br/hc/article_attachments/38141407566615)

**(10)** No diretório `C:/sankhya/wildfly_producao/standalone/deployments`, verifique se **apenas** os arquivos `mge-ds.xml` e `wpm.war` estão presentes.

- Se o arquivo `mge-ds.xml` estiver ausente, revise a configuração correspondente no PKG.

![Imagem 11: Se o arquivo mge-ds.xml estiver ausente, revise a configuração correspondente no PKG.](https://ajuda.sankhya.com.br/hc/article_attachments/38110010388247)

- Também é **possível alterar a memória no WPM**, aba **"configurações".**

#### Inicialização automática do Wildfly Produção (Serviço do Windows)

##### Esta opção registra o Wildfly como serviço do Windows, permitindo a inicialização automática. Antes de prosseguir, é necessário desinstalar o serviço antigo, se houver.

**(1)** Para iniciar o processo, o menu apresenta as opções:

1. Instalação/atualização expressa do Sistema;
2. Selecionar Servidor;
3. Listar Servidores registrados;
4. Registrar Servidor;
5. Sair.

**(2)** Digite a **opção 2**: **''Selecionar Servidor''**;

**(3)** Em seguida, selecione a **opção 1**, referente ao **Servidor de Aplicação wildfly\_producao**;

**(4)** Após isso, o sistema apresentará novas opções para prosseguir com o registro do serviço.

![Imagem 12: (4) Após isso, o sistema apresentará novas opções para prosseguir com o registro do serviço.](https://ajuda.sankhya.com.br/hc/article_attachments/38110010388759)

- Digite a opção **10**.

**(5)** Em seguida, **repita o primeiro passo**:

- Menu inicial:

1. Instalação/atualização expressa do Sistema
2. Selecionar Servidor
3. Listar Servidores registrados
4. Registrar Servidor
5. Sair

**(6)** Digite a **opção 2: ''Selecionar Servidor''**.

**(7)** Depois, selecione a **opção 1**, referente ao **Servidor de Aplicação wildfly\_producao**

**(8)** O sistema exibirá novas opções para prosseguir com o registro ou configuração do serviço:

![Imagem 13: (8) O sistema exibirá novas opções para prosseguir com o registro ou configuração do serviço:](https://ajuda.sankhya.com.br/hc/article_attachments/38110010388759)

- Digite a opção **9**.

#### Inicialização do Wildfly

**(1)** Abra o **Executar** (atalho: `Win + R`) e digite:

```
services.msc
```

**(2)** Localize e **inicialize** os serviços:

- `wildfly_producao`;
- `wildfly_teste`;
- `wildfly_treina`.

![Imagem 14: wildfly_treina .](https://ajuda.sankhya.com.br/hc/article_attachments/38141368170391)

**(3)** Clique na aba **“Logon”** do serviço desejado.

![Imagem 15: (3) Clique na aba “Logon” do serviço desejado.](https://ajuda.sankhya.com.br/hc/article_attachments/38141407586327)

**(4)** No campo **“Digite o nome do objeto a ser selecionado”**, digite **administrador** e clique em **“Verificar nomes”**.

![Imagem 16: (4) No campo “Digite o nome do objeto a ser selecionado” , digite administrador e clique em “Verificar nomes” .](https://ajuda.sankhya.com.br/hc/article_attachments/38109965507095)

**(5)** Digite a **senha** da conta e clique em **“Aplicar”**.

**(6)** Em seguida, clique com o **botão direito** sobre cada serviço (`wildfly_producao`, `wildfly_teste`, `wildfly_treina`) e selecione **“Iniciar”**.

![Imagem 17: (6) Em seguida, clique com o botão direito sobre cada serviço ( wildfly_producao , wildfly_teste , wildfly_treina ) e…](https://ajuda.sankhya.com.br/hc/article_attachments/38141407588759)

**OBSERVAÇÃO:** Verifique se o logon do serviço está configurado com a conta **administrador**.

#### Reinicialização após falha

Após configurar a **inicialização automática** do serviço do Wildfly, é importante **configurar a recuperação** do serviço em caso de falhas:

**(1)** Abra as **propriedades do serviço** e acesse a aba **''Recuperação''**.

**(2)** Configure as opções de recuperação conforme o exemplo abaixo:

![Imagem 18: (2) Configure as opções de recuperação conforme o exemplo abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/38141368178455)

**(3)** Clique em **“Aplicar”** para salvar as alterações.

**(4)** Acesse o WPM seguindo o exemplo do link fornecido e configure a **memória do Wildfly**, se necessário.

![Imagem 19: (4) Acesse o WPM seguindo o exemplo do link fornecido e configure a memória do Wildfly , se necessário.](https://ajuda.sankhya.com.br/hc/article_attachments/38141368180503)

- **Senha padrão do WPM:** `tecsis` (confirme com o responsável caso seja diferente).

**(5)** Ajuste os **dados de conexão do banco** e **salve as configurações**.

![Imagem 20: (5) Ajuste os dados de conexão do banco e salve as configurações .](https://ajuda.sankhya.com.br/hc/article_attachments/38141407593879)

**(6)** Ajuste os **dados de conexão do banco** no WPM e **salve as configurações**.

![Imagem 21: (6) Ajuste os dados de conexão do banco no WPM e salve as configurações .](https://ajuda.sankhya.com.br/hc/article_attachments/38109965510039)

**(7)** Instale a **mesma versão do sistema** utilizada anteriormente ou o **último release** da mesma versão.

**(8)** Valide o **funcionamento do ambiente atualizado**.

#### Importância da atualização do Wildfly

A atualização do **Wildfly** é essencial para manter o ambiente **compatível com as versões atuais do JDK, do Java e do Sankhya**, garantindo a continuidade do **suporte técnico oficial**.

Além disso, a atualização oferece benefícios como:

- Correção de vulnerabilidades;
- Melhora no desempenho;
- Maior estabilidade do servidor de aplicações.

Ambientes que permanecem em versões antigas podem apresentar:

- Falhas no **deploy**;
- Quedas inesperadas durante o uso do sistema;
- Incompatibilidade com novos recursos;
- Instabilidade em cenários de alta carga;
- Indisponibilidade de **correções de segurança**.

A não atualização compromete **o funcionamento do sistema, a segurança e a manutenção futura do ambiente**.
