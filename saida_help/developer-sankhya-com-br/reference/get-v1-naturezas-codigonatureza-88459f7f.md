---
id: "https://developer.sankhya.com.br/reference/get_v1-naturezas-codigonatureza"
titulo: "Natureza Específica"
url: "https://developer.sankhya.com.br/reference/get_v1-naturezas-codigonatureza"
atualizado_em: "2026-05-27T21:06:58.000Z"
---

# Natureza Específica

Retorna uma Natureza específica com base no parâmetro enviado na requisição.

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
    "/v1/naturezas/{codigoNatureza}": {
      "get": {
        "tags": [
          "Cadastros Básicos"
        ],
        "summary": "Natureza Específica",
        "description": "Retorna uma Natureza específica com base no parâmetro enviado na requisição.",
        "parameters": [
          {
            "name": "codigoNatureza",
            "in": "path",
            "required": true,
            "schema": {
              "type": "integer",
              "default": 0
            },
            "description": "Código da Natureza para retorno"
          }
        ],
        "responses": {
          "200": {
            "description": "Dados da Natureza retornados com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Natureza"
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
      "Natureza": {
        "type": "object",
        "properties": {
          "codigoNatureza": {
            "type": "integer",
            "description": "Código da Natureza",
            "example": 1
          },
          "nome": {
            "type": "string",
            "description": "Nome da Natureza",
            "example": "Natureza Exemplo"
          },
          "analitica": {
            "type": "boolean",
            "description": "Indica se a Natureza é analítica",
            "example": true
          },
          "grau": {
            "type": "integer",
            "description": "Grau da Natureza",
            "example": 1
          },
          "ativo": {
            "type": "boolean",
            "description": "Indica se a Natureza está ativa",
            "example": true
          },
          "codigoCentroResultado": {
            "type": "integer",
            "description": "Código do Centro de Resultado",
            "example": 1001
          },
          "codigoNaturezaPai": {
            "type": "integer",
            "description": "Código da Natureza Pai",
            "example": 5001
          },
          "tipoNatureza": {
            "type": "integer",
            "enum": [
              1,
              2
            ],
            "description": "Tipo de Natureza (Receita ou Despesa)\n   - 1: Receita\n   - 2: Despesa\n",
            "example": 1
          }
        },
        "required": [
          "codigoNatureza",
          "nome",
          "ativa"
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
