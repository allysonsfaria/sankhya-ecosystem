---
id: "44012755236759"
titulo: "[TMS] - Correção no Cálculo do Frete no CTE: Consideração do Valor Total da NF"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012755236759--TMS-Corre%C3%A7%C3%A3o-no-C%C3%A1lculo-do-Frete-no-CTE-Considera%C3%A7%C3%A3o-do-Valor-Total-da-NF"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T19:38:05Z"
rotulos: ["sync_hc", "lincros", "lincros_13433267", "sync_hash_5465a14d1694"]
---

# [TMS] - Correção no Cálculo do Frete no CTE: Consideração do Valor Total da NF

## Divergência de Frete

**1 - Problema Relatado pelo Cliente:**
O cliente percebeu uma inconsistência no cálculo do frete no CTE 148616, vinculado à fatura 2337708. O sistema estava calculando o valor do frete com base no valor dos produtos, em vez de considerar o valor total da nota fiscal, o que gerou uma divergência nos valores apresentados. Essa discrepância estava impactando o cálculo correto do frete, levando o cliente a questionar a precisão do processo.

---

**2 - Passo a Passo para Resolver o Problema:**

Acessar **Operacional**> **Cargas**> **Pré-conhecimentos**e pesquisar o pré-conhecimento com divergências pelo número:

![Imagem 1: Acessar Operacional > Cargas > Pré-conhecimentos e pesquisar o pré-conhecimento com divergências pelo número:](https://ajuda.sankhya.com.br/hc/article_attachments/44012755439767)

**Localize a NF-e**: Acesse a NF-e associada ao CTE que está apresentando a discrepância no cálculo do frete, para verificar se a substituição tributária está marcada como sim.

Para acessar a nota, vá até a aba **Notas Fiscais** dentro do **pré-conhecimento** e clique no código na nota que está associada:

![Imagem 2: Para acessar a nota, vá até a aba Notas Fiscais dentro do pré-conhecimento e clique no código na nota que está…](https://ajuda.sankhya.com.br/hc/article_attachments/44012779682839)

Na NF-e, acesse a aba **Cadastro** e verifique a configuração **Fiscal/Contábil**, onde são definidas as configurações fiscais e tributárias.

![Imagem 3: Na NF-e, acesse a aba Cadastro e verifique a configuração Fiscal/Contábil , onde são definidas as configurações fiscais…](https://ajuda.sankhya.com.br/hc/article_attachments/44012751372439)

**Identifique a Tag <vST> no XML**: Para verificar essa tag no XML, é necessário realizar o download do arquivo XML na tela da nota. Para isso, acesse a nota conforme o caminho indicado acima e clique em **Download XML**.

![Imagem 4: Identifique a Tag <vST> no XML : Para verificar essa tag no XML, é necessário realizar o download do arquivo XML na…](https://ajuda.sankhya.com.br/hc/article_attachments/44012771721111)

 No XML da NF-e, localize a tag `<vST>`. Se o valor dessa tag for maior que zero, isso indica que a substituição tributária está ativa. Quando configurada dessa maneira, o cálculo do frete é realizado com base no valor dos produtos, em vez de usar o valor total da nota fiscal.

**Altere a Configuração de Substituição Tributária**: Caso a tag `<vST>` contenha um valor superior a zero, altere a configuração de **"Sim"** para **"Não"**. Isso desativará a substituição tributária, permitindo que o frete seja calculado com base no valor total da nota fiscal, corrigindo a divergência.

![Imagem 5: Altere a Configuração de Substituição Tributária : Caso a tag <vST> contenha um valor superior a zero, altere a…](https://ajuda.sankhya.com.br/hc/article_attachments/44012734286103)

**Recalcule o Pré-Conhecimento do CTE**: Após realizar a alteração, recalcule o pré-conhecimento do CTE. O componente **Ad Valorem**, responsável pelo cálculo do frete, agora passará a considerar o valor total da NF-e, ajustando corretamente o valor do frete.
