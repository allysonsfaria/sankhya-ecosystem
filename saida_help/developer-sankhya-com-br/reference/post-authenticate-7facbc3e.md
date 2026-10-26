---
id: "https://developer.sankhya.com.br/reference/post_authenticate"
titulo: "Autenticação com OAuth 2.0 (Client Credentials)"
url: "https://developer.sankhya.com.br/reference/post_authenticate"
atualizado_em: "2026-05-27T21:06:58.000Z"
---

# Autenticação com OAuth 2.0 (Client Credentials)

Este serviço implementa o fluxo **OAuth 2.0 Client Credentials**, com uso adicional do cabeçalho `X-Token`. Ele substitui o modelo antigo baseado em **appkey + token** e oferece maior segurança e flexibilidade, permitindo autenticação em todo o ecossistema de softwares do Grupo Sankhya.

[Clique aqui para ver como criar um novo componente de integração](https://developer.sankhya.com.br/docs/portal-do-desenvolvedor).

Gera um access token JWT para autenticação em APIs do ecossistema Sankhya.
É necessário enviar:
- `client_id` e `client_secret` fornecidos na Área do Desenvolvedor
- `X-Token` obtido na tela **Configurações Gateway** do Sankhya Om (ou de outros sistemas do grupo)


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
    "/authenticate": {
      "post": {
        "tags": [
          "Autenticação"
        ],
        "summary": "Autenticação com OAuth 2.0 (Client Credentials)",
        "description": "Este serviço implementa o fluxo **OAuth 2.0 Client Credentials**, com uso adicional do cabeçalho `X-Token`. Ele substitui o modelo antigo baseado em **appkey + token** e oferece maior segurança e flexibilidade, permitindo autenticação em todo o ecossistema de softwares do Grupo Sankhya.\n\n[Clique aqui para ver como criar um novo componente de integração](https://developer.sankhya.com.br/docs/portal-do-desenvolvedor).\n\nGera um access token JWT para autenticação em APIs do ecossistema Sankhya.\nÉ necessário enviar:\n- `client_id` e `client_secret` fornecidos na Área do Desenvolvedor\n- `X-Token` obtido na tela **Configurações Gateway** do Sankhya Om (ou de outros sistemas do grupo)\n",
        "requestBody": {
          "required": true,
          "content": {
            "application/x-www-form-urlencoded": {
              "schema": {
                "type": "object",
                "required": [
                  "client_id",
                  "client_secret",
                  "grant_type"
                ],
                "properties": {
                  "client_id": {
                    "type": "string",
                    "description": "Identificador único da aplicação gerado na Área do Desenvolvedor.",
                    "example": "my-client-id-123"
                  },
                  "client_secret": {
                    "type": "string",
                    "description": "Segredo da aplicação gerado na Área do Desenvolvedor.",
                    "example": "my-client-secret-abc"
                  },
                  "grant_type": {
                    "type": "string",
                    "description": "Tipo do fluxo OAuth 2.0.",
                    "enum": [
                      "client_credentials"
                    ],
                    "example": "client_credentials"
                  }
                }
              }
            }
          }
        },
        "parameters": [
          {
            "in": "header",
            "name": "X-Token",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Token obtido na tela **Configurações Gateway** do Sankhya Om (ou de outros sistemas do Grupo Sankhya).",
            "example": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
          }
        ],
        "responses": {
          "200": {
            "description": "Token de acesso gerado com sucesso",
            "content": {
              "application/x-www-form-urlencoded": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "access_token": {
                      "type": "string",
                      "description": "Token JWT a ser usado na autorização das APIs.",
                      "example": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9"
                    },
                    "expires_in": {
                      "type": "integer",
                      "description": "Tempo de expiração do token em segundos.",
                      "example": 300
                    },
                    "refresh_expires_in": {
                      "type": "integer",
                      "description": "Tempo de expiração do refresh token em segundos. Geralmente `0` se não for aplicável.",
                      "example": 0
                    },
                    "token_type": {
                      "type": "string",
                      "description": "Tipo do token retornado.",
                      "example": "Bearer"
                    },
                    "not-before-policy": {
                      "type": "integer",
                      "description": "Política de validação temporal do token.",
                      "example": 0
                    },
                    "scope": {
                      "type": "string",
                      "description": "Escopos do token. Pode estar vazio.",
                      "example": ""
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Requisição inválida (parâmetros ausentes ou incorretos)"
          },
          "401": {
            "description": "Credenciais inválidas (client_id, client_secret ou X-Token inválido)"
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
