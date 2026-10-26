---
id: "https://developer.sankhya.com.br/reference/get_v1-pessoal-periodos-aquisitivos-ferias"
titulo: "Consultar períodos aquisitivos de férias"
url: "https://developer.sankhya.com.br/reference/get_v1-pessoal-periodos-aquisitivos-ferias"
atualizado_em: "2026-06-30T15:07:56.000Z"
---

# Consultar períodos aquisitivos de férias

Retorna os períodos aquisitivos de férias **não gozados** cadastrados no SankhyaOm. Um período não gozado pode ter saldo de dias igual a zero. Por padrão, esses períodos com saldo zerado também não são retornados; utilize o parâmetro `saldoZerado=true` para incluí-los.

**Regras de filtro:**
- `codigoFuncionario` só pode ser informado em conjunto com `codigoEmpresa`.

 Versão mínima do módulo pessoal: **5.102.0**

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
    "/v1/pessoal/periodos-aquisitivos-ferias": {
      "get": {
        "summary": "Consultar períodos aquisitivos de férias",
        "tags": [
          "HCM Cadastros"
        ],
        "description": "Retorna os períodos aquisitivos de férias **não gozados** cadastrados no SankhyaOm. Um período não gozado pode ter saldo de dias igual a zero. Por padrão, esses períodos com saldo zerado também não são retornados; utilize o parâmetro `saldoZerado=true` para incluí-los.\n\n**Regras de filtro:**\n- `codigoFuncionario` só pode ser informado em conjunto com `codigoEmpresa`.\n\n Versão mínima do módulo pessoal: **5.102.0**",
        "parameters": [
          {
            "name": "codigoEmpresa",
            "in": "query",
            "required": false,
            "description": "Código da empresa. Obrigatório quando `codigoFuncionario` for informado. Entidade: **EmpresaPessoal** (TFPFUN.CODEMP).",
            "schema": {
              "type": "integer",
              "example": 1
            }
          },
          {
            "name": "codigoFuncionario",
            "in": "query",
            "required": false,
            "description": "Código do funcionário. Requer que `codigoEmpresa` também seja informado. Entidade: **Funcionário** (TFPFUN.CODFUNC).",
            "schema": {
              "type": "integer",
              "example": 100
            }
          },
          {
            "name": "updatedSince",
            "in": "query",
            "required": false,
            "description": "Filtra registros alterados a partir desta data/hora. Formato: **AAAA-MM-DDTHH:MM:SS**.",
            "schema": {
              "type": "string",
              "example": "2024-01-01T00:00:00"
            }
          },
          {
            "name": "saldoZerado",
            "in": "query",
            "required": false,
            "description": "Quando `true`, inclui na resposta períodos não gozados cujo saldo de dias é zero. Por padrão (`false`), apenas períodos não gozados com saldo maior que zero são retornados.",
            "schema": {
              "type": "boolean",
              "default": false,
              "example": false
            }
          },
          {
            "name": "page",
            "in": "query",
            "required": false,
            "description": "Número da página para paginação, iniciando em ZERO (0).",
            "schema": {
              "type": "integer",
              "default": 0,
              "example": 0
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Lista de períodos aquisitivos retornada com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PeriodosAquisitivosFeriasResponse"
                },
                "example": {
                  "periodosAquisitivos": [
                    {
                      "empresa": {
                        "codigo": 1,
                        "nomeFantasia": "Empresa ABC"
                      },
                      "funcionario": {
                        "codigo": 100,
                        "nome": "João Silva"
                      },
                      "periodoAquisitivo": {
                        "dataInicio": "01/03/2024 00:00:00",
                        "dataFim": "01/03/2025 00:00:00"
                      },
                      "abonoPecuniario": 10,
                      "faltasNoPeriodo": 2,
                      "diasPerdidoFaltas": 6,
                      "diasFeriasGozados": 10,
                      "licencaRemunerada": 0,
                      "adianta13": false,
                      "saldoDias": 14,
                      "dataAlteracao": "01/06/2024 10:30:00"
                    }
                  ]
                }
              }
            }
          },
          "400": {
            "description": "Informações Inválidas. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Periodo_Aquisitivo_Feriasretorno400"
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
                  "$ref": "#/components/schemas/Periodo_Aquisitivo_Feriasretorno404"
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
              "read:Períodos aquisitivos de férias"
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
      "PeriodosAquisitivosFeriasResponse": {
        "type": "object",
        "properties": {
          "periodosAquisitivos": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PeriodoAquisitivoFerias"
            }
          }
        }
      },
      "PeriodoAquisitivoFerias": {
        "type": "object",
        "properties": {
          "empresa": {
            "type": "object",
            "properties": {
              "codigo": {
                "type": "integer",
                "description": "Código da empresa. Entidade: **EmpresaPessoal** (TFPFUN.CODEMP).",
                "example": 1
              },
              "nomeFantasia": {
                "type": "string",
                "description": "Nome fantasia da empresa.",
                "example": "Empresa ABC"
              }
            }
          },
          "funcionario": {
            "type": "object",
            "properties": {
              "codigo": {
                "type": "integer",
                "description": "Código do funcionário. Entidade: **Funcionário** (TFPFUN.CODFUNC).",
                "example": 100
              },
              "nome": {
                "type": "string",
                "description": "Nome completo do funcionário.",
                "example": "João Silva"
              }
            }
          },
          "periodoAquisitivo": {
            "type": "object",
            "description": "Intervalo de datas do período aquisitivo de férias.",
            "properties": {
              "dataInicio": {
                "type": "string",
                "description": "Data de início do período aquisitivo. Formato: **dd/MM/yyyy HH:mm:ss**.",
                "example": "01/03/2024 00:00:00"
              },
              "dataFim": {
                "type": "string",
                "description": "Data de fim do período aquisitivo. Formato: **dd/MM/yyyy HH:mm:ss**.",
                "example": "01/03/2025 00:00:00"
              }
            }
          },
          "abonoPecuniario": {
            "type": "integer",
            "description": "Total de dias convertidos em abono pecuniário (venda de dias de férias). Entidade: **VFPPeriodoAquisitivoFerias** (ABONOPECUNIARIO).",
            "example": 10
          },
          "faltasNoPeriodo": {
            "type": "integer",
            "description": "Quantidade de faltas registradas no período aquisitivo. Entidade: **VFPPeriodoAquisitivoFerias** (FALTPER).",
            "example": 2
          },
          "diasPerdidoFaltas": {
            "type": "integer",
            "description": "Dias de férias perdidos em razão das faltas no período, conforme tabela progressiva da CLT. Entidade: **VFPPeriodoAquisitivoFerias** (DIASPERDIDOFALTAS).",
            "example": 6
          },
          "diasFeriasGozados": {
            "type": "integer",
            "description": "Total de dias de férias já gozados ou com gozo agendado (sequências com data prevista informada). Entidade: **VFPPeriodoAquisitivoFerias** (NUMDIASFER).",
            "example": 10
          },
          "licencaRemunerada": {
            "type": "integer",
            "description": "Dias de licença remunerada no período. Entidade: **VFPPeriodoAquisitivoFerias** (LICENCAREMUNERADA).",
            "example": 0
          },
          "adianta13": {
            "type": "boolean",
            "description": "Indica se o adiantamento do 13° salário foi solicitado nas férias.",
            "example": false
          },
          "saldoDias": {
            "type": "integer",
            "description": "Saldo de dias de férias disponíveis para gozo. Calculado como: `MAIOR(30 - diasPerdidoFaltas - abonoPecuniario - diasFeriasGozados, 0)`. Entidade: **VFPPeriodoAquisitivoFerias** (SALDODIAS).",
            "example": 14
          },
          "dataAlteracao": {
            "type": "string",
            "description": "Data e hora da última alteração no período aquisitivo. Formato: **dd/MM/yyyy HH:mm:ss**.",
            "example": "01/06/2024 10:30:00"
          }
        }
      },
      "Periodo_Aquisitivo_Feriasretorno400": {
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
      "Periodo_Aquisitivo_Feriasretorno404": {
        "type": "object",
        "properties": {
          "statusCode": {
            "type": "integer",
            "format": "int32",
            "example": 404
          },
          "error": {
            "$ref": "#/components/schemas/Periodo_Aquisitivo_FeriasretornoErro"
          }
        }
      },
      "Periodo_Aquisitivo_FeriasretornoErro": {
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
            "example": "O parâmetro codigoEmpresa é obrigatório quando codigoFuncionario é informado."
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
