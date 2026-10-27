---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/OverflowWatcher"
titulo: "OverflowWatcher"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/OverflowWatcher"
trilha: "Docs > Utilities > Api > Classes > Overflowwatcher"
---

# OverflowWatcher

[**@sankhyalabs/core**](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/) • **Docs**

---

[@sankhyalabs/core](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/globals) / OverflowWatcher

# Class: OverflowWatcher

## Constructors

### new OverflowWatcher()

> **new OverflowWatcher**(`__namedParameters`): [`OverflowWatcher`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/OverflowWatcher)

Cria uma instancia do OverflowWatcher

#### Parameters

• **\_\_namedParameters**: [`OverFlowWatcherParams`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/OverFlowWatcherParams)

#### Returns

[`OverflowWatcher`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/OverflowWatcher)

#### Source

src/utils/OverflowWatcher/index.ts:35

## Properties

### DATA\_ELEMENT\_ID

> `readonly` **DATA\_ELEMENT\_ID**: `"data-element-id"` = `'data-element-id'`

#### Source

src/utils/OverflowWatcher/index.ts:23

---

### \_deltaSize

> `private` **\_deltaSize**: `number`

#### Source

src/utils/OverflowWatcher/index.ts:20

---

### \_hiddenItemsProps

> `private` **\_hiddenItemsProps**: `Map`<`Element`, `SizeProps`>

#### Source

src/utils/OverflowWatcher/index.ts:18

---

### \_lastContainerInstance

> `private` **\_lastContainerInstance**: `undefined` | `HTMLElement` = `undefined`

#### Source

src/utils/OverflowWatcher/index.ts:15

---

### \_lastContainerSize

> `private` **\_lastContainerSize**: `undefined` | `number` = `undefined`

#### Source

src/utils/OverflowWatcher/index.ts:14

---

### \_notOverFlow

> `private` **\_notOverFlow**: `string`[] = `[]`

#### Source

src/utils/OverflowWatcher/index.ts:21

---

### \_notOverFlowPros

> `private` **\_notOverFlowPros**: `Map`<`string`, `SizeProps`>

#### Source

src/utils/OverflowWatcher/index.ts:19

---

### \_onResize

> `private` **\_onResize**: [`OnOverflowCallBack`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/type-aliases/OnOverflowCallBack)

#### Source

src/utils/OverflowWatcher/index.ts:12

---

### \_propSize

> `private` **\_propSize**: `string`

#### Source

src/utils/OverflowWatcher/index.ts:17

---

### \_resizeObserver

> `private` **\_resizeObserver**: `ResizeObserver`

#### Source

src/utils/OverflowWatcher/index.ts:13

---

### \_scrollDirection

> `private` **\_scrollDirection**: [`OverflowDirection`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/enumerations/OverflowDirection) = `OverflowDirection.HORIZONTAL`

#### Source

src/utils/OverflowWatcher/index.ts:16

## Methods

### addNotOverFlowElement()

> **addNotOverFlowElement**(`elementId`): `void`

#### Parameters

• **elementId**: `string`

#### Returns

`void`

#### Source

src/utils/OverflowWatcher/index.ts:52

---

### calcChildrenSize()

> `private` **calcChildrenSize**(`children`): `number`

#### Parameters

• **children**: `Element`[]

#### Returns

`number`

#### Source

src/utils/OverflowWatcher/index.ts:206

---

### calcElementSize()

> `private` **calcElementSize**(`el`): `number`

#### Parameters

• **el**: `Element`

#### Returns

`number`

#### Source

src/utils/OverflowWatcher/index.ts:213

---

### calculateVariation()

> `private` **calculateVariation**(`elementIdsToCalculate`): `number`

#### Parameters

• **elementIdsToCalculate**: `string`[]

#### Returns

`number`

#### Source

src/utils/OverflowWatcher/index.ts:178

---

### canNotOverFlowNotIncludedIds()

> `private` **canNotOverFlowNotIncludedIds**(`elements`): `string`[]

#### Parameters

• **elements**: `Element`[]

#### Returns

`string`[]

#### Source

src/utils/OverflowWatcher/index.ts:188

---

