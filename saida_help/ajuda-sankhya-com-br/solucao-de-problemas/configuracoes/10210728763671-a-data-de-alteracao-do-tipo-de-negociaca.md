---
id: "10210728763671"
titulo: "A data de alteração do Tipo de Negociação não pode ser maior que a data de movimento do modelo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10210728763671-A-data-de-altera%C3%A7%C3%A3o-do-Tipo-de-Negocia%C3%A7%C3%A3o-n%C3%A3o-pode-ser-maior-que-a-data-de-movimento-do-modelo"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:04:18Z"
rotulos: ["Configuração", "XML", "Nota Fiscal", "CORE_E00294", "Modelo de Nota", "Data de Movimento", "Erro", "Modelo de Notas"]
---

# A data de alteração do Tipo de Negociação não pode ser maior que a data de movimento do modelo

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18790396531735) MENSAGEM:**

[CORE\_E00294] A data de alteração do Tipo de Negociação não pode ser maior que a data de movimento do modelo.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18790396535959) SITUAÇÃO:**

Ao tentar ajustar o modelo de nota para a importação do XML a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18790406294039) CAUSA:**

Ocorre quando o modelo de nota fica com data inferior a data de criação do tipo de negociação.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18790406298647) SOLUÇÃO:**

O Sistema trás no campo data de negociação a data da criação do tipo de negociação, e esta não pode ser alterada. Portanto, mude a data de movimento do modelo na tela **Modelo de Notas e Pedidos** (Caminho de acesso à tela: Comercial » Consulta » Modelo de Notas e Pedidos).

Campo: Dt. do Movimento (inserir a data atual)

![Imagem 5: O Sistema trás no campo data de negociação a data da criação do tipo de negociação, e esta não pode ser alterada.…](https://ajuda.sankhya.com.br/hc/article_attachments/18790406305559)
