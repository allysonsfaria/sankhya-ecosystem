---
id: "https://developer.sankhya.com.br/docs/boas-práticas-de-logging"
titulo: "Boas Práticas de Logging"
url: "https://developer.sankhya.com.br/docs/boas-práticas-de-logging"
atualizado_em: "2026-04-04T00:01:39.000Z"
---

# Boas Práticas de Logging

# Boas Práticas de Logging

Logging é um mecanismo essencial para observabilidade, diagnóstico e auditoria. Uma estratégia consistente de logs reduz custos de manutenção e diminui o tempo médio para resolução de incidentes (MTTR). Pesquisas de mercado indicam que times com observabilidade madura reduzem cerca de **45%** o tempo na identificação da causa raiz de falhas.

A seguir, são apresentadas práticas recomendadas para padronizar e qualificar o uso de logs.

***

## 1. Bibliotecas Suportadas

Atualmente, as bibliotecas oficialmente suportadas são:

* **Log4J1**
  * **JUL (Java Util Logging)**

    > Observação: Antes de adicionar bibliotecas de terceiros, verifique compatibilidade, política corporativa e impacto em runtime.

    ***

## 2. Níveis de Log

Utilize níveis de log de forma intencional. O nível escolhido impacta diretamente no volume de logs, custos de armazenamento e esforço de análise.

| Nível          | Significado                                       | Uso recomendado                                                   |
| -------------- | ------------------------------------------------- | ----------------------------------------------------------------- |
| TRACE          | Detalhamento extremo da execução                  | Apenas para depuração profunda, geralmente desativado em produção |
| DEBUG          | Informações internas úteis para dev               | Fluxos específicos durante análise de desenvolvimento             |
| INFO           | Eventos esperados do sistema                      | Confirma ações concluídas, inicializações, checkpoints            |
| WARN           | Situação anômala, mas que não impede continuidade | Dados incompletos, entradas suspeitas, timeouts recuperáveis      |
| ERROR          | Falha que impacta funcionalidade                  | Exceções, falhas em integrações, perda parcial de operação        |
| FATAL / SEVERE | Falha crítica                                     | Interrupção completa da aplicação ou perigo de corrupção de dados |

**Consequência do mau uso:** excesso de logs em `ERROR` aumenta ruído e dificulta detecção de falhas reais.

***

## 3. Mensagens Claras e Contextualizadas

Mensagens devem explicar o que aconteceu, onde aconteceu e (quando possível) por que aconteceu.

**Inclua contexto (IDs, usuário, entidade, origem).**

Exemplo incorreto:

```
"Erro ao processar pedido"
```

Exemplo adequado:

```
"Erro ao processar pedido ID=12345, cliente='joao.silva': falha na conexão com o banco"
```

Ao registrar exceções, inclua o Throwable para garantir o stack trace:

```java
Logger logger = Logger.getLogger(MeuServico.class.getName());

try {
    executar();
} catch (Exception e) {
    logger.log(Level.ERROR, "Erro na rotina de faturamento", e);
}
```

***

## 4. Volumes e Impactos

Logging excessivo aumenta:

* Custo de armazenamento
  * Latência devido a I/O
    * Dificuldade de análise

      > **Dica:** Logue somente o necessário. Dados sensíveis devem ser anonimizados.

      ***

## 5. Consistência e Padronização

* Padronize prefixos, mensagens e formato.
  * Evite concatenar strings manualmente — prefira placeholders.
    * Utilize MDC (Log4j) (Mapped Diagnostic Context) para anexar informações automaticamente (ex: requestId).

      Exemplo:

      ```java
      MDC.put("requestId", req.getId());
      logger.info("Iniciando processamento do pagamento");
      ```

      ***

## 6. Boas Práticas Resumidas

✅ Use nível adequado
✅ Forneça contexto
✅ Registre exceções com stack trace
✅ Evite informações sensíveis
✅ Otimize o volume de logs

***

Seguir essas práticas resulta em diagnóstico mais rápido, menor custo operacional e maior confiabilidade no ciclo de desenvolvimento e manutenção.
