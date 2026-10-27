---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/FieldComparator"
titulo: "FieldComparator"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/FieldComparator"
trilha: "Docs > Utilities > Api > Classes > Fieldcomparator"
---

# FieldComparator

[**@sankhyalabs/core**](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/) • **Docs**

---

[@sankhyalabs/core](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/globals) / FieldComparator

# Class: FieldComparator

## Constructors

### new FieldComparator()

> **new FieldComparator**(): [`FieldComparator`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/FieldComparator)

#### Returns

[`FieldComparator`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/FieldComparator)

## Methods

### compare()

> `static` **compare**(`field`, `recordA`, `recordB`, `asc`, `onlyLabel`): `number`

#### Parameters

• **field**: [`FieldDescriptor`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/FieldDescriptor)

• **recordA**: [`Record`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/Record)

• **recordB**: [`Record`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/Record)

• **asc**: `boolean`= `true`

• **onlyLabel**: `boolean`= `false`

#### Returns

`number`

#### Source

src/dataunit/sorting/FieldComparator.ts:7

---

### compareUndefined()

> `static` **compareUndefined**(`isUndefinedA`, `isUndefinedB`): `undefined` | `number`

#### Parameters

• **isUndefinedA**: `boolean`

• **isUndefinedB**: `boolean`

#### Returns

`undefined` | `number`

#### Source

src/dataunit/sorting/FieldComparator.ts:19

---

### compareValues()

> `static` **compareValues**(`descriptor`, `valueA`, `valueB`, `onlyLabel`): `number`

#### Parameters

• **descriptor**: [`FieldDescriptor`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/FieldDescriptor)

• **valueA**: `any`

• **valueB**: `any`

• **onlyLabel**: `boolean`= `false`

#### Returns

`number`

#### Source

src/dataunit/sorting/FieldComparator.ts:14
