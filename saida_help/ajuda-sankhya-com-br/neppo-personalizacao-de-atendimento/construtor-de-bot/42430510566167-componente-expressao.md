---
id: "42430510566167"
titulo: "Componente Expressão"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430510566167-Componente-Express%C3%A3o"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T16:07:13Z"
rotulos: ["sync_hc", "neppo", "neppo_858000489", "sync_hash_62a42889cc06"]
---

# Componente Expressão

O componente **Expressão** avalia uma expressão e atua de dois modos: **condicional** (verdadeiro/falso, com desvio de fluxo para cada resultado) ou **avaliar expressão** (executa uma expressão **JavaScript** e grava o resultado em uma variável).

---

## Visão geral

É o "canivete suíço" da categoria Lógica:

- **Modo condicional** — decisão binária: se a condição for verdadeira, segue para um fluxo; senão, para outro. Ex.: `"{{Setor}}" == "Vendas"`.
- **Modo avaliar expressão** — cálculo/transformação: a expressão JavaScript é avaliada e o resultado vai para a variável configurada. Ex.: incrementar contador, extrair dia da semana, aplicar regex.

Para mais de dois caminhos, use **Condicionar**; para scripts com múltiplos passos, use **Executar Script**.

---

## Localização

Paleta de componentes (menu lateral direito da Área do Construtor) → categoria **Lógica** → **Expressão**.

---

## Campos de configuração

### Modo condicional

| Campo | Obrigatório | Descrição | Exemplo |
| --- | --- | --- | --- |
| Condição | Sim | Expressão booleana. Variáveis de texto entre aspas | `"{{firstMessage.originUser}}" == "WHATSAPP"` |
| Fluxo se verdadeiro | Sim | Destino quando a condição é verdadeira, com argumentos | "[Envio Ativo] - Consultar Envio Ativo Em Aberto" |
| Fluxo se falso | Sim | Destino quando a condição é falsa, com argumentos | "Inicialização do Bot" |

### Modo avaliar expressão

| Campo | Obrigatório | Descrição | Exemplo |
| --- | --- | --- | --- |
| Expressão (JavaScript) | Sim | Expressão avaliada em runtime; aceita `{{variavel}}` | `{{attempts}} ? {{attempts}} + 1 : 1` |
| Variável de armazenamento | Sim | Variável que recebe o resultado | `attempts` |

---

## Comportamento

- **As expressões aceitam JavaScript**: operadores lógicos (`&&`, `||`), ternários, objetos usados como mapa, funções nativas (`new Date()`, `JSON.stringify`) e até funções autoexecutáveis (IIFE) com regex.
- No modo condicional, a interpolação `{{variavel}}` de valores texto deve vir **entre aspas** (`"{{x}}" == "y"`); números podem ser comparados sem aspas.
- No modo avaliar, o resultado da expressão é gravado na variável e usado como `{{variavel}}` adiante.
- Internamente gera uma ação `expression`: com `condition` + `do`/`else` (condicional) ou `text` + `set` (avaliar).

---

## Exemplo real de uso

Da jornada de matrícula escolar de um bot em produção:

**Condicional — detectar o canal** (Fluxo principal):

```
"{{firstMessage.originUser}}" == "WHATSAPP"
```

Verdadeiro → fluxo de consulta de envio ativo; Falso → "Inicialização do Bot".

**Avaliar — incrementar contador de tentativas** (fluxo "[Funções] Renderizar Menu"), resultado na variável `attempts`:

```
{{attempts}} ? {{attempts}} + 1 : 1
```

**Avaliar — obter o dia da semana como código** (fluxo "Verificar Horário de Atendimento"), variáveis `day` e `daycode`:

```
new Date().toDateString().split(' ')[0]
```

```
{"Sun": 0, "Mon": 1, "Tue": 2, "Wed": 3, "Thu": 4, "Fri": 5, "Sat": 6}["{{day}}"]
```

**Avaliar — validar data de nascimento com regex** (fluxo "Quero ser aluno"), variável `resultado_data_nascimento`:

```
(function () { var data = "{{DataNascimento}}"; var regex = /^(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[0-2])\/(19|20)\d\d$/; return regex.test(data) ? "true" : "false"; })()
```

Seguido de uma Expressão condicional (`{{resultado_data_nascimento}} == true`) que desvia para "Ano Letivo" (válido) ou "Data Nascimento Inválida" (inválido).

---

## Boas práticas e limitações

- Coloque **aspas em comparações de texto** (`"{{var}}" == "valor"`) — sem aspas, valores com espaços quebram a expressão.
- Prefira o padrão **avaliar + condicional em dois componentes** para lógicas com regex (mais fácil de depurar, como no exemplo real).
- Cuidado com valores vazios/nulos: teste `"{{var}}" == ""` e `"{{var}}" == "null"` quando a variável pode não existir.
- Para mais de dois destinos, use **Condicionar**; para lógica extensa, **Executar Script**.
- Lembre-se de repassar as variáveis nos argumentos dos fluxos de destino.
