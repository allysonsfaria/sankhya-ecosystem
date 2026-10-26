---
id: "https://developer.sankhya.com.br/reference/get_v1-bairros-codigobairro"
titulo: "Bairro específico"
url: "https://developer.sankhya.com.br/reference/get_v1-bairros-codigobairro"
atualizado_em: "2026-05-13T12:41:23.000Z"
---

# Bairro específico

Retorna um Bairro específico com base no parâmetro enviado na requisição.

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
    "/v1/bairros/{codigoBairro}": {
      "get": {
        "tags": [
          "Cadastros Básicos"
        ],
        "summary": "Bairro específico",
        "description": "Retorna um Bairro específico com base no parâmetro enviado na requisição.",
        "parameters": [
          {
            "name": "codigoBairro",
            "in": "path",
            "required": true,
            "schema": {
              "type": "integer",
              "default": 0
            },
            "description": "Código do Bairro para retorno"
          }
        ],
        "responses": {
          "200": {
            "description": "Dados do Bairro retornados com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/BairrosBairro"
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
      "BairrosBairro": {
        "type": "object",
        "properties": {
          "codigoBairro": {
            "type": "integer",
            "example": 101,
            "description": "Código único identificador do bairro."
          },
          "nome": {
            "type": "string",
            "example": "Centro Histórico",
            "description": "Nome do bairro utilizado internamente no sistema."
          },
          "nomeRegiao": {
            "type": "string",
            "example": "Zona Sul",
            "description": "Nome da região Vinculada ao Bairro."
          },
          "nomeCorreio": {
            "type": "string",
            "example": "Centro",
            "description": "Nome do bairro conforme registro nos Correios."
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
