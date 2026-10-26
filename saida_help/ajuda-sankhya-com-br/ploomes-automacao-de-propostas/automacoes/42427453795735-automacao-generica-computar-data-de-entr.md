---
id: "42427453795735"
titulo: "Automação genérica: Computar data de entrada no funil"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427453795735-Automa%C3%A7%C3%A3o-gen%C3%A9rica-Computar-data-de-entrada-no-funil"
trilha: "PLOOMES: Automação de propostas  > Automações"
atualizado_em: "2026-08-03T12:59:20Z"
rotulos: ["sync_hc", "ploomes", "sync_hash_854948f86936", "ploomes_12100179"]
---

# Automação genérica: Computar data de entrada no funil

O Ploomes oferece ferramentas de automação versáteis que ajudam a monitorar métricas relacionadas ao tempo, como datas de entrada e o tempo gasto em horas ou dias em cada uma delas. Este guia mostra como configurar automações internas para aprimorar o controle de etapas.

## Introdução

Acompanhar datas de entrada e saída, bem como calcular o tempo em cada etapa, permite monitorar fluxos de trabalho e melhorar a eficiência dos processos. No Ploomes, é possível configurar campos personalizados e regras de automação para realizar essa gestão.

## Como configurar automações internas para controle de datas e tempo

## 1. Criar campos personalizados

Você precisará criar campos que armazenem os dados de cada etapa:

- **Campos de data de entrada:** um para cada etapa, por exemplo, Data de Entrada A, Data de Entrada B etc...

- **Campos de horas:** campos do tipo número inteiro para calcular o tempo gasto entre etapas em horas, por exemplo, Horas etapa A, Horas etapa B etc...

- **Campos de dias:** campos do tipo número inteiro para calcular o tempo gasto entre etapas em dias, por exemplo, Dias etapa A, Dias etapa B etc...

## 2. Criar automações

Dentro de administração será necessário criar as automações seguindo o passo a passo da configuração, onde a quantidade de automações irá depender de sua necessidade:

## 3. Capturar datas de entrada nas etapas

Para cada etapa, crie uma automação específica que preencha o campo correspondente com a data atual sempre que o negócio entrar naquela etapa..

##

---

## Passo a passo em vídeo

Para ajudar a configurar essas automação, veja o tutorial em vídeo com passo a passo:

- [Automações para Cálculo de Tempo](https://www.loom.com/share/cbca6c75c86d4bdd982a9aa73c063865?sid=b0c02e6c-e0ca-4c6b-ba41-261b14cd8225)

## Fórmulas usadas no passo a passo em vídeo

Fórmula para campo de inicio na etapa (descrito como inicio da etapa x no vídeo)

```
let data = new Date();
data.setHours(data.getHours()-3);
data.toISOString()
```

Fórmula para calculo das horas entre etapas (descrito como horas da etapa x no vídeo)

```
(function (inicial, final) {
if (!inicial || !final) return 0;

function parseDate(str) {
var parts = str.split(" ");
var dateParts = parts[0].split("/");
var timeParts = parts[1].split(":");
var ampm = parts[2];

var month = parseInt(dateParts[0], 10) - 1; // 0-indexed
var day = parseInt(dateParts[1], 10);
var year = parseInt(dateParts[2], 10);

var hour = parseInt(timeParts[0], 10);
var minute = parseInt(timeParts[1], 10);
var second = parseInt(timeParts[2], 10);

if (ampm === "PM" && hour < 12) hour += 12;
if (ampm === "AM" && hour === 12) hour = 0;

return new Date(year, month, day, hour, minute, second);
}

var data1 = parseDate(inicial);
var data2 = parseDate(final);

var diferencaMs = data2 - data1;
var diferencaHoras = diferencaMs / (1000 * 60 * 60);

return diferencaHoras.toFixed(0);
})("[Negócio.Início etapa 1]", "[Negócio.Início etapa 2]");
```

## Campo nativo Dias na Etapa

O campo nativo "Dias na Etapa" exibe apenas o tempo da etapa atual, reiniciando a cada mudança de etapa. Para ter um histórico das etapas anteriores, é necessário usar campos personalizados e automações conforme mostrado no tópicos acima.
