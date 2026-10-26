---
id: "10408646500119"
titulo: "Quais as regras do sistema para cálculo da data de vencimento dos títulos com origem = estoque "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10408646500119-Quais-as-regras-do-sistema-para-c%C3%A1lculo-da-data-de-vencimento-dos-t%C3%ADtulos-com-origem-estoque"
trilha: "Dúvidas Frequentes > Financeiro"
atualizado_em: "2026-07-22T15:03:47Z"
rotulos: ["Configuração", "Parâmetros", "Estoque", "Financeiro", "Títulos", "Ticket231073", "\"DTCALCVENC\" define a data base", "Sem parâmetros usa a Data de Negociação", "\"FORCDTFATCOMPRA\" usa a data de faturamento"]
---

# Quais as regras do sistema para cálculo da data de vencimento dos títulos com origem = estoque 

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19574886431255) SOLUÇÃO:**

![Imagem 2: Se o parâmetro "Data Base p/ Cálculo do Vencimento no Faturamento - DTCALCVENC" estiver configurado para "Data de…](https://ajuda.sankhya.com.br/hc/article_attachments/20471356788887) Se o parâmetro **"Data Base p/ Cálculo do Vencimento no Faturamento - DTCALCVENC"**  estiver configurado para **"Data de Saída"** e o campo Data de Entrada Saída preenchido:

- Será considerado a data Base = DTENTSAI (Data de Entrada e Saída)

![Imagem 3: Se o parâmetro " Força Dt. Fat. c/ Base p/ Cálculo Venc. na compra?: - FORCDTFATCOMPRA" ligado e é Pedido/Nota de…](https://ajuda.sankhya.com.br/hc/article_attachments/19574876422167) Se o parâmetro "**Força Dt. Fat. c/ Base p/ Cálculo Venc. na compra?: - FORCDTFATCOMPRA"** ligado e é Pedido/Nota de Compra e o campo Data Faturamento preenchido

- Será considerado a Data Base = DTFATUR (Data de Faturamento)

\*\* O parâmetro "**Força Dt. Fat. c/ Base p/ Cálculo Venc. na compra?: - FORCDTFATCOMPRA"** quando habilitado, o sistema irá considerar a data de faturamento como base para calcular o vencimento nas compras. Deste modo, o parâmetro "Data Base p/ Cálculo do Vencimento no Faturamento - DTCALCVENC" não será aplicado.

![Imagem 4: Se o parâmetro "Data Base p/ Cálculo do Vencimento no Faturamento - DTCALCVENC" estiver configurado para qualquer opção…](https://ajuda.sankhya.com.br/hc/article_attachments/19574886444823) Se o parâmetro **"Data Base p/ Cálculo do Vencimento no Faturamento - DTCALCVENC"** estiver configurado para qualquer opção que não seja "Negociação" e o campo Data Faturamento preenchido

- Será considerado a Data Base = DTFATUR (Data de Faturamento)

| **Importante:** Se nenhum dos anteriores for atendido será considerado **a Data Base = DTNEG (Data de Negociação)** |
| --- |
