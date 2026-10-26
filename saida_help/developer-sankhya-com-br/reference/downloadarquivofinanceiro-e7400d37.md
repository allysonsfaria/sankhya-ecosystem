---
id: "https://developer.sankhya.com.br/reference/downloadarquivofinanceiro"
titulo: "Gerar PDF do Boleto"
url: "https://developer.sankhya.com.br/reference/downloadarquivofinanceiro"
atualizado_em: "2026-06-22T19:53:08.000Z"
---

# Gerar PDF do Boleto

Endpoint `GET /v1/financeiros/{codigoFinanceiro}/boletos` - Gera e baixa o arquivo de um título financeiro de receita cadastrado no SankhyaOM. Atualmente o arquivo retornado é o boleto, em formato PDF, devolvido como conteúdo binário (`application/octet-stream`).

Pré-requisitos do título financeiro:
- Deve ser uma receita;
- Não pode estar baixado;
- Deve possuir nosso número, linha digitável e código de barras preenchidos.


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
    "/v1/financeiros/{codigoFinanceiro}/boletos": {
      "get": {
        "tags": [
          "Financeiros Movimentos"
        ],
        "summary": "Gerar PDF do Boleto",
        "description": "Endpoint `GET /v1/financeiros/{codigoFinanceiro}/boletos` - Gera e baixa o arquivo de um título financeiro de receita cadastrado no SankhyaOM. Atualmente o arquivo retornado é o boleto, em formato PDF, devolvido como conteúdo binário (`application/octet-stream`).\n\nPré-requisitos do título financeiro:\n- Deve ser uma receita;\n- Não pode estar baixado;\n- Deve possuir nosso número, linha digitável e código de barras preenchidos.\n",
        "operationId": "downloadArquivoFinanceiro",
        "parameters": [
          {
            "name": "codigoFinanceiro",
            "in": "path",
            "description": "Código único do financeiro no ERP (PK da entidade Financeiro)",
            "required": true,
            "schema": {
              "type": "integer",
              "format": "int64",
              "example": 100
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Operação bem sucedida. O boleto é retornado como arquivo PDF binário, acompanhado do cabeçalho `Content-Disposition: attachment; filename=\"boleto.pdf\"`.\n",
            "content": {
              "application/octet-stream": {
                "schema": {
                  "type": "string",
                  "format": "binary"
                }
              }
            },
            "headers": {
              "Content-Disposition": {
                "description": "Indica que a resposta é um anexo para download e informa o nome do arquivo.",
                "schema": {
                  "type": "string",
                  "example": "attachment; filename=\"boleto.pdf\""
                }
              }
            }
          },
          "400": {
            "description": "Informações Inválidas. Ocorre quando o título não atende aos pré-requisitos — por exemplo: \"Financeiro não encontrado.\", \"Título precisa ser receita.\", \"Título não pode estar baixado.\" ou \"Título precisa conter nosso número, linha digitável e código de barras.\". Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Api_Financeiroretorno400"
                }
              }
            }
          },
          "401": {
            "description": "Não autenticado. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Api_Financeiroretorno40X_50X"
                }
              }
            }
          },
          "403": {
            "description": "Autenticação inválida. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Api_Financeiroretorno40X_50X"
                }
              }
            }
          },
          "404": {
            "description": "Dados não encontrados. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Api_Financeiroretorno404"
                }
              }
            }
          },
          "500": {
            "description": "Erro interno no servidor. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Api_Financeiroretorno40X_50X"
                }
              }
            }
          },
          "501": {
            "description": "Não implementado. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Api_Financeiroretorno40X_50X"
                }
              }
            }
          },
          "502": {
            "description": "Retorno inválido do servidor. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Api_Financeiroretorno40X_50X"
                }
              }
            }
          },
          "503": {
            "description": "Serviço indisponível no momento. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Api_Financeiroretorno40X_50X"
                }
              }
            }
          },
          "504": {
            "description": "Tempo de execução excedido. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Api_Financeiroretorno40X_50X"
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
      "Api_Financeiroretorno40X_50X": {
        "required": [
          "fieldSet"
        ],
        "type": "object",
        "properties": {
          "fieldSet": {
            "type": "string"
          },
          "paginate": {
            "type": "string"
          },
          "mensagem": {
            "$ref": "#/components/schemas/Api_Financeiroerror"
          }
        }
      },
      "Api_Financeiroretorno404": {
        "required": [
          "statusCode"
        ],
        "type": "object",
        "properties": {
          "statusCode": {
            "type": "integer",
            "format": "int32",
            "example": 404
          },
          "error": {
            "$ref": "#/components/schemas/Api_FinanceiroretornoErro"
          }
        }
      },
      "Api_Financeiroerror": {
        "required": [
          "codigo"
        ],
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
