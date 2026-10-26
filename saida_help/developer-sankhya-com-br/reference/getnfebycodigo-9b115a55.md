---
id: "https://developer.sankhya.com.br/reference/getnfebycodigo"
titulo: "Consulta Específica de Nota Fiscal Eletrônica (Detalhada)"
url: "https://developer.sankhya.com.br/reference/getnfebycodigo"
atualizado_em: "2026-05-13T12:41:23.000Z"
---

# Consulta Específica de Nota Fiscal Eletrônica (Detalhada)

Retorna a estrutura completa (Descrições, Cliente, Itens e Financeiro).


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
      "name": "Vendas NF-e",
      "description": "Consulta Nota Fiscal Eletrônica modelo 55"
    }
  ],
  "paths": {
    "/v1/vendas/nfe/{codigoNota}": {
      "get": {
        "tags": [
          "Vendas NF-e"
        ],
        "summary": "Consulta Específica de Nota Fiscal Eletrônica (Detalhada)",
        "description": "Retorna a estrutura completa (Descrições, Cliente, Itens e Financeiro).\n",
        "operationId": "getNfeByCodigo",
        "security": [
          {
            "VendasNFeBearer": []
          }
        ],
        "parameters": [
          {
            "name": "codigoNota",
            "in": "path",
            "description": "Código Interno da Nota.",
            "required": true,
            "schema": {
              "type": "integer",
              "format": "int64",
              "example": 12540
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/RetornoNfe"
                }
              }
            }
          },
          "400": {
            "description": "Erro.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/RetornoErro"
                }
              }
            }
          },
          "401": {
            "description": "Não autorizado."
          },
          "404": {
            "description": "Não encontrada.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/RetornoErro"
                }
              }
            }
          },
          "500": {
            "description": "Erro interno."
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
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
      "RetornoNfe": {
        "allOf": [
          {
            "$ref": "#/components/schemas/BaseVenda"
          },
          {
            "type": "object",
            "properties": {
              "chaveNFe": {
                "type": "string",
                "example": "35240612345678000199550010000125401002541002"
              },
              "statusNFe": {
                "type": "string",
                "example": "5"
              },
              "numeroProtocoloNFe": {
                "type": "string",
                "example": "135240008899774"
              },
              "dataProtocoloNFe": {
                "type": "string",
                "format": "date-time",
                "example": "2024-06-15T10:30:00"
              },
              "numeroAleatorioNFe": {
                "type": "string",
                "example": "98765432"
              },
              "loteNFe": {
                "type": "string",
                "example": "20240055"
              },
              "numeroRegistroDPEC": {
                "type": "string",
                "example": "998877"
              },
              "dataRegEPEC": {
                "type": "string",
                "format": "date-time",
                "example": "2024-06-15T09:00:00"
              },
              "xmlNFe": {
                "type": "string",
                "example": "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz48bmZlUHJvYyB2ZXJzaW9uPSI0LjAwIiB4bWxucz0iaHR0cDovL3d3dy5wb3J0YWxmaXNjYWwuaW5mLmJyL25mZSI+Li4uPC9uZmVQcm9jPg=="
              },
              "codigoPedidoOrigem": {
                "type": "integer",
                "example": 15420
              },
              "reformaTributaria": {
                "$ref": "#/components/schemas/ReformaTributaria"
              },
              "itens": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/ItemNfe"
                }
              },
              "financeiros": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/FinanceiroNfe"
                }
              }
            }
          }
        ]
      },
      "ItemNfe": {
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
            "description": "Exige valorTotal maior que zero para cálculo do percentual de desconto do item.",
            "example": 100
          },
          "codigoLocalEstoque": {
            "type": "integer",
            "example": 2,
            "description": "CODLOCALORIG. Local de estoque de origem do item, necessário quando existe controle de estoque por local. Essa informação deve ser obtida previamente pela entidade \"Estoque\" (CODLOCAL). Deve existir em TGFLOC; caso contrário, HTTP 404. Opcional: quando ausente, o local é resolvido pelo parâmetro com.local.padrao do usuário autenticado, desde que o produto use local (TGFPRO.USALOCAL) e o parâmetro com.utiliza.local esteja ativo; na sequência, pelo local padrão da empresa (TGFEMP.LOCALPAD) quando o parâmetro com.utiliza.local.padrao.fast estiver ativo. Sem nenhum deles, o item é gravado com local zero."
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
              "$ref": "#/components/schemas/Impostos"
            }
          },
          "camposNativos": {
            "type": "object",
            "description": "Colunas nativas adicionais de TGFITE, no formato { \"NOMECOLUNA\": valor }.",
            "additionalProperties": true
          },
          "camposAdicionais": {
            "type": "object",
            "description": "Campos customizados (prefixo AD_) de TGFITE, no formato { \"AD_CAMPO\": valor }.",
            "additionalProperties": true
          }
        }
      },
      "FinanceiroNfe": {
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
          },
          "camposNativos": {
            "type": "object",
            "description": "Colunas nativas adicionais de TGFFIN, no formato { \"NOMECOLUNA\": valor }.",
            "additionalProperties": true
          },
          "camposAdicionais": {
            "type": "object",
            "description": "Campos customizados (prefixo AD_) de TGFFIN, no formato { \"AD_CAMPO\": valor }.",
            "additionalProperties": true
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
      "Impostos": {
        "type": "object",
        "properties": {
          "tipo": {
            "type": "string",
            "description": "icms, icms-st, ipi, pis e cofins gravam campos planos do item (TGFITE/TGFDIN); ibs, cbs e is gravam em TGFDIN como impostos de reforma tributária e alimentam a totalização automática do cabeçalho. Para tipo=icms, os atributos valorBaseReduzida, valorBaseFCP, percentualFCP, valorFCP, valorBaseDIFAL, valorBaseFCPInterno, percentualFCPInterno, valorFCPInterno, aliquotaInternaDestino, percentualPartilhaDIFAL, valorDIFALDestino e valorDIFALRemetente também são aceitos e gravados em TGFDIN (CODIMP=1), mas exigem que aliquota também seja informada: se qualquer um deles vier sem aliquota, a API rejeita com HTTP 400.",
            "enum": [
              "icms",
              "icms-st",
              "ipi",
              "pis",
              "cofins",
              "ibs",
              "cbs",
              "is"
            ],
            "example": "ibs"
          },
          "cst": {
            "type": "string",
            "example": "00"
          },
          "tributacaoMunicipio": {
            "type": "string",
            "example": "140801"
          },
          "classificacaoTributaria": {
            "type": "integer",
            "example": 200
          },
          "aliquota": {
            "type": "number",
            "format": "double",
            "example": 26.5
          },
          "aliquotaEfetivaRegular": {
            "type": "number",
            "format": "double",
            "example": 26.5
          },
          "aliquotaUnidadeMedida": {
            "type": "number",
            "format": "double",
            "example": 0
          },
          "aliquotaEfetivaBaseCalculo": {
            "type": "number",
            "format": "double",
            "example": 26.5
          },
          "reducaoAliquota": {
            "type": "number",
            "format": "double",
            "example": 0
          },
          "percentualFCP": {
            "type": "number",
            "format": "double",
            "description": "Percentual do FCP. Para tipo=icms, grava TGFDIN.PERCFCP (CODIMP=1).",
            "example": 0
          },
          "valorBaseFCP": {
            "type": "number",
            "format": "double",
            "description": "Base de cálculo do FCP do item. Para tipo=icms, grava TGFDIN.BASEFCP (CODIMP=1).",
            "example": 0
          },
          "valorBaseDIFAL": {
            "type": "number",
            "format": "double",
            "description": "Base de cálculo do DIFAL do item. Para tipo=icms, grava TGFDIN.BASEDIFAL (CODIMP=1).",
            "example": 43.64
          },
          "valorBaseFCPInterno": {
            "type": "number",
            "format": "double",
            "description": "Base de cálculo do FCP interno do item. Para tipo=icms, grava TGFDIN.BASEFCPINT (CODIMP=1).",
            "example": 0
          },
          "percentualFCPInterno": {
            "type": "number",
            "format": "double",
            "description": "Percentual do FCP interno do item. Para tipo=icms, grava TGFDIN.PERCFCPINT (CODIMP=1).",
            "example": 0
          },
          "valorFCPInterno": {
            "type": "number",
            "format": "double",
            "description": "Valor do FCP interno do item. Para tipo=icms, grava TGFDIN.VLRFCPINT (CODIMP=1).",
            "example": 0
          },
          "aliquotaInternaDestino": {
            "type": "number",
            "format": "double",
            "description": "Alíquota interna do estado de destino. Para tipo=icms, grava TGFDIN.ALIQINTDEST (CODIMP=1).",
            "example": 19.5
          },
          "percentualPartilhaDIFAL": {
            "type": "number",
            "format": "double",
            "description": "Percentual de partilha do DIFAL entre origem e destino. Para tipo=icms, grava TGFDIN.PERCPARTDIFAL (CODIMP=1).",
            "example": 100
          },
          "valorDIFALDestino": {
            "type": "number",
            "format": "double",
            "description": "Valor do DIFAL devido ao estado de destino. Para tipo=icms, grava TGFDIN.VLRDIFALDEST (CODIMP=1).",
            "example": 6.76
          },
          "valorDIFALRemetente": {
            "type": "number",
            "format": "double",
            "description": "Valor do DIFAL devido ao estado do remetente. Para tipo=icms, grava TGFDIN.VLRDIFALREM (CODIMP=1).",
            "example": 0
          },
          "percentualReducaoAliquotaGovernamental": {
            "type": "number",
            "format": "double",
            "example": 60
          },
          "percentualDiferimento": {
            "type": "number",
            "format": "double",
            "example": 10
          },
          "valorBase": {
            "type": "number",
            "format": "double",
            "example": 1000
          },
          "valorBaseReduzida": {
            "type": "number",
            "format": "double",
            "description": "Base de cálculo reduzida do imposto. Para tipo=icms, grava TGFDIN.BASERED (CODIMP=1). O valor enviado é gravado como recebido, mesmo 0 (sem redução) — a API não assume BASERED = base cheia por conta própria.",
            "example": 0
          },
          "valorImposto": {
            "type": "number",
            "format": "double",
            "example": 106
          },
          "valorFCP": {
            "type": "number",
            "format": "double",
            "description": "Valor do FCP. Para tipo=icms, grava TGFDIN.VLRFCP (CODIMP=1).",
            "example": 0
          },
          "valorRegular": {
            "type": "number",
            "format": "double",
            "example": 106
          },
          "valorDiferimento": {
            "type": "number",
            "format": "double",
            "example": 10.6
          },
          "valorTributoDevolvido": {
            "type": "number",
            "format": "double",
            "example": 0
          }
        }
      },
      "RetornoErro": {
        "type": "object",
        "properties": {
          "code": {
            "type": "string",
            "example": "INVALID_REQUEST"
          },
          "message": {
            "type": "string",
            "example": "Erro na requisição"
          },
          "details": {
            "type": "string",
            "example": "O código da nota não foi encontrado."
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
      },
      "VendasNFeBearer": {
        "type": "apiKey",
        "name": "Authorization",
        "in": "header",
        "description": "Insira o token com o prefixo Bearer"
      }
    }
  }
}
```
