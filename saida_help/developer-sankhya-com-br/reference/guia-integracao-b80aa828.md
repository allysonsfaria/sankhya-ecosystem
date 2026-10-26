---
id: "https://developer.sankhya.com.br/reference/guia-integracao"
titulo: "Guia de Integração com o Sankhya Om"
url: "https://developer.sankhya.com.br/reference/guia-integracao"
atualizado_em: "2025-11-10T23:38:53.000Z"
---

# Guia de Integração com o Sankhya Om

Este guia orienta **clientes Sankhya** e **parceiros desenvolvedores** sobre o processo completo de **criação, configuração e autenticação** de integrações com o Sankhya Om, utilizando o **[novo fluxo de autenticação](https://developer.sankhya.com.br/reference/post_authenticate)**.

O processo cobre:

* Acesso inicial ao **Portal do Desenvolvedor**;
* Convite e **gestão de usuários e grupos**;
* Criação de **Soluções** e **Componentes de Integração**;
* Geração de **Client ID, Client Secret e X-Token**;
* Compartilhamento seguro entre cliente e parceiro.

## Stakeholders

|                Papel               |                                 Descrição                                 |                                                                             Responsabilidades                                                                             |
| :--------------------------------: | :-----------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|         **Cliente Sankhya**        |     Empresa usuária do ERP que deseja integrar uma aplicação externa.     | Configurar o Portal do Desenvolvedor, criar a solução, criar o componente de integração com o client\_id e client\_secret, e gerar o token de autenticação no Sankhya Om. |
| **Parceiro Externo Desenvolvedor** | Parceiro externo e responsável técnico pela aplicação que será integrada. |                                 Acessar o Portal do Desenvolvedor, implementar a integração usando as credenciais fornecidas pelo cliente.                                |

<br />

### **🔁 Fluxo Resumido**

1. Cliente acessa o Portal do Desenvolvedor.
2. Convida o parceiro como usuário Desenvolvedor Externo.
3. Cria grupo de acesso e associa o usuário do parceiro.
4. Cria solução, associada ao grupo que o parceiro faz parte, e cria um componente de integração.
5. O componente de integração apresenta **Client ID** e **Client Secret**.
6. Cliente cadastra a integração no Sankhya Om via Configurações Gateway e gera o **Token**.
7. Cliente compartilha o token com o parceiro.
8. Parceiro autentica chamadas com **Client ID + Client Secret + Token (X-Token)**. Para mais detalhes sobre o fluxo de autenticação, veja a documentação dedicada aqui <https://developer.sankhya.com.br/reference/post_authenticate>

## Etapa 1 — Primeiro Acesso ao Portal do Desenvolvedor

1. O cliente acessa o **Portal do Desenvolvedor**: <https://areadev.sankhya.com.br/>
2. Caso nenhum usuário do cliente tenha o acesso ainda, o acesso deverá ser concedido via **Sankhya ID (Account)**.
   1. Para concessão de acesso via Sankhya ID, veja a documentação dedicada: <https://developer.sankhya.com.br/reference/concedendo-acesso-a-colaboradores>

### **Tipos de Acesso ao Portal**

* **Como Administrador do Portal:**\
  O usuário entra no Portal e pode **convidar outros usuários** (internos ou externos). Isso é feito via menu dedicado chamado **Gestão de Acessos.** Saiba mais em: <https://developer.sankhya.com.br/docs/portal-do-desenvolvedor>
* **Como Desenvolvedor Interno:**\
  Um administrador concede acesso ao Portal. Saiba mais aqui: <https://developer.sankhya.com.br/docs/portal-do-desenvolvedor>

💡 **Dica:** mantenha pelo menos um usuário com papel de *Administrador* do seu Portal do Desenvolvedor para gerenciar convites e permissões diretamente no Portal.

## Etapa 2 — Convite do Desenvolvedor Externo no Portal do Desenvolvedor (Gestão de Acessos > Usuários)

Antes de criar grupos, o cliente precisa **convidar o parceiro desenvolvedor** como **usuário** do seu Portal do Desenvolvedor. Para isso, o usuário do lado do cliente precisa estar logado como Administrador do Portal do Desenvolvedor da sua empresa.

1. Acesse o menu **Gestão de Acessos → Usuários**.
2. Clique em **Convidar usuário**.
3. Informe o e-mail do parceiro desenvolvedor.
4. Escolha a atribuição **Desenvolvedor Externo.**

💬 **Importante:** somente **usuários já convidados (convite com status** Enviad&#x6F;**) ou ativos** podem ser associados a grupos posteriormente.

### Caso o parceiro ainda não tenha acesso ao Portal:

* Ele deve se **cadastrar no Programa Sankhya Developer** (com o CNPJ dele) aqui: <https://www.sankhya.com.br/developers/>
* Após aprovação do cadastro, ele terá acesso ao seu próprio portal e poderá **ver o convite** feito pelo cliente.

## Etapa 3 — Criação do Grupo de Acesso (Gestão de Acessos > Grupos)

Depois de convidar o usuário:

1. Vá até **Gestão de Acessos → Grupos**.
2. Clique em **Criar grupo**.
3. Dê um nome descritivo — por exemplo, Parceiros Externos.
4. Defina as permissões do grupo:
   * Inicialmente, o cliente pode criar um grupo **sem permissões** ou apenas **visualização padrão**.
5. Associe o usuário convidado (desenvolvedor externo) ao grupo.

⚙️ **Observação:**\
O vínculo entre grupo e usuário é **independente**.\
O convite do usuário deve existir antes de associá-lo ao grupo.

💡 **Boas práticas:**

* Crie grupos separados para **usuários internos** e **parceiros externos**.
* Use nomes claros e consistentes para facilitar o controle de acessos.

## Etapa 4 — Criação da Solução e do Componente de Integração pelo Cliente

### **4.1. Criar a Solução**

1. Acesse o menu **Minhas soluções** dentro do Portal do Desenvolvedor.
2. Clique em **Criar nova solução**.
3. Selecione Solução privada, apenas para uso interno da empresa
4. Associe a solução ao grupo criado (Parceiros Externos).

⚠️ **Obrigatório:**\
Toda solução precisa estar vinculada a um grupo de acesso.\
Sem esse vínculo, não é possível criar a solução.

### **4.2. Criar o Componente de Integração**

1. Dentro da Solução, clique em **Adicionar componente.**
2. **Selecione Tipo: Integrações.**
3. Dê um **nome definitivo** ao componente.
   * Esse nome **não poderá ser alterado posteriormente** (bloqueio temporário).

💡 **Por que o nome é importante?**\
O **nome do componente** será usado no ERP Sankhya, na tela *Configurações Gateway*, para cadastrar a integração e gerar os tokens (teste e produção).\
Escolha um nome descritivo, como:\
Integração \[XPTO] - Nome do Cliente - Nome do Parceiro.

### **4.3. Geração Automática de Credenciais**

Ao criar o componente, o sistema gera automaticamente:

* **Client ID (para ambiente de produção)**
* **Client Secret (para ambiente de produção)**
* **Client ID Sandbox (para ambiente de teste)**
* **Client Secret Sandbox (para ambiente de teste)**

Essas chaves ficam disponíveis para:

* O **cliente Sankhya**, dentro da Solução;
* O **parceiro desenvolvedor**, dentro do portal dele, via Compartilhadas comigo > Solução \[nome da solução criada pelo cliente] > Componente \[título do componente de integração].

### **4.4. Acesso do Parceiro Desenvolvedor**

O parceiro poderá acessar as chaves em:\
**Portal do Desenvolvedor → Compartilhadas comigo**

Lá, ele visualiza:

* **Client ID (para ambiente de produção)**
* **Client Secret (para ambiente de produção)**
* **Client ID Sandbox (para ambiente de teste)**
* **Client Secret Sandbox (para ambiente de teste)**

⚠️ **Observação:** o parceiro ainda não possui o **Token**. Esse dado será gerado pelo cliente no Sankhya Om na tela Configurações Gateway.

## **Etapa 5 — Geração do Token no Sankhya ERP (Sankhya Om)**

O Token é gerado dentro do ERP, pelo **cliente Sankhya**, na tela:

Configurações Gateway → Cadastrar aplicação

### **5.1. Selecione o tipo de ambiente para diferentes tipos de Token**

|       Token       | Tipo de Ambiente selecionado |               Funcionará com              |
| :---------------: | :--------------------------: | :---------------------------------------: |
| **Sandbox/Teste** |             Teste            | Client ID Sandbox e Client Secret Sandbox |
|    **Produção**   |           Produção           |    Client ID e Client Secret (Produção)   |

Cada ambiente gera um **token independente**. Um token de sandbox **não funciona** com chaves client\_id e client\_secret de produção, e vice-versa.

### **5.2. Cadastrar a Integração**

1. Clique em **Cadastrar aplicação**.
2. Busque a integração pelo nome dado ao componente dentro do Portal do Desenvolvedor:
   * **Nome da integração:** deve ser **idêntico** ao nome do componente de integração criado no Portal.
3. Seleciona a integração.
4. Certifique-se que o status está como **Ativado**.
5. Configure o **Usuário de Integração.**
6. Clique em salvar (✓) para **gerar o Token**.

### **5.3. Compartilhamento Seguro**

O **token gerado** fica disponível apenas ao cliente no ERP.\
Para que o parceiro possa autenticar as chamadas, o cliente deve **compartilhar o token de forma segura**.

Para mais detalhes sobre a tela Configurações Gateway, acesse o artigo dedicado: [Central de Ajuda - Configurações Gateway](https://ajuda.sankhya.com.br/hc/pt-br/articles/10007620733463-Configura%C3%A7%C3%B5es-Gateway)

## **Etapa 6 — Uso dos Dados na Integração**

Para autenticar a integração, o parceiro precisa de **três dados**:

|         Dado        |                  Origem                  |     Responsável    |           Função           |
| :-----------------: | :--------------------------------------: | :----------------: | :------------------------: |
|    **Client ID**    |          Portal do Desenvolvedor         | Cliente / Parceiro | Identificação da aplicação |
|  **Client Secret**  |          Portal do Desenvolvedor         | Cliente / Parceiro |   Validação da aplicação   |
| **Token (X-Token)** | ERP Sankhya (tela Configurações Gateway) |       Cliente      |  Autenticação das chamadas |

O parceiro utilizará esses três elementos para autenticar as requisições via API.

# **💬 FAQ — Dúvidas Frequentes**

|                                     Problema                                     |                                                              Possível Causa                                                             |                                                                                                                  Solução Recomendada                                                                                                                  |
| :------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| **401 - Credenciais inválidas (client\_id, client\_secret ou X-Token inválido)** |                                 Token de sandbox usado com Client ID/Secret de produção (ou vice-versa).                                |                                                                                                 Gere um novo token correspondente ao ambiente correto.                                                                                                |
| **401 - Credenciais inválidas (client\_id, client\_secret ou X-Token inválido)** |                                                Dados incorretos ou credenciais trocadas.                                                |                                                                                     Verifique se o client ID, secret e token pertencem à mesma solução e ambiente.                                                                                    |
|             **Parceiro não vê a solução em “Compartilhadas comigo”**             | Associação ao grupo não concluída, grupo ao qual está associado no Portal do Desenvolvedor do cliente não está com a solução vinculada. |                                              Cliente deve verificar se o parceiro foi adicionado ao grupo. Cliente deve verificar se o grupo ao qual o parceiro está associado possui a solução correta.                                              |
|               **Não consigo criar uma solução em Minhas soluções**               |                     Usuário logado não é Administrador do seu Portal e não possui permissão para criar uma solução.                     | Verificar com o Administrador do Portal do Desenvolvedor se o usuário está associado a um grupo com permissão para Criar solução. Se o usuário logado NÃO for um cliente Sankhya e NÃO for um parceiro homologado, não tem acesso para Criar solução. |
|                 **Não consigo concluir a criação de uma solução**                |                                                         Nenhum grupo de acesso.                                                         |                                                                                                     Crie um grupo de acesso via Gestão de Acessos.                                                                                                    |
|                **Não consigo visualizar o menu Gestão de Acessos**               |                                              Usuário logado não é Administrador do Portal.                                              |                                                                                         Peça acesso a um usuário Administrador do seu Portal do Desenvolvedor.                                                                                        |
|             **Não consigo editar o nome do componente de integração**            |                                                      Bloqueio temporário de edição.                                                     |                                                                                                     Em breve retornaremos com essa funcionalidade.                                                                                                    |
|       **Não consigo encontrar a integração na tela Configurações Gateway**       |                                         Nome digitado na busca diferente do nome do componente.                                         |                                                         Ajuste o nome na busca em Configurações Gateway > Cadastrar aplicação para coincidir exatamente com o do componente criado no Portal.                                                         |
|          **Não consigo convidar um usuário como Desenvolvedor Externo**          |                                       Usuário ainda não possui vínculo ao Portal do Desenvolvedor.                                      |  Certifique que o parceiro possui um usuário vinculado ao Portal do Desenvolvedor do CNPJ dele. Se o parceiro ainda não tiver acesso ao Portal, ele deve enviar o pedido de cadastro: [sankhya.com.br/developers/](http://sankhya.com.br/developers/) |
|                   **Não consigo associar um usuário ao grupo**                   |                                                       Usuário ainda não convidado.                                                      |                                                                               Convide primeiro o usuário em *Gestão de Acessos → Usuários* antes de associá-lo ao grupo.                                                                              |
