---
id: "https://developer.sankhya.com.br/docs/08_callback"
titulo: "📞 Callbacks: Reagindo a Eventos de Documentos"
url: "https://developer.sankhya.com.br/docs/08_callback"
atualizado_em: "2025-11-17T19:28:15.000Z"
---

# 📞 Callbacks: Reagindo a Eventos de Documentos

Como usar callbacks para executar lógica customizada em resposta a eventos (ex: antes de salvar um pedido).

> 📘 **Disponibilidade**: Funcionalidade disponível a partir da versão 2.0 do Add-on Studio.

A anotação `@Callback` é um hook poderoso para interceptar eventos de alto nível no ciclo de vida de **documentos comerciais**, como a confirmação de uma nota ou o processamento de um faturamento.

Diferente de um `@Listener`, que opera em nível de persistência (CRUD de qualquer entidade), ou de uma `@BusinessRule`, que é focada no ciclo de vida comercial, o `@Callback` reage a ações de negócio específicas, sendo uma forma direta de executar lógicas customizadas nesses momentos.

***

### 🤔 Para que serve?

Use um `@Callback` para "escutar" e reagir a eventos de negócio específicos do módulo comercial, sem a complexidade de uma `@BusinessRule`.

**Casos de uso comuns:**

* **Validações Pré-Confirmação**: Executar uma última verificação antes de uma nota ser confirmada.
* **Log de Auditoria**: Registrar informações detalhadas quando uma nota é inserida ou faturada.
* **Integrações Assíncronas**: Disparar uma integração com um sistema externo após a confirmação bem-sucedida de uma nota.
* **Manipulação de Dados em Lote**: Obter a lista de notas que estão prestes a ser faturadas para alguma preparação.

***

### ⚠️ Callback vs. BusinessRule: Qual Usar?

Ambos os hooks reagem a eventos do ciclo de vida comercial, mas possuem escopos e propósitos diferentes. A escolha não se baseia em complexidade, mas sim em **aplicabilidade**.

| Hook            | Escopo de Atuação                                                            | Quando Usar                                                                                                                                                                                           |
| :-------------- | :--------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`@Callback`** | **Todos os Documentos Comerciais**, incluindo **Notas de Entrada** (Compras) | Para reagir a eventos de negócio de forma direta, especialmente em cenários onde a `@BusinessRule` não atua (como notas de compra) ou quando a interação com o barramento de regras não é necessária. |
| `@BusinessRule` | **Notas de Saída e Mov. Interna** (Vendas, Remessas, etc.)                   | Para lógicas que precisam interagir com o **barramento de regras** (`ContextoRegra`), como solicitar liberações de limite, ou para validações complexas na confirmação/faturamento.                   |

**Resumo:**

* Precisa validar uma **nota de compra** na confirmação? Use **`@Callback`**.
* Precisa solicitar **liberação de limites** em uma nota de venda? Use **`@BusinessRule`**.
* Precisa de uma lógica simples de auditoria na confirmação de qualquer nota? **`@Callback`** é mais direto.

***

### ⚙️ Como Funciona

Para criar um callback, anote uma classe que implementa `br.com.sankhya.modelcore.custommodule.ICustomCallBack` com `@Callback`.

#### A Interface `ICustomCallBack`

A classe deve implementar o método `call(String id, Map<String, Object> data)`.

* `id`: O ID do evento que disparou o callback (ex: `central.cabecalho.before`).
* `data`: Um mapa contendo dados contextuais sobre o evento. **O conteúdo deste mapa varia para cada`CallbackEvent`** . O `@Callback` se diferencia por fornecer um mapa de dados (`data`) mais rico e específico para cada evento.

#### Atributos da Anotação `@Callback`

| Atributo      | Descrição                                                                  | Exemplo                         |
| :------------ | :------------------------------------------------------------------------- | :------------------------------ |
| `when`        | Define se o callback executa **antes** (`BEFORE`) ou **depois** (`AFTER`). | `CallbackWhen.BEFORE`           |
| `event`       | O evento de negócio a ser interceptado.                                    | `CallbackEvent.CONFIRMATION`    |
| `description` | Uma descrição clara do que o callback faz.                                 | `"Valida dados na confirmação"` |

***

### 📋 Eventos Disponíveis (`CallbackEvent`)

#### `INSERTION`

Disparado na inserção ou alteração de um documento. **Não é acionado por eventos de CRUD do JAPE**, mas sim pela lógica de negócio dos portais.

