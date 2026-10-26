# Comunicação Inter-Módulos: Module-Connect e Proxy-Connect

No ecossistema corporativo do Sankhya OM, módulos desacoplados não devem importar classes concretas uns dos outros diretamente para evitar acoplamento rígido de compilação e dependências circulares.

---

## 1. Module-Connect (Chamadas de Serviços Remotos/Locais)

Framework baseado em anotações para expor e consumir serviços entre módulos:

### Expor Serviço (@ServiceApplication e @ServiceUnit)
```java
package br.com.sankhya.comercial.services;

import br.com.sankhya.moduleconnect.annotations.*;

@ServiceApplication("comercial")
public class FaturamentoServiceApp {

    @ServiceUnit("faturamento")
    public static class FaturamentoUnit {

        @ServiceAction("cancelarNota")
        public JsonObject cancelarNota(JsonPayload payload) throws Exception {
            BigDecimal nuNota = payload.getAsBigDecimal("nuNota");
            String motivo = payload.getAsString("motivo");
            
            // Regra de cancelamento
            JsonObject response = new JsonObject();
            response.addProperty("status", "OK");
            return response;
        }
    }
}
```

### Consumir Serviço (ModuleConnect.call ou @ServiceClient)
```java
import br.com.sankhya.moduleconnect.ModuleConnect;
import com.google.gson.JsonObject;

JsonObject params = new JsonObject();
params.addProperty("nuNota", nuNota);
params.addProperty("motivo", "Cancelamento via integração");

JsonObject resposta = ModuleConnect.call("comercial.faturamento.cancelarNota", params);
```

---

## 2. Proxy-Connect (Comunicação Tipada via Interfaces)

Permite instanciar interfaces em módulos consumidores enquanto a implementação reside em outro módulo:

```java
import br.com.sankhya.proxyconnect.ProxyConnect;

// Interface compartilhada (módulo contrato/API)
public interface EstoqueService {
    BigDecimal getSaldoDisponivel(BigDecimal codProd, BigDecimal codEmp);
}

// Consumo dinâmico sem dependência do JAR de implementação:
EstoqueService estoqueService = ProxyConnect.newProxy(EstoqueService.class);
BigDecimal saldo = estoqueService.getSaldoDisponivel(codProd, codEmp);
```

### Recomendações:
- Use `newStaticCachedProxy` para serviços invocados em alta frequência.
- Trate sempre `ServiceNotFoundException` e `ServiceTemporarilyUnavailableException`.
