# Receitas de Integração e Webhooks

Padrões arquiteturais para sincronização bidirecional entre o ERP Sankhya e sistemas terceiros (E-commerce, CRM, WMS, Bancos e PDVs).

---

## 1. Padrão Webhook Outbound (Sankhya → Sistema Externo)

Para enviar dados do Sankhya para um webhook externo em tempo real:
- Implemente um `@Listener` na entidade de interesse (ex: `CabecalhoNota`, `Parceiro`, `ItemNota`).
- Utilize o evento `afterInsert` ou `afterUpdate`.
- Dispare a requisição HTTP em thread assíncrona ou fila para não travar a transação do usuário caso o endpoint de destino esteja lento ou fora do ar.

```java
package br.com.empresa.modulo.listeners;

import br.com.sankhya.extensions.eventogeral.EventoGeral;
import br.com.sankhya.extensions.eventogeral.PersistenceEvent;
import br.com.sankhya.jape.vo.DynamicVO;
import java.util.concurrent.CompletableFuture;

public class PedidoVendaWebhookListener implements EventoGeral {

    @Override
    public void afterInsert(PersistenceEvent event) throws Exception {
        DynamicVO vo = (DynamicVO) event.getVo();
        String tipMov = vo.asString("TIPMOV"); // V = Venda, P = Pedido
        
        if ("P".equals(tipMov) || "V".equals(tipMov)) {
            final Object nuNota = vo.getProperty("NUNOTA");
            // Disparo assíncrono não bloqueante
            CompletableFuture.runAsync(() -> {
                notificarWebhook(nuNota);
            });
        }
    }

    private void notificarWebhook(Object nuNota) {
        // Envio HTTP POST com payload JSON para o endpoint de destino
    }

    @Override public void beforeInsert(PersistenceEvent e) {}
    @Override public void beforeUpdate(PersistenceEvent e) {}
    @Override public void beforeDelete(PersistenceEvent e) {}
    @Override public void afterUpdate(PersistenceEvent e) {}
    @Override public void afterDelete(PersistenceEvent e) {}
}
```

---

## 2. Ingestão de Dados Inbound (Sistema Externo → Sankhya)

Padrão de carga de dados com validações e retorno de chave primária gerada:
1. Autenticar via `/login` ou `MobileLoginSP.login`.
2. Verificar duplicidade de identificador externo (ex: campo `AD_IDEXTERNO` ou `NUMPEDIDO2`).
3. Chamar `CRUDServiceProvider.saveRecord` para criar a entidade mestre e obter o ID gerado (`CODPARC`, `NUNOTA`, `NUFIN`).
4. Gravar detalhes/itens relacionados.
