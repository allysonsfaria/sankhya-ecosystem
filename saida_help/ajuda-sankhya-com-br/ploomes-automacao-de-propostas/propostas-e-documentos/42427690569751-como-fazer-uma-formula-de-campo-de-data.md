---
id: "42427690569751"
titulo: "Como fazer uma fórmula de campo de data condicional"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427690569751-Como-fazer-uma-f%C3%B3rmula-de-campo-de-data-condicional"
trilha: "PLOOMES: Automação de propostas  > Propostas e documentos"
atualizado_em: "2026-08-10T18:08:10Z"
rotulos: ["sync_hc", "ploomes", "ploomes_7056837", "sync_hash_cd2366a42b29"]
---

# Como fazer uma fórmula de campo de data condicional

Para essa configuração, vou usar um modelo de **proposta**.

Para acessar os modelos, clique em:
Administração > Modelos de documento > Selecione o modelo desejado

Vou criar dois campos:

**Data de entrega**, que é um campo do tipo Data e vai receber a fórmula.

**Dias para entrega**, que é um campo de Opções pré-cadastradas e recebe as opções para entrega.

Para criar um campo, clique em:

Campos> Proposta > Criar campo

Preencha o **Tipo** (Opções pré-cadastradas), o **Título do campo**, e adicione as **Opções**:

![Imagem 1: Preencha o Tipo (Opções pré-cadastradas), o Título do campo , e adicione as Opções :](https://downloads.intercomcdn.com/i/o/685831723/addb2609319fc73d99aa41cd/image.png?expires=1786536000&signature=7532352e9f93023431a20a931c1314288b14a7dcdb3523c5bc56ac4f0438d211&req=cigiHsp%2FmoNcFb4V1XW4gZM1Ajwt%2FU46nHLv01yFJuK2LBz38xqDI4af3ACA%0AkqGHRuaBrVOiolQJ2sHLa8gVZg%3D%3D%0A)

Feito isso, seguimos para a criação do campo de data:

![Imagem 2: Feito isso, seguimos para a criação do campo de data:](https://downloads.intercomcdn.com/i/o/685832760/5f755562d690a0d0d61d732d/image.png?expires=1786536000&signature=3572906c851a6f5ecae81c8ca5214c852ab7d6677440fbcaf44b25dad87aefc6&req=cigiHsp8modfFb4V1XW4gW1WUFKtNg37NfQh8gBzEtyicUIDsP%2Fn9nQy6uAI%0AOQ9%2FHX%2Fuxss%2BKvrIOKb6valbmA%3D%3D%0A)

Aqui vamos configurar uma fórmula em "Configurações avançadas".

Selecione a fórmula padrão em "Códigos JS"

![Imagem 3: Selecione a fórmula padrão em "Códigos JS"](https://downloads.intercomcdn.com/i/o/685833198/0b2d1447be6ace0d8027772f/image.png?expires=1786536000&signature=7c739eef70d30c5e4ae6e40e5899ca87ff4a2e9a38037131d4177931e1712c33&req=cigiHsp9nIhXFb4V1XW4gVtpujoWFZp%2FwXGTVhRYXyo2hB2Xoq7mNf0WLre3%0AJt01jnEpZRYJ44AwDzMtNMUdDw%3D%3D%0A)

Substitua o gatilho pelo "Dias para entrega"

![Imagem 4: Substitua o gatilho pelo "Dias para entrega"](https://downloads.intercomcdn.com/i/o/685835259/90d39d28f3c5d8f686c85638/image.png?expires=1786536000&signature=047f89047ac9a3db66c7ed1462fc101e8e42fba220c299f375c9b33c7d9ae276&req=cigiHsp7n4RWFb4V1XW4gV%2BslDUNmxdnoJSiZys8p9vJnpDrleax2wrAQL2v%0AHUl67wtG5rkAto4NxlCSC%2BJT%2Bw%3D%3D%0A)

e o "3" por "0".

Agora, vamos configurar a condicional:

![Imagem 5: Agora, vamos configurar a condicional:](https://downloads.intercomcdn.com/i/o/685837559/7af07f8900b0792b96d67e6b/image.png?expires=1786536000&signature=4721563c9aca9badeb2eb4c5c72f42c81691ab9419cf03d87ab30f37980f947f&req=cigiHsp5mIRWFb4V1XW4gRrd%2Bz12pnlh2NLgLnM1MbWMC3oHK1GKHEPxRSrt%0AFBKdBYu2F64HDL7vmrILD1Jl3g%3D%3D%0A)

```
  if(gatilho==="Entrega no mesmo dia"){
    x=0
    }
    else if(gatilho==="Entrega no dia seginte"){
      x=1
    }else if(gatilho==="4 dias"){
      x=4
    }else if(gatilho==="7 dias"){
      x=7
    }else if(gatilho==="30 dias"){
      x=30
}
```

Na linha:

let date = new Date("[Proposta.Data]");

vamos remover o "[Proposta.Data]" caso queiramos que a data seja calculada a partir do dia de hoje.

Se precisar que seja calculado com base em outro campo de data ou caom a data da proposta, é necessário inserir o campo pelo modal "Campos":

![Imagem 6: Se precisar que seja calculado com base em outro campo de data ou caom a data da proposta, é necessário inserir o campo…](https://downloads.intercomcdn.com/i/o/685839393/3018d8bf39f0f16f079ccd93/image.png?expires=1786536000&signature=0ab620930a210e02ea665c3f9dcf97f7b3d0e0f8b8739b61efd417007683f58f&req=cigiHsp3nohcFb4V1XW4gdBKD%2F1Kloq6K3In6Su0TRBttoO%2FmvmjyJrGTyzD%0Ap8%2BNfGnEHnarVG%2Bbz3BhIhs8UA%3D%3D%0A)

Por fim, somamos 1 na variável x - isso se dá pois o Javascript começa a contar do 0.

![Imagem 7: Por fim, somamos 1 na variável x - isso se dá pois o Javascript começa a contar do 0.](https://downloads.intercomcdn.com/i/o/685840225/fec8fb36e9a3f3fde6b95e3e/image.png?expires=1786536000&signature=21819e13b7e28ede29a24f0e5ea6b88ad11cee79cc08f66a42e13d80d2b82877&req=cigiHs1%2Bn4NaFb4V1XW4gXYfqZE%2FbGiwbDm%2BVh2kCAcWIIT8EMszZ2lhv0E1%0AyJ6u3HzEXaE6%2BEdO0uOwY%2BybJw%3D%3D%0A)

Minha fórmula final ficou assim:

```
(function (gatilho, x) {
  if(gatilho==="Entrega no mesmo dia"){
    x=0
    }
    else if(gatilho==="Entrega no dia seginte"){
      x=1
    }else if(gatilho==="4 dias"){
      x=4
    }else if(gatilho==="7 dias"){
      x=7
    }else if(gatilho==="30 dias"){
      x=30
    }
  let date = new Date();
  date.setDate(date.getDate() + x+1);
  return date.toLocaleDateString("pt-Br");
})("[Proposta.Dias para entrega]", 0);
```

[Clique aqui](https://ploomesov2d9p.hippovideo.io/page/sales-page-template-zb461z-0j196p6r?custom_asset_token=qd0mlFMRON63IAEOwcWMuNyman4MbjXEAg1p2XrcYs0&org_tok=nDFUj6xX-hBXQ2yF3HglAg&utm_source=hv-campaigns&hreferer=private&_=1678195069) para ver o teste e um vídeo mostrando dicas extra
