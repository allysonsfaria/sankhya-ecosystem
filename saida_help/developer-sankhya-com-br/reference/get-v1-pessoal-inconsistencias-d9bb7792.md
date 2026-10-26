---
id: "https://developer.sankhya.com.br/reference/get_v1-pessoal-inconsistencias"
titulo: "Consulta Inconsistências de integração"
url: "https://developer.sankhya.com.br/reference/get_v1-pessoal-inconsistencias"
atualizado_em: "2026-05-13T12:41:23.000Z"
---

# Consulta Inconsistências de integração

Retorna a lista de Inconsistências identificadas nas rotinas de integração HCM.

A resposta inclui o array `results` com as Inconsistências encontradas.

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
      "name": "HCM Integrações",
      "description": "Endpoints destinados ao consumo das integrações HCM."
    }
  ],
  "paths": {
    "/v1/pessoal/inconsistencias": {
      "get": {
        "tags": [
          "HCM Integrações"
        ],
        "summary": "Consulta Inconsistências de integração",
        "description": "Retorna a lista de Inconsistências identificadas nas rotinas de integração HCM.\n\nA resposta inclui o array `results` com as Inconsistências encontradas.",
        "parameters": [
          {
            "name": "tipoInconsistencia",
            "in": "query",
            "schema": {
              "type": "string"
            },
            "description": "Filtra os tipos de Inconsistência desejados. Informe múltiplos valores separados por vírgula. Valores aceitos: `multiplosLideres`, `multiplosUsuarios`."
          }
        ],
        "responses": {
          "200": {
            "description": "Lista de Inconsistências retornada com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/InconsistenciaIntegracaoResponse"
                },
                "examples": {
                  "default": {
                    "value": {
                      "results": [
                        {
                          "tipoInconsistencia": "multiplosLideres",
                          "empresa": {
                            "codigo": 1,
                            "nome": "EMPRESA 1"
                          },
                          "funcionario": {
                            "codigo": 1001,
                            "cpf": "95844126041",
                            "nome": "LIDER FUNCIONARIO"
                          }
                        },
                        {
                          "tipoInconsistencia": "multiplosUsuarios",
                          "empresa": {
                            "codigo": 1,
                            "nome": "EMPRESA 1"
                          },
                          "funcionario": {
                            "codigo": 4,
                            "cpf": "27767831671",
                            "nome": "EVA YABUTA CASTELETE"
                          }
                        }
                      ],
                      "pagination": {
                        "page": 0,
                        "offset": 0,
                        "total": 5,
                        "hasMore": false
                      }
                    }
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
                  "$ref": "#/components/schemas/InconsistenciasIntegracaoretorno400"
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
          "503": {
            "description": "Serviço indisponível."
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "InconsistenciasIntegracaoretorno400": {
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
                "example": "O campo 'codigoEmpresa' é obrigatório."
              }
            }
          }
        }
      },
      "InconsistenciaIntegracaoResponse": {
        "type": "object",
        "properties": {
          "results": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/InconsistenciaIntegracao"
            }
          },
          "pagination": {
            "type": "object",
            "description": "Metadados de paginação padrão da EasyAPI.",
            "properties": {
              "page": {
                "type": "integer",
                "description": "Número da página atual.",
                "example": 0
              },
              "offset": {
                "type": "integer",
                "description": "Offset inicial da consulta.",
                "example": 0
              },
              "total": {
                "type": "integer",
                "description": "Total de registros encontrados.",
                "example": 5
              },
              "hasMore": {
                "type": "boolean",
                "description": "Indica se há mais páginas a serem consultadas.",
                "example": false
              }
            }
          }
        }
      },
      "InconsistenciaIntegracao": {
        "type": "object",
        "properties": {
          "tipoInconsistencia": {
            "type": "string",
            "description": "Identifica o tipo de Inconsistência encontrada.",
            "enum": [
              "multiplosLideres",
              "multiplosUsuarios"
            ],
            "example": "multiplosLideres"
          },
          "empresa": {
            "type": "object",
            "properties": {
              "codigo": {
                "type": "integer",
                "description": "Código interno da empresa.",
                "example": 1
              },
              "nome": {
                "type": "string",
                "description": "Razão social ou nome fantasia da empresa.",
                "example": "EMPRESA 1"
              }
            }
          },
          "funcionario": {
            "type": "object",
            "properties": {
              "codigo": {
                "type": "integer",
                "description": "Código do funcionário.",
                "example": 1001
              },
              "cpf": {
                "type": "string",
                "description": "CPF do funcionário.",
                "example": "95844126041"
              },
              "nome": {
                "type": "string",
                "description": "Nome completo do funcionário.",
                "example": "LIDER FUNCIONARIO"
              }
            }
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
