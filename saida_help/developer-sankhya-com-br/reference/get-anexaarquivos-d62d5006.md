---
id: "https://developer.sankhya.com.br/reference/get_anexaarquivos"
titulo: "Anexar Arquivos"
url: "https://developer.sankhya.com.br/reference/get_anexaarquivos"
atualizado_em: "2026-05-13T15:12:48.000Z"
---

# Anexar Arquivos

<h1>Anexando documentos em registros específicos</h1>
A maioria das entidades do sistema permite anexar documentos em suas respectivas telas (ex.: cadastro de parceiros, cadastro de produtos, item da nota, contratos, etc.). O objetivo deste tutorial é apresentar como isso pode ser feito via API.
O processo é realizado em duas etapas: <ul>
  <li>o primeiro passo é enviar o arquivo para o servidor.</li>
  <li>o segundo passo salva o anexo e endereça ao respectivo registro.</li>
</ul>
Para ilustrar, apresentamos a seguir as duas requisições, detalhando o objetivo e impacto de cada ação, bem como o papel de cada atributo utilizado nas requisições.  
<br /><br /> 
<h2>Observação Importante</h2>
Este serviço de anexos é destinado para envio de anexos para entidades que utilizam o componente padrão de anexos (componente do "clipe") na interface do SankhyaOm.
Entidades que não exibem o ícone de clipe na tela - como, por exemplo, o Cabeçalho de Nota, Ordem de Serviço - não são compatíveis com este mecanismo de anexos destacado aqui.
<br /><br /> 
<h2>Parte 1: Envio do arquivo</h2>
A requisição basicamente faz um POST de um formulário do tipo multipart, enviando o documento utilizando uma sessionKey que será utilizada posteriormente, no serviço de endereçamento do anexo ao registro desejado. Seguem os principais atributos dessa requisição:<br /> 
<ul>
  <li>URL Gateway Produção: https://api.sankhya.com.br/</li>
  <li>URL Gateway Sandbox: https://api.sandbox.sankhya.com.br/</li>
</ul>
<b>URL de chamada</b>: https://[URL_GATEWAY]/gateway/v1/mge/sessionUpload.mge<br /> Com os seguintes parâmetros na URL: <ul>
  <li>sessionkey=ANEXO_SISTEMA_ItemNota_2097_1</li>
  <li>fitem=S</li>
  <li>salvar=S</li>
  <li>useCache=N</li>
</ul>
Dentre esses atributos, o parâmetro mais importante é o sessionkey, que sempre varia. Este parâmetro deve ser enviado no seguinte formato:<br /><br /> ANEXO_SISTEMA: sempre fixo<br /> nomeEntidade<br /> pkRegistro<br /> <br /> No exemplo acima, a entidade é ItemNota e a PK do item nota (que é composto) é NUNOTA 2097 e SEQUENCIA 1. Com isso temos: ANEXO_SISTEMA_ItemNota_2097_1<br /><br />
Em seguida, é necessário preparar o "formulário", onde o tipo (Content-Type) deve ser "multipart/form-data" com uma variável chamada "arquivo" contendo o endereço do anexo a ser enviado.<br /><br />
Veja a seguir um exemplo prático desta requisição em formato curl:<br /><br />

    curl --location 'https://[URL_GATEWAY]/gateway/v1/mge/sessionUpload.mge?sessionkey=ANEXO_SISTEMA_ItemNota_2097_1&fitem=S&salvar=S&useCache=N' \
    --header 'appkey: APPKEY_DA_SUA_APLICACAO_BEM_AQUI' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer BEAR_TOKEN_VALIDO_BEM_AQUI' \
    --header 'Accept: text/html' \
    --header 'Content-Type: multipart/form-data' \
    --form 'arquivo=@"MtBz0s5kk/foto_atualizada.jpg"'


