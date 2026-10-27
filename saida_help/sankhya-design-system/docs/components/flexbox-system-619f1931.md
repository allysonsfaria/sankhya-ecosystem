---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/layout-doc/flexbox-system/"
titulo: "Flexbox System"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/layout-doc/flexbox-system/"
trilha: "Docs > Components > Layout Doc > Flexbox System"
---

# Flexbox System

CSS Flexbox é um sistema de layout unidimensional que você pode usar para criar um layout de eixo de linha ou coluna.
É um módulo em vez de uma única propriedade porque inclui várias propriedades, algumas das quais são para o container
flexível (elemento pai) e outras para os itens flexíveis (elementos filhos). Este módulo de layout permite que o
container altere a largura/altura (e a ordem) de seus itens para se adequar melhor ao espaço disponível e suportar
todos os dispositivos de exibição e tamanhos de tela.

## Como funciona

Para utilizar o flexbox, basta inserir a classe CSS `ez-flex`
no elemento que desejar adotar o comportamento flexível, conforme exemplo a seguir:

![Imagem 1: Para utilizar o flexbox, basta inserir a classe CSS ez-flex no elemento que desejar adotar o comportamento flexível,…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Direção

Por padrão os itens internos do eixo principal são apresentados em linha, da esquerda para a direita,
mas é possível alterar essas direções conforme será apresentado a seguir.

### Linha reversa

> Propriedade do flexbox utilizada: **row-reverse**

A classe CSS `ez-flex--row-reverse`, altera a direção dos itens internos, os mantendo em linha,
mas os apresentando da direita para a esquerda, conforme o exemplo a seguir:

![Imagem 2: A classe CSS ez-flex--row-reverse , altera a direção dos itens internos, os mantendo em linha, mas os apresentando da…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Coluna

> Propriedade do flexbox utilizada: **column**

A classe CSS `ez-flex--column`, altera a direção dos itens internos, os apresentando em coluna,
de cima para baixo, conforme o exemplo a seguir:

![Imagem 3: A classe CSS ez-flex--column , altera a direção dos itens internos, os apresentando em coluna, de cima para baixo,…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Coluna reversa

> Propriedade do flexbox utilizada: **column-reverse**

A classe CSS `ez-flex--column-reverse`, altera a direção dos itens internos, os apresentando em coluna,
mas mudando a ordem destes elementos para de baixo para cima, conforme o exemplo a seguir:

![Imagem 4: A classe CSS ez-flex--column-reverse , altera a direção dos itens internos, os apresentando em coluna, mas mudando a…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Quebra de linha

> Propriedade do flexbox utilizada: **wrap**

Dependendo da quantidade de itens internos no eixo principal, tem-se a possibilidade de
quebrar o layout (Utilizando a classe CSS `ez-flex--nowrap`, mantém o padrão, para que mantenha todos
os itens continuem na mesma linha), conforme exemplo a seguir:

![Imagem 5: Dependendo da quantidade de itens internos no eixo principal, tem-se a possibilidade de quebrar o layout (Utilizando a…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

Utilizando a classe CSS `ez-flex--wrap`, o problema da quebra de layout é resolvido ao
quebrar a linha entre os itens internos, conforme o exemplo a seguir:

![Imagem 6: Utilizando a classe CSS ez-flex--wrap , o problema da quebra de layout é resolvido ao quebrar a linha entre os itens…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

Utilizando a classe CSS `ez-flex--wrap-reverse` é possível aplicar a quebra da linha
entre os itens internos de forma reversa, conforme o exemplo a seguir:

![Imagem 7: Utilizando a classe CSS ez-flex--wrap-reverse é possível aplicar a quebra da linha entre os itens internos de forma…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Alinhamento justificado

> Propriedade do flexbox utilizada: **justify-content**

A propriedade `justify-content` define o alinhamento justificado dos itens flexíveis.
Essa propriedade possui seis valores principais que executam funções individuais,
todas destinadas a exercer algum controle sobre o alinhamento dos itens flexíveis,
a seguir será apresentado cada uma delas.

### Alinhar no início

> Propriedade do flexbox utilizada: **flex-start**

Este é o alinhamento padrão no qual os itens internos são posicionados no início do eixo principal,
mesmo que já seja o valor padrão, para casos que precise aplicá-lo, basta utilizar a classe CSS
`ez-flex--justify-start`, conforme o exemplo a seguir:

![Imagem 8: Este é o alinhamento padrão no qual os itens internos são posicionados no início do eixo principal, mesmo que já seja o…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Alinhar no final

> Propriedade do flexbox utilizada: **flex-end**

Este é o oposto do **flex-start**, pois os itens internos são posicionados no final do eixo principal.
Para aplicá-lo, basta utilizar a classe CSS `ez-flex--justify-end`, conforme o exemplo a seguir:

![Imagem 9: Este é o oposto do flex-start , pois os itens internos são posicionados no final do eixo principal. Para aplicá-lo,…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Alinhar ao centro

> Propriedade do flexbox utilizada: **center**

Este utilitário posiciona os itens internos ao centro do eixo principal. Para aplicá-lo,
basta utilizar a classe CSS `ez-flex--justify-center`, conforme o exemplo a seguir:

![Imagem 10: Este utilitário posiciona os itens internos ao centro do eixo principal. Para aplicá-lo, basta utilizar a classe CSS…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Espaço entre elementos

> Propriedade do flexbox utilizada: **space-between**

Este utilitário distribui os itens internos, começando e terminando nas extremidades do eixo principal.
Para aplicá-lo, basta utilizar a classe CSS `ez-flex--justify-between`, conforme o exemplo a seguir:

![Imagem 11: Este utilitário distribui os itens internos, começando e terminando nas extremidades do eixo principal. Para aplicá-lo,…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Espaço ao redor dos elementos

> Propriedade do flexbox utilizada: **space-around**

Essa classe CSS distribui, de acordo com o eixo principal, os itens internos com um espaço ao redor deles
(esquerda, direita, inferior e superior). Porém, os espaços inferior e superior não serão os mesmos
da direita e da esquerda, pois estes são definidos pela soma de ambos. Para aplicá-lo, basta utilizar
a classe CSS `ez-flex--justify-around`, conforme o exemplo a seguir:

![Imagem 12: Essa classe CSS distribui, de acordo com o eixo principal, os itens internos com um espaço ao redor deles (esquerda,…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Espaço uniforme ao redor dos elementos

> Propriedade do flexbox utilizada: **space-evenly**

Essa classe CSS distribui uniformemente, de acordo com o eixo principal, os itens internos criando um espaçamento exato ao redor deles
(esquerda, direita, inferior e superior). Para aplicá-lo, basta utilizar a classe CSS `ez-flex--justify-evenly`, conforme o exemplo a seguir:

![Imagem 13: Essa classe CSS distribui uniformemente, de acordo com o eixo principal, os itens internos criando um espaçamento exato…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Alinhamento de itens

> Propriedade do flexbox utilizada: **align-items**

A propriedade `align-items` alinha os itens internos dentro do eixo principal com base na direção definida (linha ou coluna).

### Elementos esticados

> Propriedade do flexbox utilizada: **stretch**

Este é o alinhamento padrão no qual os itens internos são esticados para preencher o eixo principal.
Mesmo que já seja o valor padrão, para casos que precise aplicá-lo,
basta utilizar a classe CSS `ez-flex--align-items-stretch`, conforme o exemplo a seguir:

![Imagem 14: Este é o alinhamento padrão no qual os itens internos são esticados para preencher o eixo principal. Mesmo que já seja…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Alinhar no início

> Propriedade do flexbox utilizada: **flex-start**

Neste alinhamento os itens internos são posicionados no início do eixo principal. Para aplicá-lo,
basta utilizar a classe CSS `ez-flex--align-items-start`, conforme o exemplo a seguir:

![Imagem 15: Neste alinhamento os itens internos são posicionados no início do eixo principal. Para aplicá-lo, basta utilizar a…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Alinhar no final

> Propriedade do flexbox utilizada: **flex-end**

Este é o oposto do **flex-start**, pois os itens internos são posicionados no final do eixo principal.
Para aplicá-lo, basta utilizar a classe CSS `ez-flex--align-items-end`, conforme o exemplo a seguir:

![Imagem 16: Este é o oposto do flex-start , pois os itens internos são posicionados no final do eixo principal. Para aplicá-lo,…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Alinhar ao centro

> Propriedade do flexbox utilizada: **center**

Essa classe CSS posiciona os itens internos ao centro do eixo principal. Para aplicá-lo,
basta utilizar a classe CSS `ez-flex--align-items-center`, conforme o exemplo a seguir:

![Imagem 17: Essa classe CSS posiciona os itens internos ao centro do eixo principal. Para aplicá-lo, basta utilizar a classe CSS…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Alinhar à linha de base

> Propriedade do flexbox utilizada: **baseline**

Essa classe CSS posiciona os itens internos ao centro no sentido de que suas linhas de base estão alinhadas.
Para aplicá-lo, basta utilizar a classe CSS `ez-flex--align-items-baseline`, conforme o exemplo a seguir:

![Imagem 18: Essa classe CSS posiciona os itens internos ao centro no sentido de que suas linhas de base estão alinhadas. Para…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Alinhamento de conteúdo

> Propriedade do flexbox utilizada: **align-content**

A propriedade `align-content` posiciona o grupo de itens internos dentro do eixo principal com
base na direção definida (linha ou coluna).

### Alinhar no início

> Propriedade do flexbox utilizada: **flex-start**

Este é o alinhamento padrão no qual o grupo de itens internos é posicionado no início do eixo principal,
mesmo que já seja o valor padrão, para casos que precise aplicá-lo, basta utilizar a classe CSS
`ez-flex--align-content-start`. Para demonstração deste utilitário, também será aplicado o
**flex-wrap** no eixo principal, conforme o exemplo a seguir:

![Imagem 19: Este é o alinhamento padrão no qual o grupo de itens internos é posicionado no início do eixo principal, mesmo que já…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Alinhar no final

> Propriedade do flexbox utilizada: **flex-end**

Este é o oposto do **flex-start**, pois o grupo de itens internos são posicionados no final do eixo principal.
Para aplicá-lo, basta utilizar a classe CSS `ez-flex--align-content-end`. Para demonstração deste utilitário,
também será aplicado o **flex-wrap** no eixo principal, conforme o exemplo a seguir:

![Imagem 20: Este é o oposto do flex-start , pois o grupo de itens internos são posicionados no final do eixo principal. Para…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Espaço entre os grupos de elementos

> Propriedade do flexbox utilizada: **space-between**

Essa classe CSS distribui os grupos de itens internos, começando e terminando nas extremidades do eixo principal.
Para aplicá-lo, basta utilizar a classe CSS `ez-flex--align-content-between`. Para demonstração deste utilitário,
também será aplicado o **flex-wrap** no eixo principal, conforme o exemplo a seguir:

![Imagem 21: Essa classe CSS distribui os grupos de itens internos, começando e terminando nas extremidades do eixo principal. Para…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Espaço ao redor dos grupos de elementos

> Propriedade do flexbox utilizada: **space-around**

Essa classe CSS distribui, de acordo com o eixo principal, os grupos de itens internos com um espaço ao redor deles
(esquerda, direita, inferior e superior). Porém, os espaços inferior e superior não serão os mesmos
da direita e da esquerda, pois estes são definidos pela soma de ambos. Para aplicá-lo, basta utilizar
a classe CSS `ez-flex--align-content-around`. Para demonstração dessa classe,
também será aplicado o **flex-wrap** no eixo principal, conforme o exemplo a seguir:

![Imagem 22: Essa classe CSS distribui, de acordo com o eixo principal, os grupos de itens internos com um espaço ao redor deles…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Ordenação de elemento

> Propriedade do flexbox utilizada: **order**

A propriedade `order` posiciona um item interno dentro do eixo principal de acordo com o prefixo utilizado.

### Posicionar no início

Para posicionar um elemento específico no início do eixo principal basta utilizar a classe CSS
`ez-flex-item--first`, conforme o exemplo a seguir:

![Imagem 23: Para posicionar um elemento específico no início do eixo principal basta utilizar a classe CSS ez-flex-item--first ,…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Posicionar no final

Para posicionar um elemento específico no final do eixo principal basta utilizar a classe CSS
`ez-flex-item--last`, conforme o exemplo a seguir:

![Imagem 24: Para posicionar um elemento específico no final do eixo principal basta utilizar a classe CSS ez-flex-item--last ,…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Alinhamento de elemento

> Propriedade do flexbox utilizada: **align-self**

A propriedade `align-self` alinha um item específico dentro do eixo principal com base na direção definida (linha ou coluna).

### Elemento esticado

> Propriedade do flexbox utilizada: **stretch**

Este é o alinhamento padrão no qual um item específico é esticado para preencher o eixo principal.
Mesmo que já seja o valor padrão, para casos que precise aplicá-lo,
basta utilizar a classe CSS `ez-flex-item--align-stretch`. Para demonstração deste utilitário,
também será aplicado o **flex-start** no eixo principal, conforme o exemplo a seguir:

![Imagem 25: Este é o alinhamento padrão no qual um item específico é esticado para preencher o eixo principal. Mesmo que já seja o…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Alinhar no início

> Propriedade do flexbox utilizada: **flex-start**

Neste alinhamento um item específico é posicionado no início do eixo principal. Para aplicá-lo,
basta utilizar a classe CSS `ez-flex-item--align-start`, conforme o exemplo a seguir:

![Imagem 26: Neste alinhamento um item específico é posicionado no início do eixo principal. Para aplicá-lo, basta utilizar a classe…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Alinhar no final

> Propriedade do flexbox utilizada: **flex-end**

Este é o oposto do **flex-start**, pois o item específico é posicionado no final do eixo principal.
Para aplicá-lo, basta utilizar a classe CSS `ez-flex-item--align-end`, conforme o exemplo a seguir:

![Imagem 27: Este é o oposto do flex-start , pois o item específico é posicionado no final do eixo principal. Para aplicá-lo, basta…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Alinhar ao centro

> Propriedade do flexbox utilizada: **center**

Este utilitário posiciona o item específico ao centro do eixo principal. Para aplicá-lo,
basta utilizar a classe CSS `ez-flex-item--align-center`, conforme o exemplo a seguir:

![Imagem 28: Este utilitário posiciona o item específico ao centro do eixo principal. Para aplicá-lo, basta utilizar a classe CSS…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Alinhar à linha de base

> Propriedade do flexbox utilizada: **baseline**

Este utilitário posiciona o item específico ao centro no sentido de que suas linhas de base estão alinhadas.
Para aplicá-lo, basta utilizar a classe CSS `ez-flex-item--align-baseline`, conforme o exemplo a seguir:

![Imagem 29: Este utilitário posiciona o item específico ao centro no sentido de que suas linhas de base estão alinhadas. Para…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Elemento flexível

> Propriedade do flexbox utilizada: **flex**

A propriedade `flex` dimensiona um item específico para ocupar um determinado espaço disponível dentro do eixo principal.

### Dimensionamento automático

> Propriedade do flexbox utilizada: **auto**

Essa classe CSS dimensiona um item específico para ocupar todo o espaço disponível dentro do eixo principal.
Para aplicá-lo, basta utilizar a classe CSS `ez-flex-item--auto`, conforme o exemplo a seguir:

![Imagem 30: Essa classe CSS dimensiona um item específico para ocupar todo o espaço disponível dentro do eixo principal. Para…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---
