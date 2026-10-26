---
id: "14714728084375"
titulo: "NFS-e com retenção de impostos gerando titulo financeiro com valor liquido diferente do valor de desdobramento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/14714728084375-NFS-e-com-reten%C3%A7%C3%A3o-de-impostos-gerando-titulo-financeiro-com-valor-liquido-diferente-do-valor-de-desdobramento"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T14:58:13Z"
rotulos: ["Configuração", "Movimentação Financeira", "Impostos", "Financeiro", "NFS-e", "Mantenha parâmetros e refaça financeiro", "NFS-e com retenção valor não ajustado", "Exclua impostos e refaça cálculo financeiro"]
---

# NFS-e com retenção de impostos gerando titulo financeiro com valor liquido diferente do valor de desdobramento

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16779928774295) SITUAÇÃO:**

Quando é gerada uma NFS-e de compra, onde o serviço sofre retenção de impostos, mas o valor do financeiro não poderá ser subtraído como desconto.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16779928780183) SOLUÇÃO:**

![Imagem 3: Mantenha os parâmetros "GERIMPOSTO": ligado e "CONSIMPRETNOTA": desligado, enquanto a nota é gerada e seguir com o…](https://ajuda.sankhya.com.br/hc/article_attachments/16779928781335) Mantenha os parâmetros **"GERIMPOSTO":** ligado e **"CONSIMPRETNOTA":** desligado, enquanto a nota é gerada e seguir com o mesmo procedimento anterior.

![Imagem 4: Apague os impostos na grade itens da central "Botão outras opções > Outros impostos".](https://ajuda.sankhya.com.br/hc/article_attachments/16779934759959) Apague os impostos na grade itens da central  "Botão outras opções > Outros impostos".

![Imagem 5: Apague os impostos na grade itens da central "Botão outras opções > Outros impostos".](https://ajuda.sankhya.com.br/hc/article_attachments/14762746420503)

![Imagem 6: Em seguida, refaça o financeiro no botão outras opções da tela e clique em refazer o financeiro.](https://ajuda.sankhya.com.br/hc/article_attachments/16779934763159) Em seguida, refaça o financeiro no botão outras opções da tela e clique em refazer o financeiro.

![Imagem 7: Em seguida, refaça o financeiro no botão outras opções da tela e clique em refazer o financeiro.](https://ajuda.sankhya.com.br/hc/article_attachments/14762755841943)

![Imagem 8: Assim, a retenção dos impostos ocorrerá no momento da baixa e o valor total da nota e do financeiro permanecerão o…](https://ajuda.sankhya.com.br/hc/article_attachments/16779934764439) Assim, a retenção dos impostos ocorrerá no momento da baixa e o valor total da nota e do financeiro permanecerão o mesmo (sem retenção).

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16779928799255) CAUSA:**

Os parâmetros GERIMPOSTO  e CONSIMPRETNOTA influenciam diretamente, pois estando "Desligado" e "Ligado" respectivamente, mesmo excluindo os impostos da tela **"Outros impostos"** e refazendo o financeiro, o valor liquido na movimentação financeira permanece com o desconto da retenção, ficando diferente do valor total da nota.
