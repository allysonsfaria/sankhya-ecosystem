---
id: "42430510052375"
titulo: "Componente Executar"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430510052375-Componente-Executar"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T16:07:16Z"
rotulos: ["sync_hc", "neppo", "neppo_858000522", "sync_hash_18a28cd367f7"]
---

# Componente Executar

O componente **Executar** chama **outro fluxo do bot como uma sub-rotina**, passando argumentos (variáveis). É a base da modularização dos fluxos: lógicas reutilizáveis ficam em fluxos separados e são invocadas de qualquer ponto.

---

## Visão geral

Use o Executar para:

- Reaproveitar fluxos utilitários (renderização de menus, transferência de atendimento, registro de analytics).
- Quebrar jornadas longas em fluxos menores e mais fáceis de manter.
- Iniciar a jornada a partir do Fluxo Principal.

Diferença para o **Redirecionar** (tipo fluxo): o Redirecionar desvia e **não volta**; o Executar chama o fluxo **como função**.

---

## Localização

Paleta de componentes (menu lateral direito da Área do Construtor) → categoria **Lógica** → **Executar**.

---

## Campos de configuração

| Campo | Obrigatório | Descrição | Exemplo |
| --- | --- | --- | --- |
| Fluxo de destino | Sim | Fluxo do bot a ser executado | "[Funções] Renderizar Menu" |
| Argumentos | Não | Variáveis passadas ao fluxo chamado, no formato chave/valor | `{"attempts": "0", "name": "principal"}` |

---

## Comportamento

- O fluxo chamado é executado com os **argumentos** informados — essas são as únicas variáveis do chamador visíveis nele (variáveis são locais por fluxo).
- Internamente gera uma ação `run` com `do: {sequence, args}`, apontando para o fluxo de destino.
- Fluxos só são executados quando **referenciados** por algum componente (Executar, Menu, Expressão etc.) — a ordem visual dos fluxos no construtor não influencia a execução.
- Padrão recomendado: fluxos utilitários com prefixo no nome (ex.: `[Funções]`, `[Transferir Atendimento]`) para sinalizar que são chamados por outros fluxos.

---

## Exemplo real de uso

Na jornada de matrícula escolar de um bot em produção:

**Início da jornada** (Fluxo principal):

- Fluxo de destino: "Quero ser aluno" — argumentos: `{}`

**Renderização parametrizada de menu** (fluxo "Cadastrar Nome", após salvar o nome do contato):

- Fluxo de destino: "[Funções] Renderizar Menu"
- Argumentos: `{"attempts": "0", "name": "principal"}`

O fluxo "[Funções] Renderizar Menu" usa `name` para decidir qual menu exibir e `attempts` para controlar o limite de respostas inválidas — um único fluxo genérico atende todos os menus do bot.

**Transferência reutilizável** (fluxo "[Funções] Tratativas Excedidas"):

- Fluxo de destino: "[Transferir Atendimento] - Transferir para Grupo"
- Argumentos: `{"Grupo": "Quero ser Aluno"}`

---

## Boas práticas e limitações

- Extraia para fluxos separados toda lógica usada em **mais de um lugar** (menus, transferências, registros de log).
- Parametrize os fluxos utilitários via argumentos (padrão `name`/`attempts` do exemplo real) em vez de duplicá-los.
- Lembre-se: **variáveis são locais por fluxo** — tudo que o fluxo chamado precisa deve ir nos argumentos.
- Adote convenção de nomes com prefixo (`[Funções]`, `[Transferir Atendimento]`) para identificar fluxos utilitários.
- Para desvio definitivo sem retorno, use **Redirecionar** em vez de Executar.
