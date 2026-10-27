---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/ErrorTracking"
titulo: "ErrorTracking"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/ErrorTracking"
trilha: "Docs > Utilities > Api > Classes > Errortracking"
---

# ErrorTracking

[**@sankhyalabs/core**](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/) • **Docs**

---

[@sankhyalabs/core](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/globals) / ErrorTracking

# Class: ErrorTracking

`ErrorTracking`: Handler para processar exceptions lançadas.

## Constructors

### new ErrorTracking()

> **new ErrorTracking**(): [`ErrorTracking`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/ErrorTracking)

#### Returns

[`ErrorTracking`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/ErrorTracking)

## Methods

### init()

> `static` **init**(): `void`

Inicializa o Rollbar, utilizado para rastreio de erros e análise de logs.

#### Returns

`void`

#### Source

src/traking/ErrorTraking.ts:16

---

### isInternalException()

> `static` `private` **isInternalException**(`error`): `boolean`

Retorna se o erro é uma exceção interna na aplicação.

#### Parameters

• **error**: `any`

Erro que será identificado como exceção interna ou não.

#### Returns

`boolean`

- Verdadeiro caso seja uma exceção interna.

#### Source

src/traking/ErrorTraking.ts:34
