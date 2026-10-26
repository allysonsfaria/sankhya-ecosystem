---
id: "42430362758935"
titulo: "Componente Sankhya - Tabela de Preço"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430362758935-Componente-Sankhya-Tabela-de-Pre%C3%A7o"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T17:13:26Z"
rotulos: ["sync_hc", "neppo", "neppo_857999046", "sync_hash_32a48633d4e5"]
---

# Componente Sankhya - Tabela de Preço

O componente **Tabela de Preço** identifica e retorna a **tabela de preço aplicável** para um contexto de venda (ex.: parceiro/cliente, vendedor, região, tipo de negociação), sendo a base para o cálculo correto do preço do produto no Sankhya.

bot-server: **versão 1.6.0**

bot-component-service: **versão 1.2.0**

![Imagem 1: bot-component-service: versão 1.2.0](https://ajuda.sankhya.com.br/hc/article_attachments/42639660616087)

Ele é usado principalmente para:

- Definir a tabela que será aplicada no **Preço do Produto**
- Respeitar regras de precificação configuradas no ERP
- Permitir cenários onde a tabela pode ser automática (por parceiro, perfil, região) ou selecionável (por tipo configurado)

Índice:

- [Objetivo do componente](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430362758935-Componente-Sankhya-Tabela-de-Pre%C3%A7o#Objetivo-do-componente)
- [Contextualização de negócio](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430362758935-Componente-Sankhya-Tabela-de-Pre%C3%A7o#Contextualizacao-de-negocio)
- [Integração técnica](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430362758935-Componente-Sankhya-Tabela-de-Pre%C3%A7o#Integracao-tecnica)
- [Interface do componente (leitura da tela)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430362758935-Componente-Sankhya-Tabela-de-Pre%C3%A7o#Interface-do-componente-leitura-da-tela)
- [🔧 Exemplo de requisição (Sankhya)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430362758935-Componente-Sankhya-Tabela-de-Pre%C3%A7o#-Exemplo-de-requisicao-Sankhya)
- [Estrutura do retorno (Neppo)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430362758935-Componente-Sankhya-Tabela-de-Pre%C3%A7o#Estrutura-do-retorno-Neppo)
- [Descrição dos campos retornados](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430362758935-Componente-Sankhya-Tabela-de-Pre%C3%A7o#Descricao-dos-campos-retornados)
- [Exemplos de uso no bot](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430362758935-Componente-Sankhya-Tabela-de-Pre%C3%A7o#Exemplos-de-uso-no-bot)
- [Tratamento de erros](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430362758935-Componente-Sankhya-Tabela-de-Pre%C3%A7o#Tratamento-de-erros)
- [Boas práticas](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430362758935-Componente-Sankhya-Tabela-de-Pre%C3%A7o#Boas-praticas)
- [Onde validar no sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430362758935-Componente-Sankhya-Tabela-de-Pre%C3%A7o#Onde-validar-no-sankhya)

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

Determinar, de forma dinâmica e segura, a **tabela de preço correta** que será utilizada no fluxo de venda, respeitando a configuração definida no Sankhya por meio da preferência **TIPTABPRECOS**.

---

## Contextualização de negócio

No Sankhya, a tabela de preço pode ser definida de diferentes formas, conforme o **tipo configurado na preferência TIPTABPRECOS**, que é ajustada pelo time de implantação.

Essa preferência define **qual regra será usada para encontrar a tabela de preço**.

### Tipos de regra possíveis

- ÚNICA
- REGIÃO DO VENDEDOR
- REGIÃO DO PARCEIRO
- PERFIL
- PARCEIRO
- TIPO DE NEGOCIAÇÃO
- LOCAL
- TIPO DE NEGOCIAÇÃO / VENDEDOR
- PARCEIRO / TIPO DE NEGOCIAÇÃO / VENDEDOR
- PARCEIRO / EMPRESA

### Exemplo (Tipo = PARCEIRO)

Quando o tipo configurado é **PARCEIRO**, a tabela retornada será a que estiver **vinculada diretamente no cadastro do parceiro (cliente)** no Sankhya.

---

## Integração técnica

A Neppo utiliza o serviço Sankhya:

```
ConsultaProdutosSP.contextualizarTabelaPreco
```

Esse serviço avalia a regra configurada (TIPTABPRECOS) e, com base nos parâmetros enviados, retorna a tabela de preço correta (`TGFTAB`).

---

## Interface do componente (leitura da tela)

### Parâmetros

| Campo | Descrição |
| --- | --- |
| **Código do parceiro**\* | Código do cliente/fornecedor no Sankhya (`codParc`). Obrigatório. ![Imagem 2: Código do cliente/fornecedor no Sankhya ( codParc ). Obrigatório.](https://ajuda.sankhya.com.br/hc/article_attachments/42639660895383) |
| **Código do vendedor (opcional)** | Código do vendedor (`codVend`). Utilizado quando a regra de tabela depende de vendedor, região do vendedor ou combinações. |

---

### Armazenamento

| Campo | Descrição |
| --- | --- |
| **Variável de armazenamento** | Nome da variável que receberá o resultado da consulta. Ex.: `tabelaPreco` |
| **Variável de escopo global** | Quando ativada, a tabela de preço fica acessível em todo o fluxo. |

---

## 🔧 Exemplo de requisição (Sankhya)

```
curl --location 'https://api.sankhya.com.br/gateway/v1/mgecom/service.sbr?serviceName=ConsultaProdutosSP.contextualizarTabelaPreco&outputType=json' \
--header 'Authorization: <TOKEN>' \
--header 'appkey: 3a51f41d-ebc4-429f-a888-55ff9fb48d34' \
--header 'Content-Type: application/json' \
--data '{
  "serviceName": "ConsultaProdutosSP.contextualizarTabelaPreco",
  "requestBody": {
    "criterio": {
      "tipTabPreco": "4",
      "codParc": "654",
      "codVend": null
    }
  }
}'
```

---

## Estrutura do retorno (Neppo)

### Exemplo de Resposta

```
{
  "found": true,
  "data": {
    "nuTab": 708,
    "codTab": 0,
    "name": "TABELA ZERO"
  },
  "error": null
}
```

---

## Descrição dos campos retornados

| Campo | Descrição | Origem |
| --- | --- | --- |
| found | Indica se a tabela foi encontrada | Neppo |
| data.nuTab | Número único da tabela de preço | TGFTAB.NUTAB |
| data.codTab | Código da tabela de preço | TGFTAB.CODTAB |
| data.name | Nome da tabela de preço | Retornado pelo serviço (sem campo explícito na doc oficial) |
| error | Detalhes do erro quando houver falha | Neppo |

---

## Exemplos de uso no bot

### Encadear com o componente preço do produto

O valor mais utilizado é o **NUTAB**:

```
{{tabelaPreco.data.nuTab}}
```

Esse valor deve ser informado no componente **preço do produto** para garantir o cálculo correto.

---

### Exibir tabela aplicada (diagnóstico)

```
A tabela de preço aplicada é: {{tabelaPreco.data.name}}
```

---

## Tratamento de erros

| Situação | Comportamento |
| --- | --- |
| Parceiro inválido | `found = false` |
| Regra exige vendedor e não foi informado | `error` preenchido |
| Nenhuma tabela encontrada | `found = false` |
| Falha na API | `error` preenchido |

Iremos disponibilizar exemplos de erro em breve.

---

## Boas práticas

- Sempre informe **Código do parceiro**
- Informe **Código do vendedor** quando a operação envolver vendedor ou região
- Use `nuTab` como identificador principal para precificação
- Evite hardcode de tabela quando TIPTABPRECOS estiver ativo
- Utilize escopo global quando a tabela for reutilizada em múltiplos produtos

---

## Onde validar no sankhya

As tabelas de preço podem ser conferidas diretamente no ERP em:

- **Comercial → Tabelas de preços**

![Imagem 3: Comercial → Tabelas de preços](https://ajuda.sankhya.com.br/hc/article_attachments/42639690218903)

E a regra de definição da tabela em:

- **Preferência: TIPTABPRECOS**

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
