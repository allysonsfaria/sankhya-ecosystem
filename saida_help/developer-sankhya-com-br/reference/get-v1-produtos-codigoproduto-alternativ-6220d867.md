---
id: "https://developer.sankhya.com.br/reference/get_v1-produtos-codigoproduto-alternativos"
titulo: "Produtos Alternativos de um respectivo Produto"
url: "https://developer.sankhya.com.br/reference/get_v1-produtos-codigoproduto-alternativos"
atualizado_em: "2026-05-13T12:41:23.000Z"
---

# Produtos Alternativos de um respectivo Produto

Retorna uma lista de Produtos Alternativos de um respectivo Produto, cadastradas no SankhyaOM.

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
    "/v1/produtos/{codigoProduto}/alternativos": {
      "get": {
        "tags": [
          "Produtos"
        ],
        "summary": "Produtos Alternativos de um respectivo Produto",
        "description": "Retorna uma lista de Produtos Alternativos de um respectivo Produto, cadastradas no SankhyaOM.",
        "parameters": [
          {
            "name": "codigoProduto",
            "in": "path",
            "required": true,
            "schema": {
              "type": "integer",
              "default": 0
            },
            "description": "Código do Produto para o contexto de Produtos Alternativos."
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
            "description": "Lista de Produtos Alternativos de um respectivo Produto retornada com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "produtos": {
                      "type": "array",
                      "items": {
                        "$ref": "#/components/schemas/ProdutoAlternativo"
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
      "ProdutoAlternativo": {
        "type": "object",
        "properties": {
          "codigoProduto": {
            "type": "integer",
            "description": "Código do produto alternativo.",
            "example": 2001
          },
          "ordemPrioridade": {
            "type": "integer",
            "description": "Ordem de prioridade do produto alternativo na substituição.",
            "example": 1
          },
          "quantidade": {
            "type": "integer",
            "description": "Quantidade que o produto alternativo substitui do produto principal.",
            "example": 10
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
