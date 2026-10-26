---
id: "https://developer.sankhya.com.br/docs/jobs-agendados-com-job"
titulo: "🕒 Jobs Agendados com `@Job`"
url: "https://developer.sankhya.com.br/docs/jobs-agendados-com-job"
atualizado_em: "2026-02-24T20:34:37.000Z"
---

# 🕒 Jobs Agendados com `@Job`

# 🕒 Jobs Agendados com `@Job`

A anotação `@Job` simplifica drasticamente a criação de tarefas agendadas (Jobs) na plataforma Sankhya, substituindo a necessidade de configuração via XML (`mgeschedule.xml`) por uma abordagem moderna e declarativa, diretamente no código Java.

## 🤔 Por que usar `@Job`?

* ✅ **Simplicidade:** Configure tudo em um único lugar (a classe do Job).
* ✅ **Legibilidade:** O código se torna a fonte da verdade sobre quando e como o Job é executado.
* ✅ **Menos Erros:** Elimina a desconexão entre o código Java e a configuração em XML.

***

## 📊 Abordagem Antiga vs. Nova

### ❌ Abordagem Tradicional (`mgeschedule.xml`)

No modelo antigo, era preciso criar a classe Java e depois configurá-la em um arquivo XML separado, tornando a manutenção complexa e propensa a erros.

**`MeuJob.java`**

```java
/**
 *
 * @ejb.bean name="MeuJob" jndi-name="ejb/MeuJob"
 *           type="Stateless" transaction-type="Container" view-type="local"
 * @ejb.transaction type="Supports"
 * @ejb.util generate="false"
 */
public class MeuJobBean extends SessionBean {

    /**
     * @ejb.interface-method view-type = "local"
     */
    public String getScheduleConfig() throws java.lang.Exception {
        //return "* * * * *";
        return "&" + ONE_DAY;
    }

    /**
     * @ejb.interface-method
     */
    public void onSchedule() throws Exception {
        // Lógica do job...
    }
}
```

**`mgeschedule.xml`**

```xml
<?xml version="1.0" encoding="ISO-8859-1" standalone="yes"?>
<jobs>
    <ejb-job name="MeuJob"/>
</jobs>
```

### ✅ Nova Abordagem com `@Job`

Com o SDK, toda a configuração é feita na própria classe Java, de forma limpa e intuitiva.

```java
// Toda a configuração em um único lugar!
@Job(name = "ProcessadorDeFilaSP", frequency = "&0 0/5 * * * ?")
public class ProcessadorDeFilaJob implements IJob {

    @Override
    public void onSchedule() {
        // Lógica do job delegada para um serviço
        FilaService filaService = new FilaService();
        filaService.processarItens();
    }
}
```

***

## 📝 Como Criar um Job

Para criar um Job, basta seguir dois passos:

1. Anotar uma classe com `@Job`.
2. Implementar a interface `IJob`.

### A Interface `IJob`

A interface `IJob` define o contrato que sua classe deve seguir.

* **`onSchedule()`**: Este é o método principal, onde a lógica do seu Job será executada cada vez que o agendador for disparado.
* **`getScheduleConfigHook()`**: (Opcional) Este método é executado **apenas uma vez**, durante a inicialização do sistema. É ideal para configurações dinâmicas, como ler um parâmetro do sistema para definir a frequência do Job.

### Atributos da Anotação `@Job`

| Atributo          | Obrigatório | Descrição                                                                                                                               | Exemplo                                          |
| :---------------- | :---------- | :-------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------- |
| `name`            | Sim         | Nome do serviço (Bean) que será gerado. **Deve sempre terminar com "SP"**.                                                              | `name = "MeuJobSP"`                              |
| `frequency`       | Sim         | Define a frequência de execução. Pode ser uma **expressão CRON** ou um **intervalo em milissegundos**. **Deve sempre começar com `&`**. | `&0 0/15 * * * ?` (CRON) ou `&120000` (ms)       |
| `transactionType` | Não         | Define o comportamento transacional padrão. O valor padrão é `Supports` (exige controle manual da transação).                           | `transactionType = TransactionType.NotSupported` |

**Exemplo Completo:**

```java
import br.com.sankhya.studio.stereotypes.IJob;
import br.com.sankhya.studio.annotations.Job;
import br.com.sankhya.studio.persistence.Transactional;

@Job(
    name = "SincronizadorDeEstoqueSP",
    frequency = "0 0 2 * * ?" // Executa todo dia às 02:00
)
public class SincronizadorDeEstoqueJob implements IJob {

    @Override
    @Transactional // Garante que toda a sincronização seja atômica
    public void onSchedule() {
        System.out.println("Iniciando sincronização de estoque...");
        EstoqueService estoqueService = new EstoqueService();
        estoqueService.sincronizar();
        System.out.println("Sincronização de estoque finalizada.");
    }
}
```

> ❗️ **Importante: Migração Obrigatória**
>
> Ao usar a anotação `@Job`, os arquivos `mgeschedule.xml` e `mgechedule-cfg.xml` **não são permitidos** no projeto. Se existirem, a compilação falhará. Todos os jobs antigos devem ser migrados para o novo formato de anotação.

## ✨ Boas Práticas

* **Delegue a Lógica:** Mantenha o método `onSchedule()` enxuto. A lógica de negócio complexa deve ser delegada para outras classes, que são mais fáceis de testar e reutilizar.
* **Use Transações:** Para jobs que modificam dados, use `@Transactional` no método `onSchedule()` para garantir a consistência. Para jobs de apenas leitura, considere usar `transactionType = TransactionType.NotSupported` para melhor desempenho.
* **Tratamento de Erros:** Sempre inclua um tratamento de erros robusto dentro da sua lógica para evitar que uma falha inesperada impeça futuras execuções do job.
* **Frequência Configurável:** Em vez de "hardcodar" a frequência, use o método `getScheduleConfigHook()` para ler de um parâmetro do sistema (ex: `SystemParam`).
