---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/SelectionInfo"
titulo: "SelectionInfo"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/SelectionInfo"
trilha: "Docs > Utilities > Api > Classes > Selectioninfo"
---

# SelectionInfo

[**@sankhyalabs/core**](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/) • **Docs**

---

[@sankhyalabs/core](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/globals) / SelectionInfo

# Class: SelectionInfo

## Constructors

### new SelectionInfo()

> **new SelectionInfo**(`records`, `mode`, `total`?, `filters`?, `sort`?): [`SelectionInfo`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/SelectionInfo)

#### Parameters

• **records**: [`Record`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/Record)[]

• **mode**: [`SelectionMode`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/enumerations/SelectionMode)= `SelectionMode.SOME_RECORDS`

• **total?**: `number`

• **filters?**: [`Filter`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/Filter)[]

• **sort?**: [`Sort`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/Sort)[]

#### Returns

[`SelectionInfo`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/SelectionInfo)

#### Source

src/dataunit/SelectionInfo.ts:13

## Properties

### \_records

> `private` **\_records**: [`Record`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/Record)[]

#### Source

src/dataunit/SelectionInfo.ts:10

---

### \_total?

> `private` `optional` **\_total**: `number`

#### Source

src/dataunit/SelectionInfo.ts:11

---

### filters?

> `optional` **filters**: [`Filter`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/Filter)[]

#### Source

src/dataunit/SelectionInfo.ts:7

---

### getAllRecords()?

> `optional` **getAllRecords**: () => [`Record`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/Record)[]

#### Returns

[`Record`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/Record)[]

#### Source

src/dataunit/SelectionInfo.ts:9

---

### mode

> **mode**: [`SelectionMode`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/enumerations/SelectionMode)

#### Source

src/dataunit/SelectionInfo.ts:6

---

### sort?

> `optional` **sort**: [`Sort`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/Sort)[]

#### Source

src/dataunit/SelectionInfo.ts:8

## Accessors

### length

> `get` **length**(): `number`

#### Returns

`number`

#### Source

src/dataunit/SelectionInfo.ts:41

---

### recordIds

> `get` **recordIds**(): `undefined` | `string`[]

#### Returns

`undefined` | `string`[]

#### Source

src/dataunit/SelectionInfo.ts:31

---

### records

> `get` **records**(): [`Record`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/Record)[]

#### Returns

[`Record`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/Record)[]

#### Source

src/dataunit/SelectionInfo.ts:21

## Methods

### isAllRecords()

> **isAllRecords**(): `boolean`

#### Returns

`boolean`

#### Source

src/dataunit/SelectionInfo.ts:48

---

### isEmpty()

> **isEmpty**(): `boolean`

#### Returns

`boolean`

#### Source

src/dataunit/SelectionInfo.ts:52
