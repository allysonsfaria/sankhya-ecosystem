---
id: "https://developer.sankhya.com.br/reference/get_v1-pessoal-sindicatos-codigosindicato"
titulo: "Sindicato específico"
url: "https://developer.sankhya.com.br/reference/get_v1-pessoal-sindicatos-codigosindicato"
atualizado_em: "2026-05-27T21:06:58.000Z"
---

# Sindicato específico

Retorna um Sindicato específico com base no parâmetro enviado na requisição. 

 Versão mínima do módulo pessoal: **5.53.0**

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
      "name": "HCM Cadastros",
      "description": "Cadastros Básicos relacionados a Pessoal no SankhyaOm"
    }
  ],
  "paths": {
    "/v1/pessoal/sindicatos/{codigoSindicato}": {
      "get": {
        "tags": [
          "HCM Cadastros"
        ],
        "summary": "Sindicato específico",
        "description": "Retorna um Sindicato específico com base no parâmetro enviado na requisição. \n\n Versão mínima do módulo pessoal: **5.53.0**",
        "parameters": [
          {
            "name": "codigoSindicato",
            "in": "path",
            "required": true,
            "schema": {
              "type": "integer",
              "default": 0
            },
            "description": "Código do Sindicato para retorno"
          }
        ],
        "responses": {
          "200": {
            "description": "Dados do Sindicato retornados com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SindicatoSindicato"
                }
              }
            }
          },
          "400": {
            "description": "Requisição inválida.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Sindicatoretorno400"
                }
              }
            }
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
      "Sindicatoretorno400": {
        "type": "object",
        "properties": {
          "statusCode": {
            "type": "integer",
            "format": "int32",
            "example": 400
          },
          "error": {
            "type": "object",
            "properties": {
              "code": {
                "type": "string",
                "example": "BAD_REQUEST"
              },
              "message": {
                "type": "string",
                "example": "Ocorreu algum erro inesperado!"
              },
              "details": {
                "type": "string",
                "example": "O parâmetro de paginação 'pageSize' deve ser um número inteiro positivo."
              }
            }
          }
        }
      },
      "SindicatoSindicato": {
        "type": "object",
        "properties": {
          "codigoSindicato": {
            "type": "integer",
            "description": "Código do sindicato.",
            "example": 101
          },
          "nome": {
            "type": "string",
            "description": "Nome do Sindicato.",
            "example": "Sindicato dos Desenvolvedores"
          },
          "cnpj": {
            "type": "string",
            "description": "CNPJ do sindicato (apenas números).",
            "example": "22235048000111"
          },
          "codigoSindical": {
            "type": "string",
            "description": "Código sindical segundo cadastro do Ministério do Trabalho (MTE).",
            "example": "101"
          },
          "regraCalculo": {
            "type": "object",
            "description": "Informações da regra de cálculo atribuída ao sindicato.",
            "properties": {
              "codigo": {
                "type": "integer",
                "description": "Código da regra de cálculo atribuída ao sindicato.",
                "example": 252515
              },
              "nome": {
                "type": "string",
                "description": "Nome da regra de cálculo atribuída ao sindicato.",
                "example": "REGRA 1."
              }
            }
          },
          "dataAlteracao": {
            "type": "string",
            "description": "Data da última alteração.",
            "example": "10/03/2022 16:03:12"
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
