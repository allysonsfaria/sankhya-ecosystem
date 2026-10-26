---
id: "360043154854"
titulo: "Parceiro a 'X' dias sem negociar. Há liberação pendente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043154854-Parceiro-a-X-dias-sem-negociar-H%C3%A1-libera%C3%A7%C3%A3o-pendente"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:03:53Z"
rotulos: ["Configuração", "Eventos", "Parceiro", "Crédito", "Vendas", "Configure \"DIASSEMVENDA\" e \"Prazo p/ contato\"", "Parceiro sem negociar liberação pendente", "Venda bloqueada após tempo inativo"]
---

# Parceiro a 'X' dias sem negociar. Há liberação pendente

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16143150488343) MENSAGEM:**

Parceiro a 'X' dias sem negociar. Há liberação pendente.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16143118430231) SOLUÇÃO:**

A liberação de evento para esse caso é solicitada devido configurações abaixo:

- Evento 9 - Tempo Inativo:

![Imagem 3: Tela " Preferências " (Configurações/Avançado ) >> Chave " DIASSEMVENDA" - Nro de dias p/avisar que o cliente está sem…](https://ajuda.sankhya.com.br/hc/article_attachments/16143118432919) Tela **"[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834)"** (Configurações/Avançado) >> Chave "**DIASSEMVENDA"** - Nro de dias p/avisar que o cliente está sem venda:

- Tempo em dias, a partir do qual o sistema avisa que o cliente está sem negociar com a empresa.

![Imagem 4: Tempo em dias, a partir do qual o sistema avisa que o cliente está sem negociar com a empresa.](https://ajuda.sankhya.com.br/hc/article_attachments/12125828746519)

![Imagem 5: Tela " Parceiros " (Configurações/Cadastros) >>](https://ajuda.sankhya.com.br/hc/article_attachments/16143150492311) Tela **"[Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494)"** (Configurações/Cadastros) >>

- Aba "**Crédito** ":  Campo **"Prazo p/ contato**"

- Configure o tempo, em dias, para contato com o cliente.

![Imagem 6: Configure o tempo, em dias, para contato com o cliente.](https://ajuda.sankhya.com.br/hc/article_attachments/14686593742743)

(2)** EXEMPLO:**

Ao lançar uma Venda, sendo ultrapassado o tempo configurado acima, o sistema apresenta a mensagem "Cliente inativo desde...", bloqueia a Venda e é aberto o pop-up de solicitação de Liberação de Limites.

![Imagem 7: Caso não deseje trabalhar com a liberação do evento acima, deixe em branco o parâmetro " DIASSEMVENDA ."](https://ajuda.sankhya.com.br/hc/article_attachments/16143150496151) Caso não deseje trabalhar com a liberação do evento acima, deixe em branco o parâmetro "**DIASSEMVENDA**."

![Imagem 8: Caso essa configuração seja válida, libere o evento com o usuário/liberador configurado para tal.](https://ajuda.sankhya.com.br/hc/article_attachments/16143150498455) Caso essa configuração seja válida, libere o evento com o usuário/liberador configurado para tal.

**![Imagem 9: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/17874215877271) IMPORTANTE:**

A funcionalidade do parâmetro "**DIASSEMVENDA**", tanto para avisar, quanto para bloquear a venda para parceiros que não compram a X dias, não é aplicada em Tipos de Negociação à vista.

**![Imagem 10: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16143118445463) CAUSA:**

Ocorre quando o parceiro está há muito tempo sem efetuar negociação de compra/venda, causando a solicitação de liberação de limites, geralmente usado para revisar cadastro e/ou refazer análise de crédito.
