---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/DataUnitInMemoryLoader"
titulo: "DataUnitInMemoryLoader"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/DataUnitInMemoryLoader"
trilha: "Docs > Utilities > Api > Classes > Dataunitinmemoryloader"
---

# DataUnitInMemoryLoader

[**@sankhyalabs/core**](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/) • **Docs**

---

[@sankhyalabs/core](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/globals) / DataUnitInMemoryLoader

# Class: DataUnitInMemoryLoader

## Constructors

### new DataUnitInMemoryLoader()

> **new DataUnitInMemoryLoader**(`metadata`?, `records`?, `config`?): [`DataUnitInMemoryLoader`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/DataUnitInMemoryLoader)

#### Parameters

• **metadata?**: [`UnitMetadata`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/UnitMetadata)

• **records?**: [`Record`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/Record)[]

• **config?**: [`DataUnitInMemoryLoaderConfig`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/DataUnitInMemoryLoaderConfig)

#### Returns

[`DataUnitInMemoryLoader`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/DataUnitInMemoryLoader)

#### Source

src/dataunit/loader/dataUnitInMemoryLoader.ts:26

## Properties

### \_dataUnit

> `private` **\_dataUnit**: [`DataUnit`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/DataUnit)

#### Source

src/dataunit/loader/dataUnitInMemoryLoader.ts:19

---

### \_initialRecords

> `private` **\_initialRecords**: [`Record`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/Record)[] = `[]`

#### Source

src/dataunit/loader/dataUnitInMemoryLoader.ts:21

---

### \_metadata

> `private` **\_metadata**: `undefined` | [`UnitMetadata`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/UnitMetadata)

#### Source

src/dataunit/loader/dataUnitInMemoryLoader.ts:20

---

### recordDateFormat

> `private` **recordDateFormat**: [`RECORD_DATE_FORMAT`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/enumerations/RECORD_DATE_FORMAT)

#### Source

src/dataunit/loader/dataUnitInMemoryLoader.ts:22

---

### DEFAULT\_PAGE\_SIZE

> `static` `readonly` **DEFAULT\_PAGE\_SIZE**: `150` = `150`

#### Source

src/dataunit/loader/dataUnitInMemoryLoader.ts:24

---

### IN\_MEMORY\_DATA\_UNIT\_NAME

> `static` `readonly` **IN\_MEMORY\_DATA\_UNIT\_NAME**: `"InMemoryDataUnit"` = `'InMemoryDataUnit'`

#### Source

src/dataunit/loader/dataUnitInMemoryLoader.ts:23

## Accessors

### dataUnit

> `get` **dataUnit**(): [`DataUnit`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/DataUnit)

#### Returns

[`DataUnit`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/DataUnit)

#### Source

src/dataunit/loader/dataUnitInMemoryLoader.ts:58

---

### metadata

> `get` **metadata**(): [`UnitMetadata`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/UnitMetadata)

> `set` **metadata**(`metadata`): `void`

#### Parameters

• **metadata**: [`UnitMetadata`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/UnitMetadata)

#### Returns

[`UnitMetadata`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/UnitMetadata)

#### Source

src/dataunit/loader/dataUnitInMemoryLoader.ts:122

---

### records

> `get` **records**(): [`Record`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/Record)[]

> `set` **records**(`records`): `void`

#### Parameters

• **records**: [`Record`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/Record)[]

#### Returns

[`Record`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/Record)[]

#### Source

src/dataunit/loader/dataUnitInMemoryLoader.ts:62

## Methods

### buildColumns()

> `private` **buildColumns**(): `undefined` | `Map`<`string`, [`FieldDescriptor`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/FieldDescriptor)>

#### Returns

`undefined` | `Map`<`string`, [`FieldDescriptor`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/FieldDescriptor)>

#### Source

src/dataunit/loader/dataUnitInMemoryLoader.ts:92

---

### buildInitialRecords()

> `private` **buildInitialRecords**(`records`, `columns`): [`Record`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/Record)[]

#### Parameters

• **records**: [`Record`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/Record)[]

• **columns**: `undefined` | `Map`<`string`, [`FieldDescriptor`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/FieldDescriptor)>

#### Returns

[`Record`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/Record)[]

#### Source

src/dataunit/loader/dataUnitInMemoryLoader.ts:98

---

### generateUniqueId()

> `private` **generateUniqueId**(): `string`

#### Returns

`string`

#### Source

src/dataunit/loader/dataUnitInMemoryLoader.ts:134

---

### getRecordsToLoad()

> `private` **getRecordsToLoad**(): [`Record`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/Record)[]

#### Returns

[`Record`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/Record)[]

#### Source

src/dataunit/loader/dataUnitInMemoryLoader.ts:46

---

### inMemoryLoader()

> `private` **inMemoryLoader**(`dataUnit`, `request`, `recordsIn`): `Promise`<[`LoadDataResponse`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/LoadDataResponse)>

#### Parameters

• **dataUnit**: [`DataUnit`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/DataUnit)

• **request**: [`LoadDataRequest`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/LoadDataRequest)

• **recordsIn**: [`Record`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/Record)[]

#### Returns

`Promise`<[`LoadDataResponse`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/LoadDataResponse)>

#### Source

src/dataunit/loader/dataUnitInMemoryLoader.ts:138

---

### metadaLoader()

> `private` **metadaLoader**(): `Promise`<[`UnitMetadata`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/UnitMetadata)>

#### Returns

`Promise`<[`UnitMetadata`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/UnitMetadata)>

#### Source

src/dataunit/loader/dataUnitInMemoryLoader.ts:142

---

### removeLoader()

> **removeLoader**(`_dataUnit`, `recordIds`): `Promise`<`string`[]>

#### Parameters

• **\_dataUnit**: [`DataUnit`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/DataUnit)

• **recordIds**: `string`[]

#### Returns

`Promise`<`string`[]>

#### Source

src/dataunit/loader/dataUnitInMemoryLoader.ts:173

---

### saveLoader()

> `private` **saveLoader**(`_dataUnit`, `changes`): `Promise`<[`SavedRecord`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/SavedRecord)[]>

#### Parameters

• **\_dataUnit**: [`DataUnit`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/DataUnit)

• **changes**: [`Change`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/Change)[]

#### Returns

`Promise`<[`SavedRecord`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/SavedRecord)[]>

#### Source

src/dataunit/loader/dataUnitInMemoryLoader.ts:146

---

### getConvertedValue()

> `static` **getConvertedValue**(`descriptor`, `strValue`, `dateFormat`?): `any`

#### Parameters

• **descriptor**: [`FieldDescriptor`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/FieldDescriptor)

• **strValue**: `string`

• **dateFormat?**: [`RECORD_DATE_FORMAT`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/enumerations/RECORD_DATE_FORMAT)

#### Returns

`any`

#### Source

src/dataunit/loader/dataUnitInMemoryLoader.ts:77
