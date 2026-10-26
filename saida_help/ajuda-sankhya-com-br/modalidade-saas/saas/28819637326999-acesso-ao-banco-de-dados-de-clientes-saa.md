---
id: "28819637326999"
titulo: "Acesso ao Banco de Dados de Clientes SaaS por Colaboradores Sankhya via VPN"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/28819637326999-Acesso-ao-Banco-de-Dados-de-Clientes-SaaS-por-Colaboradores-Sankhya-via-VPN"
trilha: "Modalidade SaaS > SaaS"
atualizado_em: "2026-10-02T14:34:59Z"
rotulos: ["Configuração", "Segurança", "Banco de Dados", "Saas", "VPN"]
---

# Acesso ao Banco de Dados de Clientes SaaS por Colaboradores Sankhya via VPN

###

### Atenção!

A partir do dia **31 de dezembro de 2024,** estará disponível o acesso ao banco de dados dos clientes SaaS através de VPN (o antigo acesso para consultores Sankhya via Terminal Service será descontinuado).

Siga os passos abaixo para realizar o acesso.

### Passos

#### 1- Configurar a VPN

(1)** Instale o FortiClient VPN**
Se ainda não tiver o FortiClient VPN instalado, faça o download [aqui.](https://www.fortinet.com/br/support/product-downloads)

(1)** Configure o acesso a VPN**

1. 1. Abra o FortiClient;
   2. Configure uma nova conexão VPN com as seguintes informações:
      - - **Tipo de VPN:** SSL-VPN
        - **Nome da Conexão:** (defina um nome de sua escolha)
        - **Descrição:** (opcional, defina se desejar)
        - **Gateway Remoto:** vpn.sankhya.com.br
        - **Porta Customizada:** 4443
        - **Marcar as opções:**
          - “Ativar logon único Single Sign On (SSO) para túnel VPN”
          - “Use o navegador externo como agente de usuário para autenticação de usuário saml”
   3. Salve as configurações;
   4. Conecte-se à VPN.

[GIF animado: Imagem 1: Conecte-se à VPN.](https://ajuda.sankhya.com.br/hc/article_attachments/28918220452759)

(1)** Configuração do Login do Chrome**

1. Certifique-se de que o login do Chrome esteja ativado em seu navegador.
2. Isso é necessário, pois após a configuração da VPN, o programa direciona você para o login com o Google para acessar a rede corporativa.
3. Confira os passos no gif abaixo:

![Imagem 2: Confira os passos no gif abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/28918250325143)

####

#### 2- Acessando o Vault externo

- Entre no Vault pelo link:
  <https://vault-external.sankhyacloud.com.br/ui/vault/dashboard>
- Na opção **Method** seleciona OIDC, e lá em baixo Faça login usando seu e-mail corporativo e senha.![Imagem 3: Na opção Method seleciona OIDC, e lá em baixo Faça login usando seu e-mail corporativo e senha.](https://ajuda.sankhya.com.br/hc/article_attachments/34132979928855)

#### 4- Dentro do Vault

### Acesse a seção Secrets Engines

- No painel principal do Vault, clique em **Secrets Engines**.
- Você verá seu nome.![Imagem 4: Você verá seu nome.](https://ajuda.sankhya.com.br/hc/article_attachments/34132959033111)

### Escolha o cliente desejado

- Ao clicar nele você verá a lista de clientes a qual voce tem acesso ao banco de dados.
- Clique no nome do cliente que você deseja acessar. ![Imagem 5: Clique no nome do cliente que você deseja acessar.](https://ajuda.sankhya.com.br/hc/article_attachments/34132959036055)

#### .

**PRD = Ambiente de Produção
TST = Ambiente de Teste**

- **Dentro do ambiente escolhido (PRD ou TST), clique em secret.**

![Imagem 6: Dentro do ambiente escolhido (PRD ou TST), clique em secret.](https://ajuda.sankhya.com.br/hc/article_attachments/34132979938327)

- Lá estarão as credenciais (usuário, senha, etc.) necessárias para acesso ao banco.![Imagem 7: Lá estarão as credenciais (usuário, senha, etc.) necessárias para acesso ao banco.](https://ajuda.sankhya.com.br/hc/article_attachments/34132979940119)

#### Copie as informações e use conforme necessário para conexão. com o primeiro botão copy você consegue copiar de forma mais prática

![Imagem 8: Copie as informações e use conforme necessário para conexão. com o primeiro botão copy você consegue copiar de forma…](https://ajuda.sankhya.com.br/hc/article_attachments/34132959041175)

####

#### 5- Criando a conexão e acessando o BD

Com a VPN conectada, configure a conexão no banco de dados com as credenciais de acesso:

**Observação:** o acesso ao banco de dados estará disponível enquanto a VPN estiver conectada.

![Imagem 9: Observação: o acesso ao banco de dados estará disponível enquanto a VPN estiver conectada.](https://ajuda.sankhya.com.br/hc/article_attachments/28819680659863)

#### 6- Resolução de Problemas - Certificado

#### **(1)** Verificar o Erro no FortClient VPN

No FortClient VPN acesse a opção de notificações localizada no canto superior direito e verifique se há mensagens de erro relacionadas a certificados. Anote qualquer mensagem de erro ou código fornecido.

![Imagem 10: No FortClient VPN acesse a opção de notificações localizada no canto superior direito e verifique se há mensagens de…](https://ajuda.sankhya.com.br/hc/article_attachments/28918250327063)

#### **(1)** Identificar o Certificado

Se o erro estiver relacionado a certificados, anote o nome do certificado mencionado na mensagem de erro. Acompanhe as imagens abaixo para conseguir realizar o processo.

![Imagem 11: Se o erro estiver relacionado a certificados, anote o nome do certificado mencionado na mensagem de erro. Acompanhe as…](https://ajuda.sankhya.com.br/hc/article_attachments/28918220456215)

![Imagem 12: Se o erro estiver relacionado a certificados, anote o nome do certificado mencionado na mensagem de erro. Acompanhe as…](https://ajuda.sankhya.com.br/hc/article_attachments/28918220456855)

#### **(1)** Abrir o Gerenciador de Certificados do Usuário

1. No Windows, pressione as teclas "Win + R" para abrir a janela "Executar".
2. Digite "certmgr.msc" e pressione Enter para abrir o Gerenciador de Certificados do Usuário.

#### **(1)** Localizar e Exportar o Certificado

1. No Gerenciador de Certificados, navegue até a categoria "Pessoal" > "Certificados".
2. Localize o certificado mencionado em **Identificar o Certificado**.
3. Clique com o botão direito do mouse sobre o certificado e selecione "Todas as tarefas" > "Exportar".
4. Siga as instruções do assistente de exportação para exportar o certificado. Selecione a opção "Não, não exportar a chave privada" quando solicitado.

![Imagem 13: Siga as instruções do assistente de exportação para exportar o certificado. Selecione a opção "Não, não exportar a…](https://ajuda.sankhya.com.br/hc/article_attachments/28918250329623)

#### **(1)** Excluir o Certificado

1. Após exportar o certificado, clique com o botão direito do mouse sobre ele novamente e selecione "Excluir".
2. Confirme a exclusão do certificado.

![Imagem 14: Confirme a exclusão do certificado.](https://ajuda.sankhya.com.br/hc/article_attachments/28918250330519)

#### **(1)** Reiniciar a máquina e Conectar Novamente

1. Após excluir o certificado, feche o Gerenciador de Certificados e reinicie a máquina.
2. Tente se conectar novamente à VPN e verifique se o problema foi resolvido.
