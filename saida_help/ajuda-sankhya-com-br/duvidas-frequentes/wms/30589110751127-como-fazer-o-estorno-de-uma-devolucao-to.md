---
id: "30589110751127"
titulo: "Como fazer o estorno de uma devolução total de nota gerada apartir de um recebimento?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30589110751127-Como-fazer-o-estorno-de-uma-devolu%C3%A7%C3%A3o-total-de-nota-gerada-apartir-de-um-recebimento"
trilha: "Dúvidas Frequentes > WMS"
atualizado_em: "2026-10-22T13:47:45Z"
rotulos: ["Configuração", "WMS", "Recebimento", "TOP", "Estoque", "Devolução", "Passos para resolver", "Razão do erro", "Detalhe do erro", "estorno de uma devolução total de nota", "recebimento concluído automaticamente"]
---

# Como fazer o estorno de uma devolução total de nota gerada apartir de um recebimento?

Quando ocorre a devolução total de uma nota o recebimento é concluído. Caso tenha sido uma ação indevida e os itens deveriam ter sido armazenados e tratados divergência a parte, temos a possiblidade através do sistema de fazer o estorno dessa devolução. Para isso, siga os passos abaixo:

![Imagem 1: Crie uma Top com tipo de movimento C- Compra e na aba "Estoque" , configure o campo "Atualização de estoque" como…](https://ajuda.sankhya.com.br/hc/article_attachments/30615709550103) Crie uma Top com tipo de movimento C- Compra e na aba **"Estoque"**, configure o campo **"Atualização de estoque"** como **"Nenhuma"**.

**Observação:** como a nota de compra já foi confirmada na conferência, o estoque já está confirmado no comercial, faltando apenas entrar no estoque do WMS.

![Imagem 2: Observação: como a nota de compra já foi confirmada na conferência, o estoque já está confirmado no comercial, faltando…](https://ajuda.sankhya.com.br/hc/article_attachments/30615375780503)

![Imagem 3: Na aba "WMS" , escolha a opção " Sim " no campo "Permitir confirmação antes do envio para o WMS" . No campo…](https://ajuda.sankhya.com.br/hc/article_attachments/30615767518359) Na aba **"WMS"**, escolha a opção **"Sim"**no campo **"Permitir confirmação antes do envio para o WMS"**. No campo **"Endereçamento no WMS"** marque **"Automática"** e em **"Atualização no WMS"** selecione **"Entrar".**

![Imagem 4: Acesse a tela "Modelo de notas e pedidos" (Comercial » Consulta » Modelo de Notas e Pedidos) e crie um modelo para a…](https://ajuda.sankhya.com.br/hc/article_attachments/30615756704407) Acesse a tela **"Modelo de notas e pedidos"** (Comercial » Consulta » Modelo de Notas e Pedidos) e crie um modelo para a empresa do recebimento do WMS com a TOP cadastrada anteriormente.

![Imagem 5: Acesse a tela Preferências da empresa , na aba "WMS" , em Movimentações e Armazenagem , no campo "Modelo Estorno WMS -…](https://ajuda.sankhya.com.br/hc/article_attachments/30615756705431) Acesse a tela **Preferências da empresa**, na aba **"WMS"**, em **Movimentações e Armazenagem**, no campo **"Modelo Estorno WMS - Dev. Compra"** inclua o modelo cadastrado anteriormente.

![Imagem 6: Acesse o portal de compras, na nota de devolução que foi gerada a partir do recebimento, clique na lixeira para excluir…](https://ajuda.sankhya.com.br/hc/article_attachments/30615904502807) Acesse o portal de compras, na nota de devolução que foi gerada a partir do recebimento, clique na lixeira para excluir a nota e informe que deseja gerar um recebimento das mercadorias. Encaminhe para uma doca de entrada e realize o processo de conferência do recebimento e armazenagem dos produtos.

[GIF animado: Imagem 7: Acesse o portal de compras, na nota de devolução que foi gerada a partir do recebimento, clique na lixeira para excluir…](https://ajuda.sankhya.com.br/hc/article_attachments/30616287078807)

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/30589110746775)CAUSA:**

Ocorre quando uma devolução total da nota é gerada de forma indevida na tratativa de divergência de um recebimento e existe a necessidade de receber as mercadorias no WMS, porém o recebimento já está como concluído.
