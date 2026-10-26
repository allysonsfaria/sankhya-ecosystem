---
id: "https://developer.sankhya.com.br/reference/getfinanceirosdespesas"
titulo: "Obter Despesas"
url: "https://developer.sankhya.com.br/reference/getfinanceirosdespesas"
atualizado_em: "2026-05-27T21:17:01.000Z"
---

# Obter Despesas

Endpoint `GET /v1/financeiros/despesas` - Fornece acesso aos dados financeiros de despesas lançados no SankhyaOM, com suporte a ordenação dinâmica via parâmetro sort. A paginação é controlada automaticamente pela integração (routeWithRepeat).

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
    "/v1/financeiros/despesas": {
      "get": {
        "tags": [
          "Financeiros Movimentos"
        ],
        "summary": "Obter Despesas",
        "description": "Endpoint `GET /v1/financeiros/despesas` - Fornece acesso aos dados financeiros de despesas lançados no SankhyaOM, com suporte a ordenação dinâmica via parâmetro sort. A paginação é controlada automaticamente pela integração (routeWithRepeat).",
        "operationId": "getFinanceirosDespesas",
        "parameters": [
          {
            "name": "page",
            "in": "query",
            "description": "Número da página para paginação dos resultados. O valor mínimo é 1. Quando não informado, será considerada a página 1.",
            "required": false,
            "schema": {
              "type": "integer",
              "example": 1
            }
          },
          {
            "name": "sort",
            "in": "query",
            "description": "Ordenação dos resultados no formato campo,direcao. Permite múltiplos parâmetros.\n\nCampos disponíveis:\n- dataVencimento\n- dataBaixa\n- valorParcela\n- nomeParceiro\n- nomeEmpresa\n- codigoNota\n\nDireção:\n- asc\n- desc\n\nExemplo:\n?sort=dataBaixa,desc",
            "required": false,
            "schema": {
              "type": "string",
              "example": "dataBaixa,desc"
            }
          },
          {
            "name": "codigoEmpresa",
            "in": "query",
            "description": "Filtra registros retornando apenas financeiro da respectiva empresa enviada no filtro.\n",
            "required": false,
            "schema": {
              "type": "integer",
              "format": "int64",
              "example": 1456
            }
          },
          {
            "name": "codigoParceiro",
            "in": "query",
            "description": "Filtra registros retornando apenas financeiro do respectivo parceiro enviado no filtro.\n",
            "required": false,
            "schema": {
              "type": "integer",
              "format": "int64",
              "example": 1456
            }
          },
          {
            "name": "statusFinanceiro",
            "in": "query",
            "description": "Status do Título Financeiro no SankhyaOM:\n- 1 - Aberto\n- 2 - Baixado\n- 3 - Todos\n",
            "required": false,
            "schema": {
              "type": "integer",
              "enum": [
                1,
                2,
                3
              ]
            }
          },
          {
            "name": "tipoFinanceiro",
            "in": "query",
            "description": "Tipo do Título Financeiro no SankhyaOM:\n- 1 - Real\n- 2 - Provisao\n- 3 - Todos\n",
            "required": false,
            "schema": {
              "type": "integer",
              "enum": [
                1,
                2,
                3
              ]
            }
          },
          {
            "name": "dataNegociacaoInicio",
            "in": "query",
            "description": "Filtra registros que foram negociados a partir da data enviada no filtro. O formato da data deve seguir o padrão dd/MM/yyyy.\n",
            "required": false,
            "schema": {
              "type": "string",
              "example": "10/02/2025"
            }
          },
          {
            "name": "dataNegociacaoFinal",
            "in": "query",
            "description": "Filtra registros que foram negociados até a data enviada no filtro. O formato da data deve seguir o padrão dd/MM/yyyy.\n",
            "required": false,
            "schema": {
              "type": "string",
              "example": "20/02/2025"
            }
          },
          {
            "name": "dataVencimentoInicio",
            "in": "query",
            "description": "Filtra registros com vencimento a partir da data enviada no filtro. O formato da data deve seguir o padrão dd/MM/yyyy.\n",
            "required": false,
            "schema": {
              "type": "string",
              "example": "10/03/2025"
            }
          },
          {
            "name": "dataVencimentoFinal",
            "in": "query",
            "description": "Filtra registros com vencimento até a data enviada no filtro. O formato da data deve seguir o padrão dd/MM/yyyy.\n",
            "required": false,
            "schema": {
              "type": "string",
              "example": "20/03/2025"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Operação bem sucedida. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/financeiroResponseList"
                }
              }
            }
          },
          "400": {
            "description": "Informações Inválidas. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
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
      "paginacaoResponse": {
        "type": "object",
        "description": "Metadados de paginação retornados nas listagens.",
        "properties": {
          "page": {
            "type": "integer",
            "description": "Página atual (inicia em 1).",
            "example": 1
          },
          "pageSize": {
            "type": "integer",
            "description": "Quantidade de registros por página.",
            "example": 50
          },
          "total": {
            "type": "integer",
            "description": "Total de registros encontrados.",
            "example": 100
          },
          "totalPages": {
            "type": "integer",
            "description": "Total de páginas disponíveis.",
            "example": 2
          },
          "hasMore": {
            "type": "boolean",
            "description": "Indica se existem mais páginas após a atual.",
            "example": true
          }
        }
      },
      "boletoResponse": {
        "type": "object",
        "description": "Dados do boleto retornados na listagem de financeiros.",
        "properties": {
          "codigoBarras": {
            "type": "string",
            "description": "Código de barras do boleto (TGFFIN.CODBARRA).",
            "example": "341067330330018805201725766099"
          },
          "nossoNumero": {
            "type": "string",
            "description": "Nosso número do boleto (TGFFIN.NOSSONUM).",
            "example": "568454558"
          },
          "linhaDigitavel": {
            "type": "string",
            "description": "Linha digitável do boleto (TGFFIN.LINHADIGITAL).",
            "example": "0018801122446653232464655662245"
          },
          "numeroRemessa": {
            "type": "string",
            "description": "Número de remessa do boleto (TGFFIN.NUMREMESSA).",
            "example": "0012"
          }
        }
      },
      "rateioResponse": {
        "type": "object",
        "description": "Item de rateio retornado na listagem de financeiros.",
        "properties": {
          "codigoContaContabil": {
            "type": "integer",
            "description": "Código da conta contábil do rateio (TGFRAT.CODCTACTB).",
            "example": 42
          },
          "percentual": {
            "type": "number",
            "description": "Percentual do rateio (TGFRAT.PERCRATEIO).",
            "example": 50
          },
          "codigoNatureza": {
            "type": "integer",
            "description": "Código da natureza do rateio (TGFRAT.CODNAT).",
            "example": 101005
          },
          "codigoProjeto": {
            "type": "integer",
            "description": "Código do projeto do rateio (TGFRAT.CODPROJ).",
            "example": 10011
          },
          "codigoCentroResultado": {
            "type": "integer",
            "description": "Código do centro de resultado do rateio (TGFRAT.CODCENCUS).",
            "example": 3004002
          },
          "codigoParceiro": {
            "type": "integer",
            "description": "Código do parceiro do rateio (TGFRAT.CODPARC).",
            "example": 1581
          }
        }
      },
      "contaFinanceiroResponse": {
        "type": "object",
        "description": "Dados da conta bancária associada ao meio de recebimento/pagamento do financeiro.",
        "properties": {
          "idContaExterna": {
            "type": "string",
            "description": "Identificador externo da conta na integração (TFTCTA.ULIDAPI).",
            "example": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
          },
          "codBanco": {
            "type": "integer",
            "description": "Código do banco (TSICTA.CODBCO).",
            "example": 341
          },
          "nomeBanco": {
            "type": "string",
            "description": "Nome do banco (TSIBCO.NOMEBCO).",
            "example": "ITAÚ UNIBANCO S.A."
          },
          "agencia": {
            "type": "string",
            "description": "Número da agência (TSICTA.CODAGE).",
            "example": "1234"
          },
          "codConta": {
            "type": "integer",
            "description": "Código da conta bancária (TFTCTA.CODCTA).",
            "example": 42
          }
        }
      },
      "beneficiarioResponse": {
        "type": "object",
        "description": "Dados do beneficiário do financeiro. Em receitas representa a empresa (TSIEMP); em despesas, o parceiro (TGFPAR).",
        "properties": {
          "nome": {
            "type": "string",
            "description": "Nome do beneficiário. Em receitas, nome fantasia da empresa (TSIEMP.NOMEFANTASIA); em despesas, nome do parceiro (TGFPAR.NOMEPARC).",
            "example": "TECH SOLUTIONS"
          },
          "razaoSocial": {
            "type": "string",
            "description": "Razão social do beneficiário. Em receitas (TSIEMP.RAZAOSOCIAL); em despesas (TGFPAR.RAZAOSOCIAL).",
            "example": "TECH SOLUTIONS LTDA"
          },
          "cnpjCpf": {
            "type": "string",
            "description": "CNPJ ou CPF do beneficiário. Em receitas (TSIEMP.CGC); em despesas (TGFPAR.CGC_CPF).",
            "example": "12345678000190"
          }
        }
      },
      "recebimentoResponse": {
        "type": "object",
        "description": "Dados de recebimento do financeiro. Retornado apenas para receitas que possuam recebimento via PIX.",
        "properties": {
          "pix": {
            "type": "object",
            "description": "Dados do recebimento via PIX (TFTPIX).",
            "properties": {
              "emvPix": {
                "type": "string",
                "description": "Código EMV (copia e cola) do PIX (TFTPIX.EMV).",
                "example": "00020126360014BR.GOV.BCB.PIX0114+5511999999999520400005303986540510.005802BR5913FULANO DE TAL6008BRASILIA62070503***6304ABCD"
              },
              "status": {
                "type": "string",
                "description": "Status do recebimento via PIX (TFTPIX.STATUS).",
                "example": "CONCLUIDO"
              },
              "idExterno": {
                "type": "string",
                "description": "Identificador externo do PIX na integração (TFTPIX.IDAPI).",
                "example": "pix-9f8e7d6c5b4a"
              },
              "conta": {
                "$ref": "#/components/schemas/contaFinanceiroResponse"
              }
            }
          }
        }
      },
      "pagamentoResponse": {
        "type": "object",
        "description": "Dados de pagamento do financeiro. Retornado apenas para despesas que possuam pagamento via boleto.",
        "properties": {
          "boleto": {
            "type": "object",
            "description": "Dados do pagamento via boleto (TFTPAG).",
            "properties": {
              "codigoBarras": {
                "type": "string",
                "description": "Código de barras do boleto (TGFFIN.CODBARRA).",
                "example": "34191790010104351004791020150008291070026000"
              },
              "status": {
                "type": "string",
                "description": "Status do pagamento (TFTPAG.STATUS).",
                "example": "PENDENTE"
              },
              "idExterno": {
                "type": "string",
                "description": "Identificador externo do pagamento na integração (TFTPAG.ID_GATEWAY).",
                "example": "pag-1a2b3c4d5e6f"
              },
              "conta": {
                "$ref": "#/components/schemas/contaFinanceiroResponse"
              },
              "contasElegiveis": {
                "type": "array",
                "description": "Lista de contas bancárias elegíveis para realizar o pagamento.",
                "items": {
                  "$ref": "#/components/schemas/contaFinanceiroResponse"
                }
              }
            }
          }
        }
      },
      "Api_Financeirocartao": {
        "required": [
          "autorizacao",
          "bandeira",
          "dataHoraTransacao",
          "parcela",
          "rede",
          "valorTaxa"
        ],
        "type": "object",
        "properties": {
          "bandeira": {
            "type": "string",
            "description": "Segue padrão para bandeiras de cartões de créditos disponível no layout da nota fiscal eletronica (TGFTEF.BANDEIRA). As Bandeiras são cadastradas na tela \"Bandeiras  Tef\" no SankhyaOM (TSIBTEF.BANDEIRA). Esse código é facilmente acessível através da nossa API, no endpoint \"GET /v1/bandeirasTef\". Obtenha essa informação e mantenha seus registros sempre atualizados.",
            "example": "2"
          },
          "autorizacao": {
            "type": "string",
            "description": "Código de autorização na transação fornecedido pela administradora do cartão de crédito (TGFTEF.AUTORIZACAO).",
            "example": "04581596"
          },
          "NSU": {
            "type": "string",
            "description": "NSU da transação fornecedido pela administradora do cartão de crédito (TGFTEF.NUMNSU)",
            "example": "123456"
          },
          "rede": {
            "type": "string",
            "description": "Código da Rede (Adquirente) do cartão (TGFTEF.REDE). As Redes são cadastradas na tela \"Rede Tef\"  no SankhyaOM (TSIRTEF.REDE). Esse código é facilmente acessível através da nossa API, no endpoint \"GET /v1/redesTef\". Obtenha essa informação e mantenha seus registros sempre atualizados.",
            "example": "1"
          },
          "parcela": {
            "type": "integer",
            "description": "Número da Parcela fornecida pela administradora do cartão de crédito (TGFTEF.DESDOBRAMENTO)",
            "example": 1
          },
          "dataHoraTransacao": {
            "type": "string",
            "description": "Data e Hora da Transação fornecida pela administradora do cartão de crédito (TGFTEF.DTTRANSACAO)",
            "format": "datetime"
          },
          "valorTaxa": {
            "type": "number",
            "description": "Valor da Taxa fornecedida pela administradora do cartão de crédito (TGFTEF.VLRTAXA)",
            "example": 0.65
          }
        },
        "description": "Esta informação deve ser enviada \"apenas\" quando a opção de pagamento (atributo \"codigoTipoPagamento\") seja do subtipo 7 - Cartão de crédito (\"7\") ou Cartão de débito\"Cheque\" (\"8\"). Recebe dados da transação do cartão utilizado como meio de pagamento. "
      },
      "Api_Financeirocheque": {
        "required": [
          "codigoBarras",
          "valorCheque"
        ],
        "type": "object",
        "properties": {
          "codigoBarras": {
            "type": "string",
            "description": "Código de barras do cheque (TGFCHQ.CMC7)",
            "example": "341067330330018805201725766099"
          },
          "numeroCheque": {
            "type": "string",
            "description": "Número do cheque (TGFCHQ.NUMCHEQUE)",
            "example": "66009"
          },
          "banco": {
            "type": "string",
            "description": "Código Banco emissor do cheque (TGFCHQ.CODBCO)",
            "example": "341"
          },
          "agencia": {
            "type": "string",
            "description": "Agência bancária emissora do cheque (TGFCHQ.AGENCIA)",
            "example": "673"
          },
          "conta": {
            "type": "string",
            "description": "Número conta bancária emissora do cheque (TGFCHQ.CONTA)",
            "example": "576609"
          },
          "nome": {
            "type": "string",
            "description": "Nome emitente do cheque (TGFCHQ.NOMEEMITENTE)",
            "example": "José da Silva Souza"
          },
          "cnpjCpf": {
            "type": "string",
            "description": "CNPJ/CPF emitente (TGFCHQ.CGC_CPF)",
            "example": "14532515955"
          },
          "valorCheque": {
            "type": "number",
            "example": 200
          },
          "dataCheque": {
            "type": "string",
            "description": "Data do Cheque (TGFCHQ.DATACHEQUE)",
            "format": "date"
          }
        },
        "description": "Esta informação deve ser enviada \"apenas\" quando a opção de pagamento (atributo \"codigoTipoPagamento\") seja do subtipo \"Cheque\" (\"4\"). Recebe dados de Cheque utilizado como meio de pagamento"
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
      },
      "financeiroResponse": {
        "type": "object",
        "description": "Representa um título financeiro retornado nos endpoints de listagem.",
        "properties": {
          "codigoFinanceiro": {
            "type": "integer",
            "description": "Identificador único do financeiro (NUFIN).",
            "example": 8115
          },
          "origemFinanceiro": {
            "type": "string",
            "description": "Origem do financeiro (ORIGEM). Indica se foi gerado por nota fiscal, manualmente, etc.",
            "example": "N"
          },
          "dataNegociacaoInicio": {
            "type": "string",
            "description": "Data de negociação do financeiro (DTNEG), formato yyyy-MM-dd.",
            "example": "2025-02-11"
          },
          "codigoEmpresa": {
            "type": "integer",
            "description": "Código da empresa (CODEMP).",
            "example": 1
          },
          "codigoTipoOperacao": {
            "type": "integer",
            "description": "Código do tipo de operação (CODTIPOPER).",
            "example": 108
          },
          "codigoNatureza": {
            "type": "integer",
            "description": "Código da natureza financeira (CODNAT).",
            "example": 101005
          },
          "codigoProjeto": {
            "type": "integer",
            "description": "Código do projeto (CODPROJ).",
            "example": 10011
          },
          "codigoCentroResultado": {
            "type": "integer",
            "description": "Código do centro de resultado (CODCENCUS).",
            "example": 3004002
          },
          "codigoParceiro": {
            "type": "integer",
            "description": "Código do parceiro (CODPARC).",
            "example": 1581
          },
          "codigoContaBancaria": {
            "type": "integer",
            "description": "Código da conta bancária (CODCTABCOINT).",
            "example": 42
          },
          "codigoMoeda": {
            "type": "integer",
            "description": "Código da moeda (CODMOEDA).",
            "example": 22
          },
          "codigoTipoPagamento": {
            "type": "integer",
            "description": "Código do tipo de pagamento / tipo de título (CODTIPTIT).",
            "example": 19
          },
          "numeroNota": {
            "type": "integer",
            "description": "Número da nota vinculada ao financeiro (NUMNOTA).",
            "example": 33569
          },
          "dataNegociacao": {
            "type": "string",
            "description": "Data de negociação do financeiro (DTNEG), formato yyyy-MM-dd.",
            "example": "2025-02-11"
          },
          "dataVencimento": {
            "type": "string",
            "description": "Data de vencimento do financeiro (DTVENC), formato yyyy-MM-dd.",
            "example": "2025-03-11"
          },
          "numeroParcela": {
            "type": "integer",
            "description": "Número da parcela / desdobramento (DESDOBRAMENTO).",
            "example": 1
          },
          "maiorNumeroParcela": {
            "type": "integer",
            "description": "Maior número de parcela da nota (máximo de DESDOBRAMENTO por NUMNOTA).",
            "example": 10
          },
          "valorParcela": {
            "type": "number",
            "description": "Valor total da parcela (VLRDESDOB).",
            "example": 3.38
          },
          "valorBaixa": {
            "type": "number",
            "description": "Valor efetivamente baixado.",
            "example": 3.38
          },
          "dataBaixa": {
            "type": "string",
            "description": "Data da baixa financeira, formato yyyy-MM-dd.",
            "example": "2025-02-15"
          },
          "observacao": {
            "type": "string",
            "description": "Observação / histórico do financeiro (HISTORICO).",
            "example": "Pagamento referente à NF 33569"
          },
          "nomeEmpresa": {
            "type": "string",
            "description": "Nome fantasia da empresa (TSIEMP.NOMEFANTASIA).",
            "example": "TECH SOLUTIONS"
          },
          "nomeTipoOperacao": {
            "type": "string",
            "description": "Descrição do tipo de operação (TGFTOP.DESCROPER).",
            "example": "VENDAS PARA FORA DO ESTADO"
          },
          "nomeNatureza": {
            "type": "string",
            "description": "Descrição da natureza financeira (TGFNAT.DESCRNAT).",
            "example": "RECEITA COM VENDAS"
          },
          "nomeProjeto": {
            "type": "string",
            "description": "Descrição do projeto (TGFPRO.DESCRPROJ).",
            "example": "SEM PROJETO"
          },
          "nomeCentroResultado": {
            "type": "string",
            "description": "Descrição do centro de resultado (TSICUS.DESCRCENCUS).",
            "example": "VENDAS PRONTA ENTREGA"
          },
          "nomeParceiro": {
            "type": "string",
            "description": "Nome do parceiro (TGFPAR.NOMEPARC).",
            "example": "JOÃO DA SILVA"
          },
          "codigoNota": {
            "type": "integer",
            "description": "Identificador interno da nota (NUNOTA).",
            "example": 456159
          },
          "beneficiario": {
            "$ref": "#/components/schemas/beneficiarioResponse"
          },
          "recebimento": {
            "$ref": "#/components/schemas/recebimentoResponse"
          },
          "pagamento": {
            "$ref": "#/components/schemas/pagamentoResponse"
          },
          "boleto": {
            "$ref": "#/components/schemas/boletoResponse"
          },
          "rateios": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/rateioResponse"
            }
          },
          "cheque": {
            "$ref": "#/components/schemas/Api_Financeirocheque"
          },
          "cartao": {
            "$ref": "#/components/schemas/Api_Financeirocartao"
          }
        }
      },
      "financeiroResponseList": {
        "type": "object",
        "properties": {
          "pagination": {
            "$ref": "#/components/schemas/paginacaoResponse"
          },
          "financeiros": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/financeiroResponse"
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
