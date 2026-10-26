---
id: "https://developer.sankhya.com.br/reference/getcliente"
titulo: "Retornar lista de clientes"
url: "https://developer.sankhya.com.br/reference/getcliente"
atualizado_em: "2026-05-27T21:06:58.000Z"
---

# Retornar lista de clientes

Permite acessar a lista de clientes cadastrados no ERP. A resposta da API contém apenas os clientes ativos ou inativos que já foram cadastrados previamente no ERP.


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
      "name": "Clientes",
      "description": "Cadastrar, atualizar e retornar clientes disponíveis no SankhyaOm"
    }
  ],
  "paths": {
    "/v1/parceiros/clientes": {
      "get": {
        "tags": [
          "Clientes"
        ],
        "summary": "Retornar lista de clientes",
        "description": "Permite acessar a lista de clientes cadastrados no ERP. A resposta da API contém apenas os clientes ativos ou inativos que já foram cadastrados previamente no ERP.\n",
        "operationId": "getCliente",
        "parameters": [
          {
            "name": "page",
            "in": "query",
            "description": "Informe neste atributo a \"página\" desejada\n",
            "required": true,
            "schema": {
              "type": "integer",
              "format": "int64",
              "example": 1
            }
          },
          {
            "name": "dataHoraAlteracao",
            "in": "query",
            "description": "Informe neste atributo a data e hora da alteração do registro. Enviando este atributo, o serviço irá retornar apenas registros que tiveram alteração maior ou igual ao valor informado. O padrão de envio é \"dd/mm/aaaa hh:mm\"\n",
            "required": false,
            "schema": {
              "type": "string",
              "example": "28/01/2025 16:24"
            }
          },
          {
            "name": "sort_by",
            "in": "query",
            "description": "É recomendado enviar este atributo com o valor 'codigoCliente' conforme exemplo, para que a requisição desse endpoint garanta consistência de dados entre as paginações de registros dos clientes retornados.",
            "required": false,
            "schema": {
              "type": "string",
              "example": "codigoCliente"
            }
          },
          {
            "name": "sort_order",
            "in": "query",
            "description": "É recomendado enviar este atributo com o valor 'ASC' conforme exemplo junto com o atributo 'sort_by' mencionado acima, para que a requisição desse endpoint garanta consistência de dados entre as paginações de registros dos clientes retornados.",
            "required": false,
            "schema": {
              "type": "string",
              "example": "ASC"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Operação bem sucedida. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/clienteResponseList"
                }
              }
            }
          },
          "400": {
            "description": "Informações Inválidas. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Clientes_e_Estoqueretorno400"
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
                  "$ref": "#/components/schemas/Clientes_e_Estoqueretorno404"
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
              "write:clientes",
              "read:clientes"
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
      "paginacao": {
        "type": "object",
        "properties": {
          "page": {
            "type": "integer",
            "format": "int32",
            "example": 2
          },
          "numeroRegistros": {
            "type": "integer",
            "format": "int32",
            "example": 50
          },
          "temMaisRegistros": {
            "type": "boolean",
            "example": true
          }
        }
      },
      "retorno": {
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
      "Clientes_e_Estoquecliente": {
        "type": "object",
        "description": "Esta tag é opcional e funciona da seguinte forma:\n\n  - Enviar sem a tag consumidor. O serviço assume o CODPARC contido na nota modelo utilizada para vincular ao documento.\n  \n  - Enviar na tag consumidor, apenas o cnpjCpf. O serviço vai tentar encontrar o cliente com base nesse número. Se o serviço não conseguir localizar o cliente, ele vai salvar o CPF ou CNPJ no cabeçalho do documento (TGFCAB) em um campo específico para essa informação.\n  \n  - Enviar tag consumidor completa. O serviço exigirá que todos os campos sejam preenchidos para poder incluir ou atualizar as informações do parceiro.\n  \nOs atributos apresentados aqui estão vinculados ao cliente, mapeados pela entidade \"Parceiro\". Para personalizar a integração, é possível enviar os atributos dessa entidade, como \"CGCCPF\" em vez de \"cnpjCpf\". Além disso, é possível utilizar campos que, embora não estejam detalhados nesta documentação, fazem parte do dicionário de dados. ",
        "properties": {
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
            "description": "Nome social para pessoa jurídica",
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
          "limiteCredito": {
            "type": "number",
            "example": 10500
          },
          "grupoAutorizacao": {
            "description": "Este campo garante que um tipo de negociação só possa ser usado por Clientes que fazem parte do mesmo grupo de autorização. Para mais detalhes [clique aqui](https://ajuda.sankhya.com.br/hc/pt-br/articles/7884939083671-Grupo-de-Autoriza%C3%A7%C3%A3o-Como-vincular-Tipo-de-Negocia%C3%A7%C3%A3o-ao-Parceiro) e saiba mais.\n",
            "type": "string",
            "example": "AB"
          },
          "endereco": {
            "$ref": "#/components/schemas/enderecoCliente"
          },
          "camposAdicionais": {
            "type": "object",
            "$ref": "#/components/schemas/camposAdicionais"
          }
        }
      },
      "camposAdicionais": {
        "type": "object",
        "description": "Os campos adicionais necessários precisam estar dentro desde objeto.",
        "required": [
          "AD_TESTE_API_CAMPO_ADICIONAL_1",
          "AD_TESTE_API_CAMPO_ADICIONAL_2",
          "AD_TESTE_API_CAMPO_ADICIONAL_3",
          "AD_TESTE_API_CAMPO_ADICIONAL_4"
        ],
        "properties": {
          "AD_TESTE_API_CAMPO_ADICIONAL_1": {
            "type": "string",
            "example": "Conteudo do campo 01"
          },
          "AD_TESTE_API_CAMPO_ADICIONAL_2": {
            "type": "string",
            "example": "Conteudo do campo 02"
          },
          "AD_TESTE_API_CAMPO_ADICIONAL_3": {
            "type": "string",
            "example": "Conteudo do campo 03"
          },
          "AD_TESTE_API_CAMPO_ADICIONAL_4": {
            "type": "string",
            "example": "Conteudo do campo 04"
          }
        }
      },
      "Clientes_e_Estoqueendereco": {
        "type": "object",
        "required": [
          "bairro",
          "cep",
          "cidade",
          "codigoIbge",
          "logradouro",
          "numero",
          "uf"
        ],
        "properties": {
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
      "enderecoCliente": {
        "allOf": [
          {
            "$ref": "#/components/schemas/Clientes_e_Estoqueendereco"
          }
        ],
        "type": "object",
        "properties": {
          "latitude": {
            "type": "string",
            "example": "-18.93780355114217"
          },
          "longitude": {
            "type": "string",
            "example": "-48.31682084784485"
          }
        }
      },
      "clienteResponse": {
        "allOf": [
          {
            "$ref": "#/components/schemas/Clientes_e_Estoquecliente"
          },
          {
            "type": "object",
            "properties": {
              "codigoCliente": {
                "type": "number",
                "example": 5
              }
            }
          }
        ]
      },
      "clienteResponseList": {
        "allOf": [
          {
            "$ref": "#/components/schemas/retorno"
          },
          {
            "$ref": "#/components/schemas/paginacao"
          },
          {
            "type": "object",
            "properties": {
              "clientes": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/clienteResponse"
                }
              }
            }
          }
        ]
      },
      "Clientes_e_Estoqueretorno400": {
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
            "$ref": "#/components/schemas/Clientes_e_EstoqueretornoErro"
          }
        }
      },
      "Clientes_e_Estoqueretorno404": {
        "type": "object",
        "properties": {
          "statusCode": {
            "type": "integer",
            "format": "int32",
            "example": 404
          },
          "error": {
            "$ref": "#/components/schemas/Clientes_e_EstoqueretornoErro"
          }
        }
      },
      "Clientes_e_EstoqueretornoErro": {
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
