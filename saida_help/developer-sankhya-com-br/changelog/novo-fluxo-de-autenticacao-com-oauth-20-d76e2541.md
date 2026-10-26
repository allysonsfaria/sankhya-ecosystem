---
id: "https://developer.sankhya.com.br/changelog/novo-fluxo-de-autenticacao-com-oauth-20"
titulo: "Novo Fluxo de Autenticação com OAuth 2.0"
url: "https://developer.sankhya.com.br/changelog/novo-fluxo-de-autenticacao-com-oauth-20"
---

# Novo Fluxo de Autenticação com OAuth 2.0

Para elevar a segurança e a padronização das nossas integrações, implementamos um novo fluxo de autenticação baseado no protocolo **OAuth 2.0**, utilizando o fluxo `client_credentials`.\
Esse novo método substitui o modelo antigo que usava apenas **appkey** e **token**, trazendo mais controle e modernidade.

***

## O que mudou?

### Antes

No **Portal do Desenvolvedor** (também referenciado como *Área do Desenvolvedor* ou *Dev Portal*), um componente de integração recebia uma **appkey** (para ambientes de sandbox e produção).\
O login era feito usando essa appkey junto com um **token** gerado na tela **Configurações Gateway** do Sankhya Om.

### Agora

O processo foi atualizado:

* No **Portal do Desenvolvedor**, cada novo componente de integração gera um par de credenciais:
  * `client_id`
  * `client_secret`\
    Para os ambientes de **sandbox (homologação)** e **produção**.
* O **token** continua sendo obtido na tela **Configurações Gateway** do Sankhya OM, caso a integração seja para se conectar a este sistema.
* O novo modelo é mais flexível: **outros softwares do Grupo Sankhya** agora também podem gerar um token, permitindo que seu client acesse diferentes sistemas do grupo, não se limitando apenas ao Sankhya Om.

***

## Como funciona a nova autenticação?

O novo fluxo exige que você utilize o **client\_id**, o **client\_secret** e o **token**.\
Essas credenciais, quando enviadas corretamente, validam sua aplicação e autorizam o acesso.

### Exemplo de requisição cURL (produção):

```bash
curl --request POST \
  --url https://api.sankhya.com.br/authenticate \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --header 'X-Token: TOKEN_DO_CLIENTE_AQUI' \
  --data grant_type=client_credentials \
  --data client_id=SEU_CLIENT_ID_AQUI \
  --data client_secret=SEU_CLIENT_SECRET_AQUI

 
```

<br />

## Benefícios

Esse novo modelo, além de **mais seguro**, simplifica o acesso a todo o **ecossistema de softwares do Grupo Sankhya**, garantindo **maior controle e interoperabilidade** nas integrações.\
👉 [Saiba mais aqui](https://developer.sankhya.com.br/reference/post_authenticate)

***

## Como realizar a migração?

Planeje a migração para o novo serviço **`/authenticate`** o quanto antes, garantindo que suas integrações estejam alinhadas ao padrão atual.

> ❗️ O serviço **login** permanecerá disponível até **31/03/2026**.
>
> Após essa data, **apenas o novo serviço estará disponível**.

Para utilizar o novo fluxo, é necessário:

1. Criar um **novo componente do tipo integração** dentro da solução no **Portal do Desenvolvedor**.
2. Obter um **novo token** com os clientes que utilizam a integração.

👉 [Clique aqui para ver como criar um novo componente de integração](https://developer.sankhya.com.br/docs/portal-do-desenvolvedor)
