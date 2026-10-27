---
id: "https://gilded-nasturtium-6b64dd.netlify.app/blog/diretrizes-de-documentacao"
titulo: "Diretrizes de documentação"
url: "https://gilded-nasturtium-6b64dd.netlify.app/blog/diretrizes-de-documentacao"
trilha: "Blog > Diretrizes De Documentacao"
---

# Diretrizes de documentação

17 de fevereiro de 2023 · 4 min para ler

![Heliton Rodovalho](https://gilded-nasturtium-6b64dd.netlify.app/img/authors/HelitonRodovalho.png)

Heliton Rodovalho

Developer Specilist

O escopo desta seção é referente aos comentários TSDoc colocados diretamente acima das anotações do Stencil no projeto EzUI.

## Propriedades

Antes de nos preocupar com o texto propriamente dito devemos entender que toda a estrutura da propriedade é levada em consideração ao gerar a documentação.
**Por exemplo**: valor padrão, tipo, se a propriedade se reflete na tag, etc.

Toda propriedade precisa ser o mais específica possível em relação a tipos.
Quando não houver um tipo especifico e sim uma lista de valores possíveis, devemos usar o [union types do typescript](https://www.w3schools.com/typescript/typescript_union_types.php).

**Por exemplo:**

```
// ⛔️ Genérico demais:
@Prop({ reflect: true }) mode: string = "regular";

// ✅ Mais específico:
@Prop({ reflect: true }) mode: "link" | "icon" | "label-icon" | undefined = "regular";
```

- O valor padrão também é importante para documentar o que precisa efetivamente ser atribuído ao componente.
- Todo atributo anotado com `@Prop` deve ter uma documentação informando o que representa para o componente. Essa documentação deve ser clara e objetiva detalhando exatamente como interfere no comportamento do componente.
- Seja direto e evite ambiguidades: Utilize "Define o tamanho do ez-button" no lugar de "É possível escolher entre [small,medium,large]".
- Não é necessário comentar quais valores serão aceitos, pois já são gerados automaticamente.
- Flags devem ser descritas pelo que acontece quando alteradas: Utilize "Se true define o backgroud transparente para o botão" ao invés de "Define se o background do botão será transparent".
- Sempre colocar o comportamento que a `@Prop` altera.
- Para propriedades booleanas lembre-se de documentar o comportamento contrário do padrão.
- Descreva também as estruturas envolvidas: Sempre que for necessário adicione exemplos de código na documentação, utilize a crase (`) para marcar o trecho como código. Exemplo: **"…Array no formato {value: string, label: string}\…"**

Além dessas regras básicas, devemos nos lembrar que a biblioteca precisa de uma linguagem padronizada, ou seja, precisamos utilizar termos semelhantes a fim de conferir padronização e coesão no texto.
Veja alguns casos que se repetem na maioria dos componentes:

```
/**
* Texto a ser apresentado como título do campo.
*/
@Prop({ reflect: true }) label: string;

/**
* Define o valor do campo.
*/
@Prop({ reflect: true, mutable: true }) value: Date;

/**
* Se false o usuário não pode interagir com o campo.
*/
@Prop({ reflect: true }) enabled: boolean = true;
```

## Funções

O nome do método é o maior responsável por explicar o que ele faz, mas isso pode não ser suficiente para o entendimento mais amplo. Podemos documentar com intuito de explicar melhor os detalhes, mas tome cuidado para não exagerar na explicação.
Veja algumas regras:

- A descrição do que o método faz sempre deve ser clara e objetiva.
- Não utilizar a palavra função ou método na documentação: "Método para fazer o foco no input".
- Utilize "Oculta o ez-calendar" no lugar de "Faz com que o componente seja ocultado".
- Utilize "Exibe o ez-popover" no lugar de "Mostra o ez-popover".
- Utilize "Obtém o modo atual do ez-check" no lugar de "Devolve o modo escolhido para o componente".
- A documentação sempre deve ter um verbo indicando uma ação.

```
/**
 * Aplica o foco no botão.
 */
@Method()
async setFocus(): Promise<void> {
  this._button.focus();
}

/**
 * Remove o foco do botão.
 */
@Method()
async setBlur(): Promise<void> {
  this._button.blur();
}
```

Não é necessário mencionar o tipo de dado que o método retorna pois essa informação é obtida na sua assinatura. Para que isso funcione é necessário que **SEMPRE sejam declarados os tipos de parâmetros e de retorno**.

Veja alguns exemplos:

```
// ⛔️ Pouco específico:
@Method()
async getMode() {
  return this.mode;
}

// ✅ Mais específico:
@Method()
async getMode(): Promise<CheckMode> {
  return this.mode;
}
```

```
// ⛔️ Pouco específico:
@Method()
async isInvalid() {
  return typeof this.errorMessage === "string" && this.errorMessage.trim() !== "";
}

// ✅ Mais específico:
@Method()
async isInvalid() Promise<boolean> {
  return typeof this.errorMessage === "string" && this.errorMessage.trim() !== "";
}
```

## Eventos

A exemplo das propriedades e dos métodos, devemos ser pontuais, descritivos e específicos com relação aos eventos.

Eventos comuns também devem ser descritos de forma padronizada.

O padrão para se descrever eventos é: “Emitido quando acontece a alteração de [estado|valor] do [nome do componente, etc]".

**Por exemplo:**

```
  /**
   * Emitido quando acontece a alteração de valor do campo.
   */
  @Event({ composed: true, bubbles: true }) ezChange: EventEmitter<IOption>;
```

```
  /**
   * Emitido quando acontece a alteração de valor do componente.
   */
  @Event({ composed: true, bubbles: true }) ezChange: EventEmitter<Tab>;
```
