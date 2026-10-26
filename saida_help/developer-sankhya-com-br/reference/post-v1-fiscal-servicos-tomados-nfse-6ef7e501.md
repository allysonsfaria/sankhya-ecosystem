---
id: "https://developer.sankhya.com.br/reference/post_v1-fiscal-servicos-tomados-nfse"
titulo: "Importar Nota Fiscal de Serviço"
url: "https://developer.sankhya.com.br/reference/post_v1-fiscal-servicos-tomados-nfse"
atualizado_em: "2026-05-27T21:06:58.000Z"
---

# Importar Nota Fiscal de Serviço

Disponível a partir da versão 4.32 do SankhyaOm, a API de Importação de Notas Fiscais de Serviços Tomados foi projetada para simplificar e automatizar o processo de importação de notas fiscais emitidas por fornecedores. Essa integração permite que empresas importem de forma eficiente e segura os dados fiscais diretamente para seus sistemas de gestão, eliminando a necessidade de inserção manual e reduzindo erros humanos.
- Benefícios de utilizar a API estão na eficiência operacional, redução de erros, conformidade legal, integração flexivel e escalabilidade.
- Para evitar a duplicidade na escrituração de documentos, o serviço utiliza uma chave única composta pelos seguintes elementos: CNPJ do Prestador, Número da Nota, Número do RPS, Série da Nota e data de emissão. Essa chave única garante que cada documento fiscal seja registrado apenas uma vez, prevenindo inconsistências e duplicações.


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
      "name": "Fiscal",
      "description": "Breve descrição sobre o respectivo contexto"
    }
  ],
  "paths": {
    "/v1/fiscal/servicos-tomados/nfse": {
      "post": {
        "tags": [
          "Fiscal"
        ],
        "summary": "Importar Nota Fiscal de Serviço",
        "description": "Disponível a partir da versão 4.32 do SankhyaOm, a API de Importação de Notas Fiscais de Serviços Tomados foi projetada para simplificar e automatizar o processo de importação de notas fiscais emitidas por fornecedores. Essa integração permite que empresas importem de forma eficiente e segura os dados fiscais diretamente para seus sistemas de gestão, eliminando a necessidade de inserção manual e reduzindo erros humanos.\n- Benefícios de utilizar a API estão na eficiência operacional, redução de erros, conformidade legal, integração flexivel e escalabilidade.\n- Para evitar a duplicidade na escrituração de documentos, o serviço utiliza uma chave única composta pelos seguintes elementos: CNPJ do Prestador, Número da Nota, Número do RPS, Série da Nota e data de emissão. Essa chave única garante que cada documento fiscal seja registrado apenas uma vez, prevenindo inconsistências e duplicações.\n",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/NFSe"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Operação bem sucedida. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ImportacaoResposta"
                }
              }
            }
          },
          "400": {
            "description": "Informações Inválidas. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Requisicao_de_Servicos_Tomadosretorno400"
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
                  "$ref": "#/components/schemas/retorno404"
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
              "write:bairros",
              "read:bairros"
            ]
          }
        ]
      }
    }
  },
  "components": {
    "schemas": {
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
      "NFSe": {
        "type": "object",
        "properties": {
          "notaModelo": {
            "type": "integer",
            "description": "Este atributo é utilizado para preparar a inclusão do movimento no SankhyaOm, permitindo que o serviço obtenha informações essenciais, como empresa, tipo de operação, natureza, tipo de negociação, entre outros. Para saber mais como configurar um Modelo de Nota, Clique [aqui](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051706514-Modelo-de-Notas-e-Pedidos)\n\n Observações importantes:\n- As informações minimas no Nota Modelo é Empresa, Tipo de Operação (TOP) e Tipo de Negociação, demais informações fica a cargo de utilização do usuário como CR, Natureza, etc.\n- Para que a escrituração aconteça a TOP informada no modelo deve ter a opção de \"Cálculo de ICMS, IPI e ISS\" como não calcula e digita.\n",
            "example": 123
          },
          "prestador": {
            "type": "object",
            "properties": {
              "cnpj": {
                "type": "string",
                "description": "CNPJ do prestador - O CNPJ do prestador deve estar previamente cadastrado e com tipo \"fornecedor\" ativo.\n",
                "example": "12345678000100"
              },
              "inscricaoMunicipal": {
                "type": "string",
                "description": "Inscrição municipal do prestador",
                "example": "123456"
              }
            },
            "required": [
              "cnpj",
              "inscricaoMunicipal"
            ]
          },
          "numeroNota": {
            "type": "string",
            "description": "Número da nota",
            "example": "12345"
          },
          "numeroRPS": {
            "type": "integer",
            "description": "Número do RPS",
            "example": 1234567890
          },
          "serieRPS": {
            "type": "string",
            "description": "Série do RPS",
            "example": "NF"
          },
          "dataEmissao": {
            "type": "string",
            "format": "date",
            "description": "Data de emissão da nota",
            "example": "08/01/2025"
          },
          "horaEmissao": {
            "type": "string",
            "format": "time",
            "description": "Hora de emissão da nota",
            "example": "15:05"
          },
          "valorTotalNota": {
            "type": "number",
            "format": "double",
            "description": "Valor Total da Nota",
            "example": 1500
          },
          "valorDescontoCondicionado": {
            "type": "number",
            "format": "double",
            "description": "Valor do desconto condicionado",
            "example": 0
          },
          "valorDescontoIncondicionado": {
            "type": "number",
            "format": "double",
            "description": "Valor do desconto incondicionado",
            "example": 0
          },
          "valorDeducoes": {
            "type": "number",
            "format": "double",
            "description": "Valor das deduções",
            "example": 0
          },
          "issRetido": {
            "type": "boolean",
            "description": "Indica se o ISS foi retido",
            "example": true
          },
          "aliquotaiss": {
            "type": "number",
            "format": "double",
            "description": "Alíquota do ISS",
            "example": 15
          },
          "valorIss": {
            "type": "number",
            "format": "double",
            "description": "Valor do ISS",
            "example": 225
          },
          "ir": {
            "type": "object",
            "properties": {
              "valor": {
                "type": "number",
                "format": "double",
                "description": "Valor do IR",
                "example": 45
              },
              "retido": {
                "type": "boolean",
                "description": "Indica se o IR foi retido",
                "example": true
              },
              "tipoRetencao": {
                "type": "integer",
                "description": "Tipo de retenção do IR, as opções são:\n  - 1 - Competência\n  - 2 - Baixa\n",
                "enum": [
                  1,
                  2
                ],
                "example": 1
              }
            }
          },
          "inss": {
            "type": "object",
            "properties": {
              "valor": {
                "type": "number",
                "format": "double",
                "description": "Valor do INSS",
                "example": 75
              },
              "retido": {
                "type": "boolean",
                "description": "Indica se o INSS foi retido",
                "example": true
              },
              "tipoRetencao": {
                "type": "integer",
                "description": "Tipo de retenção do INSS, as opções são:\n  - 1 - Competência\n  - 2 - Baixa\n",
                "enum": [
                  1,
                  2
                ],
                "example": 1
              }
            }
          },
          "pis": {
            "type": "object",
            "properties": {
              "valor": {
                "type": "number",
                "format": "double",
                "description": "Valor do PIS",
                "example": 30
              },
              "retido": {
                "type": "boolean",
                "description": "Indica se o PIS foi retido",
                "example": true
              },
              "tipoRetencao": {
                "type": "integer",
                "description": "Tipo de retenção do PIS, as opções são:\n  - 1 - Competência\n  - 2 - Baixa\n",
                "enum": [
                  1,
                  2
                ],
                "example": 2
              }
            }
          },
          "cofins": {
            "type": "object",
            "properties": {
              "valor": {
                "type": "number",
                "format": "double",
                "description": "Valor do COFINS",
                "example": 69
              },
              "retido": {
                "type": "boolean",
                "description": "Indica se o COFINS foi retido",
                "example": true
              },
              "tipoRetencao": {
                "type": "integer",
                "description": "Tipo de retenção do COFINS, as opções são:\n  - 1 - Competência\n  - 2 - Baixa\n",
                "enum": [
                  1,
                  2
                ],
                "example": 2
              }
            }
          },
          "csll": {
            "type": "object",
            "properties": {
              "valor": {
                "type": "number",
                "format": "double",
                "description": "Valor do CSLL",
                "example": 30
              },
              "retido": {
                "type": "boolean",
                "description": "Indica se o CSLL foi retido",
                "example": true
              },
              "tipoRetencao": {
                "type": "integer",
                "description": "Tipo de retenção do CSLL, as opções são:\n  - 1 - Competência\n  - 2 - Baixa\n",
                "enum": [
                  1,
                  2
                ],
                "example": 2
              }
            }
          },
          "observacao": {
            "type": "string",
            "description": "Observação adicional",
            "example": "Pagamento em 30 dias."
          },
          "codigoVerificacao": {
            "type": "string",
            "description": "Código de verificação da nota",
            "example": "ABC123456"
          },
          "servico": {
            "type": "object",
            "properties": {
              "itemListaServico": {
                "type": "string",
                "description": "Item da lista de serviços:\n   Neste item deve ser informado o código do serviço conforme a aplicabilidade do município, podendo utilizar a LC 116 que é uma lista de atividades de prestação de serviço de âmbito federal ou um código específico do município. Essa informação é de suma importância para identificação do serviço a ser escriturado. \n   Para mais informações sobre essa Lista de serviços clique [aqui](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599414-Lista-de-Servi%C3%A7os)\n",
                "example": "0103"
              },
              "descricao": {
                "type": "string",
                "description": "Descrição do serviço",
                "example": "Consultoria técnica"
              },
              "quantidade": {
                "type": "integer",
                "description": "Quantidade do serviço",
                "example": 1
              },
              "valorUnitario": {
                "type": "number",
                "format": "double",
                "description": "Valor unitário do serviço",
                "example": 1500
              },
              "valorTotal": {
                "type": "number",
                "format": "double",
                "description": "Valor total do serviço",
                "example": 1500
              }
            }
          }
        },
        "required": [
          "notaModelo",
          "prestador",
          "numeroNota",
          "numeroRPS",
          "serieRPS",
          "dataEmissao",
          "horaEmissao",
          "valorTotalNota",
          "issRetido",
          "aliquota",
          "valorIss",
          "ir",
          "inss",
          "pis",
          "cofins",
          "csll",
          "servico"
        ]
      },
      "ImportacaoResposta": {
        "type": "object",
        "properties": {
          "status": {
            "type": "string",
            "description": "Status da importação",
            "example": "sucesso"
          },
          "mensagem": {
            "type": "string",
            "description": "Mensagem detalhada sobre a importação",
            "example": "Nota Fiscal de Serviço importada com sucesso."
          }
        }
      },
      "Requisicao_de_Servicos_Tomadosretorno400": {
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
            "$ref": "#/components/schemas/Requisicao_de_Servicos_TomadosretornoErro"
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
