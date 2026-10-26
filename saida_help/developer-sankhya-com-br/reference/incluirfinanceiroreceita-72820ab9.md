---
id: "https://developer.sankhya.com.br/reference/incluirfinanceiroreceita"
titulo: "Registrar Receitas"
url: "https://developer.sankhya.com.br/reference/incluirfinanceiroreceita"
atualizado_em: "2026-05-27T21:17:01.000Z"
---

# Registrar Receitas

Registra financeiro de receita

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
    "/v1/financeiros/receitas": {
      "post": {
        "tags": [
          "Financeiros Movimentos"
        ],
        "summary": "Registrar Receitas",
        "description": "Registra financeiro de receita",
        "operationId": "incluirFinanceiroReceita",
        "requestBody": {
          "description": "Inclui um financeiro de receita no SankhyaOm.\n",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/financeiroAtualizarIncluir"
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
                  "$ref": "#/components/schemas/retornoMovimentoFinanceiro"
                }
              }
            }
          },
          "400": {
            "description": "Informações Inválidas. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Api_Financeiroretorno400"
                }
              }
            }
          },
          "401": {
            "description": "Não autenticado. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Api_Financeiroretorno40X_50X"
                }
              }
            }
          },
          "403": {
            "description": "Autenticação inválida. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Api_Financeiroretorno40X_50X"
                }
              }
            }
          },
          "404": {
            "description": "Dados não encontrados. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Api_Financeiroretorno404"
                }
              }
            }
          },
          "500": {
            "description": "Erro interno no servidor. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Api_Financeiroretorno40X_50X"
                }
              }
            }
          },
          "501": {
            "description": "Não implementado. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Api_Financeiroretorno40X_50X"
                }
              }
            }
          },
          "502": {
            "description": "Retorno inválido do servidor. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Api_Financeiroretorno40X_50X"
                }
              }
            }
          },
          "503": {
            "description": "Serviço indisponível no momento. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Api_Financeiroretorno40X_50X"
                }
              }
            }
          },
          "504": {
            "description": "Tempo de execução excedido. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.",
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
      "financeiroAtualizarIncluir": {
        "type": "object",
        "description": "Este serviço permite a inclusão e baixa/liquidação financeiros de receita no SankhyaOM.",
        "allOf": [
          {
            "$ref": "#/components/schemas/Api_FinanceirofinanceiroModelo"
          }
        ]
      },
      "Api_FinanceirofinanceiroModelo": {
        "required": [
          "codigoBanco",
          "codigoCentroResultado",
          "codigoContaBancaria",
          "codigoEmpresa",
          "codigoNatureza",
          "codigoParceiro",
          "codigoTipoOperacao",
          "codigoTipoPagamento",
          "dataNegociacao",
          "dataVencimento",
          "numeroNota",
          "numeroParcela",
          "valorParcela"
        ],
        "type": "object",
        "properties": {
          "codigoEmpresa": {
            "type": "integer",
            "description": "Insira o código da Empresa para realizar a inclusão do Financeiro. Esse código é facilmente acessível através da nossa API, na entidade \"Empresa\" (CODEMP). Obtenha essa informação e mantenha seus registros sempre atualizados. Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "example": 1
          },
          "codigoTipoOperacao": {
            "type": "integer",
            "description": "Insira o código do Tipo de Operação para realizar a inclusão do Financeiro. Esse código é facilmente acessível através da nossa API, na entidade \"TipoOperacao\" (CODTIPOPER) com o critério TIPMOV = 'I'. Obtenha essa informação e mantenha seus registros sempreatualizados. Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "example": 108
          },
          "codigoNatureza": {
            "type": "integer",
            "description": "Insira o código da Natureza analítica para realizar a inclusão do Financeiro. Esse código é facilmente acessível através da nossa API, na entidade \"Natureza\" (CODNAT). Obtenha essa informação e mantenha seus registros sempreatualizados. Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "example": 101005
          },
          "codigoProjeto": {
            "type": "integer",
            "description": "Insira o código do Projeto analítico para realizar a inclusão do Financeiro. Esse código é facilmente acessível através da nossa API, na entidade \"Projeto\" (CODPROJ). Obtenha essa informação e mantenha seus registros sempreatualizados. Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "example": 10011
          },
          "codigoCentroResultado": {
            "type": "integer",
            "description": "Insira o código do Centro de Resultado analítico para realizar a inclusão do Financeiro. Esse código é facilmente acessível através da nossa API, na entidade \"CentroResultado\" (TGFFIN.CODCENCUS). Obtenha essa informação e mantenha seus registros sempreatualizados. Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "example": 3004002
          },
          "codigoParceiro": {
            "type": "integer",
            "description": "Insira o código do Parceiro para realizar a inclusão do Financeiro. Esse código é facilmente acessível através da nossa API, na entidade \"Parceiro\" (TGFFIN.CODPARC). Obtenha essa informação e mantenha seus registros sempreatualizados. Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "example": 1581
          },
          "codigoBanco": {
            "type": "integer",
            "description": "Insira o código do Banco para realizar a inclusão do Financeiro. Esse código é facilmente acessível através da nossa API, na entidade \"Banco\" (TGFFIN.CODBCO).",
            "example": 1
          },
          "codigoContaBancaria": {
            "type": "integer",
            "description": "Insira o código da Conta Bancária para realizar a inclusão do Financeiro. Esse código é facilmente acessível através da nossa API, na entidade \"ContaBancaria\" (TGFFIN.CODCTABCOINT). Inserindo o código da conta, o campo Banco (TGFFIN.CODBCO) na movimentação financeiro será preenchido conforme o código do banco vinculado no cadastro da conta.  Obtenha essa informação e mantenha seus registros sempre atualizados. Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "example": 42
          },
          "codigoMoeda": {
            "type": "integer",
            "description": "Código da moeda (TGFFIN.CODMOEDA).",
            "example": 22
          },
          "codigoTipoPagamento": {
            "type": "integer",
            "description": "Tipo de Título para o respectivo financeiro. Essa informação deve ser obtida previamente pela entidade \"TipoTitulo\" (TGFFIN.CODTIPTIT). Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "example": 19
          },
          "numeroNota": {
            "type": "integer",
            "description": "Insira o número da Nota.",
            "example": 33569
          },
          "dataNegociacao": {
            "type": "string",
            "description": "Data de negociação do financeiro (TGFFIN.DTNEG).",
            "example": "2025-02-11"
          },
          "dataVencimento": {
            "type": "string",
            "description": "Data do vencimento do financeiro (TGFFIN.DTVENC).",
            "example": "2025-02-11"
          },
          "numeroParcela": {
            "type": "integer",
            "description": "Numero da Parcela (TGFFIN.DESDOBRAMENTO).",
            "example": 1
          },
          "valorParcela": {
            "type": "number",
            "description": "Valor total da parcela (TGFFIN.VLRDESDOB).",
            "example": 3.38
          },
          "maiorNumeroParcela": {
            "type": "integer",
            "description": "Maior número de parcela do financeiro, considerando todas as parcelas da mesma nota (máximo de TGFFIN.DESDOBRAMENTO por NUNOTA).",
            "example": 10
          },
          "nomeEmpresa": {
            "type": "string",
            "description": "Nome da empresa vinculada ao financeiro (TSIEMP.NOMEFANTASIA).",
            "example": "TECH SOLUTIONS"
          },
          "nomeTipoOperacao": {
            "type": "string",
            "description": "Descrição do tipo de operação do financeiro (TGFTOP.DESCROPER).",
            "example": "VENDAS PARA FORA DO ESTADO"
          },
          "nomeNatureza": {
            "type": "string",
            "description": "Descrição da natureza financeira (TGFNAT.DESCRNAT).",
            "example": "RECEITA COM VENDAS"
          },
          "nomeProjeto": {
            "type": "string",
            "description": "Descrição do projeto vinculado ao financeiro (TGFPRO.DESCRPROJ).",
            "example": "SEM PROJETO"
          },
          "nomeCentroResultado": {
            "type": "string",
            "description": "Descrição do centro de resultado (TSICUS.DESCRCENCUS).",
            "example": "VENDAS PRONTA ENTREGA"
          },
          "nomeParceiro": {
            "type": "string",
            "description": "Nome do parceiro vinculado ao financeiro (TGFPAR.NOMEPARC).",
            "example": "JOÃO DA SILVA"
          },
          "cheque": {
            "$ref": "#/components/schemas/Api_Financeirocheque"
          },
          "cartao": {
            "$ref": "#/components/schemas/Api_Financeirocartao"
          },
          "boleto": {
            "$ref": "#/components/schemas/boleto"
          },
          "rateios": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/rateio"
            }
          }
        },
        "description": "Os atributos apresentados aqui estão vinculados ao financeiro da nota, mapeados pela entidade \"Financeiro\". Para personalizar a integração é possível enviar os atributos dessa entidade, como \"DTVENC\" em vez de \"dataVencimento\". Além disso, é possível utilizar campos que, embora não estejam detalhados nesta documentação, fazem parte do dicionário de dados."
      },
      "rateio": {
        "required": [
          "codigoCentroResultado",
          "codigoNatureza",
          "percentual"
        ],
        "type": "object",
        "properties": {
          "codigoNatureza": {
            "type": "integer",
            "description": "Insira o código da Natureza para realizar a inclusão do Financeiro. Esse código é facilmente acessível através da nossa API, na entidade \"Natureza\" (TGFRAT.CODNAT). Obtenha essa informação e mantenha seus registros sempreatualizados. Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "example": 101005
          },
          "codigoProjeto": {
            "type": "integer",
            "description": "Insira o código do Projeto para realizar a inclusão do Financeiro. Esse código é facilmente acessível através da nossa API, na entidade \"Projeto\" (TGFRAT.CODPROJ). Obtenha essa informação e mantenha seus registros sempreatualizados. Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "example": 10011
          },
          "codigoCentroResultado": {
            "type": "integer",
            "description": "Insira o código do Centro de Resultado para realizar a inclusão do Financeiro. Esse código é facilmente acessível através da nossa API, na entidade \"CentroResultado\" (TGFRAT.CODCENCUS). Obtenha essa informação e mantenha seus registros sempreatualizados. Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "example": 3004002
          },
          "codigoParceiro": {
            "type": "integer",
            "description": "Insira o código do Parceiro para realizar a inclusão do Financeiro. Esse código é facilmente acessível através da nossa API, na entidade \"Parceiro\" (TGFRAT.CODPARC). Obtenha essa informação e mantenha seus registros sempreatualizados. Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "example": 1581
          },
          "codigoContaContabil": {
            "type": "integer",
            "description": "Insira o código da Conta Bancária para realizar a inclusão do Financeiro. Esse código é facilmente acessível através da nossa API, na entidade \"ContaBancaria\" (TGFRAT.CODCTABCOINT). Obtenha essa informação e mantenha seus registros sempre atualizados. Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "example": 42
          },
          "percentual": {
            "type": "number",
            "description": "Percentual do rateio (TGFRAT.PERCRATEIO)",
            "example": 50
          }
        },
        "description": "Esta informação deve ser enviada \"apenas\" quando o financeiro estiver rateado. Recebe dados do rateio."
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
      "boleto": {
        "required": [
          "codigoBarras",
          "dataPagamento",
          "linhaDigitavel",
          "nossoNumero"
        ],
        "type": "object",
        "properties": {
          "codigoBarras": {
            "type": "string",
            "description": "Código de Barras do boleto (TGFFIN.CODBARRA)",
            "example": "\"341067330330018805201725766099\""
          },
          "nossoNumero": {
            "type": "string",
            "description": "\"Nosso numero\" do boleto (TGFFIN.NOSSONUM)",
            "example": "568454558"
          },
          "linhaDigitavel": {
            "type": "string",
            "description": "\"Nosso numero\" do boleto (TGFFIN.LINHADIGITAL)",
            "example": "0018801122446653232464655662245"
          },
          "numeroRemessa": {
            "type": "string",
            "description": "\"Nosso numero\" do boleto (TGFFIN.NUMREMESSA)",
            "example": "0012"
          },
          "dataPagamento": {
            "type": "string",
            "description": "Data e Hora do Pagamento do Boleto (TGFFIN.TIMDHBAIXA)",
            "example": "13/03/2025 17:22:00"
          }
        },
        "description": "Esta informação deve ser enviada \"apenas\" quando a opção de pagamento (atributo \"codigoTipoPagamento\") seja do subtipo \"A prazo\" (\"2\"). Recebe dados de boleto utilizado como meio de pagamento"
      },
      "retornoMovimentoFinanceiro": {
        "required": [
          "codigo"
        ],
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
            "type": "string",
            "example": "Financeiro Incluído/Atualizado/Baixado com sucesso."
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
