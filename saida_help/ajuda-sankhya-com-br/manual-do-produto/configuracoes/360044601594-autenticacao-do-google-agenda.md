---
id: "360044601594"
titulo: "Autenticação do Google Agenda"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601594-Autentica%C3%A7%C3%A3o-do-Google-Agenda"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:51:43Z"
rotulos: ["manual", "Configuração", "Integração", "Administração", "Autenticação", "Agenda", "Google", "br.com.sankhya.core.cfg.administracaoservidorgoogle", "Autenticação do Google Agenda manual", "Configuração da Autenticação do Google Agenda", "API", "Google Agenda"]
---

# Autenticação do Google Agenda

Trataremos neste artigo, sobre as etapas necessárias para à Autenticação do Google Agenda.

**Importante:** os processos especificados nesse artigo podem não ser exatos devido às constantes alterações nos processos do Google.

**1.** Crie uma conta no console do Google que irá vincular a aplicação que se está usando (no caso, o Sankhya-Om ou Jiva) com algum recurso do Google (no caso, o Google Calendar). Isto é necessário, pois é dessa maneira que o Google identifica quem está acessando e solicita a autorização para utilizar a conta por aplicativos de terceiros. Para realizar esta etapa, acesse o link: <https://console.developers.google.com/iam-admin/projects>

**2.** Após o login, será apresentado a tela abaixo:

![clip4835](https://ajuda.sankhya.com.br/hc/article_attachments/360061920553)

**3.** Clique na opção **"Criar Projeto"**. Assim, será exibido um pop-up solicitando o nome para este novo aplicativo. Informe o nome do sistema (Sankhya-Om ou Jiva). Esta criação pode levar alguns segundos:

![Imagem 2: 3. Clique na opção "Criar Projeto" . Assim, será exibido um pop-up solicitando o nome para este novo aplicativo.…](https://ajuda.sankhya.com.br/hc/article_attachments/360101862234)

**4.** Após isto, será apresentada uma tela com uma série de opções de aplicativos do Google. Clique em **"Calendar API"** em API  do Google Apps:

![clip4839](https://ajuda.sankhya.com.br/hc/article_attachments/360060996374)

**5.** Na tela de **"Gerenciador de API"** do Google Calendar, clique em **"Ativar"**:

![Imagem 4: 5. Na tela de "Gerenciador de API" do Google Calendar, clique em "Ativar" :](https://ajuda.sankhya.com.br/hc/article_attachments/1500003030721)

**6.** Feito isto, será exibida a mensagem que a API está ativada, porém não pode-se usá-la sem credenciais no projeto:

![clip4845](https://ajuda.sankhya.com.br/hc/article_attachments/360060996414)

**7.** No menu a esquerda, temos a opção **"Credenciais"**:

![Imagem 6: 7. No menu a esquerda, temos a opção "Credenciais" :](https://ajuda.sankhya.com.br/hc/article_attachments/1500003030561)

**8.** Nesta tela de Credenciais o primeiro passo é configurar o nome do produto na aba **"Tela de Consentimento OAuth"**. Insira o nome do sistema (Sankhya-Om ou Jiva):

![clip4851](https://ajuda.sankhya.com.br/hc/article_attachments/360061920613)

**9.** De volta à aba **"Credenciais"** deve-se **"Criar credenciais"**:

![clip4854](https://ajuda.sankhya.com.br/hc/article_attachments/360061920633)

**10.** Será apresentado um popup solicitando a escolha de um tipo de autenticação. Selecione a opção **"ID do Cliente OAuth"**:

![clip4859](https://ajuda.sankhya.com.br/hc/article_attachments/360061920653)

**11.** Na próxima tela, indique o tipo de aplicativo que se está cadastrando. Neste caso, trata-se de um **"Aplicativo Web"**:

![clip4860](https://ajuda.sankhya.com.br/hc/article_attachments/360061920673)

**12.** Ao selecionar a opção Aplicativo Web, serão apresentadas algumas configurações adicionais. O primeiro é o nome que será dado ao aplicativo com que o Google Agenda se comunica. Novamente, insira o nome do sistema (Sankhya-Om ou Jiva). Além disso, configure uma origem autorizada e uma URL de redirecionamento:

![Imagem 11: 12. Ao selecionar a opção Aplicativo Web , serão apresentadas algumas configurações adicionais. O primeiro é o nome que…](https://ajuda.sankhya.com.br/hc/article_attachments/360104028953)

#### O que é uma URL de Redirecionamento?

Ao finalizar o processo de autorização, a "Microsoft/ Google" precisa retornar as informações de acesso para o sistema para que seja possível a sincronização dos eventos em sua agenda. Deste modo, é necessário cadastrar um endereço validado na internet, isto é, que o sistema consiga ser acessado externamente. Um detalhe importante é que este endereço deve ser HTTPS, pois o redirecionamento só é permitido por meio de uma conexão segura.

Exemplo de URL de redirecionamento:

<https://www.SEUDOMINIO.com.br/mge/oAuth.mge>

**Nota:** o endereço correto sempre deverá terminar com **"/mge/oAuth.mge"**, que se trata da página dentro do sistema que espera receber os dados de acesso da agenda e salvar estas informações na base de dados.

**13.** Após concluir a criação, será apresentado um pop-up com as informações **"ID do Cliente"** e **"Chave Secreta"**. Anote e salve com cuidado estas informações, pois são elas as responsáveis por todo o processo de autorização na sincronização das agendas do Google com o sistema.

![clip4866](https://ajuda.sankhya.com.br/hc/article_attachments/360061920713)

**14.** Com as informações **"ID do Cliente"**, **"Chave Secreta"** e **"URL de Redirecionamento"** acesse a tela [Administração do Servidor](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833) no sistema e configure na aba [Autorização de Acesso](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833#abaautoriza%C3%A7%C3%A3odeacesso), estes dados referentes ao Google Agenda:

![Imagem 13: 14. Com as informações "ID do Cliente" , "Chave Secreta" e "URL de Redirecionamento" acesse a tela Administração do…](https://ajuda.sankhya.com.br/hc/article_attachments/360104028693)

Após isto, clique em **"Salvar"**.
