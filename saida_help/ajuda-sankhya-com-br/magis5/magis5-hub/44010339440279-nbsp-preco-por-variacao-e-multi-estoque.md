---
id: "44010339440279"
titulo: "&nbsp;Preço por Variação e Multi estoque no Mercado Livre"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010339440279--nbsp-Pre%C3%A7o-por-Varia%C3%A7%C3%A3o-e-Multi-estoque-no-Mercado-Livre"
trilha: "Magis5 > Magis5 HUB"
atualizado_em: "2026-10-05T18:35:58Z"
rotulos: ["sync_hc", "magis5", "magis5_215666079146", "sync_hash_20aa7e3de3e6"]
---

# &nbsp;Preço por Variação e Multi estoque no Mercado Livre

## Entenda neste guia, como funciona a nova funcionalidade do Mercado Live.

---

💡 O Mercado Livre está mudando a forma como os anúncios funcionam para deixar o seu catálogo mais parecido com grandes plataformas globais. Essa nova estrutura é chamada internamente de **MLBUs**, mas para você, vendedor, ela significa duas grandes novidades: **Preço por Variação e Estoque Multi Origem**

### O que muda na prática?

Antigamente, se você vendesse uma **"Camiseta"**, todas as variações dela (P, M, G, Amarela, Azul) precisavam ter obrigatoriamente o mesmo preço, o mesmo tipo de anúncio (Clássico ou Premium) e a mesma logística.

**Agora, cada variação funciona como um produto independente!**

#### Veja o que muda com essa nova funcionalidade:

- **Preços Diferentes:** Você pode cobrar mais barato por uma variação que está encalhada ou cobrar mais caro por aquele **tamanho/cor** que é o campeão de vendas.
- **Logística Mista:** Você pode enviar a variação que mais vende para o **Full** (FBM) e deixar as variações que vendem menos no seu próprio galpão (Mercado Envios / Coleta).
- **Promoções Direcionadas:** Crie descontos e campanhas de anúncios (Ads) apenas para a cor ou tamanho específico que você precisa girar no estoque.
- **Estoque Multi origem (Vários Galpões):** Se você tem estoque físico em mais de um lugar (ex: uma loja em SP e um galpão em MG), o Mercado Livre saberá disso. Quando o cliente comprar, o ML vai direcionar o pedido para sair do galpão mais próximo do comprador, barateando o frete e acelerando a entrega.

Para ilustrar os conceitos apresentados anteriormente, confira a seguir a comparação entre a publicação no modelo antigo e no modelo atual.

![userproduct](https://ajuda.sankhya.com.br/hc/article_attachments/44010327153815)

Pense na **"Família"** como um agrupador de produtos que possuem a mesma finalidade, mas apresentam características diferentes, como cor, tamanho, voltagem ou qualquer outra variação.

**Exemplo:** A família é **Camiseta Básica**.

No modelo **Endgame** do fluxograma, cada variação da família é representada por um **Produto Físico**. Além disso, um mesmo Produto Físico pode estar vinculado a mais de um anúncio.

#### Camiseta Amarela (Produto Físico 1)

Neste exemplo, a **Camiseta Amarela** corresponde ao **Produto Físico 1**. Para esse mesmo produto físico, existem dois anúncios cadastrados:

- **Anúncio Premium (Verde):** R$ 100,00.
- **Anúncio Clássico (Cinza):** R$ 90,00.

Embora os anúncios sejam diferentes, ambos estão vinculados ao mesmo Produto Físico (UP\_1). Isso significa que os dois representam exatamente a mesma camiseta amarela em estoque.

#### Camiseta Azul (Produto Físico 2)

Da mesma forma, a **Camiseta Azul** corresponde ao **Produto Físico 2**. Também existem dois anúncios vinculados a esse produto:

- **Anúncio Premium (Verde):** R$ 100,00.
- **Anúncio Clássico (Cinza):** R$ 90,00.

Assim como no exemplo anterior, os dois anúncios fazem referência ao mesmo Produto Físico, representando a mesma unidade de estoque.

### Entendendo a diferença entre MLBU e MLB

Ao trabalhar com integrações do Mercado Livre, você encontrará dois códigos importantes: **MLBU** e **MLB**.

A maneira mais simples de entender essa diferença é pensar em uma **prateleira de estoque** e em uma **vitrine de vendas**.

- **MLBU** representa o produto físico armazenado no estoque.
- **MLB** representa o anúncio publicado no Mercado Livre.

#### MLBU (Produto Físico)

O **MLBU** (também chamado de **Produto Físico** ou **User Product**) representa o item físico existente no seu estoque. Ele **não é um anúncio** e não é visualizado pelo comprador.

É nele que ficam armazenadas informações como:

- Código de barras (EAN);
- Peso e dimensões;
- Quantidade disponível em estoque;
- Demais informações relacionadas ao produto físico.

**Regra:** Cada produto físico possui um único **MLBU**.

**Exemplo:**

Se você possui **50 camisetas azuis** em estoque, existe **1 MLBU** representando essa variação, com saldo de **50 unidades**.

#### MLB (Anúncio)

O **MLB** é o anúncio publicado no Mercado Livre. É ele que aparece para o comprador durante a pesquisa e é por meio dele que as vendas são realizadas.

Cada anúncio pode possuir configurações próprias, como:

- Preço;
- Tipo do anúncio (Premium ou Clássico);
- Condições de frete;
- Parcelamento;
- Outras configurações comerciais.

**Regra:** Um mesmo Produto Físico **(MLBU)** pode estar vinculado a um ou vários anúncios **(MLB)**.
