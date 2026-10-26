---
id: "https://developer.sankhya.com.br/reference/get_v1-regioes"
titulo: "Lista de Regiões"
url: "https://developer.sankhya.com.br/reference/get_v1-regioes"
atualizado_em: "2026-05-13T12:41:23.000Z"
---

# Lista de Regiões

Retorna uma lista de Regiões, com paginação, cadastradas no SankhyaOM.

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
      "name": "Cadastros Básicos",
      "description": "Cadastros Básicos disponíveis no SankhyaOM"
    }
  ],
  "paths": {
    "/v1/regioes": {
      "get": {
        "tags": [
          "Cadastros Básicos"
        ],
        "summary": "Lista de Regiões",
        "description": "Retorna uma lista de Regiões, com paginação, cadastradas no SankhyaOM.",
        "parameters": [
          {
            "name": "page",
            "in": "query",
            "schema": {
              "type": "integer",
              "default": 0
            },
            "description": "Número da página, iniciando sempre por ZERO (0)."
          }
        ],
        "responses": {
          "200": {
            "description": "Lista de Regiões retornada com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "regioes": {
                      "type": "array",
                      "items": {
                        "$ref": "#/components/schemas/Regiao"
                      }
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Requisição inválida."
          },
          "401": {
            "description": "Não autorizado."
          },
          "403": {
            "description": "Acesso proibido."
          },
          "404": {
            "description": "Recurso não encontrado."
          },
          "500": {
            "description": "Erro interno do servidor."
          },
          "501": {
            "description": "Não implementado."
          },
          "502": {
            "description": "Erro de gateway."
          },
          "503": {
            "description": "Serviço indisponível."
          },
          "504": {
            "description": "Tempo limite excedido."
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "Regiao": {
        "type": "object",
        "properties": {
          "codigoRegiao": {
            "type": "integer",
            "description": "Código da região.",
            "example": 101
          },
          "codigoRegiaoPai": {
            "type": "integer",
            "description": "Código da região pai (caso exista hierarquia).",
            "example": 100
          },
          "nome": {
            "type": "string",
            "description": "Nome da região.",
            "example": "Região Sul"
          },
          "grau": {
            "type": "integer",
            "description": "Grau da região, utilizado para hierarquia ou classificação.",
            "example": 2
          },
          "analitica": {
            "type": "boolean",
            "description": "Indica se a região é analítica.",
            "example": true
          },
          "ativa": {
            "type": "boolean",
            "description": "Indica se a região está ativa.",
            "example": true
          }
        }
      }
    },
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
