---
id: "37197963992471"
titulo: "Erro ao acessar tela Minhas Soluções: “The connection is blocked because it was initiated by a public page to connect to devices or servers on your local network.”"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37197963992471-Erro-ao-acessar-tela-Minhas-Solu%C3%A7%C3%B5es-The-connection-is-blocked-because-it-was-initiated-by-a-public-page-to-connect-to-devices-or-servers-on-your-local-network"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:18:50Z"
rotulos: ["Configuração", "Segurança", "Navegador", "Sankhya ID", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Erro", "Vincular o usuário do Sankhya Om ao Sankhya ID", "Chromium", "Minhas Soluções", "Erro ao acessar tela", "Vincular usuário do Sankhya Om"]
---

# Erro ao acessar tela Minhas Soluções: “The connection is blocked because it was initiated by a public page to connect to devices or servers on your local network.”

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/37197963985815) **MENSAGEM:**

“The connection is blocked because it was initiated by a public page to connect to devices or servers on your local network.”

![Imagem 2: “The connection is blocked because it was initiated by a public page to connect to devices or servers on your local…](https://ajuda.sankhya.com.br/hc/article_attachments/37197963986967)

**SITUAÇÃO:**

Ao acessar a tela ''**Minhas Soluções''** (Comercial » Arquivo » Cadastros » Minhas Soluções), o navegador exibe a mensagem de erro acima, impedindo o carregamento da tela após o login e bloqueando o gerenciamento ou a atualização das soluções.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/37197963987607)SOLUÇÃO:**

Para corrigir o problema, é necessário **vincular o usuário do ''Sankhya Om''** a um usuário do [**''Sankhya ID''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050259413-Sankhya-ID), garantindo autenticação correta. Siga o passo a passo abaixo:

**(1)** Acesse a tela [''**Usuários''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios) (Configurações » Controle de Acesso » Usuários).

**(2)** Localize o usuário do Om (exemplo: `GERENTE`).

**(3)** Em seguida, realize o **vínculo com um usuário do ''**Sankhya ID''.

**(4)** Acesse a tela ''Minhas Soluções'' (Comercial » Arquivo » Cadastros » Minhas Soluções) e utilize o **usuário do Sankhya ID**.

**(5)** Após o vínculo, a tela será carregada corretamente e será possível gerenciar ou atualizar as soluções normalmente.

##### Solução de Contorno (Alternativa Temporária)

Enquanto o ambiente não é ajustado, é possível contornar o bloqueio utilizando:

- **Navegador Sankhya**
- **Mozilla Firefox**

**ATENÇÃO:**Esta alternativa é temporária, pois o Firefox pode futuramente adotar políticas de bloqueio semelhantes às do Chromium.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/37197963988759)CAUSA:**

O erro está relacionado a **políticas de segurança aplicadas por navegadores baseados em Chromium**, como **Google Chrome** e **Microsoft Edge**. Após atualizações recentes, esses navegadores passaram a **bloquear conexões HTTP iniciadas por páginas públicas para endereços da rede local** (Private Network Access – PNA).

No caso da tela ''Minhas Soluções'' (Comercial » Arquivo » Cadastros » Minhas Soluções), o acesso é realizado pelo ''Sankhya Om'' via endereço HTTP (intranet). Nesse cenário, o navegador bloqueia a comunicação e impede a gravação dos tokens de autenticação no **localStorage**, fazendo com que a sessão não seja validada corretamente e a tela não carregue.

O problema ocorre principalmente em acessos por **IP interno**. Em acessos via IP externo ou em navegadores que não aplicam essa política, o erro não se manifesta.

##### OBSERVAÇÃO:

- A Sankhya **não realiza ajustes** relacionados a políticas de segurança de navegador ou infraestrutura de rede do cliente.
- Recomenda-se que o cliente avalie internamente a adoção de **HTTPS**, DNS seguro ou adequações de rede para evitar esse tipo de bloqueio no futuro.
- O comportamento não está relacionado a falha do Sankhya Place ou das soluções adquiridas.
