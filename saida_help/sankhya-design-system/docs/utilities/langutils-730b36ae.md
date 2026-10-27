---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/LangUtils"
titulo: "LangUtils"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/LangUtils"
trilha: "Docs > Utilities > Api > Classes > Langutils"
---

# LangUtils

[**@sankhyalabs/core**](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/) • **Docs**

---

[@sankhyalabs/core](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/globals) / LangUtils

# Class: LangUtils

A classe `LangUtils` fornece métodos utilitários para gerenciar configurações de
idioma, incluindo recuperar, definir e aplicar preferências de idioma.

## Constructors

### new LangUtils()

> **new LangUtils**(): [`LangUtils`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/LangUtils)

#### Returns

[`LangUtils`](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/LangUtils)

## Properties

### ELanguages

> `static` **ELanguages**: typeof `__class`

Classe estática contendo os códigos de idioma predefinidos.

#### Source

src/utils/LangUtils.ts:14

## Methods

### applyLanguageFromCookie()

> `static` **applyLanguageFromCookie**(): `void`

Define o atributo `lang` no elemento `<html>` com base no cookie de idioma, se existir.

#### Returns

`void`

#### Example

```
LangUtils.applyLanguageFromCookie(); // Aplica o idioma do cookie ao elemento `<html>`
```

#### Source

src/utils/LangUtils.ts:123

---

### convertLanguage()

> `static` `private` **convertLanguage**(`lang`): `string`

Converte o idioma fornecido para um dos códigos predefinidos.

#### Parameters

• **lang**: `string`

O idioma a ser convertido (ex.: "en", "es", "pt-BR").

#### Returns

`string`

O código de idioma correspondente (ex.: "en\_US", "es\_ES").

#### Example

```
LangUtils.convertLanguage("en"); // Retorna "en_US"
LangUtils.convertLanguage("es-es"); // Retorna "es_ES"
```

#### Source

src/utils/LangUtils.ts:30

---

### getHtmlLanguage()

> `static` **getHtmlLanguage**(): `string`

Recupera o valor do atributo `lang` do elemento `<html>`. Se o ambiente
estiver em modo de desenvolvimento, o idioma padrão será `"pt_BR"`. Caso
contrário, utiliza o idioma do navegador ou `"pt-BR"` como padrão.

#### Returns

`string`

O idioma definido no elemento `<html>` ou o padrão.

#### Example

```
LangUtils.getHtmlLanguage(); // Retorna "pt_BR" no modo desenvolvimento
```

#### Source

src/utils/LangUtils.ts:77

---

### getLanguage()

> `static` **getLanguage**(): `string`

Captura o idioma atualmente definido. Primeiro verifica se há um idioma
armazenado nos cookies. Caso contrário, utiliza o idioma definido no elemento
`<html>`. Se nenhum valor for encontrado nos cookies ou no elemento `<html>`,
é utilizada a configuração do navegador. Caso o navegador também não forneça
um idioma, o padrão será `"pt_BR"`.

#### Returns

`string`

O idioma definido (ex.: "pt\_BR", "en\_US").

#### Example

```
LangUtils.getLanguage(); // Retorna o idioma atual
```

#### Source

src/utils/LangUtils.ts:57

---

### getLanguageFromCookie()

> `static` **getLanguageFromCookie**(): `null` | `string`

Recupera o valor do cookie de idioma.

#### Returns

`null` | `string`

O valor do cookie de idioma ou `null` se não existir.

#### Example

```
LangUtils.getLanguageFromCookie(); // Retorna "pt_BR" se o cookie existir
```

#### Source

src/utils/LangUtils.ts:112

---

### setHtmlLanguage()

> `static` **setHtmlLanguage**(`language`): `void`

Define o atributo `lang` no elemento `<html>` e atualiza o cookie de idioma.

#### Parameters

• **language**: `string`

O idioma a ser definido (ex.: "pt\_BR", "en\_US").

> **Nota:** Definir o idioma no elemento `<html>` é essencial para garantir que o conteúdo
> da página seja interpretado corretamente por navegadores, leitores de tela e mecanismos de
> busca, melhorando a acessibilidade e a indexação.

#### Returns

`void`

#### Example

```
LangUtils.setHtmlLanguage("en_US"); // Define o idioma como "en_US"
```

#### Source

src/utils/LangUtils.ts:99
