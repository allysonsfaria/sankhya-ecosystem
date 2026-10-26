---
id: "4403786556823"
titulo: "Valor e índice do evento  50- Hora Extra no log de calculo de médias divergente do Acumulados do ano. Saiba mais! "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4403786556823-Valor-e-%C3%ADndice-do-evento-50-Hora-Extra-no-log-de-calculo-de-m%C3%A9dias-divergente-do-Acumulados-do-ano-Saiba-mais"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:35:50Z"
rotulos: ["Configuração", "Eventos", "Folha", "eSocial", "Erro: Divergência de valor e índice no evento 50", "Solução: Ajustar índices e recalcular férias", "Causa: Unidade \"Horas\" mal convertida na TFPACU", "Central de Projetos"]
---

# Valor e índice do evento  50- Hora Extra no log de calculo de médias divergente do Acumulados do ano. Saiba mais! 

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16345473341591) MENSAGEM**:

Sistema está levando valor e índice divergentes do evento de 50- Hora Extra para o log de calculo de médias, nos meses de abril e junho, dos índices que foram informados na tabela acumulados do ano (TFPACU).

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16345473345303)SOLUÇÃO:**

Faça o ajuste dos índices de acordo com a unidade (horas), informada na tabela acumulados do ano (TFPACU), a quantidade de horas para os meses que estão incorretos.

Depois, realize o recalculo das férias (ou do cálculo que estava sendo feito) para que a o log assuma os valores corrigidos.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16345473346711) CAUSA:**

O evento e-50 tem como unidade "Horas", então deve ser lançado na  TFPACU os valores correspondentes a quantidade de horas, para que o sistema faça a transição para decimais através do próprio cálculo automaticamente.
Neste caso, como foi lançado na TFPACU em abril 3,90 (3horas e 90 minutos) o sistema entendeu que eram 4 horas e 30 minutos devido a configuração do evento ser unidade horas. E em junho 9,62 (9horas e 62 minutos) o sistema entende 10 horas e 02 minutos.

Tela acumulados do ano.

![Imagem 4: Tela acumulados do ano.](https://ajuda.sankhya.com.br/hc/article_attachments/15083022762007)

 Log apresentando a médias do evento 50 -HORAS EXTRA.

![Imagem 5: Log apresentando a médias do evento 50 -HORAS EXTRA.](https://ajuda.sankhya.com.br/hc/article_attachments/4403786483991)
