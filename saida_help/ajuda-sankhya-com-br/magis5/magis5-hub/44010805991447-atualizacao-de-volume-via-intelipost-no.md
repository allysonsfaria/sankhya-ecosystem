---
id: "44010805991447"
titulo: "Atualização de volume via Intelipost no Magis5 HUB"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010805991447-Atualiza%C3%A7%C3%A3o-de-volume-via-Intelipost-no-Magis5-HUB"
trilha: "Magis5 > Magis5 HUB"
atualizado_em: "2026-10-05T18:47:37Z"
rotulos: ["sync_hc", "magis5", "magis5_208645657268", "sync_hash_bc076b8e5c90"]
---

# Atualização de volume via Intelipost no Magis5 HUB

## Entenda, neste artigo, como funciona o processo de atualização de volumes para a Intelipost dentro do Magis5 HUB.

![Imagem 1: Entenda, neste artigo, como funciona o processo de atualização de volumes para a Intelipost dentro do Magis5 HUB.](https://ajuda.sankhya.com.br/hc/article_attachments/44010806116759)![Imagem 2: Entenda, neste artigo, como funciona o processo de atualização de volumes para a Intelipost dentro do Magis5 HUB.](https://ajuda.sankhya.com.br/hc/article_attachments/44010827748759)![Imagem 3: Entenda, neste artigo, como funciona o processo de atualização de volumes para a Intelipost dentro do Magis5 HUB.](https://ajuda.sankhya.com.br/hc/article_attachments/44010827819671)![Imagem 4: Entenda, neste artigo, como funciona o processo de atualização de volumes para a Intelipost dentro do Magis5 HUB.](https://ajuda.sankhya.com.br/hc/article_attachments/44010812572183)![https://ajuda.magis5.com.br/magis5-hub#expedi%C3%A7%C3%A3o](https://ajuda.sankhya.com.br/hc/article_attachments/44010818836119)![Imagem 6: Entenda, neste artigo, como funciona o processo de atualização de volumes para a Intelipost dentro do Magis5 HUB.](https://ajuda.sankhya.com.br/hc/article_attachments/44010812728087)![Imagem 7: Entenda, neste artigo, como funciona o processo de atualização de volumes para a Intelipost dentro do Magis5 HUB.](https://ajuda.sankhya.com.br/hc/article_attachments/44010828201111)

---

- A funcionalidade permite que a quantidade de volumes de um pedido seja automaticamente ajustada com base nas informações retornadas durante a cotação de frete realizada pela **Intelipost**, garantindo mais precisão e automatização no processo logístico.

### Como configurar a atualização de volume no Magis5 HUB

Feito login no Magis5, acesse **"Configurações", "Integrações"**e por fim **"Logística"

![Captura de tela 2026-03-03 152441](https://ajuda.sankhya.com.br/hc/article_attachments/44010806641175)**

Dentro de **"Integrações"** clique em **"Editar"** na integração logística Intelipost que deseja configurar.

![Captura de tela 2026-03-03 153233](https://ajuda.sankhya.com.br/hc/article_attachments/44010841289495)

Ative a opção **"Utilizar a quantidade de volumes informada pela Intelipost"**

![Captura de tela 2026-03-03 154331](https://ajuda.sankhya.com.br/hc/article_attachments/44010828580503)

- Ao realizar a cotação por meio da integração com a **Intelipost**, o **Magis5 HUB** identifica automaticamente os volumes e utiliza a quantidade de itens da lista para preencher as informações correspondentes na Nota Fiscal.

⚠️ **IMPORTANTE:** A cotação de frete é realizada exclusivamente para possibilitar a criação do pedido de envio na Intelipost. O Magis5 HUB **não utiliza essa cotação para calcular ou exibir valores de frete nos anúncios dos marketplaces ao comprador.**

Após ativar a opção clique em **"Salvar"** no canto superior da tela.

![Captura de tela 2026-03-03 155649](https://ajuda.sankhya.com.br/hc/article_attachments/44010841447191)

💡 Para que a Intelipost retorne a quantidade de volumes na cotação de frete, é **obrigatório** que estejam configuradas as embalagens e associe os produtos a essas embalagens diretamente na plataforma da Intelipost.

**Essa configuração deve ser realizada exclusivamente dentro da própria Intelipost.**

- A quantidade de volumes é definida exclusivamente pela contagem dos itens da lista de volumes retornada na cotação.
- Não é realizado tratamento individual dos detalhes de cada volume **(dimensões, peso etc.).**
- A atualização do campo volume na Nota Fiscal só ocorre se a configuração [("Utilizar a quantidade de volumes informada pela Intelipost")](https://ajuda.sankhya.com.br/hc/pt-br/articles/44010805991447-Atualiza%C3%A7%C3%A3o-de-volume-via-Intelipost-no-Magis5-HUB#Volumes) estiver habilitada.
