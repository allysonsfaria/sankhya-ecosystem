---
id: "https://developer.sankhya.com.br/docs/sankhya-js"
titulo: "SankhyaJS (HTML5)"
url: "https://developer.sankhya.com.br/docs/sankhya-js"
atualizado_em: "2025-11-10T23:37:47.000Z"
---

# SankhyaJS (HTML5)

O objetivo deste artigo é apresentar o framework **SankhyaJs**, centralizando informações para acesso a documentação técnica, ferramentas de desenvolvimento além de referências de formação.

O SankhyaJS, comumente chamado de HTML5, é um framework front-end que se baseia nos padrões web e no framework AngularJS. Ele tem por finalidade facilitar o desenvolvimento de telas e recursos visuais de maneira padronizada e ágil, simplificando sua criação, alteração e customização. A figura abaixo apresenta uma visão da arquitetura em camadas da plataforma Sankhya, com destaque para o uso do SankhyaJS no front-end.

<Image title="1 - Arquitetura.png" alt={1877} align="center" className="border" border={true} src="https://files.readme.io/43b8b87-1_-_Arquitetura.png" />

## Primeiros Passos

Visando uma melhor compreensão do **SankhyaJS** é necessário que o desenvolvedor tenha experiência com desenvolvimento web e conhecimento do framework AngularJS. Abaixo recomendamos alguns recursos de formação e referência:

| Curso                                                                                                     | Plataforma         | Carga Horária Prevista |
| :-------------------------------------------------------------------------------------------------------- | :----------------- | :--------------------- |
| [W3Schools- AngularJS References](https://www.w3schools.com/angular/angular_ref_directives.asp);          | W3Schools          | N/A                    |
| [AngularJS: crie webapps poderosas](https://cursos.alura.com.br/course/angularjs-mvc);                    | Alura              | 16 Horas               |
| [AngularJS por Rodrigo Branas](https://www.youtube.com/playlist?list=PLQCmSnNFVYnTD5p2fR4EXmtlR6jQJMbPb); | Youtube            | 10 Horas               |
| [AngularJS Docs](https://code.angularjs.org/1.5.8/docs/api)                                               | code.angularjs.org | N/A                    |

> 🚧 Informação Importante
>
> É altamente recomendável visualizar o curso Associate Front-End para a adquirir conhecimentos a respeito do framework front-end da Sankhya. Maiores informações podem ser obtidas clicando no botão abaixo.

<HTMLBlock>{`
<div></div>
<div class="center">
 <a class="button_background button_size"
                    href="https://developer.sankhya.com.br/docs/associate-front-end"
                    rel="noopener noreferrer">Associate Front-End</a>

</div>

<style>
    
   .center {
       display: flex;
       justify-content: center;
       align-items: center;
       height: 100px;
   }
  
   .button_size {
       background-color: #4CAF50;
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
 text-decoration: none !important;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);

    }

    .button_background {
        background-color: #66cc66;
        color: #fff !important;
    }
<style></style>
`}</HTMLBlock>

## Documentação Técnica

A documentação técnica do SankhyaJS centraliza  informações sobre os principais componentes, seu funcionamento, parâmetros e exemplos de uso, processo de build dentre outros.

* **Recursos de Api** - apresenta a descrição, parâmetros e exemplos de uso de todos os componentes utilizados;

* **Conceitos** - apresenta conceitos como funcionamento interno, maneiras de se trabalhar com o framework;

* **Principais Componentes** - apresenta os componentes visuais que estruturaram e padronizam a construção de telas, assim como o processo de renderização de dados no front-end;

* **Temas/Less** - apresenta informações sobre os layouts e temas utilizados no framework;

* **JSON/XML** - apresenta informações sobre o uso e manipulação de dados em formato JSON/XML;

* **Build** - apresenta informações sobre o processo de compilação do framework que é baseado no task runner GruntJS.

<HTMLBlock>{`
<div></div>
<div class="center">
 <a class="button_background button_size"
                    href="http://webrush.dev.sankhya.com.br/master/docs-sankhya-js/#!/"
                    rel="noopener noreferrer">Documentação Técnica</a>

</div>

<style>
    
   .center {
       display: flex;
       justify-content: center;
       align-items: center;
       height: 100px;
   }
  
   .button_size {
       background-color: #4CAF50;
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
 text-decoration: none !important;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);

    }

    .button_background {
        background-color: #66cc66;
        color: #fff !important;
    }
<style></style>
`}</HTMLBlock>

## Showcase de Componentes

O showcase é um recurso disponível para apresentar como os principais componentes do framework se comportam em execução. Com ele é possível ter uma visualização interativa dos componentes.\
Para visualizar o showcase acesse acesse a url a seguir na sua instância de desenvolvimento **https\://local:8080/mge/ShowcaseHTML5.xhtml5**.

<Image title="showcase gif.gif" alt={1092} align="center" className="border" width="100%" border={true} src="https://files.readme.io/3cc0883-showcase_gif.gif" />

## Ferramentas de Desenvolvimento

Para desenvolvimento front-end na plataforma Sankhya estão disponíveis dois plugins que possibilitam construir telas utilizando o Visual Studio Code, sendo elas o **snkCode** e o **Generator Sankhya**.

* **snkCode**;

O snkCode contém funcionalidades de autocomplete e sugestão de snippets, facilitando a criação de interfaces com o framework.

Para instalar, basta pesquisar por snkcode nas extensões do Visual Studio Code

Acesse o post na comunidade Sankhya Developer para maiores informações [Extensão Visual Studio Code Sankhya](https://comunidade.sankhya.com.br/t/extensao-visual-studio-code-sankhya/861).

<Image title="snkcode.jpg" alt={1918} align="center" className="border" border={true} src="https://files.readme.io/742586d-snkcode.jpg" />

<HTMLBlock>{`
<div></div>
<div class="center">
 <a class="button_background button_size"
                    href="https://marketplace.visualstudio.com/items?itemName=DevOpsSnk.snkCode"
                    rel="noopener noreferrer">snkCode</a>

</div>

<style>
    
   .center {
       display: flex;
       justify-content: center;
       align-items: center;
       height: 100px;
   }
  
   .button_size {
       background-color: #4CAF50;
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
 text-decoration: none !important;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);

    }

    .button_background {
        background-color: #66cc66;
        color: #fff !important;
    }
<style></style>
`}</HTMLBlock>

* **Generator Sankhya**;

O Generator Sankhya é um gerador de código, utilizado juntamente com o componente dynaform, para padronizar a criação de recursos visuais, facilitar a adição de interceptors e operações de CRUD.

Para maiores informações acesse o artigo [Generator Sankhya](https://developer.sankhya.com.br/docs/generator-sankhya).

<Image title="2- sankhya generator.png" alt={477} align="center" className="border" border={true} src="https://files.readme.io/490b0fb-2-_sankhya_generator.png" />

<HTMLBlock>{`
<div></div>
<div class="center">
 <a class="button_background button_size"
                    href="https://developer.sankhya.com.br/docs/generator-sankhya"
                    rel="noopener noreferrer">Generator Sankhya</a>

</div>

<style>
    
   .center {
       display: flex;
       justify-content: center;
       align-items: center;
       height: 100px;
   }
  
   .button_size {
       background-color: #4CAF50;
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
 text-decoration: none !important;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);

    }

    .button_background {
        background-color: #66cc66;
        color: #fff !important;
    }
<style></style>
`}</HTMLBlock>

## Como tirar dúvidas?

Para tirar dúvidas e compartilhar informações, use a sala [Sankhya Developers](https://community.sankhya.com.br/developers) da comunidade Sankhya Developer.
