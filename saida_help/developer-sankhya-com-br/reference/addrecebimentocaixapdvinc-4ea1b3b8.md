---
id: "https://developer.sankhya.com.br/reference/addrecebimentocaixapdvinc"
titulo: "Registra recebimento para um Caixa/PDV"
url: "https://developer.sankhya.com.br/reference/addrecebimentocaixapdvinc"
atualizado_em: "2026-05-27T21:06:58.000Z"
---

# Registra recebimento para um Caixa/PDV

Registra recebimento para um Caixa/PDV.

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
      "name": "Vendas Gestão de Caixa",
      "description": "Gestão de Caixa (NFC-e e CF-e/SAT)"
    }
  ],
  "paths": {
    "/v1/caixa/recebimento": {
      "post": {
        "tags": [
          "Vendas Gestão de Caixa"
        ],
        "summary": "Registra recebimento para um Caixa/PDV",
        "description": "Registra recebimento para um Caixa/PDV.",
        "operationId": "addRecebimentoCaixaPDVinc",
        "requestBody": {
          "description": "Inclui um recebimento realizado em um Caixa/PDV no SankhyaOm. Vale ressaltar que não será permitido a inclusão de um financeiro repetido e para isso o serviço irá considerar os seguintes atributos como únicos: codigoParceiro, dataVencimento, codigoTipoOperação, codigoNatureza, identificador, tipoPagamento e valorParcela.\n",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/recebimentoIncluir"
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
              "write:caixa/recebimento",
              "read:caixa/recebimento"
            ]
          }
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "recebimentoModelo": {
        "type": "object",
        "properties": {
          "codigoCaixa": {
            "type": "integer",
            "description": "Identificador do Caixa/PDV que está aberto. Esta informação é retonrada ao abrir o caixa e pode ser consultada também pelo endpoint caixa/{codigoPdv}/{cpfOperador}",
            "example": 348
          },
          "dataBaixa": {
            "type": "string",
            "description": "Data da baixa do recebimento",
            "example": "26/10/2024"
          },
          "valorBaixa": {
            "type": "number",
            "description": "Valor da baixa do recebimento",
            "example": 3.4
          },
          "valorJuro": {
            "type": "number",
            "description": "Valor de juros do recebimento",
            "example": 0.02
          },
          "valorMulta": {
            "type": "number",
            "description": "Valor de multa do recebimento",
            "example": 0
          },
          "valorDesconto": {
            "type": "number",
            "description": "Valor de desconto do recebimento",
            "example": 0
          },
          "identificador": {
            "type": "string",
            "description": "Número identificador do recebívelf, pode ser o código de barras, nosso número, ou algum outra informação que seja capaz de identificar o finaceiro recebido.",
            "example": 1025469845
          },
          "observacao": {
            "type": "string",
            "example": "Observações para o recebimento"
          }
        }
      },
      "recebimentoIncluir": {
        "description": "Este serviço permite a inclusão e baixa de recebimentos realizados no Caixa/PDV. A identificação da empresa associada à transação é obtida automaticamente com base no Caixa/PDV que executa a operação. A classificação do movimento financeiro como receita ou despesa será determinada pela Natureza da transação, indicada pelo código \"codigoNatureza\" fornecido na requisição.",
        "allOf": [
          {
            "$ref": "#/components/schemas/financeiroModelo"
          },
          {
            "$ref": "#/components/schemas/recebimentoModelo"
          }
        ],
        "type": "object",
        "required": [
          "tipoPagamento",
          "dataVencimento",
          "valorParcela",
          "dataBaixa",
          "valorBaixa",
          "codigoCaixa",
          "codigoTipoOperacao",
          "codigoNatureza",
          "codigoParceiro"
        ],
        "properties": {
          "codigoTipoOperacao": {
            "type": "integer",
            "description": "Insira o código do Tipo de Operação para realizar a inclusão do Financeiro. Esse código é facilmente acessível através da nossa API, na entidade \"TipoOperacao\" (CODTIPOPER) com o critério TIPMOV = 'I'. Obtenha essa informação e mantenha seus registros sempreatualizados. Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "example": 108
          },
          "codigoNatureza": {
            "type": "integer",
            "description": "Insira o código da Natureza para realizar a inclusão do Financeiro. Esse código é facilmente acessível através da nossa API, na entidade \"Natureza\" (CODNAT). Obtenha essa informação e mantenha seus registros sempreatualizados. Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "example": 101005
          },
          "codigoProjeto": {
            "type": "integer",
            "description": "Insira o código do Projeto para realizar a inclusão do Financeiro. Esse código é facilmente acessível através da nossa API, na entidade \"Projeto\" (CODPROJ). Obtenha essa informação e mantenha seus registros sempreatualizados. Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "example": 10011
          },
          "codigoCentroResultado": {
            "type": "integer",
            "description": "Insira o código do Centro de Resultado para realizar a inclusão do Financeiro. Esse código é facilmente acessível através da nossa API, na entidade \"CentroResultado\" (CODCENCUS). Obtenha essa informação e mantenha seus registros sempreatualizados. Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "example": 3004002
          },
          "codigoParceiro": {
            "type": "integer",
            "description": "Insira o código do Parceiro para realizar a inclusão do Financeiro. Esse código é facilmente acessível através da nossa API, na entidade \"Parceiro\" (CODPARC). Obtenha essa informação e mantenha seus registros sempreatualizados. Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "example": 1581
          }
        }
      },
      "financeiroModelo": {
        "type": "object",
        "description": "Os atributos apresentados aqui estão vinculados ao financeiro da nota, mapeados pela entidade \"Financeiro\". Para personalizar a integração é possível enviar os atributos dessa entidade, como \"DTVENC\" em vez de \"dataVencimento\". Além disso, é possível utilizar campos que, embora não estejam detalhados nesta documentação, fazem parte do dicionário de dados.",
        "properties": {
          "tipoPagamento": {
            "type": "integer",
            "description": "Tipo de Título para o respectivo financeiro. Essa informação deve ser obtida previamente pela entidade \"TipoTitulo\" (CODTIPTIT). Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "example": 19
          },
          "cheque": {
            "$ref": "#/components/schemas/cheque"
          },
          "cartao": {
            "$ref": "#/components/schemas/cartao"
          },
          "dataVencimento": {
            "type": "string",
            "description": "Data do vencimento do financeiro.",
            "example": "30/05/2024"
          },
          "dataBaixa": {
            "type": "string",
            "description": "Data da baixa do financeiro. Em casos de deixar sem baixar, basta não enviar esta informação.",
            "example": "30/05/2024"
          },
          "valorParcela": {
            "type": "number",
            "description": "Valor total da parcela.",
            "example": 3.38
          },
          "idTransacao": {
            "type": "string",
            "description": "ID da transação quando houver. Por exemplo o protocolo da transação PIX.",
            "example": "dadotiuiwnlkeuhcnhlahdiwlaoaokd48ge65x"
          }
        }
      },
      "cartao": {
        "type": "object",
        "properties": {
          "bandeira": {
            "type": "string",
            "description": "Segue padrão para bandeiras de cartões de créditos disponível no layout da nota fiscal eletronica.\n  - 01 - Visa\n  - 02 - Mastercard\n  - 03 - American Express\n  - 04 - Sorocred\n  - 05 - Diners Club\n  - 06 - Elo\n  - 07 - Hipercard\n  - 08 - Aura\n  - 09 - Cabal\n  - 99 - Outros",
            "example": "02"
          },
          "autorizacao": {
            "type": "string",
            "description": "Código de autorização na transação fornecedido pela administradora do cartão de crédito. Informação utilizada para conciliação financeira.",
            "example": "04581596"
          }
        }
      },
      "cheque": {
        "type": "object",
        "properties": {
          "codigoBarras": {
            "type": "string",
            "example": "\"341067330330018805201725766099\""
          },
          "banco": {
            "type": "string",
            "example": "341"
          },
          "agencia": {
            "type": "string",
            "example": "0673"
          },
          "conta": {
            "type": "string",
            "example": "576609"
          },
          "numero": {
            "type": "string",
            "example": "001880"
          },
          "nome": {
            "type": "string",
            "example": "José da Silva Souza"
          },
          "cnpjCpf": {
            "type": "string",
            "example": "14532515955"
          }
        },
        "description": "Esta informação deve ser enviada \"apenas\" quando a opção de pagamento (atributo \"tipoPagamento\") seja do tipo \"Cheque\" (\"02\"). Recebe dados de Cheque utilizado como meio de pagamento"
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
