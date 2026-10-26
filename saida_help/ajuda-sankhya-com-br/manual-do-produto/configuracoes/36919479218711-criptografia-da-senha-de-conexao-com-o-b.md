---
id: "36919479218711"
titulo: "Criptografia da Senha de Conexão com o Banco de Dados (Segurança, WPM)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36919479218711-Criptografia-da-Senha-de-Conex%C3%A3o-com-o-Banco-de-Dados-Seguran%C3%A7a-WPM"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T14:00:51Z"
rotulos: ["Configuração", "Segurança", "WPM", "WildFly", "Editar dados de conexão", "Servidor de Aplicações", "Criptografia da Senha de Conexão com o Banco de Dados (Segurança WPM)", "Criptografia da Senha", "Banco de Dados"]
---

# Criptografia da Senha de Conexão com o Banco de Dados (Segurança, WPM)

**Versão Mínima**: Acima das versões 4.33b189, 4.34b268 e 4.35b305

**Caminho de Acesso**: Atualização do sistema > Configurações > Editar dados de conexão

---

### 1. Descrição da Funcionalidade

A partir das versões indicadas, o **Web Package Maneger (WPM)**, que é a ferramenta de gerenciamento hospedada pelo **servidor de aplicações WildFly**, incorporou um novo recurso de segurança para proteger a **senha de conexão com o banco de dados (Datasource)**.

O principal propósito desta funcionalidade é aprimorar a segurança e confiabilidade do ambiente do servidor de aplicações, garantindo que a credencial de acesso ao banco de dados seja **gerenciada e criptografada internamente pelo próprio WildFly**, em vez de ser armazenada de forma legível em arquivos de configuração externos.

---

### 2. Pré-requisitos

- **Permissões necessárias**: Acesso ao Servidor de Aplicações e credenciais de login para o WPM.

---

### 3. Jornada de Uso

O processo para ativar a criptografia (Armazenamento privado dos dados) é realizado dentro do WPM, durante a configuração ou edição do Datasource.

#### 3.1. Ativação em Conexão Existente

Se o servidor de aplicações já possui uma configuração de conexão (Datasource) ativa:

1. Acesse o **WPM** (Web Package Maneger).
2. Na seção de configurações de conexão, clique na opção para **"Editar a conexão"** existente.

![Imagem 1: Na seção de configurações de conexão, clique na opção para "Editar a conexão" existente.](https://ajuda.sankhya.com.br/hc/article_attachments/36919479209111)

3. No formulário **"Informação de Conexão com o Banco de Dados"** (Datasource), localize o campo da senha.
4. **Digite a senha novamente** no campo correspondente (mesmo que já estivesse preenchido com pontos).
5. Certifique-se de que a opção de **"Armazenamento privado dos dados"** esteja selecionada (essa é a opção que garante a criptografia e o gerenciamento interno pelo WildFly).
6. Clique em **"Salvar Configurações"**. A senha será criptografada e armazenada internamente pelo WildFly.

#### 3.2. Ativação em Nova Conexão

Se não existe uma conexão configurada (primeiro acesso ou nova instalação):

1. Faça o login no **WPM**.
2. O pop-up de **"Informação de Conexão com o Banco de Dados"** será exibido automaticamente, sendo o preenchimento obrigatório.
3. Preencha todos os campos da conexão, incluindo a **senha**.
4. O sistema utilizará automaticamente o mecanismo de "Armazenar configurações em modo privado" para criptografar e gerenciar a senha internamente no WildFly.

![Imagem 2: O sistema utilizará automaticamente o mecanismo de "Armazenar configurações em modo privado" para criptografar e…](https://ajuda.sankhya.com.br/hc/article_attachments/36919479210391)

5. Clique em **"Salvar Configurações"**.

---

### 4. Pontos de Atenção e Boas Práticas

| Ponto de Atenção | Descrição |
| --- | --- |
| **Recomendação para Produção** | É **altamente recomendado** que esta opção de "Armazenamento privado dos dados" (criptografia interna pelo WildFly) seja utilizada em **todos os ambientes produtivos** para maximizar a segurança. |
| **Arquivo** **mge-ds.xml** | O arquivo mge-ds.xml **deixa de ser utilizado** para armazenar credenciais, pois elas passam a ser gerenciadas internamente pelo **WildFly** de forma segura e criptografada. Em versões anteriores, este arquivo era a fonte do Datasource. |
| **Reversão** | Para desativar o armazenamento privado e retornar ao método antigo, é necessário desmarcar a opção no WPM e salvar. Isso fará com que o WildFly volte a utilizar um método de armazenamento menos seguro. **Não recomendado para produção.** |
