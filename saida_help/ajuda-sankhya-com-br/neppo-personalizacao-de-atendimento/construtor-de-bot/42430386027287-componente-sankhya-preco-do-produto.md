---
id: "42430386027287"
titulo: "Componente Sankhya - Preço do Produto"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430386027287-Componente-Sankhya-Pre%C3%A7o-do-Produto"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T17:13:28Z"
rotulos: ["sync_hc", "neppo", "neppo_857998762", "sync_hash_d81c6eaf8fb5"]
---

# Componente Sankhya - Preço do Produto

O componente **preço do produto** permite consultar o **preço final de um produto** diretamente no ERP Sankhya, considerando todas as regras comerciais configuradas no ambiente, como tabela de preços, parceiro, tipo de negociação, unidade, controle do produto e tipo de operação.

bot-server: **versão 1.6.0**

bot-component-service: **1.2.0**

Doc Sankhya: <https://developer.sankhya.com.br/docs/operacoes-comerciais>

[GIF animado: Imagem 1: Doc Sankhya: https://developer.sankhya.com.br/docs/operacoes-comerciais](https://ajuda.sankhya.com.br/hc/article_attachments/42639651620631)

Esse componente é essencial para:

- Exibir preços corretos no atendimento via bot
- Simular valores antes da criação do pedido
- Aplicar regras comerciais reais da Sankhya
- Evitar divergência entre preço exibido e preço faturado

Índice:

- [Objetivo do componente](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430386027287-Componente-Sankhya-Pre%C3%A7o-do-Produto#Objetivo-do-componente)
- [Integração técnica](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430386027287-Componente-Sankhya-Pre%C3%A7o-do-Produto#Integracao-tecnica)
- [Interface do componente (tela)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430386027287-Componente-Sankhya-Pre%C3%A7o-do-Produto#Interface-do-componente-tela)
- [Estrutura do retorno](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430386027287-Componente-Sankhya-Pre%C3%A7o-do-Produto#Estrutura-do-retorno)
- [Descrição dos campos retornados](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430386027287-Componente-Sankhya-Pre%C3%A7o-do-Produto#Descricao-dos-campos-retornados)
- [Contextualização de negócio (Importante)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430386027287-Componente-Sankhya-Pre%C3%A7o-do-Produto#Contextualizacao-de-negocio-Importante)
- [Exemplo de chamada ao serviço da Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430386027287-Componente-Sankhya-Pre%C3%A7o-do-Produto#Exemplo-de-chamada-ao-servico-da-Sankhya)
- [Exemplos de uso no bot](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430386027287-Componente-Sankhya-Pre%C3%A7o-do-Produto#Exemplos-de-uso-no-bot)
- [Tratamento de erros](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430386027287-Componente-Sankhya-Pre%C3%A7o-do-Produto#Tratamento-de-erros)

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

Garantir que o preço apresentado ao cliente no fluxo conversacional seja **exatamente o mesmo** que o ERP Sankhya calcularia em um cenário real de venda, respeitando todas as variáveis de negócio.

---

## Integração técnica

A consulta de preço utiliza o serviço Sankhya:

```
CentralVendaRapidaSP.consultarDetalhesPreco
```

Esse serviço executa o **motor de precificação da Sankhya**, retornando o valor final do produto com base nos parâmetros informados.

---

## Interface do componente (tela)

### Dados do produto

| Campo | Descrição |
| --- | --- |
| **Código do Produto**\* | Código único do produto no Sankhya (`CODPROD`). Obrigatório. |
| **Volume (opcional)** | Unidade de medida do produto (`CODVOL`). Ex: UN, CX, KG. |
| **Local de Estoque (opcional)** | Código do local de estoque (`CODLOCAL`). |
| **Controle (opcional)** | Controle do produto (variação). Ex: sabor, cor, tamanho. |

> 🔎 O campo **Controle** é essencial para produtos com variações configuradas na Sankhya.

---

### Contexto de negócio

| Campo | Descrição |
| --- | --- |
| **Tabela de preço (opcional)** | Código ou número da tabela de preços (`NUTAB`). |
| **Parceiro (opcional)** | Código do cliente ou fornecedor (`CODPARC`). |
| **Empresa (opcional)** | Código da empresa (`CODEMP`). |
| **Tipo de Negociação (opcional)** | Forma de pagamento (`CODTIPVENDA`). |
| **Código da TOP (opcional)** | Tipo de operação (`CODTIPOPER`). |

> Quanto mais campos preenchidos, **mais preciso será o preço retornado**.

---

### Armazenamento

| Campo | Descrição |
| --- | --- |
| **Variável de armazenamento** | Nome da variável que receberá o retorno do preço. |
| **Variável de escopo global** | Permite reutilizar o preço em todo o fluxo do bot. |

Exemplo:

```
precoProduto
```

---

## Estrutura do retorno

### Exemplo de resposta

```
{
    "found": true,
    "data": {
        "value": 6,
        "baseValue": 6,
        "promoValue": 0,
        "priceTableCode": 999,
        "priceTableNumber": 609,
        "priceTableName": "TABELA PADRÃO",
        "description": "Preço"
    },
    "error": null
}
```

---

## Descrição dos campos retornados

| Campo | Descrição |
| --- | --- |
| found | Indica se o preço foi encontrado |
| data.value | Preço final calculado |
| data.baseValue | Preço base |
| data.promoValue | Preço promocional |
| data.priceTableCode | Código da tabela de preço |
| data.priceTableNumber | Número da tabela de preço |
| data.priceTableName | Nome da tabela de preço |
| data.description | Descrição do retorno |
| error | Mensagem de erro, se houver |

---

## Contextualização de negócio (Importante)

O preço retornado **não é um valor fixo**, mas o resultado de um **cálculo dinâmico** baseado nas regras da Sankhya.

O valor pode variar conforme:

- **Tabela de preço**
- **Unidade (volume)**
- **Local de estoque**
- **Tipo de negociação (forma de pagamento)**
- **Parceiro**
- **Empresa**
- **Controle do produto** (sabor, cor, tamanho, etc.)
- **Tipo de operação (TOP)**

---

### Exemplo prático de controle de produto

No ambiente Sankhya, o produto **Balas Sortidas** possui **controle por sabor**, como:

- MAÇÃ VERDE
- UVA
- MORANGO

Na **Tabela Padrão**, existem regras de preço específicas por controle.
Isso significa que:

- O preço pode variar de acordo com o sabor
- Informar corretamente o campo **Controle** é essencial

Ao consultar o preço informando `CONTROLE = MORANGO`, o valor retornado será calculado com base **nas regras específicas desse sabor**.

---

## Exemplo de chamada ao serviço da Sankhya

```
curl --location 'https://api.sankhya.com.br/gateway/v1/mgecom/service.sbr?serviceName=CentralVendaRapidaSP.consultarDetalhesPreco&outputType=json' \
--header 'Authorization: Bearer <TOKEN>' \
--header 'appkey: <APPKEY>' \
--header 'Content-Type: application/json' \
--data '{
    "serviceName": "CentralVendaRapidaSP.consultarDetalhesPreco",
    "requestBody": {
        "criterio": {
            "RESOURCEID": "br.com.sankhya.mgecom.VendaAssistida.DetalhesPrecoLayout",
            "CODPROD": "1185",
            "CODLOCAL": "0",
            "QTDNEG": 1,
            "CONTROLE": "MORANGO",
            "CODVOL": "UN",
            "CODPARC": "654",
            "CODTIPOPER": "50",
            "CODTIPVENDA": "1",
            "CODEMP": "0",
            "NUTAB": "609",
            "MANDARVOLUMES": false,
            "MANDARLOCAIS": false
        }
    }
}'
```

---

## Exemplos de uso no bot

### Exibir preço ao cliente

```
O valor do produto é R$ {{precoProduto.data.value}}.
```

---

### Verificar preço promocional

```
Se {{precoProduto.data.promoValue}} > 0
→ Exibir preço promocional
Senão
→ Exibir preço base
```

---

## Tratamento de erros

| Situação | Comportamento |
| --- | --- |
| Produto não encontrado | found = false |
| Parâmetros inválidos | error preenchido |
| Regra inexistente | valor retornado pode ser 0 |

Iremos disponibilizar exemplos de erro em breve.

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
