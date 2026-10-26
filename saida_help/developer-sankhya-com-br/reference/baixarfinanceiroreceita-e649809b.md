---
id: "https://developer.sankhya.com.br/reference/baixarfinanceiroreceita"
titulo: "Realiza Baixa de Receitas"
url: "https://developer.sankhya.com.br/reference/baixarfinanceiroreceita"
atualizado_em: "2026-05-27T21:17:01.000Z"
---

# Realiza Baixa de Receitas

Realiza a baixa de um título financeiro.
O campo dataBaixa é obrigatório.
Caso codigoContaBancaria não seja informado:
- se existir apenas uma conta válida, ela será utilizada automaticamente;
- se existir mais de uma conta válida, será necessário informar uma conta para prosseguir.

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
      "name": "Financeiros Movimentos",
      "description": "Breve descrição sobre o respectivo contexto"
    }
  ],
  "paths": {
    "/v1/financeiros/receitas/{codigoFinanceiro}/baixa": {
      "post": {
        "tags": [
          "Financeiros Movimentos"
        ],
        "summary": "Realiza Baixa de Receitas",
        "description": "Realiza a baixa de um título financeiro.\nO campo dataBaixa é obrigatório.\nCaso codigoContaBancaria não seja informado:\n- se existir apenas uma conta válida, ela será utilizada automaticamente;\n- se existir mais de uma conta válida, será necessário informar uma conta para prosseguir.",
        "operationId": "baixarFinanceiroReceita",
        "parameters": [
          {
            "name": "codigoFinanceiro",
            "in": "path",
            "description": "Informe neste atributo o \"código do financeiro\" desejado\n",
            "required": true,
            "schema": {
              "type": "integer",
              "format": "int64",
              "example": 4599
            }
          }
        ],
        "requestBody": {
          "description": "Dados para realizar a baixa do financeiro de receita.\n",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/baixaFinanceiroRequest"
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
                  "$ref": "#/components/schemas/baixaFinanceiroResponse"
                }
              }
            }
          },
          "400": {
            "description": "Informações Inválidas.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Api_Financeiroretorno400"
                },
                "examples": {
                  "multiplas_contas": {
                    "summary": "Mais de uma conta financeira disponível",
                    "value": {
                      "erro": "Mais de uma conta financeira disponível. Informe a conta para prosseguir com a baixa."
                    }
                  }
                }
              }
            }
          }
        },
        "security": [
          {
            "Bearer": [
              "write:financeiro",
              "read:financeiro"
            ]
          }
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "baixaFinanceiroRequest": {
        "type": "object",
        "required": [
          "dataBaixa"
        ],
        "properties": {
          "codigoTipoOperacao": {
            "type": "integer",
            "description": "Código do Tipo de Operação para realizar a baixa do financeiro. Consulte o endpoint /v1/tipos-operacao para obter os valores disponíveis.",
            "example": 108
          },
          "codigoContaBancaria": {
            "type": "integer",
            "description": "Código da Conta Bancária para realizar a baixa. Quando não informado, será utilizada automaticamente se houver apenas uma conta válida. Consulte o endpoint /v1/financeiros/contas-bancaria para obter os valores disponíveis.",
            "example": 42
          },
          "dataBaixa": {
            "type": "string",
            "description": "Data da baixa do financeiro (yyyy-MM-dd).",
            "example": "2025-02-11"
          },
          "valorBaixa": {
            "type": "number",
            "description": "Valor efetivo da baixa.",
            "example": 3.4
          },
          "valorJuro": {
            "type": "number",
            "description": "Valor de juros.",
            "example": 0.02
          },
          "valorMulta": {
            "type": "number",
            "description": "Valor de multa.",
            "example": 0
          },
          "valorDesconto": {
            "type": "number",
            "description": "Valor de desconto.",
            "example": 0
          },
          "observacao": {
            "type": "string",
            "description": "Observações para a baixa.",
            "example": "Observações para a baixa"
          }
        }
      },
      "baixaFinanceiroResponse": {
        "type": "object",
        "properties": {
          "tipo": {
            "type": "string",
            "example": "OK"
          },
          "mensagem": {
            "type": "string",
            "example": "Financeiro baixado com sucesso."
          },
          "retorno": {
            "$ref": "#/components/schemas/numeroFinanceiro"
          }
        }
      },
      "Api_Financeiroretorno400": {
        "required": [
          "statusCode"
        ],
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
            "$ref": "#/components/schemas/Api_FinanceiroretornoErro"
          },
          "erro": {
            "type": "string",
            "description": "Mensagem de erro descritiva. Exemplos:\n- Parâmetro dataBaixa é obrigatório.\n- Formato de data inválido. Utilize yyyy-MM-dd.\n- Conta financeira informada não existe.\n- Mais de uma conta financeira disponível. Informe a conta para prosseguir com a baixa.",
            "example": "Parâmetro dataBaixa é obrigatório."
          }
        }
      },
      "Api_FinanceiroretornoErro": {
        "required": [
          "code"
        ],
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
            "example": "O valor enviado não existe."
          },
          "help": {
            "type": "string",
            "example": "https://api.sankhya.com.br/api/docs/?ERROR_CODE=INVALID_REQUEST"
          }
        }
      },
      "numeroFinanceiro": {
        "required": [
          "codigoFinanceiro"
        ],
        "type": "object",
        "properties": {
          "codigoFinanceiro": {
            "type": "integer",
            "description": "Insira o código do Financeiro para realizar baixa. Esse código é facilmente acessível através da nossa API, na entidade \"Financeiro\" (NUFIN). Obtenha essa informação e mantenha seus registros sempre atualizados. Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "example": 8115
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
