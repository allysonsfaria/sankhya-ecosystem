---
id: "32985191226647"
titulo: "Como realizar login exclusivo com SSO (SAML)?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32985191226647-Como-realizar-login-exclusivo-com-SSO-SAML"
trilha: "Manual do Produto > Plataforma e Integrações > Plataforma"
atualizado_em: "2026-07-29T16:13:49Z"
rotulos: ["Configuração", "Segurança", "Autenticação", "Preferências", "Sankhya ID", "SAML", "SSO", "USUÁRIO SUP", "LOGIN EXCLUSIVO", "SSOLOGINONLY"]
---

# Como realizar login exclusivo com SSO (SAML)?

| **Versão miníma:** a partir da 4.35b30  **Telas:**   1. Preferências (Configurações > Avançado> Preferências) 2. Usuários (Configurações > Controle de Acesso> Usuários) |
| --- |

---

### Sumário

| [Descrição](https://ajuda.sankhya.com.br/hc/pt-br/articles/32985191226647-Como-realizar-login-exclusivo-com-SSO-SAML#h_01JYE651PZFMN7FBXM2Z7TJAWJ) |
| --- |
| [Pré-requisitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/32985191226647-Como-realizar-login-exclusivo-com-SSO-SAML#h_01JYE5H0Z3HY4W3EQVDSWZRZBF) |
| [Jornada de uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/32985191226647-Como-realizar-login-exclusivo-com-SSO-SAML#h_01JYE68T29S0B4V47BNQ6MMSQJ) |
| [Pontos de atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/32985191226647-Como-realizar-login-exclusivo-com-SSO-SAML#h_01JYE5H0ZHY3BF0TBHBWN5VDGH) |

---

### Descrição

O login exclusivo com SSO (SAML) pode ser usado para deixar o acesso ao **Sankhya OM** mais seguro. Com ele, **você acessa o sistema apenas com a conta de usuário que sua empresa já usa em outros programas**, sem precisar da tela de login comum do **Sankhya OM**.

A única exceção é **o usuário SUP**, que continuará acessando o sistema pela tela de login tradicional.

### Pré-requisitos

#### **(1)** Como ativar o login exclusivo?

Para ativar esta opção, você precisa utilizar da [Autenticação via IDP](https://ajuda.sankhya.com.br/hc/pt-br/articles/17010449985175-Autentica%C3%A7%C3%A3o-via-IDP), após isso, siga estes passos:

1. Acesse a tela [**Preferências**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias).
2. Ative o parâmetro **SSOLOGINONLY**.

![Imagem 1: Ative o parâmetro SSOLOGINONLY .](https://ajuda.sankhya.com.br/hc/article_attachments/32985191226007)

#### **(1)** Atenção à ativação do login exclusivo

Antes de ativar esta função, é importante garantir que o campo **"Email"** esteja preenchido no cadastro de **todos os seus** [**usuários**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios), com exceção do usuário **SUP**. Embora o sistema não exija o email do SUP no momento da ativação, é importante destacar que, em atualizações posteriores feitas na tela de [Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios), o preenchimento do e-mail para o SUP pode ser obrigatório.

O email deve ser o mesmo que eles usam para acessar outros sistemas da sua empresa. Assim, o login funcionará corretamente.

### Jornada de uso

#### **(1)** Como preencher o campo Email no cadastro de usuários?

Para preencher o email, siga estes passos:

1. Acesse a tela de **Usuários**.
2. Vá até a aba [**Identificação**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abaidentificao).
3. Preencha o campo **Email**.

Com o login exclusivo ativado, o campo **Email** no cadastro de usuários se torna **obrigatório**. Você vai precisar preenchê-lo sempre que cadastrar ou atualizar um usuário.

#### **(1)** Como acessar o sistema?

Quando o **login exclusivo** está ativado, seu jeito de entrar no **Sankhya OM** muda um pouco, mas fica ainda mais fácil e seguro:

1. Abra o **Sankhya OM**: você verá uma nova tela de login com um botão chamado **"Login com SSO"**.

![Imagem 2: Abra o Sankhya OM : você verá uma nova tela de login com um botão chamado "Login com SSO" .](https://ajuda.sankhya.com.br/hc/article_attachments/32985191226263)

2. **Clique em "Login com SSO"**: ao fazer isso, o sistema vai te redirecionar para a página de login da sua empresa – o mesmo lugar onde você já acessa outros sistemas internos, como seu email corporativo ou outras ferramentas. Essa página é o que chamamos de **Provedor de Identidade (IdP)**.
3. **Faça seu login (se necessário)**: se você já estiver logado na rede ou em algum sistema da sua empresa, é provável que nem precise digitar sua senha novamente. Caso contrário, insira suas credenciais habituais.
4. **Retorno ao Sankhya OM**: assim que seu login for confirmado pelo sistema da sua empresa, você será automaticamente direcionado de volta para o **Sankhya OM**, já logado e pronto para trabalhar.

### Pontos de atenção

#### **(1)** Acesso para administradores

![Imagem 3: (1) Acesso para administradores](https://ajuda.sankhya.com.br/hc/article_attachments/32985207297303)

Se você é um administrador e precisa acessar o sistema com o **usuário SUP**, o processo é um pouco diferente para garantir a segurança:

- **Acesse a URL de administrador**: você deve usar o seguinte endereço no seu navegador: **/mge/?scope=admin**.
- **Tela de login tradicional**: essa URL abrirá a tela de login padrão do Sankhya OM.
- **Acesso restrito ao SUP**: por segurança, apenas o **usuário SUP** conseguirá fazer login por essa tela. Isso garante que a administração do sistema mantenha um ponto de acesso separado e controlado.
