---
id: "https://developer.sankhya.com.br/reference/post_login-1"
titulo: "Autenticação com usuário e senha (fluxo legado/descontinuado)"
url: "https://developer.sankhya.com.br/reference/post_login-1"
atualizado_em: "2026-05-27T21:06:58.000Z"
---

# Autenticação com usuário e senha (fluxo legado/descontinuado)

Este serviço de login corresponde ao modelo de autenticação legado/descontinuado, que utiliza usuário e senha do SankhyaID, em conjunto com as chaves appkey e token.

Embora ainda esteja disponível para manter a compatibilidade com integrações existentes, ele foi substituído pelo novo fluxo OAuth 2.0, que oferece mais segurança e flexibilidade.

**Recomendação**: Planeje a migração para o novo serviço `/authenticate` o quanto antes, garantindo que suas integrações estejam alinhadas ao padrão atual. O serviço `login` permanecerá disponível, porém sem nenhuma atualização/evolução. A Sankhya indica fortemente que todas as integrações migrem para o novo modelo de autenticação `/authenticate`.

Para utilizar o novo fluxo, basta criar um componente do tipo integração no Portal do Desenvolvedor. 

[Clique aqui para ver como criar um novo componente de integração](https://developer.sankhya.com.br/docs/portal-do-desenvolvedor).

**Fluxo recomendado:**
1. Login (`/login`)
2. Chamadas subsequentes usando o `bearerToken`
3. Logout (`/gateway/v1/mge/service.sbr?serviceName=MobileLoginSP.logout`)

- O `bearerToken` deve ser enviado no cabeçalho `Authorization` das chamadas subsequentes.
- Sessão expira após 30 minutos de inatividade (configurável pelo parâmetro `INATSESSTIMEOUT`).
- Recomenda-se sempre realizar **logout** ao final.

Autentica o usuário no SankhyaOM utilizando **usuário, senha, appkey e token**.
Retorna um `bearerToken` que deve ser utilizado em todas as requisições seguintes.


# OpenAPI definition

```json
{
  "openapi": "3.0.3",
  "info": {
    "title": "API Sankhya",
    "description": "API de Integrações com Gateway Sankhya.\n\nOs endpoints aqui documentados estão todos baseados no EasyAPI, seguindo padrão Rest e documentação padrão OpenAPI/Swagger.\n\nPara utilizar todos os serviços, é necessário realizar o login conforme descrito na documentação.\n",
    "termsOfService": "https://www.sankhya.com.br/",
    "license": {
      "name": "Licença Sankhya",
      "url": "https://www.sankhya.com.br/"
    },
    "version": "1.0"
  },
  "servers": [
    {
      "url": "https://api.sankhya.com.br",
      "description": "Produção"
    },
    {
      "url": "https://api.sandbox.sankhya.com.br",
      "description": "Sandbox"
    }
  ],
  "externalDocs": {
    "description": "Saiba mais sobre a API Sankhya",
    "url": "https://developer.sankhya.com.br/reference/api-de-integra%C3%A7%C3%B5es-sankhya"
  },
  "security": [
    {
      "Bearer": []
    }
  ],
  "tags": [
    {
      "name": "Autenticação",
      "description": "Fluxo de Autenticação para utilizar APIs Gateway da Sankhya"
    }
  ],
  "paths": {
    "/login": {
      "post": {
        "tags": [
          "Autenticação"
        ],
        "summary": "Autenticação com usuário e senha (fluxo legado/descontinuado)",
        "description": "Este serviço de login corresponde ao modelo de autenticação legado/descontinuado, que utiliza usuário e senha do SankhyaID, em conjunto com as chaves appkey e token.\n\nEmbora ainda esteja disponível para manter a compatibilidade com integrações existentes, ele foi substituído pelo novo fluxo OAuth 2.0, que oferece mais segurança e flexibilidade.\n\n**Recomendação**: Planeje a migração para o novo serviço `/authenticate` o quanto antes, garantindo que suas integrações estejam alinhadas ao padrão atual. O serviço `login` permanecerá disponível, porém sem nenhuma atualização/evolução. A Sankhya indica fortemente que todas as integrações migrem para o novo modelo de autenticação `/authenticate`.\n\nPara utilizar o novo fluxo, basta criar um componente do tipo integração no Portal do Desenvolvedor. \n\n[Clique aqui para ver como criar um novo componente de integração](https://developer.sankhya.com.br/docs/portal-do-desenvolvedor).\n\n**Fluxo recomendado:**\n1. Login (`/login`)\n2. Chamadas subsequentes usando o `bearerToken`\n3. Logout (`/gateway/v1/mge/service.sbr?serviceName=MobileLoginSP.logout`)\n\n- O `bearerToken` deve ser enviado no cabeçalho `Authorization` das chamadas subsequentes.\n- Sessão expira após 30 minutos de inatividade (configurável pelo parâmetro `INATSESSTIMEOUT`).\n- Recomenda-se sempre realizar **logout** ao final.\n\nAutentica o usuário no SankhyaOM utilizando **usuário, senha, appkey e token**.\nRetorna um `bearerToken` que deve ser utilizado em todas as requisições seguintes.\n",
        "parameters": [
          {
            "in": "header",
            "name": "token",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Token obtido na tela **Configurações Gateway** do SankhyaOm.",
            "example": "8fedf240-ea7f-11ed-a05b-0242ac120003"
          },
          {
            "in": "header",
            "name": "appkey",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Chave da aplicação gerada na Área do Desenvolvedor.",
            "example": "db654b42-ea7f-11ed-a05b-0242ac120003"
          },
          {
            "in": "header",
            "name": "username",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Usuário válido vinculado ao SankhyaID.",
            "example": "user@dominio.com.br"
          },
          {
            "in": "header",
            "name": "password",
            "required": true,
            "schema": {
              "type": "string",
              "format": "password"
            },
            "description": "Senha do usuário informado.",
            "example": "MinhaSenhaSegura123"
          }
        ],
        "responses": {
          "200": {
            "description": "Login realizado com sucesso",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "bearerToken": {
                      "type": "string",
                      "description": "Token de sessão a ser usado no cabeçalho `Authorization` das chamadas subsequentes.",
                      "example": "bearerToken_da_sessao_ativa_retorna_bem_aqui"
                    },
                    "error": {
                      "type": "string",
                      "nullable": true,
                      "description": "Informações de erro, se houver.",
                      "example": null
                    }
                  }
                }
              }
            }
          },
          "401": {
            "description": "Credenciais inválidas (usuário, senha, appkey ou token incorretos)"
          },
          "500": {
            "description": "Erro interno no servidor de autenticação"
          }
        }
      }
    }
  },
  "components": {
    "securitySchemes": {
      "Bearer": {
        "type": "apiKey",
        "name": "Authorization",
        "in": "header",
        "description": "Insira o token com o prefixo 'Bearer: ' ex. \"Bearer abcde12345\"."
      }
    }
  }
}
```
