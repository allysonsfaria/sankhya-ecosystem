---
id: "4402896909207"
titulo: "Integração contábil não respeita a opção selecionada no campo \"Contabilizado Por\", realizando a integração sempre pelo \"Centro de Resultado\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4402896909207-Integra%C3%A7%C3%A3o-cont%C3%A1bil-n%C3%A3o-respeita-a-op%C3%A7%C3%A3o-selecionada-no-campo-Contabilizado-Por-realizando-a-integra%C3%A7%C3%A3o-sempre-pelo-Centro-de-Resultado"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:35:48Z"
rotulos: ["Configuração", "Centro de Resultado", "Contabilização", "Financeiro", "#validadoRayssa", "Problema na Integração Contábil pelo Centro de Resultado", "Erro"]
---

# Integração contábil não respeita a opção selecionada no campo "Contabilizado Por", realizando a integração sempre pelo "Centro de Resultado"

| **Antes de realizar a alteração é necessário que os responsáveis pela contabilidade avaliem os impactos dessa marcação no módulo. Abaixo foi evidenciado somente os impactos no módulo de Folha.** |
| --- |

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16342762798487) MENSAGEM:**

Na Contabilização da Folha foi apresentada uma situação em que mesmo marcando a opção de **"Contabilizar por Empresa"** o sistema estava rateando por 'Centro de Resultado'. Ou seja, os valores estavam sendo enviados para a contabilidade de forma individual e não unificados, como deveria.

![Imagem 2: Na Contabilização da Folha foi apresentada uma situação em que mesmo marcando a opção de "Contabilizar por Empresa" o…](https://ajuda.sankhya.com.br/hc/user_images/6JfgDfIEBUwF_ItD0hz03g.png)

![Imagem 3: Na Contabilização da Folha foi apresentada uma situação em que mesmo marcando a opção de "Contabilizar por Empresa" o…](https://ajuda.sankhya.com.br/hc/user_images/XxqWCaXW1vfvhB5WQOWiNw.png)

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16342759675927) SOLUÇÃO:**

Segue demonstração de exemplo da localização da marcação e no banco de dados:

![Imagem 5: Segue demonstração de exemplo da localização da marcação e no banco de dados:](https://ajuda.sankhya.com.br/hc/article_attachments/15081085909783)

Após realizar um teste colocando o campo igual a 'N', a Contabilização da Folha retornou com o resultado esperado:

![Imagem 6: Após realizar um teste colocando o campo igual a 'N', a Contabilização da Folha retornou com o resultado esperado:](https://ajuda.sankhya.com.br/hc/article_attachments/15081083223063)

**![Imagem 7: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16342762808727) OBSERVAÇÃO:**

Em alguns casos será necessário realizar a desmarcação da flag via banco: UPDATE TCBEMP SET UTILCENCUS = 'N'

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16342762816279) CAUSA:**

Isso acontece pois o sistema olha a marcação **"Utiliza Centro de resultado"** (da Contabilidade), na tela **"Empresa"** do módulo. Se essa opção estiver marcada, o sistema terá esse comportamento e sempre vai adotar o critério de rateio cadastrado para contabilizar, independente da marcação do tipo da contabilização.
