---
id: "https://developer.sankhya.com.br/reference/put_v1-pessoal-funcionarios-codigofuncionario-empresa-codigoempresa-recibos-esocial"
titulo: "Atualiza recibos eSocial SST do Funcionário"
url: "https://developer.sankhya.com.br/reference/put_v1-pessoal-funcionarios-codigofuncionario-empresa-codigoempresa-recibos-esocial"
atualizado_em: "2026-05-13T12:41:23.000Z"
---

# Atualiza recibos eSocial SST do Funcionário

Recebe, valida e persiste recibos e datas dos eventos SST do eSocial (S-2210, S-2220, S-2221, S-2240) para um funcionário/empresa.

Observações:
- Cada evento enviado deve conter os três campos: recibo, dataEvento e dataEnvio.
- Apenas os eventos presentes no corpo serão processados.
 

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
      "name": "HCM Funcionários",
      "description": "Cadastros relacionados a Funcionários no SankhyaOm"
    }
  ],
  "paths": {
    "/v1/pessoal/funcionarios/{codigoFuncionario}/empresa/{codigoEmpresa}/recibos-esocial": {
      "put": {
        "tags": [
          "HCM Funcionários"
        ],
        "summary": "Atualiza recibos eSocial SST do Funcionário",
        "description": "Recebe, valida e persiste recibos e datas dos eventos SST do eSocial (S-2210, S-2220, S-2221, S-2240) para um funcionário/empresa.\n\nObservações:\n- Cada evento enviado deve conter os três campos: recibo, dataEvento e dataEnvio.\n- Apenas os eventos presentes no corpo serão processados.\n ",
        "parameters": [
          {
            "name": "codigoFuncionario",
            "in": "path",
            "required": true,
            "schema": {
              "type": "integer"
            },
            "description": "Código do Funcionário"
          },
          {
            "name": "codigoEmpresa",
            "in": "path",
            "required": true,
            "schema": {
              "type": "integer"
            },
            "description": "Código da Empresa"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/RecibosEsocialSSTPayload"
              },
              "examples": {
                "exemploCompleto": {
                  "summary": "Quatro eventos (completos)",
                  "value": {
                    "evento2210": {
                      "recibo": "1.1.1234567890123456789",
                      "dataEvento": "2025-10-15T14:00:00Z",
                      "dataEnvio": "2025-10-15T14:05:00Z"
                    },
                    "evento2220": {
                      "recibo": "1.1.1234567890123456790",
                      "dataEvento": "2025-10-16T09:30:00Z",
                      "dataEnvio": "2025-10-16T09:35:00Z"
                    },
                    "evento2221": {
                      "recibo": "1.1.1234567890123456791",
                      "dataEvento": "2025-10-17T11:10:00Z",
                      "dataEnvio": "2025-10-17T11:12:00Z"
                    },
                    "evento2240": {
                      "recibo": "1.1.1234567890123456792",
                      "dataEvento": "2025-10-19T16:45:00Z",
                      "dataEnvio": "2025-10-20T08:00:00Z"
                    }
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Atualização realizada com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "status": {
                      "type": "string",
                      "example": "OK"
                    }
                  }
                },
                "examples": {
                  "sucesso": {
                    "value": {
                      "status": "OK"
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Requisição inválida (evento incompleto ou formato incorreto).",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/RecibosEsocialSSTretorno400"
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
            "description": "Funcionário/Empresa não encontrado."
          },
          "500": {
            "description": "Erro interno do servidor."
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "RecibosEsocialSSTretorno400": {
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
                "example": "O campo obrigatório 'codigoFuncionario' está ausente na requisição."
              }
            }
          }
        }
      },
      "EventoSST": {
        "type": "object",
        "properties": {
          "recibo": {
            "type": "string",
            "maxLength": 23,
            "description": "Número do recibo eSocial (até 23 caracteres).",
            "example": "1.1.1234567890123456789"
          },
          "dataEvento": {
            "type": "string",
            "format": "date-time",
            "description": "Data e hora do evento (ISO-8601).",
            "example": "2025-10-15T14:00:00Z"
          },
          "dataEnvio": {
            "type": "string",
            "format": "date-time",
            "description": "Data e hora do envio (ISO-8601).",
            "example": "2025-10-15T14:05:00Z"
          }
        },
        "required": [
          "recibo",
          "dataEvento",
          "dataEnvio"
        ]
      },
      "RecibosEsocialSSTPayload": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "evento2210": {
            "$ref": "#/components/schemas/EventoSST"
          },
          "evento2220": {
            "$ref": "#/components/schemas/EventoSST"
          },
          "evento2221": {
            "$ref": "#/components/schemas/EventoSST"
          },
          "evento2240": {
            "$ref": "#/components/schemas/EventoSST"
          }
        },
        "description": "Objeto com os eventos SST a serem atualizados. Cada chave é opcional; quando presente, deve conter os três campos obrigatórios."
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
