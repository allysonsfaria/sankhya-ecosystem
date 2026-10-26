---
id: "42430493568791"
titulo: "Componente Para JSON"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430493568791-Componente-Para-JSON"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T16:07:10Z"
rotulos: ["sync_hc", "neppo", "neppo_858000456", "sync_hash_5cd6dc2661d3"]
---

# Componente Para JSON

O componente **Para JSON** converte uma **string JSON** em um **objeto navegável**, permitindo acessar campos individuais com a sintaxe `{{variavel.campo}}`.

---

## Visão geral

O caso de uso principal é o tratamento de retornos de API: os componentes **Requisitar API** e **Neppo API** devolvem o corpo da resposta como **string** (`{{Retorno.body}}`). O Para JSON transforma essa string em objeto, habilitando o acesso direto aos campos (`{{Retorno_obj.campo}}`, `{{Retorno_obj.results.0.nome}}`).

---

## Localização

Paleta de componentes (menu lateral direito da Área do Construtor) → categoria **Lógica** → **Para JSON**.

---

## Campos de configuração

| Campo | Obrigatório | Descrição | Exemplo |
| --- | --- | --- | --- |
| Texto (string JSON) | Sim | String a ser convertida. Normalmente o corpo de um retorno de API | `{{GetSchedule.body}}` |
| Variável de armazenamento | Sim | Variável que recebe o objeto convertido | `GetSchedule_obj` |
| Variável de escopo global | Não | Torna o objeto acessível em todos os fluxos | — |

---

## Comportamento

- A conversão é imediata e o fluxo segue para o próximo componente.
- Após a conversão, os campos são acessados por caminho: `{{Var_obj.campo}}`, `{{Var_obj.objeto.campo}}` e itens de lista por índice: `{{Var_obj.results.0.openTime}}`.
- Convenção de nomenclatura recomendada: variável de origem `X` → objeto `X_obj` (ou `X_json`), facilitando a leitura do fluxo.
- Se a string não for um JSON válido, a conversão falha — a ocorrência pode ser inspecionada na tela **Execuções**.
- Internamente gera uma ação `json` com `text` (string de entrada) e a variável de destino.

---

## Exemplo real de uso

Na jornada de matrícula escolar de um bot em produção, o padrão **Neppo API → Para JSON → uso dos campos** se repete em toda a verificação de horário de atendimento:

**Parse do retorno de horários** (fluxo "Verificar Horário de Atendimento"):

- Texto: `{{ScheduleWork.body}}`
- Variável de armazenamento: `ScheduleWork_obj`

Em seguida, uma **Expressão** acessa os campos por índice para filtrar o horário de abertura do dia atual:

```
{0: "{{ScheduleWork_obj.results.0.openTime}}", 1: "{{ScheduleWork_obj.results.1.openTime}}", ...}["{{daycode}}"]
```

**Parse da última mensagem** (fluxo "[Funções] Guardar Relatório Analítico"):

- Texto: `{{GetLastMessage.body}}` → variável `GetLastMessage_obj`
- Uso posterior: `{{GetLastMessage_obj.message}}` no body de um Requisitar API.

---

## Boas práticas e limitações

- Converta **todo retorno de API** antes de acessar campos — `{{Retorno.body.campo}}` não funciona sobre a string crua.
- Siga a convenção `X` → `X_obj` para manter os fluxos legíveis.
- Valide a existência dos campos antes de usar (com **Expressão**/**Condicionar**) — respostas de erro têm estrutura diferente da resposta de sucesso.
- Para listas, acesse itens por índice numérico (`results.0`, `results.1`) ou percorra com o componente **Iteração**.
