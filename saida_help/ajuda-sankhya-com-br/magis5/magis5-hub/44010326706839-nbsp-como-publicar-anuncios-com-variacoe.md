---
id: "44010326706839"
titulo: "&nbsp;Como Publicar Anúncios com Variações na Leroy Merlin"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010326706839--nbsp-Como-Publicar-An%C3%BAncios-com-Varia%C3%A7%C3%B5es-na-Leroy-Merlin"
trilha: "Magis5 > Magis5 HUB"
atualizado_em: "2026-10-05T18:35:55Z"
rotulos: ["sync_hc", "magis5", "magis5_221690071809", "sync_hash_692efeec2196"]
---

# &nbsp;Como Publicar Anúncios com Variações na Leroy Merlin

## Veja neste artigo como realizar a publicação de anúncios com variações para a Leroy utilizando o Magis5 HUB.

---

Para publicar anúncios com variações na Leroy Merlin através do Magis5, é obrigatório preencher o atributo **código variante** em todos os produtos que farão parte dessa variação.

### O que é o código variante e como ele funciona?

O atributo **codigo variante** funciona como um código da família do produto. Ele serve para avisar a Leroy Merlin que diferentes SKUs (produtos filhos) pertencem, na verdade, ao mesmo produto principal (produto pai).

Para que o canal entenda que os produtos são variações de um mesmo anúncio, todos os SKUs daquela família precisam ser enviados com o **exato mesmo valor** no atributo **variant-code.**

.![Imagem 1: .](https://ajuda.sankhya.com.br/hc/article_attachments/44010373517719)

#### Exemplo Prático:

Imagine que você vende um modelo de chuveiro que possui duas voltagens diferentes **(110V e 220V)**. No sistema, eles são dois **SKUs diferentes**, mas na Leroy Merlin eles devem aparecer na mesma tela para o cliente escolher.

 Veja como os atributos devem ser preenchidos:

| SKU do Produto (Filho) | Tensão Elétrica (A Variação) | Atributo: codigo variante |
| --- | --- | --- |
| **CH-220** | 220V | **CH** |
| **CH-110** | 110V | **CH** |

No exemplo acima, a Leroy Merlin lerá o código "**CH"** e entenderá automaticamente que o **SKU CH-220 e o SKU CH-110** são o mesmo chuveiro, agrupando-os no mesmo anúncio com a opção de escolha de voltagem.

⚠️ **Atenção**

- **Digitação Exata:** O **codigo variante** diferencia letras maiúsculas, minúsculas e espaços. O código **"CH"**, **"ch"** e **"CH"** (com espaço) serão lidos como produtos diferentes. Padronize a escrita!
- **Atributos Base Iguais:** Para que a união dê certo, os produtos que compartilham o mesmo **codigo variante** devem ter características base idênticas (como Marca, Modelo, Descrição e Imagem Principal), divergindo apenas no atributo da variação **(ex: Voltagem)**.
- **Ausência do Código:** Se você enviar um produto sem o**codigo variante**, a Leroy Merlin o tratará como um anúncio simples, sem variações.

### Publicando anuncio no Magis5 HUB

Após realizar o mapeamento do atributo **código agrupador**, você pode escolher a melhor forma de publicar o seu anúncio na Leroy Merlin através de um dos fluxos abaixo: 

- [Publicar anúncios a partir da opção "Novos anúncios de um produto"](https://ajuda.sankhya.com.br/publicar-anuncios-a-partir-da-opcao-novos-anuncios-de-um-produto?hsLang=pt-br)
- **[Como publicar anúncios no Magis5 HUB](https://ajuda.sankhya.com.br/anuncios/como-publicar-anuncios?hsLang=pt-br)**

Assim que realizar a publicação, seu anúncio será enviado para a **Leroy Merlin** já estruturado com as variações.
