---
id: "42430272083095"
titulo: "Componente Receber chamada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430272083095-Componente-Receber-chamada"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T16:02:55Z"
rotulos: ["sync_hc", "neppo", "neppo_857997589", "sync_hash_13d375179f6a"]
---

# Componente Receber chamada

## Visão Geral

Este documento tem como finalidade orientar a utilização do componente Receber Chamada para fins de criação de bot de voz na funcionalidade Construtor de bot.

## Usabilidade

O componente de Receber Chamada deve ser o primeiro componente do fluxo para um bot receptivo de voz. Ele é o componente responsável por atender a ligação, após atendida a ligação, passará para o próximo passo.

O usuário poderá desligar a ligação em qualquer momento da chamada, o componente de Receber Chamada possibilitará informar o direcionamento para o fluxo desejado.

Nele poderemos configurar redirecionamento também com base em outros estados da chamada, por exemplo quando estiver chamando(ringing), quando for retomada(unheld), quando estiver conectando(early) e também quando estiver em espera(held).

Link da documentação do FreeSWITCH: <https://developer.signalwire.com/freeswitch/FreeSWITCH-Explained/Dialplan/Call-States_32178212/>

![Imagem 1: Link da documentação do FreeSWITCH:…](https://ajuda.sankhya.com.br/hc/article_attachments/42637726188183)
