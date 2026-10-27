---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/ServiceUtils"
titulo: "ServiceUtils"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/ServiceUtils"
trilha: "Docs > Utilities > Api > Classes > Serviceutils"
---

# ServiceUtils

[**@sankhyalabs/core**](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/) • **Docs**

---

[@sankhyalabs/core](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/globals) / ServiceUtils

# Class: ServiceUtils

## Constructors

### new ServiceUtils()

> **new ServiceUtils**(): [`ServiceUtils`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/ServiceUtils)

#### Returns

[`ServiceUtils`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/ServiceUtils)

## Methods

### useCacheWithService()

> `static` **useCacheWithService**<`T`>(`identifier`, `fetchFunction`, `storageType`): `Promise`<`T`>

Auxilia no uso do CacheManager, gerando automaticamente uma chave de cache com base no identificador.

#### Type parameters

• **T**

Tipo do dado a ser retornado.

#### Parameters

• **identifier**: `string`

Identificadores únicos usados para compor a chave de cache.

• **fetchFunction**

Função que retorna uma `Promise` com o valor a ser armazenado no cache caso ele não exista ou tenha expirado.

• **storageType**: [`StorageType`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/enumerations/StorageType)= `StorageType.IN_MEMORY_CACHE`

Tipo de armazenamento: `'sessionStorage'` ou `'localStorage'`. O padrão é `'sessionStorage'`.

#### Returns

`Promise`<`T`>

Uma `Promise` com o valor armazenado ou obtido via `fetchFunction`.

#### Example

```
const actions = await useCacheWithService(
 `${this.entityName} - ${this.resourceID}`,
  async () => {
    return await fetchActionsFromAPI();
  }
);
console.log(actions);
```

#### Source

src/utils/ServiceUtils.ts:28
