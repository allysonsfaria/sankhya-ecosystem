---
id: "https://gilded-nasturtium-6b64dd.netlify.app/blog/tags/exemplos"
titulo: "Uma publicação com a etiqueta \"exemplos\""
url: "https://gilded-nasturtium-6b64dd.netlify.app/blog/tags/exemplos"
trilha: "Blog > Tags > Exemplos"
---

# Uma publicação com a etiqueta "exemplos"

## [Criando exemplos de componentes](https://gilded-nasturtium-6b64dd.netlify.app/blog/criando-exemplos-componentes)

13 de março de 2023 · 4 min para ler

![Helikson Rufino](https://gilded-nasturtium-6b64dd.netlify.app/img/authors/HeliksonRufino.jpg)

Helikson Rufino

Software Architect

![Leonardo Jorge](https://gilded-nasturtium-6b64dd.netlify.app/img/authors/LeonardoJorge.png)

Leonardo Jorge

Software Architect

![Penelope Moraes](https://gilded-nasturtium-6b64dd.netlify.app/img/authors/PenelopeMoraes.png)

Penelope Moraes

QA Analyst

Para criar uma demonstração, podemos utilizar o DocDemo criado no projeto do docusaurus.

**As seguintes regras devem ser seguidas para documentação:**

- As demos devem ser criadas no seguinte diretório do projeto: `/sankhya-design-system-docs/static/demos/react/nome_do_componente`
  - Ex: `/sankhya-design-system-docs/static/demos/react/ez-button/demo.jsx`
- O arquivo deve sempre ser exportado como um componente chamado Demo e com a extensão .jsx. Ex:

```
const Demo = () => {
	return (
	...
	)
};

export default Demo;
```

- Quando existir a necessidade de criar CSS para o exemplo, o nome do arquivo CSS deve ser o mesmo nome do arquivo do componente. Essa é uma restrição do componente DocDemo.
- Quando for necessário criar exemplos mais elaborados do componente, por exemplo, posicionamento de dois botões com ícones na view, podemos criar subpastas.
  - Exemplo: `static\demos\react\ez-button\button-icons\button-double-icon.jsx`
- Para cada componente, criar uma pasta, no path: `sankhya-design-system-docs\docs\components\02 - components-doc`. Dentro dessa pasta, adicionar um arquivo `readme.mdx` com o título `# Nome do componente`.
- O nome do componente deve ser sem o prefixo `ez-` e com a primeira letra maiúscula.

**A estrutura deve sempre seguir esses pontos:**

- O primeiro componente apresentado deve demonstrar o seu estado e comportamento padrão. Nesse exemplo, adicionar alguma iteração com o componente quando for possível.
- Os demais exemplos são as variações relevantes do componente, no `ez-button` por exemplo, temos o estado primary, secondary e tertiary. Para ver essas variações, sugiro verificar o Figma do Design System.
- Por último, apresentar um caso de uso real do componente, por exemplo, montar uma demo utilizando os botões em um componente de login.
- Todos exemplos devem ser relacionados a utilização do componente no contexto do ERP. Por exemplo, para
  os exemplos do botão, adotaremos o label de "Salvar registro" que diz a respeito a operações de CRUD
  que podem ser realizadas no ERP. Já para o componente DropDown, adotamos um exemplo de ações que podem
  ser executadas em uma nota fiscal.
- O título do menu, e dos sub-menus, quando possuir títulos compostos,
  deverão ser escritos separadamente, e com ambas as letras iniciais em maiúsculo.

  - ❌ Incorreto
    - FilterBar
    - DateInput
  - ✅ Correto
    - Filter Bar
    - Date Input
- O menu deverá seguir o seguinte padrão:

  - Os subtítulos não devem possuir caracteres especiais, como: parênteses, e não devem utilizar ponto final “.”;
  - Devem ser escritos sempre em **Português**
    - Para a propriedade disabled, o titulo apresentado deve ser "Desabilitado".
  - Para propriedades, poderá converter o nome da prop para um título que a represente corretamente, segundo os critérios estabelecidos.
  - Os nomes dos métodos e eventos não devem ser subtítulos. Eles devem ser em formato de texto, em negrito, para que possuam destaque;
  - Como subtítulos, adotaremos:
    - Principais métodos
    - Exemplos de eventos
  - A ordem a ser seguida na documentação é essa (Principais métodos; Exemplo de eventos; - exceto quando houver justa necessidade de que os eventos precedam aos métodos);
  - A hierarquia utilizada no menu é:
    - Variações e estados:
      - os tipos de variações e estados
    - Principais métodos
    - Exemplos de eventos

  Exemplo:

  ![alt text](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/menu-121324a34db0aa2f74b13bdf766ac7e8.png "Image 01")

  - Para os botões que exemplificam algum método, devemos sempre adotar o nome genérico do componente.

  Atenção

  Atenção: apenas a primeira letra deverá ficar em maiúsculo.

  - "Focar input" (Date Time Input, Filter Input);
  - "Focar botão" (Actions Button);

  Exemplo:

  ![alt text](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/exemplo_iteracoes-a1ee828a62ac023049fcdac0d429bb39.png "Image 02")

  - Botões e textos (componentes no geral) devem utilizar o modo secundário e serem alinhados à esquerda:

  Exemplo:

  ![alt text](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/exemplo_btn-16e362943f0d7cfc3ee7fdd6b6bbba0b.png "Image 03")

  ![alt text](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/exemplo_txt-b607a0862f067c9529fce80d2bd1ccb3.png "Image 04")

  - Para alertas, infos e observações, a apresentação deverá ser padronizada,
    obedecendo os seguintes títulos/cores:

  Informação

  Aqui vai uma **informação** que merece destaque

  Observação

  Aqui vai uma **observação** que merece destaque

  Importante

  Aqui vai um **alerta** que merece destaque
