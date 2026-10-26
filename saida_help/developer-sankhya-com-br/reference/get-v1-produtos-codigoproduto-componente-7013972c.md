---
id: "https://developer.sankhya.com.br/reference/get_v1-produtos-codigoproduto-componentes"
titulo: "Componentes de um respectivo Produto"
url: "https://developer.sankhya.com.br/reference/get_v1-produtos-codigoproduto-componentes"
atualizado_em: "2026-05-13T12:41:23.000Z"
---

# Componentes de um respectivo Produto

Retorna uma lista de Componentes que compõe um respectivo Produto, cadastradas no SankhyaOM.

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
    "/v1/produtos/{codigoProduto}/componentes": {
      "get": {
        "tags": [
          "Produtos"
        ],
        "summary": "Componentes de um respectivo Produto",
        "description": "Retorna uma lista de Componentes que compõe um respectivo Produto, cadastradas no SankhyaOM.",
        "parameters": [
          {
            "name": "codigoProduto",
            "in": "path",
            "required": true,
            "schema": {
              "type": "integer",
              "default": 0
            },
            "description": "Código do Produto para o contexto de componentes do produto."
          },
          {
            "name": "page",
            "in": "query",
            "schema": {
              "type": "integer",
              "default": 0
            },
            "description": "Número da página, iniciando sempre por ZERO (0)."
          }
        ],
        "responses": {
          "200": {
            "description": "Lista de Componentes de um respectivo Produto retornada com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "componentes": {
                      "type": "array",
                      "items": {
                        "$ref": "#/components/schemas/Componente"
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
      "Componente": {
        "type": "object",
        "properties": {
          "codigoProduto": {
            "type": "integer",
            "example": 123,
            "description": "Código do produto componente utilizado para compor o produto principal."
          },
          "unidade": {
            "type": "string",
            "example": "UN",
            "description": "Código da unidade de medida do componente (ex: UN para unidade, KG para quilograma)."
          },
          "quantidade": {
            "type": "number",
            "format": "float",
            "example": 1.5,
            "description": "Quantidade da componentes utilizado para compor o produto principal."
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
