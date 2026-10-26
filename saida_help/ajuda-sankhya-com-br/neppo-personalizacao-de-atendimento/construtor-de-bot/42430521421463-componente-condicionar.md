---
id: "42430521421463"
titulo: "Componente Condicionar"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430521421463-Componente-Condicionar"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T16:07:08Z"
rotulos: ["sync_hc", "neppo", "neppo_858000440", "sync_hash_7041edf04032"]
---

# Componente Condicionar

O componente **Condicionar** avalia **múltiplas condições em sequência** e desvia o fluxo para o destino da primeira condição verdadeira — o equivalente a um "se / senão se / senão" com vários ramos.

---

## Visão geral

Use o Condicionar quando houver **mais de dois caminhos possíveis** a partir de valores de variáveis (roteamento por menu, por perfil, por status de API etc.). Para decisões binárias simples (verdadeiro/falso), o componente **Expressão** em modo condicional é mais direto.

Cada condição é montada na UI com a estrutura **Se (variável) + Condição (comparador) + Valores**, e várias condições podem ser combinadas com o conector **"e"**.

---

## Localização

Paleta de componentes (menu lateral direito da Área do Construtor) → categoria **Lógica** → **Condicionar**.

---

## Campos de configuração

| Campo | Obrigatório | Descrição | Exemplo |
| --- | --- | --- | --- |
| Se (variável) | Sim | Variável avaliada na condição | `{{menuName}}` |
| Condição (comparador) | Sim | Operador de comparação: igual, maior, menor, contém etc. | `igual` |
| Valores | Sim | Valor(es) comparados com a variável | `principal` |
| Combinador "e" | Não | Adiciona condições extras que devem ser verdadeiras em conjunto | `{{attempts}} <= 3 e {{menuName}} == "principal"` |
| Fluxo de destino (por condição) | Sim | Fluxo executado quando a condição é verdadeira, com argumentos opcionais | "Menu Principal" com `{"attempts": "{{attempts}}"}` |
| Opção padrão (else) | Sim (recomendado) | Fluxo executado quando nenhuma condição é satisfeita | "[Funções] Tratativas Excedidas" |

---

## Comportamento

- As condições são avaliadas **na ordem configurada**; o fluxo desvia para o destino da **primeira** condição verdadeira.
- Se nenhuma condição for satisfeita, executa a **opção padrão (else)**.
- Cada destino recebe os **argumentos** configurados — repasse as variáveis necessárias.
- Internamente gera uma ação `conditions` com uma lista de `options` (`expression` + `do`) e um `else`; a representação da UI (variável/comparador/valores) fica registrada em metadados do componente.
- Valores de variáveis em comparações de texto são interpolados entre aspas (`"{{menuName}}" == "principal"`).

---

## Exemplo real de uso

Na jornada de matrícula escolar de um bot em produção (fluxo "[Funções] Renderizar Menu"), o Condicionar roteia o usuário para o menu correto, combinando o limite de tentativas com o nome do menu:

| Condição | Destino | Argumentos |
| --- | --- | --- |
| `attempts <= 3` **e** `menuName == "principal"` | Menu Principal | `{"attempts": "{{attempts}}"}` |
| `attempts <= 3` **e** `menuName == "serportal"` | Quero ser aluno | `{"attempts": "{{attempts}}"}` |
| `attempts <= 3` **e** `menuName == "souportal"` | Sou Aluno | `{"attempts": "{{attempts}}"}` |
| `attempts <= 3` **e** `menuName == "trabalhe"` | Trabalhe conosco | `{"attempts": "{{attempts}}"}` |
| `attempts <= 3` **e** `menuName == "fornecedor"` | Fornecedor | `{"attempts": "{{attempts}}"}` |
| **Opção padrão (else)** | [Funções] Tratativas Excedidas | `{}` |

Assim, um único fluxo de renderização atende todos os menus do bot, e o estouro de tentativas cai automaticamente na tratativa de transferência para atendimento humano.

---

## Boas práticas e limitações

- Sempre configure a **opção padrão (else)** — sem ela, valores inesperados deixam o fluxo sem rumo.
- Ordene as condições da mais específica para a mais genérica (a primeira verdadeira vence).
- Combine condições com **"e"** para regras compostas (ex.: limite de tentativas + valor do menu).
- Para apenas dois caminhos, prefira **Expressão** (mais simples de manter).
- Repasse as variáveis necessárias nos argumentos de cada destino.
