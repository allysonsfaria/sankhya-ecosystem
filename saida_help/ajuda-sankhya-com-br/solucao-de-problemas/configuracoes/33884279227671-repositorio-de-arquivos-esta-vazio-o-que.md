---
id: "33884279227671"
titulo: "Repositório de arquivos está vazio: O que verificar?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33884279227671-Reposit%C3%B3rio-de-arquivos-est%C3%A1-vazio-O-que-verificar"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:28:02Z"
rotulos: ["Configuração", "FREPBASEFOLDER", "Repositório de Arquivos", "Parâmetro", "Erro", "O que verificar?", "pastas do servidor", "usuário SUP", ".sw_file_repositor", "Repositório de arquivos está vazio", "Sistema"]
---

# Repositório de arquivos está vazio: O que verificar?

O Repositório de Arquivo funciona como um espelho das pastas do servidor, mostrando na interface do sistema os diretórios e arquivos conforme o caminho definido. Sua correta configuração depende de parâmetros específicos, especialmente o ''**FREPBASEFOLDER''**, que deve apontar para o diretório-base correto. Neste artigo, serão apresentadas as configurações essenciais para evitar que o Repositório de Arquivos apareça vazio.

**Atenção:** é necessário estar logado com o usuário SUP.

A seguir, detalhamos as configurações que impactam diretamente essa funcionalidade.

![Imagem 1: A seguir, detalhamos as configurações que impactam diretamente essa funcionalidade.](https://ajuda.sankhya.com.br/hc/article_attachments/33884306685463)

#### Configurações essenciais

**(1)** Parâmetro **''FREPBASEFOLDER''** (Diretório base para o repositório de arquivos):

Esse é o principal parâmetro que define qual diretório do servidor será refletido na tela de Repositório de Arquivos. O sistema utiliza o valor deste parâmetro para localizar as pastas e arquivos que devem ser exibidos.

**Exemplos de configuração:**

- **Linux:**
  FREPBASEFOLDER = /home/mgeweb/
- **Windows:**
  FREPBASEFOLDER = D:\mgeweb

Nesse cenário, o sistema exibirá no Repositório de Arquivos tudo o que estiver contido dentro desses diretórios.

**(2)** Quando o parâmetro está vazio:

Caso o FREPBASEFOLDER esteja sem valor definido, o sistema considera como diretório padrão uma pasta chamada **.sw\_file\_repositor** dentro do diretório do usuário.

Nesse caso, é comum que o sistema não consiga exibir ou salvar arquivos, pois essa pasta pode não existir ou não possuir permissões de leitura/escrita, resultando em um repositório completamente vazio.

**(3)** Quando o parâmetro aponta para um diretório inexistente:

- Se o valor for, por exemplo, **D:\Teste** e esse diretório não existir, ao acessar o Repositório de Arquivos, o sistema tentará criá-lo automaticamente.
- Se o valor for apenas **teste** (sem path completo), o sistema criará esse diretório dentro da pasta **bin** do JBoss (ou do WildFly), que é o diretório base da aplicação. Se já existir, ele será utilizado normalmente.

**(4)** Verificando o histórico de alterações do parâmetro:

Se os arquivos eram exibidos anteriormente e pararam de aparecer, é importante verificar se houve alterações recentes no valor do parâmetro, o que pode ter causado o problema.

Você pode consultar o histórico usando o SQL abaixo:

**SELECT \* FROM TSIPARLGT**

**WHERE CHAVE LIKE '%FREPBASEFOLDER%'**

**ORDER BY DHACAO DESC;**

**Importante:** Antes de alterar o valor do parâmetro FREPBASEFOLDER, certifique-se de que o novo diretório realmente existe e que o usuário da aplicação possui permissão total (leitura, gravação e execução).

**(1)** Além disso, esse parâmetro também impacta outras funcionalidades do sistema, como:

- Anexo de arquivos em cadastros;
- Impressão de logomarcas em relatórios e pedidos;
- Caminhos padrão usados por eventos personalizados.

**CAUSA:**

A exibição vazia do Repositório de Arquivos é normalmente causada por uma configuração incorreta ou ausente do parâmetro FREPBASEFOLDER.

Quando esse parâmetro está:

- **Vazio**: o sistema tenta acessar um diretório padrão, que pode não existir ou estar sem permissão.
- **Com caminho inválido**: o sistema cria um novo diretório onde for possível, geralmente fora do local desejado, resultando em um repositório sem os arquivos esperados.

Essas situações ocorrem frequentemente após mudanças de ambiente, atualizações, restauração de backup ou modificações manuais no valor do parâmetro, sem validação do impacto.
