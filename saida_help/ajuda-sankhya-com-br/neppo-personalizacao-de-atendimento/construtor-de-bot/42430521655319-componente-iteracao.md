---
id: "42430521655319"
titulo: "Componente Iteração"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430521655319-Componente-Itera%C3%A7%C3%A3o"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T16:07:11Z"
rotulos: ["sync_hc", "neppo", "neppo_858000473", "sync_hash_31a7612a10e9"]
---

# Componente Iteração

O componente **Iteração** percorre uma **lista** (array) e executa um fluxo **para cada item**, permitindo processar coleções de dados — resultados de API, listas de produtos, itens de pedido etc.

---

## Visão geral

Use a Iteração quando precisar repetir uma sequência de ações para cada elemento de uma lista: exibir cada produto retornado por uma busca, enviar uma mensagem por item do pedido, processar registros um a um.

O componente trabalha em conjunto com **Para JSON** (que transforma o retorno de API em objeto com a lista) e com um **fluxo por item**, que recebe cada elemento em uma variável.

---

## Localização

Paleta de componentes (menu lateral direito da Área do Construtor) → categoria **Lógica** → **Iteração**.

---

## Campos de configuração

| Campo | Obrigatório | Descrição | Exemplo |
| --- | --- | --- | --- |
| Iteração sobre | Sim | Caminho da lista a percorrer, informado **SEM chaves** `{{ }}` | `retornoApi.produtos` |
| Variável de cada item | Sim | Nome da variável que representa o item corrente dentro do fluxo por item | `elemento_lista` |
| Fluxo por item | Sim | Fluxo executado uma vez para cada elemento da lista | "Exibir Produto" |
| Argumentos | Não | Variáveis adicionais passadas ao fluxo por item | `{"AnoLetivo": "{{AnoLetivo}}"}` |

---

## Comportamento

- **Atenção à sintaxe**: o campo "Iteração sobre" recebe a referência da lista **sem chaves** (`retornoApi.produtos`, e não `{{retornoApi.produtos}}`).
- Dentro do fluxo por item, o elemento corrente é acessado **com chaves**: `{{elemento_lista.campo}}` (ex.: `{{elemento_lista.nome}}`, `{{elemento_lista.preco}}`).
- O fluxo por item é executado uma vez para cada elemento, em sequência; ao final da lista, a execução retorna ao fluxo principal, no componente seguinte à Iteração.
- Variáveis do fluxo chamador não são visíveis no fluxo por item, exceto as passadas como argumentos.

---

## Exemplo real de uso

A jornada de matrícula escolar analisada nesta documentação não utiliza o componente Iteração — as listas retornadas (horários de atendimento) foram acessadas por índice fixo (`{{ScheduleWork_obj.results.0.openTime}}` ... `results.6`), o que funciona porque a lista tem tamanho conhecido (7 dias da semana).

Um uso típico no mesmo cenário seria listar dinamicamente os cursos disponíveis retornados por uma API:

- Requisitar API → variável `Cursos` → Para JSON → `Cursos_obj`
- Iteração sobre: `Cursos_obj.results` (sem chaves)
- Variável de cada item: `curso`
- Fluxo por item: envia um Texto com `📚 {{curso.nome}} — {{curso.turno}}`

---

## Boas práticas e limitações

- **Não use chaves** no campo "Iteração sobre" — este é o erro de configuração mais comum do componente.
- Converta o retorno de API com **Para JSON** antes de iterar.
- Evite iterar listas muito grandes que gerem dezenas de mensagens; limite os resultados na origem (paginação/`size` na API).
- Para listas de tamanho fixo e pequeno, o acesso por índice (`results.0`, `results.1`...) pode ser mais simples que a Iteração.
- Passe como argumentos as variáveis de contexto que o fluxo por item precisar.
