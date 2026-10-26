---
id: "https://developer.sankhya.com.br/reference/get_v1-pessoal-funcionarios-requisicoes-ferias-codigosolicitacao"
titulo: "Buscar detalhes de uma requisição de férias"
url: "https://developer.sankhya.com.br/reference/get_v1-pessoal-funcionarios-requisicoes-ferias-codigosolicitacao"
atualizado_em: "2026-06-30T15:07:56.000Z"
---

# Buscar detalhes de uma requisição de férias

Este endpoint permite buscar os detalhes de uma requisição de férias existente pelo seu código de solicitação, retornado na criação da mesma. 

 Versão mínima do módulo pessoal: **a definir**

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
    "/v1/pessoal/funcionarios/requisicoes-ferias/{codigoSolicitacao}": {
      "get": {
        "summary": "Buscar detalhes de uma requisição de férias",
        "tags": [
          "HCM Cadastros"
        ],
        "description": "Este endpoint permite buscar os detalhes de uma requisição de férias existente pelo seu código de solicitação, retornado na criação da mesma. \n\n Versão mínima do módulo pessoal: **a definir**",
        "parameters": [
          {
            "name": "codigoSolicitacao",
            "in": "path",
            "required": true,
            "description": "ID da requisição de férias, retornado na criação da mesma.",
            "schema": {
              "type": "integer",
              "example": 42
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Detalhes da Requisição de Férias.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/RequisicaoFeriasGetResponse"
                }
              }
            }
          },
          "400": {
            "description": "Informações Inválidas. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Requisicao_de_Feriasretorno400"
                }
              }
            }
          },
          "401": {
            "description": "Não autenticado. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/retorno40X_50X"
                }
              }
            }
          },
          "403": {
            "description": "Autenticação inválida. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/retorno40X_50X"
                }
              }
            }
          },
          "404": {
            "description": "Requisição de Férias não encontrada. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Requisicao_de_Feriasretorno404"
                }
              }
            }
          },
          "500": {
            "description": "Erro interno no servidor. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/retorno40X_50X"
                }
              }
            }
          },
          "501": {
            "description": "Não implementado. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/retorno40X_50X"
                }
              }
            }
          },
          "502": {
            "description": "Retorno inválido do servidor. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/retorno40X_50X"
                }
              }
            }
          },
          "503": {
            "description": "Serviço indisponível no momento. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/retorno40X_50X"
                }
              }
            }
          },
          "504": {
            "description": "Tempo de execução excedido. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
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
              "read:Requisição de férias"
            ]
          }
        ]
      }
    }
  },
  "components": {
    "schemas": {
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
      "RequisicaoFeriasGetResponse": {
        "type": "object",
        "properties": {
          "codigoSolicitacao": {
            "type": "integer",
            "description": "Código (ID) da solicitação de férias.",
            "example": 42
          },
          "codigoEmpresa": {
            "type": "integer",
            "description": "Código da empresa do funcionário.",
            "example": 1
          },
          "codigoFuncionario": {
            "type": "integer",
            "description": "Código do funcionário.",
            "example": 100
          },
          "numeroDaSolicitacao": {
            "type": "integer",
            "description": "Número sequencial da solicitação de férias do funcionário.",
            "example": 3
          },
          "periodoAquisitivo": {
            "type": "object",
            "properties": {
              "dataInicioAquisitivo": {
                "type": "string",
                "description": "Data de início do período aquisitivo. Formato: **dd/MM/yyyy**.",
                "example": "01/03/2024"
              }
            }
          },
          "ferias": {
            "type": "object",
            "properties": {
              "dataInicioGozo": {
                "type": "string",
                "description": "Data de início do gozo de férias. Formato: **dd/MM/yyyy**.",
                "example": "01/07/2024"
              },
              "numeroDias": {
                "type": "integer",
                "description": "Quantidade de dias de férias solicitados.",
                "example": 30
              },
              "adianta13": {
                "type": "boolean",
                "description": "Indica se há adiantamento do 13° salário.",
                "example": false
              },
              "abonoPecuniario": {
                "type": "boolean",
                "description": "Indica se há abono pecuniário. Para a quantidade de dias convertidos, consulte `diasAbonoPecuniario`.",
                "example": true
              },
              "diasAbonoPecuniario": {
                "type": "integer",
                "description": "Quantidade de dias convertidos em abono pecuniário.",
                "example": 10
              }
            }
          },
          "status": {
            "type": "string",
            "description": "Status atual da solicitação de férias.",
            "example": "0"
          },
          "sequencia": {
            "type": "integer",
            "description": "Sequência da solicitação de férias.",
            "example": 1
          },
          "dataSolicitacao": {
            "type": "string",
            "description": "Data e hora em que a solicitação foi registrada. Formato: **dd/MM/yyyy HH:mm:ss**.",
            "example": "15/06/2024 10:30:00"
          },
          "observacao": {
            "type": "string",
            "description": "Observação registrada na solicitação.",
            "example": "Férias programadas para o recesso de julho."
          }
        }
      },
      "Requisicao_de_Feriasretorno400": {
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
                "example": "O campo 'codFunc' é obrigatório."
              }
            }
          }
        }
      },
      "Requisicao_de_Feriasretorno404": {
        "type": "object",
        "properties": {
          "statusCode": {
            "type": "integer",
            "format": "int32",
            "example": 404
          },
          "error": {
            "$ref": "#/components/schemas/Requisicao_de_FeriasretornoErro"
          }
        }
      },
      "Requisicao_de_FeriasretornoErro": {
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
            "example": "O registro [6] enviado não existe."
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
