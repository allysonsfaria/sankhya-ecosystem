---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/DataUnitStorage"
titulo: "DataUnitStorage"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/DataUnitStorage"
trilha: "Docs > Utilities > Api > Classes > Dataunitstorage"
---

# DataUnitStorage

[**@sankhyalabs/core**](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/) • **Docs**

---

[@sankhyalabs/core](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/globals) / DataUnitStorage

# Class: DataUnitStorage

Classe responsável por armazenar instâncias de DataUnit.

## Constructors

### new DataUnitStorage()

> **new DataUnitStorage**(): [`DataUnitStorage`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/DataUnitStorage)

#### Returns

[`DataUnitStorage`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/DataUnitStorage)

## Properties

### dataUnitMap

> `static` `private` **dataUnitMap**: `WeakMap`<`object`, [`DataUnit`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/DataUnit)>

#### Type declaration

##### key

> **key**: `string`

#### Source

src/dataunit/DataUnitStorage.ts:7

---

### keyMap

> `static` `private` **keyMap**: `Map`<`string`, `object`>

#### Source

src/dataunit/DataUnitStorage.ts:8

## Methods

### get()

> `static` **get**(`dataUnitName`): `undefined` | [`DataUnit`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/DataUnit)

Retorna uma instância de DataUnit armazenada no DataUnitStorage.

#### Parameters

• **dataUnitName**: `string`

O nome do DataUnit.

#### Returns

`undefined` | [`DataUnit`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/DataUnit)

- A instância do DataUnit ou undefined caso não seja encontrada.

#### Source

src/dataunit/DataUnitStorage.ts:15

---

### put()

> `static` **put**(`dataUnit`): `void`

Armazena uma instância de DataUnit no DataUnitStorage.

#### Parameters

• **dataUnit**: [`DataUnit`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/DataUnit)

A instância de DataUnit a ser armazenada.

#### Returns

`void`

#### Source

src/dataunit/DataUnitStorage.ts:24

---

### remove()

> `static` **remove**(`dataUnit`): `void`

Remove uma instância de DataUnit do DataUnitStorage.

#### Parameters

• **dataUnit**: `string` | [`DataUnit`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/DataUnit)

A instância de DataUnit ou o nome do DataUnit a ser removido.

#### Returns

`void`

#### Source

src/dataunit/DataUnitStorage.ts:34
