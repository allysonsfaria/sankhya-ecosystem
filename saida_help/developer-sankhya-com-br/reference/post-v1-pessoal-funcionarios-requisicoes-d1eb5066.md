---
id: "https://developer.sankhya.com.br/reference/post_v1-pessoal-funcionarios-requisicoes-ferias"
titulo: "Criar uma nova requisição de férias"
url: "https://developer.sankhya.com.br/reference/post_v1-pessoal-funcionarios-requisicoes-ferias"
atualizado_em: "2026-06-30T15:07:56.000Z"
---

# Criar uma nova requisição de férias

Este endpoint permite o registro de uma nova requisição de férias de um funcionário. O processo é realizado em duas etapas internas: validação dos campos e período aquisitivo, seguida do lançamento da solicitação.

 Versão mínima do módulo pessoal: **5.106.0**

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
    "/v1/pessoal/funcionarios/requisicoes-ferias": {
      "post": {
        "summary": "Criar uma nova requisição de férias",
        "tags": [
          "HCM Cadastros"
        ],
        "description": "Este endpoint permite o registro de uma nova requisição de férias de um funcionário. O processo é realizado em duas etapas internas: validação dos campos e período aquisitivo, seguida do lançamento da solicitação.\n\n Versão mínima do módulo pessoal: **5.106.0**",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/RequisicaoFeriasRequest"
              },
              "example": {
                "codFunc": 100,
                "codEmp": 1,
                "periodoAquisitivo": {
                  "dataInicioAquisitivo": "01/03/2024",
                  "dataFimAquisitivo": "01/03/2025"
                },
                "ferias": {
                  "dataInicioGozo": "01/07/2024",
                  "numeroDias": 30,
                  "adianta13": false,
                  "abonoPecuniario": 10
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Requisição de Férias criada com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/RequisicaoFeriasCreateResponse"
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
            "description": "Dados não encontrados. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
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
              "write:Requisição de férias",
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
      "RequisicaoFeriasRequest": {
        "type": "object",
        "required": [
          "codFunc",
          "codEmp",
          "periodoAquisitivo",
          "ferias"
        ],
        "properties": {
          "codFunc": {
            "type": "integer",
            "description": "Código do funcionário. Entidade: **Funcionário** (TFPFUN.CODFUNC).",
            "example": 100
          },
          "codEmp": {
            "type": "integer",
            "description": "Código da empresa. Entidade: **EmpresaPessoal** (TFPFUN.CODEMP).",
            "example": 1
          },
          "periodoAquisitivo": {
            "type": "object",
            "required": [
              "dataInicioAquisitivo"
            ],
            "description": "Dados do período aquisitivo de férias do funcionário.",
            "properties": {
              "dataInicioAquisitivo": {
                "type": "string",
                "description": "Data de início do período aquisitivo. Formato: **dd/MM/yyyy**.",
                "example": "01/03/2024"
              },
              "dataFimAquisitivo": {
                "type": "string",
                "description": "Data de fim do período aquisitivo. Formato: **dd/MM/yyyy**. Opcional — utilizado para desambiguação quando há múltiplos períodos com a mesma data de início.",
                "example": "01/03/2025"
              }
            }
          },
          "ferias": {
            "type": "object",
            "required": [
              "dataInicioGozo",
              "numeroDias"
            ],
            "description": "Dados do gozo de férias.",
            "properties": {
              "dataInicioGozo": {
                "type": "string",
                "description": "Data de início do gozo de férias. Formato: **dd/MM/yyyy**.",
                "example": "01/07/2024"
              },
              "numeroDias": {
                "type": "integer",
                "minimum": 1,
                "description": "Quantidade de dias de férias solicitados.",
                "example": 30
              },
              "adianta13": {
                "type": "boolean",
                "description": "Indica se o funcionário deseja adiantar o 13° salário junto às férias.",
                "default": false,
                "example": false
              },
              "abonoPecuniario": {
                "type": "integer",
                "minimum": 0,
                "description": "Quantidade de dias de abono pecuniário (conversão de dias de férias em dinheiro). Quando não informado, assume **0**. A soma de `numeroDias + abonoPecuniario` não pode exceder 30.",
                "default": 0,
                "example": 10
              }
            }
          }
        }
      },
      "RequisicaoFeriasCreateResponse": {
        "type": "object",
        "properties": {
          "codigoSolicitacao": {
            "type": "integer",
            "description": "Código da requisição de férias criada.",
            "example": 42
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
