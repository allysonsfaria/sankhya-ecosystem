# Segurança, Logging e Boas Práticas

Padrões de segurança corporativa e rastreabilidade para extensões Sankhya OM.

---

## 1. Logging com SankhyaLogger

Nunca use `System.out.println`, `System.err` ou `e.printStackTrace()`. Utilize a classe oficial `SankhyaLogger`:

```java
package br.com.empresa.modulo.util;

import br.com.sankhya.util.log.SankhyaLogger;

public class IntegracaoService {
    private static final SankhyaLogger log = SankhyaLogger.getLogger(IntegracaoService.class);

    public void processar() {
        if (log.isDebugEnabled()) {
            log.debug("Iniciando processamento de integração...");
        }

        try {
            // Regra
        } catch (Exception e) {
            log.error("Falha ao integrar pedido: " + e.getMessage(), e);
        }
    }
}
```

### Níveis Recomendados:
- **ERROR**: Falhas críticas com interrupção de fluxo. Sempre repassar a exceção `(msg, e)`.
- **WARN**: Situações anômalas contornadas.
- **INFO**: Eventos macro de ciclo de vida (início/fim de processamento em lote).
- **DEBUG**: Detalhes técnicos e depuração (sempre envolver em `if (log.isDebugEnabled())`).

---

## 2. Prevenção Contra SQL Injection

Ao usar `NativeSql`, **NUNCA** concatene valores vindos de parâmetros ou variáveis:

```java
// ERRADO (VULNERÁVEL)
sql.appendSql("SELECT * FROM TGFPAR WHERE NOMEPARC = '" + nomeParc + "'");

// CORRETO (PREVENÇÃO DE INJECTION)
sql.appendSql("SELECT * FROM TGFPAR WHERE NOMEPARC = :NOME");
sql.setNamedParameter("NOME", nomeParc);
```

---

## 3. Isolamento de Tenant e Multi-Empresa

O Sankhya OM opera em ambiente multi-empresa e multi-tenant:
- Sempre filtrar por `CODEMP` ou respeitar os filtros de acesso do usuário logado.
- Obter informações da sessão corrente:
```java
AuthenticationInfo auth = AuthenticationInfo.getCurrent();
BigDecimal codUsu = auth.getUserID();
BigDecimal codEmp = auth.getEmpresaPadrao();
```

---

## 4. Auditoria e Operações Sensíveis
- Gravação de trilha de auditoria para exclusão ou alteração de registros financeiros e fiscais.
- Em integrações com PDV/TEF: nunca trafegar ou persistir dados de cartão em claro (PAN completo ou CVV) em tabelas ou logs.
