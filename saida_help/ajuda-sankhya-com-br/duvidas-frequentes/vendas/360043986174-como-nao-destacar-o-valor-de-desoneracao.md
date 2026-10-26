---
id: "360043986174"
titulo: "Como não destacar o valor de desoneração no DANFE?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043986174-Como-n%C3%A3o-destacar-o-valor-de-desonera%C3%A7%C3%A3o-no-DANFE"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-22T15:57:19Z"
rotulos: ["Configuração", "Impressão", "NF-e", "XML", "DANFE", "Não destacar valor de desoneração  DANFE", "Atualize para modelo mais recente se preferir", "Para remover desoneração ajuste no IReport"]
---

# Como não destacar o valor de desoneração no DANFE?

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17125371963927) SITUAÇÃO:**

No modelo de DANFE Padrão Sankhya, o valor de desoneração é destacado na coluna "Valor Desconto".

Isso ocorre devido a seguinte sintaxe:

- DanfeUtils.getCurrencyAsBigDecimal(DanfeUtils.convertCalculaValor($F{ValorDesconto}, **$F{ValorDesoneracao**}))

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17125371967255) SOLUÇÃO:**

![Imagem 3: Caso o cliente não deseje que o valor de desoneração seja destacado, a sintaxe deverá ser alterada via Ireport para:](https://ajuda.sankhya.com.br/hc/article_attachments/17125414517015) Caso o cliente não deseje que o valor de desoneração seja destacado, a sintaxe deverá ser alterada via Ireport para:

- DanfeUtils.getCurrencyAsBigDecimal(DanfeUtils.convertCalculaValor($F{ValorDesconto}))

Essa configuração é realizada no Text field Expression do IReport.

Caso tenha mais personalizações em seu modelo de impressão de NF-e, faça somente o ajuste acima.

**ou**

![Imagem 4: Caso deseje, poderá atualizar para um modelo mais recente que já contempla o ajuste, não sendo necessário nenhuma…](https://ajuda.sankhya.com.br/hc/article_attachments/17125371972887) Caso deseje, poderá atualizar para um modelo mais recente que já contempla o ajuste, não sendo necessário nenhuma intervenção no modelo.
Para tal, acesse a rotina: Comercial » Arquivo » Cadastros » Modelo de Impressão (Nota/Pedido, clique no botão: **"Baixar Modelos Padrões"**, e baixe a versão mais recente de Impressão de NF-e(DANFE) 4.0.

**![Imagem 5: OBSERVAÇÕES:](https://ajuda.sankhya.com.br/hc/article_attachments/17125371976471) OBSERVAÇÕES:**

![Imagem 6: Quando o ICMS desonerado não for abatido do valor total da nota, esse não destaque no DANFE poderá ocorrer. Sendo…](https://ajuda.sankhya.com.br/hc/article_attachments/17125414517015) Quando o ICMS desonerado não for abatido do valor total da nota, esse não destaque no DANFE poderá ocorrer. Sendo válido uma sintonia com contador antes de validar tal alteração.

![Imagem 7: Alteração a ser realizada por um usuário com conhecimento na ferramenta Ireport. Para mais detalhes: Melhores práticas…](https://ajuda.sankhya.com.br/hc/article_attachments/17125371972887) Alteração a ser realizada por um usuário com conhecimento na ferramenta Ireport. Para mais detalhes: [Melhores práticas para personalização do DANFE na Impressão de NF-e [Ireport].](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044579874)
