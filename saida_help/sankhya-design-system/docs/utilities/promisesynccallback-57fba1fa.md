---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/PromiseSyncCallback"
titulo: "PromiseSyncCallback"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/interfaces/PromiseSyncCallback"
trilha: "Docs > Utilities > Api > Interfaces > Promisesynccallback"
---

# PromiseSyncCallback

[**@sankhyalabs/core**](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/) • **Docs**

---

[@sankhyalabs/core](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/globals) / PromiseSyncCallback

# Interface: PromiseSyncCallback<T>

Representa o callback de um sincronizador `PromiseSync<T>`.

## Type parameters

• **T**

## Methods

### resolve()

> **resolve**(`result`): `void`

Será chamado sempre que todas as promessas adicionadas finalizarem.

#### Parameters

• **result**: `PromiseSettledResult`<`Awaited`<`T`>>[]

A lista com o resultado de todas as promises aguardadas.

#### Returns

`void`

#### Source

src/async/PromiseSync.ts:48
