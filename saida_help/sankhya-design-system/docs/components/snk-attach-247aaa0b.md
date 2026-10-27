---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-attach/"
titulo: "Attach"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-attach/"
trilha: "Docs > Components > Sankhya Erp Componentes > Snk Attach"
---

# Attach

O **[SnkAttach](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-attach)**
é um componente que comtepla a funcionalidade de anexar arquivos, possibilitando a visualização e download dos mesmos.
Este componente é utilizado em conjunto com o **[SnkSimpleCrud](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-simpe-crud)** e **[SnkSimpleBar](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-simpe-bar)**.

[![Imagem 1: O SnkAttach é um componente que comtepla a funcionalidade de anexar arquivos, possibilitando a visualização e download…](https://gilded-nasturtium-6b64dd.netlify.app/img/demos/snk-attach/demo.png)](https://gilded-nasturtium-6b64dd.netlify.app/img/demos/snk-attach/demo.png)

## Exemplo

Para utilizar o componente pode-se implementar da seguinte forma:

```
import React from 'react';
import { SnkApplication, SnkAttach } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const viewStackRef = React.useRef(null);

    const handleAttachmentView = () => {
        viewStackRef.current.show(2)
    }

    return (
        <SnkApplication>
            <ez-view-stack ref={(ref) => viewStackRef = ref}>
                <stack-item>
                    <ez-button label="Abrir anexos" onClick={handleAttachmentView}></ez-button>
                </stack-item>
                <stack-item>
                    <SnkAttach registerKey="999" entityName="Financeiro" />
                </stack-item>
            </ez-view-stack>
        </SnkApplication>
    )
};

export default Demo;
```

## Propriedades

### Identificação do registro

> Propriedade utilizada: **registerKey**

Esta propriedade é necessária para identificar o servidor a qual registro o anexo pertence.

### Nome da entidade

> Propriedade utilizada: **entityName**

Esta propriedade é necessária para identificar o servidor a qual entidade o anexo pertence.

## Exemplo de eventos

> Método utilizado: **onBack**

Evento disparado ao clicar no botão de voltar presente no breadcrumb e botão de voltar do **[SnkSimpleBar](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-simpe-bar)**,
como também ao botão **Finalizar** do mesmo quando não houver alterações não salvas.

```
import React from 'react';
import { SnkApplication, SnkAttach } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const viewStackRef = React.useRef(null);

    const handleAttachmentView = () => {
        viewStackRef.current.show(2)
    }

    const handleBack = () => {
        viewStackRef.current.show(1)
    }

    return (
        <SnkApplication>
            <ez-view-stack ref={(ref) => viewStackRef = ref}>
                <stack-item>
                    <ez-button label="Abrir anexos" onClick={handleAttachmentView}></ez-button>
                </stack-item>
                <stack-item>
                    <SnkAttach onBack={handleBack} />
                </stack-item>
            </ez-view-stack>
        </SnkApplication>
    )
};

export default Demo;
```

## API do componente

### Properties

| Property Attribute Description Type Default| `dataUnit` -- DataUnit responsável por carregar os dados. `DataUnit` `undefined`| `dataUnitBuilder` -- DataUnitBuilder responsável por implementar dados a serem utilizados no DataUnit. `FetcherFacade` `undefined`| `entityName` `entity-name` Nome da entidade à ser utilizada para relacionar o anexo ao DataUnit pai. `string` `undefined`| `fetcher` -- Fetcher responsável por carregar os dados do DataUnit. `AttachFetcherFacadeInterface` `undefined`| `fetcherType` `fetcher-type` FetcherType define o tipo de fetcher responsável por carregar os dados do DataUnit. `"AnexoSistema" | "Another" | "Attach"` `undefined`| `gridLegacyConfigName` `grid-legacy-config-name` Chave da configuração legado da grid. `string` `undefined`| `messagesBuilder` -- Responsável por flexibilizar e padronizar o uso de mensagens nos blocos de construção. `SnkMessageBuilder` `undefined`| `registerKey` (required) `register-key` Identificação do registro pai. `string` `undefined` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `back` Evento disparado quando o usuário clica no botão voltar. `CustomEvent<void>` | | | | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- |

### Dependencies

#### Used by

- [snk-crud](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-crud)
- [snk-detail-view](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-crud/subcomponents/snk-detail-view)

#### Depends on

- [snk-simple-bar](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-simple-bar)
- [snk-simple-crud](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-simple-crud)

#### Graph

```
graph TD;
  snk-attach --> snk-simple-bar
  snk-attach --> snk-simple-crud
  snk-simple-crud --> snk-taskbar
  snk-simple-crud --> snk-data-unit
  snk-simple-crud --> snk-simple-form-config
  snk-simple-crud --> snk-configurator
  snk-simple-crud --> snk-grid-config
  snk-simple-crud --> snk-data-exporter
  snk-simple-crud --> snk-actions-button
  snk-simple-crud --> taskbar-split-button
  snk-simple-crud --> taskbar-actions-button
  snk-taskbar --> snk-data-exporter
  snk-taskbar --> snk-actions-button
  snk-taskbar --> taskbar-split-button
  snk-taskbar --> taskbar-actions-button
  snk-data-exporter --> snk-exporter-email-sender
  snk-configurator --> snk-layout-form-config
  snk-layout-form-config --> snk-view-representation
  snk-grid-config --> snk-select-box
  snk-crud --> snk-attach
  snk-detail-view --> snk-attach
  style snk-attach fill:#f9f,stroke:#333,stroke-width:4px
```

---
