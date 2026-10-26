---
id: "https://developer.sankhya.com.br/docs/07_listeners"
titulo: "🎧 Listeners: Reagindo a Eventos de Persistência"
url: "https://developer.sankhya.com.br/docs/07_listeners"
atualizado_em: "2025-11-10T23:36:31.000Z"
---

# 🎧 Listeners: Reagindo a Eventos de Persistência

Guia para criar listeners que reagem a eventos de persistência (ex: após inserir um registro).

> 📘 **Disponibilidade**: Funcionalidade disponível a partir da versão 2.0 do Add-on Studio.

A anotação `@Listener` é um hook de baixo nível que permite "escutar" e reagir a eventos de persistência (CRUD: Create, Read, Update, Delete) de **qualquer entidade (JAPE)** do sistema. É a ferramenta ideal para criar lógicas transversais, como auditoria, validações genéricas ou integrações, que são acionadas quando dados são inseridos, atualizados ou excluídos no banco de dados.

Diferente de `@BusinessRule` e `@Callback`, que reagem a eventos de negócio de alto nível (como "confirmar nota"), o `@Listener` opera diretamente na camada de persistência.

***

### 🤔 Para que serve?

Use um `@Listener` para executar lógicas que devem ser aplicadas de forma genérica a uma ou mais entidades durante as operações de CRUD.

**Casos de uso comuns:**

* **Auditoria**: Gravar logs detalhados sobre quem alterou, inseriu ou excluiu um registro em qualquer tabela.
* **Validações Genéricas**: Aplicar uma regra de validação a todas as entidades que possuem um determinado campo (ex: validar o formato de um CNPJ em `Parceiro`, `Empresa`, etc.).
* **Sincronização de Dados**: Manter campos denormalizados atualizados. Por exemplo, ao alterar a descrição de um produto, replicar essa descrição para outras tabelas relacionadas.
* **Disparar Integrações Assíncronas**: Enfileirar uma mensagem (JMS) ou iniciar uma tarefa assíncrona (`CompletableFuture`) para notificar sistemas externos sobre uma mudança de dados, sem impactar a performance da transação principal.

***

### ⚠️ Listener vs. BusinessRule vs. Callback: Qual Usar?

Entender a diferença entre esses três hooks é crucial para uma arquitetura limpa e eficiente.

| Ferramenta      | Foco Principal                                    | Quando Usar                                                                                                                                                                            |
| :-------------- | :------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`@Listener`** | **Eventos de Persistência de Baixo Nível** (CRUD) | Para lógicas genéricas de CRUD (validação, auditoria, modificação) que se aplicam a **qualquer entidade** (JAPE) do sistema, não apenas documentos comerciais.                         |
| `@BusinessRule` | **Ciclo de Vida da Confirmação/Faturamento**      | Para lógicas complexas na confirmação/faturamento de **notas de saída** que precisam interagir com o **barramento de regras** (ex: solicitar liberação de limites).                    |
| `@Callback`     | **Eventos de Negócio de Alto Nível** (Comercial)  | Para reagir a ações como "Confirmar Nota" ou "Faturar" em **todos os tipos de nota** (incluindo entrada). É mais simples que uma `@BusinessRule` e mais específico que um `@Listener`. |

**Resumo:** Se a sua lógica precisa rodar no `beforeInsert` de `Produto`, `Parceiro` e `Nota`, use **`@Listener`**. Se a lógica é "solicitar liberação de limite ao confirmar uma venda", use **`@BusinessRule`**. Se é "enviar um e-mail após a confirmação de uma nota de compra", use **`@Callback`**.

***

### ⚙️ Como Funciona

Para criar um listener, anote uma classe que estende `br.com.sankhya.jape.event.PersistenceEventAdapter` com `@Listener`.

#### Atributos da Anotação `@Listener`

* `instanceNames`: Um array de `String` contendo os nomes das entidades (instâncias JAPE) que este listener irá monitorar.

#### Classe `PersistenceEventAdapter`

Esta classe base oferece métodos que podem ser sobrescritos para reagir a eventos específicos do ciclo de vida da persistência. Os mais comuns são:

* `beforeInsert(PersistenceEvent event)`
* `afterInsert(PersistenceEvent event)`
* `beforeUpdate(PersistenceEvent event)`
* `afterUpdate(PersistenceEvent event)`
* `beforeDelete(PersistenceEvent event)`
* `afterDelete(PersistenceEvent event)`

#### O Objeto `PersistenceEvent`

