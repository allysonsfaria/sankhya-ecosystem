---
id: "https://developer.sankhya.com.br/docs/06_business_rules"
titulo: "📜 Regras de Negócio"
url: "https://developer.sankhya.com.br/docs/06_business_rules"
atualizado_em: "2025-11-10T23:36:30.000Z"
---

# 📜 Regras de Negócio

Guia para criar regras de negócio que disparam ações automáticas com base em eventos do sistema.

> 📘 **Disponibilidade**: Funcionalidade disponível a partir da versão 2.0 do Add-on Studio.

A anotação `@BusinessRule` é o hook ideal para implementar lógicas de negócio durante os eventos de **confirmação e faturamento** de **documentos comerciais**, como Pedidos e Notas de Venda.

Embora ela também possa interceptar eventos de CRUD (Create, Read, Update, Delete), a abordagem moderna prefere o uso de **`@Listener`** para essas operações, reservando a `@BusinessRule` para as etapas mais complexas e específicas do ciclo de vida comercial.

***

### 🤔 Para que serve?

Use uma Regra de Negócio para executar validações, modificações ou iniciar processos que devem ocorrer especificamente no momento em que um documento é **confirmado** ou **faturado**.

**Casos de uso comuns:**

* **Validações de Confirmação**: Verificar o estoque disponível ou o limite de crédito do cliente apenas no momento da confirmação da nota.
* **Solicitação de Liberação de Limites**: Iniciar um processo de aprovação quando um pedido excede um determinado valor ou condição durante a tentativa de confirmação.
* **Integrações Pós-Confirmação**: Disparar **operações assíncronas** (ex: via JMS ou `CompletableFuture`) para enviar dados a sistemas externos após a confirmação, sem bloquear a thread principal.
* **Cálculos Complexos de Faturamento**: Aplicar lógicas de impostos ou comissões que dependem do estado final da nota no momento do faturamento.

***

### ⚠️ BusinessRule vs. Callback: Qual Usar?

Ambos os hooks reagem a eventos do ciclo de vida comercial, mas possuem escopos e propósitos diferentes. A escolha não se baseia em complexidade, mas sim em **aplicabilidade**.

| Hook                | Escopo de Atuação                                                            | Quando Usar                                                                                                                                                                                 |
| :------------------ | :--------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **`@BusinessRule`** | **Notas de Saída e Mov. Interna** (Vendas, Remessas, etc.)                   | Para lógicas que precisam interagir com o **barramento de regras** (`ContextoRegra`), como solicitar liberações de limite, ou para validações complexas na confirmação/faturamento.         |
| `@Callback`         | **Todos os Documentos Comerciais**, incluindo **Notas de Entrada** (Compras) | Para reagir a eventos de negócio de forma direta, especialmente em cenários onde a `@BusinessRule` não atua (como notas de compra) ou quando a interação com o barramento não é necessária. |

**Resumo:**

* Precisa solicitar **liberação de limites** em uma nota de venda? Use **`@BusinessRule`**.
* Precisa validar uma **nota de compra** na confirmação? Use **`@Callback`**.
* Precisa de uma lógica simples de auditoria na confirmação de qualquer nota? **`@Callback`** é mais direto.

***

### ⚙️ Como Funciona

Para criar uma regra de negócio, anote uma classe que implementa `br.com.sankhya.modelcore.comercial.Regra` com `@BusinessRule`.

#### A Interface `Regra`

A classe deve implementar os métodos que correspondem aos eventos do ciclo de vida do documento. Embora os métodos de CRUD (`beforeInsert`, `afterUpdate`, etc.) existam, o foco principal da `@BusinessRule` está nos eventos de **confirmação e faturamento**.

#### O `ContextoRegra`

O objeto `ctx` é seu ponto de acesso a todas as informações da execução e é o **principal diferencial** da `@BusinessRule`. Com ele, você pode:

* **Acessar a Nota**:
  * `ctx.getPrePersistEntityState().getNewVO()`: Obtém o `DynamicVO` da nota com as **modificações atuais**.
  * `ctx.getPrePersistEntityState().getOldVO()`: Obtém o `DynamicVO` da nota com os **dados originais** (disponível em `beforeUpdate` e `beforeDelete`).
* **Interagir com o Barramento de Regras**:
  * `ctx.getBarramentoRegra().addMensagem("Mensagem de aviso")`: Exibe um aviso não bloqueante para o usuário.
  * `ctx.getBarramentoRegra().addLiberacaoSolicitada(...)`: Inicia um evento de liberação de limites, a principal aplicação da `@BusinessRule`.

***

### 🧩 Exemplos Práticos

#### 1. Solicitando Liberação de Limite na Confirmação

Este é o caso de uso ideal para uma `@BusinessRule`, pois exige acesso ao barramento de regras. Para que funcione, um evento de liberação (ex: ID 2000) deve ser previamente cadastrado no sistema.

