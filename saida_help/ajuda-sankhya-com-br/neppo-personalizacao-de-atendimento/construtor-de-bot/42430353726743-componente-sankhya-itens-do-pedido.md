---
id: "42430353726743"
titulo: "Componente Sankhya - Itens do Pedido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430353726743-Componente-Sankhya-Itens-do-Pedido"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T17:13:29Z"
rotulos: ["sync_hc", "neppo", "neppo_857998640", "sync_hash_77da29b3909f"]
---

# Componente Sankhya - Itens do Pedido

O componente **Itens do Pedido** é utilizado para consultar os produtos de um pedido de venda registrado na base Sankhya, retornando informações detalhadas sobre quantidade, preço, controle de estoque, logística e informações comerciais.

bot-server: **versão 1.4.0**

bot-component-service: **versão 1.0.0**

Doc Sankhya: <https://developer.sankhya.com.br/docs/operacoes-comerciais#tgfite>

![Imagem 1: Doc Sankhya: https://developer.sankhya.com.br/docs/operacoes-comerciais#tgfite](https://ajuda.sankhya.com.br/hc/article_attachments/42639617823767)

Permite ações como:

- Apresentar os produtos comprados pelo cliente
- Validar pendências de entrega e conferência
- Apoiar processos de pós-venda, reenvio ou SAC
- Criar automações baseadas em produtos adquiridos

- [Interface do componente (tela)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430353726743-Componente-Sankhya-Itens-do-Pedido#Interface-do-componente-tela)
- [Estrutura do retorno](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430353726743-Componente-Sankhya-Itens-do-Pedido#Estrutura-do-retorno)
- [Mapeamento técnico](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430353726743-Componente-Sankhya-Itens-do-Pedido#Mapeamento-tecnico)
- [Tratamento de erros](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430353726743-Componente-Sankhya-Itens-do-Pedido#Tratamento-de-erros)
- [Boas práticas](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430353726743-Componente-Sankhya-Itens-do-Pedido#Boas-praticas)
- [Segurança](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430353726743-Componente-Sankhya-Itens-do-Pedido#Seguranca)
- [Retorno de erro](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430353726743-Componente-Sankhya-Itens-do-Pedido#Retorno-de-erro)

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

## Interface do componente (tela)

### Parâmetros

| Campo | Descrição |
| --- | --- |
| **Código do pedido**\* (`{{numPedido}}`) | Número único do pedido no Sankhya. Obrigatório para buscar os itens relacionados. |

> Observação: o valor desta variável normalmente vem da consulta anterior no componente de **Obter Pedidos**.

---

### Armazenamento

| Campo | Descrição |
| --- | --- |
| **Variável de armazenamento** | Nome da variável onde o retorno será salvo. Exemplo: `itensPedido` |
| **Variável de escopo global** | Quando ativada, a variável estará disponível em todo o fluxo. Ideal para reutilização em etapas posteriores. |

---

## Estrutura do retorno

### Exemplo de resposta

```
{
  "hasMore": false,
  "size": 1,
  "content": [
    {
      "orderCode": 3721165,
      "sequence": 1,
      "pending": true,
      "unitPrice": 4.7,
      "total": 235,
      "discount": {
        "value": 0,
        "percent": 0
      },
      "company": {
        "code": 1,
        "tradeName": "EMPRESA EXEMPLO"
      },
      "quantities": {
        "ordered": 50,
        "delivered": 0,
        "checked": 0
      },
      "product": {
        "code": 1185,
        "reference": "9XXXX",
        "control": "VARIANTE_EXEMPLO",
        "description": "PRODUTO EXEMPLO",
        "group": {
          "code": 0
        },
        "brand": {
          "code": 242,
          "name": "MARCA EXEMPLO"
        }
      },
      "logistics": {
        "unit": {
          "code": "UN",
          "description": "Unidade"
        },
        "originLocation": {
          "code": 8000,
          "description": "LOCAL EXEMPLO"
        }
      },
      "commercial": {
        "seller": {
          "code": 0,
          "nickname": ""
        },
        "notes": null
      }
    }
  ],
  "error": null
}
```

---

## Mapeamento técnico

| JSON | Campo Sankhya | Tabela |
| --- | --- | --- |
| orderCode | NUNOTA | TGFITE |
| sequence | SEQUENCIA | TGFITE |
| pending | PENDENTE | TGFITE |
| unitPrice | VLRUNIT | TGFITE |
| total | VLRTOT | TGFITE |
| discount.value | VLRDESC | TGFITE |
| discount.percent | PERCDESC | TGFITE |
| company.code | CODEMP | TGFITE |
| company.tradeName | NOMEFANTASIA (via CODEMP) | TSIEMP |
| quantities.ordered | QTDNEG | TGFITE |
| quantities.delivered | QTDENTREGUE | TGFITE |
| quantities.checked | QTDCONFERIDA | TGFITE |
| product.code | CODPROD | TGFITE |
| product.reference | REFERENCIA | TGFPRO |
| product.control | CONTROLE | TGFITE |
| product.description | DESCRPROD | TGFPRO |
| product.group.code | CODGRUPOPROD | TGFPRO |
| product.brand.code | CODMARCA | TGFPRO |
| product.brand.name | MARCA | TGFPRO |
| logistics.unit.code | CODVOL | TGFITE |
| logistics.unit.description | DESCRVOL (via CODVOL) | TGFVOL |
| originLocation.code | CODLOCALORIG | TGFITE |
| originLocation.description | DESCRLOCAL | TGFLOC |
| seller.code | CODVEND | TGFITE |
| seller.nickname | APELIDO | TGFVEN |
| commercial.notes | OBSERVACAO | TGFITE |

---

## Tratamento de erros

| Situação | Comportamento Esperado |
| --- | --- |
| Pedido não existe ou inválido | content = [], ac:local-id="8fa3020a-533e-4751-ba89-a572664b035f"> | Falha na requisição | error preenchido |
| Pedido sem itens | content vazio |

---

## Boas práticas

- Validar o número do pedido antes da chamada
- Iterar sobre `content` para múltiplos itens
- Utilizar escopo global quando itens forem reutilizados em diferentes blocos
- Tratar `pending`, `quantities`, `discounts` e `notes` para controle mais preciso

---

## Segurança

- Requisições autenticadas
- Acesso condicionado às permissões da API
- Utilização segura em fluxos de atendimento e automação

---

## Retorno de erro

**Itens do pedido com número do pedido inválido**
Quando o número do pedido é informado em formato inválido (não numérico), a integração falha na conversão e a API retorna `content` e `size` como `null`, com o objeto `error` detalhando o motivo.

```
{
  "scenario": "Itens do Pedido com número do pedido inválido",
  "input": {
    "orderCode": "aaaaa"
  },
  "response": {
    "hasMore": false,
    "size": null,
    "content": null,
    "error": {
      "code": "SANKHYA_INTEGRATION_FAILED",
      "message": "Erro de conversão para número: aaaaa"
    }
  }
}
```

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
