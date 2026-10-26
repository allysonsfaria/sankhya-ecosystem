---
id: "17010449985175"
titulo: "Autenticação via IDP"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/17010449985175-Autentica%C3%A7%C3%A3o-via-IDP"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:41:07Z"
rotulos: ["Configuração", "Segurança", "Sankhya ID", "IDP", "Provedor de Identidade", "Autenticação via IDP", "Configuração de Autenticação via IDP para SSO", "SAML", "SSO"]
---

# Autenticação via IDP

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42310486729239) Versão disponível: a partir da 4.21
```

---

A SSO (Single Sign-On) é uma funcionalidade que o permitirá acessar vários sistemas ou aplicativos com um único login. Desse modo, irá possuir uma experiência simplificada, o que permite que o sistema **Sankhya Om** seja acessado com suas credenciais de identificação da aplicação SSO escolhida.

Existem dois tipos de aplicações, a IDP (Provedor de Identidade) que é um sistema que cria, armazena e gerencia identidades digitais, como, por exemplo, Microsoft Azure, OKTA, JumpCloud e OneLogin; e o SP (Provedor de Serviços), que é a aplicação na qual se deseja fazer o login a partir da autorização de um IDP, que nesse caso, é representado pelo nosso sistema.

Sendo assim, abordaremos nesse artigo a configuração necessária para integrar o sistema com um SSO terceiro. Tal configuração consiste na geração e carregamento de dois arquivos com informações de ambiente.

![Imagem 2: O padrão suportado pelo Sankhya Om para esse tipo de conexão é o SAML2.0.](https://ajuda.sankhya.com.br/hc/article_attachments/17010480989719) O padrão suportado pelo **Sankhya Om** para esse tipo de conexão é o SAML2.0.

| **Gerações e Configurações para a autenticação** | |
| --- | --- |
| [Geração do arquivo IDP](https://ajuda.sankhya.com.br/hc/pt-br/articles/17010449985175-Autentica%C3%A7%C3%A3o-via-IDP#Gera%C3%A7%C3%A3odoarquivoIDP) | [Geração do arquivo SP](https://ajuda.sankhya.com.br/hc/pt-br/articles/17010449985175-Autentica%C3%A7%C3%A3o-via-IDP#Gera%C3%A7%C3%A3odoarquivoSP) |
| [Configuração no Sankhya Om](https://ajuda.sankhya.com.br/hc/pt-br/articles/17010449985175-Autentica%C3%A7%C3%A3o-via-IDP#Configura%C3%A7%C3%A3onoSankhyaOm) |  |

---

## Geração do arquivo IDP

O primeiro arquivo de configuração (metadado) a ser gerado é o IDP metadado e, este deve ser gerado pela aplicação utilizada para autenticação (Azure, OKTA, entre outros) após sua preparação para ser utilizado como Single Sign-On. 

Ao efetuar a configuração, deve-se realizar o download do arquivo de configuração IDP disponibilizado pela aplicação e, em seguida, nomear o documento como **"IDP\_metadados.xml"** e armazená-lo em uma pasta ou local de fácil acesso em sua máquina.

Conforme o padrão SAML, a aplicação IDP utilizada precisará de determinadas preferências do **Sankhya Om**, sendo elas:

- **EntityID:** nome do servidor da aplicação. Exemplo: SankhyaOmProdução;
- **Single Sign-On Service Endpoint:** URL externa de acesso ao **Sankhya Om** + /mge/sso. Exemplo: [https://skwinovacao.sankhya.com.br/mge/sso;](https://skwinovacao.sankhya.com.br/mge/sso)
- **Assertion Consumer Service URL:** URL externa de acesso ao **Sankhya Om** + /mge/acs. Exemplo: <https://skwinovacao.sankhya.com.br/mge/acs>.

Além disso, o atributo utilizado pelo sistema para identificação do usuário é o emailAddress e deve ser encaminhado com o nome igual à **"EmailAddress"**.

Caso a aplicação não possua recurso que permita realizar o download das configurações (metadados), o mesmo poderá ser gerado a partir de outra ferramenta, como, por exemplo, a [SAMLTool](https://www.samltool.com/idp_metadata.php).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/17010449985175-Autentica%C3%A7%C3%A3o-via-IDP#top)

## Geração do arquivo SP

O segundo arquivo de configuração (metadado) a ser gerado é o SP metadado, e este deve seguir o padrão SAML.

![Imagem 3: Para facilitar essa tarefa, sugerimos a utilização da ferramenta Sam Developer Tools .](https://ajuda.sankhya.com.br/hc/article_attachments/17010466329751) Para facilitar essa tarefa, sugerimos a utilização da ferramenta [Sam Developer Tools](https://www.samltool.com/sp_metadata.php).

Na ferramenta, clique na opção **"SP"** do menu **"BUILD METADATA"** para que a ferramenta apresente o menu **"Build SP Metadata"**:

![Imagem 4: Na ferramenta, clique na opção "SP" do menu "BUILD METADATA" para que a ferramenta apresente o menu "Build SP Metadata"…](https://ajuda.sankhya.com.br/hc/article_attachments/19840413585943)

Em seguida, preencha os campos da seguinte maneira:

O nome da aplicação configurada deve ser informado no campo **"EntityID"**, como, por exemplo, skwinovacao.

Em **"Attribute Consume Service Endpoint (HTTP-POST)"**, deve ser configurada com a URL externa de acesso ao **Sankhya Om** + /mge/acs, como <https://snkinovacao.sankhya.com.br/mge/acs>.

No campo **"Single logout Service Endpoint (HTTP-REDIRECT)"** insira a URL externa de acesso ao **Sankhya Om** + /mge/sso, por exemplo, <https://snkinovacao.sankhya.com.br/mge/sso>.

![Imagem 5: Lembre-se que as informações dos campos acima devem ser as mesmas realizadas na aplicação IDP.](https://ajuda.sankhya.com.br/hc/article_attachments/17010480989719) Lembre-se que as informações dos campos acima devem ser as mesmas realizadas na aplicação IDP.

Logo depois, no campo **"Nameid Format"** informe a opção **"urn:oasis:names:tc:SAML:1:nameid-format:unspecified"**.

Por fim, ao pressionar o botão ![Imagem 6: Por fim, ao pressionar o botão "BUILD SP METADATA" salve ele com o nome "SP_metadados.xml" e armazene-o em um local na…](https://ajuda.sankhya.com.br/hc/article_attachments/19840189282199) **"BUILD SP METADATA"** salve ele com o nome **"SP\_metadados.xml"** e armazene-o em um local na sua máquina de fácil acesso para utilizá-lo posteriormente.

Em **"AuthnRequestsSigned"**, deve-se definir a opção **"False"** e no campo **"WantAssertionsSigned"**, a opção **"True"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/17010449985175-Autentica%C3%A7%C3%A3o-via-IDP#top)

## Configuração no Sankhya Om

Para iniciar a configuração, primeiramente, inicie a aplicação com usuário SUP e acesse a tela [Repositório de Arquivos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596594).

Na aba **"Sistemas"**, por meio do botão ![Imagem 7: Na aba "Sistemas" , por meio do botão "Criar nova pasta" , realize a criação da pasta com o nome "sso" :](https://ajuda.sankhya.com.br/hc/article_attachments/17010495328407) **"Criar nova pasta"**, realize a criação da pasta com o nome **"sso"**:

![Imagem 8: Na aba "Sistemas" , por meio do botão "Criar nova pasta" , realize a criação da pasta com o nome "sso" :](https://ajuda.sankhya.com.br/hc/article_attachments/19840208642711)

Então, na pasta recém gerada, sso, adicione por meio do botão ![Imagem 9: Então, na pasta recém gerada, sso , adicione por meio do botão "Adicionar Arquivo" os dois metadados gerados…](https://ajuda.sankhya.com.br/hc/article_attachments/17023668654231) **"Adicionar Arquivo"** os dois metadados gerados anteriormente, sendo eles o SP-metadados, gerado na ferramenta SAMLTOOL, e o IDP\_metadados, gerados na aplicação.

![Imagem 10: Então, na pasta recém gerada, sso , adicione por meio do botão "Adicionar Arquivo" os dois metadados gerados…](https://ajuda.sankhya.com.br/hc/article_attachments/17023668654871)

Dessa forma, os arquivos serão salvos na tela Repositório de Arquivos:

![Imagem 11: Dessa forma, os arquivos serão salvos na tela Repositório de Arquivos :](https://ajuda.sankhya.com.br/hc/article_attachments/19840189306647)

Para que o login na Plataforma **Sankhya Om** seja bem-sucedido, o e-mail cadastro no usuário da Aplicação IDP (Azure, Okta, entre outros) deve ser o mesmo presente no usuário do **Sankhya Om**:

![Imagem 12: Para que o login na Plataforma Sankhya Om seja bem-sucedido, o e-mail cadastro no usuário da Aplicação IDP (Azure,…](https://ajuda.sankhya.com.br/hc/article_attachments/19840189315479)

**Observação:** para o uso do SSO deve existir apenas um usuário com o mesmo email.

**Nota:** a definição do usuário a ser utilizado deve ser realizada na tela [Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874).

Então, após as configurações serem realizadas, acesse a plataforma a partir da URL de login acrescida de **"/sso"**, como, por exemplo, <https://nomedaaplicacao.com.br/mge/sso,> e assim, haverá o redirecionamento para efetuar o login no **Sankhya Om** utilizando a ferramento de SSO:

![Imagem 13: Então, após as configurações serem realizadas, acesse a plataforma a partir da URL de login acrescida de "/sso" , como,…](https://ajuda.sankhya.com.br/hc/article_attachments/19840208674583)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/17010449985175-Autentica%C3%A7%C3%A3o-via-IDP#top)
