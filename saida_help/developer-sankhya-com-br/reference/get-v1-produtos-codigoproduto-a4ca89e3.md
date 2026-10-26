---
id: "https://developer.sankhya.com.br/reference/get_v1-produtos-codigoproduto"
titulo: "Produto específico"
url: "https://developer.sankhya.com.br/reference/get_v1-produtos-codigoproduto"
atualizado_em: "2026-05-13T12:41:23.000Z"
---

# Produto específico

Retorna um Produto específico com base no parâmetro enviado na requisição.

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
      "name": "Produtos",
      "description": "Cadastros Relacionados a Produtos"
    }
  ],
  "paths": {
    "/v1/produtos/{codigoProduto}": {
      "get": {
        "tags": [
          "Produtos"
        ],
        "summary": "Produto específico",
        "description": "Retorna um Produto específico com base no parâmetro enviado na requisição.",
        "parameters": [
          {
            "name": "codigoProduto",
            "in": "path",
            "required": true,
            "schema": {
              "type": "integer",
              "default": 0
            },
            "description": "Código do Produto para retorno"
          }
        ],
        "responses": {
          "200": {
            "description": "Dados do Produto retornados com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ProdutosProduto"
                }
              }
            }
          },
          "400": {
            "description": "Requisição inválida."
          },
          "401": {
            "description": "Não autorizado."
          },
          "403": {
            "description": "Acesso proibido."
          },
          "404": {
            "description": "Recurso não encontrado."
          },
          "500": {
            "description": "Erro interno do servidor."
          },
          "501": {
            "description": "Não implementado."
          },
          "502": {
            "description": "Erro de gateway."
          },
          "503": {
            "description": "Serviço indisponível."
          },
          "504": {
            "description": "Tempo limite excedido."
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "ProdutosProduto": {
        "type": "object",
        "properties": {
          "dataAltercao": {
            "type": "string",
            "description": "Data de alteração",
            "example": "01/09/2025 11:03:11"
          },
          "codigoProduto": {
            "type": "integer",
            "description": "Código do produto",
            "example": 123
          },
          "nome": {
            "type": "string",
            "description": "Nome do produto",
            "example": "Produto exemplo"
          },
          "complemento": {
            "type": "string",
            "description": "Complemento da descrição do produto",
            "example": "Produto modelo 2025"
          },
          "caracteristicas": {
            "type": "string",
            "description": "Informações detalhadas dobre o produto",
            "example": "Resistente à água"
          },
          "referencia": {
            "type": "string",
            "description": "Referência do produto",
            "example": "REF123456"
          },
          "codigoGrupoProduto": {
            "type": "integer",
            "description": "Código do grupo de produto",
            "example": 10
          },
          "nomeGrupoProduto": {
            "type": "string",
            "description": "Nome do grupo de produto",
            "example": "Camisa Masculina"
          },
          "volume": {
            "type": "string",
            "description": "Unidade de medida (volume) padrão do produto",
            "example": "UN"
          },
          "marca": {
            "type": "string",
            "description": "Marca do produto",
            "example": "MarcaGenérica"
          },
          "decimaisValor": {
            "type": "integer",
            "description": "Número de casas decimais para valor",
            "example": 2
          },
          "decimaisQuantidade": {
            "type": "integer",
            "description": "Número de casas decimais para quantidade",
            "example": 3
          },
          "pesoBruto": {
            "type": "number",
            "format": "float",
            "description": "Peso bruto do produto",
            "example": 1.25
          },
          "agrupamentoMinimo": {
            "type": "number",
            "format": "float",
            "description": "Agrupamento mínimo de venda ou compra",
            "example": 0.5
          },
          "quantidadeEmbalagem": {
            "type": "integer",
            "description": "Quantidade de embalagens",
            "example": 12
          },
          "tipoControleEstoque": {
            "type": "integer",
            "enum": [
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8
            ],
            "description": "Tipo de controle de estoque:\n  1 - Série\n  2 - Grade\n  3 - Livre\n  4 - Data de validade\n  5 - Sem controle adicional\n  6 - Parceiro\n  7 - Lista\n  8 - Lote",
            "example": 2
          },
          "ativo": {
            "type": "boolean",
            "description": "Indica se o produto está ativo",
            "example": true
          },
          "estoqueMaximo": {
            "type": "number",
            "format": "float",
            "description": "Estoque máximo permitido",
            "example": 500
          },
          "estoqueMinimo": {
            "type": "number",
            "format": "float",
            "description": "Estoque mínimo permitido",
            "example": 10
          },
          "homepage": {
            "type": "string",
            "description": "URL da homepage do produto",
            "example": "https://exemplo.com/produto"
          },
          "grupoDesconto": {
            "type": "string",
            "description": "Grupo de desconto do Produto",
            "example": "DESC10"
          },
          "referenciaFornecedor": {
            "type": "string",
            "description": "Referência do fornecedor",
            "example": "FORN001"
          },
          "usadoComo": {
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
              11,
              12,
              13,
              14
            ],
            "description": "Uso do produto:\n  1 - Subproduto\n  2 - Produto intermediário\n  3 - Demonstração\n  4 - Brinde\n  5 - Consumo\n  6 - Revenda (por fórmula)\n  7 - Embalagem\n  8 - Brinde (NF)\n  9 - Imobilizado\n  10 - Matéria-prima\n  11 - Outros insumos\n  12 - Em processo\n  13 - Revenda\n  14 - Terceiros\n  15 - Produdto Intermediário",
            "example": 2
          },
          "cnae": {
            "type": "integer",
            "description": "Código CNAE do produto",
            "example": 1234567
          },
          "metroCubico": {
            "type": "number",
            "format": "float",
            "description": "Metros Cúbicos do produto",
            "example": 3.45
          },
          "altura": {
            "type": "number",
            "format": "float",
            "description": "Altura do produto",
            "example": 10.5
          },
          "largura": {
            "type": "number",
            "format": "float",
            "description": "Largura do produto",
            "example": 15
          },
          "espessura": {
            "type": "number",
            "format": "float",
            "description": "Espessura ou profundidade do produto",
            "example": 2
          },
          "unidadeMedida": {
            "type": "string",
            "description": "Uso do produto:\n  CM -centímetro\n  MM - milímetro\n  M - metro",
            "enum": [
              "CM",
              "MM",
              "M"
            ],
            "example": "MM"
          },
          "utilizaBalanca": {
            "type": "boolean",
            "description": "Indica se o produto utiliza balança",
            "example": false
          },
          "codigoPais": {
            "type": "integer",
            "description": "Código do país de origem",
            "example": 55
          },
          "ncm": {
            "type": "string",
            "description": "Código NCM",
            "example": "267328"
          },
          "cest": {
            "type": "string",
            "description": "Código Especificador ST",
            "example": "0100100"
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
