---
id: "https://gilded-nasturtium-6b64dd.netlify.app/blog/criacao-de-blocos"
titulo: "Criação de blocos"
url: "https://gilded-nasturtium-6b64dd.netlify.app/blog/criacao-de-blocos"
trilha: "Blog > Criacao De Blocos"
---

# Criação de blocos

29 de agosto de 2024 · Um minuto para ler

![André Luiz Barquet Moreira](https://gilded-nasturtium-6b64dd.netlify.app/img/authors/AndreMoreira.jpg)

André Luiz Barquet Moreira

Developer

## Introdução

O objetivo deste artigo, é mostrar como ficaria a criação de um CRUD utilizando apenas os componentes
do Ez-UI (como EzForm, EzGrid, EzViewStack, EzButton, EzChip, etc.) visando dar um exemplo de utilização em casos
onde não é possivel a utilização de componentes "Snk" no projeto que está sendo desenvolvido

### Detalhamento e considerações

Para realizar a impementação de um crud, é necessário instanciar um DataUnit, e a partir dele sobrescrever
os metodos de carregamento de dados (dataLoader), de carregamento dos metadados (metadataLoader), de salvar
registros (saveLoader) e de remoção de registros (removeLoader).

Para realizar a troca da visão do formulário para grade e vice versa, é necessário a utilização do EzViewStack.

Como neste cenário não é possível a utilização do SnkFilterBar, é necessário realizar a implementação manual, utilizando
o EzChip para os filtros, EzButton para os botão de inserir, cancelar e de configurações, além das verificações manuais de
qual botão deverá aparecer durante a inserção de um novo registro ou qual deverá aparecer no modo formulário/grade

### Exemplo de implementação

![Imagem 2: Exemplo de implementação](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---
