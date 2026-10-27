---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/api-java/sankhya-bff/ICustomFilterBarResolver/"
titulo: "ICustomFilterBarResolver"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/api-java/sankhya-bff/ICustomFilterBarResolver/"
trilha: "Docs > Api Java > Sankhya Bff > Icustomfilterbarresolver"
---

# ICustomFilterBarResolver

Interface para resolver e manipular configurações da `FilterBar`.

## handle

Manipula a configuração da `FilterBar`, permitindo ajustes nos filtros ou demais parâmetros disponíveis.

```
@CustomFilterBarResolver(resourceId = "br.com.sankhya.fin.cad.movimentacaoBancaria")
public class CustomFilterBarResolver implements ICustomFilterBarResolver {

  @Override
  public void handle(FilterBarConfig filterBarConfig) throws Exception {

    if(!filterBarConfig){
      System.out.println("Nenhuma configuração informada");
      return;
    }

    System.out.println("Lidando com configurações: " + filterBarConfig);
  }
}
```
