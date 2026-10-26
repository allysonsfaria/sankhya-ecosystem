---
id: "https://developer.sankhya.com.br/reference/addcfesat"
titulo: "Incluir Cupom Fiscal eletronico"
url: "https://developer.sankhya.com.br/reference/addcfesat"
atualizado_em: "2026-05-27T21:06:58.000Z"
---

# Incluir Cupom Fiscal eletronico

Inclui um Cupom Fiscal eletronico modelo 59 emitido em um PDV externo.

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
      "name": "Vendas CF-e/SAT",
      "description": "Cupom Fiscal Eletrônico (CF-e/SAT)"
    }
  ],
  "paths": {
    "/v1/vendas/cfe-sat": {
      "post": {
        "tags": [
          "Vendas CF-e/SAT"
        ],
        "summary": "Incluir Cupom Fiscal eletronico",
        "description": "Inclui um Cupom Fiscal eletronico modelo 59 emitido em um PDV externo.",
        "operationId": "addCfeSat",
        "requestBody": {
          "description": "Inclui Cupom Fiscal eletrônico no SankhyaOm",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/movimento"
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
              "write:vendas/cfe-sat",
              "read:vendas/cfe-sat"
            ]
          }
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "movimento": {
        "description": "Os atributos apresentados aqui estão vinculados ao cabeçalho da nota, mapeados pela entidade \"CabecalhoNota\". Além disso, é possível utilizar campos que, embora não estejam detalhados nesta documentação, fazem parte do dicionário de dados, como por exemplo \"CODNAT\" que é o \"código da natureza\".",
        "required": [
          "notaModelo",
          "ambiente",
          "tipoEmissao",
          "finalidade",
          "protocolo",
          "dataProtocolo",
          "horaProtocolo",
          "numeroAleatorio",
          "numeroDocumento",
          "data",
          "hora",
          "serie",
          "chaveNfe",
          "xml",
          "valorTotal",
          "itens",
          "financeiros"
        ],
        "type": "object",
        "properties": {
          "notaModelo": {
            "type": "integer",
            "description": "Este atributo é utilizado para preparar a inclusão do movimento no SankhyaOm, permitindo que o serviço obtenha informações essenciais, como empresa, tipo de operação, natureza, entre outros. É importante destacar que é possível enviar parâmetros que sobrescrevem os valores definidos no modelo da nota, como, por exemplo, o campo CODEMP (código da empresa). Para saber mais como configurar um Modelo de Nota, [clique aqui](https://ajuda.sankhya.com.br/hc/pt-br/articles/360047012513-Config-Modelo-de-Notas)",
            "example": 45941
          },
          "ambiente": {
            "type": "integer",
            "description": "Indica o ambiente de emissão do documento fiscal. Aceitos:\n  - 1 - Produção\n  - 2 - Homologação",
            "example": 1
          },
          "tipoEmissao": {
            "type": "integer",
            "description": "Valores aceitos:\n\n  - 1 - Emissão normal (não em contingência)\n  - 2 - Contingência\n  - 3 - Contingência SCAN\n  - 4 - Contingência EPEC\n  - 5 - Contingência FS-DA\n  - 6 - Contingência SVC-AN\n  - 7 - Contingência SVC-RS\n  - 9 - Contingência off-line da NFC-e",
            "example": 1
          },
          "finalidade": {
            "type": "integer",
            "description": "Valores aceitos:\n\n  - 1 - NF-e normal; \n  - 2 - NF-e complementar; \n  - 3 - NF-e de ajuste; \n  - 4 - Devolução de mercadoria.",
            "example": 1
          },
          "protocolo": {
            "type": "string",
            "description": "Protocolodo de emissão do documento.",
            "example": "326230259108944"
          },
          "dataProtocolo": {
            "type": "string",
            "description": "Data do protocolo de emissão do documento",
            "example": "30/05/2024"
          },
          "horaProtocolo": {
            "type": "string",
            "description": "Hora do protocolo de emissão do documento",
            "example": "07:34"
          },
          "numeroAleatorio": {
            "type": "integer",
            "description": "Número aleatório gerado pelo emitente para cada NF-e para evitar acessos indevidos da NF-e.",
            "example": 15948752
          },
          "numeroDocumento": {
            "type": "string",
            "description": "Número do documento",
            "example": "0554489"
          },
          "serie": {
            "type": "string",
            "description": "Série utilizada para emissão do documento",
            "example": 3
          },
          "data": {
            "type": "string",
            "description": "Data da emissão do documento",
            "example": "30/05/2024"
          },
          "hora": {
            "type": "string",
            "description": "Data da emissão do documento",
            "example": "07:34"
          },
          "codigoPedidoOrigem": {
            "type": "integer",
            "description": "Utilizado para \"faturar\" pedidos lançados no SankhyaOm. Para registrar a origem da venda, insira o código do pedido lançado no SankhyaOm quando houver. Esse código pode ser acessado e validado através da nossa API, na entidade \"CabecalhoNota\" (NUNOTA). Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "example": 542365
          },
          "codigoVendedor": {
            "type": "integer",
            "description": "Para registrar com precisão as vendas, insira o código do vendedor responsável pela negociação. Esse código é facilmente acessível através da nossa API, na entidade \"Vendedor\" (CODVEND). Obtenha essa informação e mantenha seus registros sempre atualizados. Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "example": 11
          },
          "codigoCaixa": {
            "type": "integer",
            "description": "Identificador do Caixa/PDV que está aberto. Esta informação é retonrada ao abrir o caixa e pode ser consultada também pelo endpoint caixa/{codigoPdv}/{cpfOperador}",
            "example": 348
          },
          "consumidor": {
            "$ref": "#/components/schemas/consumidor"
          },
          "observacao": {
            "type": "string",
            "example": "Observações específicas da venda aqui"
          },
          "valorFrete": {
            "type": "number",
            "example": 0
          },
          "valorIcms": {
            "type": "number",
            "example": 0
          },
          "valorPis": {
            "type": "number",
            "example": 0
          },
          "valorCofins": {
            "type": "number",
            "example": 0
          },
          "valorFcp": {
            "description": "Valor referente a ICMS Fundo de Combate a Pobreza",
            "type": "number",
            "example": 0
          },
          "valorJuro": {
            "type": "number",
            "description": "Valor referente a juros acrescidos no documento",
            "example": 3.38
          },
          "valorTotal": {
            "type": "number",
            "description": "Valor total final do documento",
            "example": 3.38
          },
          "numeroSerieSat": {
            "type": "string",
            "description": "Enviado apenas para documentos fiscais modelo 59 (cfe-sat)",
            "example": "xxxxxxxx"
          },
          "chaveNfe": {
            "type": "string",
            "example": "26230507381608000152650030003505701343991111"
          },
          "xml": {
            "type": "string",
            "description": "XML do movimento codificado em padrão base64",
            "example": "PHhtbD54bWwgY29tcGxldG8gYXF1aTwveG1sPg=="
          },
          "itens": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/item"
            }
          },
          "financeiros": {
            "type": "array",
            "description": "Todos os dados financeiros envolvidos na transação devem ser enviados. No caso de cartão de crédito parcelado, envie as parcelas em sequência. Se houver pagamento misto, envie todas as formas de pagamento também em sequência. É importante destacar que a API está preparada para receber diferentes formas de pagamento, incluindo parcelas de cartão de crédito. Basta garantir que todos os pagamentos, inclusive as parcelas, sejam enviados sequenciadas.",
            "items": {
              "$ref": "#/components/schemas/financeiro"
            }
          }
        }
      },
      "item": {
        "type": "object",
        "description": "Os atributos apresentados aqui estão vinculados ao item da nota, mapeados pela entidade \"ItemNota\". Para personalizar a integração é possível enviar os atributos dessa entidade, como \"QTDNEG\" em vez de \"quantidade\". Além disso, é possível utilizar campos que, embora não estejam detalhados nesta documentação, fazem parte do dicionário de dados.",
        "required": [
          "sequencia",
          "codigoProduto",
          "cfop",
          "unidade",
          "quantidade",
          "valorUnitario"
        ],
        "properties": {
          "sequencia": {
            "type": "integer",
            "description": "Sequência dos itens da negociação. Deve seguir uma sequência numérica crescente, começando de 1, e prosseguir como 2, 3, e assim por diante.",
            "example": 1
          },
          "sequenciaItemOrigem": {
            "type": "integer",
            "description": "Utilizado para \"faturar\" pedidos lançados no SankhyaOm. Para registrar a origem do item na venda, insira aqui a \"sequencia\" do item no pedido lançado no SankhyaOm quando houver. Essa informação pode ser obtida e validada através da nossa API, na entidade \"ItemNota\" (SEQUENCIA da NUNOTA registrada no atributo \"codigoPedidoOrigem\"). Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "example": 2
          },
          "cancelado": {
            "$ref": "#/components/schemas/itemCancelado"
          },
          "codigoProduto": {
            "type": "integer",
            "description": "Para registrar os produtos utilizados da negociação, informe neste atributo o \"código do produto\" disponível no SankhyaOm. Esse código é facilmente acessível através da nossa API, na entidade \"Produto\" (CODPROD). Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "example": 9145
          },
          "cfop": {
            "type": "string",
            "example": 5405
          },
          "unidade": {
            "type": "string",
            "description": "Para registrar os produtos utilizados da negociação, informe neste atributo a \"unidade de medida\" disponível no SankhyaOm. Essa informação é facilmente acessível através da nossa API, na entidade \"Produto\" ou \"UnidadeAlternativa\" (CODVOL). Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "example": "UN"
          },
          "quantidade": {
            "type": "number",
            "example": 1
          },
          "controle": {
            "type": "string",
            "description": "Para registrar os produtos utilizados na negociação, insira neste campo o \"controle\" correspondente. No SankhyaOm, o controle é essencial para a gestão de estoque e pode incluir características como voltagem, sabor, tamanho, cor, entre outros. Por exemplo, para um produto controlado por cor, o valor \"verde\" seria uma informação esperada. Certifique-se de obter esses dados previamente através das entidades \"Produto\" ou \"Estoque\". Veja como funciona controle adicional de estoque em nossa ajuda [clicando aqui](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abacontroleadicional). Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "example": "Verde"
          },
          "codigoLocalEstoque": {
            "type": "integer",
            "description": "Código do Local de Estoque para o produto utilizado na negociação. Necessário quando existe controle de estoque envolvendo local. Essa informação deve ser obtida previamente pela entidade \"Estoque\" (CODLOCAL). Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "example": 0
          },
          "valorDesconto": {
            "type": "number",
            "example": 0
          },
          "valorUnitario": {
            "type": "number",
            "example": 3.38
          },
          "icms": {
            "$ref": "#/components/schemas/icms"
          },
          "pis": {
            "$ref": "#/components/schemas/pis"
          },
          "cofins": {
            "$ref": "#/components/schemas/cofins"
          }
        }
      },
      "itemCancelado": {
        "type": "object",
        "required": [
          "cpfOperador",
          "motivo"
        ],
        "description": "Propriedade opcional e utilizadas apenas em situação onde há a necessidade de registrar os itens que foram incluídos na venda, mas por alguma razão foram retirados.",
        "properties": {
          "cpfOperador": {
            "type": "string",
            "description": "Insira o CPF do operador de caixa que autorizou o cancelamento do item. Para mais detalhes sobre o cadastro de usuários, [clique aqui](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios)",
            "example": "15975325800"
          },
          "motivo": {
            "type": "string",
            "example": "Lançado errado"
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
      "financeiro": {
        "allOf": [
          {
            "$ref": "#/components/schemas/financeiroModelo"
          }
        ],
        "type": "object",
        "required": [
          "sequencia",
          "tipoPagamento",
          "dataVencimento",
          "valorParcela"
        ],
        "description": "Os atributos apresentados aqui estão vinculados ao financeiro da nota, mapeados pela entidade \"Financeiro\". Para personalizar a integração é possível enviar os atributos dessa entidade, como \"DTVENC\" em vez de \"dataVencimento\". Além disso, é possível utilizar campos que, embora não estejam detalhados nesta documentação, fazem parte do dicionário de dados.",
        "properties": {
          "sequencia": {
            "type": "integer",
            "description": "Número da parcela financeira. Deve seguir uma sequência numérica crescente, começando de 1, e prosseguir como 2, 3, e assim por diante.",
            "example": 1
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
      "icms": {
        "type": "object",
        "properties": {
          "cst": {
            "type": "string",
            "description": "Valores aceitos:\n\n  - 00 – Tributada integralmente\n  - 10 – Tributada e com cobrança do ICMS por substituição tributária\n  - 20 – Com redução de base de cálculo\n  - 30 – Isenta ou não tributada e com cobrança do ICMS por substituição tributária\n  - 40 – Isenta\n  - 41 – Não tributada\n  - 50 – Suspensão\n  - 51 – Diferimento\n  - 60 – ICMS cobrado anteriormente por substituição tributária\n  - 70 – Com redução de base de cálculo e cobrança do ICMS por substituição tributária\n  - 90 – Outras",
            "enum": [
              "00",
              "10",
              "20",
              "30",
              "40",
              "41",
              "50",
              "51",
              "60",
              "70",
              "90"
            ]
          },
          "valorBaseCalculo": {
            "type": "number",
            "example": 0
          },
          "percentual": {
            "type": "number",
            "example": 18
          },
          "valor": {
            "type": "number",
            "example": 0
          },
          "valorFcp": {
            "description": "Valor referente a ICMS Fundo de Combate a Pobreza",
            "type": "number",
            "example": 0
          },
          "percentualFcp": {
            "description": "Percentual referente a ICMS Fundo de Combate a Pobreza",
            "type": "number",
            "example": 0
          }
        }
      },
      "pis": {
        "type": "object",
        "properties": {
          "cst": {
            "type": "string",
            "description": "Conforme tabela de CST – PIS / COFINS",
            "example": 1
          },
          "valorBaseCalculo": {
            "type": "number",
            "example": 0
          },
          "percentual": {
            "type": "number",
            "example": 18
          },
          "valor": {
            "type": "number",
            "example": 0
          }
        }
      },
      "cofins": {
        "type": "object",
        "properties": {
          "cst": {
            "type": "string",
            "description": "Conforme tabela de CST – PIS / COFINS",
            "example": 1
          },
          "valorBaseCalculo": {
            "type": "number",
            "example": 0
          },
          "percentual": {
            "type": "number",
            "example": 18
          },
          "valor": {
            "type": "number",
            "example": 0
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
      "consumidor": {
        "type": "object",
        "description": "Esta tag é opcional e funciona da seguinte forma:\n\n  - Enviar sem a tag consumidor. O serviço assume o CODPARC contido na nota modelo utilizada para vincular ao documento.\n  \n  - Enviar na tag consumidor, apenas o cnpjCpf. O serviço vai tentar encontrar o cliente com base nesse número. Se o serviço não conseguir localizar o cliente, ele vai salvar o CPF ou CNPJ no cabeçalho do documento (TGFCAB) em um campo específico para essa informação.\n  \n  - Enviar tag consumidor completa. O serviço exigirá que todos os campos sejam preenchidos para poder incluir ou atualizar as informações do parceiro.\n  \nOs atributos apresentados aqui estão vinculados ao cliente, mapeados pela entidade \"Parceiro\". Para personalizar a integração, é possível enviar os atributos dessa entidade, como \"CGCCPF\" em vez de \"cnpjCpf\". Além disso, é possível utilizar campos que, embora não estejam detalhados nesta documentação, fazem parte do dicionário de dados. ",
        "properties": {
          "atualizar": {
            "type": "boolean",
            "description": "Ao configurar como \"true\", este parâmetro atualizará os dados cadastrais do parceiro, caso ele já exista no SankhyaOm. Se configurado como \"false\", a API não realizará atualizações cadastrais. Independentemente da configuração, se o parceiro não for encontrado pelo CPF ou CNPJ informado, ele será automaticamente incluído no SankhyaOm com o tipo \"cliente\" habilitado.",
            "example": false
          },
          "tipo": {
            "type": "string",
            "description": "Tipo da pessoa que pode ser Física ou Jurídica",
            "example": "PF",
            "enum": [
              "PF",
              "PJ"
            ]
          },
          "cnpjCpf": {
            "type": "string",
            "description": "Documento CNPJ ou CPF, de acordo com o tipo do consumidor",
            "example": "12315914799"
          },
          "ieRg": {
            "type": "string",
            "description": "Documento Inscrição Estadual ou RG, de acordo com o tipo do consumidor",
            "example": "12315914799"
          },
          "nome": {
            "type": "string",
            "description": "Nome da pessoa física ou nome fantasia para pessoa juridica",
            "example": "José da Silva"
          },
          "razao": {
            "type": "string",
            "description": "Nome social para pessoa jurídica"
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
            "$ref": "#/components/schemas/endereco"
          }
        }
      },
      "endereco": {
        "type": "object",
        "properties": {
          "entrega": {
            "type": "boolean",
            "description": "Para e-commerces e outros cenários onde é necessário especificar o endereço de entrega, utilize o atributo \"tipo\" para definir essa ação com precisão. Enviando este atributo com \"true\" indica que o endereço é destinado à entrega, com isso o cadastro será registrado como contato do cliente e vinculado à negociação.",
            "example": true
          },
          "logradouro": {
            "type": "string",
            "example": "Rua Maria Roberta"
          },
          "numero": {
            "type": "string",
            "format": "int64",
            "example": 10
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
            "type": "string",
            "example": 11155566
          },
          "uf": {
            "type": "string",
            "example": "MG"
          },
          "cep": {
            "type": "string",
            "example": 38400000
          }
        }
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
