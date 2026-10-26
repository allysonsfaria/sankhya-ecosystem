---
id: "42430364291351"
titulo: "Componente Sankhya - Tipos de Negociação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430364291351-Componente-Sankhya-Tipos-de-Negocia%C3%A7%C3%A3o"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T17:13:24Z"
rotulos: ["sync_hc", "neppo", "neppo_857999166", "sync_hash_a6e44a319816"]
---

# Componente Sankhya - Tipos de Negociação

O componente **Tipos de Negociação** consulta no Sankhya os **tipos de negociação disponíveis** (formas comerciais de pagamento/venda), como:

- À vista
- Boleto
- Boleto parcelado
- Cartão de crédito
- Outras modalidades configuradas no ERP

bot-server: **versão 1.5.0**

bot-component-service: **versão 1.1.0**

Doc Sankhya: <https://developer.sankhya.com.br/docs/operacoes-comerciais#tgftpv>

![Imagem 1: Doc Sankhya: https://developer.sankhya.com.br/docs/operacoes-comerciais#tgftpv](https://ajuda.sankhya.com.br/hc/article_attachments/42639680980631)

Esses tipos determinam **condições comerciais críticas**, como juros, descontos permitidos, prazos, parcelas e regras de autorização.

índice:

- [Objetivo do componente](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430364291351-Componente-Sankhya-Tipos-de-Negocia%C3%A7%C3%A3o#Objetivo-do-componente)
- [Contextualização de negócio](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430364291351-Componente-Sankhya-Tipos-de-Negocia%C3%A7%C3%A3o#Contextualizacao-de-negocio)
- [Integração técnica](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430364291351-Componente-Sankhya-Tipos-de-Negocia%C3%A7%C3%A3o#Integracao-tecnica)
- [Interface do componente (leitura da tela)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430364291351-Componente-Sankhya-Tipos-de-Negocia%C3%A7%C3%A3o#Interface-do-componente-leitura-da-tela)
- [Estrutura do retorno (Neppo)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430364291351-Componente-Sankhya-Tipos-de-Negocia%C3%A7%C3%A3o#Estrutura-do-retorno-Neppo)
- [Mapeamento técnico dos campos](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430364291351-Componente-Sankhya-Tipos-de-Negocia%C3%A7%C3%A3o#Mapeamento-tecnico-dos-campos)
- [Descrição dos campos retornados](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430364291351-Componente-Sankhya-Tipos-de-Negocia%C3%A7%C3%A3o#Descricao-dos-campos-retornados)
- [Exemplos de uso no bot](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430364291351-Componente-Sankhya-Tipos-de-Negocia%C3%A7%C3%A3o#Exemplos-de-uso-no-bot)
- [Tratamento de erros](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430364291351-Componente-Sankhya-Tipos-de-Negocia%C3%A7%C3%A3o#Tratamento-de-erros)
- [Boas práticas](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430364291351-Componente-Sankhya-Tipos-de-Negocia%C3%A7%C3%A3o#Boas-praticas)
- [Onde validar no Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430364291351-Componente-Sankhya-Tipos-de-Negocia%C3%A7%C3%A3o#Onde-validar-no-Sankhya)

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

Disponibilizar no fluxo do bot a **lista de tipos de negociação válidos**, permitindo:

- Apresentar opções corretas ao cliente
- Direcionar regras de preço, juros e desconto
- Garantir consistência entre bot, pedido e faturamento
- Evitar seleção de tipos inativos ou inválidos

---

## Contextualização de negócio

No Sankhya, o **Tipo de Negociação** define:

- Forma de pagamento
- Condições financeiras (juros, descontos, prazos)
- Limites de valor mínimo/máximo
- Necessidade de autorização
- Quantidade de parcelas

Esses tipos são mantidos no Sankhya OM na tela:

**Comercial → Tipos de Negociação**

---

## Integração técnica

A consulta é baseada na entidade:

- `TGFTPV` – Tipos de Negociação

A Neppo retorna os registros de forma paginada, permitindo filtrar apenas os tipos **ativos** e controlar a listagem.

---

## Interface do componente (leitura da tela)

### Configuração de filtro

| Campo | Descrição |
| --- | --- |
| **Listar apenas ativos?** | Quando ativado, retorna somente tipos de negociação com status ativo no Sankhya (`ATIVO = S`). |
| **Continuar listagem (opcional)** | Controle de paginação. • `0` → lista inicial (até 50 registros) • `1` → próximos 50 • `2`, `3`… para continuar |

> ⚠️ Recomenda-se utilizar paginação apenas quando `hasMore = true` no retorno.

---

### Armazenamento

| Campo | Descrição |
| --- | --- |
| **Variável de armazenamento** | Nome da variável que receberá a lista. Ex.: `tiposNegociacao` |
| **Variável de escopo global** | Torna os tipos de negociação acessíveis em todo o fluxo. |

---

## Estrutura do retorno (Neppo)

### Exemplo de resposta

```
{
  "hasMore": false,
  "size": 7,
  "content": [
    {
      "code": 35,
      "updatedAt": "26/06/2019 14:39:49",
      "description": "BOLETO PARCELADO- 30/60/90",
      "subType": "3",
      "minSale": 0,
      "maxSale": 0,
      "interestRate": 3,
      "maxDiscount": null,
      "promoDiscount": true,
      "minTerm": null,
      "active": true,
      "feeType": "E",
      "interestType": "I",
      "authGroup": null,
      "installments": 0,
      "simulatedInterestRate": null,
      "simulatedInterestType": null,
      "firstInstallmentRounding": null
    }
  ],
  "error": null
}
```

---

## Mapeamento técnico dos campos

| Campo (JSON) | Descrição | Campo Sankhya | Tabela |
| --- | --- | --- | --- |
| content[n].code | Identificador único | CODTIPVENDA | TGFTPV |
| content[n].updatedAt | Data de alteração | DHALTER | TGFTPV |
| content[n].description | Descrição | DESCRTIPVENDA | TGFTPV |
| content[n].subType | Código do subtipo | SUBTIPOVENDA | TGFTPV |
| content[n].minSale | Valor mínimo de venda | VENDAMIN | TGFTPV |
| content[n].maxSale | Valor máximo de venda | VENDAMAX | TGFTPV |
| content[n].interestRate | Taxa de juros | TAXAJURO | TGFTPV |
| content[n].maxDiscount | Desconto máximo permitido | DESCMAX | TGFTPV |
| content[n].promoDiscount | Flag de desconto promocional | DESCPROM | TGFTPV |
| content[n].minTerm | Prazo mínimo | PRAZOMIN | TGFTPV |
| content[n].active | Status | ATIVO | TGFTPV |
| content[n].feeType | Tipo de taxa | TIPTAXA | TGFTPV |
| content[n].interestType | Tipo de juros | TIPJURO | TGFTPV |
| content[n].authGroup | Grupo de autorização | GRUPOAUTOR | TGFTPV |
| content[n].installments | Número de parcelas | NROPARCELAS | TGFTPV |
| content[n].simulatedInterestRate | Juros simulados | TAXAJURSIM | TGFTPV |
| content[n].simulatedInterestType | Tipo de juros simulado | TIPOJURSIM | TGFTPV |
| content[n].firstInstallmentRounding | Arredondamento 1ª parcela | ARREDPRIMEIRAPARC | TGFTPV |

---

## Descrição dos campos retornados

| Campo | Descrição |
| --- | --- |
| hasMore | Indica se existem mais tipos para paginação |
| size | Quantidade total retornada |
| content | Lista de tipos de negociação |
| content[].active | Indica se o tipo está ativo |
| content[].interestRate | Juros aplicáveis |
| content[].minSale / maxSale | Limites de valor |
| error | Detalhes do erro quando ocorrer falha |

---

## Exemplos de uso no bot

### Listar opções para o cliente

```
Escolha a forma de pagamento:
1️⃣ {{tiposNegociacao.content[0].description}}
2️⃣ {{tiposNegociacao.content[1].description}}
```

---

### Validar se o tipo exige autorização

```
Se {{tipo.authGroup}} ≠ null
→ Solicitar aprovação
```

---

### Aplicar regras de juros

```
Juros aplicáveis: {{tipo.interestRate}}%
```

---

## Tratamento de erros

| Situação | Comportamento |
| --- | --- |
| Nenhum tipo ativo | `size = 0`, `content = []` |
| Página inválida | Retorno repetido da página 0 |
| Falha na API | Campo `error` preenchido |

Iremos disponibilizar exemplos de erro em breve.

---

## Boas práticas

- Ativar **listar apenas ativos** para fluxos comerciais
- Validar limites `minSale` e `maxSale` antes de confirmar pedido
- Usar `authGroup` para fluxos que exigem aprovação
- Tratar paginação com base em `hasMore`
- Evitar hardcode de tipos no fluxo

---

## Onde validar no Sankhya

No ERP Sankhya OM:

- **Comercial → Tipos de Negociação**

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
