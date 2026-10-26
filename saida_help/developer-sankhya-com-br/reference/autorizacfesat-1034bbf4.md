---
id: "https://developer.sankhya.com.br/reference/autorizacfesat"
titulo: "Autoriza Nota Fiscal de Consumidor eletronico que está em contigência"
url: "https://developer.sankhya.com.br/reference/autorizacfesat"
atualizado_em: "2026-05-27T21:06:58.000Z"
---

# Autoriza Nota Fiscal de Consumidor eletronico que está em contigência

Autoriza um Nota Fiscal de Consumidor eletronico modelo 59 emitido em um PDV externo que está armazenado no SankhyaOm. É importante ressaltar que a NFC-e deve ter sido previamente emitida em modo contingência (tipoEmissao = 9).

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
      "name": "Vendas NFC-e",
      "description": "Nota Fiscal do Consumidor eletrônico (NFC-e)"
    }
  ],
  "paths": {
    "/v1/vendas/nfce/autorizar": {
      "post": {
        "tags": [
          "Vendas NFC-e"
        ],
        "summary": "Autoriza Nota Fiscal de Consumidor eletronico que está em contigência",
        "description": "Autoriza um Nota Fiscal de Consumidor eletronico modelo 59 emitido em um PDV externo que está armazenado no SankhyaOm. É importante ressaltar que a NFC-e deve ter sido previamente emitida em modo contingência (tipoEmissao = 9).",
        "operationId": "autorizaCfeSat",
        "requestBody": {
          "description": "Autoriza Nota Fiscal de Consumidor eletronico que está em contigência no SankhyaOm",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/autorizarMovimento"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "Operação bem sucedida",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/retornoMovimento"
                }
              }
            }
          },
          "400": {
            "description": "Informações Inválidas. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/retorno400"
                }
              }
            }
          },
          "401": {
            "description": "Não autenticado. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/retorno40X_50X"
                }
              }
            }
          },
          "403": {
            "description": "Autenticação inválida. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/retorno40X_50X"
                }
              }
            }
          },
          "404": {
            "description": "Dados não encontrados. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/retorno404"
                }
              }
            }
          },
          "500": {
            "description": "Erro interno no servidor. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/retorno40X_50X"
                }
              }
            }
          },
          "501": {
            "description": "Não implementado. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/retorno40X_50X"
                }
              }
            }
          },
          "502": {
            "description": "Retorno inválido do servidor. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/retorno40X_50X"
                }
              }
            }
          },
          "503": {
            "description": "Serviço indisponível no momento. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/retorno40X_50X"
                }
              }
            }
          },
          "504": {
            "description": "Tempo de execução excedido. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/retorno40X_50X"
                }
              }
            }
          }
        },
        "security": [
          {
            "Bearer": [
              "write:vendas/cfe-sat",
              "read:vendas/cfe-sat"
            ]
          }
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "autorizarMovimento": {
        "type": "object",
        "description": "Contrato para autorizar momentos fiscais enviados para o SankhyaOm com \"tipoEmissao\" em contingência. Será autorizado, apenas movimentos existentes no SankhyaOm e que estejam com \"tipoEmissao\" diferente de \"Emissão normal\" (1).",
        "required": [
          "chaveNfe",
          "protocolo",
          "data",
          "hora",
          "xml"
        ],
        "properties": {
          "chaveNfe": {
            "type": "string",
            "example": "26230507381608000152650030003505701343991111"
          },
          "protocolo": {
            "type": "string",
            "description": "Protocolodo de autorização do documento.",
            "example": "326230259108944"
          },
          "data": {
            "type": "string",
            "description": "Data do protocolo de autorização do documento",
            "example": "30/05/2024"
          },
          "hora": {
            "type": "string",
            "description": "Hora do protocolo de autorização do documento",
            "example": "07:34"
          },
          "desvincularCnpjCpf": {
            "type": "boolean",
            "description": "Utilizado para eliminar o CPF ou CNPJ enviado no movimento fiscal anteriormente. Isso é necessário quando o CPF ou CNPJ possui alguma irregularidade que impede a aprovação do documento fiscal na receita federal. Com isso, os dados no SankhyaOm ficam em conformidade com o documento fiscal aprovado pela receita.",
            "example": true
          },
          "xml": {
            "type": "string",
            "description": "XML do movimento codificado em padrão base64",
            "example": "PHhtbD54bWwgY29tcGxldG8gYXF1aTwveG1sPg=="
          }
        }
      },
      "retornoMovimento": {
        "type": "object",
        "properties": {
          "codigo": {
            "type": "integer",
            "format": "int32"
          },
          "tipo": {
            "type": "string"
          },
          "mensagem": {
            "type": "string"
          }
        }
      },
      "retorno400": {
        "type": "object",
        "properties": {
          "statusCode": {
            "type": "integer",
            "format": "int32",
            "example": 400
          },
          "error": {
            "type": "string"
          },
          "mensagem": {
            "$ref": "#/components/schemas/retornoErro"
          }
        }
      },
      "retorno40X_50X": {
        "type": "object",
        "properties": {
          "fieldSet": {
            "type": "string"
          },
          "paginate": {
            "type": "string"
          },
          "mensagem": {
            "$ref": "#/components/schemas/error"
          }
        }
      },
      "retorno404": {
        "type": "object",
        "properties": {
          "statusCode": {
            "type": "integer",
            "format": "int32",
            "example": 404
          },
          "error": {
            "$ref": "#/components/schemas/Requisicao_de_Servicos_TomadosretornoErro"
          }
        }
      },
      "error": {
        "type": "object",
        "properties": {
          "codigo": {
            "type": "string"
          },
          "descricao": {
            "type": "string"
          }
        }
      },
      "retornoErro": {
        "type": "object",
        "properties": {
          "code": {
            "type": "string",
            "example": "INVALID_REQUEST"
          },
          "message": {
            "type": "string",
            "example": "Ocorreu algum erro inesperado!"
          },
          "details": {
            "type": "string",
            "example": "O produto [9554] enviado não existe."
          },
          "help": {
            "type": "string",
            "example": "https://api.sankhya.com.br/api/docs/?ERROR_CODE=INVALID_REQUEST"
          }
        }
      },
      "Requisicao_de_Servicos_TomadosretornoErro": {
        "type": "object",
        "properties": {
          "code": {
            "type": "string",
            "example": "INVALID_REQUEST"
          },
          "message": {
            "type": "string",
            "example": "Ocorreu algum erro inesperado!"
          },
          "details": {
            "type": "string",
            "example": "O bairro [6] enviado não existe."
          },
          "help": {
            "type": "string",
            "example": "https://api.sankhya.com.br/api/docs/?ERROR_CODE=INVALID_REQUEST"
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
