---
id: "10264475533975"
titulo: "O pedido com número único já foi enviado para separação no WMS e não pode ter a ordem de carga alterada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10264475533975-O-pedido-com-n%C3%BAmero-%C3%BAnico-j%C3%A1-foi-enviado-para-separa%C3%A7%C3%A3o-no-WMS-e-n%C3%A3o-pode-ter-a-ordem-de-carga-alterada"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T15:04:04Z"
rotulos: ["Ordem de Carga", "WMS", "Expedição", "CORE_E05075", "Não é possível alterar a ordem de carga", "Cancele expedição para nova OC", "Pedido enviado para WMS", "Erro"]
---

# O pedido com número único já foi enviado para separação no WMS e não pode ter a ordem de carga alterada

(1)** MENSAGEM:**

[CORE\_E05075] O pedido com número único já foi enviado para separação no WMS e não pode ter a ordem de carga alterada.

(2)** CAUSA:**

Ocorre quando se tenta alterar a ordem de carga de um pedido já enviado para separação no WMS.

(3)** SOLUÇÃO:**

Não é possível alterar uma OC de um pedido que já foi enviado para expedição.

Caso seja preciso alterar a ordem de carga, primeiro acesse a tela **Expedição de Mercadorias** (Caminho de aceso à tela: WMS » Rotinas » Expedição de Mercadorias) e cancele a expedição da OC do pedido enviado. Em seguida, vá até a tela **Formação de Carga** (Caminho de acesso à tela: Comercial » Rotinas » Ordem de Carga » Formação de Carga) e vincule uma nova OC.

![Imagem 1: Caso seja preciso alterar a ordem de carga, primeiro acesse a tela Expedição de Mercadorias (Caminho de aceso à tela:…](https://ajuda.sankhya.com.br/hc/article_attachments/10287957086743)