### canNotRegisterNotOverFlow()

> `private` **canNotRegisterNotOverFlow**(`id`): `boolean`

#### Parameters

• **id**: `string`

#### Returns

`boolean`

#### Source

src/utils/OverflowWatcher/index.ts:96

---

### canOverFlowElement()

> `private` **canOverFlowElement**(`element`): `boolean`

#### Parameters

• **element**: `Element`

#### Returns

`boolean`

#### Source

src/utils/OverflowWatcher/index.ts:158

---

### clearOverFlow()

> `private` **clearOverFlow**(): `void`

#### Returns

`void`

#### Source

src/utils/OverflowWatcher/index.ts:126

---

### destroy()

> **destroy**(): `void`

#### Returns

`void`

#### Source

src/utils/OverflowWatcher/index.ts:58

---

### exceedsAvaliableSize()

> `private` **exceedsAvaliableSize**(`sumElementsSize`, `elements`, `avaliableSize`): `boolean`

#### Parameters

• **sumElementsSize**: `number`

• **elements**: `Element`[]

• **avaliableSize**: `number`

#### Returns

`boolean`

#### Source

src/utils/OverflowWatcher/index.ts:167

---

### forceUpdate()

> **forceUpdate**(): `void`

#### Returns

`void`

#### Source

src/utils/OverflowWatcher/index.ts:62

---

### getDataElementId()

> `private` **getDataElementId**(`element`): `string`

#### Parameters

• **element**: `Element`

#### Returns

`string`

#### Source

src/utils/OverflowWatcher/index.ts:163

---

### getElementSizeProps()

> `private` **getElementSizeProps**(`element`): `SizeProps`

#### Parameters

• **element**: `Element`

#### Returns

`SizeProps`

#### Source

src/utils/OverflowWatcher/index.ts:198

---

### handleResize()

> `private` **handleResize**(`entries`): `void`

#### Parameters

• **entries**: `ResizeObserverEntry`[]

#### Returns

`void`

#### Source

src/utils/OverflowWatcher/index.ts:68

---

### hasChangedSize()

> `private` **hasChangedSize**(`elementSize`): `boolean`

#### Parameters

• **elementSize**: `number`

#### Returns

`boolean`

#### Source

src/utils/OverflowWatcher/index.ts:100

---

### isElementOverFlowing()

> `private` **isElementOverFlowing**(`elementsThatFit`, `element`): `boolean`

#### Parameters

• **elementsThatFit**: `Element`[]

• **element**: `Element`

#### Returns

`boolean`

#### Source

src/utils/OverflowWatcher/index.ts:154

---

### isOverFlowed()

> `private` **isOverFlowed**(`el`): `boolean`

#### Parameters

• **el**: `Element`

#### Returns

`boolean`

#### Source

src/utils/OverflowWatcher/index.ts:227

---

### proccessElements()

> `private` **proccessElements**(`elementSize`, `children`): `void`

#### Parameters

• **elementSize**: `number`

• **children**: `Element`[]

#### Returns

`void`

#### Source

src/utils/OverflowWatcher/index.ts:112

---

### proccessElementsOverFlow()

> `private` **proccessElementsOverFlow**(`allElements`, `avaliableSize`): `void`

#### Parameters

• **allElements**: `Element`[]

• **avaliableSize**: `number`

#### Returns

`void`

#### Source

src/utils/OverflowWatcher/index.ts:131

---

### registerElementSize()

> `private` **registerElementSize**(`element`): `void`

#### Parameters

• **element**: `Element`

#### Returns

`void`

#### Source

src/utils/OverflowWatcher/index.ts:193

---

### registerNotOverflowProps()

> `private` **registerNotOverflowProps**(`children`): `void`

#### Parameters

• **children**: `Element`[]

#### Returns

`void`

#### Source

src/utils/OverflowWatcher/index.ts:88

---

### updateOverFlowedItems()

> `private` **updateOverFlowedItems**(`container`, `containerSize`): `void`

#### Parameters

• **container**: `HTMLElement`

• **containerSize**: `number`

#### Returns

`void`

#### Source

src/utils/OverflowWatcher/index.ts:80
