---
id: "42430510301463"
titulo: "Componente Executar Script"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430510301463-Componente-Executar-Script"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T16:07:19Z"
rotulos: ["sync_hc", "neppo", "neppo_858000555", "sync_hash_90feb2864afd"]
---

# Componente Executar Script

O componente **Executar Script** executa código **JavaScript** dentro do fluxo do bot e disponibiliza o retorno em uma variável, permitindo transformações de dados e lógicas que os demais componentes não cobrem.

---

## Visão geral

Use o Executar Script para manipulações complexas: formatar datas e valores, montar estruturas de dados, aplicar regras de negócio com várias etapas, tratar listas antes de uma Iteração etc.

Para expressões simples de uma linha (cálculos, regex, ternários), o componente **Expressão** em modo "Avaliar Expressão" costuma ser suficiente e mais leve.

---

## Localização

Paleta de componentes (menu lateral direito da Área do Construtor) → categoria **Lógica** → **Executar Script**.

---

## Campos de configuração

| Campo | Obrigatório | Descrição | Exemplo |
| --- | --- | --- | --- |
| Script (JavaScript) | Sim | Função no formato `var script = function (vars) { ... return {...}; }`. As variáveis do fluxo chegam pelo parâmetro `vars` | Ver exemplo abaixo |
| Variável de armazenamento | Sim | Variável que recebe o objeto retornado pela função | `dadosTratados` |
| Variável de escopo global | Não | Torna o retorno acessível em todos os fluxos | — |

---

## Comportamento

- O script deve seguir o formato de função:

```
var script = function (vars) {
  // lógica em JavaScript
  return { campo1: "valor", campo2: 123 };
};
```

- O **objeto retornado** é gravado na variável configurada e seus campos são acessados como `{{variavel.campo1}}` nos componentes seguintes.
- As variáveis do fluxo ficam disponíveis dentro do script (parâmetro `vars`), além da interpolação `{{variavel}}` no corpo do código.
- A execução é síncrona: o fluxo aguarda o término do script.
- Internamente gera uma ação `javascript` com o código no argumento `js`.

---

## Exemplo real de uso

Na jornada de matrícula escolar de um bot em produção, as transformações foram implementadas com o componente **Expressão** em modo JavaScript — por exemplo, a validação do formato da data de nascimento com função autoexecutável:

```
(function () {
  var data = "{{DataNascimento}}";
  var regex = /^(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[0-2])\/(19|20)\d\d$/;
  return regex.test(data) ? "true" : "false";
})()
```

A mesma lógica, no componente Executar Script, ficaria assim (com a vantagem de retornar múltiplos campos):

```
var script = function (vars) {
  var data = "{{DataNascimento}}";
  var regex = /^(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[0-2])\/(19|20)\d\d$/;
  return {
    valida: regex.test(data),
    dataOriginal: data
  };
};
```

Com variável de armazenamento `validacaoData`, o resultado é lido como `{{validacaoData.valida}}`.

---

## Boas práticas e limitações

- **Retorne sempre um objeto** — o retorno vira a variável configurada e os campos são acessados por `{{variavel.campo}}`.
- Prefira **Expressão** para lógicas de uma linha; reserve o Executar Script para transformações com múltiplos passos ou múltiplos retornos.
- Cuidado com a interpolação: `{{variavel}}` é substituída pelo texto do valor antes da execução — envolva em aspas quando for string.
- Evite scripts longos e dependentes de estado externo; o script não faz chamadas HTTP (use **Requisitar API** para isso).
- Teste o fluxo na tela **Execuções** para inspecionar entrada/saída do node em caso de erro.
