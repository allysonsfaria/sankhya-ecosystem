---
id: "https://developer.sankhya.com.br/reference/get_v1-cidades-codigocidade"
titulo: "Cidade específica"
url: "https://developer.sankhya.com.br/reference/get_v1-cidades-codigocidade"
atualizado_em: "2026-05-13T12:41:23.000Z"
---

# Cidade específica

Retorna uma Cidade específica com base no parâmetro enviado na requisição.

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
    "/v1/cidades/{codigoCidade}": {
      "get": {
        "tags": [
          "Cadastros Básicos"
        ],
        "summary": "Cidade específica",
        "description": "Retorna uma Cidade específica com base no parâmetro enviado na requisição.",
        "parameters": [
          {
            "name": "codigoCidade",
            "in": "path",
            "required": true,
            "schema": {
              "type": "integer",
              "default": 0
            },
            "description": "Código da Cidade para retorno"
          }
        ],
        "responses": {
          "200": {
            "description": "Dados da Cidade retornado com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/CidadesCidade"
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
      "CidadesCidade": {
        "type": "object",
        "properties": {
          "codigoCidade": {
            "type": "integer",
            "description": "Código identificador único da cidade no sistema.",
            "example": 123
          },
          "nome": {
            "type": "string",
            "description": "Nome da cidade.",
            "example": "Uberlândia"
          },
          "uf": {
            "type": "string",
            "description": "Sigla da Unidade Federativa (UF) da cidade.",
            "example": "MG"
          },
          "codigoRegiao": {
            "type": "integer",
            "description": "Código da região da cidade pertence.",
            "example": 101
          },
          "nomeRegiao": {
            "type": "string",
            "description": "Nome da região da cidade pertence.",
            "example": "Triângulo Mineiro"
          },
          "nomeCorreio": {
            "type": "string",
            "description": "Nome da cidade conforme registro nos correios.",
            "example": "Uberlândia"
          },
          "codigoMunicipioFiscal": {
            "type": "integer",
            "description": "Código do município de domicílio fiscal relacionado à cidade.",
            "example": 456
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
