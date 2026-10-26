---
id: "https://developer.sankhya.com.br/reference/get_v1-financeiros-moedas-codigomoeda"
titulo: "Moeda Específica"
url: "https://developer.sankhya.com.br/reference/get_v1-financeiros-moedas-codigomoeda"
atualizado_em: "2026-05-27T21:06:58.000Z"
---

# Moeda Específica

Retorna uma Moeda específica com base no parâmetro enviado na requisição.

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
      "name": "Financeiros Cadastros",
      "description": "Breve descrição sobre o respectivo contexto"
    }
  ],
  "paths": {
    "/v1/financeiros/moedas/{codigoMoeda}": {
      "get": {
        "tags": [
          "Financeiros Cadastros"
        ],
        "summary": "Moeda Específica",
        "description": "Retorna uma Moeda específica com base no parâmetro enviado na requisição.",
        "parameters": [
          {
            "name": "codigoMoeda",
            "in": "path",
            "required": true,
            "schema": {
              "type": "integer",
              "default": 0
            },
            "description": "Código da Moeda para retorno"
          }
        ],
        "responses": {
          "200": {
            "description": "Dados da Moeda retornados com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Moeda"
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
        },
        "security": [
          {
            "Bearer": [
              "write:financeiro",
              "read:financeiro"
            ]
          }
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "Moeda": {
        "type": "object",
        "properties": {
          "codigoMoeda": {
            "type": "integer",
            "description": "Código da moeda.",
            "example": 840
          },
          "nome": {
            "type": "string",
            "description": "Nome da moeda.",
            "example": "Dólar Americano"
          },
          "codigoTabelaInternacional": {
            "type": "integer",
            "description": "Código da tabela internacional.",
            "example": 1
          },
          "codigoTabelaBCB": {
            "type": "integer",
            "description": "Código da tabela BCB.",
            "example": 178
          },
          "tipoAcumulo": {
            "type": "integer",
            "description": "Tipo do acúmulo. Valoes aceitos: \n  - 1 - Simples\n  - 2 - Composto\n",
            "enum": [
              1,
              2
            ],
            "example": 1
          },
          "tipoTaxa": {
            "type": "integer",
            "description": "Tipo de taxa. Valoes aceitos: \n  - 1 - Venda\n  - 2 - Compra\n",
            "enum": [
              1,
              2
            ],
            "example": 1
          },
          "tipoMoeda": {
            "type": "integer",
            "description": "Tipo da moeda. Valoes aceitos: \n  - 1 - Valor\n  - 2 - Índice\n",
            "enum": [
              1,
              2
            ],
            "example": 1
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
