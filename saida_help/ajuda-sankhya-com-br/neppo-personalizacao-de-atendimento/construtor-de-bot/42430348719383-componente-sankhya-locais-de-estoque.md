---
id: "42430348719383"
titulo: "Componente Sankhya - Locais de Estoque"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430348719383-Componente-Sankhya-Locais-de-Estoque"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T17:13:27Z"
rotulos: ["sync_hc", "neppo", "neppo_857998872", "sync_hash_3d5973af9e46"]
---

# Componente Sankhya - Locais de Estoque

O componente **Locais de Estoque** permite consultar no ERP **Sankhya** os **locais de armazenamento vinculados a um produto**, retornando os locais configurados no cadastro do produto por empresa.

Essa consulta utiliza as informações definidas na tela **Produtos → aba “Impostos / Informações por empresa”**, especificamente o campo **Local Padrão**.

O resultado indica **em quais locais o produto pode ser armazenado ou movimentado**, permitindo que o bot determine corretamente **de qual local o estoque será considerado** durante o processo de venda.

bot-server: **versão 1.7.0**

bot-component-service: **versão 1.3.0**

![Imagem 1: bot-component-service: versão 1.3.0](https://ajuda.sankhya.com.br/hc/article_attachments/42639636662551)

Índice:

- [Objetivo do componente](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430348719383-Componente-Sankhya-Locais-de-Estoque#Objetivo-do-componente)
- [Interface do componente (leitura da tela)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430348719383-Componente-Sankhya-Locais-de-Estoque#Interface-do-componente-leitura-da-tela)
- [Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430348719383-Componente-Sankhya-Locais-de-Estoque#Armazenamento)
- [Integração técnica](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430348719383-Componente-Sankhya-Locais-de-Estoque#Integracao-tecnica)
- [Exemplo de requisição](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430348719383-Componente-Sankhya-Locais-de-Estoque#Exemplo-de-requisicao)
- [Estrutura do retorno (componente)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430348719383-Componente-Sankhya-Locais-de-Estoque#Estrutura-do-retorno-componente)
- [Descrição dos campos retornados](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430348719383-Componente-Sankhya-Locais-de-Estoque#Descricao-dos-campos-retornados)
- [Mapeamento técnico dos campos](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430348719383-Componente-Sankhya-Locais-de-Estoque#Mapeamento-tecnico-dos-campos)
- [Comportamento da consulta](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430348719383-Componente-Sankhya-Locais-de-Estoque#Comportamento-da-consulta)
- [Exemplos de uso no bot](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430348719383-Componente-Sankhya-Locais-de-Estoque#Exemplos-de-uso-no-bot)
- [Tratamento de erros](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430348719383-Componente-Sankhya-Locais-de-Estoque#Tratamento-de-erros)
- [Boas práticas](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430348719383-Componente-Sankhya-Locais-de-Estoque#Boas-praticas)

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

Permitir que o fluxo do bot identifique os **locais de estoque válidos para um produto**, garantindo que consultas de estoque e criação de pedidos utilizem locais compatíveis com o cadastro do ERP.

---

## Interface do componente (leitura da tela)

## Configuração de consulta

**Definição dos parâmetros da busca**

| Campo | Descrição | Origem Sankhya |
| --- | --- | --- |
| **Código do Produto**\* | Código único do produto no sistema | `TGFPRO.CODPROD` |
| **Empresa (opcional)** | Código da empresa associada ao produto | `TSIEMP.CODEMP` |
| **Continuar Listagem (opcional)** | Página da listagem para paginação | `offsetPage` |

### Código do produto

Exemplo:

```
PROD001
```

ou usando variável do fluxo:

```
{{codigoProduto}}
```

---

### Empresa (opcional)

Permite restringir a consulta a uma empresa específica.

Exemplo:

```
01
```

ou

```
{{codigoEmpresa}}
```

Quando não informado, a consulta pode retornar **locais cadastrados para o produto em diferentes empresas**.

---

### Continuar listagem (opcional)

Utilizado para paginação dos resultados.

| Valor | Comportamento |
| --- | --- |
| 0 | Retorna a primeira página |
| 1 | Retorna os próximos registros |
| 2+ | Continua avançando na listagem |

Exemplo:

```
0
```

---

## Armazenamento

| Campo | Descrição |
| --- | --- |
| **Variável de armazenamento** | Nome da variável que receberá o resultado da consulta |
| **Variável de escopo global** | Permite acessar os dados em qualquer fluxo |

Exemplo:

```
locaisEstoque
```

---

## Integração técnica

A consulta utiliza o serviço da API Sankhya:

```
CRUDServiceProvider.loadRecords
```

Entidade consultada:

**EmpresaProdutoImpostos**

Essa entidade contém as configurações de **informações do produto por empresa**, incluindo o **Local Padrão** de estoque.

---

## Exemplo de requisição

```
curl --location 'https://api.sankhya.com.br/gateway/v1/mge/service.sbr?serviceName=CRUDServiceProvider.loadRecords&outputType=json' \
--header 'Authorization: Bearer <TOKEN>' \
--header 'Content-Type: application/json' \
--data '{
"serviceName": "CRUDServiceProvider.loadRecords",
"requestBody": {
"dataSet": {
"rootEntity": "EmpresaProdutoImpostos",
"includePresentationFields": "S",
"offsetPage": "0",
"criteria": {
"expression": {
"$": "this.CODPROD = ? AND this.CODLOCALPAD != ? AND this.CODEMP = ?"
},
"parameter": [
{ "$": "1236", "type": "I" },
{ "$": "0", "type": "I" },
{ "$": "1", "type": "I" }
]
},
"entity": {
"fieldset": {
"list": "CODLOCALPAD"
}
}
}
}
}'
```

---

## Estrutura do retorno (componente)

### Exemplo de resposta

```
{
  "hasMore": false,
  "size": 1,
  "content": [
    {
      "location": {
        "code": 8000,
        "description": "Almoxarifado"
      },
      "product": {
        "code": 1236,
        "description": "GUARANÁ SANTANA"
      },
      "company": {
        "code": 1,
        "tradeName": "AUDAZ ATACADO/DISTRIBUIDOR"
      }
    }
  ],
  "error": null
}
```

---

## Descrição dos campos retornados

| Campo | Descrição |
| --- | --- |
| **hasMore** | Indica se existem mais registros disponíveis para paginação |
| **size** | Quantidade de registros retornados na consulta |
| **content[]** | Lista de locais de estoque retornados |
| **content[].location.code** | Código do local de estoque |
| **content[].location.description** | Descrição do local de estoque |
| **content[].product.code** | Código do produto |
| **content[].product.description** | Descrição do produto |
| **content[].company.code** | Código da empresa |
| **content[].company.tradeName** | Nome fantasia da empresa |
| **error** | Informações de erro quando a consulta falha |

---

## Mapeamento técnico dos campos

| Campo | Origem Sankhya | Tabela |
| --- | --- | --- |
| location.code | CODLOCALPAD | EmpresaProdutoImpostos |
| location.description | LocalFinanceiro\_DESCRLOCAL | TGFLOC |
| product.code | CODPROD | EmpresaProdutoImpostos |
| product.description | Produto\_DESCRPROD | TGFPRO |
| company.code | CODEMP | EmpresaProdutoImpostos |
| company.tradeName | Empresa\_NOMEFANTASIA | TSIEMP |

---

## Comportamento da consulta

O componente retorna os **locais de estoque configurados no cadastro do produto por empresa**.

Se um produto estiver configurado em múltiplas empresas, cada empresa poderá possuir **um local padrão diferente**.

Exemplo:

| Empresa | Produto | Local |
| --- | --- | --- |
| 1 | Guaraná Santana | Almoxarifado |
| 2 | Guaraná Santana | Depósito Central |

---

## Exemplos de uso no bot

### Selecionar local automaticamente

```
Local de estoque utilizado:
{{locaisEstoque.content[0].location.description}}
```

---

### Usar local para consulta de estoque

```
{{locaisEstoque.content[0].location.code}}
```

Esse valor pode ser utilizado em:

- **Estoque do Produto**
- **Criação do Pedido**
- **Consulta de preço**

---

## Tratamento de erros

| Situação | Comportamento |
| --- | --- |
| Produto inexistente | lista vazia |
| Produto sem local configurado | `size = 0` |
| Falha de integração | campo `error` preenchido |

---

## Boas práticas

- Sempre consultar o **Local de Estoque antes de consultar estoque**
- Utilizar o local retornado para consultas posteriores
- Validar `size > 0` antes de continuar o fluxo
- Evitar assumir um local fixo sem consulta

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
