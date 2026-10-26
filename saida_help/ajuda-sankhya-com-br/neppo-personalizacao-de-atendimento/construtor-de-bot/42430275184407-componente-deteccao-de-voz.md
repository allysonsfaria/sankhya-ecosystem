---
id: "42430275184407"
titulo: "Componente Detecção de Voz"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430275184407-Componente-Detec%C3%A7%C3%A3o-de-Voz"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T16:03:23Z"
rotulos: ["sync_hc", "neppo", "neppo_857997888", "sync_hash_75fe14e097b7"]
---

# Componente Detecção de Voz

## Visão Geral

Este documento tem como finalidade orientar a utilização do componente Detecção de Voz para fins de criação de bot de voz na funcionalidade Construtor de bot.

## Usabilidade

O componente Detecção de Voz é responsável por detectar a voz do usuário, ele possibilita a parametrização do tempo máximo que o usuário poderá ficar em silêncio e também o tempo máximo para detecção de voz, além de determinar o nível de silêncio para diferenciação de ruídos e voz. A URL da gravação da voz detectada será salvar na variável de armazenamento definida e estará no formato wav(pcm16).

O nível de silêncio padrão foi estabelecido de acordo com a análise com base nas gravações disponíveis na base Neppo, sendo o valor observado em 90% dos áudios.

Link da documentação freeSWITCH: <https://developer.signalwire.com/freeswitch/FreeSWITCH-Explained/Modules/mod-dptools/52168497/#:~:text=Description%E2%80%8B&text=The%20silence_thresh%20value%20is%20the,to%20be%20treated%20as%20silence> .

É recomendado informar o período de inatividade uma vez que a confirmação da detecção de voz poderá não ser reconhecida pelo bot.

![Imagem 1: É recomendado informar o período de inatividade uma vez que a confirmação da detecção de voz poderá não ser reconhecida…](https://ajuda.sankhya.com.br/hc/article_attachments/42637719602711)
