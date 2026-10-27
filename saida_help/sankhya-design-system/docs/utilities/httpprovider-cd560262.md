---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/HttpProvider"
titulo: "HttpProvider"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/HttpProvider"
trilha: "Docs > Utilities > Api > Classes > Httpprovider"
---

# HttpProvider

[**@sankhyalabs/core**](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/) • **Docs**

---

[@sankhyalabs/core](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/globals) / HttpProvider

# Class: HttpProvider

Abstração do XMLHttpRequest. Este serviço é responsável por realizar as requisições
ao backend. Todos os métodos são estáticos.

## Constructors

### new HttpProvider()

> **new HttpProvider**(): [`HttpProvider`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/HttpProvider)

#### Returns

[`HttpProvider`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/HttpProvider)

## Methods

### dispatch()

> `static` `private` **dispatch**(`requestMetadata`, `payload`?): `Promise`<`any`>

#### Parameters

• **requestMetadata**: [`RequestMetadata`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/RequestMetadata)

• **payload?**: `Object`

#### Returns

`Promise`<`any`>

#### Source

src/http/HttpProvider.ts:32

---

### get()

> `static` **get**(`url`, `headers`?): `Promise`<`Object`>

Faz uma requisição usando o método GET do HTTP para uma URL específica.

#### Parameters

• **url**: `string`

A URL que deve ser chamada.

• **headers?**: `Header`[]

[Opcional] Cabeçalhos HTTP.

#### Returns

`Promise`<`Object`>

Uma promessa de que a requisição será preenchida.

#### Source

src/http/HttpProvider.ts:16

---

### post()

> `static` **post**(`url`, `payload`, `headers`?): `Promise`<`any`>

Faz uma requisição usando o método POST do HTTP para uma URL específica.

#### Parameters

• **url**: `string`

A URL que deve ser chamada.

• **payload**: `Object`

Informações a serem enviadas.

• **headers?**: `Header`[]

[Opcional] Cabeçalhos HTTP.

#### Returns

`Promise`<`any`>

Uma promessa de que a requisição será preenchida.

#### Source

src/http/HttpProvider.ts:28
