---
id: "https://developer.sankhya.com.br/reference/get_v1-centros-resultado"
titulo: "Lista de Centros de Resultado"
url: "https://developer.sankhya.com.br/reference/get_v1-centros-resultado"
atualizado_em: "2026-05-27T21:06:58.000Z"
---

# Lista de Centros de Resultado

Retorna a lista de Centro de Resultado, com paginação, cadastradas no SankhyaOM.

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
    "/v1/centros-resultado": {
      "get": {
        "tags": [
          "Cadastros Básicos"
        ],
        "summary": "Lista de Centros de Resultado",
        "description": "Retorna a lista de Centro de Resultado, com paginação, cadastradas no SankhyaOM.",
        "parameters": [
          {
            "name": "page",
            "in": "query",
            "schema": {
              "type": "integer",
              "default": 1
            },
            "description": "Número da página para paginação dos resultados. O valor mínimo é 1. Quando não informado, será considerada a página 1."
          }
        ],
        "responses": {
          "200": {
            "description": "Lista de centros de resultado retornada com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/CentroResultado"
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
      "CentroResultado": {
        "type": "object",
        "properties": {
          "codigoCentroResultado": {
            "type": "integer",
            "description": "Código do Centro de Resultado",
            "example": 1
          },
          "nome": {
            "type": "string",
            "description": "Nome do Centro de Resultado",
            "example": "Centro de Resultado Exemplo"
          },
          "analitico": {
            "type": "boolean",
            "description": "Indica se o Centro de Resultado é analítico",
            "example": true
          },
          "grau": {
            "type": "integer",
            "description": "Grau do Centro de Resultado",
            "example": 3
          },
          "ativo": {
            "type": "boolean",
            "description": "Indica se o Centro de Resultado está ativo",
            "example": true
          },
          "codigoCentroResultadoPai": {
            "type": "integer",
            "description": "Código do Centro de Resultado Pai",
            "example": 2
          },
          "codigoTabelaPreco": {
            "type": "integer",
            "description": "Código da Tabela de Preço",
            "example": 789
          },
          "nomeTabelaPreco": {
            "type": "string",
            "description": "Nome da Tabela de Preço",
            "example": "Atacado (B2B)"
          }
        },
        "required": [
          "codigoCentroResultado",
          "nome",
          "ativo"
        ]
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
