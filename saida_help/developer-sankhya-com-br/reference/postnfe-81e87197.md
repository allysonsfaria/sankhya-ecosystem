---
id: "https://developer.sankhya.com.br/reference/postnfe"
titulo: "Inclusão de Nota Fiscal Completa"
url: "https://developer.sankhya.com.br/reference/postnfe"
atualizado_em: "2026-10-22T11:38:21.000Z"
---

# Inclusão de Nota Fiscal Completa

Importa uma NF-e própria (modelo 55) já autorizada externamente (ex.: Magis5, Mercado Livre Full), gravando diretamente Cabeçalho, Itens, Financeiro e, opcionalmente, o XML autorizado.

Restrições importantes desta operação:
- **Sem transmissão à SEFAZ e sem recálculo de impostos** — os valores fiscais informados no payload são gravados como enviados.
- **Sem validação de saldo de estoque** — o estoque é movimentado conforme a Tipo de Operação informada.
- **Somente NF-e aprovada** (`statusNFe = "A"`) pode ser importada.
- A `chaveNFe` não pode já existir em uma nota ativa nem em uma nota cancelada — chaves duplicadas são rejeitadas.
- O somatório de `valorParcela` em `financeiros` deve fechar com `valorNota` (tolerância de 0,01).
- Em `financeiros`, apenas os campos `tipoPagamento`, `dataVencimento`, `valorParcela` e `cartao` são processados por este endpoint; `cheque` e `idTransacao` são reservados para consulta (GET) e não são persistidos aqui.
- Os totais do objeto `reformaTributaria` (IBS/CBS/IS) são calculados automaticamente a partir dos impostos informados em `itens[].impostos[]` — não é necessário (nem persistido) enviá-los no cabeçalho.
- **Sem validação do XML enviado** — a API não valida chave de acesso, `cStat`, assinatura ou qualquer outro conteúdo do XML; apenas grava o XML recebido e, quando presente, extrai o protocolo de autorização (`protNFe`).


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
      "post": {
        "tags": [
          "Vendas NF-e"
        ],
        "summary": "Inclusão de Nota Fiscal Completa",
        "description": "Importa uma NF-e própria (modelo 55) já autorizada externamente (ex.: Magis5, Mercado Livre Full), gravando diretamente Cabeçalho, Itens, Financeiro e, opcionalmente, o XML autorizado.\n\nRestrições importantes desta operação:\n- **Sem transmissão à SEFAZ e sem recálculo de impostos** — os valores fiscais informados no payload são gravados como enviados.\n- **Sem validação de saldo de estoque** — o estoque é movimentado conforme a Tipo de Operação informada.\n- **Somente NF-e aprovada** (`statusNFe = \"A\"`) pode ser importada.\n- A `chaveNFe` não pode já existir em uma nota ativa nem em uma nota cancelada — chaves duplicadas são rejeitadas.\n- O somatório de `valorParcela` em `financeiros` deve fechar com `valorNota` (tolerância de 0,01).\n- Em `financeiros`, apenas os campos `tipoPagamento`, `dataVencimento`, `valorParcela` e `cartao` são processados por este endpoint; `cheque` e `idTransacao` são reservados para consulta (GET) e não são persistidos aqui.\n- Os totais do objeto `reformaTributaria` (IBS/CBS/IS) são calculados automaticamente a partir dos impostos informados em `itens[].impostos[]` — não é necessário (nem persistido) enviá-los no cabeçalho.\n- **Sem validação do XML enviado** — a API não valida chave de acesso, `cStat`, assinatura ou qualquer outro conteúdo do XML; apenas grava o XML recebido e, quando presente, extrai o protocolo de autorização (`protNFe`).\n",
        "operationId": "postNfe",
        "security": [
          {
            "VendasNFeBearer": []
          }
        ],
        "requestBody": {
          "description": "Objeto completo da nota fiscal para inclusão.",
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/NfeTransacaoCompleta"
              },
              "example": {
                "notaModelo": 45941,
                "dataNegociacao": "15/06/2024",
                "codigoTipoOperacao": 1200,
                "chaveNFe": "31260726314062000161550010009999991194759990",
                "statusNFe": "A",
                "valorNota": 5325,
                "baseICMS": 43.64,
                "valorICMS": 1.75,
                "valorIPI": 0,
                "valorPIS": 0.72,
                "valorCOFINS": 3.32,
                "indicadorIntermediador": 2,
                "codigoIntermediador": 19002,
                "cliente": {
                  "tipo": "PF",
                  "cnpjCpf": "12315914799",
                  "nome": "José da Silva",
                  "email": "contato@provedor.com.br"
                },
                "itens": [
                  {
                    "sequencia": 1,
                    "codigoProduto": 1050,
                    "quantidade": 2,
                    "unidade": "UN",
                    "valorUnitario": 2500,
                    "valorTotal": 5000,
                    "cfop": "5101",
                    "ncm": "84714100",
                    "cst": "000",
                    "impostos": [
                      {
                        "tipo": "icms",
                        "cst": "00",
                        "aliquota": 19.5,
                        "valorBase": 43.64,
                        "valorImposto": 1.75,
                        "valorBaseReduzida": 0,
                        "valorBaseDIFAL": 43.64,
                        "aliquotaInternaDestino": 19.5,
                        "percentualPartilhaDIFAL": 100,
                        "valorDIFALDestino": 6.76,
                        "valorDIFALRemetente": 0
                      }
                    ]
                  }
                ]
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Nota fiscal importada com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/RetornoNfe"
                }
              }
            }
          },
          "400": {
            "description": "Erro de validação: campo obrigatório ausente, status diferente de aprovada, chave de NF-e duplicada, ou somatório do financeiro divergente do valor da nota.",
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
            "description": "Produto ou local de estoque informado em um item não foi localizado.",
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
      "NfeTransacaoCompleta": {
        "type": "object",
        "description": "Schema de entrada do POST /v1/vendas/nfe (Cabeçalho + Cliente + Itens + Financeiro).\n\nAlém dos campos abaixo, aceita campos livres do dicionário de dados do SankhyaOm: qualquer nome de coluna de TGFCAB enviado em UPPERCASE (ex.: `NUMCONTRATO`) é gravado diretamente. Para maior controle, é possível enviar os blocos `camposNativos` (colunas nativas de TGFCAB, chave:valor) e `camposAdicionais` (campos customizados prefixados com `AD_`).\n\nQuando o mesmo dado é enviado tanto em um atributo oficial (ex.: `baseICMS`) quanto em `camposNativos`/`camposAdicionais` (ex.: `BASEICMS`), o valor do atributo oficial prevalece.\n\n`baseICMS`, `valorICMS`, `valorIPI`, `valorPIS` e `valorCOFINS` são obrigatórios e espelham exatamente o valor enviado: a API não recalcula esses 5 totais a partir da soma dos itens, então a nota reflete fielmente o que o integrador informou (inclusive eventuais divergências de arredondamento).",
        "required": [
          "notaModelo",
          "dataNegociacao",
          "codigoTipoOperacao",
          "chaveNFe",
          "statusNFe",
          "valorNota",
          "baseICMS",
          "valorICMS",
          "valorIPI",
          "valorPIS",
          "valorCOFINS",
          "cliente",
          "itens"
        ],
        "properties": {
          "notaModelo": {
            "type": "integer",
            "description": "Código da nota modelo (TGFCAB) usada como base para os valores padrão da negociação (empresa, natureza, etc.).",
            "example": 45941
          },
          "dataNegociacao": {
            "type": "string",
            "description": "Data da negociação, formato dd/MM/yyyy.",
            "example": "15/06/2024"
          },
          "numeroNota": {
            "type": "integer",
            "example": 254100
          },
          "serieNota": {
            "type": "string",
            "example": "1"
          },
          "codigoTipoOperacao": {
            "type": "integer",
            "description": "Código da Tipo de Operação (TGFTOP). Define TIPMOV, se movimenta estoque (ATUALEST) e se a nota fica pendente.",
            "example": 1200
          },
          "codigoTipoNegociacao": {
            "type": "integer",
            "description": "Código do Tipo de Negociação (TGFTPV). Quando ausente, usa o valor da nota modelo.",
            "example": 110
          },
          "codigoNatureza": {
            "type": "integer",
            "example": 30100
          },
          "codigoCentroResultado": {
            "type": "integer",
            "example": 10100
          },
          "codigoProjeto": {
            "type": "integer",
            "example": 202401
          },
          "codigoContrato": {
            "type": "integer",
            "example": 4502
          },
          "codigoVendedor": {
            "type": "integer",
            "example": 55
          },
          "codigoContato": {
            "description": "Código do Contato do Parceiro que contém o endereço de entrega da venda.",
            "type": "integer",
            "example": 5
          },
          "codigoMoeda": {
            "type": "integer",
            "example": 0
          },
          "valorMoeda": {
            "type": "number",
            "format": "double",
            "example": 0
          },
          "cliente": {
            "$ref": "#/components/schemas/ConsumidorCliente"
          },
          "valorNota": {
            "type": "number",
            "format": "double",
            "description": "Valor total da nota. O somatório de financeiros.valorParcela deve fechar com este valor (tolerância de 0,01).",
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
          "valorFrete": {
            "type": "number",
            "format": "double",
            "example": 180
          },
          "valorDestaque": {
            "type": "number",
            "format": "double",
            "example": 0
          },
          "codigoRemetente": {
            "type": "integer",
            "example": 1
          },
          "codigoTransportadora": {
            "type": "integer",
            "example": 800
          },
          "chaveNFe": {
            "type": "string",
            "description": "Chave de acesso da NF-e (44 dígitos). Não pode existir em outra nota ativa nem em nota cancelada.",
            "example": "35240612345678000199550010000125401002541002"
          },
          "statusNFe": {
            "type": "string",
            "description": "Status da NF-e. Somente \"A\" (Aprovada) é aceito para importação por este endpoint.",
            "enum": [
              "A"
            ],
            "example": "A"
          },
          "numeroProtocolo": {
            "type": "string",
            "description": "Número do protocolo de autorização da SEFAZ.",
            "example": "135240008899774"
          },
          "dataProtocoloNFe": {
            "type": "string",
            "description": "Data/hora do protocolo de autorização. Aceita \"dd/MM/yyyy HH:mm:ss\" ou \"dd/MM/yyyy\".",
            "example": "15/06/2024 10:30:00"
          },
          "numeroAleatorioNFe": {
            "type": "string",
            "example": "98765432"
          },
          "loteNFe": {
            "type": "string",
            "example": "20240055"
          },
          "xmlNFe": {
            "type": "string",
            "description": "XML autorizado da NF-e, em base64. É gravado exatamente como recebido (sem reformatar, reindentar ou reserializar) nos campos XML e XMLENVCLI. Quando o XML contém a tag protNFe, o trecho literal <protNFe>...</protNFe> é extraído e gravado como protocolo de autorização; quando ausente (ou não puder ser extraído), a nota é incluída normalmente e o protocolo fica vazio. A API não valida a chave de acesso, o cStat nem qualquer outro conteúdo do XML — apenas grava e extrai o protocolo.",
            "example": "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz48bmZlUHJvYyB2ZXJzaW9uPSI0LjAwIiB4bWxucz0iaHR0cDovL3d3dy5wb3J0YWxmaXNjYWwuaW5mLmJyL25mZSI+Li4uPC9uZmVQcm9jPg=="
          },
          "itens": {
            "type": "array",
            "description": "Itens da nota. Obrigatório informar ao menos um.",
            "minItems": 1,
            "items": {
              "$ref": "#/components/schemas/ItemNfe"
            }
          },
          "financeiros": {
            "type": "array",
            "description": "Parcelas financeiras da nota (títulos a vencer, sem baixa em caixa PDV).",
            "items": {
              "$ref": "#/components/schemas/FinanceiroNfe"
            }
          },
          "observacao": {
            "type": "string",
            "description": "Observação da nota (TGFCAB.OBSERVACAO).",
            "example": "Exemplo de envio"
          },
          "baseICMS": {
            "type": "number",
            "format": "double",
            "description": "Base de cálculo do ICMS do cabeçalho (TGFCAB.BASEICMS). Obrigatório: o valor enviado é gravado como recebido, sem recálculo a partir da soma dos itens.",
            "example": 43.64
          },
          "baseICMSFrete": {
            "type": "number",
            "format": "double",
            "description": "Base de cálculo do ICMS sobre o frete (TGFCAB.BASEICMSFRETE).",
            "example": 0
          },
          "valorICMS": {
            "type": "number",
            "format": "double",
            "description": "Valor do ICMS do cabeçalho (TGFCAB.VLRICMS). Obrigatório: o valor enviado é gravado como recebido, sem recálculo a partir da soma dos itens.",
            "example": 1.75
          },
          "valorICMSFCP": {
            "type": "number",
            "format": "double",
            "description": "Valor do FCP do ICMS do cabeçalho (TGFCAB.VLRICMSFCP).",
            "example": 0
          },
          "valorICMSFCPInterno": {
            "type": "number",
            "format": "double",
            "description": "Valor do FCP interno do ICMS do cabeçalho (TGFCAB.VLRICMSFCPINT).",
            "example": 0
          },
          "valorSTFCPInterno": {
            "type": "number",
            "format": "double",
            "description": "Valor do FCP interno da substituição tributária do cabeçalho (TGFCAB.VLRSTFCPINT).",
            "example": 0
          },
          "valorIPI": {
            "type": "number",
            "format": "double",
            "description": "Valor do IPI do cabeçalho (TGFCAB.VLRIPI). Obrigatório: o valor enviado é gravado como recebido, sem recálculo a partir da soma dos itens.",
            "example": 0
          },
          "valorPIS": {
            "type": "number",
            "format": "double",
            "description": "Valor do PIS do cabeçalho (TGFCAB.VLRPIS). Obrigatório: o valor enviado é gravado como recebido, sem recálculo a partir da soma dos itens.",
            "example": 0.72
          },
          "valorCOFINS": {
            "type": "number",
            "format": "double",
            "description": "Valor do COFINS do cabeçalho (TGFCAB.VLRCOFINS). Obrigatório: o valor enviado é gravado como recebido, sem recálculo a partir da soma dos itens.",
            "example": 3.32
          },
          "valorICMSDIFALDestino": {
            "type": "number",
            "format": "double",
            "description": "Valor do ICMS DIFAL devido ao estado de destino (TGFCAB.VLRICMSDIFALDEST).",
            "example": 6.76
          },
          "valorICMSDIFALRemetente": {
            "type": "number",
            "format": "double",
            "description": "Valor do ICMS DIFAL devido ao estado do remetente (TGFCAB.VLRICMSDIFALREM).",
            "example": 0
          },
          "dataEntradaSaida": {
            "type": "string",
            "description": "Data de entrada/saída da nota, formato dd/mm/aaaa (TGFCAB.DTENTSAI).",
            "example": "07/09/2026"
          },
          "pesoBruto": {
            "type": "number",
            "format": "double",
            "description": "Peso bruto da nota (TGFCAB.PESOBRUTO).",
            "example": 0.25
          },
          "quantidadeVolumes": {
            "type": "integer",
            "description": "Quantidade de volumes da nota (TGFCAB.QTDVOL).",
            "example": 1
          },
          "pesoLiquido": {
            "type": "number",
            "format": "double",
            "description": "Peso líquido da nota (TGFCAB.PESO).",
            "example": 0.25
          },
          "indicadorIntermediador": {
            "type": "integer",
            "description": "Indica se a venda ocorreu em plataforma de terceiros. Opções não iniciam em zero (convenção EasyAPI): 1 = operação sem intermediador (grava INTERMED=0); 2 = operação em site/plataforma de terceiros, marketplace (grava INTERMED=1). Qualquer valor diferente de 1 ou 2 é rejeitado com HTTP 400.",
            "enum": [
              1,
              2
            ],
            "example": 1
          },
          "codigoIntermediador": {
            "type": "integer",
            "format": "int64",
            "description": "Código do parceiro intermediador/canal de venda (TGFCAB.CODINTERM). Opcional mesmo com indicadorIntermediador=2. Deve corresponder a um parceiro existente; caso contrário, HTTP 400 com a mensagem \"O parceiro Intermediador enviado nao foi encontrado\".",
            "example": 19002
          },
          "camposNativos": {
            "type": "object",
            "description": "Colunas nativas adicionais de TGFCAB não cobertas pelos campos acima, no formato { \"NOMECOLUNA\": valor }.",
            "additionalProperties": true
          },
          "camposAdicionais": {
            "type": "object",
            "description": "Campos customizados (prefixo AD_) de TGFCAB, no formato { \"AD_CAMPO\": valor }.",
            "additionalProperties": true
          }
        }
      },
      "ConsumidorCliente": {
        "type": "object",
        "description": "Dados do cliente (parceiro) vinculado à NF-e. Campo obrigatório no cabeçalho.\n\nO parceiro é localizado por CPF/CNPJ (priorizando o ativo de menor CODPARC); se não for encontrado, é criado automaticamente com o tipo \"cliente\" habilitado. Além dos campos abaixo, é possível enviar diretamente atributos da entidade Parceiro (ex.: `CGCCPF` em vez de `cnpjCpf`).",
        "properties": {
          "atualizar": {
            "type": "boolean",
            "description": "Quando true, sobrescreve os dados cadastrais de um parceiro já existente. Quando false/ausente, os dados só são usados para localizar ou criar o parceiro.",
            "example": false
          },
          "cnpjCpf": {
            "type": "string",
            "description": "CPF (11 dígitos numéricos) ou CNPJ (14 caracteres) do parceiro.",
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
            "allOf": [
              {
                "$ref": "#/components/schemas/Endereco"
              }
            ],
            "description": "Endereço do cliente. Quando endereco.entrega = true, os dados são gravados como Contato de entrega do parceiro (nomeContato passa a ser obrigatório) em vez de alterar o endereço cadastral."
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