```java
@BusinessRule(description = "Solicita liberação para vendas com desconto alto")
public class LiberacaoDescontoRegra implements Regra {

    @Override
    public void beforeUpdate(ContextoRegra ctx) throws Exception {
        DynamicVO notaVO = (DynamicVO) ctx.getPrePersistEntityState().getNewVO();

        // A lógica de liberação é geralmente acionada durante a confirmação,
        // que internamente pode disparar um 'update' na nota.
        Boolean isConfirmando = (Boolean)JapeSession.getProperty("CabecalhoNota.confirmando.nota");
        if (!Boolean.TRUE.equals(isConfirmando)) return;

        BigDecimal percentualDesconto = notaVO.asBigDecimal("PERCDESC");

        if (percentualDesconto != null && percentualDesconto.compareTo(new BigDecimal("10")) > 0) {
            // ID do evento de liberação (deve ser cadastrado no sistema)
            int idEventoLiberacao = 2000;

            LiberacaoSolicitada liberacao = new LiberacaoSolicitada(
                    notaVO.asBigDecimal("NUNOTA"),
                    "TGFCAB", // Tabela da nota
                    idEventoLiberacao,
                    BigDecimal.ONE // ID do usuário que solicita (pode ser dinâmico)
            );
            liberacao.setPendente(true);

            ctx.getBarramentoRegra().addLiberacaoSolicitada(liberacao);
            ctx.getBarramentoRegra().addMensagem("Solicitação de liberação enviada para desconto acima de 10%.");
        }
    }

    // ... outros métodos da interface ...
}
```

#### 2. Modificando um Campo na Confirmação

Para modificações de dados durante o CRUD (salvar, excluir), a abordagem recomendada é usar um **`@Listener`**. No entanto, se a modificação precisa ocorrer **especificamente no momento da confirmação da nota**, a `@BusinessRule` é a ferramenta correta.

O exemplo abaixo adiciona uma observação no exato momento em que a nota é confirmada.

```java
@BusinessRule(description = "Adiciona observação de conferência na confirmação")
public class AdicionaObservacaoConfirmacaoRegra implements Regra {

    @Override
    public void beforeUpdate(ContextoRegra ctx) throws Exception {
        DynamicVO notaVO = (DynamicVO) ctx.getPrePersistEntityState().getNewVO();
        DynamicVO oldNotaVO = (DynamicVO) ctx.getPrePersistEntityState().getOldVO();

        // Verifica se a nota está sendo confirmada (o campo CONFIRMADA mudou de 'N' para 'S')
        boolean isConfirmando = "S".equals(notaVO.asString("CONFIRMADA"))
                && (oldNotaVO == null || !"S".equals(oldNotaVO.asString("CONFIRMADA")));

        if (isConfirmando) {
            String obsAtual = notaVO.asString("OBSERVACAO");
            String novaObs = "Nota conferida e confirmada pelo sistema.";

            notaVO.setProperty("OBSERVACAO", obsAtual == null ? novaObs : obsAtual + "\n" + novaObs);
        }
    }

    // ... outros métodos da interface ...
}
```

***

### ✨ Boas Práticas

* **Execução Rápida**: Uma regra de negócio deve ser extremamente rápida e executar em **milissegundos**. Ela roda dentro da mesma transação da confirmação da nota, e qualquer lentidão impactará diretamente a performance do sistema para o usuário.
* **Use Assincronismo para Integrações**: Para integrações com sistemas externos (APIs, etc.), **nunca** faça chamadas síncronas. Use mecanismos assíncronos (como `CompletableFuture`, `ExecutorService`, ou publicando um evento JMS) para isolar a integração da transação principal e não impactar o tempo de resposta do usuário.
* **Foco na Confirmação**: Use a `@BusinessRule` para o que ela faz de melhor: lidar com a lógica de negócio no momento da confirmação e faturamento.
* **Lógica em Services**: Mantenha a classe da `@BusinessRule` enxuta. Delegue a lógica de negócio complexa para classes de serviço (`@Service`).
* **Feedback ao Usuário**: Use `ctx.getBarramentoRegra().addMensagem()` para informar ao usuário sobre ações automáticas que a regra executou.
* **Validações Bloqueantes**: Para impedir uma operação, lance uma exceção. A mensagem da exceção será exibida ao usuário. Ex: `throw new Exception("Limite de crédito excedido.")`.

### 🚫 Anti-Patterns (O que evitar)

* **Usar para CRUD Simples**: Evite usar `@BusinessRule` para validações ou modificações de campo que podem ser feitas de forma mais eficiente com um `@Listener`. Isso acopla sua lógica desnecessariamente ao módulo comercial.
* **Chamadas Síncronas Externas**: Fazer chamadas de rede (API, Web Service) de forma síncrona dentro de uma regra de negócio. Isso degrada drasticamente a performance e pode causar timeouts.
* **Manipular a UI**: Regras de negócio são para lógica de back-end. Não tente manipular componentes de interface a partir delas.
* **Ignorar o Evento Correto**: Não use `afterInsert` para fazer uma validação que deveria ter sido feita em `beforeInsert`. Após o registro ser salvo, pode ser tarde demais.
