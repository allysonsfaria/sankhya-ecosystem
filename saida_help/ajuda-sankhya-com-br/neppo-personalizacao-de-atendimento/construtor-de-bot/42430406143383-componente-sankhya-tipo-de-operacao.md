---
id: "42430406143383"
titulo: "Componente Sankhya - Tipo de Operação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430406143383-Componente-Sankhya-Tipo-de-Opera%C3%A7%C3%A3o"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T17:13:25Z"
rotulos: ["sync_hc", "neppo", "neppo_857999110", "sync_hash_7e6e17f8e0e3"]
---

# Componente Sankhya - Tipo de Operação

O componente **Tipo de Operação (TOP)** consulta no Sankhya os **dados de um tipo de operação comercial** (ex.: Orçamento, Pedido de Venda, Nota Fiscal), a partir do **código único da TOP**.

A TOP é um dos pilares do processo comercial no Sankhya, pois define **como a operação se comporta**: tipo de movimento, regras fiscais, integração com NF-e, estoque, financeiro e faturamento.

bot-server: **versão 1.5.0**

bot-component-service: **versão 1.1.0**

Doc Sankhya: <https://developer.sankhya.com.br/docs/operacoes-comerciais#tgftop>

![Imagem 1: Doc Sankhya: https://developer.sankhya.com.br/docs/operacoes-comerciais#tgftop](https://ajuda.sankhya.com.br/hc/article_attachments/42639690719895)

Esse componente é utilizado para:

- Validar se uma TOP é compatível com o fluxo de venda
- Obter metadados da operação antes de criar pedidos
- Direcionar regras de negócio no bot (ex.: orçamento x venda)
- Garantir consistência com a configuração do ERP

- [Objetivo do componente](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430406143383-Componente-Sankhya-Tipo-de-Opera%C3%A7%C3%A3o#Objetivo-do-componente)
- [Contextualização de negócio](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430406143383-Componente-Sankhya-Tipo-de-Opera%C3%A7%C3%A3o#Contextualizacao-de-negocio)
- [Integração técnica](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430406143383-Componente-Sankhya-Tipo-de-Opera%C3%A7%C3%A3o#Integracao-tecnica)
- [Interface do componente (leitura da tela)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430406143383-Componente-Sankhya-Tipo-de-Opera%C3%A7%C3%A3o#Interface-do-componente-leitura-da-tela)
- [Estrutura do retorno (Neppo)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430406143383-Componente-Sankhya-Tipo-de-Opera%C3%A7%C3%A3o#Estrutura-do-retorno-Neppo)
- [Mapeamento técnico dos campos](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430406143383-Componente-Sankhya-Tipo-de-Opera%C3%A7%C3%A3o#Mapeamento-tecnico-dos-campos)
- [Descrição dos campos retornados](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430406143383-Componente-Sankhya-Tipo-de-Opera%C3%A7%C3%A3o#Descricao-dos-campos-retornados)
- [Exemplos de uso no bot](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430406143383-Componente-Sankhya-Tipo-de-Opera%C3%A7%C3%A3o#Exemplos-de-uso-no-bot)
- [Tratamento de erros](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430406143383-Componente-Sankhya-Tipo-de-Opera%C3%A7%C3%A3o#Tratamento-de-erros)
- [Boas práticas](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430406143383-Componente-Sankhya-Tipo-de-Opera%C3%A7%C3%A3o#Boas-praticas)
- [Onde validar no Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430406143383-Componente-Sankhya-Tipo-de-Opera%C3%A7%C3%A3o#Onde-validar-no-Sankhya)

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

Disponibilizar no fluxo do bot as **informações oficiais da TOP configurada no Sankhya**, garantindo que o comportamento do atendimento esteja alinhado ao processo comercial real.

---

## Contextualização de negócio

No Sankhya, a **TOP (Tipo de Operação)** define:

- Se a operação é **pedido, orçamento, devolução, transferência**, etc.
- O **tipo de movimento** (ex.: Pedido, Entrada, Saída)
- A relação com **NF-e**
- Regras fiscais, contábeis e de estoque

As TOPs podem ser visualizadas e mantidas no Sankhya OM na tela:

**Comercial → Tipos de Operação (TOP)**

---

## Integração técnica

A consulta do tipo de operação é feita a partir da tabela:

- `TGFTOP` – Tipos de Operação

A Neppo retorna os dados normalizados no formato de lista (`content`), mesmo quando a consulta é por uma única TOP.

---

## Interface do componente (leitura da tela)

### Configuração de consulta

| Campo | Descrição |
| --- | --- |
| **Código da TOP**\* | Código único do Tipo de Operação no Sankhya (`CODTIPOPER`). Obrigatório. |

> Exemplo: `1001`

---

### Armazenamento

| Campo | Descrição |
| --- | --- |
| **Variável de armazenamento** | Nome da variável onde o resultado será salvo. Ex.: `tipoOperacao` |
| **Variável de escopo global** | Quando ativada, a variável fica disponível em todo o fluxo. |

---

## Estrutura do retorno (Neppo)

### Exemplo de resposta

```
{
  "hasMore": false,
  "size": 1,
  "content": [
    {
      "code": 1,
      "updatedAt": "13/05/2024 17:37:02",
      "description": "ORÇAMENTO",
      "movementType": "P",
      "nfeTypeCode": "M"
    }
  ],
  "error": null
}
```

---

## Mapeamento técnico dos campos

| Campo (JSON) | Descrição | Campo Sankhya | Tabela |
| --- | --- | --- | --- |
| content[n].code | Identificador único da TOP | CODTIPOPER | TGFTOP |
| content[n].updatedAt | Data/hora da última alteração | DHALTER | TGFTOP |
| content[n].description | Descrição da operação | DESCROPER | TGFTOP |
| content[n].movementType | Tipo de movimento | TIPMOV | TGFTOP |
| content[n].nfeTypeCode | Código de NF-e | NFE | TGFTOP |

---

## Descrição dos campos retornados

| Campo | Descrição |
| --- | --- |
| hasMore | Indica se existem mais registros para paginação |
| size | Quantidade de TOPs retornadas |
| content | Lista de tipos de operação |
| content[].code | Código da TOP |
| content[].description | Nome/descrição da operação |
| content[].movementType | Tipo de movimento (ex.: Pedido, Entrada, Saída) |
| content[].nfeTypeCode | Indica relação com NF-e |
| content[].updatedAt | Data da última alteração |
| error | Detalhes do erro quando a consulta falhar |

---

## Exemplos de uso no bot

### Validar tipo de operação antes de criar pedido

```
Se {{tipoOperacao.content[0].movementType}} = "P"
→ Permitir fluxo de pedido/orçamento
```

---

### Exibir tipo de operação aplicado

```
A operação selecionada é: {{tipoOperacao.content[0].description}}
```

---

## Tratamento de erros

| Situação | Comportamento |
| --- | --- |
| Código de TOP inexistente | `size = 0`, `content = []` |
| TOP inativa ou inválida | `found implícito = false` |
| Falha na API | `error` preenchido |

Iremos disponibilizar exemplos de erro em breve.

---

## Boas práticas

- Sempre valide a TOP antes de criar pedidos
- Use TOP coerente com o tipo de venda (orçamento x venda)
- Centralize a definição da TOP via preferência quando aplicável
- Utilize escopo global quando a TOP for reutilizada no fluxo

---

## Onde validar no Sankhya

No ERP Sankhya OM:

- **Comercial → Tipos de Operação (TOP)**

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
