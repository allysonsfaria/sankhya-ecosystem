---
id: "42429875498263"
titulo: "Componente Converter Fala para Texto"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42429875498263-Componente-Converter-Fala-para-Texto"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T16:13:39Z"
rotulos: ["sync_hc", "neppo", "neppo_300613633", "sync_hash_d8dfe369ba78"]
---

# Componente Converter Fala para Texto

- [Visão Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429875498263-Componente-Converter-Fala-para-Texto#Visao-Geral)
- [Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429875498263-Componente-Converter-Fala-para-Texto#Usabilidade)
- [Formatos de áudio da plataforma](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429875498263-Componente-Converter-Fala-para-Texto#Formatos-de-audio-da-plataforma)
- [Modelos disponíveis](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429875498263-Componente-Converter-Fala-para-Texto#Modelos-disponiveis)
- [Leituras recomendadas](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429875498263-Componente-Converter-Fala-para-Texto#Leituras-recomendadas)

## Visão Geral

O componente **Converter Fala para Texto** do Construtor de Bot permite transcrever áudios enviados pelo usuário, expandindo as interações do chatbot para além do texto.

Para utilizar os modelos da OpenAI ou da ElevenLabs, é necessário cadastrar o valor do token correspondente no Neppo Vault, utilizando os caminhos `openai/token` ou `elevenLabs/token`. Veja mais em [Neppo Vault](https://sankhya.zendesk.com/hc/pt-br/articles/42429418990359)

## Usabilidade

O componente **Converter Fala para Texto** transcreve um áudio enviado pelo usuário para texto. Para usá-lo, é necessário fornecer:

- **Modelo**: qual modelo de transcrição utilizar (ex: Scribe V1, GPT-4o Mini Transcribe, GPT-4o Transcribe, Whisper-1)
- **Linguagem**: linguagem falada no áudio (ex: Português, Inglês)
- **Url do áudio:** URL acessível do arquivo de áudio para transcrição
- **Variável de armazenamento:** variável onde será armazenado o texto transcrito

![Imagem 1: Variável de armazenamento: variável onde será armazenado o texto transcrito](https://ajuda.sankhya.com.br/hc/article_attachments/42637348014231)

## Formatos de áudio da plataforma

| Origem do áudio | Formato padrão |
| --- | --- |
| Áudios enviados em chats de texto | oga e ogg |
| Chamadas de voz | wav |

## Modelos disponíveis

| Modelo | Provedor | Formato de Entrada | Particularidades | Link da Documentação |
| --- | --- | --- | --- | --- |
| Whisper-1 | OpenAI | mp3, mp4, mpeg, oga, ogg, mpga, m4a, wav, e webm | Suporte a áudios de no máximo 25 MB. | [Link](https://platform.openai.com/docs/models/whisper-1) |
| GPT-4o-mini-transcribe | OpenAI | mp3, mp4, mpeg, mpga, m4a, wav, e webm | Suporte a áudios de no máximo 25 MB. | [Link](https://platform.openai.com/docs/models/gpt-4o-mini-transcribe) |
| GPT-4o-transcribe | OpenAI | mp3, mp4, mpeg, mpga, m4a, wav, e webm | Suporte a áudios de no máximo 25 MB. | [Link](https://platform.openai.com/docs/models/gpt-4o-transcribe) |
| Scribe v1 | Eleven Labs | mp3, mp4, mpeg, oga, ogg, mpga, m4a, wav, e webm | Suporte a áudios de no máximo 3GB | [Link](https://elevenlabs.io/docs/models#scribe-v1) |

## Leituras recomendadas

- [Precificação - OpenAI](https://platform.openai.com/docs/pricing#audio-tokens)
- [Comparação dos modelos da OpenAI](https://platform.openai.com/docs/models/compare)