* **Parâmetros em`data` (`when = BEFORE`):**
  * `cabState` (`PrePersistEntityState`): Estado da entidade antes de ser persistida. Permite acessar o `newVO`.
* **Parâmetros em`data` (`when = AFTER`):**
  * `cabState` (`PrePersistEntityState`): Estado da entidade antes de ser persistida.
  * `oldCabVO` (`DynamicVO`): VO do cabeçalho antes da alteração.
  * `bRegras` (`BarramentoRegra`): Barramento de regras do documento.

#### `CONFIRMATION` / `PROCESS_CONFIRMATION`

Disparado no início e no fim da confirmação de um documento. Sendo que `CONFIRMATION` é invocado ao confirmar notas pelos Portais e `PROCESS_CONFIRMATION` é invocado ao confirmar notas pelas telas Centrais.

* **Parâmetros em`data` (`when = BEFORE`):**
  * `nunota` (`BigDecimal`): Número Único do documento sendo confirmado.
  * `bRegras` (`BarramentoRegra`): Barramento de regras do processo.
* **Parâmetros em`data` (`when = AFTER`):**
  * `nunota` (`BigDecimal`): Número Único do documento confirmado.
  * `bRegras` (`BarramentoRegra`): Barramento de regras do processo.
  * `error` (`Exception`): Contém a exceção, caso tenha ocorrido um erro durante a confirmação.

#### `PROCESS_BILLING`

Disparado no início do processo de faturamento. **Não possui evento`AFTER`** .

* **Parâmetros em`data` (`when = BEFORE`):**
  * `notasSelecao` (`Collection<BigDecimal>`): Coleção dos Números Únicos dos documentos sendo faturados.
  * `itensEditados` (`Map<String,BigDecimal>`): Mapa com os itens editados (chave: `nunota-sequencia`, valor: `quantidade a faturar`).

***

### 🧩 Exemplo Prático: Validando Antes da Confirmação

```java
package br.com.fabricante.addon.exemplos.callback;

import br.com.sankhya.modelcore.custommodule.ICustomCallBack;
import br.com.sankhya.studio.annotations.hooks.Callback;
import br.com.sankhya.studio.annotations.hooks.CallbackEvent;
import br.com.sankhya.studio.annotations.hooks.CallbackWhen;
import java.math.BigDecimal;
import java.util.Map;

/**
 * Callback que valida se o NUNOTA existe antes de tentar confirmar a nota.
 */
@Callback(
    when = CallbackWhen.BEFORE,
    event = CallbackEvent.CONFIRMATION,
    description = "Valida dados antes da confirmação da nota"
)
public class ValidaConfirmacaoCallback implements ICustomCallBack {

    @Override
    public Object call(String id, Map<String, Object> data) throws Exception {
        System.out.println("CALLBACK ACIONADO: Antes de Confirmar Nota");
        
        BigDecimal nunota = (BigDecimal) data.get("nunota");
        
        if (nunota == null) {
            throw new Exception("Erro crítico: NUNOTA não encontrado no contexto da confirmação.");
        }
        
        System.out.println("Validando confirmação para a nota: " + nunota);
        
        // Lógica de validação adicional aqui...
        
        return null;
    }
}
```

***

### ✨ Boas Práticas

* **Verifique o Conteúdo do Mapa`data`** : Sempre verifique se as chaves que você espera existem no mapa `data` antes de usá-las para evitar `NullPointerException`.
* **Mantenha a Lógica Simples**: Callbacks devem ser rápidos. Para lógicas complexas, delegue a execução para um `@Service`, preferencialmente de forma assíncrona se envolver I/O.
* **Use para Notas de Entrada**: `@Callback` é a ferramenta correta para interceptar eventos em notas de compra, onde `@BusinessRule` não atua.

### 🚫 Anti-Patterns (O que evitar)

* **Lógica de Liberação de Limites**: Não tente implementar solicitações de liberação de limites em um `@Callback`. Essa lógica pertence exclusivamente à `@BusinessRule` devido à sua interação com o `BarramentoRegra`.
* **Lógica de CRUD Genérica**: Se a sua lógica precisa ser aplicada a várias entidades diferentes (não apenas documentos comerciais), um `@Listener` é a ferramenta mais adequada e reutilizável.
* **Bloquear a Thread Principal**: Evite executar operações lentas (chamadas de API síncronas, I/O de disco) diretamente no método `call`. Isso impacta a performance do sistema.
