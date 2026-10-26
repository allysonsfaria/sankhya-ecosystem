---
id: "https://developer.sankhya.com.br/docs/07_telas"
titulo: "💻 Telas Personalizadas (UI)"
url: "https://developer.sankhya.com.br/docs/07_telas"
atualizado_em: "2025-11-10T23:36:02.000Z"
---

# 💻 Telas Personalizadas (UI)

Quando os [Formulários Dinâmicos](https://developer.sankhya.com.br/docs/03_dynamicform.md) não são suficientes e você precisa de total controle sobre a interface, o Add-on Studio permite a criação de telas personalizadas usando a tecnologia [HTML5 da Sankhya](https://developer.sankhya.com.br/docs/sankhya-js).

Isso é ideal para dashboards, relatórios complexos ou qualquer interface que exija um layout e comportamento específicos.

***

### 🏗️ Como Funciona?

A criação de uma tela personalizada envolve dois passos principais:

1. **Criar o Arquivo da View**: Desenvolver o arquivo `.xhtml5` com a estrutura da sua tela.
2. **Declarar a Tela no Menu**: Usar a tag `<ui>` no dicionário de dados para vincular o arquivo a um item de menu.

***

### 🛠️ Passo a Passo: Criando uma Tela

#### Passo 1: Crie o Arquivo da View

1. Dentro do seu projeto, navegue até `src/main/webapp/`.
2. Crie uma estrutura de pastas para organizar suas telas (ex: `src/main/webapp/html5/`).
3. Crie seu arquivo de view, por exemplo, `minha_tela.xhtml5`.

#### Passo 2: Adicione a Tela ao Menu

Agora, edite seu arquivo de menu no dicionário de dados (ex: `SGT_MENU.xml`) e adicione a tag `<ui>`.

```xml
<!-- arquivo: src/main/resources/datadictionary/SGT_MENU.xml -->
<?xml version="1.0" encoding="ISO-8859-1"?>
<metadados xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
           xsi:noNamespaceSchemaLocation="../.gradle/metadados.xsd">

    <menu id="SGT_MEUMENU" description="Super Gestão">
        <!-- A tag <ui> cria um link para sua tela personalizada -->
        <ui id="SGT_MINHA_TELA" 
            url="/$ctx/telas/minha_tela.xhtml5" 
            description="Minha Primeira Tela"/>
    </menu>
</metadados>
```

**Atributos da tag`<ui>`:**

| Atributo      | Descrição                                                        | Exemplo                         |
| :------------ | :--------------------------------------------------------------- | :------------------------------ |
| `id`          | Identificador único para o item de menu da tela.                 | `SGT_MINHA_TELA`                |
| `url`         | **O mais importante**: O caminho para o seu arquivo `.xhtml5`.   | `/$ctx/telas/minha_tela.xhtml5` |
| `description` | O texto que aparecerá no menu para o usuário.                    | `Minha Primeira Tela`           |
| `resourceId`  | (Opcional) Usado para compatibilidade com add-ons legados (DWF). | `54321`                         |

> **Importante**: A variável `/$ctx/` é fundamental. Ela é substituída em tempo de execução pelo caminho raiz do seu add-on, garantindo que o sistema encontre seu arquivo de view corretamente. **Sempre a utilize no início da URL.**

***

### ✨ Boas Práticas

* **Organize suas Views**: Crie subpastas dentro de `src/main/webapp/` para organizar suas telas, scripts e folhas de estilo (ex: `/telas`, `/js`, `/css`).
* **Use um Prefixo Único**: Assim como nos menus e tabelas, use um prefixo exclusivo nos IDs das suas tags `<ui>` para evitar conflitos.
* **Componentização**: Para telas complexas, utilize componentes JSF (JavaServer Faces) para reutilizar partes da sua interface.

### 🚫 Anti-Patterns (O que evitar)

* **Uso do Prefixo`AD_`** : Não use o prefixo `AD_`. Ele é genérico e pode levar a conflitos. Crie um prefixo único para seu projeto.
* **Esquecer o`/$ctx/`** : Não usar a variável `/$ctx/` na URL fará com que o sistema não encontre sua tela, resultando em um erro 404.
* **IDs Duplicados**: Usar o mesmo `id` para diferentes itens de menu (`<ui>`, `<dynamicForm>`, etc.) causará conflitos.
* **Expor Lógica de Negócio na View**: A tela (XHTML) deve ser responsável apenas pela apresentação. Mantenha a lógica de negócio em classes Java (Beans) que se comunicam com a view.
