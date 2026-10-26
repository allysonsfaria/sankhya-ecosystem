---
id: "https://developer.sankhya.com.br/reference/putpedido"
titulo: "Atualizar Pedido de Venda"
url: "https://developer.sankhya.com.br/reference/putpedido"
atualizado_em: "2026-05-27T21:06:58.000Z"
---

# Atualizar Pedido de Venda

A atualização de um Pedido de Venda já confirmado só é permitida se a TOP do pedido estiver configurada com a opção 'Permitir Alteração após Confirmar' ativada. Alem disto, na alteração de pedido, sempre enviar o itens e os financeiros.
- Versão mínima requirida do Sankhya Om para utilizar essa API: 4.34


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
      "put": {
        "tags": [
          "Vendas Pedidos"
        ],
        "summary": "Atualizar Pedido de Venda",
        "description": "A atualização de um Pedido de Venda já confirmado só é permitida se a TOP do pedido estiver configurada com a opção 'Permitir Alteração após Confirmar' ativada. Alem disto, na alteração de pedido, sempre enviar o itens e os financeiros.\n- Versão mínima requirida do Sankhya Om para utilizar essa API: 4.34\n",
        "operationId": "putPedido",
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
        "requestBody": {
          "description": "Inclui Pedido de Venda no SankhyaOm",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/atualizarPedido"
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
                  "$ref": "#/components/schemas/retornoPedido"
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
            "Bearer": [
              "write:vendas/pedidos",
              "read:vendas/pedidos"
            ]
          }
        ]
      }
    }
  },
  "components": {
    "schemas": {
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
      "atualizarPedido": {
        "required": [
          "data",
          "financeiros",
          "hora",
          "itens",
          "serie",
          "valorTotal"
        ],
        "type": "object",
        "properties": {
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
          "codigoVendedor": {
            "type": "integer",
            "description": "Para registrar com precisão as vendas, insira o código do vendedor responsável pela negociação. Esse código é facilmente acessível através da nossa API, na entidade \"Vendedor\" (CODVEND). Obtenha essa informação e mantenha seus registros sempre atualizados. Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "example": 11
          },
          "codigoCliente": {
            "type": "integer",
            "description": "Insira o código do cliente.Esse código é facilmente retornado pelo serviço: GET /v1/parceiros/clientes",
            "example": 8115
          },
          "observacao": {
            "type": "string",
            "example": "Observações específicas da venda aqui"
          },
          "valorFrete": {
            "type": "number",
            "example": 50
          },
          "valorSeguro": {
            "type": "number",
            "example": 10
          },
          "valorOutros": {
            "type": "number",
            "example": 0
          },
          "valorIcms": {
            "type": "number",
            "example": 0
          },
          "valorCofins": {
            "type": "number",
            "example": 0
          },
          "valorFcp": {
            "type": "number",
            "description": "Valor referente a ICMS Fundo de Combate a Pobreza",
            "example": 0
          },
          "valorJuro": {
            "type": "number",
            "description": "Valor referente a juros acrescidos no documento",
            "example": 0
          },
          "valorTotal": {
            "type": "number",
            "description": "Valor total final do documento",
            "example": 1060
          },
          "itens": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Pedido_de_Vendasitem"
            }
          },
          "financeiros": {
            "type": "array",
            "description": "Todos os dados financeiros envolvidos na transação devem ser enviados. No caso de cartão de crédito parcelado, envie as parcelas em sequência. Se houver pagamento misto, envie todas as formas de pagamento também em sequência. É importante destacar que a API está preparada para receber diferentes formas de pagamento, incluindo parcelas de cartão de crédito. Basta garantir que todos os pagamentos, inclusive as parcelas, sejam enviados sequenciadas.",
            "items": {
              "$ref": "#/components/schemas/Pedido_de_Vendasfinanceiro"
            }
          }
        },
        "description": "Os atributos apresentados aqui estão vinculados ao cabeçalho da nota, mapeados pela entidade \"CabecalhoNota\". Além disso, é possível utilizar campos que, embora não estejam detalhados nesta documentação, fazem parte do dicionário de dados, como por exemplo \"CODNAT\" que é o \"código da natureza\"."
      },
      "Pedido_de_Vendasitem": {
        "required": [
          "codigoLocalEstoque",
          "codigoProduto",
          "controle",
          "quantidade",
          "sequencia",
          "valorUnitario"
        ],
        "type": "object",
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
          "codigoProduto": {
            "type": "integer",
            "description": "Para registrar os produtos utilizados da negociação, informe neste atributo o \"código do produto\" disponível no SankhyaOm. Esse código é facilmente acessível através da nossa API, na entidade \"Produto\" (CODPROD). Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "example": 9145
          },
          "cfop": {
            "type": "string",
            "example": "5405"
          },
          "unidade": {
            "type": "string",
            "description": "Para registrar os produtos utilizados da negociação, informe neste atributo a \"unidade de medida\" disponível no SankhyaOm. Essa informação é facilmente acessível através da nossa API, na entidade \"Produto\" ou \"UnidadeAlternativa\" (CODVOL). Para saber mais, [clique aqui](https://developer.sankhya.com.br/reference/get_loadrecords)",
            "example": "UN"
          },
          "quantidade": {
            "type": "number",
            "example": 10
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
            "example": 100
          },
          "impostos": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Pedido_de_VendasImpostos"
            }
          }
        },
        "description": "Os atributos apresentados aqui estão vinculados ao item da nota, mapeados pela entidade \"ItemNota\". Para personalizar a integração é possível enviar os atributos dessa entidade, como \"QTDNEG\" em vez de \"quantidade\". Além disso, é possível utilizar campos que, embora não estejam detalhados nesta documentação, fazem parte do dicionário de dados."
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
      "Pedido_de_VendasfinanceiroModelo": {
        "type": "object",
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
            "example": 1060
          },
          "idTransacao": {
            "type": "string",
            "description": "ID da transação quando houver. Por exemplo o protocolo da transação PIX.",
            "example": "dadotiuiwnlkeuhcnhlahdiwlaoaokd48ge55x"
          }
        },
        "description": "Os atributos apresentados aqui estão vinculados ao financeiro da nota, mapeados pela entidade \"Financeiro\". Para personalizar a integração é possível enviar os atributos dessa entidade, como \"DTVENC\" em vez de \"dataVencimento\". Além disso, é possível utilizar campos que, embora não estejam detalhados nesta documentação, fazem parte do dicionário de dados.\n"
      },
      "Pedido_de_Vendasfinanceiro": {
        "required": [
          "dataVencimento",
          "sequencia",
          "tipoPagamento",
          "valorParcela"
        ],
        "type": "object",
        "properties": {
          "sequencia": {
            "type": "integer",
            "description": "Número da parcela financeira. Deve seguir uma sequência numérica crescente, começando de 1, e prosseguir como 2, 3, e assim por diante.",
            "example": 1
          }
        },
        "description": "Os atributos apresentados aqui estão vinculados ao financeiro da nota, mapeados pela entidade \"Financeiro\". Para personalizar a integração é possível enviar os atributos dessa entidade, como \"DTVENC\" em vez de \"dataVencimento\". Além disso, é possível utilizar campos que, embora não estejam detalhados nesta documentação, fazem parte do dicionário de dados.",
        "allOf": [
          {
            "$ref": "#/components/schemas/Pedido_de_VendasfinanceiroModelo"
          }
        ]
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
      },
      "retornoPedido": {
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
            "example": "Pedido Incluído/Atualizado/Cancelado com sucesso."
          },
          "retorno": {
            "$ref": "#/components/schemas/codigoPedido"
          }
        }
      },
      "codigoPedido": {
        "type": "object",
        "properties": {
          "codigoPedido": {
            "type": "integer",
            "description": "Identificador único pedido.",
            "example": 98115
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
