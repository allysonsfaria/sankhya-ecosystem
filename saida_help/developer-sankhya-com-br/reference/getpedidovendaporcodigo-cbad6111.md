---
id: "https://developer.sankhya.com.br/reference/getpedidovendaporcodigo"
titulo: "Consultar Pedido de Venda por Código"
url: "https://developer.sankhya.com.br/reference/getpedidovendaporcodigo"
atualizado_em: "2026-10-22T11:38:21.000Z"
---

# Consultar Pedido de Venda por Código

Consulta um pedido de venda específico retornando todos os dados do pedido confirmado.

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
      "name": "Vendas Pedidos",
      "description": "Enviar Pedidos de Venda"
    }
  ],
  "paths": {
    "/v1/vendas/pedidos/{codigoPedido}": {
      "get": {
        "tags": [
          "Vendas Pedidos"
        ],
        "summary": "Consultar Pedido de Venda por Código",
        "description": "Consulta um pedido de venda específico retornando todos os dados do pedido confirmado.",
        "operationId": "getPedidoVendaPorCodigo",
        "parameters": [
          {
            "name": "codigoPedido",
            "in": "path",
            "description": "Informe neste atributo o \"código do pedido\" desejado\n",
            "required": true,
            "schema": {
              "type": "integer",
              "format": "int64",
              "example": 4599
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Operação bem sucedida",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/RetornoPedido"
                }
              }
            }
          },
          "400": {
            "description": "Informações Inválidas. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/retorno400"
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
                  "$ref": "#/components/schemas/Pedido_de_Vendasretorno404"
                }
              }
            }
          },
          "409": {
            "description": "Conflito. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/retorno40X_50X"
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
            "Bearer": []
          }
        ]
      }
    }
  },
  "components": {
    "schemas": {
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
      "Endereco": {
        "type": "object",
        "properties": {
          "entrega": {
            "type": "boolean",
            "example": true
          },
          "nomeContato": {
            "type": "string",
            "example": "Maria Roberta"
          },
          "email": {
            "type": "string",
            "example": "maria.roberta@provedor.com.br"
          },
          "logradouro": {
            "type": "string",
            "example": "Rua Maria Roberta"
          },
          "numero": {
            "type": "string",
            "example": "10"
          },
          "complemento": {
            "type": "string",
            "example": "Apto 104"
          },
          "bairro": {
            "type": "string",
            "example": "Centro"
          },
          "cidade": {
            "type": "string",
            "example": "Uberlândia"
          },
          "codigoIbge": {
            "type": "integer",
            "example": 11155566
          },
          "uf": {
            "type": "string",
            "example": "MG"
          },
          "cep": {
            "type": "string",
            "example": "38400000"
          }
        }
      },
      "Cliente": {
        "type": "object",
        "properties": {
          "atualizar": {
            "type": "boolean",
            "example": false
          },
          "tipo": {
            "type": "string",
            "example": "PF"
          },
          "cnpjCpf": {
            "type": "string",
            "example": "12315914799"
          },
          "ieRg": {
            "type": "string",
            "example": "12315914799"
          },
          "nome": {
            "type": "string",
            "example": "José da Silva"
          },
          "razao": {
            "type": "string",
            "example": "José da Silva ME"
          },
          "email": {
            "type": "string",
            "example": "contato@provedor.com.br"
          },
          "telefoneDdd": {
            "type": "string",
            "example": "34"
          },
          "telefoneNumero": {
            "type": "string",
            "example": "912349966"
          },
          "endereco": {
            "$ref": "#/components/schemas/Endereco"
          }
        }
      },
      "BaseVenda": {
        "type": "object",
        "properties": {
          "codigoEmpresa": {
            "type": "integer",
            "example": 1
          },
          "nomeEmpresa": {
            "type": "string",
            "example": "Sankhya Gestão de Negócios Matriz"
          },
          "cliente": {
            "$ref": "#/components/schemas/Cliente"
          },
          "confirmada": {
            "type": "boolean",
            "example": true
          },
          "pendente": {
            "type": "boolean",
            "example": false
          },
          "statusWMS": {
            "type": "integer",
            "example": 2
          },
          "situacaoWMS": {
            "type": "integer",
            "example": 17
          },
          "statusConferencia": {
            "type": "integer",
            "example": 6
          },
          "dataNegociacao": {
            "type": "string",
            "example": "15/06/2024"
          },
          "dataHoraAlteracao": {
            "type": "string",
            "example": "15/06/2024 14:45:30"
          },
          "numeroNota": {
            "type": "integer",
            "example": 254100
          },
          "codigoNota": {
            "type": "integer",
            "example": 12540
          },
          "serieNota": {
            "type": "string",
            "example": "1"
          },
          "codigoTipoNegociacao": {
            "type": "integer",
            "example": 110
          },
          "nomeTipoNegociacao": {
            "type": "string",
            "example": "Venda de Mercadoria Nacional"
          },
          "codigoTipoOperacao": {
            "type": "integer",
            "example": 1200
          },
          "nomeTipoOperacao": {
            "type": "string",
            "example": "Venda Estadual de Produção Própria"
          },
          "codigoNatureza": {
            "type": "integer",
            "example": 30100
          },
          "nomeNatureza": {
            "type": "string",
            "example": "Venda de Produção do Estabelecimento"
          },
          "codigoCentroResultado": {
            "type": "integer",
            "example": 10100
          },
          "nomeCentroResultado": {
            "type": "string",
            "example": "Departamento Comercial SP"
          },
          "codigoProjeto": {
            "type": "integer",
            "example": 202401
          },
          "nomeProjeto": {
            "type": "string",
            "example": "Expansão Sudeste 2024"
          },
          "codigoContrato": {
            "type": "integer",
            "example": 4502
          },
          "codigoVendedor": {
            "type": "integer",
            "example": 55
          },
          "nomeVendedor": {
            "type": "string",
            "example": "Carlos Eduardo Silva"
          },
          "codigoContato": {
            "type": "integer",
            "example": 302
          },
          "nomeContato": {
            "type": "string",
            "example": "Maria Paula"
          },
          "codigoMoeda": {
            "type": "integer",
            "example": 0
          },
          "nomeMoeda": {
            "type": "string",
            "example": "Real"
          },
          "valorMoeda": {
            "type": "number",
            "format": "double",
            "example": 0
          },
          "valorNota": {
            "type": "number",
            "format": "double",
            "example": 5450
          },
          "descontoTotal": {
            "type": "number",
            "format": "double",
            "example": 250
          },
          "valorSeguro": {
            "type": "number",
            "format": "double",
            "example": 45
          },
          "valorDestaque": {
            "type": "number",
            "format": "double",
            "example": 0
          },
          "valorVendor": {
            "type": "number",
            "format": "double",
            "example": 0
          },
          "valorJuro": {
            "type": "number",
            "format": "double",
            "example": 0
          },
          "valorOutros": {
            "type": "number",
            "format": "double",
            "example": 85
          },
          "valorEmbalagem": {
            "type": "number",
            "format": "double",
            "example": 20
          },
          "valorFrete": {
            "type": "number",
            "format": "double",
            "example": 180
          },
          "vencimentoFrete": {
            "type": "string",
            "format": "date",
            "example": "2024-07-15"
          },
          "codigoOrdemCarga": {
            "type": "integer",
            "example": 995512
          },
          "codigoVeiculo": {
            "type": "integer",
            "example": 45
          },
          "placaVeiculo": {
            "type": "string",
            "example": "ABC-1234"
          },
          "codigoMotorista": {
            "type": "integer",
            "example": 102
          },
          "nomeMotorista": {
            "type": "string",
            "example": "Roberto Mendes"
          },
          "codigoTransportadora": {
            "type": "integer",
            "example": 800
          },
          "nomeTransportadora": {
            "type": "string",
            "example": "Expresso Logística Rápida"
          },
          "codigoRemetente": {
            "type": "integer",
            "example": 1
          },
          "nomeRemetente": {
            "type": "string",
            "example": "Sankhya Gestão de Negócios Matriz"
          },
          "codigoDestinatario": {
            "type": "integer",
            "example": 20500
          },
          "nomeDestinatario": {
            "type": "string",
            "example": "Tech Solutions Comercio e Servicos LTDA"
          },
          "quantidadeVolumes": {
            "type": "integer",
            "example": 12
          },
          "numeracaoVolumes": {
            "type": "string",
            "example": "1/12 a 12/12"
          },
          "lacres": {
            "type": "string",
            "example": "LACRE-001254"
          },
          "pesoBruto": {
            "type": "number",
            "format": "double",
            "example": 245.5
          },
          "cifFob": {
            "type": "integer",
            "enum": [
              1,
              2,
              3,
              4,
              5,
              6
            ],
            "example": 1
          },
          "tipoFrete": {
            "type": "integer",
            "enum": [
              1,
              2
            ],
            "example": 2
          },
          "baseICMSFrete": {
            "type": "number",
            "format": "double",
            "example": 180
          },
          "icmsFrete": {
            "type": "number",
            "format": "double",
            "example": 21.6
          }
        }
      },
      "Cheque": {
        "type": "object",
        "properties": {
          "codigoBarras": {
            "type": "string",
            "example": "341067330330018805201725766099"
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
            "type": "integer",
            "example": 1880
          },
          "nome": {
            "type": "string",
            "example": "José da Silva Souza"
          },
          "cnpjCpf": {
            "type": "string",
            "example": "14532515955"
          }
        }
      },
      "Cartao": {
        "type": "object",
        "properties": {
          "bandeira": {
            "type": "string",
            "enum": [
              "01",
              "02",
              "03",
              "04",
              "05",
              "06",
              "07",
              "08",
              "09",
              "99"
            ],
            "example": "02"
          },
          "autorizacao": {
            "type": "integer",
            "example": 4581596
          }
        }
      },
      "ReformaTributaria": {
        "type": "object",
        "properties": {
          "valorCreditoPresumido": {
            "type": "number",
            "format": "double",
            "example": 0
          },
          "valorCreditoPresumidoSuspensivaCBS": {
            "type": "number",
            "format": "double",
            "example": 0
          },
          "valorCreditoPresumidoSuspensivaIBS": {
            "type": "number",
            "format": "double",
            "example": 0
          },
          "valorTotalImposto": {
            "type": "number",
            "format": "double",
            "example": 1325
          },
          "valorDevolucaoCBS": {
            "type": "number",
            "format": "double",
            "example": 0
          },
          "valorDevolucaoTributosIBSUF": {
            "type": "number",
            "format": "double",
            "example": 0
          },
          "valorDevolucaoTributosMunicipio": {
            "type": "number",
            "format": "double",
            "example": 0
          },
          "valorDiferimento": {
            "type": "number",
            "format": "double",
            "example": 0
          },
          "valorDiferimentoIBSUF": {
            "type": "number",
            "format": "double",
            "example": 0
          },
          "valorDiferimentoMunicipioIBS": {
            "type": "number",
            "format": "double",
            "example": 0
          },
          "valorIBSUF": {
            "type": "number",
            "format": "double",
            "example": 662.5
          },
          "valorIBSMunicipio": {
            "type": "number",
            "format": "double",
            "example": 150
          },
          "valorImpostoSeletivo": {
            "type": "number",
            "format": "double",
            "example": 0
          },
          "valorBaseCalculo": {
            "type": "number",
            "format": "double",
            "example": 5000
          },
          "valorTotalDocumento": {
            "type": "number",
            "format": "double",
            "example": 6325
          }
        }
      },
      "RetornoPedido": {
        "allOf": [
          {
            "$ref": "#/components/schemas/BaseVenda"
          },
          {
            "type": "object",
            "properties": {
              "reformaTributaria": {
                "$ref": "#/components/schemas/ReformaTributaria"
              },
              "itens": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/Pedido_de_VendasItemNfe"
                }
              },
              "financeiros": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/Pedido_de_VendasFinanceiroNfe"
                }
              }
            }
          }
        ]
      },
      "Pedido_de_VendasFinanceiroNfe": {
        "type": "object",
        "properties": {
          "sequencia": {
            "type": "integer",
            "example": 1
          },
          "tipoPagamento": {
            "type": "integer",
            "example": 19
          },
          "cheque": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Cheque"
              }
            ]
          },
          "cartao": {
            "$ref": "#/components/schemas/Cartao"
          },
          "dataVencimento": {
            "type": "string",
            "example": "30/05/2024"
          },
          "dataBaixa": {
            "type": "string",
            "example": "30/05/2024"
          },
          "valorParcela": {
            "type": "number",
            "format": "double",
            "example": 3.38
          },
          "idTransacao": {
            "type": "string",
            "example": "dadotiuiwnlkeuhcnhlahdiwlaoaokd48ge55x"
          }
        }
      },
      "Pedido_de_VendasItemNfe": {
        "type": "object",
        "properties": {
          "sequencia": {
            "type": "integer",
            "example": 1
          },
          "codigoProduto": {
            "type": "integer",
            "example": 1050
          },
          "descricaoProduto": {
            "type": "string",
            "example": "Notebook Gamer i7 16GB"
          },
          "quantidade": {
            "type": "number",
            "format": "double",
            "example": 2
          },
          "unidade": {
            "type": "string",
            "example": "UN"
          },
          "valorUnitario": {
            "type": "number",
            "format": "double",
            "example": 2500
          },
          "valorTotal": {
            "type": "number",
            "format": "double",
            "example": 5000
          },
          "cfop": {
            "type": "string",
            "example": "5101"
          },
          "ncm": {
            "type": "string",
            "example": "84714100"
          },
          "cst": {
            "type": "string",
            "example": "000"
          },
          "valorDesconto": {
            "type": "number",
            "format": "double",
            "example": 100
          },
          "valorICMS": {
            "type": "number",
            "format": "double",
            "example": 900
          },
          "valorIPI": {
            "type": "number",
            "format": "double",
            "example": 250
          },
          "impostos": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Pedido_de_VendasImpostos"
            }
          }
        }
      },
      "Pedido_de_VendasImpostos": {
        "type": "object",
        "properties": {
          "tipo": {
            "type": "string",
            "description": "Tipo do imposto.\n",
            "example": "ibs",
            "enum": [
              "icms",
              "icms-st",
              "ipi",
              "ibs",
              "cbs",
              "is"
            ]
          },
          "cst": {
            "type": "string",
            "description": "Código de Situação Tributária.\n",
            "example": "00"
          },
          "tributacaoMunicipio": {
            "type": "string",
            "description": "Código de tributação do município. Utilizar como referencia a Tabela de Código de Classificação Tributária do IBS/CBS.",
            "example": "140801"
          },
          "classificacaoTributaria": {
            "type": "integer",
            "description": "Código de Classificação Tributária. Utilizar como referencia a Tabela de Código de Classificação Tributária do IBS/CBS.",
            "example": 200
          },
          "aliquota": {
            "type": "number",
            "description": "Aliquota do imposto\n",
            "format": "double",
            "example": 26.5
          },
          "aliquotaEfetivaRegular": {
            "type": "number",
            "description": "Alíquota efetiva regular do CBS ou do IBS",
            "format": "double",
            "example": 26.5
          },
          "aliquotaUnidadeMedida": {
            "type": "number",
            "description": "Alíquota específica por unidade de medida apropriada",
            "format": "double",
            "example": 0
          },
          "aliquotaEfetivaBaseCalculo": {
            "type": "number",
            "description": "Alíquota Efetiva que será aplicada a Base de Cálculo",
            "format": "double",
            "example": 26.5
          },
          "reducaoAliquota": {
            "type": "number",
            "description": "Percentual da redução de alíquota",
            "format": "double",
            "example": 0
          },
          "percentualFCP": {
            "type": "number",
            "description": "Percentual do Fundo de Combate a Pobreza (FCP).\n",
            "format": "double",
            "example": 0
          },
          "percentualReducaoAliquotaGovernamental": {
            "type": "number",
            "description": "Percentual da redução de alíquota Governamental",
            "format": "double",
            "example": 60
          },
          "percentualDiferimento": {
            "type": "number",
            "description": "Percentual do diferimento",
            "format": "double",
            "example": 10
          },
          "valorBase": {
            "type": "number",
            "description": "Valor da base de cálculo\n",
            "format": "double",
            "example": 1000
          },
          "valorBaseReduzida": {
            "type": "number",
            "description": "Valor Base Cálc.Reduzida (Já com reduções da Reforma aplicadas)",
            "format": "double",
            "example": 400
          },
          "valorImposto": {
            "type": "number",
            "description": "Valor do imposto calculado",
            "format": "double",
            "example": 106
          },
          "valorFCP": {
            "type": "number",
            "description": "Valor do Fundo de Combate a Pobreza (FCP).\n",
            "format": "double",
            "example": 0
          },
          "valorRegular": {
            "type": "number",
            "description": "Valor do Regular do IBS ou do Município, de acordo com o tipo do imposto enviado.",
            "format": "double",
            "example": 106
          },
          "valorDiferimento": {
            "type": "number",
            "description": "Valor do Diferimento",
            "format": "double",
            "example": 10.6
          },
          "valorTributoDevolvido": {
            "type": "number",
            "description": "Valor do tributo devolvido",
            "format": "double",
            "example": 0
          }
        },
        "description": "Detalhamento dos impostos calculados para o produto (IBS/CBS e Legado)\n"
      },
      "Pedido_de_Vendasretorno404": {
        "type": "object",
        "properties": {
          "statusCode": {
            "type": "integer",
            "format": "int32",
            "example": 404
          },
          "error": {
            "$ref": "#/components/schemas/retornoErro"
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
