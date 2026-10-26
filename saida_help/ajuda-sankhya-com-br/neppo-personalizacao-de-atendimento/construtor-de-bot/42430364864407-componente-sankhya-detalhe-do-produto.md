---
id: "42430364864407"
titulo: "Componente Sankhya - Detalhe do Produto"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430364864407-Componente-Sankhya-Detalhe-do-Produto"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T17:13:24Z"
rotulos: ["sync_hc", "neppo", "neppo_857999222", "sync_hash_819c2fdb7365"]
---

# Componente Sankhya - Detalhe do Produto

O componente **Detalhe do Produto** consulta no Sankhya as **informações cadastrais completas de um produto**, retornando dados como descrição, unidade padrão, marca, grupo, características, regras comerciais e eventuais controles (ex.: sabor, tamanho, cor).

Esse componente é usado para:

- Exibir informações detalhadas do produto no bot
- Validar dados antes de adicionar ao carrinho
- Identificar controles e variações disponíveis
- Obter regras comerciais como desconto máximo ou agrupamento mínimo

bot-server: **versão 1.7.0**

bot-component-service: **versão 1.3.0**

![Imagem 1: bot-component-service: versão 1.3.0](https://ajuda.sankhya.com.br/hc/article_attachments/42639677236759)

Índice:

- [Interface do componente (leitura da tela)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430364864407-Componente-Sankhya-Detalhe-do-Produto#Interface-do-componente-leitura-da-tela)
- [Integração técnica](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430364864407-Componente-Sankhya-Detalhe-do-Produto#Integracao-tecnica)
- [Estrutura do retorno (componente)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430364864407-Componente-Sankhya-Detalhe-do-Produto#Estrutura-do-retorno-componente)
- [Mapeamento técnico dos campos](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430364864407-Componente-Sankhya-Detalhe-do-Produto#Mapeamento-tecnico-dos-campos)
- [Campo especial: controls](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430364864407-Componente-Sankhya-Detalhe-do-Produto#Campo-especial-controls)
- [Exemplos de uso no bot](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430364864407-Componente-Sankhya-Detalhe-do-Produto#Exemplos-de-uso-no-bot)
- [Tratamento de erros](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430364864407-Componente-Sankhya-Detalhe-do-Produto#Tratamento-de-erros)
- [Boas práticas](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430364864407-Componente-Sankhya-Detalhe-do-Produto#Boas-praticas)

- [Dados do Cliente](https://sankhya.zendesk.com/hc/pt-br/articles/42430352793239)
- [Obter pedidos](https://sankhya.zendesk.com/hc/pt-br/articles/42430345961879)
- [Itens do Pedido](https://sankhya.zendesk.com/hc/pt-br/articles/42430353726743)
- [Criar Pedido](https://sankhya.zendesk.com/hc/pt-br/articles/42430354191767)
- [Preço do Produto](https://sankhya.zendesk.com/hc/pt-br/articles/42430386027287)
- [Estoque do Produto](https://sankhya.zendesk.com/hc/pt-br/articles/42430402782487)
- [Locais de Estoque](https://sankhya.zendesk.com/hc/pt-br/articles/42430348719383)
- [Volumes Alternativos](https://sankhya.zendesk.com/hc/pt-br/articles/42430361336343)
- [Obter Preferência](https://sankhya.zendesk.com/hc/pt-br/articles/42430349855127)
- [Tabela de Preço](https://sankhya.zendesk.com/hc/pt-br/articles/42430362758935)
- [Tipo de Operação](https://sankhya.zendesk.com/hc/pt-br/articles/42430406143383)
- [Tipos de Negociação](https://sankhya.zendesk.com/hc/pt-br/articles/42430364291351)
- [Detalhe do Produto](https://sankhya.zendesk.com/hc/pt-br/articles/42430364864407)
- [Busca de Produto](https://sankhya.zendesk.com/hc/pt-br/articles/42430376763159)
- [Adicionar ao Carrinho](https://sankhya.zendesk.com/hc/pt-br/articles/42430377203479)
- [Alterar Quantidade no Carrinho](https://sankhya.zendesk.com/hc/pt-br/articles/42430377845911)
- [Obter Itens do Carrinho](https://sankhya.zendesk.com/hc/pt-br/articles/42430378480151)

---

## Objetivo do componente

Disponibilizar no fluxo do bot os **dados oficiais do cadastro de produtos do Sankhya**, garantindo que as informações exibidas ao usuário estejam alinhadas com o ERP.

---

## Interface do componente (leitura da tela)

## Parâmetros

**Configuração da consulta de produto**

| Campo | Descrição | Origem Sankhya |
| --- | --- | --- |
| **Código do Produto**\* | Código único do produto no Sankhya | `TGFPRO.CODPROD` |

Esse campo pode receber:

```
1001
```

ou uma variável do fluxo:

```
{{codigoProduto}}
```

---

## Armazenamento

| Campo | Descrição |
| --- | --- |
| **Variável de armazenamento** | Nome da variável que receberá o resultado da consulta |
| **Variável de escopo global** | Permite reutilizar os dados em qualquer ponto do fluxo |

Exemplo:

```
produtoDetalhe
```

---

## Integração técnica

A consulta utiliza o serviço da API Sankhya:

```
CRUDServiceProvider.loadRecords
```

Entidade principal:

- **Produto (TGFPRO)**

Entidade auxiliar:

- **Volume (TGFVOL)** → utilizada para retornar a descrição da unidade.

---

## Exemplo de requisição

```
curl --location 'https://api.sankhya.com.br/gateway/v1/mge/service.sbr?serviceName=CRUDServiceProvider.loadRecords&outputType=json' \
--header 'Authorization: Bearer <TOKEN>' \
--header 'appkey: <APPKEY>' \
--header 'Content-Type: application/json' \
--data '{
"serviceName": "CRUDServiceProvider.loadRecords",
"requestBody": {
"dataSet": {
"rootEntity": "Produto",
"includePresentationFields": "S",
"tryJoinedFields": "true",
"parallelLoader": "true",
"offsetPage": "0",
"criteria": {
"expression": { "$": "CODPROD = ? AND ATIVO = ?" },
"parameter": [
{ "$": "1242", "type": "I" },
{ "$": "S", "type": "S" }
]
},
"entity": [
{
"path": "",
"fieldset": {
"list": "CODPROD,REFERENCIA,DESCRPROD,CODVOL,CODGRUPOPROD,USALOCAL,CODLOCALPADRAO,CODMARCA,MARCA,AGRUPMIN,DESCMAX,ATIVO,CARACTERISTICAS,COMPLDESC,HOMEPAGE,GRUPODESCPROD"
}
},
{
"path": "Volume",
"fieldset": { "list": "DESCRVOL" }
}
]
}
}
}'
```

---

## Estrutura do retorno (componente)

### Produto encontrado

```
{
  "found": true,
  "data": {
    "code": 1236,
    "reference": 91236,
    "description": "GUARANÁ SANTANA",
    "descriptionComplement": null,
    "characteristics": "Teste Caracteristicas",
    "control": null,
    "usesLocation": false,
    "defaultLocationCode": null,
    "minimumGrouping": null,
    "maxDiscount": 50,
    "active": true,
    "controls": [
      {
        "name": "Tamanho",
        "options": [
          "500ML",
          "1L",
          "2L"
        ]
      }
    ],
    "homepageUrl": null,
    "discountGroup": "TESTE",
    "defaultUnit": {
      "code": "UN",
      "description": "Unidade"
    },
    "group": {
      "code": 300000
    },
    "brand": {
      "code": 241,
      "name": "MINEIRO"
    }
  },
  "error": null
}
```

---

### Produto não encontrado

```
{
  "found": false,
  "data": null,
  "error": null
}
```

---

## Mapeamento técnico dos campos

| Campo | Descrição | Campo Sankhya | Tabela |
| --- | --- | --- | --- |
| data.code | Código do produto | CODPROD | TGFPRO |
| data.reference | Referência do produto | REFERENCIA | TGFPRO |
| data.description | Descrição do produto | DESCRPROD | TGFPRO |
| data.descriptionComplement | Complemento da descrição | COMPLDESC | TGFPRO |
| data.characteristics | Características do produto | CARACTERISTICAS | TGFPRO |
| data.control | Controle do produto | CONTROLE | TGFPRO |
| data.usesLocation | Indica uso de local | USALOCAL | TGFPRO |
| data.defaultLocationCode | Local padrão | CODLOCALPADRAO | TGFPRO |
| data.minimumGrouping | Agrupamento mínimo | AGRUPMIN | TGFPRO |
| data.maxDiscount | Desconto máximo permitido | DESCMAX | TGFPRO |
| data.active | Produto ativo | ATIVO | TGFPRO |
| data.homepageUrl | URL/Homepage | HOMEPAGE | TGFPRO |
| data.discountGroup | Grupo de desconto | GRUPODESCPROD | TGFPRO |
| data.defaultUnit.code | Unidade padrão | CODVOL | TGFPRO |
| data.defaultUnit.description | Descrição da unidade | DESCRVOL | TGFVOL |
| data.group.code | Grupo do produto | CODGRUPOPROD | TGFPRO |
| data.brand.code | Código da marca | CODMARCA | TGFPRO |
| data.brand.name | Nome da marca | MARCA | TGFPRO |

---

## Campo especial: controls

Quando o retorno da API Sankhya contém informações na estrutura `_rmd`, o componente interpreta esses dados e gera a lista:

```
data.controls
```

Essa lista representa **controles ou variações do produto**, por exemplo:

- Tamanho
- Sabor
- Cor
- Modelo

Exemplo:

```
Tamanho
 - 500ML
 - 1L
 - 2L
```

---

## Exemplos de uso no bot

### Exibir detalhes do produto

```
Produto: {{produtoDetalhe.data.description}}
Marca: {{produtoDetalhe.data.brand.name}}
Unidade: {{produtoDetalhe.data.defaultUnit.description}}
```

---

### Verificar se produto possui controle

```
Se {{produtoDetalhe.data.controls}} existir
→ Solicitar escolha da variação
```

---

### Validar desconto máximo permitido

```
Desconto máximo permitido: {{produtoDetalhe.data.maxDiscount}}%
```

---

## Tratamento de erros

| Situação | Comportamento |
| --- | --- |
| Produto inexistente | `found = false` |
| Produto inativo | não retornado quando filtro ativo |
| Falha na API | `error` preenchido |

---

## Boas práticas

- Sempre validar `found` antes de usar os dados
- Verificar se o produto possui **controles** antes de pedir escolha ao usuário
- Utilizar unidade padrão ao calcular preço
- Respeitar `minimumGrouping` quando houver

- [Dados do Cliente](https://sankhya.zendesk.com/hc/pt-br/articles/42430352793239)
- [Obter pedidos](https://sankhya.zendesk.com/hc/pt-br/articles/42430345961879)
- [Itens do Pedido](https://sankhya.zendesk.com/hc/pt-br/articles/42430353726743)
- [Criar Pedido](https://sankhya.zendesk.com/hc/pt-br/articles/42430354191767)
- [Preço do Produto](https://sankhya.zendesk.com/hc/pt-br/articles/42430386027287)
- [Estoque do Produto](https://sankhya.zendesk.com/hc/pt-br/articles/42430402782487)
- [Locais de Estoque](https://sankhya.zendesk.com/hc/pt-br/articles/42430348719383)
- [Volumes Alternativos](https://sankhya.zendesk.com/hc/pt-br/articles/42430361336343)
- [Obter Preferência](https://sankhya.zendesk.com/hc/pt-br/articles/42430349855127)
- [Tabela de Preço](https://sankhya.zendesk.com/hc/pt-br/articles/42430362758935)
- [Tipo de Operação](https://sankhya.zendesk.com/hc/pt-br/articles/42430406143383)
- [Tipos de Negociação](https://sankhya.zendesk.com/hc/pt-br/articles/42430364291351)
- [Detalhe do Produto](https://sankhya.zendesk.com/hc/pt-br/articles/42430364864407)
- [Busca de Produto](https://sankhya.zendesk.com/hc/pt-br/articles/42430376763159)
- [Adicionar ao Carrinho](https://sankhya.zendesk.com/hc/pt-br/articles/42430377203479)
- [Alterar Quantidade no Carrinho](https://sankhya.zendesk.com/hc/pt-br/articles/42430377845911)
- [Obter Itens do Carrinho](https://sankhya.zendesk.com/hc/pt-br/articles/42430378480151)
