---
id: "42430361336343"
titulo: "Componente Sankhya - Volumes Alternativos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430361336343-Componente-Sankhya-Volumes-Alternativos"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T17:13:26Z"
rotulos: ["sync_hc", "neppo", "neppo_857998926", "sync_hash_63c508c3656d"]
---

# Componente Sankhya - Volumes Alternativos

O componente **Volumes Alternativos do Produto** consulta na Sankhya as **unidades alternativas** disponíveis para comercialização/expedição de um produto (ex.: `UN`, `CX`, `FD`), retornando a equivalência com a unidade base e, quando configurado, **regras de fator de preço** (multiplica/divide) e informações complementares como **cubagem**.

bot-server: **versão 1.6.0**

bot-component-service: **versão 1.2.0**

Doc Sankhya: <https://developer.sankhya.com.br/reference/get_loadrecords>

![Imagem 1: Doc Sankhya: https://developer.sankhya.com.br/reference/get_loadrecords](https://ajuda.sankhya.com.br/hc/article_attachments/42639658610967)

Esse componente é útil para:

- Listar opções válidas de unidade no bot (ex.: “Unidade” vs “Caixa”)
- Calcular equivalência de quantidade na unidade base
- Definir regras comerciais por volume alternativo
- Respeitar configurações por **controle** quando existirem (sabor/cor/tamanho)

Índice:

- [Objetivo do componente](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430361336343-Componente-Sankhya-Volumes-Alternativos#Objetivo-do-componente)
- [Integração técnica](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430361336343-Componente-Sankhya-Volumes-Alternativos#Integracao-tecnica)
- [Interface do componente (tela)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430361336343-Componente-Sankhya-Volumes-Alternativos#Interface-do-componente-tela)
- [Estrutura do retorno](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430361336343-Componente-Sankhya-Volumes-Alternativos#Estrutura-do-retorno)
- [Descrição dos campos retornados](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430361336343-Componente-Sankhya-Volumes-Alternativos#Descricao-dos-campos-retornados)
- [Contextualização de negócio](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430361336343-Componente-Sankhya-Volumes-Alternativos#Contextualizacao-de-negocio)
- [Exemplo de requisição (Sankhya)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430361336343-Componente-Sankhya-Volumes-Alternativos#Exemplo-de-requisicao-Sankhya)
- [Exemplos de uso no bot](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430361336343-Componente-Sankhya-Volumes-Alternativos#Exemplos-de-uso-no-bot)
- [Tratamento de erros](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430361336343-Componente-Sankhya-Volumes-Alternativos#Tratamento-de-erros)
- [Alerta técnico de paginação (Sankhya)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430361336343-Componente-Sankhya-Volumes-Alternativos#Alerta-tecnico-de-paginacao-Sankhya)
- [Tela no Sankhya OM](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430361336343-Componente-Sankhya-Volumes-Alternativos#Tela-no-Sankhya-OM)
- [Boas práticas](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430361336343-Componente-Sankhya-Volumes-Alternativos#Boas-praticas)

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

Disponibilizar no fluxo do bot as unidades alternativas cadastradas no Sankhya para um produto, permitindo que o usuário escolha a unidade correta e que a automação siga regras coerentes com o ERP.

---

## Integração técnica

A consulta é realizada via serviço da API Sankhya:

- `CRUDServiceProvider.loadRecords`
- Entidade: `VolumeAlternativo`
- Relacionamento para apresentação: `Volume (DESCRVOL)`

O filtro normalmente considera:

- Produto (`CODPROD`)
- Ativo (`ATIVO = 'S'`)
- (Opcional) regras por controle, quando aplicável

---

## Interface do componente (tela)

### Dados do produto

| Campo | Descrição |
| --- | --- |
| **Código do produto**\* | Código único do produto no Sankhya (`CODPROD`). Obrigatório. |
| **Controle (opcional)** | Quando utilizado, permite filtrar volumes associados a uma variação (sabor/cor/tamanho), se existir cadastro por controle. |

> Observação: na prática, muitos ambientes não vinculam volume alternativo ao controle. Quando existir, é um refinamento importante.

---

### Armazenamento

| Campo | Descrição |
| --- | --- |
| **Variável de armazenamento** | Variável que receberá o retorno (ex.: `volumesAlternativos`). |
| **Variável de escopo Global** | Quando ativada, a variável fica acessível em todo o fluxo. |

---

## Estrutura do retorno

### Exemplo de resposta

```
{
  "hasMore": false,
  "size": 1,
  "content": [
    {
      "unitCode": "CX",
      "unitDescription": "Caixa",
      "baseUnitQuantity": 24,
      "priceFactor": 1,
      "priceFactorOperation": "M",
      "active": true,
      "cubicMeters": null,
      "productControl": null
    }
  ],
  "error": null
}
```

---

## Descrição dos campos retornados

| Campo | Descrição |
| --- | --- |
| hasMore | Indica se existem mais itens para paginação |
| size | Total de volumes alternativos retornados (considerando filtros) |
| content | Lista de volumes/unidades alternativas |
| content[].unitCode | Código do volume/unidade alternativa (ex.: UN, CX) |
| content[].unitDescription | Descrição do volume/unidade alternativa |
| content[].baseUnitQuantity | Equivalência com unidade base (ex.: 1 CX = 24 UN) |
| content[].priceFactor | Fator de preço associado ao volume alternativo |
| content[].priceFactorOperation | Operação do fator: `M` (multiplica) ou `D` (divide) |
| content[].active | Indica se o volume alternativo está ativo |
| content[].cubicMeters | Cubagem (m³) quando configurada |
| content[].productControl | Controle vinculado ao volume (quando aplicável) |
| error | Detalhes do erro quando falhar (nulo em sucesso) |

---

## Contextualização de negócio

**Volumes alternativos (unidades alternativas)** representam formas adicionais de comercialização/expedição do mesmo produto, definindo:

- **Equivalência com unidade base** (ex.: “Caixa” = 24 “Unidades”)
- **Fator de preço** (multiplicar/dividir), quando configurado
- **Cubagem** (m³), quando aplicável
- **Possível variação por controle** (quando o cadastro existir)

Essas informações podem ser verificadas diretamente no Sankhya em:

**Produtos → aba “Unidades Alternativas”**

---

## Exemplo de requisição (Sankhya)

A consulta é feita usando `CRUDServiceProvider.loadRecords` na entidade `VolumeAlternativo`, filtrando por produto e ativo, retornando também descrição do volume via entidade relacionada `Volume`.

```
curl --location 'https://api.sankhya.com.br/gateway/v1/mge/service.sbr?serviceName=CRUDServiceProvider.loadRecords&outputType=json' \
--header 'Authorization: Bearer <TOKEN>' \
--header 'appkey: 3a51f41d-ebc4-429f-a888-55ff9fb48d34' \
--header 'Content-Type: application/json' \
--data '{
  "serviceName": "CRUDServiceProvider.loadRecords",
  "requestBody": {
    "dataSet": {
      "rootEntity": "VolumeAlternativo",
      "includePresentationFields": "N",
      "offsetPage": "0",
      "criteria": {
        "expression": {
          "$": "ATIVO = ? AND CODPROD = ?"
        },
        "parameter": [
          { "$": "S", "type": "S" },
          { "$": "1236", "type": "I" }
        ]
      },
      "entity": [
        {
          "path": "",
          "fieldset": {
            "list": "CODVOL, QUANTIDADE, MULTIPVLR, ATIVO, M3, DIVIDEMULTIPLICA"
          }
        },
        {
          "path": "Volume",
          "fieldset": {
            "list": "DESCRVOL"
          }
        }
      ]
    }
  }
}'
```

---

## Exemplos de uso no bot

### Listar unidades alternativas para escolha do usuário

- “Você quer comprar em qual unidade?”

  - `UN - Unidade`
  - `CX - Caixa`

Exemplo de leitura:

```
{{volumesAlternativos.content[0].unitCode}} - {{volumesAlternativos.content[0].unitDescription}}
```

---

### Converter quantidade para unidade base

Se o usuário pedir 2 caixas e `baseUnitQuantity = 24`:

- total base = `2 * 24` = `48 unidades`

---

### Aplicar fator de preço (quando configurado)

Se:

- `priceFactorOperation = M`
- `priceFactor = 1.2`

Então o preço ajustado pode ser:

- `precoFinal = precoBase * 1.2`

> Observação: em muitos cenários, o fator de preço é só informativo e o preço final deve ser calculado pelo **serviço de preço** (seu componente de Preço do Produto).

---

## Tratamento de erros

| Situação | Comportamento |
| --- | --- |
| Produto sem unidade alternativa | `size = 0`, `content = []` |
| Falha na API | `error` preenchido |
| Paginação | respeitar `hasMore` e `offsetPage` |

Iremos disponibilizar exemplos de erro em breve.

---

## Alerta técnico de paginação (Sankhya)

A API da Sankhya pode retornar novamente a **página 0** caso você envie `offsetPage > 0` quando **hasMore** já for `false`.
Regra prática:

```
Se hasMore = true → incrementa offsetPage
Se hasMore = false → encerra paginação
```

---

## Tela no Sankhya OM

![Imagem 2: Tela no Sankhya OM](https://ajuda.sankhya.com.br/hc/article_attachments/42639654305943)

---

## Boas práticas

- Sempre filtrar por `ATIVO = 'S'`
- Usar unidades alternativas para seleção do usuário antes do cálculo de preço
- Se houver controle, considerar filtrar/validar `productControl`
- Evitar paginação desnecessária (normalmente retorna poucos registros)

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
