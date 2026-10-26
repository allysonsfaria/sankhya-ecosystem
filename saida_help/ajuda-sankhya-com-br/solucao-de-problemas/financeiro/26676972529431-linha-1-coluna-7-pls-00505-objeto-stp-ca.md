---
id: "26676972529431"
titulo: "linha 1, coluna 7: PLS-00505 objeto STP_CALCULARCUSTOMEDIODIA Invalido ORA-06550 linha 1, coluna 7: PL/SQL Statement ignored"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26676972529431-linha-1-coluna-7-PLS-00505-objeto-STP-CALCULARCUSTOMEDIODIA-Invalido-ORA-06550-linha-1-coluna-7-PL-SQL-Statement-ignored"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T14:40:49Z"
rotulos: ["Custos", "Configuração", "Preferências", "Passos para resolver", "Razão do erro", "Detalhe do erro", "ORA-06550", "linha 1 coluna 7: PLS-00505 objeto STP_CALCULARCUSTOMEDIODIA", "Erro"]
---

# linha 1, coluna 7: PLS-00505 objeto STP_CALCULARCUSTOMEDIODIA Invalido ORA-06550 linha 1, coluna 7: PL/SQL Statement ignored

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/26676972507927) **MENSAGEM:**

ORA-06550 linha 1, coluna 7: PLS-00505 objeto STP\_CALCULARCUSTOMEDIODIA Invalido ORA-06550 linha 1, coluna 7: PL/SQL Statement ignored

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26676972510359)SOLUÇÃO:**

![Imagem 3: Acesse a tela "Preferências" (Caminho: Configurações » Avançado » Preferências) e altere o parâmetro "CALCCUSTOASSINC"…](https://ajuda.sankhya.com.br/hc/article_attachments/26676987771927) Acesse a tela **"Preferências"** (Caminho: Configurações » Avançado » Preferências) e altere o parâmetro **"CALCCUSTOASSINC"** para a opção **"Transação por nota".**

Através do parâmetro Cálculo de Custo Assíncrono - CALCCUSTOASSINC que, por padrão é apresentado desativado, determine como o sistema procederá com o cálculo de custos, conforme as seguintes opções:

**(1)** **Transação por Nota:** o sistema efetuará uma transação por nota para realizar o cálculo de custos;
**(1)** **Transação por item:** por essa opção tem-se uma transação item à item para realização do cálculo de custos;
**(1)** **Desabilitado:** o cálculo do custo não será feito de maneira assíncrona.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/26676987776279)CAUSA:**

Quando o cálculo do custo não é feito de maneira assíncrona, a quantidade de linhas de custos a serem calculadas podem ocasionar o erro.
