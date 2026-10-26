---
id: "15861494058775"
titulo: "O pedido XX ja esta sendo faturado neste momento pelo usuário X"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/15861494058775-O-pedido-XX-ja-esta-sendo-faturado-neste-momento-pelo-usu%C3%A1rio-X"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:55:58Z"
rotulos: ["Configuração", "Cache", "Faturamento", "Administração do Servidor", "CORE_E04682", "Erro de Faturamento Preso por Usuário", "Erro"]
---

# O pedido XX ja esta sendo faturado neste momento pelo usuário X

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/15861445221143) MENSAGEM:**

[CORE\_E04682] O pedido XX ja esta sendo faturado neste momento pelo usuário X.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/15861450918295) CAUSA:**

Pode ocorre por alguma instabilidade ou faturamento "preso" na aplicação.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/15861461601815) SOLUÇÃO:**

O sistema geralmente costuma apresentar essa mensagem quando algum procedimento de faturamento acaba ficando "preso" na aplicação após algum problema de conexão ou instabilidade, ou até mesmo em função de alguma encerramento de sessão indevido. 
Por mais que o usuário não esteja acessando o sistema naquele momento, pode ser que o processo de faturamento esteja vinculado na sessão e por isso a execução da rotina esteja impedida de ser concluída.
 Para solucionar o problema, é possível reinicializar o sistema através da tela Administração do Servidor, na aba Geral.
 
\* Administração do Servidor (Configurações » Avançado » Administração do Servidor)
\* Aba Geral » Descartar Cache
\* Aba Geral » Reinicializar Sistema

![Imagem 4: O sistema geralmente costuma apresentar essa mensagem quando algum procedimento de faturamento acaba ficando "preso" na…](https://ajuda.sankhya.com.br/hc/article_attachments/15861429106071)