O parâmetro `event` é seu ponto de acesso ao contexto da operação:

* `event.getVo()`: O `DynamicVO` com os dados da entidade que está sofrendo a ação.
* `event.getOldVO()`: O `DynamicVO` com os dados originais antes da alteração (disponível em `before/afterUpdate` e `before/afterDelete`).
* `event.getJdbcWrapper()`: O wrapper JDBC para executar operações de banco de dados **dentro da transação corrente**.

***

### 🧩 Exemplo Prático: Auditoria Genérica

O exemplo abaixo cria um listener que grava um log em uma tabela customizada (`AD_AUDITORIA`) sempre que uma nota (`CabecalhoNota`) ou um financeiro (`Financeiro`) é inserido.

```java
package br.com.fabricante.addon.listeners;

import br.com.sankhya.jape.event.PersistenceEvent;
import br.com.sankhya.jape.event.PersistenceEventAdapter;
import br.com.sankhya.jape.wrapper.JapeFactory;
import br.com.sankhya.jape.wrapper.JapeWrapper;
import br.com.sankhya.jape.wrapper.fluid.FluidCreateVO;
import br.com.sankhya.studio.annotations.Listener;
import br.com.sankhya.modelcore.auth.AuthenticationInfo;
import br.com.sankhya.jape.util.JdbcWrapper;

@Listener(instanceNames = {"CabecalhoNota", "Financeiro"})
public class AuditoriaListener extends PersistenceEventAdapter {

    @Override
    public void afterInsert(PersistenceEvent event) throws Exception {
        // ✅ Boa prática: Obter o JDBC Wrapper do evento para garantir
        // que a operação de auditoria ocorra na mesma transação.
        JdbcWrapper jdbc = event.getJdbcWrapper();
        
        JapeWrapper auditoriaDAO = JapeFactory.dao("AD_AUDITORIA", jdbc);
        FluidCreateVO log = auditoriaDAO.create();
        
        log.set("TABELA", event.getVo().getEntityName());
        log.set("USUARIO", AuthenticationInfo.getCurrent().getUserID());
        log.set("EVENTO", "INSERT");
        log.set("DESCRICAO", "Novo registro inserido com a chave: " + event.getVo().getPrimaryKey());
        
        log.save();
        
        // ❗️ Correto: Não fechar o jdbc! O framework gerencia o ciclo de vida.
    }
}
```

***

### ✨ Boas Práticas

* **Use o`JdbcWrapper` do Evento**: Sempre obtenha a conexão com o banco a partir de `event.getJdbcWrapper()`. Isso garante que sua operação execute dentro da transação correta.
* **Use Assincronismo para Integrações**: Para integrações com sistemas externos (APIs, Web Services), **nunca** faça chamadas síncronas. Isso bloqueia a transação principal e degrada a performance do CRUD. A abordagem correta é disparar uma tarefa assíncrona.
  ```java
  // Exemplo de como disparar uma tarefa assíncrona
  CompletableFuture.runAsync(() -> {
      // Lógica de integração (ex: chamar uma API REST)
      // Esta lógica rodará em uma thread separada.
  });
  ```
* **Mantenha a Lógica Enxuta**: Listeners devem ser rápidos. Delegue regras de negócio complexas para classes de serviço (`@Service`) para manter o código organizado e testável.
* **Validações Bloqueantes**: Para impedir uma operação (em eventos `before...`), lance uma exceção. A mensagem será exibida ao usuário. Ex: `throw new Exception("O campo X é obrigatório.")`.

### 🚫 Anti-Patterns (O que evitar)

* **Usar para Eventos de Negócio**: Não use `@Listener` para reagir a eventos como "confirmação de nota". O listener será acionado em qualquer `UPDATE`, não apenas na confirmação, levando a execuções indesejadas. Para isso, use `@BusinessRule` ou `@Callback`.
* **Obter`JdbcWrapper` da`EntityFacadeFactory`** : Chamar `EntityFacadeFactory.getDWFFacade().getJdbcWrapper()` pode retornar uma conexão fora da transação atual, causando inconsistência de dados e locks.
* **Fechar a Conexão**: Nunca chame `jdbc.close()` no `JdbcWrapper` obtido do evento. O framework é responsável por gerenciar o ciclo de vida da conexão.
* **Lógica de Negócio Específica de Documentos**: Se a lógica se aplica apenas ao ciclo de vida de documentos comerciais (pedidos, notas), `@BusinessRule` ou `@Callback` são mais semânticos e apropriados.
