---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/ColumnFilterManager"
titulo: "ColumnFilterManager"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/ColumnFilterManager"
trilha: "Docs > Utilities > Api > Classes > Columnfiltermanager"
---

# ColumnFilterManager

[**@sankhyalabs/core**](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/) • **Docs**

---

[@sankhyalabs/core](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/globals) / ColumnFilterManager

# Class: ColumnFilterManager

## Constructors

### new ColumnFilterManager()

> **new ColumnFilterManager**(): [`ColumnFilterManager`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/ColumnFilterManager)

#### Returns

[`ColumnFilterManager`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/ColumnFilterManager)

## Methods

### compileDistinct()

> `static` **compileDistinct**(`fieldName`, `dataUnit`): `IMultiSelectionOption`[]

#### Parameters

• **fieldName**: `string`

• **dataUnit**: [`DataUnit`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/DataUnit)

#### Returns

`IMultiSelectionOption`[]

#### Source

src/utils/ColumnFilterManager.ts:74

---

### compileDistinctFromArray()

> `static` **compileDistinctFromArray**(`fieldName`, `dataUnit`, `records`): `IMultiSelectionOption`[]

#### Parameters

• **fieldName**: `string`

• **dataUnit**: [`DataUnit`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/DataUnit)

• **records**: [`Record`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/Record)[]

#### Returns

`IMultiSelectionOption`[]

#### Source

src/utils/ColumnFilterManager.ts:80

---

### doCompileDistinct()

> `static` `private` **doCompileDistinct**(`request`, `fieldName`, `dataUnit`, `list`): `IMultiSelectionOption`[]

#### Parameters

• **request**: `undefined` | [`LoadDataRequest`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/LoadDataRequest)

• **fieldName**: `string`

• **dataUnit**: [`DataUnit`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/DataUnit)

• **list**: [`Record`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/Record)[]

#### Returns

`IMultiSelectionOption`[]

#### Source

src/utils/ColumnFilterManager.ts:85

---

### getColumnFilters()

> `static` **getColumnFilters**(`filters`, `fieldName`): `Map`<`string`, `IColumnFilter`>

#### Parameters

• **filters**: [`Filter`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/Filter)[]

• **fieldName**: `string`

#### Returns

`Map`<`string`, `IColumnFilter`>

#### Source

src/utils/ColumnFilterManager.ts:12

---

### getFilterFunction()

> `static` **getFilterFunction**(`dataUnit`, `filters`?): `undefined` | (`record`) => `boolean`

#### Parameters

• **dataUnit**: [`DataUnit`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/DataUnit)

• **filters?**: `IColumnFilter`[]

#### Returns

`undefined` | (`record`) => `boolean`

#### Source

src/utils/ColumnFilterManager.ts:31

---

### recordMatchesFilter()

> `static` `private` **recordMatchesFilter**(`dataUnit`, `record`, `columnFilter`): `boolean`

#### Parameters

• **dataUnit**: [`DataUnit`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/DataUnit)

• **record**: [`Record`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/Record)

• **columnFilter**: `IColumnFilter`

#### Returns

`boolean`

#### Source

src/utils/ColumnFilterManager.ts:44
