---
id: "https://developer.sankhya.com.br/reference/get_logalteracoestabelas"
titulo: "Histórico de Alterações (LOG de Tabelas)"
url: "https://developer.sankhya.com.br/reference/get_logalteracoestabelas"
atualizado_em: "2026-05-13T15:12:48.000Z"
---

# Histórico de Alterações (LOG de Tabelas)

<h1>Regras de negócio</h1> 
Esse serviço permite consultar a data de alteração de um período específico que seja passado no campo dhAlter e entidades específicas passadas no campo Entidade. <br /><br />
Para utilizar a API, deve-se fazer uma requisição <b>POST</b> para o endpoint correspondente ao serviço desejado. <br />
<h3>Dependências</h3>
<br>Da versão `4.35 (ou superior) do SankhyaOm`, basta seguir [este guia](https://ajuda.sankhya.com.br/hc/pt-br/articles/34538747408407-Log-de-Altera%C3%A7%C3%B5es-para-API-como-ativar-desativar-e-acompanhar-os-registros-de-altera%C3%A7%C3%A3o) para para ativar a rotina.



<br> <br>Da versão 4.34, ou anterior, o processo é conforme segue: <br>1) Para que o serviço retorne informações, é necessário habilitar o parametro <b>LOGTABOPER</b> disponível nas Preferencias do SankhyaOm. Este liga ou desliga a funcionalidade de Log.<br /> ![Parâmetro para ativação da rotina](https://images2.imgbox.com/44/7b/MmiPYv6O_o.png)

<b>IMPORTANTE:</b> Ao ativar este parâmetro, serão criados gatilhos (triggers) no Banco de Dados. Durante o processo de ativação, pode haver um bloqueio temporário das tabelas, o que pode impactar a performance do SankhyaOM. Para minimizar qualquer impacto negativo no desempenho do sistema, recomendamos que a ativação do parâmetro seja realizada fora do horário de operação. <br>
<br /> 2) Temos também o parâmetro <b>LOGTABMAXAGE</b> que permite alterar a quantidade de dias que o Log ficará disponível. Por padrão, o tempo é de 3 dias corridos e este parâmetro permite alterar para até 7 dias corridos. Vale ressaltar que não é possível guardar os logs por mais de 7 dias. <br />
![Parâmetro para definição de tempo para armazenar os logs](https://images2.imgbox.com/62/0b/eaPMSbWT_o.png)



<h3>Entidades e tabelas logadas</h3>
Ao habilitar o parâmetro LOGTABOPER as seguintes entidades terão suas inserções, edições ou deleções logadas para consulta pela API Gateway: [link](https://developer.sankhya.com.br/reference/entidades-para-log-de-altera%C3%A7%C3%A3o)</br></br> 
<h3>Detalhes Técnicos</h3> O campo <u>entidades</u> é <b>obrigatório</b>. Ao menos uma entidade deve ser requisitada. <br />O campo <u>dhAlter</u> não é <b>obrigatório</b>. Quando não especificado, todos os logs referentes às entidades são consultados. Ao especificar a data e hora de alteração, são retornados os logs cuja a data de alteração é maior ou igual à dhAlter. <br/><br/>
<b>Importante:</b> O parâmetro modifiedSince recebe o padrão da data da RFC3339: “YYYY-MM-DDTHH24:MI:SS”<br />
<h3>Requisitos Mínimos</h3>
Versões do SankhyaOM:
  - 4.25b188;
  - 4.26b109;
  - 4.27 até 4.34;
  - A partir da 4.35 esta rotina é ativada através da tela <b>[Configurações » Rotinas » Log de Alterações para API](https://developer.sankhya.com.br/reference/entidades-para-log-de-altera%C3%A7%C3%A3o)</b> no SankhyaOm;
  - Banco de dados Oracle 11G ou superior;
  - Banco de Dados SQL Server 2017 ou superior.

<br /> Para realizarmos a busca através do Json, utilizamos o serviço <i><b>\"GatewayServiceProviderSP.logAlteracoesTabelas\".</b></i><br />
<h3>Exemplo de uso:</h3> <ul>
  <li>URL Gateway Produção: https://api.sankhya.com.br/</li>
  <li>URL Gateway Sandbox: https://api.sandbox.sankhya.com.br/</li>
</ul> <b>URL de chamada</b>: https://[URL_GATEWAY]/gateway/v1/mge/service.sbr?serviceName=GatewayServiceProviderSP.logAlteracoesTabelas&outputType=json
<br /><br /><b>Corpo de requisição</b>

    {
      "serviceName": "GatewayServiceProviderSP.logAlteracoesTabelas",
      "status": "1",
      "requestBody": {
      "dhAlter": "2023-01-27T11:00:28",
      "size":17,
      "page":0,
      "entidades": [
          {
            "nome": "Produto"
           },
           {
            "nome": "CabecalhoNota"
           },
           {
            "nome": "ItemNota"
           },
           {
            "nome": "Estoque"
           }
          ]
       }
    }


<b>Retorno:</b>

    {
        "serviceName": "GatewayServiceProviderSP.logAlteracoesTabelas",
        "status": "1",
        "pendingPrinting": "false",
        "transactionId": "2F153D4BD713800F9B770DCC4FA1FE12",
         "responseBody": {
            "registros": [
                {
                  "entidade": "Produto",
                  "dtAlter": "2023-02-27T08:14:46",
                  "evento": "CHANGE",
                  "pk": [
                     {
                      "nomeColumnPk": "CODPROD",
                      "valorPk": 1254
                     }
                   ]
                },
                {
                  "entidade": "CabecalhoNota",
                  "dtAlter": "2023-02-27T08:14:46",
                  "evento": "CHANGE",
                  "pk": [
                     {
                      "nomeColumnPk": "NUNOTA",
                      "valorPk": 2144
                     }
                  ]
                },
                {
                    "entidade": "ItemNota",
                    "dtAlter": "2023-02-27T09:00:12",
                    "evento": "CHANGE",
                    "pk": [
                        {
                            "nomeColumnPk": "NUNOTA",
                            "valorPk": 27283
                        },
                        {
                            "nomeColumnPk": "SEQUENCIA",
                            "valorPk": 1
                        }
                    ]
                },
                {
                    "entidade": "Estoque",
                    "dtAlter": "2023-02-27T09:01:14",
                    "evento": "CHANGE",
                    "pk": [
                        {
                            "nomeColumnPk": "CONTROLE",
                            "valorPk": "018-23-76800"
                        },
                        {
                            "nomeColumnPk": "TIPO",
                            "valorPk": "P"
                        },
                        {
                            "nomeColumnPk": "CODPARC",
                            "valorPk": 0
                        },
                        {
                            "nomeColumnPk": "CODLOCAL",
                            "valorPk": 70180000
                        },
                        {
                            "nomeColumnPk": "CODPROD",
                            "valorPk": 504
                        },
                        {
                            "nomeColumnPk": "CODEMP",
                            "valorPk": 1
                        }
                    ]
                }
            ]
         }
    }

Além disso, existe uma forma de otimizar o processo e utilizar um parametro na requisição direta no loadRecords para puxar apenas registros que foram alterados a partir de um determinado momento. Basta inclui a propriedade <i><b>\"modifiedSince\".</b></i> na requisição. <br />
<h3>Exemplo de uso direto no end-point loadRecords</h3>

    {
      "serviceName": "CRUDServiceProvider.loadRecords",
      "requestBody": {
        "dataSet": {
          "rootEntity": "Parceiro",
          "includePresentationFields": "N",
          "offsetPage": "0",
          "modifiedSince":"2024-04-16T12:59:59",
          "criteria": {
            "expression": {
              "$": ""
            }
          },
          "entity": {
            "fieldset": {
              "list": "CODPARC,NOMEPARC,FORNECEDOR,CLIENTE,CODCID,CLIENTE,CLASSIFICMS"
            }
          }
        }
      }
    }

<br />O exemplo acima retorna todos os Parceiroso  que foram editados a partir de 16/04/2024 12:59:59, conforme indicado no parametro <i><b>\"modifiedSince\".</b></i> presente na requisição.


# OpenAPI definition

```json
{
  "openapi": "3.0.3",
  "info": {
    "title": "API Sankhya - Legada",
    "description": "API de Integrações Sankhya\n\nEsta documentação apresenta os serviços disponíveis para cada objetivo e entidade. Você encontrará explicações sobre as regras de negócio, demonstrações de uso dos serviços e detalhes dos campos e opções.\n\nA API é baseada em chamadas HTTP ou HTTPS, utilizando os métodos POST e GET, com corpo no formato JSON. Qualquer sistema capaz de realizar uma chamada HTTP pode utilizar os serviços.\n\nO método PUT não é utilizado, pois as operações de inclusão ou atualização são feitas pelo método POST. Se a chave primária (PK) já existir, será feito um UPDATE; se não, um INSERT.\n\nO que é uma Entidade?\n\"Entidade\" refere-se a tudo que pode ser cadastrado, editado, consultado ou excluído no Sankhya. Por exemplo, um \"Produto\" pode ser cadastrado, editado, consultado ou excluído.\n\n**Exemplo de URL de Requisição:**\nA URL de requisição segue um padrão fixo:\n\n**URL padrão:**\nhttps://api.sankhya.com.br/gateway/v1/[modulo]/service.sbr?serviceName=[nomedoserviço]&outputType=json\n\n**Módulos Utilizados:**\n\n**MGE:**\nEste módulo é para consulta e gravação de dados de cadastros.\n\nExemplos de Serviços no MGE:\n- CRUDServiceProvider.loadRecords\n- CRUDServiceProvider.saveRecord\n- DbExplorerSP.executeQuery\n\nURL padrão MGE:\nhttps://api.sankhya.com.br/gateway/v1/mge/service.sbr?serviceName=[nomedoserviço]&outputType=json\n\n**MGECOM:**\nO módulo Comercial é para consulta e gravação de movimentações, como pedidos e compras.\n\nExemplos de Serviços no MGECOM:\n- CACSP.IncluirNota\n- CACSP.incluirAlterarItemNota\n- CACSP.excluirItemNota\n- CACSP.cancelarNota\n- SelecaoDocumentoSP.faturar\n\nURL padrão MGECOM:\nhttps://api.sankhya.com.br/gateway/v1/mgecom/service.sbr?serviceName=CACSP.IncluirNota&outputType=json\n\nImportante:\nOs serviços são específicos para cada módulo. Os serviços do módulo MGECOM são exclusivos e não funcionarão se a URL for para o módulo MGE, e vice-versa.\n\nPara utilizar todos os serviços, é necessário realizar o login conforme descrito na documentação.\n",
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
  "tags": [
    {
      "name": "Log de Alterações",
      "description": "Consultas de Histórico de Entidades"
    }
  ],
  "paths": {
    "/logAlteracoesTabelas": {
      "get": {
        "tags": [
          "Log de Alterações"
        ],
        "summary": "Histórico de Alterações (LOG de Tabelas)",
        "description": "<h1>Regras de negócio</h1> \nEsse serviço permite consultar a data de alteração de um período específico que seja passado no campo dhAlter e entidades específicas passadas no campo Entidade. <br /><br />\nPara utilizar a API, deve-se fazer uma requisição <b>POST</b> para o endpoint correspondente ao serviço desejado. <br />\n<h3>Dependências</h3>\n<br>Da versão `4.35 (ou superior) do SankhyaOm`, basta seguir [este guia](https://ajuda.sankhya.com.br/hc/pt-br/articles/34538747408407-Log-de-Altera%C3%A7%C3%B5es-para-API-como-ativar-desativar-e-acompanhar-os-registros-de-altera%C3%A7%C3%A3o) para para ativar a rotina.\n\n\n\n<br> <br>Da versão 4.34, ou anterior, o processo é conforme segue: <br>1) Para que o serviço retorne informações, é necessário habilitar o parametro <b>LOGTABOPER</b> disponível nas Preferencias do SankhyaOm. Este liga ou desliga a funcionalidade de Log.<br /> ![Parâmetro para ativação da rotina](https://images2.imgbox.com/44/7b/MmiPYv6O_o.png)\n\n<b>IMPORTANTE:</b> Ao ativar este parâmetro, serão criados gatilhos (triggers) no Banco de Dados. Durante o processo de ativação, pode haver um bloqueio temporário das tabelas, o que pode impactar a performance do SankhyaOM. Para minimizar qualquer impacto negativo no desempenho do sistema, recomendamos que a ativação do parâmetro seja realizada fora do horário de operação. <br>\n<br /> 2) Temos também o parâmetro <b>LOGTABMAXAGE</b> que permite alterar a quantidade de dias que o Log ficará disponível. Por padrão, o tempo é de 3 dias corridos e este parâmetro permite alterar para até 7 dias corridos. Vale ressaltar que não é possível guardar os logs por mais de 7 dias. <br />\n![Parâmetro para definição de tempo para armazenar os logs](https://images2.imgbox.com/62/0b/eaPMSbWT_o.png)\n\n\n\n<h3>Entidades e tabelas logadas</h3>\nAo habilitar o parâmetro LOGTABOPER as seguintes entidades terão suas inserções, edições ou deleções logadas para consulta pela API Gateway: [link](https://developer.sankhya.com.br/reference/entidades-para-log-de-altera%C3%A7%C3%A3o)</br></br> \n<h3>Detalhes Técnicos</h3> O campo <u>entidades</u> é <b>obrigatório</b>. Ao menos uma entidade deve ser requisitada. <br />O campo <u>dhAlter</u> não é <b>obrigatório</b>. Quando não especificado, todos os logs referentes às entidades são consultados. Ao especificar a data e hora de alteração, são retornados os logs cuja a data de alteração é maior ou igual à dhAlter. <br/><br/>\n<b>Importante:</b> O parâmetro modifiedSince recebe o padrão da data da RFC3339: “YYYY-MM-DDTHH24:MI:SS”<br />\n<h3>Requisitos Mínimos</h3>\nVersões do SankhyaOM:\n  - 4.25b188;\n  - 4.26b109;\n  - 4.27 até 4.34;\n  - A partir da 4.35 esta rotina é ativada através da tela <b>[Configurações » Rotinas » Log de Alterações para API](https://developer.sankhya.com.br/reference/entidades-para-log-de-altera%C3%A7%C3%A3o)</b> no SankhyaOm;\n  - Banco de dados Oracle 11G ou superior;\n  - Banco de Dados SQL Server 2017 ou superior.\n\n<br /> Para realizarmos a busca através do Json, utilizamos o serviço <i><b>\\\"GatewayServiceProviderSP.logAlteracoesTabelas\\\".</b></i><br />\n<h3>Exemplo de uso:</h3> <ul>\n  <li>URL Gateway Produção: https://api.sankhya.com.br/</li>\n  <li>URL Gateway Sandbox: https://api.sandbox.sankhya.com.br/</li>\n</ul> <b>URL de chamada</b>: https://[URL_GATEWAY]/gateway/v1/mge/service.sbr?serviceName=GatewayServiceProviderSP.logAlteracoesTabelas&outputType=json\n<br /><br /><b>Corpo de requisição</b>\n\n    {\n      \"serviceName\": \"GatewayServiceProviderSP.logAlteracoesTabelas\",\n      \"status\": \"1\",\n      \"requestBody\": {\n      \"dhAlter\": \"2023-01-27T11:00:28\",\n      \"size\":17,\n      \"page\":0,\n      \"entidades\": [\n          {\n            \"nome\": \"Produto\"\n           },\n           {\n            \"nome\": \"CabecalhoNota\"\n           },\n           {\n            \"nome\": \"ItemNota\"\n           },\n           {\n            \"nome\": \"Estoque\"\n           }\n          ]\n       }\n    }\n\n\n<b>Retorno:</b>\n\n    {\n        \"serviceName\": \"GatewayServiceProviderSP.logAlteracoesTabelas\",\n        \"status\": \"1\",\n        \"pendingPrinting\": \"false\",\n        \"transactionId\": \"2F153D4BD713800F9B770DCC4FA1FE12\",\n         \"responseBody\": {\n            \"registros\": [\n                {\n                  \"entidade\": \"Produto\",\n                  \"dtAlter\": \"2023-02-27T08:14:46\",\n                  \"evento\": \"CHANGE\",\n                  \"pk\": [\n                     {\n                      \"nomeColumnPk\": \"CODPROD\",\n                      \"valorPk\": 1254\n                     }\n                   ]\n                },\n                {\n                  \"entidade\": \"CabecalhoNota\",\n                  \"dtAlter\": \"2023-02-27T08:14:46\",\n                  \"evento\": \"CHANGE\",\n                  \"pk\": [\n                     {\n                      \"nomeColumnPk\": \"NUNOTA\",\n                      \"valorPk\": 2144\n                     }\n                  ]\n                },\n                {\n                    \"entidade\": \"ItemNota\",\n                    \"dtAlter\": \"2023-02-27T09:00:12\",\n                    \"evento\": \"CHANGE\",\n                    \"pk\": [\n                        {\n                            \"nomeColumnPk\": \"NUNOTA\",\n                            \"valorPk\": 27283\n                        },\n                        {\n                            \"nomeColumnPk\": \"SEQUENCIA\",\n                            \"valorPk\": 1\n                        }\n                    ]\n                },\n                {\n                    \"entidade\": \"Estoque\",\n                    \"dtAlter\": \"2023-02-27T09:01:14\",\n                    \"evento\": \"CHANGE\",\n                    \"pk\": [\n                        {\n                            \"nomeColumnPk\": \"CONTROLE\",\n                            \"valorPk\": \"018-23-76800\"\n                        },\n                        {\n                            \"nomeColumnPk\": \"TIPO\",\n                            \"valorPk\": \"P\"\n                        },\n                        {\n                            \"nomeColumnPk\": \"CODPARC\",\n                            \"valorPk\": 0\n                        },\n                        {\n                            \"nomeColumnPk\": \"CODLOCAL\",\n                            \"valorPk\": 70180000\n                        },\n                        {\n                            \"nomeColumnPk\": \"CODPROD\",\n                            \"valorPk\": 504\n                        },\n                        {\n                            \"nomeColumnPk\": \"CODEMP\",\n                            \"valorPk\": 1\n                        }\n                    ]\n                }\n            ]\n         }\n    }\n\nAlém disso, existe uma forma de otimizar o processo e utilizar um parametro na requisição direta no loadRecords para puxar apenas registros que foram alterados a partir de um determinado momento. Basta inclui a propriedade <i><b>\\\"modifiedSince\\\".</b></i> na requisição. <br />\n<h3>Exemplo de uso direto no end-point loadRecords</h3>\n\n    {\n      \"serviceName\": \"CRUDServiceProvider.loadRecords\",\n      \"requestBody\": {\n        \"dataSet\": {\n          \"rootEntity\": \"Parceiro\",\n          \"includePresentationFields\": \"N\",\n          \"offsetPage\": \"0\",\n          \"modifiedSince\":\"2024-04-16T12:59:59\",\n          \"criteria\": {\n            \"expression\": {\n              \"$\": \"\"\n            }\n          },\n          \"entity\": {\n            \"fieldset\": {\n              \"list\": \"CODPARC,NOMEPARC,FORNECEDOR,CLIENTE,CODCID,CLIENTE,CLASSIFICMS\"\n            }\n          }\n        }\n      }\n    }\n\n<br />O exemplo acima retorna todos os Parceiroso  que foram editados a partir de 16/04/2024 12:59:59, conforme indicado no parametro <i><b>\\\"modifiedSince\\\".</b></i> presente na requisição.\n",
        "responses": {
          "201": {
            "description": "Consulta efetuada com sucesso"
          },
          "400": {
            "description": "Requisição inválida"
          },
          "500": {
            "description": "Erro interno do servidor"
          }
        }
      }
    }
  }
}
```
