---
id: "42430349855127"
titulo: "Componente Sankhya - Obter Preferência"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430349855127-Componente-Sankhya-Obter-Prefer%C3%AAncia"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T17:13:26Z"
rotulos: ["sync_hc", "neppo", "neppo_857998987", "sync_hash_f4b3417fa5af"]
---

# Componente Sankhya - Obter Preferência

O componente **Obter Preferência** consulta uma **preferência/parâmetro configurado no Sankhya** a partir de uma **Chave da Preferência** (ex.: `MODPEDVENDIGITA`, `TIPTABPRECOS`).
Ele retorna metadados completos do parâmetro (grupo, aba, usuário, tipo, lista de opções) e, quando existir, o valor “cru” e o valor interpretado.

bot-server: **versão 1.5.0**

bot-component-service: **versão 1.1.0**

![Imagem 1: bot-component-service: versão 1.1.0](https://ajuda.sankhya.com.br/hc/article_attachments/42639659628567)

Use esse componente quando você precisa:

- Ler configurações do ERP para dirigir o comportamento do bot
- Buscar “defaults” do negócio (modelo de pedido, tabela padrão, TOP, etc.)
- Transformar listas do Sankhya (ex.: `1=484`) em opções estruturadas
- Evitar hardcode de parâmetros dentro do fluxo

Índice:

- [Objetivo do componente](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430349855127-Componente-Sankhya-Obter-Prefer%C3%AAncia#Objetivo-do-componente)
- [Integração técnica](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430349855127-Componente-Sankhya-Obter-Prefer%C3%AAncia#Integracao-tecnica)
- [Interface do componente (tela)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430349855127-Componente-Sankhya-Obter-Prefer%C3%AAncia#Interface-do-componente-tela)
- [Estrutura do retorno (neppo)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430349855127-Componente-Sankhya-Obter-Prefer%C3%AAncia#Estrutura-do-retorno-neppo)
- [Retorno original da API Sankhya (referência)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430349855127-Componente-Sankhya-Obter-Prefer%C3%AAncia#Retorno-original-da-API-Sankhya-referencia)
- [Como os campos “saem” do Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430349855127-Componente-Sankhya-Obter-Prefer%C3%AAncia#Como-os-campos-saem-do-Sankhya)
- [De/Para — Neppo (data) ← Sankhya (API)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430349855127-Componente-Sankhya-Obter-Prefer%C3%AAncia#DePara--Neppo-data--Sankhya-API)
- [Descrição dos campos retornados (Neppo)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430349855127-Componente-Sankhya-Obter-Prefer%C3%AAncia#Descricao-dos-campos-retornados-Neppo)
- [Exemplos de uso no bot](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430349855127-Componente-Sankhya-Obter-Prefer%C3%AAncia#Exemplos-de-uso-no-bot)
- [Tratamento de erros](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430349855127-Componente-Sankhya-Obter-Prefer%C3%AAncia#Tratamento-de-erros)
- [Tela no Sankhya OM](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430349855127-Componente-Sankhya-Obter-Prefer%C3%AAncia#Tela-no-Sankhya-OM)
- [Boas práticas](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430349855127-Componente-Sankhya-Obter-Prefer%C3%AAncia#Boas-praticas)

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

Permitir que o fluxo do bot seja **guiado pelas regras e preferências reais do Sankhya**, garantindo governança e consistência com o ERP.

---

## Integração técnica

A consulta é realizada via serviço Sankhya:

- `ManutencaoPreferenciasSP.getParametrosComoEstrutura`

Esse serviço retorna a preferência como uma **árvore (tree)** dentro de `responseBody.root`, onde:

- `numeroParametros` informa quantos parâmetros voltaram
- `node` é o primeiro nó da árvore
- cada nível possui:

  - `nodeName` (nome do agrupamento)
  - `node` (próximo nível)
- o **nó folha** contém os atributos finais do parâmetro (key, type, module, classe, aba, etc.)

A Neppo normaliza a resposta para o formato:

```
{ "found": true/false, "data": {...}, "error": ... }
```

---

## Interface do componente (tela)

### Configuração de consulta

| Campo | Descrição |
| --- | --- |
| **Chave da Preferência**\* | Identificador técnico cadastrado no Sankhya. Ex.: `TIPTABPRECOS`, `MODPEDVENDIGITA`. |

> Dica prática: use este componente para buscar parâmetros que depois alimentam outros componentes (ex.: preço, pedido, TOP, tabela).

---

### Armazenamento

| Campo | Descrição |
| --- | --- |
| **Variável de Armazenamento** | Nome da variável que receberá o retorno. Ex.: `preferenciaVendaDigital`. |
| **Variável de Escopo Global** | Quando ativada, a variável fica acessível em todo o fluxo. |

---

## Estrutura do retorno (neppo)

### Exemplo de resposta

```
{
  "found": true,
  "data": {
    "key": "MODPEDVENDIGITA",
    "name": null,
    "label": "Modelo de pedido Venda Digital",
    "type": "PREFERENCE_CHARACTER",
    "parsedValue": null,
    "rawValue": null,
    "module": "E",
    "classe": "Especiais",
    "tab": "Venda Digital",
    "userCode": 0,
    "userName": "SUP",
    "editable": true,
    "logical": true,
    "hidden": false,
    "listContent": "1=484\r\n2=1251",
    "options": [
      { "key": "1", "value": "484" },
      { "key": "2", "value": "1251" }
    ],
    "path": ["Comercial", "Especiais", "Venda Digital"]
  },
  "error": null
}
```

---

## Retorno original da API Sankhya (referência)

```
{
  "serviceName": "ManutencaoPreferenciasSP.getParametrosComoEstrutura",
  "status": "1",
  "pendingPrinting": "false",
  "transactionId": "D2800D4D1C698E639823438BF460E6D6",
  "responseBody": {
    "root": {
      "numDecPrecision": "10",
      "numeroParametros": "1",
      "node": {
        "nodeName": "Comercial",
        "node": {
          "nodeName": "Especiais",
          "node": {
            "nodeName": "Venda Digital",
            "node": {
              "nodeName": "Modelo de pedido Venda Digital",
              "key": "MODPEDVENDIGITA",
              "type": "C",
              "module": "E",
              "classe": "Especiais",
              "aba": "Venda Digital",
              "codusu": "0",
              "nomusu": "SUP",
              "listContent": "1=484\r\n2=1251",
              "editable": "true",
              "logico": "S",
              "hidden": "N"
            }
          }
        }
      }
    }
  }
}
```

---

## Como os campos “saem” do Sankhya

O Sankhya devolve a preferência como **árvore**:

- `responseBody.root.numeroParametros` → quantidade
- `responseBody.root.node` → primeiro nível
- Cada nível:

  - `nodeName` (nome do agrupamento)
  - `node` (filho)
- **Nó folha**:

  - `key, type, module, classe, aba, codusu, nomusu, listContent, editable, logico, hidden...`

---

## De/Para — Neppo (data) ← Sankhya (API)

| Campo (nosso data) | De onde vem (Sankhya) | Descrição | Exemplo |
| --- | --- | --- | --- |
| data.key | responseBody.root.node.(...último...).key | Identificador técnico do parâmetro no Sankhya | MODPEDVENDIGITA |
| data.label | responseBody.root.node.(...último...).nodeName | Nome amigável do parâmetro (nome do nó folha) | Modelo de pedido Venda Digital |
| data.path | responseBody.root.node.nodeName → node.nodeName → node.nodeName (até o pai do último nó) | Caminho de categorias (todos os nodeName antes do nó folha) | Comercial, Especiais, Venda Digital |
| data.module | responseBody.root.node.(...último...).module | Módulo do Sankhya ao qual o parâmetro pertence | E |
| data.classe | responseBody.root.node.(...último...).classe | Classificação do parâmetro no Sankhya | Especiais |
| data.tab | responseBody.root.node.(...último...).aba | Aba/seção do parâmetro no Sankhya | Venda Digital |
| data.userCode | responseBody.root.node.(...último...).codusu | Código do usuário associado ao parâmetro (convertido para número) | 0 |
| data.userName | responseBody.root.node.(...último...).nomusu | Nome/apelido do usuário associado ao parâmetro | SUP |
| data.editable | responseBody.root.node.(...último...).editable | Indica se o parâmetro pode ser alterado ("true"/"false" → boolean) | true |
| data.logical | responseBody.root.node.(...último...).logico | Flag lógica do Sankhya ("S"/"N" → boolean) | true |
| data.hidden | responseBody.root.node.(...último...).hidden | Indica se o parâmetro está oculto ("S"/"N" → boolean) | false |
| data.type | responseBody.root.node.(...último...).type | Tipo do parâmetro no Sankhya normalizado para enum interno (ex.: "C" → PREFERENCE\_CHARACTER) | PREFERENCE\_CHARACTER |
| data.rawValue | responseBody.root.node.(...último...).value (quando existir) | Valor “cru” do parâmetro, como vem do Sankhya | null |
| data.parsedValue | Derivado de data.rawValue + data.type | Valor interpretado no tipo correto (boolean/int/decimal/date/text). Se não houver value, fica null | null |
| data.listContent | responseBody.root.node.(...último...).listContent | Lista textual de opções no formato chave=valor por linha | 1=484\r\n2=1251 |
| data.options | Derivado de data.listContent | Lista estruturada de opções (listContent parseado em {key,value}  ) | [{key:1,value:484},{key:2,value:1251}] |
| data.name | responseBody.root.node.(...último...).name (quando existir) | Nome alternativo do parâmetro (campo opcional, pode não vir na API) | null |

---

## Descrição dos campos retornados (Neppo)

| Campo | Descrição |
| --- | --- |
| found | Indica se a preferência foi encontrada |
| data.key | Chave consultada |
| data.label | Nome amigável (nó folha) |
| data.path | Caminho (pais do nó folha) |
| data.type | Tipo normalizado (enum interno) |
| data.rawValue | Valor “cru” (quando existir) |
| data.parsedValue | Valor convertido para o tipo correto |
| data.listContent | Lista textual de opções |
| data.options | Opções estruturadas (key/value) |
| error | Erro quando falhar |

---

## Exemplos de uso no bot

### Selecionar um valor padrão a partir das opções

Ex.: usar a primeira opção como default:

```
{{preferenciaVendaDigital.data.options[0].value}}
```

---

### Exibir opções no bot

```
Escolha o modelo de pedido:
1) {{preferenciaVendaDigital.data.options[0].value}}
2) {{preferenciaVendaDigital.data.options[1].value}}
```

---

## Tratamento de erros

| Situação | Comportamento |
| --- | --- |
| Chave inexistente | `found = false`, `data = null` ou vazio |
| Falha na API | `error` preenchido |
| Preferência sem lista | `listContent` nulo ou vazio, `options = []` |

Iremos disponibilizar exemplos de erro em breve.

---

## Tela no Sankhya OM

![Imagem 2: Tela no Sankhya OM](https://ajuda.sankhya.com.br/hc/article_attachments/42639688946839)

---

## Boas práticas

- Padronize as chaves consultadas (evite variações de nomenclatura)
- Prefira preferências para “defaults” de negócio (TOP, tabela, modelo)
- Sempre trate ausência de `options` e `rawValue`
- Use escopo global quando a preferência for usada em múltiplos pontos do fluxo

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
