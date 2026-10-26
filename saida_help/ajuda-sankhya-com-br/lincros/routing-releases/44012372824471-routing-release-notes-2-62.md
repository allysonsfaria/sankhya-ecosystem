---
id: "44012372824471"
titulo: "[Routing] - Release Notes 2.62"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012372824471--Routing-Release-Notes-2-62"
trilha: "Lincros > Releases (Atualizações) > Routing (Releases)"
atualizado_em: "2026-10-05T19:26:42Z"
rotulos: ["sync_hc", "lincros", "lincros_13433689", "sync_hash_9d3a71628c6c"]
---

# [Routing] - Release Notes 2.62

![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/44012345666327)

## Melhorias:

## Novo campo na API consultasessao (V2)

Adicionamos o campo "Observação do Pedido" na API /api/consultaSessao/v2, proporcionando mais informações sobre cada pedido dentro da sua sessão.

## Novo parâmetro 'Notificar transportadora nas rotas terceirizadas/fracionadas.'

Adicionado um novo parâmetro no cadastro de depósito: "**Notificar transportadora nas rotas terceirizadas/fracionadas**."

Esse parâmetro permite definir se as ordens de coleta dessas rotas devem ou não notificar a transportadora via TMS.

Quando desativado, o sistema envia a ordem sem notificação, mantendo-a aberta para edições futuras.

Com isso, evitamos comunicações indevidas e retrabalho operacional.

**Importante:** o novo comportamento aplica-se **somente a rotas com atividades do tipo fracionada ou terceirizada.**

![Imagem 2: Importante: o novo comportamento aplica-se somente a rotas com atividades do tipo fracionada ou terceirizada.](https://ajuda.sankhya.com.br/hc/article_attachments/44012354132119)
