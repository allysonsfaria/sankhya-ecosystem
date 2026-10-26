---
id: "42430492286487"
titulo: "Componente Entrada de Dados"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430492286487-Componente-Entrada-de-Dados"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T16:07:00Z"
rotulos: ["sync_hc", "neppo", "neppo_858000325", "sync_hash_3a908ad22653"]
---

# Componente Entrada de Dados

O componente **Entrada de Dados** faz uma pergunta ao usuário e **armazena a resposta em uma variável** do fluxo. É a forma padrão de capturar informações abertas — nome, datas, textos livres, números de documento etc.

---

## Visão geral

Use Entrada de Dados quando o bot precisar de uma informação digitada pelo usuário. A resposta fica disponível na variável configurada e pode ser usada em qualquer componente seguinte com a sintaxe `{{variavel}}` — em mensagens, requisições de API, expressões e argumentos de fluxo.

Para respostas com opções pré-definidas, prefira o **Menu de Opções**. Para validar o formato da resposta (CPF, CNPJ, números), combine com o componente **Validar** ou com **Expressão**.

---

## Localização

Paleta de componentes (menu lateral direito da Área do Construtor) → categoria **Elementos** → **Entrada de Dados**.

---

## Campos de configuração

| Campo | Obrigatório | Descrição | Exemplo |
| --- | --- | --- | --- |
| Mensagem (pergunta) | Sim | Texto enviado ao usuário solicitando a informação. Aceita `{{variavel}}` e formatação do canal | `*Qual o Nome completo do(a) aluno(a)?*` |
| Variável de armazenamento | Sim | Nome da variável que receberá a resposta do usuário | `NomeAluno` |
| Validação | Não | Habilita validação da resposta (quando desabilitada, qualquer texto é aceito) | Desabilitada |
| Inatividade | Não | Ação executada caso o usuário não responda dentro do tempo configurado (tempo + fluxo de destino) | Após 5 minutos → fluxo "Encerrar por inatividade" |

---

## Comportamento

- O componente envia a mensagem e **pausa o fluxo aguardando a resposta** do usuário (execução assíncrona).
- A resposta é gravada na variável configurada e acessada como `{{NomeVariavel}}` nos componentes seguintes.
- A variável é local ao fluxo; para usá-la em outro fluxo, passe-a como argumento no desvio (componentes Executar, Menu de Opções, Expressão etc.).
- Com **inatividade** habilitada, se o usuário não responder no tempo definido, o fluxo é desviado para o destino configurado.
- Internamente, o componente gera uma ação `question` (com `set`, `validation` e `async`) contendo a mensagem no grupo de ações.

---

## Exemplo real de uso

Na jornada de matrícula escolar de um bot em produção (fluxo "Quero ser aluno"), a Entrada de Dados coleta os dados do estudante em sequência:

Pergunta 1 — armazena em `NomeAluno`:

```
Ok! Agora vamos para os dados do estudante...
*Qual o Nome completo do(a) aluno(a)?*
OBS: Sem Abreviação
```

Pergunta 2 — armazena em `DataNascimento`:

```
*Consegue me enviar a data de nascimento no seguinte padrão 22/10/2015?*
```

Em seguida, um componente **Expressão** valida o formato da data com regex e desvia para o fluxo de correção caso inválida — padrão recomendado quando a validação nativa não cobre o formato desejado.

---

## Boas práticas e limitações

- Deixe claro na pergunta o **formato esperado** da resposta (ex.: "padrão 22/10/2015").
- Sempre preveja tratamento para respostas fora do formato: use **Validar**, ou **Expressão** com regex, com fluxo de reentrada da pergunta.
- Configure **inatividade** em perguntas críticas para não deixar sessões presas aguardando resposta.
- Nomeie variáveis de forma descritiva e consistente (ex.: `NomeAluno`, `DataNascimento`) — elas serão referenciadas em vários pontos do fluxo.
- Lembre-se de repassar as variáveis coletadas como argumentos ao desviar para outros fluxos, senão elas se perdem.
