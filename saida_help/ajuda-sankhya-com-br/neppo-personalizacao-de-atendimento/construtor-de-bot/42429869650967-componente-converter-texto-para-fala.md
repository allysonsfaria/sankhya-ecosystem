---
id: "42429869650967"
titulo: "Componente Converter Texto para Fala"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42429869650967-Componente-Converter-Texto-para-Fala"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T16:13:39Z"
rotulos: ["sync_hc", "neppo", "neppo_300023812", "sync_hash_37eee7c8b9dc"]
---

# Componente Converter Texto para Fala

- [Visão Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429869650967-Componente-Converter-Texto-para-Fala#Visao-Geral)
- [Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429869650967-Componente-Converter-Texto-para-Fala#Usabilidade)
- [Modelos disponíveis](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429869650967-Componente-Converter-Texto-para-Fala#Modelos-disponiveis)
- [Leituras recomendadas](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429869650967-Componente-Converter-Texto-para-Fala#Leituras-recomendadas)

## Visão Geral

O componente **Converter Texto para Fala** do Construtor de Bot permite transformar um texto em **fala sintetizada**, ampliando a experiência do chatbot e tornando as interações mais **dinâmicas, acessíveis e naturais**.

Para utilizar os modelos da OpenAI ou da ElevenLabs, é necessário cadastrar o valor do token correspondente no Neppo Vault, utilizando os caminhos `openai/token` ou `elevenLabs/token`. Veja mais em [Neppo Vault](https://sankhya.zendesk.com/hc/pt-br/articles/42429418990359)

## Usabilidade

Para usar o componente, o usuário deve preencher os seguintes campos:

- **Modelo**: modelo de sintetização de fala a ser utilizado.

  - OpenAI: `GPT-4o mini TTS`
  - ElevenLabs: `Eleven Flash v2.5`, `Eleven Turbo v2.5`
- **Linguagem**: idioma em que a fala será gerada (ex.: Português, Inglês).
- **Texto**: conteúdo textual que será convertido em áudio.
- **Voz**: voz a ser utilizada para a sintetização.

  - OpenAI oferece vozes predefinidas (ex.: Alloy).
  - ElevenLabs permite vozes personalizadas e clones de voz.
- **Prompt**: instruções adicionais para orientar como a fala deve ser gerada.

  - **OpenAI (GPT-4o mini TTS)**: aceita instruções diretamente no prompt, por exemplo:

    - “Leia de forma calma e pausada, como se estivesse narrando um audiolivro.”
    - “Fale em tom animado, como em uma apresentação de vendas.”
  - **ElevenLabs (Flash e Turbo v2.5)**: não aceitam prompt diretamente. Porém, você pode escrever instruções no campo **Prompt**, e o sistema interpreta automaticamente para ajustar parâmetros internos, como:

    - **Velocidade da fala (speed)**
    - **Estabilidade da voz (stability)**
    - **Entonação e naturalidade (similarity\_boost)**
    - **Clareza do áudio (use\_speaker\_boost)**
    - **Exagero de estilo** **(style)**

    Exemplo:

    - “Quero uma voz rápida e bem animada.” → ajusta internamente `speed` e `stability`.
    - “Fale devagar e de forma clara.” → ajusta `speed` e `similarity_boost`.
    - “Leia em tom formal e estável.” → ajusta `stability`.
- **Variável de armazenamento**: variável onde será armazenado a url do áudio sintetizado.

![Imagem 1: Variável de armazenamento : variável onde será armazenado a url do áudio sintetizado.](https://ajuda.sankhya.com.br/hc/article_attachments/42637375446295)

## Modelos disponíveis

| Modelo | Provedor | Formato padrão do áudio gerado | Link da Documentação |
| --- | --- | --- | --- |
| GPT-4o mini TTS | OpenAI | MP3 | [Link](https://platform.openai.com/docs/models/gpt-4o-mini-tts) |
| Eleven Flash v2.5 | Eleven Labs | MP3, com 44.1 kHz de sample rate e 128 kbps de bitrate | [Link](https://elevenlabs.io/docs/models#flash-v25) |
| Eleven Turbo v2.5 | Eleven Labs | MP3, com 44.1 kHz de sample rate e 128 kbps de bitrate | [Link](https://elevenlabs.io/docs/models#turbo-v25) |

## Leituras recomendadas

- [Precificação - OpenAI](https://platform.openai.com/docs/pricing#audio-tokens)
- [Limite de caracteres para geração de áudios- Eleven Labs](https://elevenlabs.io/docs/models#character-limits)
