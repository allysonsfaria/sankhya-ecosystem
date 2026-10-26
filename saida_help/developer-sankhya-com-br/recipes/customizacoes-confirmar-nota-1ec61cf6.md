---
id: "https://developer.sankhya.com.br/recipes/customizações-confirmar-nota"
titulo: "Customizações - Confirmar Nota"
url: "https://developer.sankhya.com.br/recipes/customizações-confirmar-nota"
atualizado_em: "2025-11-10T23:38:47.000Z"
---

# Customizações - Confirmar Nota

```java Java
import br.com.sankhya.modelcore.PlatformService;
import br.com.sankhya.modelcore.PlatformServiceFactory;

PlatformService confirmaNotaService = PlatformServiceFactory.getInstance().lookupService("@core:confirmacao.nota.service");

confirmaNotaService.set("NUNOTA", BigDecimal.valueOf(383));
confirmaNotaService.set("CODUSUAUTHINFO", BigDecimal.ZERO);

confirmaNotaService.execute();
```

```json Response Example
{"success":true}
```

# Imports

<!-- java@1-2 -->

Importa as classes necessárias para realizar a operação

# Cria objeto

<!-- java@4 -->

Cria objeto do tipo PlatformService a ser utilizado no processo de confirmação de nota

# Indica atributos

<!-- java@6-7 -->

Indica o NUNOTA da nota a ser confirmada e o código do usuário da confirmação.

# Realiza a confirmação

<!-- java@9 -->

Executa a confirmação da nota
