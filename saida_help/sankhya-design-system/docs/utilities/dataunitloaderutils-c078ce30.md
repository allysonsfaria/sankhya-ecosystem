---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/DataUnitLoaderUtils"
titulo: "DataUnitLoaderUtils"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/DataUnitLoaderUtils"
trilha: "Docs > Utilities > Api > Classes > Dataunitloaderutils"
---

# DataUnitLoaderUtils

[**@sankhyalabs/core**](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/) • **Docs**

---

[@sankhyalabs/core](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/globals) / DataUnitLoaderUtils

# Class: DataUnitLoaderUtils

## Constructors

### new DataUnitLoaderUtils()

> **new DataUnitLoaderUtils**(): [`DataUnitLoaderUtils`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/DataUnitLoaderUtils)

#### Returns

[`DataUnitLoaderUtils`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/DataUnitLoaderUtils)

## Methods

### applyFilter()

> `static` **applyFilter**(`records`, `dataUnit`, `filters`): [`Record`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/Record)[]

#### Parameters

• **records**: [`Record`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/Record)[]

• **dataUnit**: [`DataUnit`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/DataUnit)

• **filters**: [`Filter`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/Filter)[]

#### Returns

[`Record`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/Record)[]

#### Source

src/dataunit/loader/utils/dataUnitLoaderUtils.ts:12

---

### applySorting()

> `static` **applySorting**(`records`, `dataUnit`, `sorting`): [`Record`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/Record)[]

#### Parameters

• **records**: [`Record`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/Record)[]

• **dataUnit**: [`DataUnit`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/DataUnit)

• **sorting**: [`Sort`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/Sort)[]

#### Returns

[`Record`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/Record)[]

#### Source

src/dataunit/loader/utils/dataUnitLoaderUtils.ts:41

---

### buildLoadDataResponse()

> `static` **buildLoadDataResponse**(`recordsIn`, `dataUnit`, `request`): `Promise`<`object`>

#### Parameters

• **recordsIn**: [`Record`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/Record)[]

• **dataUnit**: [`DataUnit`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/DataUnit)

• **request**: [`LoadDataRequest`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/LoadDataRequest)

#### Returns

`Promise`<`object`>

##### paginationInfo

> **paginationInfo**: `undefined` | [`PaginationInfo`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/PaginationInfo)

##### records

> **records**: [`Record`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/Record)[]

#### Source

src/dataunit/loader/utils/dataUnitLoaderUtils.ts:21

---

### buildPaginationInfo()

> `static` **buildPaginationInfo**(`__namedParameters`): `undefined` | [`PaginationInfo`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/PaginationInfo)

#### Parameters

• **\_\_namedParameters**: [`PaginationInfoBuilderParams`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/PaginationInfoBuilderParams)

#### Returns

`undefined` | [`PaginationInfo`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/PaginationInfo)

#### Source

src/dataunit/loader/utils/dataUnitLoaderUtils.ts:62

---

### getPagesByRecords()

> `static` **getPagesByRecords**(`records`, `offset`, `limit`): [`Record`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/Record)[]

#### Parameters

• **records**: [`Record`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/Record)[]

• **offset**: `number`= `0`

• **limit**: `number`= `0`

#### Returns

[`Record`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/Record)[]

#### Source

src/dataunit/loader/utils/dataUnitLoaderUtils.ts:52

---

### hasValidLimitAndOffset()

> `static` `private` **hasValidLimitAndOffset**(`offset`, `limit`): `boolean`

#### Parameters

• **offset**: `number`

• **limit**: `number`

#### Returns

`boolean`

#### Source

src/dataunit/loader/utils/dataUnitLoaderUtils.ts:58
