---
id: "https://developer.sankhya.com.br/recipes/customizações-faturar-nota"
titulo: "Customizações - Faturar Nota"
url: "https://developer.sankhya.com.br/recipes/customizações-faturar-nota"
atualizado_em: "2025-11-10T23:38:48.000Z"
---

# Customizações - Faturar Nota

```java Java
import br.com.sankhya.modelcore.PlatformService;
import br.com.sankhya.modelcore.PlatformServiceFactory;

PlatformService faturaNotaService = PlatformServiceFactory.getInstance().lookupService("@core:faturamento.service");

Collection<BigDecimal> notasParaFaturamento = new ArrayList<>(Arrays.asList(
            new BigDecimal("20012"),
            new BigDecimal("20013"),
            new BigDecimal("20015")
        ));

faturaNotaService.set("NUNOTA"          , BigDecimal.valueOf(20016));
faturaNotaService.set("NUNOTACOLLECTION", notasParaFaturamento);
faturaNotaService.set("CODTIPOPER"      , BigDecimal.valueOf(100));
faturaNotaService.set("DTENTRADASAIDA"  , new Timestamp(System.currentTimeMillis()));
faturaNotaService.set("HRENTRADASAIDA"  , new Timestamp(System.currentTimeMillis()));
faturaNotaService.set("DTFATURAMENTO"   , new Timestamp(System.currentTimeMillis()));
faturaNotaService.set("SERIE"           , "1");
faturaNotaService.set("CODUSUAUTHINFO"  , BigDecimal.ZERO);

faturaNotaService.execute();
```

```json Response Example
{"success":true}
```

# Imports

<!-- java@1-2 -->

Realiza a importação das classes necessárias para realizar a operação

# Cria objeto

<!-- java@4 -->

Cria objeto do tipo PlatformService a ser utilizado no processo de faturamento de notas

# Seleção dos registros de origem

<!-- java@6-10 -->

Seleciona os registro de origem do faturamento. Pode conter 1 ou mais registros.

# Indica atributos

<!-- java@12-19 -->

Indica o NUNOTA da nota a ser gerada no faturamento, a relação dos registros de origem, código da TOP, data de entrada e saída, hora de entrada e saída, data do faturamento, a série da nota e o código do usuário da confirmação.

# Realiza o faturamento

<!-- java@21 -->

Executa o faturamento da nota
