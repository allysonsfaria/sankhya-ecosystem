---
id: "https://developer.sankhya.com.br/reference/getestoqueporproduto"
titulo: "Obter dados de estoque de um produto"
url: "https://developer.sankhya.com.br/reference/getestoqueporproduto"
atualizado_em: "2026-05-27T21:06:58.000Z"
---

# Obter dados de estoque de um produto


- Este serviço verifica apenas o estoque registrado no ERP Sankhya, sem considerar o estoque do WMS.
- Ele leva em conta apenas o estoque próprio da empresa, ignorando produtos armazenados por terceiros ou produtos de terceiros armazenados na empresa.
- Além disso, a API só retorna informações sobre produtos que tiveram movimentação de estoque (entrada ou saída). Caso um produto tenha sido cadastrado, mas nunca tenha tido movimentação, ele não aparecerá na resposta da API, em vez de retornar um valor "estoque = zero".
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
      "name": "Estoque",
      "description": "Retorna estoque de produto existente no SankhyaOm"
    }
  ],
  "paths": {
    "/v1/estoque/produtos/{codigoProduto}": {
      "get": {
        "tags": [
          "Estoque"
        ],
        "summary": "Obter dados de estoque de um produto",
        "description": "\n- Este serviço verifica apenas o estoque registrado no ERP Sankhya, sem considerar o estoque do WMS.\n- Ele leva em conta apenas o estoque próprio da empresa, ignorando produtos armazenados por terceiros ou produtos de terceiros armazenados na empresa.\n- Além disso, a API só retorna informações sobre produtos que tiveram movimentação de estoque (entrada ou saída). Caso um produto tenha sido cadastrado, mas nunca tenha tido movimentação, ele não aparecerá na resposta da API, em vez de retornar um valor \"estoque = zero\".\n- Versão mínima requirida do Sankhya Om para utilizar essa API: 4.34\n",
        "operationId": "getEstoquePorProduto",
        "parameters": [
          {
            "name": "codigoProduto",
            "in": "path",
            "description": "Informe neste atributo o \"código do produto\" desejado\n",
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
            "description": "Operação bem sucedida. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/estoqueResponseSingle"
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
              "write:estoque",
              "read:estoque"
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
      "estoque": {
        "type": "object",
        "required": [
          "codigoProduto",
          "codigoEmpresa",
          "codigoLocal",
          "estoque"
        ],
        "properties": {
          "codigoProduto": {
            "type": "integer",
            "description": "Este abributo indica o \"código do produto\" disponível no SankhyaOm. Esse código é facilmente acessível através da nossa API, na entidade \"Produto\" (CODPROD). Para saber mais, clique [aqui](https://developer.sankhya.com.br/reference/get_loadrecords).\n",
            "example": 99453
          },
          "codigoEmpresa": {
            "type": "integer",
            "description": "Este abributo indica o \"código da empresa\" disponível no SankhyaOm. Esse código é facilmente acessível através da nossa API, na entidade \"Empresa\" (CODEMP). Para saber mais, clique [aqui](https://developer.sankhya.com.br/reference/get_loadrecords).\n",
            "example": 1
          },
          "codigoLocal": {
            "type": "integer",
            "description": "Este atributo indica o \"código do local de estoque\" disponível no SankhyaOm. Esse código é facilmente acessível através da nossa API, na entidade \"LocalEstoque\" (CODLOCAL). Para saber mais, clique [aqui](https://developer.sankhya.com.br/reference/get_loadrecords).\n",
            "example": 100200
          },
          "controle": {
            "type": "string",
            "description": "Indica o controle utilizado no respectivo produto. No SankhyaOm, o controle é essencial para a gestão de estoque e pode incluir características como voltagem, sabor, tamanho, cor, entre outros. Por exemplo, para um produto controlado por cor, o valor \"verde\" seria uma informação esperada.\n",
            "example": "verde"
          },
          "estoque": {
            "type": "number",
            "description": "Este abributo retorna o estoque disponível para o produto (considerando os demais abributos: empresa, local e controle).\n",
            "example": 5.8
          }
        }
      },
      "estoqueResponse": {
        "type": "object",
        "properties": {
          "estoque": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/estoque"
            }
          }
        }
      },
      "estoqueResponseSingle": {
        "allOf": [
          {
            "$ref": "#/components/schemas/retorno"
          },
          {
            "$ref": "#/components/schemas/estoqueResponse"
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
