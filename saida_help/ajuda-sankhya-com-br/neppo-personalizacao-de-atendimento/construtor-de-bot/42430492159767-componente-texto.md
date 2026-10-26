---
id: "42430492159767"
titulo: "Componente Texto"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430492159767-Componente-Texto"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T16:06:58Z"
rotulos: ["sync_hc", "neppo", "neppo_858000308", "sync_hash_de87d4728ced"]
---

# Componente Texto

O componente **Texto** envia uma mensagem ao usuário dentro do fluxo do bot. É o componente mais básico e mais utilizado do construtor: serve para saudações, instruções, confirmações e qualquer comunicação unidirecional (o bot fala, mas não espera resposta).

---

## Visão geral

Use o componente Texto sempre que o bot precisar **informar algo sem capturar retorno** do usuário. Para perguntar e armazenar a resposta, utilize o componente **Entrada de Dados**; para oferecer opções de escolha, utilize o **Menu de Opções**.

O componente também suporta o envio de **arquivo por URL** (JSON, documento, imagem, áudio ou vídeo), permitindo compartilhar conteúdo hospedado externamente.

---

## Localização

Paleta de componentes (menu lateral direito da Área do Construtor) → categoria **Elementos** → **Texto**.

---

## Campos de configuração

| Campo | Obrigatório | Descrição | Exemplo |
| --- | --- | --- | --- |
| Mensagem (texto) | Sim | Conteúdo enviado ao usuário. Aceita interpolação de variáveis com `{{variavel}}`, quebras de linha, emojis e formatação do canal (ex.: `*negrito*` no WhatsApp) | `Olá, {{contact.displayName}}! Como posso ajudar?` |
| Arquivo por URL | Não | URL de um arquivo (JSON/documento/imagem/áudio/vídeo) a ser enviado junto ou no lugar do texto | `https://exemplo.com/tabela-precos.pdf` |

---

## Comportamento

- A mensagem é enviada e o fluxo **segue imediatamente** para o próximo componente — não há espera por resposta.
- Variáveis `{{...}}` são resolvidas em tempo de execução, incluindo variáveis globais de sessão (`{{firstMessage.*}}`, `{{contact.*}}`) e variáveis definidas em componentes anteriores.
- Se a variável interpolada estiver vazia, o texto é renderizado sem o valor (uma mensagem cujo conteúdo é somente uma variável vazia resulta em mensagem vazia — ver exemplo abaixo).
- Internamente, o componente gera uma ação `message` com `contentType: "TEXT"` no JSON do fluxo.

---

## Exemplo real de uso

Na jornada de matrícula escolar de um bot em produção, o componente Texto é usado na saudação inicial do fluxo "Inicialização do Bot":

```
Olá! Tudo bem?😄
Aqui é a *Ana*, sua assistente de atendimento!🙋‍♀️
```

E também com interpolação de variável no fluxo "[Funções] Renderizar Menu", onde a mensagem de resposta inválida só aparece a partir da segunda tentativa (a variável `{{RespostaInvalida}}` é calculada por um componente Expressão antes):

```
{{RespostaInvalida}}
```

Outro uso comum é a mensagem informativa antes de encerrar, como no fluxo "Trabalhe conosco":

```
#VenhaSerPortal
Clique aqui para conferir as vagas disponíveis e deixe o seu currículo no Banco de Talentos.
https://burh.com.br/carreiras/portalsorocaba
```

---

## Boas práticas e limitações

- Prefira mensagens curtas e objetivas; quebre textos longos em mais de um componente Texto.
- Utilize a formatação nativa do canal (ex.: `*negrito*` no WhatsApp) com moderação.
- Ao enviar arquivo por URL, garanta que a URL seja pública e estável.
- Para condicionar a exibição de uma mensagem, combine com **Expressão** ou **Condicionar** (ou calcule o texto em uma variável, como no exemplo acima).
- Este componente não captura resposta; mensagens seguidas são enviadas em sequência imediata.
