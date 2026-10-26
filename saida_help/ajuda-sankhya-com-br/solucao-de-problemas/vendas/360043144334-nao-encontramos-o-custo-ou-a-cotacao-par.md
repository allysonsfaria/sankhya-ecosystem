---
id: "360043144334"
titulo: "Não encontramos o Custo ou a Cotação para calcular a Base da Substituição Tributária"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043144334-N%C3%A3o-encontramos-o-Custo-ou-a-Cota%C3%A7%C3%A3o-para-calcular-a-Base-da-Substitui%C3%A7%C3%A3o-Tribut%C3%A1ria"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:04:07Z"
rotulos: ["ERRONF", "Custos", "Configuração", "Fiscal", "Impostos", "TOP", "CORE_E00268", "Custo ou cotação faltando para ST", "Ajuste TOP custos e parâmetros", "Falta de dados para cálculo", "Erro"]
---

# Não encontramos o Custo ou a Cotação para calcular a Base da Substituição Tributária

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16120782374679) MENSAGEM**:

[CORE\_E00268] Não encontramos o Custo ou a Cotação para calcular a Base da Substituição Tributária.

**![Imagem 2: SOLUÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/16120782378007) SOLUÇÃO**:

![Imagem 3: Acesse o cadastro da TOP utilizada no lançamento e verifique se realmente o campo " Usa Cus.Méd.Base ST?" precisa estar…](https://ajuda.sankhya.com.br/hc/article_attachments/16120777985431) Acesse o cadastro da TOP utilizada no lançamento e verifique se realmente o campo "**Usa Cus.Méd.Base ST?"** precisa estar marcado. Em caso negativo, desmarque o mesmo e realize um novo teste de faturamento.

**(2)** Tela **"[Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)"** (Caminho de acesso: Comercial » Arquivos » Cadastros)

**(2)** Aba **"Impostos"**,  campo **"Usa Cus.Méd.Base ST?"**

![Imagem 4: (2) Aba "Impostos" , campo "Usa Cus.Méd.Base ST?"](https://ajuda.sankhya.com.br/hc/article_attachments/14628236533399)

![Imagem 5: Se a opção mencionada no item anterior for realmente necessária, verifique na tela de " Variação de Custos de Produtos…](https://ajuda.sankhya.com.br/hc/article_attachments/16120782387863) Se a opção mencionada no item anterior for realmente necessária, verifique na tela de **"[Variação de Custos de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/Varia%C3%A7%C3%A3o%20de%20Custos%20de%20Produtos)"** se todos os produtos envolvidos no faturamento possuem custo e se algum deles não possuir, utilize a rotina de **"[Atualização de Custos de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594114-Varia%C3%A7%C3%A3o-de-Custos-de-Produtos)"** ou o processo de atualização de custos definidos pela empresa.

![Imagem 6: Verifique também os parâmetros "COTCSTDEVTOP" e "COTCSTDEVDIA" , pois quando preenchidos, podem influenciar na…](https://ajuda.sankhya.com.br/hc/article_attachments/16120782392087) Verifique também os parâmetros **"COTCSTDEVTOP"** e **"COTCSTDEVDIA"**, pois quando preenchidos, podem influenciar na ocorrência desta mensagem.

![Imagem 7: Ajustadas as marcações, custos e parâmetros, tente realizar um novo faturamento.](https://ajuda.sankhya.com.br/hc/article_attachments/16120777996055) Ajustadas as marcações, custos e parâmetros, tente realizar um novo faturamento.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16120782396823) CAUSA:**

Mensagem apresentada ao realizar faturamento com Tipo de Operação definido como Usa Cus.Méd.Base ST, e o sistema não encontra valores para compor tal cálculo.
