---
id: "42630060227607"
titulo: "Como ativar a criptografia da senha de conexão com o banco de dados"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42630060227607-Como-ativar-a-criptografia-da-senha-de-conex%C3%A3o-com-o-banco-de-dados"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-08-31T18:32:54Z"
---

# Como ativar a criptografia da senha de conexão com o banco de dados

**Caminho de acesso:** Web Package Manager (WPM) › Configurações › Editar dados de conexão

---

## O que é e para que serve

O **Web Package Manager (WPM)** permite proteger a senha de conexão com o banco de dados armazenando as credenciais de forma criptografada, gerenciada internamente pelo próprio Wildfly. Use essa opção para aumentar a segurança e a confiabilidade da conexão do ambiente com o banco de dados. Esse recurso não altera nem exige a criação do arquivo `mge-ds.xml` — pelo contrário, esse arquivo deixa de existir quando a proteção está ativa.

![Imagem 1: O Web Package Manager (WPM) permite proteger a senha de conexão com o banco de dados armazenando as credenciais de…](https://ajuda.sankhya.com.br/hc/article_attachments/42630060225815)

## Antes de começar

Tenha em mãos as credenciais de conexão com o banco de dados (**Banco**, **HostIP**, **Porta**, **SID**, **Usuário** e **Senha**), já que você precisa digitá-las novamente ao salvar as configurações de conexão.

## Como usar a tela

O comportamento de ativação muda conforme o servidor de aplicações já ter ou não uma conexão com o banco de dados configurada. Quando já existe uma conexão, você precisa editá-la manualmente para ativar a proteção. Quando não existe conexão, o WPM já exibe o formulário obrigatório logo após o login, com a proteção pronta para ser confirmada.

### Quando já existe uma conexão configurada

1. Acesse a aba **Configurações** no WPM.
2. Clique em **Editar dados de conexão**.
3. No formulário **Informações de Conexão com o Banco de Dados**, digite a **Senha** novamente.
4. Marque **Armazenar configurações em modo privado**, caso ainda não esteja marcada.
5. Clique em **Salvar configurações**.

![Imagem 2: Clique em Salvar configurações .](https://ajuda.sankhya.com.br/hc/article_attachments/42630051722903)

### Quando não existe uma conexão configurada

1. Faça login no WPM.
2. Preencha o formulário **Informações de Conexão com o Banco de Dados**, exibido automaticamente — o preenchimento é obrigatório.
3. Clique em **Salvar configurações**.

## Pontos de atenção

**⚠️ Atenção**

Ao ativar a marcação **Armazenar configurações em modo privado**, o arquivo `mge-ds.xml` deixa de existir, porque as credenciais passam a ser gerenciadas internamente pelo próprio Wildfly.

Para ambientes de produção, ative sempre essa proteção — ela garante mais segurança e confiabilidade na conexão com o banco de dados.
