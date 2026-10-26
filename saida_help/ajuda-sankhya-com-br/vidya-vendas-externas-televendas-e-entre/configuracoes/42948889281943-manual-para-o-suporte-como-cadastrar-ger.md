---
id: "42948889281943"
titulo: "Manual para o Suporte: como cadastrar, gerenciar clientes e validar integrações no novo ambiente AWS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42948889281943-Manual-para-o-Suporte-como-cadastrar-gerenciar-clientes-e-validar-integra%C3%A7%C3%B5es-no-novo-ambiente-AWS"
trilha: "VIDYA: Vendas externas, televendas e entregas > Central de ajuda > Configurações"
atualizado_em: "2026-08-24T16:55:04Z"
rotulos: ["sync_hc", "vidya", "vidya_567937", "sync_hash_83a2c7bdea8e"]
---

# Manual para o Suporte: como cadastrar, gerenciar clientes e validar integrações no novo ambiente AWS

Com a chegada do **backend unificado**, todos os clientes da Vidya passam agora a utilizar **um único backend centralizado na AWS**. Isso traz mais estabilidade, performance e padronização, além de eliminar boa parte dos erros que antes aconteciam por configurações manuais no servidor.

Este guia explica **de forma prática** como a equipe de Suporte deve atuar a partir de agora.

## 1. O que muda com o Backend Unificado

### Antes:

- Cada cliente tinha seu próprio backend.
- Era necessário cadastrar **servidor**, **application**, **token**, ajustar links manualmente etc.
- Alto risco de erro (token errado, ambiente errado, SQL/Oracle invertidos etc).
- Variáveis repetidas em cada instalação.

### Agora:

- Todos os clientes usam **o mesmo backend único**.
- Todas as informações ficam **centralizadas na AWS**.
- O cadastro do cliente é feito **uma única vez** via Postman.
- Alterações como mudança de link ou token são feitas por endpoints específicos.

## 2. O que é a Collection “Gerenciar Clientes” Imagem 1: 2. O que é a Collection “Gerenciar Clientes”

Uma collection exclusiva criada para:

### ✔ Cadastrar novos clientes

### ✔ Atualizar link/token/ambiente

### ✔ Listar clientes cadastrados

### ✔ Consultar detalhes de um cliente

### ✔ Atualizar hosts (base principal e testes)

### ✔ Forçar refresh de cache

### ✔ Executar testes automáticos de requisições

Esta collection será utilizada pelo Suporte, Implantação e Delivery.

## 3. Como cadastrar um novo cliente Imagem 2: 3. Como cadastrar um novo cliente

No Postman, abra a collection **Gerenciar Clientes → POST manager > add-complete-client**.

Você deverá preencher os seguintes campos **apenas uma vez**:

- **clientId:** nome identificador do cliente (ex.: CasaDoCroissant)
- **db:** Oracle ou SQL
- **hosts (link Sankhya):**

  - **host:** URL do SANKHYA do cliente
  - **token:** Token gerado no Sankhya
  - **isSandBox:** "S" → se no Sankhya estiver “Teste” / "N" se estiver “Produção”

> 🔍 **Onde verificar se é Sandbox?**
> No Sankhya, acesse **Configurações → Gateway → Tipo de Ambiente**.

## 4. Como alterar o link ou token do cliente Imagem 3: 4. Como alterar o link ou token do cliente

Se o cliente mudar o link do Sankhya ou regenerar token:

Use o endpoint **POST manager > add-host.**

Preencha as informações:

- ClientID (nome cadastrado)
- hostIndex
- Novo host
- Novo token
- Sandbox

Não é necessário mexer em servidor, base ou estrutura.
A alteração é feita globalmente e vale imediatamente.

## 5. Consultar clientes cadastrados Imagem 4: 5. Consultar clientes cadastrados

No Postman, abra a collection **Gerenciar Clientes → POST manager > clients-status**, para uma listagem de todos os clientes cadastrados.

Caso precise de informações especificas de um cliente, utilize **GET manager > clients-get, onde deverá pesquisar pelo cliente ID na própria requisição**

## 6. Cache e Refresh

O novo backend salva em cache:

- configurações
- tabelas
- campos
- informações de cabeçalho
- informações de sincronização inicial

Sempre que cadastrar um cliente, o refresh é automático.

Caso precise:

✔ Use **POST manager > refresh-clients**
Recarrega as informações da AWS manualmente.

## 7. Base64

O base64 deverá seguir a estrutura abaixo, sendo a única mudança a baseUrl, que sempre será o da api.force:

{

"baseName": "NOME CLIENTE",

"baseUrl": "http://api.force.vidyacode.com.br:1500",

"baseImage": "LINK SANKHYA DO CLIENTE"

}

**Obs:** Para consultas de status e cliente especifico utilizando o clientID, utilize o base64 nessa estrutura:

{"urlErp": "", "user": "vidya"}

## 8. Boas práticas para testes

- Sempre configure corretamente as **variáveis** (host, clientID, vendedor, produto etc).
- Sempre teste **após qualquer migração**.
- Em caso de erro, verifique se é:

  - ⚠ problema de regra de negócio
  - ⚠ configuração no Sankhya
  - ❌ erro do backend (encaminhar ao Dev)

## 9. Base de Teste

Agora a lógica muda:

- Existe **uma base de teste única** (ex.: `api.teste.videacode.com.br`)
- Todos que testam usam a mesma base
- Clientes não possuem mais múltiplos “servidores próprios” de teste

Se o vendedor de teste estiver com problema:

- Basta mover ele temporariamente para a base normal do cliente.
