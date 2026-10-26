---
id: "42430272570647"
titulo: "Componente Discar"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430272570647-Componente-Discar"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T16:02:59Z"
rotulos: ["sync_hc", "neppo", "neppo_857997640", "sync_hash_32a293d61878"]
---

# Componente Discar

## Visão Geral

Este documento tem como finalidade orientar a utilização do componente Discar para fins de criação de bot de voz na funcionalidade Construtor de bot.

## Usabilidade

No componente de Discar, o usuário poderá informar um número de telefone ou variável que contenha o número. Ele é o componente responsável por iniciar a ligação, após atendida a ligação pelo usuário, passará para o próximo passo.

O usuário poderá desligar a ligação em qualquer momento da chamada, o componente de Discar possibilitará informar o direcionamento para o fluxo desejado.

Nele poderemos configurar redirecionamento também com base em outros estados da chamada, por exemplo quando estiver chamando(ringing), quando for retomada(unheld), quando estiver conectando(early) e também quando estiver em espera(held).

É recomendado informar o período de inatividade uma vez que a confirmação de atendimento ou encerramento pelo usuário poderá não ser reconhecida pelo bot.

Observação:

Somente será necessário informar o DDD do número caso seja diferente do DDD 34.

![Imagem 1: Somente será necessário informar o DDD do número caso seja diferente do DDD 34.](https://ajuda.sankhya.com.br/hc/article_attachments/42637701476631)
