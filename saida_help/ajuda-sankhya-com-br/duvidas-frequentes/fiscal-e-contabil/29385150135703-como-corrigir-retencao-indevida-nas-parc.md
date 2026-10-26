---
id: "29385150135703"
titulo: "Como corrigir retenção indevida nas parcelas dos Impostos Retidos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/29385150135703-Como-corrigir-reten%C3%A7%C3%A3o-indevida-nas-parcelas-dos-Impostos-Retidos"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:37:11Z"
rotulos: ["Configuração", "Parceiro", "Movimentação Financeira", "Impostos", "Financeiro", "RETIMPPARCNOTA"]
---

# Como corrigir retenção indevida nas parcelas dos Impostos Retidos

![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/29963730111127)**SOLUÇÃO:**

Ao gerar uma nota fiscal que contenha retenção de impostos, o sistema proporcionaliza a retenção de acordo com o valor de cada parcela, mesmo que ela seja relativa ao valor de imposto.

Para corrigir e flexibilizar esse comportamento, foi criado o parâmetro **RETIMPPARCNOTA - 'Reter impostos (ISS, INSS, IRF) p/ Parc. da nota?'.**

Abaixo estão os detalhes de funcionamento do parâmetro:

**Comportamento do Parâmetro:**

-**Padrão**: O parâmetro é configurado como desligado.
-**Ligado**: Quando ativado, o sistema **não realizará o cálculo de impostos retidos** nas parcelas financeiras cuja associação de parceiro seja diferente da nota.
-**Desligado**: Caso permaneça desativado, o sistema **calculará os impostos retidos para todas as parcelas financeiras**, seguindo o comportamento anterior.

**Configuração Requerida:**

-É importante configurar o parâmetro **'Reter impostos (ISS,INSS,IRF) p/ Parc. da nota? - RETIMPPARCNOTA'** antes de efetuar o lançamento da nota fiscal.

**Impacto no Processo:**

-Este parâmetro permite maior controle sobre o cálculo de impostos retidos, evitando divergências nos valores financeiros associados às parcelas da nota fiscal.

Recomenda-se que os usuários revisem as configurações do sistema e certifiquem-se de que o parâmetro esteja configurado de acordo com a necessidade da operação antes de realizar o lançamento de notas. fiscais.
