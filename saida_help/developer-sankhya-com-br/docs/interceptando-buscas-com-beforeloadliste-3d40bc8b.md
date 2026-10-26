---
id: "https://developer.sankhya.com.br/docs/interceptando-buscas-com-beforeloadlistener"
titulo: "🔍 Interceptando Buscas com `@BeforeLoadListener`"
url: "https://developer.sankhya.com.br/docs/interceptando-buscas-com-beforeloadlistener"
atualizado_em: "2026-09-08T19:12:29.000Z"
---

# 🔍 Interceptando Buscas com `@BeforeLoadListener`

<br />

# 🔍 Interceptando Buscas com `@BeforeLoadListener`

O `@BeforeLoadListener` permite que você execute uma lógica personalizada sempre que uma entidade for carregada ou pesquisada via JAPE. Ele funciona interceptando a execução do "Finder", permitindo modificar filtros, adicionar ordenações ou validar parâmetros de busca antes que a consulta chegue ao banco de dados.

Esta anotação automatiza a configuração do atributo `finder-listener` no arquivo XML da entidade.

## ⚠️ Pré-requisito Fundamental

Para que o `@BeforeLoadListener` funcione, a entidade **precisa estar declarada no Dicionário de Dados** do seu projeto. Isso pode ser feito de duas formas:

1. Através de um arquivo XML de entidade (ex: `Produto.xml`) na pasta `datadicionary`.
2. Através da anotação [`@JapeEntity`](08_relational_mapping.md) em sua classe de modelo.

> **Importante:** Se a entidade não estiver declarada por nenhum destes meios, o SDK não terá onde injetar a configuração do listener.

***

## 🚀 Como Usar

Para criar um interceptor, siga estes passos:

1. Crie uma classe que implemente a interface `br.com.sankhya.jape.core.FinderListener`.
2. Anote a classe com `@BeforeLoadListener`, informando o nome da instância (entidade) que deseja interceptar.
3. Implemente o método `beforeExecute`.

### Exemplo Prático: Filtro de Segurança

Imagine que você deseja garantir que usuários de um determinado grupo só possam visualizar produtos ativos.

```java
import br.com.sankhya.jape.core.FinderListener;
import br.com.sankhya.jape.metadata.EntityMetaData;
import br.com.sankhya.jape.wrapper.FinderWrapper;
import br.com.sankhya.studio.annotations.BeforeLoadListener;

import java.util.logging.Logger;

@BeforeLoadListener(instance = "MinhaInstancia")
public class MinhaInstanciaFiltroSeguranca implements FinderListener {

    private static final Logger logger = Logger.getLogger(MinhaInstanciaFiltroSeguranca.class.getName());

    @Override
    public void beforeExecute(EntityMetaData entity, FinderWrapper finder) throws Exception {
        // Adiciona um critério de busca adicional
        finder.where("this.ATIVO = 'S'");

        logger.info("Filtro de segurança aplicado para a entidade: " + entity.getName());
    }
}
```

***

## ✨ Benefícios

* ✅ **Injeção de Dependências:** Diferente dos listeners JAPE tradicionais, aqui você pode usar `@Inject` para acessar outros serviços e repositórios.
* ✅ **Configuração Zero:** Não é necessário editar manualmente arquivos XML de entidade para registrar o listener.
* ✅ **Segurança Tipada:** O SDK valida se a sua classe realmente implementa `FinderListener` e se o nome da instância foi fornecido.

## 🚫 Restrição de Instâncias

O `@BeforeLoadListener` só pode ser utilizado em **instâncias criadas pelo seu próprio add-on**.

Não é permitido utilizá-lo em instâncias nativas do sistema (ex: `Parceiro`, `Produto` nativo, `CabecalhoNota`, etc.).

***

## 💡 Dicas e Boas Práticas

* **Cuidado com a Performance:** O método `beforeExecute` é chamado em **todas** as buscas da entidade. Evite consultas pesadas ao banco de dados dentro deste método.
* **Filtros Dinâmicos:** Use o objeto `finder` para adicionar critérios dinâmicos baseados no contexto do usuário logado (`JapeSession.getContext().getUserID()`).
* **Apenas uma instância:** Cada entidade só pode ter **um** `@BeforeLoadListener`. Se você declarar múltiplos para a mesma instância, o SDK reportará um erro de compilação.
