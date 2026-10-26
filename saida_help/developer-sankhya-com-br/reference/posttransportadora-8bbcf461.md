---
id: "https://developer.sankhya.com.br/reference/posttransportadora"
titulo: "Incluir transportadora"
url: "https://developer.sankhya.com.br/reference/posttransportadora"
atualizado_em: "2026-05-13T12:41:23.000Z"
---

# Incluir transportadora

Permite incluir uma transportadora no ERP.

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
      "name": "Logística",
      "description": "Cadastros básicos relacionados a motorista, transportadora, ordens de carga, veículos, no Sankhya Om"
    }
  ],
  "paths": {
    "/v1/parceiros/transportadoras": {
      "post": {
        "tags": [
          "Logística"
        ],
        "summary": "Incluir transportadora",
        "description": "Permite incluir uma transportadora no ERP.",
        "operationId": "postTransportadora",
        "requestBody": {
          "description": "Objeto da transportadora a ser incluída.",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/transportadoraInput"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Operação bem sucedida.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/transportadora"
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
          "500": {
            "description": "Erro interno do servidor."
          }
        },
        "security": [
          {
            "Bearer": []
          }
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "transportadoraInput": {
        "type": "object",
        "required": [
          "nome",
          "cnpj"
        ],
        "properties": {
          "nome": {
            "type": "string",
            "description": "Nome da transportadora.",
            "example": "Transportadora Veloz"
          },
          "cnpj": {
            "type": "string",
            "description": "CNPJ da empresa transportadora.",
            "example": "21291462000158"
          },
          "ie": {
            "type": "string",
            "description": "Inscrição estadual da transportadora.",
            "example": "123159149"
          },
          "email": {
            "type": "string",
            "example": "contato@transportadoraveloz.com.br"
          },
          "telefone": {
            "type": "string",
            "description": "Número de telefone.",
            "example": "1155554444"
          },
          "endereco": {
            "$ref": "#/components/schemas/Transportadorasendereco"
          }
        }
      },
      "transportadora": {
        "allOf": [
          {
            "type": "object",
            "properties": {
              "ativo": {
                "type": "boolean",
                "description": "Indica se o cadastro está ativo.",
                "example": true,
                "readOnly": true
              },
              "codigoTransportadora": {
                "type": "integer",
                "description": "Código da transportadora.",
                "example": 9542
              }
            }
          },
          {
            "$ref": "#/components/schemas/transportadoraInput"
          }
        ]
      },
      "Transportadorasendereco": {
        "type": "object",
        "properties": {
          "logradouro": {
            "type": "string",
            "example": "Rua Central"
          },
          "numero": {
            "type": "string",
            "example": "123"
          },
          "complemento": {
            "type": "string",
            "example": "Sala 10"
          },
          "bairro": {
            "type": "string",
            "example": "Centro"
          },
          "cidade": {
            "type": "string",
            "example": "Uberlândia"
          },
          "codigoIbge": {
            "type": "string",
            "example": "3170206"
          },
          "uf": {
            "type": "string",
            "example": "MG"
          },
          "cep": {
            "type": "string",
            "example": "38400000"
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
