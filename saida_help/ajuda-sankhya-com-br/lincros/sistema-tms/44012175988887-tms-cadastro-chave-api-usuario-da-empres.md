---
id: "44012175988887"
titulo: "[TMS] - Cadastro chave API usuário da empresa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012175988887--TMS-Cadastro-chave-API-usu%C3%A1rio-da-empresa"
trilha: "Lincros > TMS > Sistema - TMS"
atualizado_em: "2026-10-05T19:21:30Z"
rotulos: ["sync_hc", "lincros", "lincros_13434312", "sync_hash_82f369cbe5a4"]
---

# [TMS] - Cadastro chave API usuário da empresa

**Menu:**Sistema > Acesso > Usuário > Usuários da empresa

**Objetivo:**Indicar aonde são criadas as chaves de usuário para serem utilizadas em chamadas de API, facilitando o processo de configuração do recurso

## Considerações:

- É necessário possuir um perfil de acesso com liberação para efetuar este processo, normalmente 'Administrador';

Abaixo segue os procedimentos, mas antes precisamos entender o que seria uma API.

API é um conjunto de normas que possibilita a comunicação entre plataformas através de uma série de padrões e protocolos. Possuindo uma configuração em dois ambientes distinto é possível criar uma conexão de troca de informações e processos.

 A API Key pode ser enviada no cabeçalho da requisição com Authentication com valor Bearer <chave api key> como alternativa a autenticação via Token.

![Imagem 1: A API Key pode ser enviada no cabeçalho da requisição com Authentication com valor Bearer <chave api key> como…](https://ajuda.sankhya.com.br/hc/article_attachments/44012176265879)

Recursos que demandam a chamada de uma API para utilização de usuários e externalização de informações são necessários possuir uma chave, por questão de segurança apenas com esta chave gerada e registrada com sucesso é possível utilizar este recurso de maneira correta.

Para efetuar este processo acessar o Menu: Sistema > Acesso > Usuário > Usuários da empresa, aqui podemos proceder de duas maneiras: Cadastrar a chave em um usuário já previamente existente ou cadastrar um novo usuário já criando em conjunto com sua chave, ambos são processos similares em sua configuração.

Ao acessar o menu de Usuários da Empresa, vamos clicar no código do usuário desejado:

![Imagem 2: Ao acessar o menu de Usuários da Empresa, vamos clicar no código do usuário desejado:](https://ajuda.sankhya.com.br/hc/article_attachments/44012128424087)

Dentro do cadastro, podemos localizar o item 'Chave de Api';

![Imagem 3: Dentro do cadastro, podemos localizar o item 'Chave de Api';](https://ajuda.sankhya.com.br/hc/article_attachments/44012162564887)

Dentro deste item, temos as seguintes opções:

**Gerar Chave:** Gera uma nova chave aleatória , ao clicar nesse botão mesmo que já exista uma chave criada será gerada uma nova sem a possibilidade de retornar a antiga;

**Copiar Chave:** Copia a chave para a memória, ou seja ao utilizar o recurso colar irá colar a chave inteira de maneira automática;

**Excluir Chave:** Exclui a atual chave registrada no Usuário;

**Gerar Token Temporário:** Gera um token com validade temporária, aconselhamos entrar em contato com o suporte para utilizar e entender esse recurso e sua utilização caso seja necessário;

**Obs.:** Aconselhamos a utilizar o 'COPIAR CHAVE', para facilitar e diminuir a chance de copiar de maneira o código de chave gerado.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
