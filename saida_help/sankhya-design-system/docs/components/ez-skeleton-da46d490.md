---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-skeleton/"
titulo: "Skeleton"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-skeleton/"
trilha: "Docs > Components > Components Doc > Ez Skeleton"
---

# Skeleton

O **Skeleton** é um componente de carregamento que simula o layout do conteúdo enquanto os dados estão sendo carregados. Ele fornece feedback visual aos usuários durante os estados de carregamento.

```
<ez-skeleton></ez-skeleton>
```

```
<EzSkeleton></EzSkeleton>
```

## Variantes

O componente suporta as seguintes `variant`:

- `text (Default)`: Forma de linha de texto.

![Imagem 1: text (Default) : Forma de linha de texto.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

- `rect`: Forma retangular.

![Imagem 2: rect : Forma retangular.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

- `circle`: Forma circular.

![Imagem 3: circle : Forma circular.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Animações

Define o tipo de `animation` do componente.

- `progress (Default)`: Animação de progresso de carregamento

![Imagem 4: progress (Default) : Animação de progresso de carregamento](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

- `pulse`: Animação pulsante

![Imagem 5: pulse : Animação pulsante](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

- `false`: Sem animação

![Imagem 6: false : Sem animação](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Dimensões

É possível definir o `width` e o `height` do componente. Os valores aceitos são os mesmos aceitos pelo CSS.

![Imagem 7: É possível definir o width e o height do componente. Os valores aceitos são os mesmos aceitos pelo CSS.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Margem

O componente oferece controle individual das margens:

- `marginTop`: Margem superior
- `marginRight`: Margem direita
- `marginBottom`: Margem inferior
- `marginLeft`: Margem esquerda

![Imagem 8: marginLeft : Margem esquerda](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Contador

Repete o número de itens skeleton a serem renderizados na tela com as mesmas propriedades informadas. Por padrão o `count` do componente é sempre **1**.

![Imagem 9: Repete o número de itens skeleton a serem renderizados na tela com as mesmas propriedades informadas. Por padrão o…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Estilização via Style Props

O componente EzSkeleton permite customização através de propriedades CSS personalizadas (custom properties) passadas via prop `style`. As seguintes propriedades são suportadas:

- `--skeleton-width`: Define a largura do skeleton
- `--skeleton-height`: Define a altura do skeleton
- `--skeleton-border-radius`: Define o raio da borda
- `--skeleton-background`: Define a cor de fundo base
- `--skeleton-background-image`: Define a cor da animação
- `--skeleton-margin-top`: Define a margem superior
- `--skeleton-margin-right`: Define a margem direita
- `--skeleton-margin-bottom`: Define a margem inferior
- `--skeleton-margin-left`: Define a margem esquerda

### Exemplo de uso:

![Imagem 10: Exemplo de uso:](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Templates Dinâmicos

Define o template a ser usado para a estrutura do skeleton. O componente permite criar estruturas personalizadas de carregamento que se adaptam ao seu layout.

- Tipo: `HTMLElement | string`

### Comportamento dos Templates:

- Elementos com `class="skeleton"`: O componente renderiza o skeleton aplicando todas as propriedades disponíveis (variant, animation, width, height, etc)
- Quando elementos pai e filho possuem `class="skeleton"`: O skeleton é renderizado apenas no elemento pai, evitando duplicidade
- Elementos `sem` a `class="skeleton"`: São renderizados normalmente, permitindo customização através de classes e styles próprios

### Características dos Templates:

- Podem ser compostos por múltiplos elementos skeleton
- Herdam as propriedades de animação definidas
- Suportam diferentes variantes (circle, rect, text) em um mesmo template
- Permitem configuração individual de dimensões para cada elemento
- Mantêm a consistência de animação entre todos os elementos

### Boas Práticas:

- Use templates para replicar a estrutura exata do conteúdo final
- Combine diferentes variantes para criar layouts complexos
- Mantenha as dimensões proporcionais ao conteúdo real
- Utilize o atributo count para repetir estruturas similares
- Aplique margens adequadas para manter o espaçamento visual
- Evite usar class="skeleton" em elementos aninhados quando o pai já possui a classe

### Exemplos de Uso de Templates

![Imagem 11: Exemplos de Uso de Templates](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

![Imagem 12: Exemplos de Uso de Templates](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

![Imagem 13: Exemplos de Uso de Templates](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Acessibilidade

O componente Skeleton implementa os seguintes atributos ARIA para garantir uma melhor experiência para usuários de tecnologias assistivas:

- `role="progressbar"`: Indica que o elemento representa uma barra de progresso
- `data-busy="true"`: Comunica que o conteúdo está em estado de carregamento
- `data-valuemin="0"`: Define o valor mínimo do progresso
- `data-valuemax="100"`: Define o valor máximo do progresso
- `data-valuetext="Loading..."`: Fornece um texto descritivo do estado atual
- `tabindex="0"`: Permite que o elemento receba foco via teclado

Estes atributos são aplicados automaticamente em todos os elementos skeleton, garantindo que o componente seja acessível e forneça feedback adequado sobre seu estado de carregamento.
