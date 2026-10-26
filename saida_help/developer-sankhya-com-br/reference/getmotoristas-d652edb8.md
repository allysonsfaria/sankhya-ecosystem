---
id: "https://developer.sankhya.com.br/reference/getmotoristas"
titulo: "Retornar lista de motoristas"
url: "https://developer.sankhya.com.br/reference/getmotoristas"
atualizado_em: "2026-05-13T12:41:23.000Z"
---

# Retornar lista de motoristas

Permite acessar a lista de motoristas cadastrados no ERP.

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
      "get": {
        "tags": [
          "Logística"
        ],
        "summary": "Retornar lista de motoristas",
        "description": "Permite acessar a lista de motoristas cadastrados no ERP.",
        "operationId": "getMotoristas",
        "parameters": [
          {
            "name": "page",
            "in": "query",
            "description": "Informe neste atributo a \"página\" desejada.",
            "required": true,
            "schema": {
              "type": "integer",
              "format": "int64",
              "example": 1
            }
          },
          {
            "name": "modifiedSince",
            "in": "query",
            "description": "Data e hora da última modificação. Quando esse parâmetro é enviado, o serviço retorna apenas os registros que foram modificados a partir da data e hora informadas. Vale ressaltar que este recurso é condicionada a utilização do [Log de Alterações no SankhyaOm](https://developer.sankhya.com.br/reference/get_logalteracoestabelas) no ambiente do cliente. O formato deve ser o seguinte: DD/MM/AAAA HH:MM",
            "required": false,
            "schema": {
              "type": "string",
              "example": "07/10/2025 10:38"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Operação bem sucedida.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/motoristaResponseList"
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
      "motoristaResponseList": {
        "type": "object",
        "properties": {
          "motoristas": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/motorista"
            }
          },
          "pagination": {
            "$ref": "#/components/schemas/pagination"
          }
        }
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
      },
      "pagination": {
        "type": "object",
        "properties": {
          "page": {
            "type": "string",
            "example": "0"
          },
          "offset": {
            "type": "string",
            "example": "0"
          },
          "total": {
            "type": "string",
            "example": "14"
          },
          "hasMore": {
            "type": "boolean",
            "example": false
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
