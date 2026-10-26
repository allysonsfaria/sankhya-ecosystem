---
id: "42427552532247"
titulo: "Aprenda a criar novas opções em campos do tipo “Opções Pré-Cadastradas”"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427552532247-Aprenda-a-criar-novas-op%C3%A7%C3%B5es-em-campos-do-tipo-Op%C3%A7%C3%B5es-Pr%C3%A9-Cadastradas"
trilha: "PLOOMES: Automação de propostas  > Gestão da conta e financeiro > Campos e formulários"
atualizado_em: "2026-08-03T13:28:50Z"
rotulos: ["sync_hc", "ploomes", "ploomes_12632903", "sync_hash_150c8d828561"]
---

# Aprenda a criar novas opções em campos do tipo “Opções Pré-Cadastradas”

## 1) O que são campos do tipo “Opções Pré-Cadastradas”?

Campo de **“Opções Pré‑Cadastradas”** é um tipo de campo em formulários do Ploomes que oferece ao usuário uma lista fixa de respostas pré‑definidas, como se fosse um menu suspenso. Em vez de digitar livremente, o usuário escolhe uma das opções previamente cadastradas, ou cria novas opções a partir do preenchimento do campo, caso tenha permissão, garantindo padronização e consistência nas respostas.

## 2) Como criar novas opções para seleção em campos do tipo “Opções Pré-Cadastradas”?

No Ploomes você consegue criar novas opções selecionáveis para um campo do tipo “Opções Pré-Cadastradas” de duas formas:

1. ### Através da Aba Administração

   1. Caso você seja um usuário administrador, basta acessar o menu Administração → Opções Pré-Cadastradas e seguir o passo a passo presente [neste artigo](https://sankhya.zendesk.com/hc/pt-br/articles/42427406083607)
2. ### Através do Formulário

   1. Antes, nos campos de **Opções Pré‑Cadastradas**, bastava ativar a permissão em um perfil para que todos os usuários daquele perfil pudessem criar novas respostas. Com a atualização, o controle ficou mais granular: agora é possível definir exatamente quem pode adicionar opções, escolhendo usuários individuais, equipes, perfis específicos ou liberando para toda a empresa. Para configurar essa permissão de forma adequada, siga o passo a passo abaixo.

## 3) Sobre a Configuração de Permissões em Campos de “Opções Pré‑Cadastradas”

A nova regra de permissão nos campos do tipo Opções Pré-Cadastradas permite controlar quem pode adicionar novas respostas nesse tipo de campo . Em vez de depender apenas do perfil do usuário, cada campo agora possui uma seção **Configurações de Criação de Opções de Campo**, onde o administrador escolhe os usuários, equipes ou perfis autorizados, ou libera a todos da empresa. Isso evita alterações não autorizadas e dá flexibilidade às organizações.

## 4) Pré‑requisitos

- Para editar as permissões, é necessário ser usuário com perfil Administrador no Ploomes
- O campo precisa ser do tipo **“Opções Pré‑Cadastradas”**

## 5) Configurando as permissões de um campo do tipo “Opções pré-cadastradas”

### 5.1) Configurando a permissão de um campo já criado

- Acesse a aba “Administração” e navegue até a **opção “Campos e Formulários”**
- Selecione a Entidade e, em seguida, o clique no lápis ao lado do campo desejado para editá-lo
- Vá até a opção **“Configurações de Criação de Opções do Campo”**
- Selecione o tipo de regra desejado dentre as opções: um ou mais usuários, perfis, equipes ou todos da empresa

### 5.2) Configurando a permissão ao criar um novo campo

- Crie um novo campo e selecione **Opções Pré‑Cadastradas** como tipo
- Na seção **Configurações de Criação de Opções de Campo**, selecione uma das quatro regras disponíveis e clique em Salvar

### 5.3) Regras de permissionamento

- **Um ou mais usuários**: você poderá buscar e selecionar individualmente quem terá permissão
- **Uma ou mais equipes**: escolha uma ou mais equipes cadastradas; todos os membros dessas equipes poderão criar opções
- **Um ou mais perfis de usuários**: associe perfis (ex.: Vendas, Suporte) autorizados
- **Todos da empresa**: qualquer usuário com acesso ao formulário poderá incluir novas opções

Caso escolha uma das três primeiras opções, selecione ao menos um item; se não selecionar, o sistema impedirá o salvamento do campo.

### 5.4) Migração de campos existentes

- Todos os campos criados antes de 13/11/2025 receberam a configuração **“Por perfil”** nos casos em que algum perfil não tinha permissão para criar novas opções. Quando a conta não tinha nenhuma restrição — ou seja, **todos os perfis podiam criar opções** — então o campo foi configurado como **“Todos da empresa”**.
- Após a migração, administradores podem ajustar a regra em cada campo do tipo Opções Pré-Cadastradas, adaptado o permissionamento por usuários, equipes, todos da empresa, ou reavaliar os perfis que estão com permissão.

## 6) Utilizando a funcionalidade

### 6.1) Inclusão de opções via formulário

- Ao preencher um formulário, usuários autorizados poderão criar novas respostas apenas nos campos em que possuem permissão.
- Se digitarem um valor ainda não existente, poderão cadastrá‑lo; a nova opção ficará disponível para todos os usuários.
- Quem não tiver a devida permissão não verá o botão para adicionar novas opções durante o preenchimento.

### 6.2) Edição de campos via Administração

- Administradores continuam podendo adicionar, editar ou excluir opções diretamente pela aba **Administração > Opções Pré‑Cadastradas**, independentemente da configuração do campo.
- Essa área não é afetada pela nova regra de permissionamento.

## 7) F.A.Q.

### 7.1) Usuários não conseguem adicionar novas opções. O que verificar?

Verifique se eles estão incluídos na regra de permissão configurada para o campo. Usuários não autorizados não veem a opção de adicionar.

### 7.2) Posso alterar a configuração de permissão após salvar o campo?

Sim. Basta editar o campo, acessar a seção **Configurações de Criação de Opções de Campo** e ajustar a regra.

### 7.3) O que acontece se selecionar “Todos da empresa”?

Qualquer usuário com acesso ao formulário poderá criar novas opções naquele campo. Utilize com cautela para campos sensíveis.

## 8) Artigos relacionados

- [https://suporte.ploomes.com/pt-BR/articles/5452378-como-gerenciar-opcoes-pre-cadastradas](https://sankhya.zendesk.com/hc/pt-br/articles/42427406083607)
- [https://suporte.ploomes.com/pt-BR/articles/5452321-como-criar-um-campo-de-opcoes-pre-cadastradas-multiplas](https://sankhya.zendesk.com/hc/pt-br/articles/42427345577751)
