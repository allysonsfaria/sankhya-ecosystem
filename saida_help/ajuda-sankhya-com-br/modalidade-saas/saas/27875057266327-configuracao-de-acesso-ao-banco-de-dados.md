---
id: "27875057266327"
titulo: "Configuração de acesso ao Banco de Dados para clientes SaaS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/27875057266327-Configura%C3%A7%C3%A3o-de-acesso-ao-Banco-de-Dados-para-clientes-SaaS"
trilha: "Modalidade SaaS > SaaS"
atualizado_em: "2026-09-29T13:12:30Z"
rotulos: ["Configuração", "Segurança", "Parceiro", "Banco de Dados para clientes SaaS", "FortiClient VPN", "Banco de Dados", "Saas", "VPN"]
---

# Configuração de acesso ao Banco de Dados para clientes SaaS

### 1. Configurar a VPN

#### Instale o FortiClient VPN

Se ainda não tiver o FortiClient VPN instalado, faça o download [aqui](https://www.fortinet.com/br/support/product-downloads).

#### Token de Acesso à VPN

Para autenticação, utilize o usuário e senha enviadas no email:

![Imagem 1: Abra o FortiClient;](https://ajuda.sankhya.com.br/hc/article_attachments/27875057242775) Abra o FortiClient;

![Imagem 2: Configure uma nova conexão VPN com as seguintes informações:](https://ajuda.sankhya.com.br/hc/article_attachments/27875057246871) Configure uma nova conexão VPN com as seguintes informações:

- **Tipo de VPN:** SSL-VPN
- **Nome da Conexão:** defina um nome de sua escolha
- **Descrição:** opcional, defina se desejar
- **Gateway Remoto:** vpn-cloud.sankhyacloud.com.br
- **Porta Customizada:** 10443
- **Salvar Login:** Marque esta opção
- **Usuário:** Insira seu e-mail (somente a parte antes do @)

![Imagem 3: Salve as configurações;](https://ajuda.sankhya.com.br/hc/article_attachments/27875050336279) Salve as configurações;

![Imagem 4: Insira a senha (Utilize o token enviado);](https://ajuda.sankhya.com.br/hc/article_attachments/27875050339607) Insira a senha (Utilize o token enviado);

![Imagem 5: No primeiro acesso, você receberá um token para autenticação de dois fatores;](https://ajuda.sankhya.com.br/hc/article_attachments/27875057256599) No primeiro acesso, você receberá um token para autenticação de dois fatores;

![Imagem 6: Conecte-se à VPN.](https://ajuda.sankhya.com.br/hc/article_attachments/27875057258263) Conecte-se à VPN.

![Imagem 7: Conecte-se à VPN.](https://ajuda.sankhya.com.br/hc/article_attachments/27875050344087)

![Imagem 8: Conecte-se à VPN.](https://ajuda.sankhya.com.br/hc/article_attachments/27875050346519)

### 2. Acesse o cofre de senha (Vault) e obtenha as credenciais:

[GIF animado: Imagem 9: 2. Acesse o cofre de senha (Vault) e obtenha as credenciais:](https://ajuda.sankhya.com.br/hc/article_attachments/27881648296855)

#### Com a VPN conectada:

![Imagem 10: Entre no Vault, selecione o Method: Username - utilizando as credenciais recebidas: seu e-mail e a senha fornecida no…](https://ajuda.sankhya.com.br/hc/article_attachments/27875057242775) Entre no Vault, selecione o Method: Username - utilizando as credenciais recebidas: seu e-mail e a senha fornecida no email: <https://vault-external.sankhyacloud.com.br/>

![Imagem 11: Selecione a opção Method: Username](https://ajuda.sankhya.com.br/hc/article_attachments/27875057246871) Selecione a opção Method: Username

![Imagem 12: Navegue até o caminho: Nome do parceiro > prd (produção) ou tst (teste) > Profile > Basic, Professional ou Enterprise >…](https://ajuda.sankhya.com.br/hc/article_attachments/27875050336279) Navegue até o caminho: Nome do parceiro > prd (produção) ou tst (teste) > Profile > Basic, Professional ou Enterprise > Secret, para obter as credenciais de acesso.

- <https://vault-external.sankhyacloud.com.br>
- Selecione a opção Method: Username
- Informe o username e senha que foram enviados no email
- Selecionar nome do parceiro
- Selecione Prd (Produção) ou Tst (Teste)
- Clique em Profile
- Selecionar : Basic, Enterprise ou Professional de acordo com a modalidade contratada.
- Clicar em Secret
- Serão exibidas as credenciais

Essas são as informações necessárias para criar a conexão no banco de dados:

- hostname
- password
- port
- servicename
- username

![Imagem 13: username](https://ajuda.sankhya.com.br/hc/article_attachments/27876929587479)

### 3. Criando a conexão e acessando o BD

Com a VPN conectada, configure a conexão no banco de dados, com as credenciais de acesso:

![Imagem 14: Com a VPN conectada, configure a conexão no banco de dados, com as credenciais de acesso:](https://ajuda.sankhya.com.br/hc/article_attachments/27876929590295)
