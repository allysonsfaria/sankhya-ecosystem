---
id: "42430493252631"
titulo: "Componente Esperar"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430493252631-Componente-Esperar"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T16:07:06Z"
rotulos: ["sync_hc", "neppo", "neppo_858000424", "sync_hash_ae2ec6acaf3c"]
---

# Componente Esperar

O componente **Esperar** pausa a execução do fluxo por um tempo determinado antes de seguir para o próximo componente.

---

## Visão geral

Use o Esperar para introduzir pausas intencionais no fluxo: aguardar processamento externo, espaçar mensagens para dar ritmo natural à conversa, ou aguardar uma janela de tempo antes de uma nova verificação.

---

## Localização

Paleta de componentes (menu lateral direito da Área do Construtor) → categoria **Lógica** → **Esperar**.

---

## Campos de configuração

| Campo | Obrigatório | Descrição | Exemplo |
| --- | --- | --- | --- |
| Tempo | Sim | Duração da espera | `2` |
| Unidade de tempo | Sim | Unidade da duração (ex.: minutos) | `minutos` |
| Variável (timer) | Sim | Variável exigida pelo componente para controlar o timer | `timerEspera` |

---

## Comportamento

- O fluxo fica **pausado** pelo tempo configurado e retoma automaticamente no componente seguinte.
- O componente **exige uma variável** para armazenar/controlar o timer da espera.
- Internamente gera uma ação `timeout` com `time`, `type` (unidade) e execução assíncrona; o motor também suporta um atraso adicional em milissegundos (`delay`) (verificar na UI).
- Não confunda com a configuração de **inatividade** de outros componentes (Entrada de Dados, Menu de Opções, requisições): inatividade reage à ausência de resposta do usuário ou timeout de requisição; o Esperar é uma pausa incondicional do próprio fluxo.

---

## Exemplo real de uso

A jornada de matrícula escolar analisada nesta documentação não utiliza o componente Esperar — as pausas de interação são naturais, pois os componentes de Entrada de Dados e Menu aguardam a resposta do usuário.

Um uso típico no mesmo cenário seria aguardar alguns segundos após disparar o registro no relatório analítico (Requisitar API) antes de consultar o status do processamento em uma segunda chamada.

---

## Boas práticas e limitações

- Use esperas curtas; pausas longas aumentam o risco de o usuário abandonar a conversa.
- Para reagir à **falta de resposta do usuário**, prefira a configuração de inatividade dos componentes de interação (ou o hook global de inatividade do bot) em vez do Esperar.
- Ao aguardar processamento externo, combine Esperar + Requisitar API + Expressão em um laço controlado com contador de tentativas, evitando espera infinita.
- Lembre-se de preencher a variável do timer — ela é obrigatória para o funcionamento do componente.
