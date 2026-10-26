---
id: "https://developer.sankhya.com.br/reference/get_v1-grupos-produto"
titulo: "Lista de Grupos de Produto"
url: "https://developer.sankhya.com.br/reference/get_v1-grupos-produto"
atualizado_em: "2026-05-13T12:41:23.000Z"
---

# Lista de Grupos de Produto

Retorna uma lista de Grupos de Produto, com paginação, cadastradas no SankhyaOM.

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
      "name": "Produtos",
      "description": "Cadastros Relacionados a Produtos"
    }
  ],
  "paths": {
    "/v1/grupos-produto": {
      "get": {
        "tags": [
          "Produtos"
        ],
        "summary": "Lista de Grupos de Produto",
        "description": "Retorna uma lista de Grupos de Produto, com paginação, cadastradas no SankhyaOM.",
        "parameters": [
          {
            "name": "page",
            "in": "query",
            "schema": {
              "type": "integer",
              "default": 0
            },
            "description": "Número da página, iniciando sempre por ZERO (0)."
          },
          {
            "name": "modifiedSince",
            "in": "query",
            "schema": {
              "type": "string",
              "example": "07/10/2025 10:38"
            },
            "description": "Data e hora da última modificação. Quando esse parâmetro é enviado, o serviço retorna apenas os registros que foram modificados a partir da data e hora informadas. Vale ressaltar que este recurso é condicionada a utilização do [Log de Alterações no SankhyaOm](https://developer.sankhya.com.br/reference/get_logalteracoestabelas) no ambiente do cliente. O formato deve ser o seguinte: DD/MM/AAAA HH:MM"
          }
        ],
        "responses": {
          "200": {
            "description": "Lista de Grupos de Produto retornada com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "grupos": {
                      "type": "array",
                      "items": {
                        "$ref": "#/components/schemas/GrupoProduto"
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
      "GrupoProduto": {
        "type": "object",
        "properties": {
          "codigoGrupoProduto": {
            "type": "integer",
            "example": 101,
            "description": "Código identificador do grupo de produto."
          },
          "nome": {
            "type": "string",
            "example": "Eletrônicos",
            "description": "Descrição do grupo de produto."
          },
          "codigoGrupoProdutoPai": {
            "type": "integer",
            "example": 100,
            "description": "Código do grupo de produto pai."
          },
          "grau": {
            "type": "integer",
            "example": 2,
            "description": "Grau do grupo na hierarquia."
          },
          "grupoIcms": {
            "type": "integer",
            "example": 5,
            "description": "Código do grupo de ICMS associado."
          },
          "analitico": {
            "type": "boolean",
            "description": "Indica se o grupo é analítico.",
            "example": true
          },
          "ativo": {
            "type": "boolean",
            "description": "Indica se o grupo está ativo.",
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
