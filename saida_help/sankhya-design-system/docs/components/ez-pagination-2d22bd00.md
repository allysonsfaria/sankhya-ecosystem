---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-pagination/"
titulo: "Pagination"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-pagination/"
trilha: "Docs > Components > Components Doc > Ez Pagination"
---

# Pagination

Componente de Paginação reutilizável e flexível, que permite navegação entre páginas de forma
acessível e responsiva, com possibilidade de exibir ou ocultar o texto de paginação e personalizar seu conteúdo.

![Imagem 1: Componente de Paginação reutilizável e flexível, que permite navegação entre páginas de forma acessível e responsiva,…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

Atenção

Para que o componente funcione corretamente,
é necessário informar as seguintes propriedades:

- `totalItems`: quantidade total de itens a serem paginados.
- `pageSize`: quantidade de itens por página.

## Tipos de exibição

Existem dois tipos de exibição do componente, o tipo padrão e o tipo numérico.

> A propriedade type é do tipo string e aceita os valores `default` e `numeric`.

### Tipo padrão

É o tipo de exibição padrão do componente, no qual são exibidos os botões de navegação para a página anterior e próxima,
além do texto de paginação, informando a quantidade total de elementos.

![Imagem 2: É o tipo de exibição padrão do componente, no qual são exibidos os botões de navegação para a página anterior e…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Tipo numérico

É o tipo de paginação convencional, no qual são exibidos os números das páginas, além dos botões de navegação para a página anterior e próxima.

![Imagem 3: É o tipo de paginação convencional, no qual são exibidos os números das páginas, além dos botões de navegação para a…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Esconder informações de paginação

É possível ocultar o texto de paginação, que informa a quantidade total de elementos e a página atual, por meio da propriedade `hideInfoLabel`.

![Imagem 4: É possível ocultar o texto de paginação, que informa a quantidade total de elementos e a página atual, por meio da…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Limite de páginas

É possível definir a quantidade de páginas que devem ser exibidas no componente em tipo numérico,
por meio da propriedade `pageLimit`.

![Imagem 5: É possível definir a quantidade de páginas que devem ser exibidas no componente em tipo numérico, por meio da…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

Dica

O valor padrão da propriedade `pageLimit` é **10**, ou seja, serão exibidas **no máximo 10** opções de páginas.

## Eventos

### ezPageChange

Emitido ao realizar a troca de página, informando o número da página selecionada.

![Imagem 6: Emitido ao realizar a troca de página, informando o número da página selecionada.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---
