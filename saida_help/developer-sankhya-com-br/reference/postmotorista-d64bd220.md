---
id: "https://developer.sankhya.com.br/reference/postmotorista"
titulo: "Incluir motorista"
url: "https://developer.sankhya.com.br/reference/postmotorista"
atualizado_em: "2026-05-13T12:41:23.000Z"
---

# Incluir motorista

Permite incluir um motorista no ERP.

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
    "/v1/parceiros/motoristas": {
      "post": {
        "tags": [
          "Logística"
        ],
        "summary": "Incluir motorista",
        "description": "Permite incluir um motorista no ERP.",
        "operationId": "postMotorista",
        "requestBody": {
          "description": "Objeto do motorista a ser incluído.",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/motoristaPayload"
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
                  "$ref": "#/components/schemas/motorista"
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
      "motoristaPayload": {
        "type": "object",
        "required": [
          "nome",
          "cpf"
        ],
        "properties": {
          "nome": {
            "type": "string",
            "description": "Nome do motorista",
            "example": "José da Silva"
          },
          "cpf": {
            "type": "string",
            "description": "Documento CPF.",
            "example": "12315914799"
          },
          "rg": {
            "type": "string",
            "description": "Documento RG.",
            "example": "12315914799"
          },
          "cnh": {
            "type": "string",
            "description": "Número da CNH.",
            "example": "12315914799"
          },
          "categoriaCnh": {
            "type": "string",
            "description": "Categoria da CNH.",
            "example": "DE"
          },
          "dataVencimentoCnh": {
            "type": "string",
            "description": "Data de vencimento da CNH.",
            "example": "15/09/2026 00:00:00"
          },
          "email": {
            "type": "string",
            "example": "contato@provedor.com.br"
          },
          "telefone": {
            "type": "string",
            "description": "Número de telefone.",
            "example": "34912349966"
          },
          "endereco": {
            "$ref": "#/components/schemas/Motoristasendereco"
          }
        }
      },
      "motorista": {
        "allOf": [
          {
            "type": "object",
            "properties": {
              "codigoMotorista": {
                "type": "integer",
                "description": "Código do motorista.",
                "example": 8115
              }
            }
          },
          {
            "$ref": "#/components/schemas/motoristaPayload"
          }
        ]
      },
      "Motoristasendereco": {
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
