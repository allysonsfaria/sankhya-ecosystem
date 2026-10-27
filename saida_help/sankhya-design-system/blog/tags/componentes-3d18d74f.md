---
id: "https://gilded-nasturtium-6b64dd.netlify.app/blog/tags/componentes"
titulo: "Uma publicação com a etiqueta \"componentes\""
url: "https://gilded-nasturtium-6b64dd.netlify.app/blog/tags/componentes"
trilha: "Blog > Tags > Componentes"
---

# Uma publicação com a etiqueta "componentes"

## [Boas práticas de codificação e codereview para componentes](https://gilded-nasturtium-6b64dd.netlify.app/blog/boas-praticas-code-review-componentes)

7 de abril de 2023 · 3 min para ler

![Helikson Rufino](https://gilded-nasturtium-6b64dd.netlify.app/img/authors/HeliksonRufino.jpg)

Helikson Rufino

Software Architect

![Leonardo Jorge](https://gilded-nasturtium-6b64dd.netlify.app/img/authors/LeonardoJorge.png)

Leonardo Jorge

Software Architect

![Marcos Sobral](https://gilded-nasturtium-6b64dd.netlify.app/img/authors/MarcosSobral.png)

Marcos Sobral

Software Architect

Para implementação de componentes devemos seguir todas as regras de Clean Code citadas anteriormente, porém,
existem algumas regras específicas para a implementação de componentes nas bibliotecas do design system.

Além das [diretrizes de boas práticas e clean code](https://gilded-nasturtium-6b64dd.netlify.app/blog/boas-praticas-code-review-codificacao), as regras diretrizes a seguir também devem ser seguidas.

### TSX

- Todas propriedades, retorno de funções, argumento de funções e tipo da dados de eventos devem ser tipadas, e com nomes sugestivos:

```
const user = { name: "Sankhya" }
const userArray = []
// ❌ Incorreto
@Prop()
autoClose: any = true;
// ✅ Correto
@Prop()
autoClose: boolean = true;
// ❌ Incorreto
@Method()
async show(top, left){
// Do something
}
// ✅ Correto
@Method()
async show(top: string, left: string):Promise<boolean> {
// Do something
}
// ❌ Incorreto
@Event() ezVisibilityChange: EventEmitter<any>;
// ✅ Correto
@Event() ezVisibilityChange: EventEmitter<boolean>;
```

- Propriedades públicas, métodos públicos e eventos devem
  estar devidamente documentados seguindo as regras das [diretrizes de documentação](https://gilded-nasturtium-6b64dd.netlify.app/blog/diretrizes-de-documentacao).
- Qualquer necessidade de adicionar propriedade pública, método público e evento nos componentes deve
  ser alinhado com o time de arquitetura ou tech leads, e esses devem ser adicionados na estória de implementação do Jira com
  a tabela no seguinte padrão:

> Propriedades

| Nome Tipo Valor padrão Descrição| items `Array<string>` [] Lista de itens que vão ser apresentados | | | | | --- | --- | --- | --- | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |

> Métodos

| Nome Argumentos Descrição| selectItem `id:string` Efetua a seleção de um item. | | | | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- |

> Eventos

| Nome Tipo Descrição| ezChange `id:string` Disparado quando um item é selecionado. | | | | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- |

- As alterações em métodos públicos devem ser muito bem avaliadas, pois, isso impacta na aplicação que esse método pode estar sendo usado.
- As variáveis que fazem parte do state, estão sendo alteradas só quando necessário? Evitando re-render.
- O componente está com shadowdom ou scoped ativo?
- Os atributos de testability foram adicionados utilizando o guia Definindo bons data [element id de testabilidade no design system](https://gilded-nasturtium-6b64dd.netlify.app/blog/definindo-bons-element-id).

### CSS

- Os tokens públicos devem estar devidamente documentados conforme exemplo a seguir:

```
/*@doc Define a largura mínima do componente.*/
--ez-button--min-width: 100px;
```

### Utilitários do projeto core

- Sempre avaliar se esse utilitário é necessário, as seguintes perguntas devem ser feitas:

  - Não temos nada do JavaScript que resolva esse problema de forma simples?
  - Esse utilitário agrega valor? Será utilizado por outros desenvolvedores?
  - Caso o utilitário seja criado, a API dele tem que ser muito bem pensada de tal forma que seja reutilizado em outros lugares da aplicação.

### DataUnit

O componente DataUnit é um componente bem crítico dos utilitários do design system, por isso,
neste item vamos tratar de alguns pontos relevantes durante o desenvolvimento e revisão desse componente.

- O componente DataUnit tem uma responsabilidade muito clara: “Gerenciar dados de uma aplicação”,
  por conta desse conceito, é muito importante o DataUnit se mantenha agnóstico a qualquer regra de negócio.
- Para criação de novos slices, actions e métodos públicos deve ser solicitado na estória de implementação, e alinhado com Tech Leads ou Arquiteto.
- Os conceitos de arquitetura flux estão sendo seguidos?
- Os conceitos descritos no documento [Arquitetura do DataUnit](https://gitlab.sankhya.com.br/dti/design-system/sankhyacore/-/wikis/Arquitetura-do-DataUnit)
  estão sendo seguidos?
