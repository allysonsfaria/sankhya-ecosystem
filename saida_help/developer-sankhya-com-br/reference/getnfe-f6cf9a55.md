---
id: "https://developer.sankhya.com.br/reference/getnfe"
titulo: "Consultar Cabeçalho de Notas Fiscais (Modelo 55)"
url: "https://developer.sankhya.com.br/reference/getnfe"
atualizado_em: "2026-05-13T12:41:23.000Z"
---

# Consultar Cabeçalho de Notas Fiscais (Modelo 55)

Retorna uma lista paginada apenas com os dados principais (cabeçalho) das Notas Fiscais modelo 55.
Utiliza o formato padrão com descrições e objeto cliente.


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
    "/v1/vendas/nfe": {
      "get": {
        "tags": [
          "Vendas NF-e"
        ],
        "summary": "Consultar Cabeçalho de Notas Fiscais (Modelo 55)",
        "description": "Retorna uma lista paginada apenas com os dados principais (cabeçalho) das Notas Fiscais modelo 55.\nUtiliza o formato padrão com descrições e objeto cliente.\n",
        "operationId": "getNfe",
        "security": [
          {
            "VendasNFeBearer": []
          }
        ],
        "parameters": [
          {
            "$ref": "#/components/parameters/PageParam"
          },
          {
            "$ref": "#/components/parameters/ModifiedSinceParam"
          },
          {
            "$ref": "#/components/parameters/CodigoEmpresaParam"
          },
          {
            "$ref": "#/components/parameters/CodigoNotaParam"
          },
          {
            "$ref": "#/components/parameters/NumeroNotaParam"
          },
          {
            "$ref": "#/components/parameters/SerieNotaParam"
          },
          {
            "$ref": "#/components/parameters/DataNegociacaoInicioParam"
          },
          {
            "$ref": "#/components/parameters/DataNegociacaoFinalParam"
          },
          {
            "$ref": "#/components/parameters/CodigoClienteParam"
          },
          {
            "$ref": "#/components/parameters/ConfirmadaParam"
          },
          {
            "$ref": "#/components/parameters/PendenteParam"
          },
          {
            "$ref": "#/components/parameters/StatusNFeParam"
          },
          {
            "$ref": "#/components/parameters/CodigoNaturezaParam"
          },
          {
            "$ref": "#/components/parameters/CodigoCentroResultadoParam"
          },
          {
            "$ref": "#/components/parameters/CodigoProjetoParam"
          },
          {
            "$ref": "#/components/parameters/CodigoContratoParam"
          },
          {
            "$ref": "#/components/parameters/CodigoOrdemCargaParam"
          }
        ],
        "responses": {
          "200": {
            "description": "Sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/RespostaPaginadaNfeCabecalho"
                }
              }
            }
          },
          "400": {
            "description": "Erro na requisição.",
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
          "500": {
            "description": "Erro interno."
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "RespostaPaginadaNfeCabecalho": {
        "type": "object",
        "properties": {
          "metadados": {
            "$ref": "#/components/schemas/Metadados"
          },
          "registros": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/RetornoNfeCabecalho"
            }
          }
        }
      },
      "Metadados": {
        "type": "object",
        "properties": {
          "paginaAtual": {
            "type": "integer",
            "example": 1
          },
          "totalPaginas": {
            "type": "integer",
            "example": 12
          },
          "totalRegistros": {
            "type": "integer",
            "example": 580
          },
          "possuiMaisPaginas": {
            "type": "boolean",
            "example": true
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
      "RetornoNfeCabecalho": {
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
              }
            }
          }
        ]
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
    },
    "parameters": {
      "PageParam": {
        "name": "page",
        "in": "query",
        "description": "Informe neste atributo a \"página\" desejada",
        "required": true,
        "schema": {
          "type": "integer",
          "format": "int64",
          "example": 1,
          "minimum": 1
        }
      },
      "ModifiedSinceParam": {
        "name": "modifiedSince",
        "in": "query",
        "description": "Data hora da ultima modificação. Quando este parametro é enviado, o serviço retorana apenas registros que tiveram modificação deste da data/hora enviada. Vale ressaltar que este recurso é condicionada a utilização do [Log de Alterações no SankhyaOm](https://developer.sankhya.com.br/reference/get_logalteracoestabelas) no ambiente do cliente. O formato deve ser o seguinte: AAAA-MM-DDTHH:MM:SS",
        "required": false,
        "schema": {
          "type": "string",
          "example": "2025-01-28T16:24:00"
        }
      },
      "CodigoEmpresaParam": {
        "name": "codigoEmpresa",
        "in": "query",
        "description": "Código da Empresa",
        "required": false,
        "schema": {
          "type": "integer",
          "example": 1
        }
      },
      "CodigoNotaParam": {
        "name": "codigoNota",
        "in": "query",
        "description": "Código Interno da Nota (NUNOTA).",
        "required": false,
        "schema": {
          "type": "integer",
          "format": "int64",
          "example": 12540
        }
      },
      "NumeroNotaParam": {
        "name": "numeroNota",
        "in": "query",
        "description": "Número da Nota Fiscal (NUMNOTA).",
        "required": false,
        "schema": {
          "type": "integer",
          "format": "int64",
          "example": 254100
        }
      },
      "SerieNotaParam": {
        "name": "serieNota",
        "in": "query",
        "description": "Série da Nota",
        "required": false,
        "schema": {
          "type": "string",
          "example": "1"
        }
      },
      "DataNegociacaoInicioParam": {
        "name": "dataNegociacaoInicio",
        "in": "query",
        "description": "Data inicial (dd/mm/aaaa)",
        "required": false,
        "schema": {
          "type": "string",
          "example": "10/02/2025"
        }
      },
      "DataNegociacaoFinalParam": {
        "name": "dataNegociacaoFinal",
        "in": "query",
        "description": "Data final (dd/mm/aaaa)",
        "required": false,
        "schema": {
          "type": "string",
          "example": "20/02/2025"
        }
      },
      "CodigoClienteParam": {
        "name": "codigoCliente",
        "in": "query",
        "description": "Código do Cliente (Parceiro)",
        "required": false,
        "schema": {
          "type": "integer"
        }
      },
      "ConfirmadaParam": {
        "name": "confirmada",
        "in": "query",
        "description": "Nota Confirmada?",
        "required": false,
        "schema": {
          "type": "boolean",
          "example": true
        }
      },
      "PendenteParam": {
        "name": "pendente",
        "in": "query",
        "description": "Nota Pendente?",
        "required": false,
        "schema": {
          "type": "boolean",
          "example": false
        }
      },
      "StatusNFeParam": {
        "name": "statusNFe",
        "in": "query",
        "description": "Status da NF-e (Enum numérico)",
        "required": false,
        "schema": {
          "type": "integer",
          "enum": [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11
          ],
          "example": 5
        }
      },
      "CodigoNaturezaParam": {
        "name": "codigoNatureza",
        "in": "query",
        "description": "Código da Natureza (CODNAT)",
        "required": false,
        "schema": {
          "type": "integer",
          "example": 30100
        }
      },
      "CodigoCentroResultadoParam": {
        "name": "codigoCentroResultado",
        "in": "query",
        "description": "Código do CR",
        "required": false,
        "schema": {
          "type": "integer",
          "example": 202
        }
      },
      "CodigoProjetoParam": {
        "name": "codigoProjeto",
        "in": "query",
        "description": "Código do Projeto",
        "required": false,
        "schema": {
          "type": "integer",
          "example": 0
        }
      },
      "CodigoContratoParam": {
        "name": "codigoContrato",
        "in": "query",
        "description": "Código do Contrato",
        "required": false,
        "schema": {
          "type": "integer",
          "example": 159
        }
      },
      "CodigoOrdemCargaParam": {
        "name": "codigoOrdemCarga",
        "in": "query",
        "description": "Código da Ordem de Carga",
        "required": false,
        "schema": {
          "type": "integer",
          "example": 55412
        }
      }
    }
  }
}
```
