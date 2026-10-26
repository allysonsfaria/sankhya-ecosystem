---
id: "14224197305495"
titulo: "Tipo de operação não está ativo. Nota de Nro unico: xxx"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/14224197305495-Tipo-de-opera%C3%A7%C3%A3o-n%C3%A3o-est%C3%A1-ativo-Nota-de-Nro-unico-xxx"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T14:59:09Z"
rotulos: ["Configuração", "Central de Vendas", "TOP", "ORA-20101", "Use Monitor de Consulta para verificar erro", "Tipo de operação inativa", "Ativar TOP vinculada", "Erro"]
---

# Tipo de operação não está ativo. Nota de Nro unico: xxx

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16948895305751) MENSAGEM:**

[ORA-20101]: Tipo de operação não está ativo. Nota de Nro unico: xxx
[ORA-06512]: em "xx.TRG\_UPD\_TGFCAB", line xx
[ORA-04088]: erro durante a execução do gatilho 'xx.TRG\_UPD\_TGFCAB'

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16948895310999) SOLUÇÃO:**

![Imagem 3: Inicialmente, verifique se a TOP do lançamento está realmente ativa na tela "Tipos de Operação". Se estiver ativa, siga…](https://ajuda.sankhya.com.br/hc/article_attachments/16970698218135) Inicialmente, verifique se a TOP do lançamento está realmente ativa na tela **"Tipos de Operação".** Se estiver ativa, siga para tratativa abaixo:

![Imagem 4: Acesse a tela "Monitor de Consulta " e inicie o Monitoramento;](https://ajuda.sankhya.com.br/hc/article_attachments/16970698222871) Acesse a tela **"Monitor de Consulta**" e inicie o Monitoramento;

![Imagem 5: Volte na Central de Venda e confirme a nota, nesse ponto será apresentada o erro:](https://ajuda.sankhya.com.br/hc/article_attachments/16970681790743) Volte na Central de Venda e confirme a nota, nesse ponto será apresentada o erro:

[ORA-20101]: Tipo de operação não está ativo. Nota de Nro unico: xxx

Volte no Monitor de Consulta e pare o Monitoramento.

**![Imagem 6: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16970698226199) OBSERVAÇÃO:**

Manual sobre a rotina Monitor de Consulta

[Monitor de Consultas – Sankhya Gestão de Negócios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108733-Monitor-de-Consultas)

![Imagem 7: Após parar o monitoramento, será gerado um arquivo com Monitor de Processo e outro com Monitor de Consulta;](https://ajuda.sankhya.com.br/hc/article_attachments/16970698227607) Após parar o monitoramento, será gerado um arquivo com Monitor de Processo e outro com Monitor de Consulta;

![Imagem 8: Abra o Monitor de Processo e busque pelo erro, será apresentado o ID;](https://ajuda.sankhya.com.br/hc/article_attachments/16970681798935) Abra o Monitor de Processo e busque pelo erro, será apresentado o ID;

![Imagem 9: Abra o Monitor de Processo e busque pelo erro, será apresentado o ID;](https://ajuda.sankhya.com.br/hc/article_attachments/16749156719895)

![Imagem 10: Feito isso, abra o Monitor de Consulta e busque pelo mesmo ID apresentado no Monitor de Processo;](https://ajuda.sankhya.com.br/hc/article_attachments/16970698232343) Feito isso, abra o Monitor de Consulta e busque pelo mesmo ID apresentado no Monitor de Processo;

![Imagem 11: Nele vai ser possível identificar qual top esta sendo solicitada no erro;](https://ajuda.sankhya.com.br/hc/article_attachments/16970681804695) Nele vai ser possível identificar qual top esta sendo solicitada no erro;

![Imagem 12: Nele vai ser possível identificar qual top esta sendo solicitada no erro;](https://ajuda.sankhya.com.br/hc/article_attachments/16749158601367)

![Imagem 13: Acesse o cadastro da TOP e ative a.](https://ajuda.sankhya.com.br/hc/article_attachments/16970681808407) Acesse o cadastro da TOP e ative a.

**![Imagem 14: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16948936081815) CAUSA:**

Geralmente ocorre quando está utilizando uma TOP que está ativa, mas consta outra TOP vinculada, por exemplo, top denegada e essa está desativada

**(1)** **TOP 1100**

![Imagem 15: TOP 1114](https://ajuda.sankhya.com.br/hc/article_attachments/17036347621527)
 
**(1)** **TOP 1114**

![Imagem 16: (1) TOP 1114](https://ajuda.sankhya.com.br/hc/article_attachments/17036419399191)
