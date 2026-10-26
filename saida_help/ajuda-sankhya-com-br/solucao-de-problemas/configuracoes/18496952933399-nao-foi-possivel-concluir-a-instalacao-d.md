---
id: "18496952933399"
titulo: "Não foi possível concluir a instalação dos módulos adicionais do Wildfly"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/18496952933399-N%C3%A3o-foi-poss%C3%ADvel-concluir-a-instala%C3%A7%C3%A3o-dos-m%C3%B3dulos-adicionais-do-Wildfly"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:52:30Z"
rotulos: ["Configuração", "Atualização", "Problema com Instalação no Wildfly", "WildFly", "Erro", "Java"]
---

# Não foi possível concluir a instalação dos módulos adicionais do Wildfly

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18496926839575) **MENSAGEM:**

Não foi possível concluir a instalação dos módulo adicionais do Wildfly. Algumas funcionalidades podem apresentar comportamentos inesperados.

Erro ao instalar/atualizar módulos do Wildfly

Consulte o log para maiores detalhes, o mesmo pode ser obtido clicando no botão 'Download do log' que está localizado na parte inferior da aba 'Configurações'.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18496926846359)CAUSA:**

Falta do argumento da variável do JAVA\_HOME no arquivo .bash\_profile.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18496938761751)SOLUÇÃO:**

![Imagem 4: Certifique-se de estar conectado ao servidor de aplicação Sankhya e acesse o diretório /home/mgeweb. Você pode usar o…](https://ajuda.sankhya.com.br/hc/article_attachments/18523305525015) Certifique-se de estar conectado ao servidor de aplicação Sankhya e acesse o diretório /home/mgeweb. Você pode usar o comando 'cd' para navegar até o diretório.

```
cd /home/mgeweb
```

![Imagem 5: Editar o Arquivo .bash_profile Agora, você precisa editar o arquivo .bash_profile para adicionar a variável JAVA. Você…](https://ajuda.sankhya.com.br/hc/article_attachments/18523258837655) Editar o Arquivo .bash\_profile
Agora, você precisa editar o arquivo .bash\_profile para adicionar a variável JAVA. Você pode fazer isso usando o editor de texto nano ou vim. Vamos demonstrar como fazer isso com o nano:

```
nano .bash_profile
```

Dentro do arquivo .bash\_profile, adicione o seguinte argumento JAVA\_HOME e o caminho para a sua instalação do Java. Certifique-se de substituir '/home/mgeweb/jdk8' pelo caminho correto para a sua instalação do Java, caso seja diferente.

```
JAVA_HOME=/home/mgeweb/jdk8 ; export JAVA_HOME
PATH=$JAVA_HOME/bin:$PATH:$HOME/bin ; export PATH
```

![Imagem 6: Dentro do arquivo .bash_profile, adicione o seguinte argumento JAVA_HOME e o caminho para a sua instalação do Java.…](https://ajuda.sankhya.com.br/hc/article_attachments/18523305540375)

Depois de adicionar essas linhas, pressione 'Ctrl' + 'O' para salvar o arquivo e, em seguida, 'Ctrl' + 'X' para sair do editor nano.

Utilizando o comando VIM:

```
vim .bash_profile
```

O arquivo será aberto no vim. No vim, você está no modo de comando por padrão. Use as teclas de seta ou as teclas de movimentação (h, j, k, l) para navegar até a posição onde deseja inserir o argumento JAVA. Por exemplo, você pode usar as teclas de seta para ir até o final do arquivo.

Inserir e editar o texto:
Para entrar no modo de inserção no Vi, pressione a tecla "i" ou 'Insert'. Agora você pode começar a digitar ou colar o argumento JAVA\_HOME e o caminho, conforme mencionado no guia anterior.

Após adicionar o texto, pressione a tecla "Esc" para sair do modo de inserção. Em seguida, digite ':wq!' para salvar as alterações no arquivo e sair do modo de edição do arquivo.

![Imagem 7: Atualize o Arquivo .bash_profile Após adicionar o argumento no arquivo .bash_profile, é importante atualizá-lo para que…](https://ajuda.sankhya.com.br/hc/article_attachments/18523305543191) Atualize o Arquivo .bash\_profile
Após adicionar o argumento no arquivo .bash\_profile, é importante atualizá-lo para que as alterações tenham efeito imediato. Use o seguinte comando:

```
. .bash_profile
```

![Imagem 8: Reinicie o Serviço do Wildfly Por fim, para garantir que as alterações tenham efeito, reinicie o serviço do Wildfly no…](https://ajuda.sankhya.com.br/hc/article_attachments/18523258860439) Reinicie o Serviço do Wildfly
Por fim, para garantir que as alterações tenham efeito, reinicie o serviço do Wildfly no servidor de aplicação Sankhya. Isso pode variar dependendo do seu ambiente, mas geralmente você pode usar um comando como este utilizando o usuário mgeweb.

```
killprod

jb_startprod
```

Após seguir esses passos, você deve conseguir realizar a atualização do sistema sem encontrar mais o erro mencionado. Certifique-se de verificar se o caminho para a instalação do Java está correto e que as alterações no arquivo .bash\_profile foram feitas corretamente.

Se você continuar tendo problemas ou precisar de assistência adicional, consulte o log para obter mais detalhes ou entre em contato com o Service Desk da Sankhya para obter ajuda especializada.
