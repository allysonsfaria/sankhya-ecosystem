---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-pesquisa/"
titulo: "Pesquisa"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-pesquisa/"
trilha: "Docs > Components > Sankhya Erp Componentes > Snk Pesquisa"
---

# Pesquisa

O componente **SnkPesquisa** é um painel avançado para pesquisa de registros de uma entidade no ERP Sankhya. Ele permite localizar, visualizar e selecionar registros de forma eficiente, suportando diferentes modos de exibição (lista, grade e árvore hierárquica) e integração com funções assíncronas para carregamento de dados.

[![Imagem 1: O componente SnkPesquisa é um painel avançado para pesquisa de registros de uma entidade no ERP Sankhya. Ele permite…](https://gilded-nasturtium-6b64dd.netlify.app/img/demos/snk-pesquisa/snk-pesquisa.png)](https://gilded-nasturtium-6b64dd.netlify.app/img/demos/snk-pesquisa/snk-pesquisa.png)

## Quando utilizar

Utilize o **SnkPesquisa** quando for necessário:

- Permitir ao usuário pesquisar e selecionar registros de uma entidade de forma flexível e dinâmica.
- Exibir resultados de pesquisa em diferentes formatos (lista, grade ou árvore hierárquica).
- Integrar a pesquisa com carregadores assíncronos customizados, como buscas em APIs ou serviços externos.
- Oferecer uma experiência de pesquisa avançada, com destaque de termos encontrados e suporte a filtros.

## Quando não utilizar

Evite utilizar o **SnkPesquisa** quando:

- A pesquisa for simples e não exigir múltiplos modos de exibição ou integração com carregadores customizados.
- O contexto exigir apenas um campo de busca básico, sem necessidade de seleção detalhada de registros.
- Não houver necessidade de navegação hierárquica ou exibição de múltiplos detalhes dos registros.

## Propriedades

### Carregador de pesquisa

> Propriedade utilizada: `searchLoader`

Esta propriedade corresponde à função responsável por carregar os registros do componente **SnkPesquisa**.

A seguir é apresentado um exemplo desta propriedade em conjunto com o método loadAdvancedSearch
que faz parte da classe **PesquisaFetcher**.

[![Imagem 2: A seguir é apresentado um exemplo desta propriedade em conjunto com o método loadAdvancedSearch que faz parte da classe…](https://gilded-nasturtium-6b64dd.netlify.app/img/demos/snk-pesquisa/search-loader.png)](https://gilded-nasturtium-6b64dd.netlify.app/img/demos/snk-pesquisa/search-loader.png)

```
import { SnkPesquisa } from "@sankhyalabs/sankhyablocks/react/components";
import { PesquisaFetcher } from '@sankhyalabs/sankhyablocks/dist/collection/lib';

const Demo = () => {
    const pesquisaFetcher = new PesquisaFetcher();

    const searchLoader = (text) => {
        return pesquisaFetcher.loadAdvancedSearch("ImplantacaoSaldoConta", text);
    };

    return (
        <div className="ez-padding--large">
            <SnkPesquisa
                searchLoader={searchLoader}>
            </SnkPesquisa>
        </div>
    );
};

export default Demo;
```

### Selecionar item

> Propriedade utilizada: `selectItem`

Função disparada ao selecionar um item.

[![Imagem 3: Função disparada ao selecionar um item.](https://gilded-nasturtium-6b64dd.netlify.app/img/demos/snk-pesquisa/select-item.png)](https://gilded-nasturtium-6b64dd.netlify.app/img/demos/snk-pesquisa/select-item.png)

```
import { useState } from "react";
import { SnkPesquisa } from "@sankhyalabs/sankhyablocks/react/components";
import { PesquisaFetcher } from '@sankhyalabs/sankhyablocks/dist/collection/lib';

const Demo = () => {
    const [option, setOption] = useState();
    const pesquisaFetcher = new PesquisaFetcher();

    const searchLoader = (text) => {
        return pesquisaFetcher.loadAdvancedSearch("ImplantacaoSaldoConta", text);
    };

    return (
        <div className="ez-flex ez-flex--column ez-padding--large">
            <label className="ez-label ez-margin-bottom--medium">
                Opção Selecionada: <strong>{JSON.stringify(option)}</strong>
            </label>

            <SnkPesquisa
                searchLoader={searchLoader}
                selectItem={setOption}>
            </SnkPesquisa>
        </div>
    );
};

export default Demo;
```

### Argumento para pesquisa

> Propriedade utilizada: `argument`

Texto apresentado como argumento da pesquisa e utilizado ao chamar a função **searchLoader**.

[![Imagem 4: Texto apresentado como argumento da pesquisa e utilizado ao chamar a função searchLoader .](https://gilded-nasturtium-6b64dd.netlify.app/img/demos/snk-pesquisa/argument.png)](https://gilded-nasturtium-6b64dd.netlify.app/img/demos/snk-pesquisa/argument.png)

```
import { SnkPesquisa } from "@sankhyalabs/sankhyablocks/react/components";
import { PesquisaFetcher } from '@sankhyalabs/sankhyablocks/dist/collection/lib';

const Demo = () => {
    const pesquisaFetcher = new PesquisaFetcher();

    const searchLoader = (text) => {
        return pesquisaFetcher.loadAdvancedSearch("ImplantacaoSaldoConta", text);
    };

    return (
        <div className="ez-padding--large">
            <SnkPesquisa
                searchLoader={searchLoader}
                argument="brasil">
            </SnkPesquisa>
        </div>
    );
};

export default Demo;
```

### allowsNonAnalytic

> Propriedade utilizada: `allowsNonAnalytic`

Permite a seleção de itens não analíticos(Itens que não possuem itens filhos) na pesquisa, útil para entidades hierárquicas como plano de contas.

[![Imagem 5: Permite a seleção de itens não analíticos(Itens que não possuem itens filhos) na pesquisa, útil para entidades…](https://gilded-nasturtium-6b64dd.netlify.app/img/demos/snk-pesquisa/allows-non-nalytic.png)](https://gilded-nasturtium-6b64dd.netlify.app/img/demos/snk-pesquisa/allows-non-nalytic.png)

```
import { useState } from "react";
import { SnkPesquisa } from "@sankhyalabs/sankhyablocks/react/components";
import { PesquisaFetcher } from '@sankhyalabs/sankhyablocks/dist/collection/lib';

const Demo = () => {
    const [option, setOption] = useState();
    const pesquisaFetcher = new PesquisaFetcher();

  const searchLoader = (text) => {
    return pesquisaFetcher.loadAdvancedSearch("Natureza", text);
  };

  const treeLoader = (text) => {
    return pesquisaFetcher.loadTree("Natureza", text);
  };

  return (
    <div className="ez-padding--large">
        <label className="ez-label ez-margin-bottom--medium">
            Opção Selecionada: <strong>{JSON.stringify(option)}</strong>
        </label>
        <SnkPesquisa
            allowsNonAnalytic={false}
            isHierarchyEntity={true}
            searchLoader={searchLoader}
            selectItem={setOption}
            treeLoader={treeLoader}
        />
    </div>
  );
};

export default Demo;
```

### isHierarchyEntity

> Propriedade utilizada: `isHierarchyEntity`

Ativa o modo de pesquisa hierárquica, exibindo os dados em formato de árvore.

[![Imagem 6: Ativa o modo de pesquisa hierárquica, exibindo os dados em formato de árvore.](https://gilded-nasturtium-6b64dd.netlify.app/img/demos/snk-pesquisa/hierarchy.png)](https://gilded-nasturtium-6b64dd.netlify.app/img/demos/snk-pesquisa/hierarchy.png)

```
import { SnkPesquisa } from "@sankhyalabs/sankhyablocks/react/components";
import { PesquisaFetcher } from '@sankhyalabs/sankhyablocks/dist/collection/lib';

const Demo = () => {
  const pesquisaFetcher = new PesquisaFetcher();

  const searchLoader = (text) => {
    return pesquisaFetcher.loadAdvancedSearch("Natureza", text);
  };

  const treeLoader = (text) => {
    return pesquisaFetcher.loadTree("Natureza", text);
  };

  return (
    <div className="ez-padding--large">
      <SnkPesquisa
        entityName="Natureza"
        isHierarchyEntity={true}
        searchLoader={searchLoader}
        treeLoader={treeLoader}
      />
    </div>
  );
};

export default Demo;
```

### entityName

> Propriedade utilizada: `entityName`

Define a entidade sobre a qual a pesquisa será realizada.

```
import { SnkPesquisa } from "@sankhyalabs/sankhyablocks/react/components";
import { PesquisaFetcher } from '@sankhyalabs/sankhyablocks/dist/collection/lib';

const Demo = () => {
  const pesquisaFetcher = new PesquisaFetcher();

  const searchLoader = (text) => {
    return pesquisaFetcher.loadAdvancedSearch("Produto", text);
  };

  return (
    <div className="ez-padding--large">
      <SnkPesquisa
        entityName="Produto"
        searchLoader={searchLoader}
      />
    </div>
  );
};

export default Demo;
```

### treeLoader

> Propriedade utilizada: `treeLoader`

Permite customizar a busca dos dados hierárquicos, útil para entidades com estrutura em árvore.

```
import { SnkPesquisa } from "@sankhyalabs/sankhyablocks/react/components";
import { PesquisaFetcher } from '@sankhyalabs/sankhyablocks/dist/collection/lib';

const Demo = () => {
  const pesquisaFetcher = new PesquisaFetcher();

  const searchLoader = (text) => {
    return pesquisaFetcher.loadAdvancedSearch("ContaContabil", text);
  };

  const treeLoader = (text) => {
    // Exemplo de busca hierárquica customizada
    return pesquisaFetcher.loadTree("ContaContabil", text);
  };

  return (
    <div className="ez-padding--large">
      <SnkPesquisa
        entityName="ContaContabil"
        isHierarchyEntity={true}
        treeLoader={treeLoader}
        searchLoader={searchLoader}
      />
    </div>
  );
};

export default Demo;
```

## API do componente

### Properties

| Property Attribute Description Type Default| `allowsNonAnalytic` `allows-non-analytic` Define se permite a seleção de itens não analíticos. `boolean` `false`| `argument` `argument` Argumento utilizado ao chamar a função searchLoader. Pode ser alterado externamente. `string` `undefined`| `entityName` `entity-name` Nome da entidade sobre a qual a pesquisa será realizada. `string` `undefined`| `isHierarchyEntity` `is-hierarchy-entity` Define se a popup de pesquisa terá ou não modo hierárquico. `boolean` `false`| `searchLoader` -- Função responsável em carregar os itens do componente snk-pesquisa. Deve retornar uma Promise com os dados encontrados. `(text: string) => Promise<any>` `undefined`| `selectItem` -- Função disparada ao selecionar um item da pesquisa. `(option: IOption) => void` `undefined`| `treeLoader` -- Função responsável por carregar a árvore hierárquica do componente. Opcional. Caso não seja fornecida, o modo árvore não estará disponível. `(text: string) => Promise<any>` `undefined` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Dependencies

#### Used by

- [snk-application](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-application)

#### Depends on

- [pesquisa-grid](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-pesquisa/pesquisa-grid)
- [pesquisa-tree](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-pesquisa/pesquisa-tree)

#### Graph

```
graph TD;
  snk-pesquisa --> pesquisa-grid
  snk-pesquisa --> pesquisa-tree
  snk-application --> snk-pesquisa
  style snk-pesquisa fill:#f9f,stroke:#333,stroke-width:4px
```

---
