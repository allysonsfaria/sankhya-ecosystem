---
id: "https://developer.sankhya.com.br/reference/gettransportadoras"
titulo: "Retornar lista de transportadoras"
url: "https://developer.sankhya.com.br/reference/gettransportadoras"
atualizado_em: "2026-05-13T12:41:23.000Z"
---

# Retornar lista de transportadoras

Permite acessar a lista de transportadoras cadastradas no ERP.

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
      "get": {
        "tags": [
          "Logística"
        ],
        "summary": "Retornar lista de transportadoras",
        "description": "Permite acessar a lista de transportadoras cadastradas no ERP.",
        "operationId": "getTransportadoras",
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
              "example": "22/10/2025 10:45"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Operação bem sucedida.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/transportadoraResponseList"
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
      },
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
      "transportadoraResponseList": {
        "type": "object",
        "properties": {
          "transportadoras": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/transportadora"
            }
          },
          "pagination": {
            "$ref": "#/components/schemas/pagination"
          }
        }
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