<br /> Nesta requsição, estamos enviando a imagem "foto_atualizada.jpg". <br /><br /> <h2>Parte 2: Salvar  e Vincular anexo ao registro</h2> Agora que o anexo foi enviado para o servidor, é hora de realizar o “vínculo” do mesmo com o respectivo registro desejado.<br />
Veja os principais parâmetros variáveis desta requisição:<br />
<ul>
  <li>Nome do serviço: AnexoSistemaSP.salvar</li>
  <li>pkEntity: chave primária da entidade. No caso de chave composta, separa com _</li>
  <li>keySession: utilizar exatamente a mesma utilizada no serviço anterior.</li>
  <li>nameEntity: nome da entidade</li>
  <li>description: descrição desejada para anexo (texto com até 20 caracteres).</li>
  <li>nameAttach: nome para o anexo. Sugestão de enviar o mesmo nome que o documento tem, ao utilizar o serviço de enviar o anexo.</li>
</ul> Os demais parâmetros contidos na requisição, devem permanecer sempre fixos, conforme exemplo a seguir. <br /><br /> A seguir um exemplo da requisição:<br /> URL POST: https://[URL_GATEWAY]/gateway/v1/mge/service.sbr?serviceName=AnexoSistemaSP.salvar&outputType=json

    {
       "serviceName":"AnexoSistemaSP.salvar",
       "requestBody":{
          "params":{
             "pkEntity":"2097_1",
             "keySession":"ANEXO_SISTEMA_ItemNota_2097_1",
             "nameEntity":"ItemNota",
             "description":"Foto Atualizada 1",
             "keyAttach":"",
             "typeAcess":"ALL",
             "typeApres":"GLO",
             "nuAttach":"",
             "nameAttach":"foto_atualizada.jpg",
             "fileSelect":1,
             "oldFile":""
          }
       }
    }

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
      "name": "Serviços Especialistas",
      "description": "Serviços especialistas disponiveis no SankhyaOm"
    }
  ],
  "paths": {
    "/AnexaArquivos": {
      "get": {
        "tags": [
          "Serviços Especialistas"
        ],
        "summary": "Anexar Arquivos",
        "description": "<h1>Anexando documentos em registros específicos</h1>\nA maioria das entidades do sistema permite anexar documentos em suas respectivas telas (ex.: cadastro de parceiros, cadastro de produtos, item da nota, contratos, etc.). O objetivo deste tutorial é apresentar como isso pode ser feito via API.\nO processo é realizado em duas etapas: <ul>\n  <li>o primeiro passo é enviar o arquivo para o servidor.</li>\n  <li>o segundo passo salva o anexo e endereça ao respectivo registro.</li>\n</ul>\nPara ilustrar, apresentamos a seguir as duas requisições, detalhando o objetivo e impacto de cada ação, bem como o papel de cada atributo utilizado nas requisições.  \n<br /><br /> \n<h2>Observação Importante</h2>\nEste serviço de anexos é destinado para envio de anexos para entidades que utilizam o componente padrão de anexos (componente do \"clipe\") na interface do SankhyaOm.\nEntidades que não exibem o ícone de clipe na tela - como, por exemplo, o Cabeçalho de Nota, Ordem de Serviço - não são compatíveis com este mecanismo de anexos destacado aqui.\n<br /><br /> \n<h2>Parte 1: Envio do arquivo</h2>\nA requisição basicamente faz um POST de um formulário do tipo multipart, enviando o documento utilizando uma sessionKey que será utilizada posteriormente, no serviço de endereçamento do anexo ao registro desejado. Seguem os principais atributos dessa requisição:<br /> \n<ul>\n  <li>URL Gateway Produção: https://api.sankhya.com.br/</li>\n  <li>URL Gateway Sandbox: https://api.sandbox.sankhya.com.br/</li>\n</ul>\n<b>URL de chamada</b>: https://[URL_GATEWAY]/gateway/v1/mge/sessionUpload.mge<br /> Com os seguintes parâmetros na URL: <ul>\n  <li>sessionkey=ANEXO_SISTEMA_ItemNota_2097_1</li>\n  <li>fitem=S</li>\n  <li>salvar=S</li>\n  <li>useCache=N</li>\n</ul>\nDentre esses atributos, o parâmetro mais importante é o sessionkey, que sempre varia. Este parâmetro deve ser enviado no seguinte formato:<br /><br /> ANEXO_SISTEMA: sempre fixo<br /> nomeEntidade<br /> pkRegistro<br /> <br /> No exemplo acima, a entidade é ItemNota e a PK do item nota (que é composto) é NUNOTA 2097 e SEQUENCIA 1. Com isso temos: ANEXO_SISTEMA_ItemNota_2097_1<br /><br />\nEm seguida, é necessário preparar o \"formulário\", onde o tipo (Content-Type) deve ser \"multipart/form-data\" com uma variável chamada \"arquivo\" contendo o endereço do anexo a ser enviado.<br /><br />\nVeja a seguir um exemplo prático desta requisição em formato curl:<br /><br />\n\n    curl --location 'https://[URL_GATEWAY]/gateway/v1/mge/sessionUpload.mge?sessionkey=ANEXO_SISTEMA_ItemNota_2097_1&fitem=S&salvar=S&useCache=N' \\\n    --header 'appkey: APPKEY_DA_SUA_APLICACAO_BEM_AQUI' \\\n    --header 'Content-Type: application/json' \\\n    --header 'Authorization: Bearer BEAR_TOKEN_VALIDO_BEM_AQUI' \\\n    --header 'Accept: text/html' \\\n    --header 'Content-Type: multipart/form-data' \\\n    --form 'arquivo=@\"MtBz0s5kk/foto_atualizada.jpg\"'\n\n\n<br /> Nesta requsição, estamos enviando a imagem \"foto_atualizada.jpg\". <br /><br /> <h2>Parte 2: Salvar  e Vincular anexo ao registro</h2> Agora que o anexo foi enviado para o servidor, é hora de realizar o “vínculo” do mesmo com o respectivo registro desejado.<br />\nVeja os principais parâmetros variáveis desta requisição:<br />\n<ul>\n  <li>Nome do serviço: AnexoSistemaSP.salvar</li>\n  <li>pkEntity: chave primária da entidade. No caso de chave composta, separa com _</li>\n  <li>keySession: utilizar exatamente a mesma utilizada no serviço anterior.</li>\n  <li>nameEntity: nome da entidade</li>\n  <li>description: descrição desejada para anexo (texto com até 20 caracteres).</li>\n  <li>nameAttach: nome para o anexo. Sugestão de enviar o mesmo nome que o documento tem, ao utilizar o serviço de enviar o anexo.</li>\n</ul> Os demais parâmetros contidos na requisição, devem permanecer sempre fixos, conforme exemplo a seguir. <br /><br /> A seguir um exemplo da requisição:<br /> URL POST: https://[URL_GATEWAY]/gateway/v1/mge/service.sbr?serviceName=AnexoSistemaSP.salvar&outputType=json\n\n    {\n       \"serviceName\":\"AnexoSistemaSP.salvar\",\n       \"requestBody\":{\n          \"params\":{\n             \"pkEntity\":\"2097_1\",\n             \"keySession\":\"ANEXO_SISTEMA_ItemNota_2097_1\",\n             \"nameEntity\":\"ItemNota\",\n             \"description\":\"Foto Atualizada 1\",\n             \"keyAttach\":\"\",\n             \"typeAcess\":\"ALL\",\n             \"typeApres\":\"GLO\",\n             \"nuAttach\":\"\",\n             \"nameAttach\":\"foto_atualizada.jpg\",\n             \"fileSelect\":1,\n             \"oldFile\":\"\"\n          }\n       }\n    }",
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
