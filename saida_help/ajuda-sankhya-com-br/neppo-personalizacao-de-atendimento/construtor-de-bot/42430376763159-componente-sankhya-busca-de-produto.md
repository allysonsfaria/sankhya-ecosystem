---
id: "42430376763159"
titulo: "Componente Sankhya - Busca de Produto"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430376763159-Componente-Sankhya-Busca-de-Produto"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T17:13:23Z"
rotulos: ["sync_hc", "neppo", "neppo_857999276", "sync_hash_46e474f112c5"]
---

# Componente Sankhya - Busca de Produto

O componente **Busca de Produto** permite localizar produtos cadastrados no **ERP Sankhya** a partir de um **termo de busca**, retornando uma lista de produtos correspondentes.

A busca pode ocorrer de duas formas:

**Busca direta no Sankhya (padrão)**

**Busca indexada (Elastic / IAN)** para melhorar relevância e tolerância a erros de digitação.

Esse componente normalmente é o **ponto inicial da jornada de venda digital**, permitindo ao usuário pesquisar produtos pelo nome, referência ou descrição.

bot-server: **versão 1.7.0**

bot-component-service: **versão 1.3.0**

![Imagem 1: bot-component-service: versão 1.3.0](https://ajuda.sankhya.com.br/hc/article_attachments/42639697308311)

Índice:

- [Objetivo do componente](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430376763159-Componente-Sankhya-Busca-de-Produto#Objetivo-do-componente)
- [Interface do componente (leitura da tela)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430376763159-Componente-Sankhya-Busca-de-Produto#Interface-do-componente-leitura-da-tela)
- [Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430376763159-Componente-Sankhya-Busca-de-Produto#Armazenamento)
- [Estrutura do retorno (busca direta no sankhya)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430376763159-Componente-Sankhya-Busca-de-Produto#Estrutura-do-retorno-busca-direta-no-sankhya)
- [Estrutura do retorno (busca indexada)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430376763159-Componente-Sankhya-Busca-de-Produto#Estrutura-do-retorno-busca-indexada)
- [Estrutura do retorno (erro)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430376763159-Componente-Sankhya-Busca-de-Produto#Estrutura-do-retorno-erro)
- [Descrição dos campos retornados](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430376763159-Componente-Sankhya-Busca-de-Produto#Descricao-dos-campos-retornados)
- [Comportamento da busca](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430376763159-Componente-Sankhya-Busca-de-Produto#Comportamento-da-busca)
- [Integração técnica](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430376763159-Componente-Sankhya-Busca-de-Produto#Integracao-tecnica)
- [Exemplos de uso no bot](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430376763159-Componente-Sankhya-Busca-de-Produto#Exemplos-de-uso-no-bot)
- [Tratamento de erros](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430376763159-Componente-Sankhya-Busca-de-Produto#Tratamento-de-erros)
- [Boas práticas](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430376763159-Componente-Sankhya-Busca-de-Produto#Boas-praticas)

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

Permitir que o bot encontre produtos no Sankhya utilizando **busca textual**, retornando opções para que o usuário escolha o item desejado.

---

## Interface do componente (leitura da tela)

## Busca de produto

**Configuração dos parâmetros de busca**

| Campo | Descrição |
| --- | --- |
| **Termo de busca**\* | Texto utilizado para localizar produtos |
| **Habilitar busca indexada** | Ativa busca inteligente via índice (Elastic / IAN) |

---

### Termo de busca

Campo utilizado para localizar produtos por:

- nome
- descrição
- referência
- código

Exemplo:

```
bala
```

ou utilizando variável do fluxo:

```
{{nomeProduto}}
```

---

### Habilitar busca indexada

Quando ativado:

- utiliza um **índice de busca (Elastic)**
- permite **busca por aproximação**
- tolera **erros de digitação**
- retorna resultados **ordenados por relevância**

Exemplo:

```
bala
```

retorna:

- BALAS SORTIDAS
- BALA DE MORANGO
- BALA DE UVA

---

### Aviso importante

> A busca indexada utiliza dados de índice, que podem ter uma defasagem de até **24 horas** em relação às atualizações de cadastro ou estoque no Sankhya.

---

## Armazenamento

| Campo | Descrição |
| --- | --- |
| **Variável de armazenamento** | Nome da variável que receberá o resultado da busca |
| **Variável de escopo global** | Permite acessar os dados em qualquer fluxo |

Exemplo:

```
produtosEncontrados
```

---

## Estrutura do retorno (busca direta no sankhya)

### Exemplo

```
{
  "hasMore": false,
  "size": 1,
  "content": [
    {
      "code": 1185,
      "description": "BALAS SORTIDAS",
      "score": null
    }
  ],
  "extra": {
    "source": "sankhya",
    "indexed": false
  },
  "error": null
}
```

---

## Estrutura do retorno (busca indexada)

```
{
  "hasMore": false,
  "size": 3,
  "content": [
    {
      "code": 73,
      "description": "MACA GALA",
      "score": 4.4879365
    },
    {
      "code": 1185,
      "description": "BALAS SORTIDAS",
      "score": 4.379388
    }
  ],
  "extra": {
    "source": "ian",
    "indexed": true
  },
  "error": null
}
```

---

## Estrutura do retorno (erro)

```
{
  "hasMore": false,
  "size": null,
  "content": null,
  "extra": {},
  "error": {
    "code": "SEARCH_TERM_IS_NULL_OR_EMPTY",
    "message": "Search term is required. Provide a non-empty 'text' argument."
  }
}
```

---

## Descrição dos campos retornados

| Campo | Descrição |
| --- | --- |
| **hasMore** | Indica se existem mais registros para paginação |
| **size** | Quantidade de produtos retornados |
| **content[]** | Lista de produtos encontrados |
| **content[].code** | Código do produto |
| **content[].description** | Nome ou descrição do produto |
| **content[].score** | Pontuação de relevância (apenas busca indexada) |
| **extra.source** | Origem da busca (`sankhya` ou `ian`) |
| **extra.indexed** | Indica se a busca veio do índice |
| **extra.fallbackReason** | Motivo do fallback para Sankhya (quando aplicável) |
| **error** | Erro retornado pela ação |

---

## Comportamento da busca

### Quando use\_indexed\_search = true

Fluxo de execução:

```
Busca Indexada (Elastic / IAN)
       ↓
Se retornar resultados → retorna
       ↓
Se índice indisponível ou 0 resultados
       ↓
Fallback automático
       ↓
Busca direta no Sankhya
```

---

## Integração técnica

## Busca direta no sankhya

Serviço utilizado:

```
ConsultaProdutosSP.consultaProdutos
```

### Exemplo de requisição

```
curl --location 'https://api.sankhya.com.br/gateway/v1/mgecom/service.sbr?serviceName=ConsultaProdutosSP.consultaProdutos&outputType=json'
--header 'Authorization: Bearer {{accessToken}}'
--header 'Content-Type: application/json'
--data '{
"serviceName": "ConsultaProdutosSP.consultaProdutos",
"requestBody": {
"filtros": {
"criterio": {
"resourceID": "br.com.sankhya.com.cons.consultaProdutos",
"PERCDESC": "0",
"VALOR": { "$": "bala" }
},
"isPromocao": { "$": "false" },
"isLiquidacao": { "$": "false" }
}
}
}'
```

---

## Busca indexada (IAN / Elastic)

Endpoint utilizado:

```
index_search
```

### Exemplo de requisição

```
curl --location 'https://hml-api.neppo.com.br/qatransformersapi/0.0.1/index_search'
--header 'accept: application/json'
--header 'Content-Type: application/json'
--header 'apikey: <token>'
--data '{
"index": "qa_digital_sales_sankhya_products_data_pt",
"item": "bala",
"size": 50,
"page": 1
}'
```

---

## Exemplos de uso no bot

### Mostrar lista de produtos encontrados

```
Encontramos estes produtos:

{{produtosEncontrados.content[0].description}}
{{produtosEncontrados.content[1].description}}
```

---

### Selecionar produto para consulta

```
Código do produto selecionado:

{{produtosEncontrados.content[0].code}}
```

Esse valor pode ser usado em:

- **Detalhe do produto**
- **Estoque do produto**
- **Preço do produto**

---

## Tratamento de erros

| Situação | Comportamento |
| --- | --- |
| Termo vazio | erro `SEARCH_TERM_IS_NULL_OR_EMPTY` |
| Produto não encontrado | `size = 0` |
| Falha na busca indexada | fallback automático para Sankhya |

---

## Boas práticas

- Utilizar **busca indexada para catálogos grandes**
- Validar `size > 0` antes de prosseguir
- Limitar número de resultados exibidos ao usuário
- Utilizar **score** para ordenar produtos por relevância

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
