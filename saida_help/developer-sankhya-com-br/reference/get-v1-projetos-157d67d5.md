---
id: "https://developer.sankhya.com.br/reference/get_v1-projetos"
titulo: "Lista de Projetos"
url: "https://developer.sankhya.com.br/reference/get_v1-projetos"
atualizado_em: "2026-05-27T21:06:58.000Z"
---

# Lista de Projetos

Retorna a lista de Projetos, com paginação, cadastradas no SankhyaOM.


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
    "/v1/projetos": {
      "get": {
        "tags": [
          "Cadastros Básicos"
        ],
        "summary": "Lista de Projetos",
        "description": "Retorna a lista de Projetos, com paginação, cadastradas no SankhyaOM.\n",
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
            "description": "Lista de projetos retornada com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/Projeto"
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
      "Projeto": {
        "type": "object",
        "properties": {
          "codigoProjeto": {
            "type": "integer",
            "description": "Código do Projeto",
            "example": 1
          },
          "abreviacao": {
            "type": "string",
            "description": "Abreviação do Projeto",
            "example": "PROJ-001"
          },
          "descricao": {
            "type": "string",
            "description": "Identificação do Projeto",
            "example": "Projeto de Desenvolvimento"
          },
          "analitico": {
            "type": "boolean",
            "description": "Indica se o Projeto é analítico",
            "example": true
          },
          "grau": {
            "type": "integer",
            "description": "Grau do Projeto",
            "example": 3
          },
          "ativo": {
            "type": "boolean",
            "description": "Indica se o Projeto está ativo",
            "example": true
          },
          "codigoProjetoPai": {
            "type": "integer",
            "description": "Código do Projeto Pai",
            "example": 5001
          }
        },
        "required": [
          "codigoProjeto",
          "abreviacao",
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
