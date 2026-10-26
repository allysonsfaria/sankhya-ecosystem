---
id: "https://developer.sankhya.com.br/reference/get_v1-pessoal-funcionarios-detalhados"
titulo: "Lista os funcionários com dados detalhados"
url: "https://developer.sankhya.com.br/reference/get_v1-pessoal-funcionarios-detalhados"
atualizado_em: "2026-10-22T11:38:21.000Z"
---

# Lista os funcionários com dados detalhados

Retorna uma lista paginada de funcionários com dados completos do cadastro: dados pessoais, documentos, endereço, dados contratuais (jornada, remuneração, lotação, ponto, sindicato, provisões), FGTS, afastamento, transferência, cedência, estrangeiro, eSocial, redução de jornada, vale social, médico, processo trabalhista, aprendiz, benefícios e tomador/estabelecimento.

Para utilizar o filtro `modifiedSince`, o parâmetro LOGTABOPER deve estar ativado no ambiente.

Versão mínima do módulo pessoal: **5.126.0**

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
      "name": "HCM Funcionários",
      "description": "Cadastros relacionados a Funcionários no SankhyaOm"
    }
  ],
  "paths": {
    "/v1/pessoal/funcionarios-detalhados": {
      "get": {
        "summary": "Lista os funcionários com dados detalhados",
        "tags": [
          "HCM Funcionários"
        ],
        "description": "Retorna uma lista paginada de funcionários com dados completos do cadastro: dados pessoais, documentos, endereço, dados contratuais (jornada, remuneração, lotação, ponto, sindicato, provisões), FGTS, afastamento, transferência, cedência, estrangeiro, eSocial, redução de jornada, vale social, médico, processo trabalhista, aprendiz, benefícios e tomador/estabelecimento.\n\nPara utilizar o filtro `modifiedSince`, o parâmetro LOGTABOPER deve estar ativado no ambiente.\n\nVersão mínima do módulo pessoal: **5.126.0**",
        "parameters": [
          {
            "name": "page",
            "in": "query",
            "required": false,
            "schema": {
              "type": "integer",
              "minimum": 0
            },
            "description": "Página de resultados a ser exibida (paginação)."
          },
          {
            "name": "modifiedSince",
            "in": "query",
            "required": false,
            "schema": {
              "type": "string",
              "format": "date-time",
              "example": "2024-01-01T00:00:00"
            },
            "description": "Retorna apenas funcionários modificados a partir desta data/hora. Requer o parâmetro LOGTABOPER ativado no ambiente. Formato: AAAA-MM-DDTHH:MM:SS"
          },
          {
            "name": "codigoEmpresa",
            "in": "query",
            "required": false,
            "schema": {
              "type": "integer",
              "minimum": 1,
              "example": 1
            },
            "description": "Filtra os funcionários pelo código da empresa."
          },
          {
            "name": "situacao",
            "in": "query",
            "required": false,
            "schema": {
              "type": "string",
              "enum": [
                "0",
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9"
              ],
              "example": "1"
            },
            "description": "Filtra pela situação do funcionário:\n- `0` - Demitido\n- `1` - Atividade normal\n- `2` - Afastado sem remuneração\n- `3` - Afastado por acidente de trabalho\n- `4` - Afastado para serviço militar\n- `5` - Afastado por licença maternidade\n- `6` - Afastado por doença acima de 15 dias\n- `7` - Outros\n- `8` - Transferido\n- `9` - Aposentadoria por invalidez"
          },
          {
            "name": "tipoRemuneracao",
            "in": "query",
            "required": false,
            "schema": {
              "type": "integer",
              "minimum": 1,
              "maximum": 3,
              "example": 1
            },
            "description": "Filtra pelo tipo de remuneração do funcionário:\n- `1` - Salário fixo\n- `2` - Variável\n- `3` - Salário fixo + variável"
          }
        ],
        "responses": {
          "200": {
            "description": "Lista de funcionários detalhados retornada com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ListaFuncionariosDetalhados"
                }
              }
            }
          },
          "400": {
            "description": "Requisição inválida.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Funcionariosretorno400"
                }
              }
            }
          },
          "500": {
            "description": "Erro interno no servidor."
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "Funcionariosretorno400": {
        "type": "object",
        "properties": {
          "statusCode": {
            "type": "integer",
            "format": "int32",
            "example": 400
          },
          "error": {
            "type": "object",
            "properties": {
              "code": {
                "type": "string",
                "example": "BAD_REQUEST"
              },
              "message": {
                "type": "string",
                "example": "Ocorreu algum erro inesperado!"
              },
              "details": {
                "type": "string",
                "example": "O parâmetro de paginação 'pageSize' deve ser um número inteiro positivo."
              }
            }
          }
        }
      },
      "Pagination": {
        "type": "object",
        "properties": {
          "page": {
            "type": "string",
            "description": "Número da página atual"
          },
          "offset": {
            "type": "string",
            "description": "Quantidade de registros a serem desconsiderados no início. Geralmente usado para controle de navegação."
          },
          "total": {
            "type": "string",
            "description": "Quantidade total de registros encontrados."
          },
          "hasMore": {
            "type": "string",
            "description": "Indica se há mais páginas para serem consultadas"
          }
        }
      },
      "Bairro": {
        "type": "object",
        "properties": {
          "codigo": {
            "type": "integer",
            "example": 789
          },
          "descricao": {
            "type": "string",
            "example": "Centro"
          }
        }
      },
      "Cidade": {
        "type": "object",
        "properties": {
          "codigo": {
            "type": "integer",
            "example": 1011
          },
          "descricao": {
            "type": "string",
            "example": "São Paulo"
          },
          "codigoIBGE": {
            "type": "integer",
            "example": 3550308
          }
        }
      },
      "Empresa": {
        "type": "object",
        "properties": {
          "codigo": {
            "type": "integer",
            "example": 1
          },
          "cnpj": {
            "type": "string",
            "example": "12345678000199"
          },
          "razaoSocial": {
            "type": "string",
            "example": "Empresa Exemplo S/A"
          }
        }
      },
      "FuncionariosDepartamento": {
        "type": "object",
        "properties": {
          "codigo": {
            "type": "integer",
            "example": 22
          },
          "descricao": {
            "type": "string",
            "example": "TI"
          }
        }
      },
      "FuncionariosCargo": {
        "type": "object",
        "properties": {
          "codigo": {
            "type": "integer",
            "example": 7
          },
          "descricao": {
            "type": "string",
            "example": "Desenvolvedor"
          },
          "cbo": {
            "type": "integer",
            "example": 317105
          }
        }
      },
      "FuncionariosFuncao": {
        "type": "object",
        "properties": {
          "codigo": {
            "type": "integer",
            "example": 15
          },
          "descricao": {
            "type": "string",
            "example": "Analista de Sistemas"
          },
          "cbo": {
            "type": "integer",
            "example": 212415
          }
        }
      },
      "LocalTrabalho": {
        "type": "object",
        "properties": {
          "codigo": {
            "type": "integer",
            "example": 3
          },
          "descricao": {
            "type": "string",
            "example": "Matriz"
          }
        }
      },
      "CidadeTrabalho": {
        "type": "object",
        "properties": {
          "codigo": {
            "type": "integer",
            "example": 1011
          },
          "descricao": {
            "type": "string",
            "example": "São Paulo"
          },
          "codigoIBGE": {
            "type": "integer",
            "example": 3550308
          }
        }
      },
      "Sindicato": {
        "type": "object",
        "properties": {
          "codigo": {
            "type": "integer",
            "example": 9
          },
          "nome": {
            "type": "string",
            "example": "Sindicato dos Programadores"
          },
          "cnpj": {
            "type": "string",
            "example": "11222333444455"
          }
        }
      },
      "CargaHoraria": {
        "type": "object",
        "properties": {
          "codigo": {
            "type": "integer",
            "example": 40
          },
          "descricao": {
            "type": "string",
            "example": "Carga Horária Semanal - 40h"
          }
        }
      },
      "CausaAfastamento": {
        "type": "object",
        "properties": {
          "codigo": {
            "type": "integer",
            "example": 6
          },
          "descricao": {
            "type": "string",
            "example": "Doença"
          }
        }
      },
      "TipoRescisao": {
        "type": "object",
        "properties": {
          "codigo": {
            "type": "integer",
            "example": 2
          },
          "descricao": {
            "type": "string",
            "example": "Dispensa sem Justa Causa"
          }
        }
      },
      "DadosBancarios": {
        "type": "object",
        "properties": {
          "tipoConta": {
            "type": "string",
            "example": "CC",
            "description": "Tipo da conta bancária:\n- `CC` - Conta Corrente\n- `CP` - Conta Poupança"
          },
          "tipoRecebimento": {
            "type": "string",
            "example": "B",
            "description": "Forma de recebimento do salário:\n- `B` - Banco\n- `C` - Cheque\n- `D` - Dinheiro"
          },
          "codigoBanco": {
            "type": "string",
            "example": "341"
          },
          "conta": {
            "type": "string",
            "example": "12345-6"
          }
        }
      },
      "ListaFuncionariosDetalhados": {
        "type": "object",
        "properties": {
          "funcionarios": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/FuncionarioDetalhado"
            }
          },
          "pagination": {
            "$ref": "#/components/schemas/Pagination"
          }
        }
      },
      "FuncionarioDetalhado": {
        "type": "object",
        "properties": {
          "codigoEmpresa": {
            "type": "integer",
            "example": 1,
            "description": "Código da empresa."
          },
          "codigoFuncionario": {
            "type": "integer",
            "example": 33,
            "description": "Código do funcionário."
          },
          "cpf": {
            "type": "string",
            "example": "12345678900"
          },
          "nome": {
            "type": "string",
            "example": "João da Silva"
          },
          "nomeSocial": {
            "type": "string",
            "example": "Joana Silva",
            "description": "Nome social do funcionário, quando informado."
          },
          "matricula": {
            "type": "integer",
            "example": 1234,
            "description": "Número de matrícula do funcionário na empresa."
          },
          "matriculaAnterior": {
            "type": "integer",
            "example": 567,
            "description": "Número de matrícula do funcionário no empregador anterior (aba Admissão)."
          },
          "dadosPessoais": {
            "$ref": "#/components/schemas/DadosPessoaisDetalhado"
          },
          "documentos": {
            "$ref": "#/components/schemas/DocumentosDetalhado"
          },
          "endereco": {
            "$ref": "#/components/schemas/EnderecoDetalhado"
          },
          "dadosContratuais": {
            "$ref": "#/components/schemas/DadosContratuaisDetalhado"
          },
          "fgts": {
            "$ref": "#/components/schemas/FGTS"
          },
          "afastamento": {
            "$ref": "#/components/schemas/AfastamentoDetalhado"
          },
          "transferencia": {
            "$ref": "#/components/schemas/TransferenciaDetalhada"
          },
          "cedencia": {
            "$ref": "#/components/schemas/Cedencia"
          },
          "estrangeiro": {
            "$ref": "#/components/schemas/Estrangeiro"
          },
          "esocial": {
            "$ref": "#/components/schemas/ESocial"
          },
          "reducao": {
            "$ref": "#/components/schemas/ReducaoJornada"
          },
          "valeSocial": {
            "$ref": "#/components/schemas/ValeSocial"
          },
          "medico": {
            "$ref": "#/components/schemas/Medico"
          },
          "processoTrabalhista": {
            "$ref": "#/components/schemas/ProcessoTrabalhista"
          },
          "aprendiz": {
            "$ref": "#/components/schemas/Aprendiz"
          },
          "beneficios": {
            "$ref": "#/components/schemas/BeneficiosFuncionario"
          },
          "tomadorEstabelecimento": {
            "$ref": "#/components/schemas/TomadorEstabelecimento"
          }
        }
      },
      "DadosPessoaisDetalhado": {
        "type": "object",
        "properties": {
          "nascimento": {
            "type": "string",
            "example": "01/01/1990",
            "description": "Data de nascimento do funcionário."
          },
          "sexo": {
            "type": "string",
            "example": "M",
            "description": "Sexo do funcionário:\n- `M` - Masculino\n- `F` - Feminino"
          },
          "celular": {
            "type": "string",
            "example": "11999998888"
          },
          "telefone": {
            "type": "string",
            "example": "1133334444"
          },
          "email": {
            "type": "string",
            "example": "joao@email.com"
          },
          "emailCorporativo": {
            "type": "string",
            "example": "joao@empresa.com",
            "description": "E-mail corporativo do funcionário."
          },
          "nomeMae": {
            "type": "string",
            "example": "Maria da Silva"
          },
          "nomePai": {
            "type": "string",
            "example": "José da Silva"
          },
          "estadoCivil": {
            "type": "integer",
            "example": 1,
            "description": "Código do estado civil:\n- `1` - Solteiro\n- `2` - Casado\n- `3` - Divorciado/Desquitado\n- `4` - Viúvo\n- `5` - Concubinato\n- `6` - Outros\n- `7` - União Estável\n- `9` - Separado"
          },
          "racaFuncionario": {
            "type": "integer",
            "example": 1,
            "description": "Código de raça/cor conforme tabela eSocial:\n- `1` - Branca\n- `2` - Preta\n- `3` - Parda\n- `4` - Amarela\n- `5` - Indígena\n- `6` - Não informado"
          },
          "identidadeGenero": {
            "type": "string",
            "example": "01",
            "description": "Código da identidade de gênero conforme tabela eSocial:\n- `00` - Não informado\n- `01` - Cisgênero\n- `02` - Transgênero\n- `03` - Não-binário"
          },
          "orientacaoSexual": {
            "type": "string",
            "example": "01",
            "description": "Código da orientação sexual:\n- `00` - Não informado\n- `01` - Heterossexual\n- `02` - Gay/Lésbica\n- `03` - Bissexual"
          },
          "travestiTransexual": {
            "type": "string",
            "example": "N",
            "description": "Indica se o funcionário se identifica como travesti ou transexual:\n- `S` - Sim\n- `N` - Não"
          },
          "naturalidade": {
            "type": "integer",
            "example": 3550308,
            "description": "Código do município de nascimento (IBGE)."
          },
          "nacionalidade": {
            "type": "integer",
            "example": 10,
            "description": "Código da nacionalidade conforme tabela eSocial."
          },
          "codigoPaisNacionalidade": {
            "type": "integer",
            "example": 105,
            "description": "Código do país de nascimento."
          },
          "nacionalidadePais": {
            "type": "integer",
            "example": 10,
            "description": "Código do país de nacionalidade."
          },
          "grauInstrucao": {
            "type": "integer",
            "example": 7,
            "description": "Código do nível de escolaridade conforme tabela eSocial."
          },
          "possuiFilhos": {
            "type": "string",
            "example": "S",
            "description": "Indica se o funcionário possui filhos:\n- `S` - Sim\n- `N` - Não"
          },
          "filhosBrasil": {
            "type": "string",
            "example": "S",
            "description": "Indica se o funcionário possui filhos nascidos no Brasil:\n- `S` - Sim\n- `N` - Não"
          },
          "casadoBrasil": {
            "type": "string",
            "example": "N",
            "description": "Indica se o funcionário é casado no Brasil:\n- `S` - Sim\n- `N` - Não"
          }
        }
      },
      "DocumentosDetalhado": {
        "type": "object",
        "properties": {
          "rg": {
            "$ref": "#/components/schemas/RGDetalhado"
          },
          "cpf": {
            "$ref": "#/components/schemas/CPFDocumento"
          },
          "pis": {
            "$ref": "#/components/schemas/PIS"
          },
          "ctps": {
            "$ref": "#/components/schemas/CTPSDetalhado"
          },
          "cnh": {
            "$ref": "#/components/schemas/CNHDetalhado"
          },
          "tituloEleitor": {
            "$ref": "#/components/schemas/TituloEleitorDetalhado"
          },
          "reservista": {
            "type": "string",
            "example": "123456789",
            "description": "Número do documento de reservista."
          },
          "oc": {
            "$ref": "#/components/schemas/OC"
          },
          "ric": {
            "$ref": "#/components/schemas/RIC"
          },
          "rne": {
            "$ref": "#/components/schemas/RNE"
          },
          "passaporte": {
            "$ref": "#/components/schemas/Passaporte"
          },
          "certidao": {
            "$ref": "#/components/schemas/Certidao"
          },
          "consignado": {
            "$ref": "#/components/schemas/Consignado"
          }
        }
      },
      "RGDetalhado": {
        "type": "object",
        "properties": {
          "numero": {
            "type": "string",
            "example": "1234567"
          },
          "uf": {
            "type": "integer",
            "example": 25,
            "description": "Código da UF emissora."
          },
          "orgaoEmissor": {
            "type": "string",
            "example": "SSP"
          },
          "dataEmissao": {
            "type": "string",
            "example": "01/01/2010"
          },
          "complemento": {
            "type": "string",
            "example": ""
          }
        }
      },
      "CPFDocumento": {
        "type": "object",
        "description": "Informações de alteração de CPF.",
        "properties": {
          "anterior": {
            "type": "string",
            "example": "",
            "description": "CPF anterior, quando houve alteração."
          },
          "dataAlteracao": {
            "type": "string",
            "example": null,
            "description": "Data da alteração do CPF."
          },
          "observacaoAlteracao": {
            "type": "string",
            "example": "",
            "description": "Justificativa da alteração do CPF."
          }
        }
      },
      "PIS": {
        "type": "object",
        "properties": {
          "numero": {
            "type": "string",
            "example": "12345678901"
          },
          "diaVencimento": {
            "type": "integer",
            "example": 15,
            "description": "Dia de vencimento do PIS."
          },
          "dataCadastro": {
            "type": "string",
            "example": "01/01/2010"
          }
        }
      },
      "CTPSDetalhado": {
        "type": "object",
        "properties": {
          "numero": {
            "type": "integer",
            "example": 12345
          },
          "serie": {
            "type": "string",
            "example": "001"
          },
          "uf": {
            "type": "integer",
            "example": 25,
            "description": "Código da UF da CTPS."
          },
          "dataEmissao": {
            "type": "string",
            "example": "01/06/2005"
          },
          "ctpsDigital": {
            "type": "string",
            "example": "N",
            "description": "Indica se a CTPS é digital:\n- `S` - Digital\n- `N` - Física"
          }
        }
      },
      "CNHDetalhado": {
        "type": "object",
        "properties": {
          "numero": {
            "type": "string",
            "example": "12345678900"
          },
          "categoria": {
            "type": "string",
            "example": "B"
          },
          "vencimento": {
            "type": "string",
            "example": "31/12/2027"
          },
          "orgao": {
            "type": "string",
            "example": "DETRAN"
          },
          "uf": {
            "type": "integer",
            "example": 25,
            "description": "Código da UF emissora da CNH."
          },
          "dataExpiracao": {
            "type": "string",
            "example": "31/12/2027"
          },
          "primeiraCnh": {
            "type": "string",
            "example": "N",
            "description": "Indica se é a primeira CNH:\n- `S` - Sim\n- `N` - Não"
          }
        }
      },
      "TituloEleitorDetalhado": {
        "type": "object",
        "properties": {
          "numero": {
            "type": "string",
            "example": "123456789012"
          },
          "secao": {
            "type": "integer",
            "example": 1
          },
          "zona": {
            "type": "integer",
            "example": 1
          },
          "cartorio": {
            "type": "string",
            "example": ""
          }
        }
      },
      "OC": {
        "type": "object",
        "description": "Registro em Conselho de Classe (OAB, CRM, CREA, etc.).",
        "properties": {
          "numero": {
            "type": "string",
            "example": "12345"
          },
          "orgao": {
            "type": "string",
            "example": "CRM"
          },
          "dataExpiracao": {
            "type": "string",
            "example": "31/12/2027"
          }
        }
      },
      "RIC": {
        "type": "object",
        "description": "Registro de Identidade Civil.",
        "properties": {
          "numero": {
            "type": "string",
            "example": "12345"
          },
          "orgao": {
            "type": "string",
            "example": "SSP"
          },
          "codigoCidade": {
            "type": "integer",
            "example": 3550308
          },
          "dataEmissao": {
            "type": "string",
            "example": "01/01/2010"
          }
        }
      },
      "RNE": {
        "type": "object",
        "description": "Registro Nacional de Estrangeiro.",
        "properties": {
          "numero": {
            "type": "string",
            "example": "V123456-A"
          },
          "orgao": {
            "type": "string",
            "example": "DPF"
          },
          "dataExpiracao": {
            "type": "string",
            "example": "31/12/2027"
          }
        }
      },
      "Passaporte": {
        "type": "object",
        "properties": {
          "numero": {
            "type": "string",
            "example": "AA123456"
          },
          "uf": {
            "type": "integer",
            "example": 25
          },
          "orgaoEmissor": {
            "type": "string",
            "example": "DPF"
          },
          "dataEmissao": {
            "type": "string",
            "example": "01/01/2020"
          },
          "dataValidade": {
            "type": "string",
            "example": "01/01/2030"
          }
        }
      },
      "Certidao": {
        "type": "object",
        "properties": {
          "tipo": {
            "type": "string",
            "example": "N",
            "description": "Tipo de certidão civil:\n- `N` - Nascimento\n- `C` - Casamento\n- `D` - Casamento Religioso\n- `E` - Separação\n- `O` - Óbito"
          },
          "numeroCertidaoObito": {
            "type": "string",
            "example": ""
          },
          "numeroCertidaoCivil": {
            "type": "string",
            "example": "123456"
          },
          "codigoCidade": {
            "type": "integer",
            "example": 3550308
          },
          "dataEmissao": {
            "type": "string",
            "example": "01/01/1990"
          }
        }
      },
      "Consignado": {
        "type": "object",
        "description": "Identificação do funcionário para fins de crédito consignado.",
        "properties": {
          "id": {
            "type": "string",
            "example": "12345"
          },
          "inscricao": {
            "type": "string",
            "example": "123456"
          }
        }
      },
      "EnderecoDetalhado": {
        "type": "object",
        "properties": {
          "cep": {
            "type": "string",
            "example": "01234567"
          },
          "codigo": {
            "type": "integer",
            "example": 456
          },
          "descricao": {
            "type": "string",
            "example": "Rua Exemplo"
          },
          "numero": {
            "type": "string",
            "example": "123"
          },
          "complemento": {
            "type": "string",
            "example": "Apto 45"
          },
          "caixaPostal": {
            "type": "string",
            "example": ""
          },
          "enderecoFiscalExterior": {
            "type": "string",
            "example": "N",
            "description": "Endereço fiscal no exterior (para estrangeiros): `S` - Sim, `N` - Não."
          },
          "bairro": {
            "$ref": "#/components/schemas/Bairro"
          },
          "cidade": {
            "$ref": "#/components/schemas/Cidade"
          }
        }
      },
      "DadosContratuaisDetalhado": {
        "type": "object",
        "properties": {
          "empresa": {
            "$ref": "#/components/schemas/Empresa"
          },
          "dataAdmissao": {
            "type": "string",
            "example": "15/01/2020"
          },
          "codigoCategoriaEsocial": {
            "type": "integer",
            "example": 101,
            "description": "Código da categoria do trabalhador conforme tabela eSocial:\n- `101` - Empregado - Geral (CLT)\n- `102` - Empregado - Trabalhador rural (Lei 11.718/2008)\n- `103` - Empregado - Aprendiz\n- `104` - Empregado - Doméstico\n- `105` - Empregado - Contrato a termo (Lei 9601/98)\n- `106` - Trabalhador Temporário (Lei 6019/74)\n- `107` - Empregado - Contrato Verde e Amarelo sem acordo rescisório FGTS\n- `108` - Empregado - Contrato Verde e Amarelo com acordo rescisório FGTS\n- `111` - Empregado - Contrato Intermitente\n- `201` - Trabalhador Avulso Portuário\n- `202` - Trabalhador Avulso Não Portuário\n- `301` - Servidor Público Titular de Cargo Efetivo\n- `302` - Servidor Público Cargo Exclusivo em Comissão\n- `303` - Exercente de Mandato Eletivo\n- `307` - Militar\n- `308` - Conscrito\n- `401` - Dirigente Sindical\n- `410` - Trabalhador Cedido / Exercício em Outro Órgão\n- `701` - Contribuinte Individual - Autônomo\n- `711` - Contribuinte Individual - Transportador Autônomo de Passageiros\n- `712` - Contribuinte Individual - Transportador Autônomo de Carga\n- `721` - Contribuinte Individual - Diretor Não Empregado com FGTS\n- `722` - Contribuinte Individual - Diretor Não Empregado sem FGTS\n- `723` - Contribuinte Individual - Empresários, Sócios e Membros de Conselho\n- `731` - Contribuinte Individual - Cooperado via Cooperativa de Trabalho\n- `741` - Contribuinte Individual - MEI\n- `901` - Estagiário\n- `902` - Médico Residente\n- `903` - Bolsista (Lei 8958/1994)\n- `904` - Participante de Curso de Formação em Concurso Público"
          },
          "codigoCategoriaEsocialAnterior": {
            "type": "integer",
            "example": null,
            "description": "Código da categoria anterior, em caso de alteração."
          },
          "situacao": {
            "type": "string",
            "example": "1",
            "description": "Situação do funcionário:\n- `0` - Demitido\n- `1` - Atividade normal\n- `2` - Afastado sem remuneração\n- `3` - Afastado por acidente de trabalho\n- `4` - Afastado para serviço militar\n- `5` - Afastado por licença maternidade\n- `6` - Afastado por doença acima de 15 dias\n- `7` - Outros\n- `8` - Transferido\n- `9` - Aposentadoria por invalidez"
          },
          "situacaoAnterior": {
            "type": "string",
            "example": null,
            "description": "Situação anterior em caso de alteração."
          },
          "salarioBase": {
            "type": "number",
            "example": 3500,
            "description": "Salário base do funcionário."
          },
          "bolsaEstagioOuProLabore": {
            "type": "number",
            "example": null,
            "description": "Valor da bolsa de estágio ou pró-labore."
          },
          "tipoSalario": {
            "type": "string",
            "example": "1",
            "description": "Tipo de salário:\n- `1` - Mensal\n- `2` - Quinzenal\n- `3` - Semanal\n- `4` - Diarista\n- `5` - Horista\n- `6` - Tarefa"
          },
          "horasSemana": {
            "type": "number",
            "example": 44,
            "description": "Quantidade de horas semanais contratadas."
          },
          "vinculo": {
            "type": "integer",
            "example": 1,
            "description": "Código do tipo de vínculo empregatício."
          },
          "regime": {
            "type": "integer",
            "example": 1,
            "description": "Código do regime de trabalho."
          },
          "diasFerias": {
            "type": "integer",
            "example": 30,
            "description": "Quantidade de dias de férias a que o funcionário tem direito."
          },
          "percentualAdiantamento": {
            "type": "number",
            "example": 40,
            "description": "Percentual de adiantamento salarial."
          },
          "periodoExperiencia": {
            "$ref": "#/components/schemas/PeriodoExperiencia"
          },
          "tipoContrato": {
            "$ref": "#/components/schemas/TipoContrato"
          },
          "indicadoresAdmissao": {
            "$ref": "#/components/schemas/IndicadoresAdmissao"
          },
          "codigoConvenio": {
            "type": "integer",
            "example": null,
            "description": "Código do convênio coletivo aplicado ao funcionário."
          },
          "jornada": {
            "$ref": "#/components/schemas/Jornada"
          },
          "remuneracao": {
            "$ref": "#/components/schemas/Remuneracao"
          },
          "dadosBancarios": {
            "$ref": "#/components/schemas/DadosBancarios"
          },
          "lotacao": {
            "$ref": "#/components/schemas/LotacaoDetalhada"
          },
          "ponto": {
            "$ref": "#/components/schemas/Ponto"
          },
          "grupoHorario": {
            "$ref": "#/components/schemas/GrupoHorario"
          },
          "sindicato": {
            "$ref": "#/components/schemas/SindicatoContrato"
          },
          "provisoes": {
            "$ref": "#/components/schemas/Provisoes"
          },
          "situacaoEmprego": {
            "$ref": "#/components/schemas/SituacaoEmprego"
          },
          "outros": {
            "$ref": "#/components/schemas/OutrosDadosContratuais"
          }
        }
      },
      "PeriodoExperiencia": {
        "type": "object",
        "description": "Dados do período de experiência e término do contrato.",
        "properties": {
          "dataTerminoContrato": {
            "type": "string",
            "example": null,
            "description": "Data de término do contrato (para contratos por prazo determinado)."
          },
          "dataVencimento1Periodo": {
            "type": "string",
            "example": null,
            "description": "Data de vencimento do 1° período de experiência."
          },
          "dataVencimento2Periodo": {
            "type": "string",
            "example": null,
            "description": "Data de vencimento do 2° período de experiência (prorrogação)."
          },
          "referenciaVencimento2Periodo": {
            "type": "string",
            "example": null,
            "description": "Referência utilizada para calcular o vencimento do 2° período."
          },
          "dispensadoDaExperiencia": {
            "type": "string",
            "example": "N",
            "description": "Indica se o funcionário foi dispensado do período de experiência:\n- `S` - Sim\n- `N` - Não"
          },
          "dataVencimento1PeriodoOriginal": {
            "type": "string",
            "example": null,
            "description": "Data original de vencimento do 1° período (antes de ajustes)."
          },
          "dataVencimento2PeriodoOriginal": {
            "type": "string",
            "example": null,
            "description": "Data original de vencimento do 2° período (antes de ajustes)."
          }
        }
      },
      "TipoContrato": {
        "type": "object",
        "description": "Detalhes sobre o tipo e cláusulas do contrato de trabalho.",
        "properties": {
          "contratacaoTemporaria": {
            "type": "integer",
            "example": null,
            "description": "Código do tipo de contratação temporária (Lei 6019/74)."
          },
          "numeroContrato": {
            "type": "string",
            "example": null,
            "description": "Número do contrato de trabalho."
          },
          "objetivoContratacao": {
            "type": "string",
            "example": null,
            "description": "Objetivo da contratação temporária."
          },
          "justificativaContratacao": {
            "type": "string",
            "example": null,
            "description": "Justificativa da contratação temporária."
          },
          "justificativaProrrogacao": {
            "type": "string",
            "example": null,
            "description": "Justificativa da prorrogação do contrato temporário."
          },
          "contratoSuspenso": {
            "type": "string",
            "example": "N",
            "description": "Indica se o contrato está suspenso:\n- `S` - Sim\n- `N` - Não"
          },
          "suspensaoContrato": {
            "type": "string",
            "example": null,
            "description": "Código do motivo da suspensão do contrato."
          },
          "suspensaoExpatiradoAfast": {
            "type": "string",
            "example": null,
            "description": "Suspensão de expatriado afastado."
          },
          "direitoReciproco": {
            "type": "string",
            "example": null,
            "description": "Indicador de direito recíproco no contrato."
          },
          "dataFimContratoIntermitente": {
            "type": "string",
            "example": null,
            "description": "Data de fim do contrato de trabalho intermitente."
          },
          "tipoInclusaoContrato": {
            "type": "integer",
            "example": null,
            "description": "Tipo de inclusão do contrato no eSocial:\n- `1` - Inclusão\n- `2` - Reativação"
          }
        }
      },
      "IndicadoresAdmissao": {
        "type": "object",
        "properties": {
          "indicadorAdmissao": {
            "type": "integer",
            "example": 1,
            "description": "Indicador do tipo de admissão conforme tabela eSocial:\n- `1` - Admissão\n- `3` - Transferência para mesmo grupo econômico\n- `4` - Transferência por sucessão, incorporação ou fusão\n- `5` - Transferência para empresa consorciada\n- `6` - Sem vínculo empregatício anterior\n- `7` - Reintegração\n- `8` - Readmissão"
          },
          "indicadorAdmissaoAnterior": {
            "type": "integer",
            "example": null,
            "description": "Indicador de admissão anterior (em caso de alteração)."
          }
        }
      },
      "Jornada": {
        "type": "object",
        "description": "Dados da jornada de trabalho do funcionário.",
        "properties": {
          "regimeJornada": {
            "type": "integer",
            "example": 1,
            "description": "Regime de jornada conforme tabela eSocial:\n- `1` - Submetido a horário de trabalho (Cap. II CLT)\n- `2` - Atividade externa sem horário fixo\n- `3` - Teletrabalho\n- `4` - Jornada 12x36\n- `5` - Tempo parcial (art. 58-A CLT)\n- `6` - Outros"
          },
          "regimeTrabalho": {
            "type": "integer",
            "example": 1,
            "description": "Regime de trabalho:\n- `1` - CLT (setor privado)\n- `2` - Estatutário (setor público)\n- `3` - Outros"
          },
          "semanasPorMes": {
            "type": "number",
            "example": null,
            "description": "Quantidade de semanas por mês (para jornada semanal variável)."
          },
          "diasPorSemana": {
            "type": "integer",
            "example": null,
            "description": "Quantidade de dias trabalhados por semana."
          },
          "horasSemanaCompensado": {
            "type": "number",
            "example": null,
            "description": "Horas semanais no regime compensado."
          },
          "horasSemanaReduzido": {
            "type": "number",
            "example": null,
            "description": "Horas semanais no regime reduzido."
          },
          "tempoParcial": {
            "type": "string",
            "example": null,
            "description": "Indicador de contrato em tempo parcial."
          },
          "semanalIntegral": {
            "type": "string",
            "example": null,
            "description": "Indicador de jornada semanal integral."
          },
          "jornadaProfissional": {
            "type": "integer",
            "example": null,
            "description": "Código da jornada profissional especial."
          },
          "jornadaEspecialProfissional": {
            "type": "string",
            "example": null,
            "description": "Descrição da jornada especial profissional."
          }
        }
      },
      "Remuneracao": {
        "type": "object",
        "description": "Dados de remuneração e composição salarial do funcionário.",
        "properties": {
          "tipoRemuneracao": {
            "type": "integer",
            "example": 1,
            "description": "Tipo de composição salarial:\n- `1` - Salário fixo\n- `2` - Variável\n- `3` - Salário fixo + variável"
          },
          "salarioBaseAnterior": {
            "type": "number",
            "example": null,
            "description": "Salário base anterior à última alteração."
          },
          "salarioBaseCompensado": {
            "type": "number",
            "example": null,
            "description": "Salário base no regime de horas compensadas."
          },
          "salarioBaseReduzido": {
            "type": "number",
            "example": null,
            "description": "Salário base no regime de jornada reduzida."
          },
          "salarioProfessor": {
            "type": "number",
            "example": null,
            "description": "Salário base aplicável a professores."
          },
          "salarioAjustadoSindicato": {
            "type": "number",
            "example": null,
            "description": "Salário ajustado pelo acordo sindical."
          },
          "remuneracaoMinima": {
            "type": "number",
            "example": null,
            "description": "Remuneração mínima aplicável ao funcionário."
          },
          "remuneracaoMesAnterior": {
            "type": "number",
            "example": null,
            "description": "Remuneração total do mês anterior."
          },
          "percentualConvenio": {
            "type": "number",
            "example": null,
            "description": "Percentual de reajuste salarial por convenção coletiva."
          },
          "percentualInsalubridade": {
            "type": "number",
            "example": null,
            "description": "Percentual de adicional de insalubridade."
          },
          "percentualPericulosidade": {
            "type": "number",
            "example": null,
            "description": "Percentual de adicional de periculosidade."
          },
          "step": {
            "type": "string",
            "example": null,
            "description": "Nível ou faixa na tabela de cargos e salários."
          },
          "tipoTabela": {
            "type": "string",
            "example": null,
            "description": "Código da tabela de cargos e salários."
          },
          "codigoNivel": {
            "type": "integer",
            "example": null,
            "description": "Código do nível na tabela salarial."
          },
          "codigoCarreira": {
            "type": "integer",
            "example": null,
            "description": "Código da carreira na tabela salarial."
          },
          "formaTributacao": {
            "type": "integer",
            "example": null,
            "description": "Código da forma de tributação do IRRF."
          }
        }
      },
      "LotacaoDetalhada": {
        "type": "object",
        "description": "Lotação do funcionário: departamento, cargo, função, local, cidade, sindicato e carga horária.",
        "properties": {
          "departamento": {
            "$ref": "#/components/schemas/FuncionariosDepartamento"
          },
          "cargo": {
            "$ref": "#/components/schemas/FuncionariosCargo"
          },
          "funcao": {
            "$ref": "#/components/schemas/FuncionariosFuncao"
          },
          "localTrabalho": {
            "$ref": "#/components/schemas/LocalTrabalho"
          },
          "cidadeTrabalho": {
            "$ref": "#/components/schemas/CidadeTrabalho"
          },
          "sindicato": {
            "$ref": "#/components/schemas/Sindicato"
          },
          "cargaHoraria": {
            "$ref": "#/components/schemas/CargaHoraria"
          }
        }
      },
      "Ponto": {
        "type": "object",
        "description": "Configurações de controle de ponto do funcionário.",
        "properties": {
          "diaApuracao": {
            "type": "integer",
            "example": 1,
            "description": "Dia de fechamento do ponto (apuração mensal)."
          },
          "dispensado": {
            "type": "string",
            "example": "N",
            "description": "Indica se o funcionário é dispensado do controle de ponto:\n- `S` - Sim\n- `N` - Não"
          },
          "dataDispensa": {
            "type": "string",
            "example": null,
            "description": "Data a partir da qual o funcionário foi dispensado do ponto."
          },
          "tipo": {
            "type": "string",
            "example": null,
            "description": "Tipo de ponto utilizado pelo funcionário."
          },
          "numeroCarta": {
            "type": "integer",
            "example": null,
            "description": "Número do cartão de ponto."
          },
          "bloqueiaAtoBatidaOnline": {
            "type": "string",
            "example": "N",
            "description": "Indica se bloqueia o acesso enquanto não houver batida online:\n- `S` - Sim\n- `N` - Não"
          }
        }
      },
      "GrupoHorario": {
        "type": "object",
        "description": "Grupo de horário de trabalho ao qual o funcionário pertence.",
        "properties": {
          "codigo": {
            "type": "integer",
            "example": null,
            "description": "Código do grupo de horário."
          },
          "ordem": {
            "type": "integer",
            "example": null,
            "description": "Ordem do funcionário no grupo de horário."
          },
          "dataInicio": {
            "type": "string",
            "example": null,
            "description": "Data de início no grupo de horário."
          },
          "compensaSabado": {
            "type": "string",
            "example": null,
            "description": "Indica se o grupo compensa sábado:\n- `S` - Sim\n- `N` - Não"
          }
        }
      },
      "SindicatoContrato": {
        "type": "object",
        "description": "Situação sindical do funcionário.",
        "properties": {
          "sindicalizado": {
            "type": "string",
            "example": "N",
            "description": "Indica se o funcionário é sindicalizado:\n- `S` - Sim\n- `N` - Não"
          },
          "situacaoSindical": {
            "type": "string",
            "example": null,
            "description": "Situação sindical do funcionário."
          },
          "contribuicaoSindical": {
            "type": "string",
            "example": "N",
            "description": "Indica se o funcionário possui contribuição sindical:\n- `S` - Sim\n- `N` - Não"
          }
        }
      },
      "Provisoes": {
        "type": "object",
        "description": "Indica se as provisões trabalhistas estão habilitadas para o funcionário.",
        "properties": {
          "provisao13": {
            "type": "string",
            "example": "S",
            "description": "Calcula provisão de 13° salário:\n- `S` - Sim\n- `N` - Não"
          },
          "provisaoFerias": {
            "type": "string",
            "example": "S",
            "description": "Calcula provisão de férias:\n- `S` - Sim\n- `N` - Não"
          },
          "pvd": {
            "type": "string",
            "example": "N",
            "description": "Calcula provisão de PDV (Programa de Demissão Voluntária):\n- `S` - Sim\n- `N` - Não"
          }
        }
      },
      "SituacaoEmprego": {
        "type": "object",
        "description": "Situação do funcionário em relação ao emprego.",
        "properties": {
          "primeiroEmprego": {
            "type": "string",
            "example": "N",
            "description": "Indica se é o primeiro emprego do funcionário:\n- `S` - Sim\n- `N` - Não"
          },
          "novoEmprego": {
            "type": "string",
            "example": "N",
            "description": "Indica se é um novo emprego (após período de desemprego):\n- `S` - Sim\n- `N` - Não"
          },
          "trabalhaAposAposentadoria": {
            "type": "string",
            "example": "N",
            "description": "Indica se o funcionário trabalha após aposentadoria:\n- `S` - Sim\n- `N` - Não"
          },
          "trabalhaEmOutraEmpresa": {
            "type": "string",
            "example": "N",
            "description": "Indica se o funcionário possui outro vínculo empregatício:\n- `S` - Sim\n- `N` - Não"
          }
        }
      },
      "OutrosDadosContratuais": {
        "type": "object",
        "description": "Demais atributos contratuais e administrativos do funcionário.",
        "properties": {
          "codigoCategoria": {
            "type": "integer",
            "example": null,
            "description": "Código da categoria funcional."
          },
          "codigoMotivoAdmissaoDesligamento": {
            "type": "integer",
            "example": null,
            "description": "Código do motivo de admissão ou desligamento."
          },
          "participacaoPat": {
            "type": "string",
            "example": null,
            "description": "Indicador de participação no PAT (Programa de Alimentação do Trabalhador)."
          },
          "descricaoAtividadeDesempenhada": {
            "type": "string",
            "example": null,
            "description": "Descrição da atividade desempenhada."
          },
          "cadastroInicial": {
            "type": "string",
            "example": "N",
            "description": "Indica se é o cadastro inicial do funcionário:\n- `S` - Sim\n- `N` - Não"
          },
          "cagedAdmissao": {
            "type": "string",
            "example": null,
            "description": "Indicador de informação ao CAGED na admissão."
          },
          "pertenceDepartamentoPessoal": {
            "type": "string",
            "example": "N",
            "description": "Indica se o funcionário pertence ao departamento de pessoal:\n- `S` - Sim\n- `N` - Não"
          },
          "validado": {
            "type": "string",
            "example": "N",
            "description": "Indica se o cadastro foi validado:\n- `S` - Sim\n- `N` - Não"
          },
          "ajudaCompensacao": {
            "type": "string",
            "example": null,
            "description": "Indicador de ajuda na compensação de horas."
          },
          "mei": {
            "type": "string",
            "example": "N",
            "description": "Indica se o funcionário é MEI (Microempreendedor Individual):\n- `S` - Sim\n- `N` - Não"
          },
          "mesDia": {
            "type": "integer",
            "example": null,
            "description": "Número de dias do mês para cálculo de salário."
          },
          "meterg": {
            "type": "string",
            "example": null,
            "description": "Código de controle do METERG."
          },
          "referenciaLider": {
            "type": "string",
            "example": null,
            "description": "Indicador de referência de liderança."
          },
          "adesaoImp927": {
            "type": "string",
            "example": null,
            "description": "Indicador de adesão ao acordo da MP 927/2020."
          },
          "temDescAssistencia": {
            "type": "string",
            "example": "N",
            "description": "Indica se possui desconto de assistência:\n- `S` - Sim\n- `N` - Não"
          },
          "numeroRequisicao": {
            "type": "integer",
            "example": null,
            "description": "Número da requisição de pessoal."
          },
          "codigoRequisicaoAdmissao": {
            "type": "integer",
            "example": null,
            "description": "Código da requisição de admissão."
          },
          "usuarioVpjSuperior": {
            "type": "integer",
            "example": null,
            "description": "Código do usuário VPJ superior."
          },
          "numeroParceiro": {
            "type": "integer",
            "example": null,
            "description": "Código do parceiro de negócios vinculado."
          },
          "grupoCBZ": {
            "type": "integer",
            "example": null,
            "description": "Código do grupo de contabilização."
          },
          "indicadorCumprimentoParcial": {
            "type": "integer",
            "example": null,
            "description": "Indicador de cumprimento parcial de requisitos."
          },
          "quemPagaRra": {
            "type": "integer",
            "example": null,
            "description": "Código de quem paga o RRA (Rendimento Recebido Acumuladamente)."
          },
          "lotenis": {
            "type": "object",
            "description": "Dados do lote de envio NIS.",
            "properties": {
              "data": {
                "type": "string",
                "example": null,
                "description": "Data do lote NIS."
              },
              "numero": {
                "type": "integer",
                "example": null,
                "description": "Número do lote NIS."
              }
            }
          },
          "registroFolha": {
            "type": "object",
            "description": "Informações do registro em livro/folha de empregados.",
            "properties": {
              "nroFolha": {
                "type": "string",
                "example": null,
                "description": "Número da folha no livro de registro de empregados."
              },
              "nroLivro": {
                "type": "string",
                "example": null,
                "description": "Número do livro de registro de empregados."
              },
              "nomeArquivoHomologNet": {
                "type": "string",
                "example": null,
                "description": "Nome do arquivo gerado no HomologNet."
              }
            }
          },
          "historico": {
            "type": "object",
            "description": "Datas de controle do cadastro.",
            "properties": {
              "dataUltimaAlteracao": {
                "type": "string",
                "example": "15/09/2026",
                "description": "Data da última alteração no cadastro do funcionário."
              },
              "dataQuitacao": {
                "type": "string",
                "example": null,
                "description": "Data de quitação do contrato."
              }
            }
          },
          "observacoes": {
            "type": "object",
            "description": "Campos de observação do funcionário.",
            "properties": {
              "empresaAnterior": {
                "type": "string",
                "example": null,
                "description": "Observação sobre a empresa anterior."
              },
              "geral": {
                "type": "string",
                "example": null,
                "description": "Observação geral do funcionário."
              },
              "mp": {
                "type": "string",
                "example": null,
                "description": "Observação específica para folha de pagamento."
              },
              "variavel": {
                "type": "string",
                "example": null,
                "description": "Observação variável / complementar."
              }
            }
          }
        }
      },
      "FGTS": {
        "type": "object",
        "description": "Dados do FGTS do funcionário.",
        "properties": {
          "conta": {
            "type": "string",
            "example": null,
            "description": "Número da conta vinculada do FGTS."
          },
          "opcao": {
            "type": "integer",
            "example": 1,
            "description": "Opção pelo FGTS:\n- `1` - Optante\n- `2` - Não optante\n- `3` - Não se aplica"
          },
          "dataOpcao": {
            "type": "string",
            "example": null,
            "description": "Data da opção pelo FGTS."
          },
          "afastamento": {
            "type": "string",
            "example": null,
            "description": "Código de afastamento FGTS."
          },
          "afastamentoAnterior": {
            "type": "string",
            "example": null,
            "description": "Código de afastamento FGTS anterior."
          },
          "codigoAdmissao": {
            "type": "string",
            "example": null,
            "description": "Código de admissão no FGTS (SEFIP)."
          },
          "codigoAdmissaoII": {
            "type": "string",
            "example": null,
            "description": "Código de admissão secundário no FGTS."
          },
          "codigoAgencia": {
            "type": "string",
            "example": null,
            "description": "Código da agência da conta FGTS."
          },
          "codigoSaque": {
            "type": "integer",
            "example": null,
            "description": "Código de saque do FGTS na rescisão."
          }
        }
      },
      "AfastamentoDetalhado": {
        "type": "object",
        "description": "Dados de afastamento, rescisão e aviso prévio.",
        "properties": {
          "motivoDesligamentoEsocial": {
            "type": "string",
            "example": null,
            "description": "Código do motivo de desligamento para o eSocial."
          },
          "dataAfastamento": {
            "type": "string",
            "example": null,
            "description": "Data do afastamento."
          },
          "causaAfastamento": {
            "$ref": "#/components/schemas/CausaAfastamento"
          },
          "causaAfastamentoAnterior": {
            "type": "integer",
            "example": null,
            "description": "Código da causa de afastamento anterior."
          },
          "tipoRescisao": {
            "$ref": "#/components/schemas/TipoRescisao"
          },
          "dataDesligamento": {
            "type": "string",
            "example": null,
            "description": "Data do desligamento do funcionário."
          },
          "dataAvisoPrevio": {
            "type": "string",
            "example": null,
            "description": "Data do aviso prévio."
          },
          "diasAvisoPrevio": {
            "type": "integer",
            "example": null,
            "description": "Quantidade de dias de aviso prévio."
          },
          "dataFimQuarentena": {
            "type": "string",
            "example": null,
            "description": "Data de fim da quarentena (restrição de recontratação)."
          },
          "afastamentoRais": {
            "type": "integer",
            "example": null,
            "description": "Código de afastamento para a RAIS."
          },
          "afastamentoRaisAnterior": {
            "type": "integer",
            "example": null,
            "description": "Código de afastamento RAIS anterior."
          }
        }
      },
      "TransferenciaDetalhada": {
        "type": "object",
        "description": "Dados de transferência do funcionário entre empresas.",
        "properties": {
          "dataTransferenciaDestino": {
            "type": "string",
            "example": null,
            "description": "Data de chegada na empresa de destino."
          },
          "empresaDestino": {
            "type": "integer",
            "example": null,
            "description": "Código da empresa de destino."
          },
          "cnpjEmpresaDestino": {
            "type": "string",
            "example": null,
            "description": "CNPJ da empresa de destino."
          },
          "codigoFuncionarioDestino": {
            "type": "integer",
            "example": null,
            "description": "Código do funcionário na empresa de destino."
          },
          "dataTransferencia": {
            "type": "string",
            "example": null,
            "description": "Data efetiva da transferência."
          },
          "empresaOrigem": {
            "type": "integer",
            "example": null,
            "description": "Código da empresa de origem."
          },
          "codigoFuncionarioOrigem": {
            "type": "integer",
            "example": null,
            "description": "Código do funcionário na empresa de origem."
          },
          "dataInicioVinculo": {
            "type": "string",
            "example": null,
            "description": "Data de início do vínculo na empresa anterior."
          },
          "cnpjNaEmpresaAnterior": {
            "type": "string",
            "example": null,
            "description": "CNPJ da empresa anterior."
          },
          "matriculaNaEmpresaAnterior": {
            "type": "string",
            "example": null,
            "description": "Matrícula do funcionário na empresa anterior."
          },
          "transferenciaExterna": {
            "type": "string",
            "example": null,
            "description": "Indica se a transferência é externa (entre empresas sem vínculo):\n- `S` - Sim\n- `N` - Não"
          }
        }
      },
      "Cedencia": {
        "type": "object",
        "description": "Dados de cedência do funcionário para outra entidade.",
        "properties": {
          "cnpjEmpresaCedente": {
            "type": "string",
            "example": null,
            "description": "CNPJ da empresa cedente."
          },
          "dataAdmissaoEmpresaCedente": {
            "type": "string",
            "example": null,
            "description": "Data de admissão na empresa cedente."
          },
          "matriculaEmpresaCedente": {
            "type": "string",
            "example": null,
            "description": "Matrícula do funcionário na empresa cedente."
          },
          "codigoCategoriaEstabelecimento": {
            "type": "integer",
            "example": null,
            "description": "Código da categoria do trabalhador cedido."
          },
          "informacaoOnus": {
            "type": "integer",
            "example": null,
            "description": "Indicação do ônus da remuneração:\n- `1` - Ônus para o cedente\n- `2` - Ônus para o cessionário\n- `3` - Sem ônus"
          },
          "tipoRegistroPrevidenciario": {
            "type": "integer",
            "example": null,
            "description": "Tipo de regime previdenciário:\n- `1` - RGPS (CLT)\n- `2` - RPPS (Estatutário)\n- `3` - Regime próprio no exterior"
          },
          "tipoRegimeTrabalho": {
            "type": "integer",
            "example": null,
            "description": "Regime de trabalho:\n- `1` - CLT\n- `2` - Estatutário\n- `3` - Outros"
          },
          "semOnusCedente": {
            "type": "string",
            "example": null,
            "description": "Indica se a cedência é sem ônus para o cedente:\n- `S` - Sim\n- `N` - Não"
          },
          "cnpjPratica": {
            "type": "string",
            "example": null,
            "description": "CNPJ da prática de cedência."
          },
          "cnpjEntidadeQualificadora": {
            "type": "string",
            "example": null,
            "description": "CNPJ da entidade qualificadora."
          },
          "substituto": {
            "type": "object",
            "description": "Funcionário substituto durante a cedência.",
            "properties": {
              "codigoEmpresa": {
                "type": "integer",
                "example": null
              },
              "codigoFuncionario": {
                "type": "integer",
                "example": null
              }
            }
          },
          "superior": {
            "type": "object",
            "description": "Superior hierárquico durante a cedência.",
            "properties": {
              "codigoEmpresa": {
                "type": "integer",
                "example": null
              },
              "codigoFuncionario": {
                "type": "integer",
                "example": null
              }
            }
          },
          "empresaResponsavelNIS": {
            "type": "integer",
            "example": null,
            "description": "Código da empresa responsável pelo NIS."
          }
        }
      },
      "Estrangeiro": {
        "type": "object",
        "description": "Dados específicos de funcionários estrangeiros.",
        "properties": {
          "classificacao": {
            "type": "integer",
            "example": null,
            "description": "Classificação do estrangeiro:\n- `1` - Sem visto/Indocumentado\n- `2` - Fronteiriço\n- `3` - Temporário\n- `4` - Permanente\n- `5` - Residente"
          },
          "condicaoIngresso": {
            "type": "string",
            "example": null,
            "description": "Condição de ingresso no país:\n- `1` - Refugiado\n- `2` - Solicitante de refúgio\n- `3` - Reunião familiar\n- `4` - Tratado de residência (ex: Mercosul)\n- `5` - Dependente de agente diplomático\n- `6` - Acordo Mercosul\n- `7` - Visto temporário\n- `8` - Outros"
          },
          "motivoExpatriado": {
            "type": "integer",
            "example": null,
            "description": "Código do motivo de expatriação."
          },
          "tempoResidencia": {
            "type": "string",
            "example": null,
            "description": "Tempo de residência no Brasil."
          },
          "nifBeneficiario": {
            "type": "string",
            "example": null,
            "description": "NIF (Número de Identificação Fiscal) do beneficiário no exterior."
          },
          "indicadorNIF": {
            "type": "string",
            "example": null,
            "description": "Indicador de NIF (Número de Identificação Fiscal):\n- `1` - Beneficiário com NIF\n- `2` - Beneficiário dispensado do NIF\n- `3` - País não exige NIF"
          },
          "dataValidadeVisto": {
            "type": "string",
            "example": null,
            "description": "Data de validade do visto."
          },
          "naturalizacao": {
            "type": "object",
            "description": "Dados da naturalização do estrangeiro.",
            "properties": {
              "numero": {
                "type": "string",
                "example": null,
                "description": "Número da certidão de naturalização."
              },
              "data": {
                "type": "string",
                "example": null,
                "description": "Data da naturalização."
              }
            }
          },
          "chegadaAoPais": {
            "type": "object",
            "description": "Dados da chegada ao Brasil.",
            "properties": {
              "ano": {
                "type": "integer",
                "example": null,
                "description": "Ano de chegada ao Brasil."
              },
              "data": {
                "type": "string",
                "example": null,
                "description": "Data de chegada ao Brasil."
              },
              "situacao": {
                "type": "string",
                "example": null,
                "description": "Situação migratória na chegada."
              },
              "dataValidade": {
                "type": "string",
                "example": null,
                "description": "Data de validade do documento de chegada."
              }
            }
          }
        }
      },
      "ESocial": {
        "type": "object",
        "description": "Dados de controle e informações para o eSocial.",
        "properties": {
          "matriculaAlternativa": {
            "type": "string",
            "example": null,
            "description": "Matrícula alternativa do funcionário utilizada como identificador no eSocial (campo MATRICULAOLD)."
          },
          "naturezaAtividade": {
            "type": "string",
            "example": null,
            "description": "Natureza da atividade do trabalhador:\n- `U` - Urbano\n- `P` - Rural"
          },
          "naturezaAtividadeAnterior": {
            "type": "string",
            "example": null,
            "description": "Natureza da atividade anterior (em caso de alteração)."
          },
          "indicadorMultiplosVinculos": {
            "type": "integer",
            "example": null,
            "description": "Indicativo de desconto do INSS em outra empresa:\n- `0` - Não se aplica\n- `1` - Contribuição descontada pela empresa\n- `2` - Contribuição descontada por outra empresa sobre valor menor que o teto\n- `3` - Contribuição descontada por outra empresa sobre valor do teto"
          },
          "indicadorSituacaoRemuneracaoDesligado": {
            "type": "integer",
            "example": null,
            "description": "Situação da remuneração do funcionário desligado:\n- `1` - Normal\n- `2` - Remuneração mista (fixa + variável)\n- `3` - Somente variável"
          },
          "motivoDesligamentoTSV": {
            "type": "integer",
            "example": null,
            "description": "Motivo de desligamento para trabalhador sem vínculo (TSV)."
          },
          "motivoDesligamentoAnterior": {
            "type": "string",
            "example": null,
            "description": "Código do motivo de desligamento anterior."
          },
          "motivoDesligamentoTransferencia": {
            "type": "string",
            "example": null,
            "description": "Código do motivo de desligamento por transferência."
          },
          "cpfSubstituido": {
            "type": "string",
            "example": null,
            "description": "CPF do funcionário substituído (em caso de reintegração ou readmissão)."
          }
        }
      },
      "ReducaoJornada": {
        "type": "object",
        "description": "Dados do acordo de redução de jornada e salário (MP 936/2020 e similares).",
        "properties": {
          "dataInicio": {
            "type": "string",
            "example": null,
            "description": "Data de início da redução."
          },
          "dataFim": {
            "type": "string",
            "example": null,
            "description": "Data de fim da redução."
          },
          "dataFimRemuneracao": {
            "type": "string",
            "example": null,
            "description": "Data de fim do pagamento de remuneração no período de redução."
          },
          "percentualReducao": {
            "type": "number",
            "example": null,
            "description": "Percentual de redução de jornada e salário."
          }
        }
      },
      "ValeSocial": {
        "type": "object",
        "description": "Período de vigência do vale social.",
        "properties": {
          "dataInicio": {
            "type": "string",
            "example": null,
            "description": "Data de início do vale social."
          },
          "dataFim": {
            "type": "string",
            "example": null,
            "description": "Data de fim do vale social."
          }
        }
      },
      "Medico": {
        "type": "object",
        "description": "Dados do médico responsável pelo ASO (Atestado de Saúde Ocupacional) do funcionário.",
        "properties": {
          "nome": {
            "type": "string",
            "example": null,
            "description": "Nome do médico responsável pelo ASO."
          },
          "telefone": {
            "type": "string",
            "example": null,
            "description": "Telefone do médico."
          },
          "crm": {
            "type": "string",
            "example": null,
            "description": "Número do CRM do médico."
          },
          "ufCrm": {
            "type": "string",
            "example": null,
            "description": "UF do CRM do médico."
          },
          "dataAso": {
            "type": "string",
            "example": null,
            "description": "Data do último ASO realizado."
          },
          "dataCarteiraSaude": {
            "type": "string",
            "example": null,
            "description": "Data de validade da carteira de saúde."
          },
          "possuiRra": {
            "type": "string",
            "example": null,
            "description": "Indica se o funcionário possui RRA (Rendimento Recebido Acumuladamente):\n- `S` - Sim\n- `N` - Não"
          },
          "dataLaudoRra": {
            "type": "string",
            "example": null,
            "description": "Data do laudo médico para RRA."
          },
          "numeroProcessoRra": {
            "type": "string",
            "example": null,
            "description": "Número do processo do RRA."
          }
        }
      },
      "ProcessoTrabalhista": {
        "type": "object",
        "description": "Dados de processos trabalhistas vinculados ao funcionário.",
        "properties": {
          "numero": {
            "type": "string",
            "example": null,
            "description": "Número do processo trabalhista."
          },
          "numeroAnterior": {
            "type": "string",
            "example": null,
            "description": "Número do processo trabalhista anterior."
          },
          "numeroDesligamento": {
            "type": "string",
            "example": null,
            "description": "Número do processo de desligamento judicial."
          },
          "numeroProcesso": {
            "type": "integer",
            "example": null,
            "description": "Número sequencial do processo."
          },
          "numeroProcessoJudicial": {
            "type": "integer",
            "example": null,
            "description": "Número do processo judicial (CNJ)."
          },
          "numeroProcessoTSVE": {
            "type": "string",
            "example": null,
            "description": "Número do processo TSVE."
          },
          "dataSentenca": {
            "type": "string",
            "example": null,
            "description": "Data da sentença judicial."
          },
          "dataAdmissaoJudicial": {
            "type": "string",
            "example": null,
            "description": "Data de admissão determinada judicialmente."
          },
          "dataDesligamentoJudicial": {
            "type": "string",
            "example": null,
            "description": "Data de desligamento determinada judicialmente."
          },
          "tipoRescisaoJudicial": {
            "type": "integer",
            "example": null,
            "description": "Código do tipo de rescisão determinada judicialmente."
          },
          "mataAnotacaoJudicial": {
            "type": "string",
            "example": null,
            "description": "Indica se cancela anotação anterior por determinação judicial:\n- `S` - Sim\n- `N` - Não"
          }
        }
      },
      "Aprendiz": {
        "type": "object",
        "description": "Dados do funcionário na condição de aprendiz.",
        "properties": {
          "contratoIndividual": {
            "type": "string",
            "example": null,
            "description": "Indica se o contrato de aprendizagem é individual:\n- `S` - Sim\n- `N` - Não"
          },
          "aprendizGravida": {
            "type": "string",
            "example": null,
            "description": "Indica se a aprendiz está grávida:\n- `S` - Sim\n- `N` - Não"
          },
          "numeroInscricao": {
            "type": "string",
            "example": null,
            "description": "Número de inscrição da entidade qualificante."
          },
          "tipoInscricao": {
            "type": "integer",
            "example": null,
            "description": "Tipo de inscrição da entidade qualificante:\n- `1` - CNPJ\n- `2` - CPF"
          }
        }
      },
      "BeneficiosFuncionario": {
        "type": "object",
        "description": "Flags de benefícios vinculados ao cadastro do funcionário.",
        "properties": {
          "possuiConvenioMedico": {
            "type": "string",
            "example": null,
            "description": "Indica se o funcionário possui convênio médico:\n- `S` - Sim\n- `N` - Não"
          },
          "seguroDesemprego": {
            "type": "string",
            "example": null,
            "description": "Indica se o funcionário tem direito ao seguro desemprego:\n- `S` - Sim\n- `N` - Não"
          }
        }
      },
      "TomadorEstabelecimento": {
        "type": "object",
        "description": "Dados do tomador de serviços e do estabelecimento vinculado (para trabalhadores avulsos ou cedidos).",
        "properties": {
          "tomador": {
            "type": "object",
            "description": "Tomador de serviços.",
            "properties": {
              "codigo": {
                "type": "integer",
                "example": null,
                "description": "Código interno do tomador."
              },
              "inscricao": {
                "type": "string",
                "example": null,
                "description": "Número de inscrição do tomador (CNPJ, CPF, etc.)."
              },
              "tipoInscricao": {
                "type": "integer",
                "example": null,
                "description": "Tipo de inscrição do tomador:\n- `1` - CNPJ\n- `2` - CPF\n- `3` - CAEPF\n- `4` - CNO"
              }
            }
          },
          "estabelecimento": {
            "type": "object",
            "description": "Estabelecimento vinculado.",
            "properties": {
              "inscricao": {
                "type": "string",
                "example": null,
                "description": "Número de inscrição do estabelecimento (CNPJ, CPF, etc.)."
              },
              "tipoInscricao": {
                "type": "integer",
                "example": null,
                "description": "Tipo de inscrição do estabelecimento:\n- `1` - CNPJ\n- `2` - CPF\n- `3` - CAEPF\n- `4` - CNO"
              }
            }
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
