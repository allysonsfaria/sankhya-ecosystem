---
id: "26733384150807"
titulo: "Campo no Absenteísmo no dash está alterando conforme a quantidade de vezes que clica em atualizar"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26733384150807-Campo-no-Absente%C3%ADsmo-no-dash-est%C3%A1-alterando-conforme-a-quantidade-de-vezes-que-clica-em-atualizar"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-07-22T14:40:48Z"
rotulos: ["Configuração", "Relatórios", "XML", "Atualização", "Passos para resolver", "Razão do erro", "Detalhe do erro", "clica em atualizar", "Campo no Absenteísmo no dash está alterando", "Erro"]
---

# Campo no Absenteísmo no dash está alterando conforme a quantidade de vezes que clica em atualizar

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/26733393048599) **MENSAGEM:**

Campo no Absenteísmo no dash está alterando conforme a quantidade de vezes que clica em atualizar.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26733384142871)SOLUÇÃO:**

O problema ocorre quando, na tela **"Construtor de Componentes de BI",** na aba **"Parâmetro",** se trabalha com parâmetro do tipo período, mas na query usou um TO\_DATE antes do valor : TO\_DATE(CAST(TO\_TIMESTAMP(?, 'yyyy-mm-dd') AS DATE), 'DD/MM/YYYY').

Pois, quando o parâmetro é do tipo período, o trecho CAST(TO\_TIMESTAMP(?, 'yyyy-mm-dd') AS DATE) é adicionado automaticamente. Assim, não é necessário o TO\_DATE no xml.

![Imagem 3: Pois, quando o parâmetro é do tipo período, o trecho CAST(TO_TIMESTAMP(?, 'yyyy-mm-dd') AS DATE) é adicionado…](https://ajuda.sankhya.com.br/hc/article_attachments/26733384145047)

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/26733393056151)CAUSA:**

Problema ocorre quando é informado o TO\_DATE em um parâmetro de período, pois essa informação já é adicionada automaticamente pelo sistema. Caso seja informado um dado, será gerada a duplicidade.
