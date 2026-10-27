---
id: "https://gilded-nasturtium-6b64dd.netlify.app/blog/link-entre-projetos"
titulo: "Link entre projetos"
url: "https://gilded-nasturtium-6b64dd.netlify.app/blog/link-entre-projetos"
trilha: "Blog > Link Entre Projetos"
---

# Link entre projetos

14 de julho de 2022 · 3 min para ler

![Leonardo Jorge](https://gilded-nasturtium-6b64dd.netlify.app/img/authors/LeonardoJorge.png)

Leonardo Jorge

Software Architect

## O que é?

A funcionalidade de `link` é um recurso do npm que permite a criação de link simbólicos entre as dependências do `node_modules` e os nossos projetos locais.
Isso é bem útil quando precisamos fazer alterações em projetos do design system (ex: core, ez-ui, sankhya-blocks) e essas alterações já sejam refletidas em um projeto React, para que seja possivel realizar testes das alterações e etc.
Porém, gerenciar manualmente o link dessas dependências em ambiente de desenvolvimento pode ser muito trabalhoso. Por isso cada projeto tem seu próprio script de link para facilitar nosso trabalho.

## Versão do Node

O projeto ez-ui requer que seja utilizada a versão 14.x do Node, isso faz com que seja obrigatório que o node utilizado para executar os comandos de link esteja nessa mesma versão (14.x). Recomenda-se que seja utilizado o [NVM](https://github.com/coreybutler/nvm-windows) para gerenciar as versões do Node com os seguintes comandos.

```
 nvm install 14.19.1
 nvm use 14.19.1
```

## Versão do NPM

O projeto ez-ui requer que seja utilizada a versão 6.14.16 do NPM, isso faz com que seja obrigatório que o NPM utilizado para executar os comandos de link esteja nessa mesma versão (6.14.16).
A versão correta pode ser instalada utilizando o comando abaixo

```
npm install npm@6.14.16 -g
```

## Scrips de link

Os scripts podem ser localizados na pasta `/script` de cada projeto.

- sankhya-core/scripts/runlink.bat
- ez-ui/scripts/runlink.bat
- sankhya-blocks/scripts/runlink.bat

## O que faz o runlink.bat

O runlink.bat nada mais é do que um script que faz o link do projeto atual com suas dependências, exporta o projeto atual como um link simbólico e inicia um watcher para alterações do projeto, e sempre que ele for alterado o build do projeto é feito. Com isso as alterações são refletidas diretamente no projeto React.

## Como usar

Para fazer o link entre projetos é necessário seguir uma ordem:

- Link sankhya-core e applicação react

  - Acessar o sankhya-core, rodar o comando `\scripts\runlink.bat`
  - Acessar a aplicação react rodar o comando `\scripts\runlink.bat` e depois `npm run start`
- Link ez-ui e applicação react

  - Acessar o sankhya-core, rodar o comando `\scripts\runlink.bat`
  - Acessar o ez-ui, rodar o comando `\scripts\runlink.bat`
  - Acessar a aplicação react rodar o comando `\scripts\runlink.bat` e depois `npm run start`
- Link sankhya-blocks e applicação react

  - Acessar o sankhya-core, rodar o comando `\scripts\runlink.bat`
  - Acessar o ez-ui, rodar o comando `\scripts\runlink.bat`
  - Acessar o sankhya-blocks, rodar o comando `\scripts\runlink.bat`
  - Acessar a aplicação react rodar o comando `\scripts\runlink.bat` e depois `npm run start`

> Observe que para fazer o link de um projeto, é necessário antes executar o link de suas dependências, dessa forma, as dependências já são linkadas com a aplicação react, não sendo necessário executar todos os grupos de comando acima.
