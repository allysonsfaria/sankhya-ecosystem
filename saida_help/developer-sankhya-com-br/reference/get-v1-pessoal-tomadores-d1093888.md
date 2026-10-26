---
id: "https://developer.sankhya.com.br/reference/get_v1-pessoal-tomadores"
titulo: "Lista de Tomadores"
url: "https://developer.sankhya.com.br/reference/get_v1-pessoal-tomadores"
atualizado_em: "2026-05-27T21:06:58.000Z"
---

# Lista de Tomadores

Retorna uma lista de Tomadores, com paginação, cadastradas no SankhyaOM.  

 Versão mínima do módulo pessoal: **5.55.0**

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
    "/v1/pessoal/tomadores": {
      "get": {
        "tags": [
          "HCM Cadastros"
        ],
        "summary": "Lista de Tomadores",
        "description": "Retorna uma lista de Tomadores, com paginação, cadastradas no SankhyaOM.  \n\n Versão mínima do módulo pessoal: **5.55.0**",
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
              "type": "string"
            },
            "description": "Data hora da ultima modificação. Quando este parametro é enviado, o serviço retorana apenas registros que tiveram modificação deste da data/hora enviada. Vale ressaltar que este recurso é condicionada a utilização do [Log de Alterações no SankhyaOm](https://developer.sankhya.com.br/reference/get_logalteracoestabelas) no ambiente do cliente. O formato deve ser o seguinte: AAAA-MM-DDTHH:MM:SS"
          },
          {
            "name": "dataInicio",
            "in": "query",
            "schema": {
              "type": "string",
              "default": ""
            },
            "description": "Data inicial limite para o tomador. Exemplo: 01-01-2025"
          },
          {
            "name": "dataFim",
            "in": "query",
            "schema": {
              "type": "string",
              "default": ""
            },
            "description": "Data final limite para o tomador. Exemplo: 01-12-2025"
          }
        ],
        "responses": {
          "200": {
            "description": "Lista de Tomadores retornada com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/Tomador"
                  }
                }
              }
            }
          },
          "400": {
            "description": "Requisição inválida.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Tomadorretorno400"
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
      "Tomadorretorno400": {
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
                "example": "O parâmetro 'codigoEmpresa' é obrigatório quando 'codigoFuncionario' é informado."
              }
            }
          }
        }
      },
      "Tomador": {
        "type": "object",
        "properties": {
          "empresa": {
            "type": "object",
            "description": "Informações da empresa.",
            "properties": {
              "codigo": {
                "type": "integer",
                "description": "Código da empresa.",
                "example": 252515
              },
              "nome": {
                "type": "string",
                "description": "Nome da empresa.",
                "example": "SANKHYA."
              }
            }
          },
          "funcionario": {
            "type": "object",
            "description": "Informações do funcionário.",
            "properties": {
              "codigo": {
                "type": "integer",
                "description": "Código do funcionário.",
                "example": 252515
              },
              "nome": {
                "type": "string",
                "description": "Nome do funcionário.",
                "example": "Pedro José Souza."
              }
            }
          },
          "parceiro": {
            "type": "object",
            "description": "Informações do Parceiro tomador de serviços.",
            "properties": {
              "codigo": {
                "type": "integer",
                "description": "Código do Parceiro tomador de serviços.",
                "example": 252515
              },
              "nome": {
                "type": "string",
                "description": "Nome do Parceiro tomador de serviços.",
                "example": "Pedro José Souza."
              }
            }
          },
          "dataInicio": {
            "type": "string",
            "description": "Data início do vínculo.",
            "example": "10/03/2025 00:00:00"
          },
          "dataFim": {
            "type": "string",
            "description": "Data final do vínculo.",
            "example": "10/03/2025 00:00:00"
          },
          "observacao": {
            "type": "string",
            "description": "Observação inserida no lançamento de tomador.",
            "example": "Nada a observar."
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
