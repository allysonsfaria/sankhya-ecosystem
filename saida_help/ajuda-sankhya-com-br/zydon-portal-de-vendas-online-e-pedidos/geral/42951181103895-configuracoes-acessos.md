---
id: "42951181103895"
titulo: "Configurações - Acessos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42951181103895-Configura%C3%A7%C3%B5es-Acessos"
trilha: "ZYDON: Portal de vendas online e pedidos B2B > Geral"
atualizado_em: "2026-08-24T13:56:59Z"
rotulos: ["zydon", "sync_hc", "zydon_213266016938", "sync_hash_98c8ddd7738f"]
---

# Configurações - Acessos

Como configurar e controlar quem pode se cadastrar em seu portal

Defina como novos clientes e usuários poderão solicitar acesso à sua loja B2B no Zydon Admin.
Este painel permite controlar **quem pode se cadastrar**, **como o acesso será solicitado e aprovado**, e **em quais grupos de usuários os novos cadastros serão inseridos**.

## Como acessar

1. No menu lateral do Zydon Admin, clique em **Configurações**
2. Depois clique em **Acessos**.

## Imagem 1: Depois clique em Acessos .

## Geral

## Cadastro público

Ative a opção **“Permitir solicitação de acesso via Loja”** para permitir que novos clientes solicitem acesso diretamente pela vitrine ou tela de login da sua loja.
Se desativado, apenas administradores poderão criar acessos manualmente.

## Perfil do cliente

Defina quais tipos de cliente sua loja aceitará no momento do cadastro:

- - Pessoa Jurídica (CNPJ)
  - Pessoa Física (CPF)

Você pode ativar um ou ambos os perfis, de acordo com sua operação.

## Pré-visualização da experiência do cliente

A tela mostra como o botão **“Solicitar acesso”** será exibido:

- - Na página de **login**, com o link "Não tem uma conta? Solicite seu acesso."
  - Na **vitrine da loja**, com o botão visível no topo da página.

![Imagem 2: Na vitrine da loja , com o botão visível no topo da página.](https://ajuda.sankhya.com.br/hc/article_attachments/42951205993879)

## Criação de usuário para cliente existente

Essa configuração define como lidar com **novos usuários vinculados a um cliente já existente** (mesmo CPF ou CNPJ).

- - **Aprovar automaticamente:** permite acesso imediato sem intervenção manual.
  - **Grupos de usuários:** define em qual grupo o novo usuário será inserido automaticamente.

## Cadastro de novo cliente

Controla como será o processo de aprovação para **clientes que ainda não existem na base**.

- - **Aprovar automaticamente:** ativa o acesso sem a necessidade de validação manual.
  - **Grupos de usuários:** define o grupo padrão em que esses novos cadastros serão inseridos.

![Imagem 3: Grupos de usuários: define o grupo padrão em que esses novos cadastros serão inseridos.](https://ajuda.sankhya.com.br/hc/article_attachments/42951221929623)

**Importante**

Estas são configurações padrão para novos acessos.
As permissões e regras podem ser personalizadas de duas formas:

- - **Individualmente:** em Acessos > Usuários, editando um usuário específico.
  - **Em grupo:** em Acessos > Grupos de Usuários, aplicando as regras ao grupo inteiro.

## Formulário de Acesso

Configure o formulário exibido para novos usuários ao solicitar acesso a sua conta, definindo quais campos serão coletados no cadastro.

Em Configurações > Acessos > Formulário de Acesso, clique em "**Clique para vincular um formulário**". Escolha um formulário já criado na lista ou clique em Adicionar para criar um novo formulário no Construtor de Formulários do Zydon.

![Imagem 4: Em Configurações > Acessos > Formulário de Acesso, clique em " Clique para vincular um formulário ". Escolha um…](https://ajuda.sankhya.com.br/hc/article_attachments/42951194981015)

## Campos de persistência

Conecte campos do formulário de acesso diretamente ao perfil dos seus clientes, automatizando a coleta de dados e garantindo que nenhuma informação importante seja perdida após o cadastro.

Em Configurações > Acessos > Campos de persistência, clique em Adicionar para criar uma nova regra de mapeamento. Para cada regra, defina:

- - **Origem do dado**: escolha entre Campo do formulário (um campo especifico de um formulário vinculado), Contexto, Tabela de dados ou Valor fixo.
  - **Destino**: informe o campo do perfil do cliente que deve receber o valor coletado.

![Imagem 5: Destino : informe o campo do perfil do cliente que deve receber o valor coletado.](https://ajuda.sankhya.com.br/hc/article_attachments/42951222102551)

**Dica**: Use Campos de persistência junto com o Formulário de Acesso para capturar dados personalizados (ex.: segmento de atuação, ramo de negocio) direto no cadastro e já salva-los automaticamente no perfil do cliente, sem retrabalho manual.

---

[admin.zydon.com.br/criacao-conta](https://admin.zydon.com.br/criacao-conta)
