---
id: "27048540237207"
titulo: "Data não está dentro do mês de referência - Tela Agendamento (Contabilização)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/27048540237207-Data-n%C3%A3o-est%C3%A1-dentro-do-m%C3%AAs-de-refer%C3%AAncia-Tela-Agendamento-Contabiliza%C3%A7%C3%A3o"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:40:16Z"
rotulos: ["Configuração", "Agendamento", "TOP", "Contabilização", "Financeiro", "Data não está dentro do mês de referência", "Tela Agendamento", "Erro", "Artigo atualizado KCS", "Fiscal/Contábil - KCS"]
---

# Data não está dentro do mês de referência - Tela Agendamento (Contabilização)

O **"Agendamento de contabilização"** (Contabilização >> Rotinas >> Agendamento) é uma funcionalidade essencial para automatizar a geração de **"Lotes contábeis"**, utilizados posteriormente em várias rotinas.

Este artigo apresenta as principais causas e soluções para problemas no agendamento de contabilização, auxiliando na identificação e resolução rápida dessas situações.

### Nenhum lançamento encontrado para contabilizar

Quando o sistema não encontra lançamentos para contabilizar no agendamento, verifique as seguintes configurações:

**(1)** Acesse a tela **"Agendamento"** (Contabilização >> Rotinas >> Agendamento).

**(2)** Verifique se o campo **"Atualiza Contabilidade"** está habilitado na **"TOP"** (Comercial >> Arquivo >> Cadastros >> Tipos de Operação - TOP) utilizada. Sem essa marcação, os lançamentos não serão contabilizados.

**(3)** Confirme se o período delimitado no agendamento está correto. O agendador contabiliza apenas documentos baixados dentro do intervalo informado. Lançamentos fora desse período não serão processados.

**(4)** Revise os filtros de contabilização aplicados. Certifique-se de que não estão criando inconsistências, como filtrar apenas lançamentos a débito sem suas contrapartidas.

### Erro: Data não está dentro do período de referência

Essa mensagem é apresentada quando há uma discordância entre a data do Lote de contabilização e a data do documento que está sendo contabilizado. A data informada na tela **"Agendamento"** (Contabilização >> Rotinas >> Agendamento) deve estar dentro do mesmo mês e ano da data do documento.

![Data não está dentro do mês de referência](https://ajuda.sankhya.com.br/hc/article_attachments/27119931657111)

Existe uma configuração na tela **"TOP Contabilização"** (Contabilização >> Arquivo >> TOP Contabilização), no campo **"Tipo de data"**, que define qual data será considerada para a contabilização. Se o campo definido não estiver dentro do mesmo mês/ano do lote, o erro ocorrerá.

![Configuração de Tipo de Data](https://ajuda.sankhya.com.br/hc/article_attachments/27119931659415)

**Para ajustar os parâmetros de processamento:**

**(2)** Na tela **"Agendamento"**, vá até a aba **"Parâmetros"** e localize a seção **"Processamento dia a dia"**.

**(3)** Configure o campo **"Qtde de dias a retroceder em relação a data de processamento"**. Atenção: ao retroceder dias, o sistema pode acessar um mês/ano diferente do informado inicialmente, gerando o erro.

**(4)** Configure o campo **"Qtde de dias a processar"**.

**(5)** Ao executar manualmente via **"Botão Contabilizar Agora"**, certifique-se de que a data de movimento esteja dentro do período de referência dos lançamentos.

Observação: Se não informar a data, o sistema utilizará a referência atual automaticamente.

### Alternativa: Uso de constantes de data

Em vez de usar a constante **"${dia-a-dia}"**, utilize outras constantes disponíveis para maior flexibilidade:

• **"${DtInicioMes}"**: Indica o início do mês de execução corrente
• **"${DtFimMes}"**: Indica o fim do mês de execução corrente
• **"${DtExec}"**: Indica a data de execução
• **"${DtInicioMesAnterior}"**: Indica o início do mês anterior à execução corrente

###

### Verificação de lançamentos não contabilizados

Para identificar os motivos pelos quais lançamentos não foram contabilizados:

**(1)** Acesse a aba **"Histórico"** na tela de **"Agendamento"** (Contabilização >> Rotinas >> Agendamento).

**(3)** Clique no **"Botão Ver Não Contabilizados"** para visualizar os erros processados.

###
