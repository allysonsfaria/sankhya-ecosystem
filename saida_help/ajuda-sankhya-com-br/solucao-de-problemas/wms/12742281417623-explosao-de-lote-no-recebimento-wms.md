---
id: "12742281417623"
titulo: "Explosão de lote no recebimento WMS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/12742281417623-Explos%C3%A3o-de-lote-no-recebimento-WMS"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T15:00:43Z"
rotulos: ["Produtos", "Configuração", "WMS", "Estoque", "Preferências", "Conferência: Atualização controle lote", "Explosão de lote: Recebimento produto", "Configuração: Aba \"WMS\" habilitada"]
---

# Explosão de lote no recebimento WMS

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17120812969495) SITUAÇÃO:**

Algumas empresas durante o processo de entrada do sistema, através de notas, não alimentam o campo controle diretamente no item, sendo utilizado nesses caso a explosão de lote durante o recebimento do produto.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17120812981527) SOLUÇÃO:**

![Imagem 3: Para tal processo, a empresa deverá ter habilitada a marcação "Utiliza explosão de lote no recebimento", na aba "WMS" ,…](https://ajuda.sankhya.com.br/hc/article_attachments/17120785070487) Para tal processo, a empresa deverá ter habilitada a marcação **"Utiliza explosão de lote no recebimento",** na aba ["WMS"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abawms), das ["Preferências da Empresa"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), para que assim o sistema realize a explosão de lote durante o recebimento da nota.

![Imagem 4: Para tal processo, a empresa deverá ter habilitada a marcação "Utiliza explosão de lote no recebimento", na aba "WMS" ,…](https://ajuda.sankhya.com.br/hc/article_attachments/13424314348183)

![Imagem 5: Após a confirmação da nota na conferência de entrada, o sistema realizará a inserção ou atualização no controle de lote…](https://ajuda.sankhya.com.br/hc/article_attachments/17120785077911) Após a confirmação da nota na conferência de entrada, o sistema realizará a inserção ou atualização no controle de lote dos itens da nota do recebimento de acordo com o lote informado no coletor de dados. Caso o produto possua controles de lotes diferentes, estes serão inseridos na grade de itens com uma sequência para cada controle cadastrado ou quantidade menor que a inicial, de forma que, o sistema irá realizar o recálculo dos valores da grade e de seus impostos.
