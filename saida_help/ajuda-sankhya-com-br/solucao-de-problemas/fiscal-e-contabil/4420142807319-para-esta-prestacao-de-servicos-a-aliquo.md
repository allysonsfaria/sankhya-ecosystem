---
id: "4420142807319"
titulo: "Para esta prestação de serviços a alíquota do ISSQN é obrigatória"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4420142807319-Para-esta-presta%C3%A7%C3%A3o-de-servi%C3%A7os-a-al%C3%ADquota-do-ISSQN-%C3%A9-obrigat%C3%B3ria"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:19:47Z"
rotulos: ["Configuração", "Cidades", "Impostos", "NFS-e", "MUNALIQPERCNFSE", "ISSQN", "Alíquota do ISSQN é obrigatória para prestação de serviços", "Corrija com código IBGE no parâmetro \"MUNALIQPERCNFSE\".", "Verifique configurações na aba \"Alíquotas de ISS\""]
---

# Para esta prestação de serviços a alíquota do ISSQN é obrigatória

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16273903082903) MENSAGEM**:

[E228] Para esta prestação de serviços a alíquota do ISSQN é obrigatória.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16273903089175) SOLUÇÃO:**

Para corrigir o incidente, siga os passos abaixo: 

![Imagem 3: Verifique as configurações na tela, alíquota de ISS >> cadastro do serviço >> aba "Alíquotas de ISS” .](https://ajuda.sankhya.com.br/hc/article_attachments/16273887080471) Verifique as configurações na tela, alíquota de ISS >> cadastro do serviço >> aba **"Alíquotas de ISS”**.

![Imagem 4: O valor sendo levado para DIN e se todos estiverem certos, mesmo assim a tag permanecer levando o valor incorretamente,…](https://ajuda.sankhya.com.br/hc/article_attachments/16273903094679) O valor sendo levado para DIN e se todos estiverem certos, mesmo assim a tag permanecer levando o valor incorretamente, insira o **cód de IBGE** da cidade emitente no parâmetro: **"MUNALIQPERCNFSE"** e gere o lote da nota novamente.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16273903096599) CAUSA:**

Esta mensagem ocorre quando se tenta gerar uma nota de serviço: A informação que está sendo levada para TAG "Alíquota" no xml.Exemplo : na TGFDIN está a alíquota 2,16 e no xml está levando o valor de 0,02.
