---
id: "https://developer.sankhya.com.br/reference/post_v2-funcionarios-admissao"
titulo: "Criar uma nova requisição de admissão"
url: "https://developer.sankhya.com.br/reference/post_v2-funcionarios-admissao"
atualizado_em: "2026-05-27T21:06:58.000Z"
---

# Criar uma nova requisição de admissão

Este endpoint permite o registro de uma nova requisição de admissão, incluindo informações detalhadas sobre o trabalhador, seu cargo, categoria, dados contratuais e cadastrais. 

 Versão mínima do módulo pessoal: **5.125.0**

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
      "name": "HCM Cadastros",
      "description": "Cadastros Básicos relacionados a Pessoal no SankhyaOm"
    }
  ],
  "paths": {
    "/v2/funcionarios/admissao": {
      "post": {
        "summary": "Criar uma nova requisição de admissão",
        "tags": [
          "HCM Cadastros"
        ],
        "description": "Este endpoint permite o registro de uma nova requisição de admissão, incluindo informações detalhadas sobre o trabalhador, seu cargo, categoria, dados contratuais e cadastrais. \n\n Versão mínima do módulo pessoal: **5.125.0**",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/RequisicaoAdmissaoV2"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Requisição de Admissão criada com sucesso.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/RequisicaoAdmissaoResponse"
                }
              }
            }
          },
          "400": {
            "description": "Informações Inválidas. Clique [aqui](https://developer.sankhya.com.br/reference/c%C3%B3digos-de-retorno-da-api) para mais detalhes.\n",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Requisicao_de_Admissaoretorno400"
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
                  "$ref": "#/components/schemas/Requisicao_de_Admissaoretorno404"
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
        }
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
      "RequisicaoAdmissaoV2": {
        "type": "object",
        "description": "Schema v2. Suporta apenas arrays de anexos, removendo os campos de anexo individuais presentes na versão v1. Por padrão, os anexos de documentos (CPF, admissão, etc.) são processados de forma assíncrona: a URL informada é enfileirada e o download do arquivo, bem como sua disponibilização no cadastro do funcionário, ocorrem em um processo em segundo plano (execução periódica, a cada poucos minutos), não durante a chamada síncrona desta API. A foto de perfil (`urlFotoPerfil`) é a única exceção e é processada de forma síncrona, dentro da própria chamada.",
        "required": [
          "contrato",
          "nome",
          "cpf",
          "estadoCivil",
          "identidadeGenero",
          "nivelEscolaridade",
          "orientacaoSexual",
          "sexo",
          "racaEtnia",
          "nascimento",
          "contato",
          "endereco"
        ],
        "properties": {
          "nome": {
            "type": "string",
            "description": "Nome do Funcionário",
            "example": "João Silva"
          },
          "cpf": {
            "type": "string",
            "description": "CPF do Funcionário",
            "example": "12345678900"
          },
          "estadoCivil": {
            "type": "integer",
            "description": "Estado Civil. Os Valores aceitos são:\n  - 1 - Solteiro(a)\n  - 2 - Casado(a)\n  - 3 - Viúvo(a)\n  - 4 - Separado(a) Judicialmente\n  - 5 - Desquitado(a)\n  - 6 - Divorciado(a)\n  - 7 - União Estável\n",
            "enum": [
              1,
              2,
              3,
              4,
              5,
              6,
              7
            ],
            "example": 1
          },
          "possuiFilhos": {
            "type": "boolean",
            "description": "Para indicar se possui filhos",
            "example": true
          },
          "identidadeGenero": {
            "type": "string",
            "description": "Identidade de Gênero. Seguem os valores aceitos:\n  - C - Cisgênero\n  - N - Não-binário\n  - T - Transgênero\n  - U - Não informado\n",
            "enum": [
              "C",
              "N",
              "T",
              "U"
            ],
            "example": "C"
          },
          "nivelEscolaridade": {
            "type": "integer",
            "description": "Escolaridade. Seguem os valores aceitos:\n  - 1 - Analfabeto\n  - 2 - Até 5º Ano Incompleto\n  - 3 - 5º Ano Completo\n  - 4 - 6º Ao 9º Ano Incompleto\n  - 5 - Fundamental Completo\n  - 6 - Ensino Médio Incompleto\n  - 7 - Ensino Médio Completo\n  - 8 - Superior Incompleto\n  - 9 - Superior Completo\n  - 10 - Mestrado Completo\n  - 11 - Doutorado Completo\n  - 12 - Pós-Graduação Completa\n",
            "enum": [
              1,
              3,
              4,
              2,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12
            ],
            "example": 9
          },
          "nomeSocial": {
            "type": "string",
            "description": "Nome Social do candidato. Opcional. Quando preenchido, o sistema registra automaticamente o candidato como travesti ou transexual. Quando não informado ou vazio, essa marcação não é realizada.",
            "example": "Joana Oliveira"
          },
          "orientacaoSexual": {
            "type": "string",
            "description": "Orientação Sexual. Seguem os valores aceitos:\n  - A - Assexual\n  - B - Bissexual\n  - E - Heterossexual\n  - H - Homossexual\n  - N - Não informado\n  - P - Panssexual\n",
            "enum": [
              "A",
              "B",
              "E",
              "H",
              "N",
              "P"
            ],
            "example": "E"
          },
          "sexo": {
            "type": "string",
            "description": "Sexo. Seguem os valores aceitos:\n  - M - Masculino\n  - F - Feminino\n",
            "enum": [
              "M",
              "F"
            ],
            "example": "M"
          },
          "racaEtnia": {
            "type": "integer",
            "description": "Raça/Etnia do Funcionário. Seguem os valores aceitos:\n  - 0 - Indígena\n  - 2 - Branca\n  - 4 - Preta\n  - 6 - Amarela\n  - 8 - Parda\n",
            "enum": [
              0,
              2,
              4,
              6,
              8
            ],
            "example": 2
          },
          "observacaoDeficiencia": {
            "type": "string",
            "description": "Observação sobre Deficiência.",
            "example": "Deficiência auditiva leve"
          },
          "urlFotoPerfil": {
            "type": "string",
            "description": "URL da foto de perfil (PNG/JPEG).",
            "example": "https://imgur.com/abcd"
          },
          "anexosCpf": {
            "type": "array",
            "description": "Lista de anexos do CPF. Processados de forma assíncrona: o download não ocorre na mesma chamada, e sim em um processo em segundo plano executado periodicamente. O vínculo automático ao cadastro do funcionário depende de `statusRequisicao` (ver descrição do campo).",
            "items": {
              "$ref": "#/components/schemas/Anexo"
            }
          },
          "anexosAdmissao": {
            "type": "array",
            "description": "Lista de anexos do documento admissional. Processados de forma assíncrona: o download não ocorre na mesma chamada, e sim em um processo em segundo plano executado periodicamente. O vínculo automático ao cadastro do funcionário depende de `statusRequisicao` (ver descrição do campo).",
            "items": {
              "$ref": "#/components/schemas/Anexo"
            }
          },
          "nascimento": {
            "type": "object",
            "required": [
              "data",
              "nacionalidade",
              "nomeMae"
            ],
            "description": "Informações do Nascimento do Funcionário",
            "properties": {
              "data": {
                "type": "string",
                "format": "date",
                "description": "Data de Nascimento",
                "example": "01/11/1978"
              },
              "codigoUF": {
                "type": "integer",
                "description": "Unidade Federativa de Nascimento.\n\n\n  - Entidade relacionada: UnidadeFederativa\n  - Atributo: CODUF\n\n\nPara consultar os registros, utilize o modelo de requisição HTTP explicado [aqui](https://developer.sankhya.com.br/reference/get_loadrecords), utilizando como rootEntity o valor da entidade relacionada.\n",
                "example": 1
              },
              "codigoCidade": {
                "type": "integer",
                "description": "Código da Cidade de Nascimento.\n\n\n  - Entidade relacionada: Cidade \n  - Atributo: CODCID\n\n\nPara consultar os registros, utilize o modelo de requisição HTTP explicado [aqui](https://developer.sankhya.com.br/reference/get_loadrecords), utilizando como rootEntity o valor da entidade relacionada.\n",
                "example": 15
              },
              "codigoCidadeIbge": {
                "type": "integer",
                "description": "Código IBGE da Cidade de Nascimento.\n\n\n  - Entidade relacionada: Cidade \n  - Atributo: CODMUNFIS\n\n\nPara consultar os registros, utilize o modelo de requisição HTTP explicado [aqui](https://developer.sankhya.com.br/reference/get_loadrecords), utilizando como rootEntity o valor da entidade relacionada.\n",
                "example": "317020(Código de IBGE referente a Uberlândia/MG)"
              },
              "nacionalidade": {
                "type": "integer",
                "description": "Nacionalidade. Seguem os valores aceitos:\n  - 10 - Brasileiro\n  - 20 - Naturalizado Brasileiro\n  - 21 - Argentino\n  - 22 - Boliviano\n  - 23 - Chileno\n  - 24 - Paraguaio\n  - 25 - Uruguaio\n  - 26 - Venezuelano\n  - 27 - Colombiano\n  - 28 - Peruano\n  - 29 - Equatoriano\n  - 30 - Alemão\n  - 31 - Belga\n  - 32 - Britânico\n  - 34 - Canadense\n  - 35 - Espanhol\n  - 36 - Estadunidense\n  - 37 - Francês\n  - 38 - Suíço\n  - 39 - Italiano\n  - 40 - Haitiano\n  - 41 - Japonês\n  - 42 - Chinês\n  - 43 - Coreano\n  - 44 - Russo\n  - 45 - Português\n  - 46 - Paquistanês\n  - 47 - Indiano\n  - 48 - Outros Latinos\n  - 49 - Outros Asiáticos\n  - 51 - Outros Europeus\n  - 60 - Angolano\n  - 61 - Congolês\n  - 62 - Sul-Africano\n  - 70 - Outros Africanos\n  - 80 - Outros\n",
                "enum": [
                  10,
                  20,
                  21,
                  22,
                  23,
                  24,
                  25,
                  26,
                  27,
                  28,
                  29,
                  30,
                  31,
                  32,
                  34,
                  35,
                  36,
                  37,
                  38,
                  39,
                  40,
                  41,
                  42,
                  43,
                  44,
                  45,
                  46,
                  47,
                  48,
                  49,
                  51,
                  60,
                  61,
                  62,
                  70,
                  80
                ],
                "example": 10
              },
              "nomeMae": {
                "type": "string",
                "description": "Nome da Mãe do Funcionário",
                "example": "Maria Silva"
              },
              "nomePai": {
                "type": "string",
                "description": "Nome do Pai do Funcionário",
                "example": "José Silva"
              }
            }
          },
          "contato": {
            "type": "object",
            "required": [
              "email"
            ],
            "description": "Informações de Contato do Funcionário",
            "properties": {
              "email": {
                "type": "string",
                "description": "Email pessoal do Funcionário",
                "example": "funcionario@exemplo.com"
              },
              "emailCorporativo": {
                "type": "string",
                "description": "Email corporativo do funcionário. Campo opcional; quando informado, deve ser um endereço de e-mail válido (máximo 80 caracteres). Distinto do e-mail pessoal.",
                "example": "funcionario@empresa.com.br",
                "maxLength": 80
              },
              "celular": {
                "type": "string",
                "description": "Celular: DDD + número (apenas números)",
                "example": 11999999999
              },
              "telefone": {
                "type": "string",
                "description": "Telefone fixo: DDD + número (apenas números)",
                "example": 1123456789
              }
            }
          },
          "endereco": {
            "type": "object",
            "required": [
              "cep",
              "numero"
            ],
            "description": "Informações de Endereço do Funcionário",
            "properties": {
              "codigoEndereco": {
                "type": "integer",
                "description": "Código do Endereço: refere-se ao logradouro do endereço\n\n\n  - Entidade relacionada: Endereco\n  - Atributo: CODEND\n\n\nPara consultar os registros, utilize o modelo de requisição HTTP explicado [aqui](https://developer.sankhya.com.br/reference/get_loadrecords), utilizando como rootEntity o valor da entidade relacionada.\n",
                "example": 40
              },
              "numero": {
                "type": "string",
                "description": "Número do Endereço",
                "example": 123
              },
              "complemento": {
                "type": "string",
                "description": "Complemento do Endereço",
                "example": "Apto 101"
              },
              "codigoBairro": {
                "type": "integer",
                "description": "Código do Bairro\n\n\n  - Entidade relacionada: Bairro\n  - Atributo: CODBAI\n\n\nPara consultar os registros, utilize o modelo de requisição HTTP explicado [aqui](https://developer.sankhya.com.br/reference/get_loadrecords), utilizando como rootEntity o valor da entidade relacionada.\n",
                "example": 54
              },
              "codigoCidade": {
                "type": "integer",
                "description": "Código da Cidade\n\n\n  - Entidade relacionada: Cidade\n  - Atributo: CODCID\n\n\nPara consultar os registros, utilize o modelo de requisição HTTP explicado [aqui](https://developer.sankhya.com.br/reference/get_loadrecords), utilizando como rootEntity o valor da entidade relacionada.\n",
                "example": 15
              },
              "codigoUF": {
                "type": "integer",
                "description": "Unidade Federativa Endereço\n\n\n  - Entidade relacionada: UnidadeFederativaDestino\n  - Atributo: CODUF\n\n\nPara consultar os registros, utilize o modelo de requisição HTTP explicado [aqui](https://developer.sankhya.com.br/reference/get_loadrecords), utilizando como rootEntity o valor da entidade relacionada.\n",
                "example": 11
              },
              "codigoPais": {
                "type": "integer",
                "description": "Código do País\n\n\n  - Entidade relacionada: Pais\n  - Atributo: CODPAIS\n\n\nPara consultar os registros, utilize o modelo de requisição HTTP explicado [aqui](https://developer.sankhya.com.br/reference/get_loadrecords), utilizando como rootEntity o valor da entidade relacionada.\n",
                "example": 31
              },
              "cep": {
                "type": "string",
                "description": "CEP (apenas números)",
                "example": 38400100
              },
              "anexos": {
                "type": "array",
                "description": "Comprovante de Residência",
                "items": {
                  "type": "object",
                  "properties": {
                    "nome": {
                      "type": "string",
                      "example": "Conta de luz"
                    },
                    "url": {
                      "type": "string",
                      "example": "https://imgur.com/abcd"
                    }
                  }
                }
              }
            }
          },
          "contrato": {
            "type": "object",
            "description": "Informações de Contrato do Funcionário",
            "required": [
              "codigoEmpresa",
              "codigoDepartamento",
              "codigoCargaHoraria",
              "codigoCategoriaESocial",
              "horasSemanais",
              "regimePrevidencia",
              "regimeJornadaTrabalho",
              "regimeTrabalho",
              "vinculo",
              "sindicato",
              "admissao",
              "remuneracao",
              "fgts",
              "periodoExperiencia"
            ],
            "properties": {
              "codigoEmpresa": {
                "type": "integer",
                "description": "Código da Empresa do Funcionário\n\n\n  - Entidade relacionada: EmpresaPessoal\n  - Atributo: CODEMP\n\n\nPara consultar os registros, utilize o modelo de requisição HTTP explicado [aqui](https://developer.sankhya.com.br/reference/get_loadrecords), utilizando como rootEntity o valor da entidade relacionada.\n",
                "example": 1
              },
              "codigoDepartamento": {
                "type": "integer",
                "description": "Código do Departamento\n\n\n  - Entidade relacionada: Departamento\n  - Atributo: CODDEP\n\n\nPara consultar os registros, utilize o modelo de requisição HTTP explicado [aqui](https://developer.sankhya.com.br/reference/get_loadrecords), utilizando como rootEntity o valor da entidade relacionada.\n",
                "example": 100100
              },
              "codigoCargo": {
                "type": "integer",
                "description": "Código do Cargo do Funcionário\n\n\n  - Entidade relacionada: Cargo\n  - Atributo: CODCARGO\n\n\nPara consultar os registros, utilize o modelo de requisição HTTP explicado [aqui](https://developer.sankhya.com.br/reference/get_loadrecords), utilizando como rootEntity o valor da entidade relacionada. \\n\\nObservação:\\n - Essa informação será obrigatória, caso o padrão da empresa seja utilizar o cargo para vinculação ao CBO.\n",
                "example": 12
              },
              "codigoFuncao": {
                "type": "integer",
                "description": "Código da Função\n\n\n  - Entidade relacionada: Funcao\n  - Atributo: CODFUNCAO\n\n\nPara consultar os registros, utilize o modelo de requisição HTTP explicado [aqui](https://developer.sankhya.com.br/reference/get_loadrecords), utilizando como rootEntity o valor da entidade relacionada. Observação: Essa informação será obrigatória, caso o padrão da empresa seja utilizar a função para vinculação ao CBO.\n",
                "example": 9
              },
              "codigoCargaHoraria": {
                "type": "integer",
                "description": "Código de Identificação da Carga Horária\n\n\n  - Entidade relacionada: IdentificacaoCargaHoraria\n  - Atributo: CODCARGAHOR\n\n\nPara consultar os registros, utilize o modelo de requisição HTTP explicado [aqui](https://developer.sankhya.com.br/reference/get_loadrecords), utilizando como rootEntity o valor da entidade relacionada.\n",
                "example": 1
              },
              "codigoCategoria": {
                "type": "integer",
                "description": "Código da Categoria\n\n\n  - Entidade relacionada: Categoria\n  - Atributo: CODCATEG\n\n\nPara consultar os registros, utilize o modelo de requisição HTTP explicado [aqui](https://developer.sankhya.com.br/reference/get_loadrecords), utilizando como rootEntity o valor da entidade relacionada.\n",
                "example": 3
              },
              "codigoCategoriaESocial": {
                "type": "integer",
                "description": "Código de Categoria para o eSocial de acordo à Tabela 01 do eSocial\n\n\n  - Entidade relacionada: CategoriaEsocial\n  - Atributo: CODCATEGESOCIAL\n\n\nPara consultar os registros, utilize o modelo de requisição HTTP explicado [aqui](https://developer.sankhya.com.br/reference/get_loadrecords), utilizando como rootEntity o valor da entidade relacionada.\n",
                "example": 2
              },
              "codigoCidadeTrabalho": {
                "type": "integer",
                "description": "Código da Cidade de Trabalho\n\n\n  - Entidade relacionada: CidadeTrabalho\n  - Atributo: CODCID\n\n\nPara consultar os registros, utilize o modelo de requisição HTTP explicado [aqui](https://developer.sankhya.com.br/reference/get_loadrecords), utilizando como rootEntity o valor da entidade relacionada.\n",
                "example": 56
              },
              "codigoCidadeTrabalhoIbge": {
                "type": "integer",
                "description": "Código IBGE da Cidade de Trabalho\n\n\n  - Entidade relacionada: CidadeTrabalho\n  - Atributo: CODMUNFIS\n\n\nPara consultar os registros, utilize o modelo de requisição HTTP explicado [aqui](https://developer.sankhya.com.br/reference/get_loadrecords), utilizando como rootEntity o valor da entidade relacionada.\n",
                "example": "317020(Código de IBGE referente a Uberlândia/MG)"
              },
              "codigoGrupoContabil": {
                "type": "integer",
                "description": "Código do Grupo Contábil\n\n\n  - Entidade relacionada: GrupoContab\n  - Atributo: CODGRUPOCTBZ\n\n\nPara consultar os registros, utilize o modelo de requisição HTTP explicado [aqui](https://developer.sankhya.com.br/reference/get_loadrecords), utilizando como rootEntity o valor da entidade relacionada.\"\n",
                "default": 0
              },
              "horasSemanais": {
                "type": "number",
                "format": "float",
                "description": "Horas de trabalho semanal",
                "example": 40.5
              },
              "mei": {
                "type": "boolean",
                "description": "Microempreendedor Individual (MEI): Campo destinado a indicar se o trabalhador é um MEI.\n",
                "example": true
              },
              "percentualAdiantamento": {
                "type": "number",
                "format": "float",
                "description": "Percentual de Adiantamento",
                "example": 10.5
              },
              "percentualInsalubridade": {
                "type": "number",
                "format": "float",
                "description": "Percentual de Insalubridade",
                "example": 20
              },
              "percentualPericulosidade": {
                "type": "number",
                "format": "float",
                "description": "Percentual de Periculosidade",
                "example": 30
              },
              "regimePrevidencia": {
                "type": "integer",
                "description": "Regime de Previdência. Seguem os valores aceitos:\n  - 1 - RPPS - Regime Próprio de Previdência Social, Reg. Parlamentares e Sist. de Proteção de Militares\n  - 2 - RGPS - Regime Geral Previdência Social\n  - 3 - RPPS em extinção\n  - 4 - RPPE - Regime Próprio Prev. Social Exterior\n",
                "enum": [
                  1,
                  2,
                  3,
                  4
                ],
                "example": 1
              },
              "regimeJornadaTrabalho": {
                "type": "integer",
                "description": "Regime de Jornada de Trabalho (utiliza o padrão disponível na documentação do eSocial [versão S-1.3], atributo \"tpRegJor\"). Seguem os valores aceitos:\n  - 1 - Submetidos Horário Trabalho (Cap. II CLT)\n  - 2 - Atividade Externa conf.Inciso I Art. 62 CLT\n  - 3 - Funções conf.Inciso II Art. 62 CLT\n  - 4 - Teletrabalho, previsto Inciso III Art. 62 CLT\n",
                "enum": [
                  1,
                  2,
                  3,
                  4
                ],
                "example": 1
              },
              "regimeTrabalho": {
                "type": "integer",
                "description": "Regime de Trabalho. Seguem os valores aceitos:\n  - 1 - CLT - Consolidação das Leis de Trabalho\n  - 2 - RJU - Regime Jurídico Único\n  - 3 - RJP - Regime Jurídico Próprio\n",
                "enum": [
                  1,
                  2,
                  3
                ],
                "example": 1
              },
              "vinculo": {
                "type": "string",
                "description": "Tipo de Vínculo. Seguem os valores aceitos:\n  - 2 - Estagiário\n  - 10 - Prazo indeterminado pessoa jurídica\n  - 15 - Prazo indeterminado pessoa física\n  - 20 - Prazo indeterminado rural (jurídica)\n  - 25 - Prazo indeterminado rural (física)\n  - 30 - Regime jurídico único\n  - 31 - Regime Jurídico Único (RGPS)\n  - 35 - Público não efetivo\n  - 40 - Funcionário avulso\n  - 50 - Contrato temporário\n  - 55 - Menor aprendiz\n  - 60 - Prazo determinado urbano (jurídica)\n  - 65 - Prazo determinado urbano (física)\n  - 70 - Prazo determinado rural (jurídica)\n  - 75 - Prazo determinado rural (física)\n  - 80 - Diretor sem vínculo empregatício\n  - 90 - Autônomo\n  - 95 - Prazo determinado (Lei 8.745)\n  - 96 - Prazo determinado (Lei Estadual)\n  - 97 - Prazo Determinado (Lei Municipal)\n  - 99 - Pensionista\n",
                "enum": [
                  "2",
                  "10",
                  "15",
                  "20",
                  "25",
                  "30",
                  "31",
                  "35",
                  "40",
                  "50",
                  "55",
                  "60",
                  "65",
                  "70",
                  "75",
                  "80",
                  "90",
                  "95",
                  "96",
                  "97",
                  "99"
                ],
                "example": 99
              },
              "tipoTabela": {
                "type": "string",
                "description": "Tipo de Tabela: informação utilizada para o cadastro de tabela de faixas, que serão aplicadas nas fórmulas de cálculo dos eventos da folha de pagamento.\n\n\n  - Entidade relacionada: TipoTabela\n  - Atributo: TIPTAB\n\n\nPara consultar os registros, utilize o modelo de requisição HTTP explicado [aqui](https://developer.sankhya.com.br/reference/get_loadrecords), utilizando como rootEntity o valor da entidade relacionada.\"\n",
                "default": "A"
              },
              "trabalhaOutraEmpresa": {
                "type": "boolean",
                "description": "Trabalha em Outra Empresa: funcionário trabalha em mais de uma empresa (possui múltiplos vínculos)\n",
                "example": false
              },
              "codigoLocalTrabalho": {
                "type": "integer",
                "description": "Código do Local de Trabalho do Funcionário\n\n\n  - Entidade relacionada: LocalPontoPessoalMais\n  - Atributo: ID\n\n\nPara consultar os registros, utilize o modelo de requisição HTTP explicado [aqui](https://developer.sankhya.com.br/reference/get_loadrecords), utilizando como rootEntity o valor da entidade relacionada.\n",
                "example": 12
              },
              "sindicato": {
                "type": "object",
                "description": "Informações de Sindicato",
                "required": [
                  "codigo",
                  "sindicalizado"
                ],
                "properties": {
                  "codigo": {
                    "type": "integer",
                    "description": "Código do Sindicato\n\n\n  - Entidade relacionada: Sindicato\n  - Atributo: CODSIND\n\n\nPara consultar os registros, utilize o modelo de requisição HTTP explicado [aqui](https://developer.sankhya.com.br/reference/get_loadrecords), utilizando como rootEntity o valor da entidade relacionada.\n",
                    "example": 4
                  },
                  "sindicalizado": {
                    "type": "boolean",
                    "description": "Filiado ao Sindicato.",
                    "example": true
                  }
                }
              },
              "admissao": {
                "type": "object",
                "description": "Informações de Admissão do Funcionário",
                "required": [
                  "tipo",
                  "indicativo",
                  "data"
                ],
                "properties": {
                  "tipo": {
                    "type": "string",
                    "description": "Tipo de Admissão. Seguem os valores aceitos:\n  - A - Transferência de outro estabelecimento da mesma empresa sem ônus\n  - H - Admissão por sucessão, incorporação e cisão/fusão\n  - N - Admissão com emprego anterior\n  - U - Transferência de empresa considerada inapta por inexistência de fato\n  - R - Reintegração\n  - S - Admissão - Primeiro emprego\n  - T - Transferência de outro estabelecimento da mesma empresa com ônus\n  - O - Outros encerramentos\n",
                    "enum": [
                      "A",
                      "H",
                      "N",
                      "U",
                      "R",
                      "S",
                      "T",
                      "O"
                    ],
                    "example": "S"
                  },
                  "indicativo": {
                    "type": "integer",
                    "description": "Indicativo de Admissão (utiliza o padrão disponível na documentação do eSocial [versão S-1.3], atributo \"indAdmissao\"). Seguem os valores aceitos:\n  - 1 - Normal\n  - 2 - Decorrente Ação Fiscal\n  - 3 - Decorrente Decisão Judicial\n",
                    "enum": [
                      1,
                      2,
                      3
                    ],
                    "example": 1
                  },
                  "data": {
                    "type": "string",
                    "format": "date",
                    "description": "Data da Admissão do Funcionário",
                    "example": "01/11/2024"
                  }
                }
              },
              "remuneracao": {
                "type": "object",
                "description": "Informações de Remuneração do Funcionário",
                "required": [
                  "tipo",
                  "salarioBase",
                  "tipoSalario"
                ],
                "properties": {
                  "tipo": {
                    "type": "integer",
                    "description": "Tipo de Remuneração. Seguem os valores aceitos:\n  - 1 - Salário Fixo\n  - 2 - Variável\n  - 3 - Sal. Fixo + Variável\n",
                    "enum": [
                      1,
                      2,
                      3
                    ],
                    "example": 1
                  },
                  "base": {
                    "type": "number",
                    "format": "float",
                    "description": "Remuneração Base: campo usado quando funcionário não possui um salário fixo, mas deve receber um mínimo garantido.\n",
                    "example": 2500
                  },
                  "salarioBase": {
                    "type": "number",
                    "format": "float",
                    "description": "Salário Base do Funcionário: informar o salário fixo do funcionário\n",
                    "example": 3000
                  },
                  "tipoSalario": {
                    "type": "integer",
                    "description": "Tipo de Salário. Seguem os valores aceitos:\n  - 1 - Mensal\n  - 2 - Quinzenal\n  - 3 - Semanal\n  - 4 - Diarista\n  - 5 - Horista\n  - 6 - Tarefa\n",
                    "enum": [
                      1,
                      2,
                      3,
                      4,
                      5,
                      6
                    ],
                    "example": 1
                  }
                }
              },
              "fgts": {
                "type": "object",
                "description": "Informações de FGTS do Funcionário",
                "required": [
                  "optante",
                  "tabelaOcorrencia",
                  "tabelaCategoria"
                ],
                "properties": {
                  "dataOpcao": {
                    "type": "string",
                    "format": "date",
                    "description": "Data de Opção pelo FGTS",
                    "example": "01/11/2024"
                  },
                  "optante": {
                    "type": "boolean",
                    "description": "Optante pelo FGTS",
                    "example": true
                  },
                  "tabelaOcorrencia": {
                    "type": "string",
                    "description": "Tabela de Ocorrência FGTS. Seguem os valores aceitos:\n  - 00 - Não exposição a agente nocivo\n  - 01 - Não exposição a agente nocivo, mas já esteve\n  - 02 - Exposição a agente nocivo (aposentadoria aos 15)\n  - 03 - Exposição a agente nocivo (aposentadoria aos 20)\n  - 04 - Exposição a agente nocivo (aposentadoria aos 25)\n  - 05 - Não exposição a agente nocivo já esteve mult.vínculo\n  - 06 - Exposição a agente nocivo (apos. aos 15) mult.vínculo\n  - 07 - Exposição a agente nocivo (apos. aos 20) mult.vínculo\n  - 08 - Exposição a agente nocivo (apos. aos 25) mult.vínculo\n",
                    "enum": [
                      "00",
                      "01",
                      "02",
                      "03",
                      "04",
                      "05",
                      "06",
                      "07",
                      "08"
                    ],
                    "example": "00"
                  },
                  "tabelaCategoria": {
                    "type": "string",
                    "description": "Tabela de Categoria FGTS. Seguem os valores aceitos:\n  - 00 - Estagiários\n  - 01 - Empregados\n  - 02 - Trabalhador avulso\n  - 03 - Trabalhador sem RGPS mas com direito ao FGTS\n  - 04 - Empregado com contrato temporário ou intermitente\n  - 05 - Contribuinte individual - Diretor com FGTS\n  - 06 - Empregado doméstico\n  - 07 - Aprendiz - Lei 10.097/2000 ou Contrato Verde\n  - 11 - Diretor não empregado e empresários sem FGTS\n  - 12 - Demais agentes públicos\n  - 13 - Autônomo ou operador de máquina com FGTS\n  - 14 - Autônomo ou operador de máquina com salário base\n  - 26 - Dirigente sindical, adicional do sindicato; juiz classista temporário do Trabalho\n  - 27 - Contribuinte individual com remuneração do exterior sujeito ao recolhimento de FGTS\n  - 28 - Contribuinte individual - dirigente sindical com FGTS\n  - 29 - Contribuinte individual - trabalhador que presta serviço a entidade internacional no Brasil\n  - 30 - Estagiário contratado por missão diplomática/consulado\n  - 31 - Trabalhador contratado no exterior e transferido ao Brasil para contrato temporário\n  - 32 - Trabalhador intermitente contratado no exterior para prestar serviços no Brasil\n",
                    "enum": [
                      "00",
                      "01",
                      "02",
                      "03",
                      "04",
                      "05",
                      "06",
                      "07",
                      "11",
                      "12",
                      "13",
                      "14",
                      "26",
                      "27",
                      "28",
                      "29",
                      "30",
                      "31",
                      "32"
                    ],
                    "example": "00"
                  }
                }
              },
              "periodoExperiencia": {
                "type": "object",
                "description": "Informações do Período de Experiência do Funcionário",
                "properties": {
                  "dispensa": {
                    "type": "boolean",
                    "description": "Dispensa Período de Experiência. Quando false, o campo contrato.dataTerminoContrato é sempre calculado automaticamente a partir de dataVencimento1, ignorando qualquer valor informado nesse campo.",
                    "example": false
                  },
                  "dataVencimento1": {
                    "type": "string",
                    "format": "date",
                    "description": "Data final do primeiro período de experiência",
                    "example": "05/10/2021"
                  },
                  "dataVencimento2": {
                    "type": "string",
                    "format": "date",
                    "description": "Data final do segundo período de experiência",
                    "example": "25/11/2021"
                  }
                }
              },
              "dataTerminoContrato": {
                "type": "string",
                "format": "date",
                "description": "Data de Término do Contrato de trabalho. Obrigatório quando vinculo for prazo determinado ou contrato temporário (50, 55, 60, 65, 70, 75, 95, 96 ou 97) e periodoExperiencia.dispensa for true. Deve ser posterior ou igual à data de admissão. Quando periodoExperiencia.dispensa for false, este valor é ignorado mesmo que seja informado — a data de término é sempre recalculada automaticamente a partir de periodoExperiencia.dataVencimento1.",
                "example": "01/12/2026"
              },
              "dataAso": {
                "type": "string",
                "format": "date",
                "description": "Data de realização do Atestado de Saúde Ocupacional — ASO do funcionário.",
                "example": "05/10/2021"
              }
            }
          },
          "documentos": {
            "type": "object",
            "description": "Informações dos Documentos do Funcionário",
            "properties": {
              "pis": {
                "type": "object",
                "description": "Informações do PIS do funcionário",
                "properties": {
                  "numero": {
                    "type": "string",
                    "description": "Número do Programa de Integração Social (PIS)",
                    "example": 12345678901
                  },
                  "dataCadastro": {
                    "type": "string",
                    "format": "date",
                    "description": "Data de Cadastro no PIS",
                    "example": "05/11/2024"
                  }
                }
              },
              "cnh": {
                "type": "object",
                "description": "Informações da CNH do funcionário",
                "properties": {
                  "categoria": {
                    "type": "string",
                    "description": "Categoria da CNH. Seguem os valores aceitos:\n  - A\n  - B\n  - C\n  - D\n  - E\n\n\nPara condutor que tenha categoria de CNH com motocicleta e veículo, a letra A deve ser inserida. Ex.: AB\n",
                    "example": "B"
                  },
                  "dataEmissao": {
                    "type": "string",
                    "format": "date",
                    "description": "Data de emissão da CNH",
                    "example": "01/11/2024"
                  },
                  "numero": {
                    "type": "string",
                    "description": "Número da CNH",
                    "example": 1234567890
                  },
                  "uf": {
                    "type": "integer",
                    "description": "Unidade Federativa da CNH\n\n\n  - Entidade relacionada: UnidadeFederativaDestino\n  - Atributo: CODUF\n\n\npara consultar os registros, utilize o modelo de requisição HTTP explicado [aqui](https://developer.sankhya.com.br/reference/get_loadrecords), utilizando como rootEntity o valor da entidade relacionada.\n",
                    "example": 11
                  },
                  "vencimento": {
                    "type": "string",
                    "description": "Vencimento da CNH",
                    "example": "01/06/2025"
                  },
                  "orgao": {
                    "type": "string",
                    "description": "Órgão Emissor da CNH",
                    "example": "Detran-SP"
                  },
                  "dataPrimeira": {
                    "type": "string",
                    "format": "date",
                    "description": "Data da primeira CNH",
                    "example": "15/06/2024"
                  },
                  "anexos": {
                    "type": "array",
                    "description": "CNH (frente/verso).",
                    "items": {
                      "type": "object",
                      "properties": {
                        "nome": {
                          "type": "string",
                          "example": "CNH - frente"
                        },
                        "url": {
                          "type": "string",
                          "description": "URL do anexo. URL deverá ser pública e apontar para um arquivo de imagem, nos formatos PNG, JPEG ou PDF.\n",
                          "example": "https://imgur.com/abcd"
                        }
                      }
                    }
                  }
                }
              },
              "rg": {
                "type": "object",
                "description": "Informações do RG do funcionário",
                "properties": {
                  "numero": {
                    "type": "string",
                    "description": "Número do RG",
                    "example": 123456789
                  },
                  "data": {
                    "type": "string",
                    "format": "date",
                    "description": "Data de emissão do RG",
                    "example": "01/11/2024"
                  },
                  "orgaoEmissor": {
                    "type": "string",
                    "description": "Órgão Emissor RG",
                    "example": "SSP-SP"
                  },
                  "uf": {
                    "type": "integer",
                    "description": "Unidade Federativa (RG)\n\n\n  - Entidade relacionada: UnidadeFederativaOrigem\n  - Atributo: CODUF\n\n\nPara consultar os registros, utilize o modelo de requisição HTTP explicado [aqui](https://developer.sankhya.com.br/reference/get_loadrecords), utilizando como rootEntity o valor da entidade relacionada.\n",
                    "example": 11
                  },
                  "anexos": {
                    "type": "array",
                    "description": "RG (frente/verso).",
                    "items": {
                      "type": "object",
                      "properties": {
                        "nome": {
                          "type": "string",
                          "description": "Nome do anexo",
                          "example": "RG - frente"
                        },
                        "url": {
                          "type": "string",
                          "description": "URL do anexo. URL deverá ser pública e apontar para um arquivo de imagem, nos formatos PNG, JPEG ou PDF.\n",
                          "example": "https://imgur.com/abcd"
                        }
                      }
                    }
                  }
                }
              },
              "ctps": {
                "type": "object",
                "description": "Informações da Carteira de Trabalho do Funcionário (CTPS)",
                "properties": {
                  "digital": {
                    "type": "boolean",
                    "description": "Funcionário possui CTPS Digital",
                    "example": true
                  },
                  "numero": {
                    "type": "integer",
                    "description": "Número da CTPS",
                    "example": 1234567
                  },
                  "serie": {
                    "type": "string",
                    "description": "Série da CTPS",
                    "example": 12345
                  },
                  "codigoUF": {
                    "type": "integer",
                    "description": "Unidade Federativa (CTPS)\n\n\n  - Entidade relacionada: UnidadeFederativaDestino\n  - Atributo: CODUF\n\n\nPara consultar os registros, utilize o modelo de requisição HTTP explicado [aqui](https://developer.sankhya.com.br/reference/get_loadrecords), utilizando como rootEntity o valor da entidade relacionada.\n",
                    "example": 11
                  },
                  "data": {
                    "type": "string",
                    "format": "date",
                    "description": "Data da CTPS",
                    "example": "03/11/2024"
                  }
                }
              },
              "reservista": {
                "type": "object",
                "description": "Informações de Reservista do Funcionário",
                "properties": {
                  "numero": {
                    "type": "string",
                    "description": "Número da Reservista do Funcionário",
                    "example": 12345
                  }
                }
              },
              "tituloEleitoral": {
                "type": "object",
                "description": "Informações do Título Eleitoral do Funcionário",
                "properties": {
                  "numero": {
                    "type": "string",
                    "description": "Número do Título Eleitoral",
                    "example": 1234567890
                  },
                  "secao": {
                    "type": "string",
                    "description": "Seção Eleitoral",
                    "example": 432
                  },
                  "zona": {
                    "type": "string",
                    "description": "Zona Eleitoral",
                    "example": 12345
                  },
                  "anexos": {
                    "type": "array",
                    "description": "Título de Eleitor",
                    "items": {
                      "type": "object",
                      "properties": {
                        "nome": {
                          "type": "string",
                          "description": "Nome do anexo",
                          "example": "Título de Eleitor - Frente"
                        },
                        "url": {
                          "type": "string",
                          "description": "URL do anexo. URL deverá ser pública e apontar para um arquivo de imagem, nos formatos PNG, JPEG ou PDF.\n",
                          "example": "https://imgur.com/abcd"
                        }
                      }
                    }
                  }
                }
              },
              "passaporte": {
                "type": "object",
                "description": "Informações do Passaporte do Funcionário",
                "properties": {
                  "numero": {
                    "type": "string",
                    "description": "Número do Passaporte",
                    "example": "AB1234567"
                  },
                  "dataEmissao": {
                    "type": "string",
                    "format": "date",
                    "description": "Data de Emissão do Passaporte",
                    "example": "01/11/2024"
                  },
                  "dataValidade": {
                    "type": "string",
                    "format": "date",
                    "description": "Data de Validade do Passaporte",
                    "example": "01/11/2028"
                  },
                  "emissor": {
                    "type": "string",
                    "description": "Órgão Emissor do Passaporte",
                    "example": "Polícia Federal"
                  },
                  "codigoUF": {
                    "type": "string",
                    "description": "Unidade Federativa do Passaporte\n\n\n  - Entidade relacionada: UnidadeFederativaDestino\n  - Atributo: CODUF\n\n\nPara consultar os registros, utilize o modelo de requisição HTTP explicado [aqui](https://developer.sankhya.com.br/reference/get_loadrecords), utilizando como rootEntity o valor da entidade relacionada.\n",
                    "example": 11
                  }
                }
              }
            }
          },
          "trabalhadorEstrangeiro": {
            "type": "object",
            "description": "Informações do Funcionário Estrangeiro",
            "properties": {
              "classificacao": {
                "type": "integer",
                "description": "Classificação do Trabalhador Estrangeiro. Seguem os valores aceitos:\n  - 1 - Visto Permanente\n  - 2 - Visto Temporário\n  - 3 - Asilado\n  - 4 - Refugiado\n  - 5 - Solicitante de Refúgio\n  - 6 - Residente fora do Brasil\n  - 7 - Deficiente físico e com mais de 51 anos\n  - 8 - Com residência provisória e anistiado, em situação irregular\n  - 9 - Permanência no Brasil em razão de filhos ou cônjuge brasileiros\n  - 10 - Beneficiado pelo acordo entre países do Mercosul\n  - 11 - Dependente de agente diplomático e/ou consular\n  - 12 - Beneficiado pelo Tratado de Amizade, Cooperação e Consulta entre Brasil e Portugal\n",
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
                  12
                ],
                "example": 2
              },
              "prazoResidencia": {
                "type": "integer",
                "description": "Prazo de residência do trabalhador imigrante no Brasil (utiliza o padrão disponível na documentação do eSocial [versão S-1.3], atributo \"tmpResid\"). Seguem os valores aceitos:\n  - 1 - Prazo indeterminado\n  - 2 - Prazo determinado\n",
                "enum": [
                  1,
                  2
                ],
                "example": 1
              },
              "dataChegadaPais": {
                "type": "string",
                "format": "date",
                "description": "Data de chegada ao país",
                "example": "01/10/2024"
              },
              "casadoBrasil": {
                "type": "boolean",
                "description": "Casado(a) com brasileiro",
                "example": false
              },
              "filhosBrasileiros": {
                "type": "boolean",
                "description": "Possui filho brasileiro",
                "example": false
              },
              "rne": {
                "type": "object",
                "description": "Informações do Registro Nacional de Estrangeiro (RNE)",
                "properties": {
                  "numero": {
                    "type": "string",
                    "description": "Número do RNE",
                    "example": 12345678
                  },
                  "dataVencimento": {
                    "type": "string",
                    "format": "date",
                    "description": "Data de vencimento do RNE",
                    "example": "01/11/2024"
                  },
                  "orgaoEmissor": {
                    "type": "string",
                    "description": "Órgão Emissor RNE",
                    "example": "PF"
                  }
                }
              }
            }
          },
          "informacoesBancarias": {
            "type": "object",
            "description": "Informações Bancárias do Funcionário",
            "properties": {
              "codigoAgencia": {
                "type": "string",
                "description": "Código da Agência Bancária\n\n\n  - Entidade relacionada: AgenciaBancaria\n  - Atributo: CODAGE\n\n\nPara consultar os registros, utilize o modelo de requisição HTTP explicado [aqui](https://developer.sankhya.com.br/reference/get_loadrecords), utilizando como rootEntity o valor da entidade relacionada.\n",
                "example": "8739X"
              },
              "codigoBanco": {
                "type": "integer",
                "description": "Código do Banco\n\n\n  - Entidade relacionada: Banco\n  - Atributo: CODBCO\n\n\nPara consultar os registros, utilize o modelo de requisição HTTP explicado [aqui](https://developer.sankhya.com.br/reference/get_loadrecords), utilizando como rootEntity o valor da entidade relacionada.\n",
                "example": 2
              },
              "numeroConta": {
                "type": "string",
                "description": "Número da Conta Bancária\n",
                "example": "8739X"
              },
              "tipoConta": {
                "type": "string",
                "description": "Tipo de Conta Bancária. Seguem os valores aceitos:\n  - A - Aplicação\n  - C - Corrente\n  - P - Poupança\n  - S - Salário\n",
                "enum": [
                  "A",
                  "C",
                  "P",
                  "S"
                ],
                "example": "S"
              },
              "anexos": {
                "type": "array",
                "description": "Comprovantes de Conta Bancária",
                "items": {
                  "type": "object",
                  "properties": {
                    "nome": {
                      "type": "string",
                      "description": "Nome do anexo",
                      "example": "Conta Bancária"
                    },
                    "url": {
                      "type": "string",
                      "description": "URL do anexo. URL deverá ser pública e apontar para um arquivo de imagem, nos formatos PNG, JPEG ou PDF. example: https://imgur.com/abcd\n"
                    }
                  }
                }
              }
            }
          },
          "convenios": {
            "type": "object",
            "description": "Informações de Convênios do Funcionário",
            "properties": {
              "possuiConvenioMedico": {
                "type": "boolean",
                "description": "Possui Convênio Médico",
                "example": true
              },
              "possuiConvenioOdonto": {
                "type": "boolean",
                "description": "Possui Convênio Odontológico",
                "example": false
              },
              "possuiSeguroVida": {
                "type": "boolean",
                "description": "Possui Seguro de Vida",
                "example": true
              },
              "possuiValeTransporte": {
                "type": "boolean",
                "description": "Possui Vale Transporte",
                "example": false
              },
              "possuiValeAlimentacaoRefeicao": {
                "type": "boolean",
                "description": "Possui Vale Alimentação",
                "example": true
              }
            }
          },
          "observacao": {
            "type": "string",
            "description": "Observação da requisição de admissão: Essa informação será apresentada ao usuário do departamento pessoal da empresa, na visualização da requisição para aprovação.\n",
            "example": "Colaborador irá atuar no atendimento ao cliente."
          },
          "deficiencias": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Deficiencias"
            }
          },
          "dependentes": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/DependentesV2"
            }
          },
          "camposAdicionais": {
            "type": "array",
            "description": "Lista de campos adicionais (personalizados) a serem preenchidos na Requisição de Admissão. Propriedade opcional: se não enviada, ou enviada como lista vazia, a requisição é processada normalmente, sem qualquer alteração de comportamento.\n\nO campo adicional informado em nomeCampo deve estar previamente criado na entidade **Funcionário** (o mesmo campo adicional utilizado no cadastro de Funcionários). Não é possível criar um campo adicional através desta API — ele precisa já existir antes do envio da requisição. Para saber como criar um campo adicional na entidade Funcionário, consulte:\n  - [Como configurar um campo adicional para que ele seja apresentado no cadastro de Funcionários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360052263273-Como-configurar-um-campo-adicional-para-que-ele-seja-apresentado-no-cadastro-de-Funcion%C3%A1rios)\n  - [Dicionário de Dados (seção \"Criando um Campo Adicional\")](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados#criandoumcampoadicional)\n\nCaso um campo adicional configurado como obrigatório não seja informado (ou seja enviado vazio), a requisição não é bloqueada: ela é criada normalmente, e o usuário do departamento pessoal recebe uma notificação para completar o campo antes de aprovar a requisição.\n",
            "items": {
              "$ref": "#/components/schemas/CampoAdicional"
            }
          },
          "statusRequisicao": {
            "type": "string",
            "description": "Controla se a requisição já deve nascer aprovada (aprovação automática) ou seguir o fluxo normal de aprovação manual pelo Departamento Pessoal.\n  - Pendente (padrão): comportamento atual, a requisição é criada e aguarda aprovação manual.\n  - Aprovado: a requisição é criada e aprovada em uma única operação atômica (tudo ou nada) - se qualquer validação falhar, nenhum dado é gravado.\n\nEsse campo também determina o destino final dos anexos assíncronos (`anexosCpf`/`anexosAdmissao`):\n  - Aprovado: quando o processo em segundo plano terminar de baixar cada anexo, ele é automaticamente disponibilizado nos anexos do cadastro do funcionário já criado - sem necessidade de nenhuma ação manual.\n  - Pendente: o anexo baixado fica associado apenas à requisição. Mesmo que a requisição seja aprovada manualmente depois pela tela, o anexo não é vinculado automaticamente ao funcionário - é necessário incluí-lo manualmente pela aba de anexos do funcionário, ou marcar a opção correspondente na aprovação manual.\n",
            "enum": [
              "Pendente",
              "Aprovado"
            ],
            "default": "Pendente",
            "example": "Aprovado"
          },
          "aprovacaoRequisicao": {
            "type": "object",
            "description": "Parâmetros que controlam a aprovação automática da requisição. Só são considerados quando statusRequisicao=\"Aprovado\".",
            "properties": {
              "isParceiro": {
                "type": "boolean",
                "description": "Indica se um parceiro comercial deve ser criado/atualizado para o funcionário. Só é considerado quando statusRequisicao=\"Aprovado\".",
                "default": false,
                "example": false
              },
              "gerarCodigoFuncionarioAutomatico": {
                "type": "boolean",
                "description": "Indica se o código do funcionário deve ser gerado automaticamente. Só é considerado quando statusRequisicao=\"Aprovado\". Se false, codigoFuncionario passa a ser obrigatório.",
                "default": true,
                "example": true
              },
              "codigoFuncionario": {
                "type": "integer",
                "description": "Código do funcionário a ser utilizado na admissão. Obrigatório quando gerarCodigoFuncionarioAutomatico=false e statusRequisicao=\"Aprovado\". Validado como único por empresa.",
                "example": 1001
              },
              "gerarMatriculaAutomatica": {
                "type": "boolean",
                "description": "Indica se a matrícula do funcionário deve ser gerada automaticamente. Só é considerado quando statusRequisicao=\"Aprovado\". Se false, matricula passa a ser obrigatória.",
                "default": true,
                "example": true
              },
              "matricula": {
                "type": "integer",
                "description": "Matrícula do funcionário a ser utilizada na admissão. Obrigatória quando gerarMatriculaAutomatica=false e statusRequisicao=\"Aprovado\". Validada como única dentro do grupo econômico (empresas com a mesma matriz).",
                "example": 500123
              }
            }
          }
        }
      },
      "Anexo": {
        "type": "object",
        "description": "Arquivo anexado (nome + URL pública para PNG/JPEG/PDF)",
        "properties": {
          "nome": {
            "type": "string",
            "description": "Nome do anexo",
            "example": "Documento - frente"
          },
          "url": {
            "type": "string",
            "description": "URL do anexo. URL deverá ser pública e apontar para um arquivo de imagem, nos formatos PNG, JPEG ou PDF.\n",
            "example": "https://imgur.com/abcd"
          }
        }
      },
      "CampoAdicional": {
        "title": "Campo Adicional",
        "type": "object",
        "description": "Valor a ser preenchido em um campo adicional (personalizado) já existente na entidade Funcionário.",
        "required": [
          "nomeCampo",
          "valor"
        ],
        "properties": {
          "nomeCampo": {
            "type": "string",
            "description": "Nome exato do campo adicional, conforme cadastrado no Dicionário de Dados **na entidade Funcionário** (o mesmo campo adicional utilizado no cadastro de Funcionários — não é uma entidade específica de Requisição de Admissão). Deve começar obrigatoriamente com o prefixo \"AD_\".\n\nValidações aplicadas:\n  - O nome deve começar com \"AD_\", caso contrário a API retorna erro 400.\n  - O campo precisa existir previamente na entidade **Funcionário**, caso contrário a API retorna erro 400 indicando campo não encontrado.\n  - O mesmo nomeCampo não pode se repetir dentro do array camposAdicionais; se repetido, a API retorna erro 400 indicando duplicidade.\n",
            "example": "AD_APELIDO"
          },
          "valor": {
            "description": "Valor a ser gravado no campo. O tipo esperado depende de como o campo foi configurado no Dicionário de Dados:\n\n| Tipo do campo | Formato esperado no valor | Exemplo |\n|---|---|---|\n| Texto | string | \"João Silva\" |\n| Número (Inteiro ou Decimal) | number | 12345 ou 123.45 |\n| Data / Data e Hora | string, formato ISO 8601 (YYYY-MM-DD) | \"2024-01-15\" |\n| Checkbox | boolean | true |\n| Lista de Opções | string, com o valor da opção (não a descrição) | \"A\" |\n\nTipos de campo não aceitos (a API retorna erro 400 se o campo informado em nomeCampo for de um destes tipos): Binário, Hora, Texto Longo (CLOB) - Arquivo, Texto Longo (CLOB) - Múltiplo Arquivo, Texto Longo (CLOB) - Texto com Formatação HTML.\n\nValidações aplicadas sobre o valor:\n  - O valor deve ser compatível com o tipo configurado para o campo (ex.: não é possível enviar texto para um campo numérico). Se incompatível, a API retorna erro 400.\n  - Para campos do tipo Data / Data e Hora, o valor deve ser uma data existente no calendário, no formato YYYY-MM-DD (ex.: 2024-02-30 é inválido, fevereiro não tem 30 dias).\n  - Para campos do tipo Checkbox, o valor deve ser um booleano (true ou false).\n  - Para campos do tipo Lista de Opções, o valor deve corresponder ao valor de uma das opções predefinidas; se inválido, a API retorna erro 400 listando as opções aceitas.\n",
            "oneOf": [
              {
                "type": "string"
              },
              {
                "type": "number"
              },
              {
                "type": "boolean"
              }
            ],
            "example": "João Silva"
          }
        }
      },
      "DependentesV2": {
        "title": "Dependentes",
        "type": "object",
        "description": "'Versão v2 de dependentes: arrays de anexos para documentos.\n  Dependentes vinculados ao funcionário. Caso não possua, não informar a propriedade'\n",
        "required": [
          "pessoal",
          "dependencia"
        ],
        "properties": {
          "pessoal": {
            "type": "object",
            "required": [
              "nome",
              "cpf",
              "sexo"
            ],
            "properties": {
              "nome": {
                "type": "string",
                "description": "Nome do dependente",
                "example": "Joaquim da Silva"
              },
              "cpf": {
                "type": "string",
                "description": "CPF do dependente",
                "example": "12345678901"
              },
              "sexo": {
                "type": "string",
                "description": "Sexo. Seguem os valores aceitos:\n  - M - Masculino\n  - F - Feminino\n",
                "enum": [
                  "M",
                  "F"
                ],
                "example": "M"
              },
              "convenio": {
                "type": "boolean",
                "description": "Dependente de Convênio Médico",
                "example": true
              },
              "idadeEscolar": {
                "type": "boolean",
                "description": "Em idade escolar",
                "example": true
              },
              "incapazTrabalho": {
                "type": "boolean",
                "description": "Possui Incapacidade Física ou Mental para o Trabalho\n",
                "example": false
              },
              "adotivo": {
                "type": "boolean",
                "description": "Filho adotivo",
                "example": false
              },
              "racaEtnia": {
                "type": "integer",
                "description": "Raça/Etnia do dependente. Seguem os valores aceitos:\n  - 10 - Indígena\n  - 20 - Branca\n  - 30 - Preta\n  - 40 - Parda\n  - 50 - Amarela\n  - 60 - Não informado\n",
                "enum": [
                  10,
                  20,
                  30,
                  40,
                  50,
                  60
                ],
                "example": 20
              },
              "anexosCpf": {
                "type": "array",
                "description": "Anexos do CPF do Dependente.",
                "items": {
                  "$ref": "#/components/schemas/Anexo"
                }
              }
            }
          },
          "nascimento": {
            "type": "object",
            "description": "Informações de nascimento do dependente",
            "properties": {
              "data": {
                "type": "string",
                "format": "date",
                "description": "Data de nascimento do dependente",
                "example": "01/12/2000"
              },
              "nacionalidade": {
                "type": "integer",
                "description": "Nacionalidade. Seguem os valores aceitos:\n  - 10 - Brasileiro\n  - 20 - Naturalizado Brasileiro\n  - 21 - Argentino\n  - 22 - Boliviano\n  - 23 - Chileno\n  - 24 - Paraguaio\n  - 25 - Uruguaio\n  - 26 - Venezuelano\n  - 27 - Colombiano\n  - 28 - Peruano\n  - 29 - Equatoriano\n  - 30 - Alemão\n  - 31 - Belga\n  - 32 - Britânico\n  - 34 - Canadense\n  - 35 - Espanhol\n  - 36 - Estadunidense\n  - 37 - Francês\n  - 38 - Suíço\n  - 39 - Italiano\n  - 40 - Haitiano\n  - 41 - Japonês\n  - 42 - Chinês\n  - 43 - Coreano\n  - 44 - Russo\n  - 45 - Português\n  - 46 - Paquistanês\n  - 47 - Indiano\n  - 48 - Outros Latinos\n  - 49 - Outros Asiáticos\n  - 51 - Outros Europeus\n  - 60 - Angolano\n  - 61 - Congolês\n  - 62 - Sul-Africano\n  - 70 - Outros Africanos\n  - 80 - Outros\n",
                "enum": [
                  10,
                  20,
                  21,
                  22,
                  23,
                  24,
                  25,
                  26,
                  27,
                  28,
                  29,
                  30,
                  31,
                  32,
                  34,
                  35,
                  36,
                  37,
                  38,
                  39,
                  40,
                  41,
                  42,
                  43,
                  44,
                  45,
                  46,
                  47,
                  48,
                  49,
                  51,
                  60,
                  61,
                  62,
                  70,
                  80
                ],
                "example": 10
              },
              "naturalidade": {
                "type": "integer",
                "description": "Código da cidade de nascimento do dependente\n\n\n  - Entidade relacionada: Cidade\n  - Atributo: CODCID\n\n\nPara consultar os registros, utilize o modelo de requisição HTTP explicado [aqui](https://developer.sankhya.com.br/reference/get_loadrecords), utilizando como rootEntity o valor da entidade relacionada.\n",
                "example": 15
              },
              "naturalidadeIbge": {
                "type": "integer",
                "description": "Código IBGE da cidade de nascimento do dependente\n\n\n  - Entidade relacionada: Cidade\n  - Atributo: CODMUNFIS\n\n\nPara consultar os registros, utilize o modelo de requisição HTTP explicado [aqui](https://developer.sankhya.com.br/reference/get_loadrecords), utilizando como rootEntity o valor da entidade relacionada.\n",
                "example": "317020(Código de IBGE referente a Uberlândia/MG)"
              },
              "nomeMae": {
                "type": "string",
                "description": "Nome da mãe do dependente",
                "example": "Maria Silva"
              },
              "anexosRg": {
                "type": "array",
                "description": "Anexos de RG/Certidão de Nascimento do Dependente",
                "items": {
                  "$ref": "#/components/schemas/Anexo"
                }
              }
            }
          },
          "dependencia": {
            "type": "object",
            "description": "Informações de dependência do dependente",
            "required": [
              "grauParentesco"
            ],
            "properties": {
              "grauParentesco": {
                "type": "integer",
                "description": "Grau de parentesco do dependente em relação ao funcionário. Seguem os valores aceitos:\n  - 1 - Filho(a)\n  - 2 - Esposo(a)\n  - 3 - Pai/Mãe\n  - 4 - Sogro(a)\n  - 5 - Sobrinho(a)\n  - 6 - Inválido(a)\n  - 7 - Outros\n  - 8 - Filho(a) ou Enteado(a) Incapaz\n  - 9 - Irmão(ã), Neto(a) ou Bisneto(a)\n  - 10 - Irmão(ã), Neto(a) ou Bisneto(a) Incapaz\n  - 11 - Menor (Até 21 Anos) sem Condições Financeiras\n  - 12 - Companheiro(a) com filho ou mais de 5 (cinco) anos em união\n  - 13 - Ex-cônjuge que Receba Pensão de Alimentos\n  - 14 - Filho(a) ou enteado(a) universitário(a) ou cursando escola técnica de 2º grau, até 24 anos\n  - 15 - Irmão(ã), Neto(a) ou Bisneto(a) sem Arrimo dos Pais, do(a) qual Detenha a Guarda Judicial\n  - 16 - Pessoa Absolutamente Incapaz, da qual seja Tutor ou Curador\n  - 17 - Agregado(a)\n  - 18 - Enteado(a)\n",
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
                  14,
                  15,
                  16,
                  17,
                  18
                ],
                "example": 1
              },
              "dependenteIRRF": {
                "type": "boolean",
                "description": "Dependente de IRRF",
                "example": true
              },
              "dataInicioDependencia": {
                "type": "string",
                "format": "date",
                "description": "Data inicial da dependência",
                "example": "05/06/2019"
              },
              "dataFimDependencia": {
                "type": "string",
                "format": "date",
                "description": "Data final da dependência",
                "example": "12/02/2024"
              },
              "motivoInicio": {
                "type": "integer",
                "description": "Motivo do início da dependência. Seguem os valores aceitos:\n  - 10 - Nascimento\n  - 11 - Invalidez\n  - 12 - Casamento\n  - 13 - União estável\n  - 14 - Adoção\n  - 15 - Decisão judicial\n  - 16 - Dependência econômica\n  - 17 - Filho póstumo\n  - 18 - Tutela do menor\n  - 19 - Designação expressa pelo Servidor\n",
                "enum": [
                  10,
                  11,
                  12,
                  13,
                  14,
                  15,
                  16,
                  17,
                  18,
                  19
                ],
                "example": 10
              },
              "motivoFim": {
                "type": "integer",
                "description": "Motivo do fim da dependência. Seguem os valores aceitos:\n  - 50 - Maioridade\n  - 51 - Óbito\n  - 52 - Separação judicial\n  - 53 - Divórcio\n  - 54 - Emancipação\n  - 55 - Decisão judicial\n  - 56 - Cessação de invalidez\n  - 57 - Independência econômica\n  - 58 - Revogação de Tutela\n  - 59 - Exclusão expressa pelo Servidor\n",
                "enum": [
                  50,
                  51,
                  52,
                  53,
                  54,
                  55,
                  56,
                  57,
                  58,
                  59
                ],
                "example": 50
              },
              "dataLimiteIRRF": {
                "type": "string",
                "format": "date",
                "description": "Data limite do IRRF",
                "example": "26/09/2028"
              },
              "descricaoDependencia": {
                "type": "string",
                "description": "Descrição da Dependência",
                "example": "Observação dependência"
              }
            }
          },
          "pensao": {
            "type": "object",
            "description": "Informações de pensão do dependente",
            "properties": {
              "tipo": {
                "type": "string",
                "description": "Tipo da Pensão. Seguem os valores aceitos:\n  - L - Líquido\n  - B - Bruto\n  - S - Salário Mínimo\n  - P - Personalizado\n",
                "enum": [
                  "L",
                  "B",
                  "S",
                  "P"
                ],
                "example": "L"
              },
              "pensionista": {
                "type": "boolean",
                "description": "Pensionista",
                "example": false
              },
              "codigoParceiro": {
                "type": "integer",
                "description": "Código do parceiro responsável pelo recebimento dos valores de pensão.\n\n\n  - Entidade relacionada: Parceiro\n  - Atributo: CODPARC\n\n\nPara consultar os registros, utilize o modelo de requisição HTTP explicado [aqui](https://developer.sankhya.com.br/reference/get_loadrecords), utilizando como rootEntity o valor da entidade relacionada.\n",
                "example": 25
              },
              "percentual": {
                "type": "number",
                "format": "float",
                "description": "Percentual da Pensão",
                "example": 5.5
              },
              "valor": {
                "type": "number",
                "format": "float",
                "description": "Valor da Pensão",
                "example": 2000
              },
              "percentualRepassePensionista": {
                "type": "number",
                "description": "Percentual de Repasse ao Pensionista: campo recebe o percentual de pensão que será destinado a cada pensionista. Caso tenha apenas um, será sempre 100%\n",
                "format": "float",
                "example": 100
              },
              "percentualHomologNet": {
                "type": "number",
                "description": "Percentual de pensão a ser apresentado no TRCT",
                "format": "float",
                "example": 15
              },
              "percentualHomologNetFGTS": {
                "type": "number",
                "description": "Percentual de pensão incidente para o FGTS",
                "format": "float",
                "example": 15
              },
              "anexosOficioPensao": {
                "type": "array",
                "description": "Anexo do ofício de pensão do dependente",
                "items": {
                  "$ref": "#/components/schemas/Anexo"
                }
              }
            }
          },
          "salarioFamilia": {
            "type": "object",
            "description": "Informações de salário família do dependente",
            "properties": {
              "dependente": {
                "type": "boolean",
                "description": "É dependente de salário família",
                "example": false
              },
              "fazRepasse": {
                "type": "boolean",
                "description": "Repassa Salário Família ao Pensionista",
                "example": false
              },
              "dataLimite": {
                "type": "string",
                "description": "Data Limite do Salário Família",
                "format": "date",
                "example": "26/09/2028"
              }
            }
          },
          "auxilioCreche": {
            "type": "object",
            "description": "Informações de auxílio creche do dependente",
            "properties": {
              "receber": {
                "type": "boolean",
                "description": "Tem Auxílio Creche",
                "example": true
              },
              "temAtestado": {
                "type": "boolean",
                "description": "Apresentou Atestado",
                "example": true
              },
              "dataLimite": {
                "type": "string",
                "description": "Data Limite do Auxílio Creche",
                "format": "date",
                "example": "11/04/2026"
              }
            }
          }
        }
      },
      "Deficiencias": {
        "type": "object",
        "description": "Deficiências do Funcionário, caso possua. Caso não possua, não informar a propriedade. Pode ser informada mais de uma deficiência.\n",
        "properties": {
          "tipo": {
            "type": "integer",
            "description": "Tipo de Deficiência do Funcionário. Seguem os valores aceitos:\n  - 1 - Física\n  - 2 - Visual\n  - 3 - Auditiva\n  - 4 - Mental\n  - 5 - Intelectual\n  - 6 - Reabilitado\n  \n  \n  Observação: Pode ser informada mais de uma deficiência\n",
            "enum": [
              1,
              2,
              3,
              4,
              5,
              6
            ],
            "example": 2
          }
        }
      },
      "RequisicaoAdmissaoResponse": {
        "type": "object",
        "properties": {
          "codigoRequisicao": {
            "type": "integer",
            "description": "Código da requisição de admissão criada",
            "example": 13
          }
        }
      },
      "Requisicao_de_Admissaoretorno400": {
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
                "example": "O campo obrigatório 'cpf' está ausente na requisição de admissão."
              }
            }
          }
        }
      },
      "Requisicao_de_Admissaoretorno404": {
        "type": "object",
        "properties": {
          "statusCode": {
            "type": "integer",
            "format": "int32",
            "example": 404
          },
          "error": {
            "$ref": "#/components/schemas/Requisicao_de_AdmissaoretornoErro"
          }
        }
      },
      "Requisicao_de_AdmissaoretornoErro": {
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
            "example": "O registro [6] enviado não existe."
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
