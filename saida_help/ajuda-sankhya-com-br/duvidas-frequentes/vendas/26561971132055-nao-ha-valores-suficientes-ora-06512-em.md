---
id: "26561971132055"
titulo: "Não há valores suficientes ORA-06512: em \"SNK_MATGIRCALCSUG\", line 424 ORA-06512: em line 1"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26561971132055-N%C3%A3o-h%C3%A1-valores-suficientes-ORA-06512-em-SNK-MATGIRCALCSUG-line-424-ORA-06512-em-line-1"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-22T14:41:15Z"
rotulos: ["Configuração", "Análise de Giro", "Financeiro", "ORA-06512", "Passos para resolver", "Razão do erro", "Detalhe do erro", "não há valores suficientes", "ORA-00947", "Erro"]
---

# Não há valores suficientes ORA-06512: em "SNK_MATGIRCALCSUG", line 424 ORA-06512: em line 1

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/26561921634455) **MENSAGEM:**

ORA-00947: não há valores suficientes ORA-06512: em "SNK\_MATGIRCALCSUG", line 424 ORA-06512: em line 1

O erro ocorre quando existe um excesso de informações a serem processadas na Análise de Giro e o banco de dados não conseguiu atender a demanda.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26561971076887)SOLUÇÃO:**

**(1)**Algumas configurações podem ser realizadas a fim de melhor a performance da consolidação de dados e do processo da matriz, que solucionam o erro.

![Imagem 3: O parâmetro "CALCMARLUCGIRO - Calcular margem e lucro no consolidador de giro?" tem a função de calcular a margem de…](https://ajuda.sankhya.com.br/hc/article_attachments/26561921641367) O parâmetro **"CALCMARLUCGIRO - Calcular margem e lucro no consolidador de giro?"** tem a função de calcular a margem de lucro dos itens na consolidação de dados, isso acrescenta vários cálculos que podem demandar um maior processamento do banco de dados . O padrão do parâmetro é desligado, mas caso esteja ligado e a margem de lucro não é necessária dentro da análise de giro, a melhor prática é deixar desabilitado.

![Imagem 4: Em "Outras Opções > Agendamento da geração da tabela de giro", verifique os campos de quantidade de meses a consolidar…](https://ajuda.sankhya.com.br/hc/article_attachments/26561971091095) Em "Outras Opções > Agendamento da geração da tabela de giro", verifique os campos de quantidade de meses a consolidar última compra/venda e a quantidade de meses para consolidar o giro, a fim de configurar apenas a quantidade necessária em sua análise.

![Imagem 5: Em "Outras Opções > Agendamento da geração da tabela de giro", verifique os campos de quantidade de meses a consolidar…](https://ajuda.sankhya.com.br/hc/article_attachments/26623418457751)

![Imagem 6: Ainda no agendamento, clique na seta ao lado da lixeira, depois em "Limpar consolidação (TGFGIR1)" . Isso fará com que…](https://ajuda.sankhya.com.br/hc/article_attachments/26561921653143) Ainda no agendamento, clique na seta ao lado da lixeira, depois em **"Limpar consolidação (TGFGIR1)"**. Isso fará com que a consolidação seja limpa e uma nova comece a rodar de imediato.

![Imagem 7: Ainda no agendamento, clique na seta ao lado da lixeira, depois em "Limpar consolidação (TGFGIR1)" . Isso fará com que…](https://ajuda.sankhya.com.br/hc/article_attachments/26623418459799)

![Imagem 8: Feito os passos acima faça o processamento da matriz.](https://ajuda.sankhya.com.br/hc/article_attachments/26561921658135) Feito os passos acima faça o processamento da matriz.

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/26561971115415)CAUSA:**

O erro ocorre quando existe um excesso de informações a serem processadas na Análise de Giro e o banco de dados não conseguiu atender a demanda.
