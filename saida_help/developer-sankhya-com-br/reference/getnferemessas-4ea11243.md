---
id: "https://developer.sankhya.com.br/reference/getnferemessas"
titulo: "Consultar Notas de Remessa"
url: "https://developer.sankhya.com.br/reference/getnferemessas"
atualizado_em: "2026-10-22T11:38:21.000Z"
---

# Consultar Notas de Remessa

Retorna lista paginada de Notas Fiscais modelo 55 com CFOPs de remessa (CONFAZ AJ003/22).

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
    "/v1/vendas/nfe/remessas": {
      "get": {
        "tags": [
          "Vendas NF-e"
        ],
        "summary": "Consultar Notas de Remessa",
        "description": "Retorna lista paginada de Notas Fiscais modelo 55 com CFOPs de remessa (CONFAZ AJ003/22).",
        "operationId": "getNfeRemessas",
        "security": [
          {
            "VendasNFeRemessasBearer": []
          }
        ],
        "parameters": [
          {
            "$ref": "#/components/parameters/VendasNFeRemessasPageParam"
          },
          {
            "$ref": "#/components/parameters/VendasNFeRemessasModifiedSinceParam"
          },
          {
            "$ref": "#/components/parameters/VendasNFeRemessasDataNegociacaoInicioParam"
          },
          {
            "$ref": "#/components/parameters/VendasNFeRemessasDataNegociacaoFinalParam"
          },
          {
            "$ref": "#/components/parameters/VendasNFeRemessasCodigoEmpresaParam"
          },
          {
            "$ref": "#/components/parameters/NumeroNotaParam"
          },
          {
            "$ref": "#/components/parameters/VendasNFeRemessasCodigoClienteParam"
          },
          {
            "$ref": "#/components/parameters/VendasNFeRemessasStatusNFeParam"
          },
          {
            "$ref": "#/components/parameters/VendasNFeRemessasCodigoNaturezaParam"
          }
        ],
        "responses": {
          "200": {
            "description": "Sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/VendasNFeRemessasRespostaPaginadaNfeCabecalho"
                }
              }
            }
          },
          "400": {
            "description": "Erro na requisição.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/VendasNFeRemessasRetornoErro"
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
      "VendasNFeRemessasRespostaPaginadaNfeCabecalho": {
        "type": "object",
        "properties": {
          "metadados": {
            "$ref": "#/components/schemas/Metadados"
          },
          "registros": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/VendasNFeRemessasRetornoNfeCabecalho"
            }
          }
        }
      },
      "VendasNFeRemessasRetornoNfeCabecalho": {
        "allOf": [
          {
            "$ref": "#/components/schemas/VendasNFeRemessasBaseVenda"
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
                "example": "1"
              },
              "numeroProtocoloNFe": {
                "type": "string",
                "example": "135240008899774"
              },
              "dataProtocoloNFe": {
                "type": "string",
                "format": "date-time",
                "example": "2024-06-15T10:30:00Z"
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
                "example": "2024-06-15T09:00:00Z"
              },
              "xmlNFe": {
                "type": "string",
                "example": "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4..."
              },
              "reformaTributaria": {
                "$ref": "#/components/schemas/VendasNFeRemessasReformaTributaria"
              }
            }
          }
        ]
      },
      "VendasNFeRemessasBaseVenda": {
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
            "$ref": "#/components/schemas/VendasNFeRemessasCliente"
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
            "description": "Data da negociação no formato DD-MM-YYYY.",
            "example": "15-06-2024"
          },
          "dataHoraAlteracao": {
            "type": "string",
            "format": "date-time",
            "example": "2024-06-15T14:45:30Z"
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
            "example": "Remessa Estadual de Mercadoria"
          },
          "codigoNatureza": {
            "type": "integer",
            "example": 30100
          },
          "nomeNatureza": {
            "type": "string",
            "example": "Remessa de Mercadoria"
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
            "example": 15000
          },
          "descontoTotal": {
            "type": "number",
            "format": "double",
            "example": 500
          },
          "valorSeguro": {
            "type": "number",
            "format": "double",
            "example": 50
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
            "example": 0
          },
          "valorEmbalagem": {
            "type": "number",
            "format": "double",
            "example": 100
          },
          "valorFrete": {
            "type": "number",
            "format": "double",
            "example": 200
          },
          "vencimentoFrete": {
            "type": "string",
            "description": "Data de vencimento do frete no formato DD-MM-YYYY.",
            "example": "20-06-2024"
          },
          "codigoOrdemCarga": {
            "type": "integer",
            "example": 8001
          },
          "codigoVeiculo": {
            "type": "integer",
            "example": 5001
          },
          "placaVeiculo": {
            "type": "string",
            "example": "ABC-1234"
          },
          "codigoMotorista": {
            "type": "integer",
            "example": 3001
          },
          "nomeMotorista": {
            "type": "string",
            "example": "Carlos Souza"
          },
          "codigoTransportadora": {
            "type": "integer",
            "example": 4001
          },
          "nomeTransportadora": {
            "type": "string",
            "example": "Transportadora X"
          },
          "codigoRemetente": {
            "type": "integer",
            "example": 1500
          },
          "nomeRemetente": {
            "type": "string",
            "example": "Matriz Origem"
          },
          "codigoDestinatario": {
            "type": "integer",
            "example": 1600
          },
          "nomeDestinatario": {
            "type": "string",
            "example": "Filial Destino"
          },
          "quantidadeVolumes": {
            "type": "integer",
            "example": 10
          },
          "numeracaoVolumes": {
            "type": "string",
            "example": "V001 até V010"
          },
          "lacres": {
            "type": "string",
            "example": "L001, L002, L003"
          },
          "pesoBruto": {
            "type": "number",
            "format": "double",
            "example": 250.5
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
            "example": 1
          },
          "baseICMSFrete": {
            "type": "number",
            "format": "double",
            "example": 200
          },
          "icmsFrete": {
            "type": "number",
            "format": "double",
            "example": 24
          }
        }
      },
      "VendasNFeRemessasCliente": {
        "type": "object",
        "properties": {
          "tipo": {
            "type": "string",
            "example": "PJ"
          },
          "cnpjCpf": {
            "type": "string",
            "example": "12345678000195"
          },
          "ieRg": {
            "type": "string",
            "example": "123456789012"
          },
          "nome": {
            "type": "string",
            "example": "Empresa Cliente LTDA"
          },
          "razao": {
            "type": "string",
            "example": "Empresa Cliente Comércio LTDA"
          },
          "email": {
            "type": "string",
            "example": "contato@empresa.com.br"
          },
          "telefoneNumero": {
            "type": "string",
            "description": "Número de telefone completo incluindo DDD.",
            "example": "1130000000"
          },
          "endereco": {
            "$ref": "#/components/schemas/VendasNFeRemessasEndereco"
          }
        }
      },
      "VendasNFeRemessasEndereco": {
        "type": "object",
        "properties": {
          "entrega": {
            "type": "boolean",
            "example": true
          },
          "nomeContato": {
            "type": "string",
            "example": "Maria Santos"
          },
          "email": {
            "type": "string",
            "example": "maria.santos@empresa.com.br"
          },
          "logradouro": {
            "type": "string",
            "example": "Rua das Flores, 123"
          },
          "numero": {
            "type": "string",
            "example": "123"
          },
          "complemento": {
            "type": "string",
            "example": "Apto 400"
          },
          "bairro": {
            "type": "string",
            "example": "Centro"
          },
          "cidade": {
            "type": "string",
            "example": "São Paulo"
          },
          "codigoIbge": {
            "type": "integer",
            "example": 3550308
          },
          "uf": {
            "type": "string",
            "example": "SP"
          },
          "cep": {
            "type": "string",
            "example": "01234-567"
          }
        }
      },
      "VendasNFeRemessasReformaTributaria": {
        "type": "object",
        "properties": {
          "valorCreditoPresumidoIBS": {
            "type": "number",
            "format": "double",
            "example": 0
          },
          "valorCreditoPresumidoCBS": {
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
            "example": 175
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
            "example": 25
          },
          "valorIBSMunicipio": {
            "type": "number",
            "format": "double",
            "example": 10
          },
          "valorImpostoSeletivo": {
            "type": "number",
            "format": "double",
            "example": 5
          },
          "valorBaseCalculo": {
            "type": "number",
            "format": "double",
            "example": 500
          },
          "valorTotalDocumento": {
            "type": "number",
            "format": "double",
            "example": 15175
          }
        }
      },
      "VendasNFeRemessasRetornoErro": {
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
            "example": "O parâmetro dataNegociacaoInicio é obrigatório."
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
      "VendasNFeRemessasBearer": {
        "type": "apiKey",
        "name": "Authorization",
        "in": "header",
        "description": "Insira o token com o prefixo Bearer"
      }
    },
    "parameters": {
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
      "VendasNFeRemessasPageParam": {
        "name": "page",
        "in": "query",
        "description": "Número da página desejada.",
        "required": true,
        "schema": {
          "type": "integer",
          "format": "int64",
          "example": 1,
          "minimum": 1
        }
      },
      "VendasNFeRemessasModifiedSinceParam": {
        "name": "modifiedSince",
        "in": "query",
        "description": "Retorna apenas registros alterados após esta data/hora (YYYY-MM-DDTHH:MM:SS).",
        "required": false,
        "schema": {
          "type": "string",
          "format": "date-time",
          "example": "2025-01-28T16:24:00Z"
        }
      },
      "VendasNFeRemessasDataNegociacaoInicioParam": {
        "name": "dataNegociacaoInicio",
        "in": "query",
        "description": "Data inicial obrigatória no formato DD-MM-YYYY.",
        "required": true,
        "schema": {
          "type": "string",
          "example": "10-02-2025"
        }
      },
      "VendasNFeRemessasDataNegociacaoFinalParam": {
        "name": "dataNegociacaoFinal",
        "in": "query",
        "description": "Data final obrigatória no formato DD-MM-YYYY.",
        "required": true,
        "schema": {
          "type": "string",
          "example": "28-02-2025"
        }
      },
      "VendasNFeRemessasCodigoEmpresaParam": {
        "name": "codigoEmpresa",
        "in": "query",
        "description": "Código da Empresa.",
        "required": true,
        "schema": {
          "type": "integer",
          "example": 1
        }
      },
      "VendasNFeRemessasCodigoClienteParam": {
        "name": "codigoCliente",
        "in": "query",
        "description": "Código do Cliente (Parceiro).",
        "required": false,
        "schema": {
          "type": "integer"
        }
      },
      "VendasNFeRemessasStatusNFeParam": {
        "name": "statusNFe",
        "in": "query",
        "description": "Status da NF-e. Valores possíveis:\n- `1` — **Aprovada**: autorização confirmada pela SEFAZ.\n- `2` — **Denegada**: nota negada pela SEFAZ (contribuinte irregular).\n- `3` — **Aguardando Autorização**: lote enviado, aguardando resposta da SEFAZ.\n- `4` — **Enviada**: transmitida à SEFAZ, sem retorno processado ainda.\n- `5` — **Não é NF-e**: documento não eletrônico (nota em papel/manual).\n- `6` — **Pendente de Retorno**: retorno da SEFAZ ainda não consultado.\n- `7` — **Aguardando Correção**: nota com inconsistências aguardando ajuste.\n- `8` — **Enviada EPEC**: transmitida via EPEC (contingência offline).\n- `9` — **NF-e de Terceiro**: nota emitida por terceiros e recebida pelo Sankhya.\n- `10` — **Com Erro de Validação**: rejeitada por erro de schema/regra de negócio.",
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
            10
          ],
          "example": 1
        }
      },
      "VendasNFeRemessasCodigoNaturezaParam": {
        "name": "codigoNatureza",
        "in": "query",
        "description": "Código da Natureza (CODNAT).",
        "required": false,
        "schema": {
          "type": "integer",
          "example": 30100
        }
      }
    }
  }
}
```
