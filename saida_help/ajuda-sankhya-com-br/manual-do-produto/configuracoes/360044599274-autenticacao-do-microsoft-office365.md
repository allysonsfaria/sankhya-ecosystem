---
id: "360044599274"
titulo: "Autenticação do Microsoft Office365"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599274-Autentica%C3%A7%C3%A3o-do-Microsoft-Office365"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:48:38Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Segurança", "Servidor", "Integração", "Administração", "Autenticação", "Microsoft", "Office365", "br.com.sankhya.core.cfg.administracaoservidoroffice", "Autenticação do Microsoft Office365 manual", "Configuração da Autenticação do Microsoft Office365"]
---

# Autenticação do Microsoft Office365

Trataremos neste artigo, sobre as etapas necessárias para à Autenticação do Microsoft Office365:

**1.** Realize o login ou crie uma nova conta no Portal de Registro de Aplicativos que irá vincular a sincronização realizada pelo sistema com o recurso da Agenda da Microsoft. Essa medida é necessária, pois é a maneira que a Microsoft identifica quem está acessando e solicita a autorização para utilizar a conta por aplicativos de terceiros. Para isso é preciso acessar o link: <https://apps.dev.microsoft.com>

![clip4589](https://ajuda.sankhya.com.br/hc/article_attachments/360060992654)

**2.** Após o login, será apresentada a tela a baixo:

![clip4809](https://ajuda.sankhya.com.br/hc/article_attachments/360061918013)

**3.** Clique no botão **"Adicionar um aplicativo"**. Será exibido um pop-up solicitando o nome para este novo aplicativo. Informe o nome do sistema (Sankhya-Om ou Jiva).

![Imagem 3: 3. Clique no botão "Adicionar um aplicativo" . Será exibido um pop-up solicitando o nome para este novo aplicativo.…](https://ajuda.sankhya.com.br/hc/article_attachments/1500003035721)

**4.** Após a criação do aplicativo, ocorre o direcionamento à página de configuração do aplicativo. Nesta página é necessário que o ID do Aplicativo seja anotado, pois este será inserido com um parâmetro do sistema.

![Imagem 4: 4. Após a criação do aplicativo, ocorre o direcionamento à página de configuração do aplicativo. Nesta página é…](https://ajuda.sankhya.com.br/hc/article_attachments/360104034053)

**5.** Além do ID do aplicativo é necessário Gerar Nova Senha:

![Imagem 5: 5. Além do ID do aplicativo é necessário Gerar Nova Senha:](https://ajuda.sankhya.com.br/hc/article_attachments/1500002988162)

**Observação:** esta senha gerada só será exibida uma única vez, por isso, salve esta informação com cuidado.

**6.** É necessário também cadastrar uma URL de Redirecionamento. Para isso: 

**6.1** Clique em **"Adicionar Plataforma"**

![clip4819](https://ajuda.sankhya.com.br/hc/article_attachments/360060992714)

**6.2** Selecione a Web:

![clip4824](https://ajuda.sankhya.com.br/hc/article_attachments/360060992734)

**6.3** Preencha uma URL de redirecionamento:

![clip4825](https://ajuda.sankhya.com.br/hc/article_attachments/360060992754)

#### O que é uma URL de Redirecionamento?

Ao finalizar o processo de autorização, a Microsoft precisa retornar as informações de acesso para o sistema para que seja possível a sincronização dos eventos na agenda. Sendo assim, é necessário que seja cadastrado um endereço validado na internet, isto é, que o sistema consiga ser acessado externamente. Um detalhe importante é que este endereço deve ser **"HTTPS"**, pois o redirecionamento só é permitido por meio de uma conexão segura.

Exemplo de URL de redirecionamento:

<https://www.SEUDOMINIO.com.br/mge/genericOAuth.mge>

![Imagem 9: O endereço correto sempre deverá terminar com "/mge/genericOAuth.mge" , que se trata da página dentro do sistema que…](https://ajuda.sankhya.com.br/hc/article_attachments/16513962808087) O endereço correto sempre deverá terminar com **"/mge/genericOAuth.mge"**, que se trata da página dentro do sistema que espera receber os dados de acesso da agenda e salvar estas informações na base de dados.

**7.** Feito isto, salve as configurações e acesse a tela [Administração do Servidor](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833) dentro do sistema, efetue o preenchimento das informações de ID do aplicativo, senha gerada e URL de Redirecionamento, no espaço referente ao Office365.

![Imagem 10: 7. Feito isto, salve as configurações e acesse a tela Administração do Servidor dentro do sistema, efetue o…](https://ajuda.sankhya.com.br/hc/article_attachments/1500003034681)

Após isto, clique em **"Salvar"**.
