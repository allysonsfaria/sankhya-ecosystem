---
id: "42430354191767"
titulo: "Componente Sankhya - Criar Pedido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430354191767-Componente-Sankhya-Criar-Pedido"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T17:13:28Z"
rotulos: ["sync_hc", "neppo", "neppo_857998696", "sync_hash_421438e4a072"]
---

# Componente Sankhya - Criar Pedido

O componente **Criar Pedido** é responsável por registrar um **pedido de venda no ERP Sankhya** diretamente a partir do fluxo do bot construído na plataforma Neppo.

Ele utiliza as informações coletadas ao longo da jornada de venda, como cliente, tipo de operação, tipo de negociação e itens do carrinho, para criar a movimentação comercial no Sankhya.

Após a execução, o pedido é criado no ERP e pode ser consultado na tela **Portal de Vendas**, utilizando o **Número Único do Pedido (NUNOTA)** retornado pela operação.

bot-server: **versão 1.7.0**

bot-component-service: **versão 1.3.0**

Serviço da Sankhya usado para criação do pedido: <https://developer.sankhya.com.br/reference/post_incluimovimentos>

<https://developer.sankhya.com.br/reference/post_incluimovimentos>

![Imagem 1: https://developer.sankhya.com.br/reference/post_incluimovimentos](https://ajuda.sankhya.com.br/hc/article_attachments/42639603953175)

Índice:

- [Interface do componente (leitura da tela)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430354191767-Componente-Sankhya-Criar-Pedido#Interface-do-componente-leitura-da-tela)
- [Itens do pedido](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430354191767-Componente-Sankhya-Criar-Pedido#Itens-do-pedido)
- [Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430354191767-Componente-Sankhya-Criar-Pedido#Armazenamento)
- [Integração técnica](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430354191767-Componente-Sankhya-Criar-Pedido#Integracao-tecnica)
- [Estrutura do retorno](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430354191767-Componente-Sankhya-Criar-Pedido#Estrutura-do-retorno)
- [Descrição dos campos retornados](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430354191767-Componente-Sankhya-Criar-Pedido#Descricao-dos-campos-retornados)
- [Onde visualizar o pedido no Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430354191767-Componente-Sankhya-Criar-Pedido#Onde-visualizar-o-pedido-no-Sankhya)
- [Exemplos de uso no bot](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430354191767-Componente-Sankhya-Criar-Pedido#Exemplos-de-uso-no-bot)
- [Tratamento de erros](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430354191767-Componente-Sankhya-Criar-Pedido#Tratamento-de-erros)
- [Boas práticas](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430354191767-Componente-Sankhya-Criar-Pedido#Boas-praticas)

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

Automatizar a criação de pedidos no Sankhya garantindo que:

- As regras comerciais do ERP sejam respeitadas
- Os dados financeiros e fiscais estejam corretos
- O fluxo digital reproduza o mesmo comportamento de uma venda realizada manualmente no sistema

---

## Interface do componente (leitura da tela)

## Cabeçalho da nota

**Informações principais do pedido**

| Campo | Descrição | Origem Sankhya |
| --- | --- | --- |
| **Parceiro**\* | Código do cliente ou fornecedor no Sankhya | `TGFPAR.CODPARC` |
| **Empresa**\* | Código da empresa responsável pela venda | `TGFCAB.CODEMP` |
| **Centro de Custo**\* | Centro de resultado da venda | `TGFCAB.CODCENCUS` |
| **Projeto**\* | Código do projeto vinculado ao pedido | `TGFCAB.CODPROJ` |
| **Natureza**\* | Natureza da operação financeira | `TGFCAB.CODNAT` |
| **Vendedor Preferencial**\* | Código do vendedor responsável | `TGFCAB.CODVEND` |
| **Tipo de Operação (TOP)**\* | Tipo de operação comercial do pedido | `TGFCAB.CODTIPOPER` |
| **Tipo de Venda**\* | Tipo de negociação (forma de pagamento) | `TGFCAB.CODTIPVENDA` |

### Observação

Alguns desses campos normalmente são obtidos dinamicamente a partir de consultas anteriores no fluxo, como:

- **Dados do cliente**
- **Tipos de negociação**
- **Tipo de operação**
- **Preferências**
- **Tabela de preço**

---

## Itens do pedido

Os **itens do pedido** não são informados diretamente nesse componente.

Na jornada de **Venda Digital**, os itens são obtidos automaticamente a partir do **carrinho de compras do bot**, que deve estar estruturado previamente no fluxo.

⚠️ **Alerta exibido na interface**

> Para a jornada de venda digital com Sankhya, serão utilizados os itens do carrinho para a criação do pedido.
> Verifique a estrutura do fluxo antes da publicação.

Cada item do carrinho será transformado em um registro na tabela:

**TGFITE – Itens da nota**

---

## Armazenamento

| Campo | Descrição |
| --- | --- |
| **Variável de armazenamento** | Nome da variável que receberá o retorno da criação do pedido. Exemplo: `pedidoCriado` |
| **Variável de escopo global** | Quando ativada, permite acessar o pedido criado em qualquer ponto do fluxo |

---

## Integração técnica

A criação do pedido utiliza o serviço Sankhya:

```
POST incluimovimentos
```

Documentação oficial:

<https://developer.sankhya.com.br/reference/post_incluimovimentos>

Esse serviço cria a movimentação comercial nas tabelas:

| Tabela | Descrição |
| --- | --- |
| **TGFCAB** | Cabeçalho do pedido |
| **TGFITE** | Itens do pedido |

---

## Estrutura do retorno

### Exemplo de resposta

```
{
  "orderCode": 3723169,
  "items": [
    {
      "product": {
        "code": 1185,
        "referenceCode": 91185,
        "defaultUnit": {
          "code": "UN",
          "description": "Unidade"
        },
        "description": "BALAS SORTIDAS",
        "complementaryDescription": null,
        "characteristics": null,
        "brand": "ERLAN"
      },
      "quantity": 5,
      "locationCode": 0,
      "unitCode": "UN",
      "controlCode": "MACA VERDE",
      "price": 4.3
    }
  ],
  "error": null
}
```

---

## Descrição dos campos retornados

| Campo | Descrição |
| --- | --- |
| **orderCode** | Número único do pedido criado (NUNOTA) |
| **items** | Lista de itens registrados no pedido |
| **items[].product.code** | Código do produto |
| **items[].product.description** | Descrição do produto |
| **items[].quantity** | Quantidade do item |
| **items[].unitCode** | Unidade de venda |
| **items[].controlCode** | Controle do produto (variação) |
| **items[].price** | Preço unitário aplicado |
| **error** | Informações de erro quando a criação falhar |

---

## Onde visualizar o pedido no Sankhya

Após a criação, o pedido pode ser visualizado na tela:

**Portal de vendas**

Para localizar o pedido:

1. Acesse **portal de vendas**
2. Utilize o filtro **número único**
3. Informe o valor retornado em **orderCode**

![Imagem 2: Informe o valor retornado em orderCode](https://ajuda.sankhya.com.br/hc/article_attachments/42639604354199)![Imagem 3: Informe o valor retornado em orderCode](https://ajuda.sankhya.com.br/hc/article_attachments/42639650583063)

---

## Exemplos de uso no bot

### Confirmar criação do pedido

```
Seu pedido foi criado com sucesso!

Número do pedido: {{pedidoCriado.orderCode}}
```

---

### Mostrar resumo do pedido

```
Pedido {{pedidoCriado.orderCode}} criado com sucesso.
Itens adicionados ao pedido:
{{pedidoCriado.items[0].product.description}}
```

---

## Tratamento de erros

| Situação | Comportamento |
| --- | --- |
| Cliente inválido | erro retornado pelo serviço |
| Produto inexistente | erro na inclusão dos itens |
| TOP incompatível | erro na validação da operação |
| Preço inválido | erro na criação da movimentação |

---

## Boas práticas

- Validar os dados do cliente antes de criar o pedido
- Garantir que o carrinho esteja estruturado corretamente
- Validar preço e tabela de preço antes da criação
- Utilizar TOP compatível com vendas digitais

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
