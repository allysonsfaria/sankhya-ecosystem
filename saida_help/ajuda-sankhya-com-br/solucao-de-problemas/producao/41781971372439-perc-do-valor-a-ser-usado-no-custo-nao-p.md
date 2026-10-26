---
id: "41781971372439"
titulo: "'Perc. do valor a ser usado no custo' não pode ter valor negativo!"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/41781971372439--Perc-do-valor-a-ser-usado-no-custo-n%C3%A3o-pode-ter-valor-negativo"
trilha: "Solução de Problemas > Produção"
atualizado_em: "2026-07-22T13:26:25Z"
rotulos: ["Custos", "Configuração", "Financeiro", "Erro", "Alíquotas de CBS", "Alíquotas de IBS"]
---

# 'Perc. do valor a ser usado no custo' não pode ter valor negativo!

**MENSAGEM**

**Aviso: 'Perc. do valor a ser usado no custo' não pode ter valor negativo!**

**SITUAÇÃO**

Essa mensagem é apresentada quando o usuário tenta inserir um valor negativo no campo **"Perc. do valor a ser usado no custo"**. (exemplo: -100)

**SOLUÇÃO**

**(1)** Acesse a tela para configurar o percentual do custo, **Filtro para Cálculo CIP (Lançamentos Contábeis)** - (**Produção » Cadastros » Filtro para Cálculo CIP (Lançamentos Contábeis)**).

Em seguida, selecione o filtro desejado e informe o percentual que será utilizado no cálculo. O valor deve ser informado apenas com números, **sem o sinal de negativo (-)**.

**Exemplo:** para informar 100%, basta preencher o campo com o valor **100**.

**(2)** Após inserir, salve as alterações.

![Imagem 1: (2) Após inserir, salve as alterações.](https://ajuda.sankhya.com.br/hc/article_attachments/41781971369879)

![Imagem 2: CAUSA](https://ajuda.sankhya.com.br/hc/article_attachments/41781971370135) **CAUSA**

O campo **"Perc. do valor a ser usado no custo"** define o percentual do valor que será considerado no cálculo do custo de uma **Tarifa CIP**.

Esse campo é utilizado, principalmente, em cenários nos quais duas ou mais tarifas compartilham o mesmo filtro de cálculo, mas cada uma deve absorver apenas uma parcela específica do valor apurado. Dessa forma, é possível distribuir o custo entre diferentes tarifas por meio da definição do percentual correspondente a cada uma.

Por se tratar de um percentual de participação no custo, o campo aceita apenas valores positivos, não sendo permitida a utilização de valores negativos.
