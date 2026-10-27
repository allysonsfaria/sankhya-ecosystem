---
id: "https://gilded-nasturtium-6b64dd.netlify.app/blog/elementos-personalizados-na-taskbar"
titulo: "Como utilizar elementos personalizados na Taskbar"
url: "https://gilded-nasturtium-6b64dd.netlify.app/blog/elementos-personalizados-na-taskbar"
trilha: "Blog > Elementos Personalizados Na Taskbar"
---

# Como utilizar elementos personalizados na Taskbar

24 de janeiro de 2024 · 7 min para ler

![Nilson Neto](https://gilded-nasturtium-6b64dd.netlify.app/img/authors/NilsonNeto.png)

Nilson Neto

Developer

![Victor Uehara](https://gilded-nasturtium-6b64dd.netlify.app/img/authors/VictorUehara.png)

Victor Uehara

Developer

## Introdução

É possível que seja solicitado pelo time de negócios que a barra de tarefas apresente algum componente que ainda não
tenha sido criado pelo time de **Design System**.
Para que os desenvolvedores não fiquem com suas demandas travadas, disponibilizamos um mecanismo para que a Taskbar
renderize qualquer elemento HTML.

![alt text](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/exemplo_1-874b493e716ed239cea43ebb8a3d53c9.png "Image Expample Custom Elements")

## Solução

É possível injetar na barra de tarefas (**SnkTaskbar**), elementos HTML utilizando uma combinação entre as propriedades
**buttons**, **customSlotId** e **customContainerId**, junto ao WebComponent **SnkCustomSlotElements** e utilização
do recurso [slot de WebComponents](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/slot).

Abaixo descreveremos alguns cenários e daremos exemplos de como injetar elementos HTML na **Taskbar** da forma correta.

## Cenários

### Filhos diretos da Taskbar

Para implementar elementos customizados como filhos diretos da **Taskbar**, basta declarar o componente **SnkCustomSlotElements**
dentro da **Taskbar** e adicionar os elementos personalizados que devem ser exibidos.

```
const Demo = () => {
    const snkDataUnit = useRef(null);

    // Exemplo de lista de botões ativos na barra de tarefas (SnkTaskbar).
    const buttons = [
        "PREVIOUS",
        "NEXT",
        "CUSTOM_ELEMENT" // Identificador do elemento personalizado que deve ser renderizado
    ];

    const loadData = async () => {
        const dataUnit = await snkDataUnit?.current.getDataUnit();
        dataUnit.loadData();
    };

    useEffect(() => {
        loadData();
    }, []);

    return (
        <SnkApplication configName="MovimentoBancario">
            <SnkDataUnit ref={snkDataUnit} entityName="MovimentoBancario">
                <SnkTaskbar buttons={buttons.join(",")}>

                    <SnkCustomSlotElements>
                        <span id="CUSTOM_ELEMENT"> Elemento customizado</span>
                    </SnkCustomSlotElements>

                </SnkTaskbar>
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

Perceba que é preciso atribuir um **id** para o elemento personalizado e repassá-lo para a prop **buttons**, pois dessa
forma a **Taskbar** saberá como encontrá-lo na DOM.

Atenção

É necessário que o desenvolvedor utilize o componente **SnkCustomSlotElements** para encapsular os elementos
personalizados, para garantir o comportamento adequado da **Taskbar**.

É possível adicionar quantos elementos personalizados quiser, basta que o atributo **id** seja único para cada um deles.

```
const Demo = () => {
    const snkDataUnit = useRef(null);

    // Exemplo de lista de botões ativos na barra de tarefas (SnkTaskbar).
    const buttons = [
        "PREVIOUS",
        "NEXT",
        "CUSTOM_ELEMENT", // Identificador do elemento personalizado 1 que deve ser renderizado
        "CUSTOM_ELEMENT_2", // Identificador do elemento personalizado 2 que deve ser renderizado
        "CUSTOM_ELEMENT_3" // Identificador do elemento personalizado 3 que deve ser renderizado
    ];

    const loadData = async () => {
        const dataUnit = await snkDataUnit?.current.getDataUnit();
        dataUnit.loadData();
    };

    useEffect(() => {
        loadData();
    }, []);

    return (
        <SnkApplication configName="MovimentoBancario">
            <SnkDataUnit ref={snkDataUnit} entityName="MovimentoBancario">
                <SnkTaskbar buttons={buttons.join(",")}>

                    <SnkCustomSlotElements>
                        <span id="CUSTOM_ELEMENT"> Elemento customizado 1</span>
                        <span id="CUSTOM_ELEMENT_2"> Elemento customizado 2</span>
                        <div id="CUSTOM_ELEMENT_3">
                            <h1>Elemento customizado 3</h1>
                            <h2>Pode ser um elemento composto por vários elementos</h2>
                        </div>
                    </SnkCustomSlotElements>

                </SnkTaskbar>
            </SnkDataUnit>
        </SnkApplication>
    );
};

export default Demo;
```

### Utilizando Slots

Existem cenários onde o desenvolvedor deseja implementar blocos de construção que contenham uma **Taskbar** e permitir
que os elementos personalizados sejam definidos externamente, ficando de responsabilidade de quem utilizar o bloco para definir os
elementos customizados.

Para implementar essa abordagem utilizamos o recurso [slot de WebComponents](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/slot),
que nos permite definir um template onde serão renderizados elementos definidos externamente.
Para usar essa abordagem, é preciso definir no bloco que implementa a **SnkTaskbar** o slot com o nome TASKBAR\_CUSTOM\_ELEMENTS
e quem for utilizar esse bloco, passar como filho o componente **SnkCustomSlotElements** contendo os elementos personalizados.

**Bloco com taskbar:**

```
const BlocoComTaskbar = ({getButtons}) => {
    return (
        <div>
            <SnkTaskbar buttons={getButtons()}> // Perceba que os botões são recuperados através de um callback
                <slot name="TASKBAR_CUSTOM_ELEMENTS"/>
            </SnkTaskbar>

            // Outros componentes que compoem o bloco
            <OutrosComponentes />
        </div>
    );
};

export default BlocoComTaskbar;
```

**Aplicação que utiliza BlocoComTaskbar:**

```
const Demo = () => {
    const getButtons = () =>{
        return [
            "NEXT",
            "PREVIOUS",
            "CUSTOM_ELEMENT" // Identificador do elemento customizado
        ]
    }

    const loadData = async () => {
        const dataUnit = await snkDataUnit?.current.getDataUnit();
        dataUnit.loadData();
    };

    useEffect(() => {
        loadData();
    }, []);

    return (
        <SnkApplication configName="MovimentoBancario">
            <SnkDataUnit ref={snkDataUnit} entityName="MovimentoBancario">

                <BlocoComTaskbar getButtons={getButtons}>
                    <SnkCustomSlotElements>
                        <span id="CUSTOM_ELEMENT"> Elemento Personalizado</span>
                    </SnkCustomSlotElements>
                </BlocoComTaskbar>

            </SnkApplication>
        </SnkDataUnit>
    );
};

export default Demo;
```

dica

É possível permitir que a taskbar renderize esses elementos personalizados de forma dinâmica criando uma classe utilitária
que implemente a interface **TaskbarManager** e seus métodos **getButtons** e **isEnabled**.

### Slots com elementos customizados

Podemos também utilizar elementos customizados na taskbar através do atributo slot.
No exemplo a seguir declaramos o slot "BTN\_ALTERAR\_CENTRAIS" através da prop buttons e depois passamos um elementos customizado pelo atributo slot.

**Exemplo:**

```
<SnkTaskbar
    dataUnit={cabecalhoNotaDU}
    primaryButton={"INSERT"}
    buttons={'ATTACH,MORE_OPTIONS,REFRESH,SAVE,BTN_ALTERAR_CENTRAIS,CANCEL,INSERT,DELETE,CONFIGURATOR'}
    disabledButtons={[]}
    presentationMode={'primary' as any}
    messagesBuilder={snkApp.messagesBuilder}
    actionsList={moreOptionsEnabled}
    onActionClick={({detail}: CustomEvent) => handleActionClick(detail)}
    >
    <div slot="BTN_ALTERAR_CENTRAIS" className='ez-margin-left--medium'>
        {lancamentos.length > 1 ? (
            <EzBadge size="extra-small" className="ez-badge--success-solid">
                {renderButtonAlternarCentrais()}
            </EzBadge>
        ) : renderButtonAlternarCentrais()
        }
    </div>
</SnkTaskbar>
```

![alt text](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/CustomElementSlot-253fcb4deb6fa2e9e9d96e890b463991.png "Elemento customizado inserido na taskbar")

### Blocos com mais de uma Taskbar

Blocos de construção mais complexos podem conter mais de uma barra de tarefas. É o caso por exemplo do bloco **SnkGrid**,
onde temos uma **Taskbar** na grade e outra no cabeçalho do bloco.

![alt text](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/snk_grid_example-4d863089f01a8e1030884e655dd8cdf5.png "Imagem de exemplo da snkgrid")

Nesse caso, o bloco que implementa as barras de tarefa, precisa definir um slot para cada container de elementos personalizados
**(SnkCustomSlotElements)**, e informar em cada **Taskbar** a propriedade **customSlotId** com o nome atribuído a esse slot.

```
const BlocoComDuasTaskbar = ({getButtons}) => {
    return (
        <div>
            <SnkTaskbar
                buttons={getButtons()}
                customSlotId="TASKBAR_CUSTOM_ELEMENTS_TOP" // Deve ser atribuído o mesmo valor do nome do slot
            >
                <slot name="TASKBAR_CUSTOM_ELEMENTS_TOP"/>
            </SnkTaskbar>

            // Outros componentes que compoem o bloco
            <OutrosComponentes />

            <SnkTaskbar
                buttons={getButtons()}
                customSlotId="TASKBAR_CUSTOM_ELEMENTS_BOTTOM" // Deve ser atribuído o mesmo valor do nome do slot
            >
                <slot name="TASKBAR_CUSTOM_ELEMENTS_BOTTOM"/>
            </SnkTaskbar>
        </div>
    );
};

export default BlocoComDuasTaskbar;
```

**Aplicação que utiliza BlocoComDuasTaskbar:**

Já a aplicação que utiliza o bloco **BlocoComDuasTaskbar** precisa implementar um container de elementos personalizados
**(SnkCustomSlotElements)** para cada **Taskbar**, atribuindo o valor da propriedade **slotName** igual ao do nome do slot
que pertence.

```
const Demo = () => {
    const getButtons = () =>{
        return [
            "NEXT",
            "PREVIOUS",
            "CUSTOM_ELEMENT_BOTTOM", // Identificador do elemento customizado TOP
            "CUSTOM_ELEMENT_TOP", // Identificador do elemento customizado BOTTOM
        ]
    }

    const loadData = async () => {
        const dataUnit = await snkDataUnit?.current.getDataUnit();
        dataUnit.loadData();
    };

    useEffect(() => {
        loadData();
    }, []);

    return (
        <SnkApplication configName="MovimentoBancario">
            <SnkDataUnit ref={snkDataUnit} entityName="MovimentoBancario">

                <BlocoComDuasTaskbar getButtons={getButtons}>
                    <SnkCustomSlotElements
                        slotName={"TASKBAR_CUSTOM_ELEMENTS_TOP"} // Nome do slot a qual pertence
                    >
                        <span id="CUSTOM_ELEMENT_TOP"> Elemento Personalizado (TOP)</span>
                    </SnkCustomSlotElements>

                    <SnkCustomSlotElements
                        slotName={"TASKBAR_CUSTOM_ELEMENTS_BOTTOM"} // Nome do slot a qual pertence
                    >
                        <span id="CUSTOM_ELEMENT_BOTTOM"> Elemento Personalizado (BOTTOM)</span>
                    </SnkCustomSlotElements>
                </BlocoComDuasTaskbar>

            </SnkApplication>
        </SnkDataUnit>
    );
};

export default Demo;
```

dica

O valor padrão da propriedade **slotName (SnkCustomSlotElements)** é CUSTOM\_SLOT\_ELEMENTS.

### Slots pré estabelecidos

Foram criados alguns slots pré estabelecidos para facilitar a inserção de elementos personalizados nas barras de tarefa
dos blocos já criados. Segue abaixo o mapeamento desses slots:

- **SnkSimpleCrud**:
  - Taskbar da grade: `TASKBAR_CUSTOM_ELEMENTS`
- **SnkGrid**:
  - Taskbar geral: `GRID_TASKBAR_CUSTOM_ELEMENTS`
  - Cabeçalho da grade: `GRID_HEADER_CUSTOM_ELEMENTS`
- **SnkCrud**
  - Views:
    - Taskbar geral do modo formulário: `GUIDES_VIEWER_TASKBAR_CUSTOM_ELEMENTS`
  - Details
    - Taskbar do formulário: `DETAIL_TASKBAR_CUSTOM_ELEMENTS`
    - Taskbar geral: `DETAIL_GRID_TASKBAR_CUSTOM_ELEMENTS`
    - Cabeçalho da grade: `DETAIL_GRID_HEADER_CUSTOM_ELEMENTS`

**Exemplo:**

```
const Demo = () => {

    // Exemplo de implementação do taskbar TaskbarManager, para gerenciar exibição dos items da taskbar.
    const taskbarManager = {
       getButtons: (taskbarId, dataState, currentButtons) => {
             // Logica para retornar um array com o id dos elementos que devem ser exibidos (botões padrão, divisores, custom buttons e elementos personalizados).
            return ['grid_header', 'grid_taskbar', 'guides_view',
             'detail_grid_header', 'detail_grid_taskbar', 'detail_taskbar' ]
       },
       isEnabled: (taskbarId, dataState, buttonName) => {
            // Lógica para retornar se botão informado está habilitado.
            return true;
       }
    }

    const snkCrud = useRef(null);
    const loadData = async () => {
        const dataUnit = await snkDataUnit?.current.getDataUnit();
        dataUnit.loadData();
    };

    useEffect(() => {
        loadData();
    }, []);

    return (
        <SnkApplication configName="MovimentoBancario">
            <SnkDataUnit ref={snkDataUnit} entityName="MovimentoBancario">
                <SnkCrud ref={snkCrud} taskbarManager={taskbarManager}>

                    // Taskbar do cabeçalho da grade
                    <SnkCustomSlotElements slotName={"GRID_HEADER_CUSTOM_ELEMENTS"}>
                        <div id={"grid_header"}>
                            <EzBadge iconLeft="alert-circle" size="medium" className="ez-badge--error-solid" />
                            <EzBadge label="Elemento Personalizado" size="medium" className="ez-badge--error-subtle" />
                        </div>
                    </SnkCustomSlotElements>

                    // Taskbar do topo da grade
                    <SnkCustomSlotElements slotName={"GRID_TASKBAR_CUSTOM_ELEMENTS"}>
                        <EzBadge id={"grid_taskbar"} label="grid_taskbar" size="medium" className="ez-badge--error-solid" />
                    </SnkCustomSlotElements>

                    // Taskbar geral do modo formulário
                    <SnkCustomSlotElements slotName={"GUIDES_VIEWER_TASKBAR_CUSTOM_ELEMENTS"}>
                        <EzBadge id={"guides_view"} label="guides_view" size="medium" className="ez-badge--warning-solid" />
                    </SnkCustomSlotElements>

                    // Taskbar no cabeçalho da grade da aba de detalhes
                    <SnkCustomSlotElements slotName={"DETAIL_GRID_HEADER_CUSTOM_ELEMENTS"}>
                        <EzBadge id={"detail_grid_header"} iconLeft="alert-circle" size="large" className="ez-badge--warning-solid" />
                    </SnkCustomSlotElements>

                    // Taskbar no topo da grade da aba de detalhes
                    <SnkCustomSlotElements slotName={"DETAIL_GRID_TASKBAR_CUSTOM_ELEMENTS"}>
                        <EzBadge id={"detail_grid_taskbar"} iconLeft="alert-circle" size="large" className="ez-badge--warning-solid" />
                    </SnkCustomSlotElements>

                    // Taskbar no modo formulário da grade da aba de detalhes
                    <SnkCustomSlotElements slotName={"DETAIL_TASKBAR_CUSTOM_ELEMENTS"}>
                        <EzBadge id={"detail_taskbar"} iconLeft="alert-circle" size="large" className="ez-badge--warning-solid" />
                    </SnkCustomSlotElements>

                   // Outros Componentes do SnkCrud
                   <OutrosComponentes />
                </SnkCrud>
            </SnkApplication>
        </SnkDataUnit>
    );
};

export default Demo;
```
