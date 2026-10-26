---
id: "9934993524375"
titulo: "Quantidade atendida deve ser maior do que 0 (Zero)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9934993524375-Quantidade-atendida-deve-ser-maior-do-que-0-Zero"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T15:05:15Z"
rotulos: ["Produtos", "Configuração", "Central de Vendas", "CORE_E02727", "Quantidade relacionada não pode ser zero", "Mensagem aparece ao deixar quantidade vazia", "Informe sempre a quantidade ao relacionar notas", "Erro"]
---

# Quantidade atendida deve ser maior do que 0 (Zero)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16360917437719) MENSAGEM:**

[CORE\_E02727] Quantidade atendida deve ser maior do que 0 (Zero).

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16360917440279) SITUAÇÃO:**

Ao relacionar uma nota manualmente informando a quantidade atendida = 0 a mensagem é apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16360917440919) SOLUÇÃO:**

Sempre que relacionar notas com pedidos ou vice-versa, informe a quantidade que está sendo relacionada.

![Quantidade](https://ajuda.sankhya.com.br/hc/article_attachments/15698230463127)

![Imagem 5: Sempre que relacionar notas com pedidos ou vice-versa, informe a quantidade que está sendo relacionada.](https://ajuda.sankhya.com.br/hc/article_attachments/13997201339927)

Quando a opção Documentos relacionados é utilizada, o sistema abrirá o pop-up **"Documentos relacionados ao produto X".** Nele você poderá visualizar os documentos já lançados no sistema e que são ligados a um ou a todos os produtos do documento em questão.

Por exemplo, ao acessar esta opção estando-se posicionado em uma Nota de Venda que foi originada de um Pedido de Venda, este pedido de Pedido de Venda será apresentado neste pop-up na seção Documento de Origem.

Caso deseje verificar mais informações, acesse o artigo: [Central de Vendas | Grade Itens > Botão Outras Opções – Sankhya Gestão de Negócios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612374-Central-de-Vendas-Grade-Itens-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#documentosrelacionados)

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16360917441303)CAUSA:**

A mensagem ocorre pois não faz sentido 'relacionar' notas sem definir uma quantidade para o item. Este 'relacionamento' fica registrado na TGFVAR indicando que 'determinada nota' foi atendida através de outra nota na quantidade informada.'
