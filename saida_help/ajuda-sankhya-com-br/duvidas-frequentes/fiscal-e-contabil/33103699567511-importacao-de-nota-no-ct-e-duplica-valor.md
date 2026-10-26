---
id: "33103699567511"
titulo: "Importação de nota no CT-e duplica valores na Medida"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33103699567511-Importa%C3%A7%C3%A3o-de-nota-no-CT-e-duplica-valores-na-Medida"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:29:41Z"
rotulos: ["ERROCTE", "CT-e", "Configuração", "NF-e", "Portal de Vendas", "Medidas", "Importação", "Passos para resolver", "Razão do erro", "Detalhe do erro", "quantidade na Medida está sendo duplicada"]
---

# Importação de nota no CT-e duplica valores na Medida

**SITUAÇÃO:**

Ao importar uma nota para o CTe, a quantidade na **Medida** está sendo duplicada.

O problema ocorre ao importar a nota fiscal através do caminho ''**Notas de Conhecimento de Transporte**'' > **''Outras opções''** > '**'Importação de NF-e para CT-e''**.

![Imagem 1: O problema ocorre ao importar a nota fiscal através do caminho '' Notas de Conhecimento de Transporte '' > ''Outras…](https://ajuda.sankhya.com.br/hc/article_attachments/33103699536919)

Veja na imagem abaixo que a quantidade aparece duplicada:

![Imagem 2: Veja na imagem abaixo que a quantidade aparece duplicada:](https://ajuda.sankhya.com.br/hc/article_attachments/33103699539095)

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/33103699541143)SOLUÇÃO:**

A informação da quantidade na medida é preenchida com base no **Peso Líquido** ou **Peso Bruto** da nota fiscal. O problema de duplicação ocorre quando, nas configurações do '**'Portal de Vendas''> Mais Opções''** > '**'Preferências para Importação de NF-e para CT-e**'', na aba **''Medidas'**', estão selecionadas simultaneamente as opções de enviar tanto o Peso Líquido quanto o Peso Bruto.

![Imagem 4: A informação da quantidade na medida é preenchida com base no Peso Líquido ou Peso Bruto da nota fiscal. O problema de…](https://ajuda.sankhya.com.br/hc/article_attachments/33103708911127)

Para solucionar o problema, configure apenas uma das opções (Peso Líquido ou Peso Bruto) e defina a outra como **''Não informar'**'.

![Imagem 5: Para solucionar o problema, configure apenas uma das opções (Peso Líquido ou Peso Bruto) e defina a outra como ''Não…](https://ajuda.sankhya.com.br/hc/article_attachments/33174826669335)

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/33103699547671)CAUSA:**

Esse problema de duplicação ocorre quando no '**'Portal de Vendas''> Mais Opções''** > '**'Preferências para Importação de NF-e para CT-e**'', na aba **''Medidas'**' estão selecionadas simultaneamente as opções para enviar o Peso Líquido e o Peso Bruto.
