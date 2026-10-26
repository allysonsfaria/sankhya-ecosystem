---
id: "360053148034"
titulo: "Lock time out. SQL Server connection timed out"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360053148034-Lock-time-out-SQL-Server-connection-timed-out"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:28:44Z"
rotulos: ["Configuração", "SQL Server", "#formatadoroger", "Timeout Excedido no SQL Server: Solução Rápida", "Erro", "Timeout", "BDE"]
---

# Lock time out. SQL Server connection timed out

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/18585757963927) MENSAGEM**:

Lock time out. SQL Server connection timed out.

**![Imagem 2: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/18585757971607) CAUSA**:

Mensagem apresentada devido ao timeout padrão do BDE para SQL Server que é de 300 segundos.

**![Imagem 3: SOLUÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/18585757982999) SOLUÇÃO**:

![Imagem 4: Acesse o BDE no diretório de instalação como 'Administrador' Aba: Configuration>>Drivers>>Native>>MSSQL](https://ajuda.sankhya.com.br/hc/article_attachments/18585757988503) Acesse o BDE no diretório de instalação como 'Administrador'
Aba: Configuration>>Drivers>>Native>>MSSQL

-**MAX QUERY TIME** = 900 [Altere de 300 para 900]

Salve clicando na seta azul para direita(Apply)

[GIF animado: Imagem 5: Salve clicando na seta azul para direita(Apply)](https://ajuda.sankhya.com.br/hc/article_attachments/360091393493)

O valor configurado por padrão é de 300 segundos, pode-se aumentá-lo para 900 de modo a ter maior tempo para a resposta.

**Nota**: Caso não tenha permissões, solicite ao Administrador, que execute o procedimento.

![Imagem 6: Após os ajustes, acesse novamente o sistema.](https://ajuda.sankhya.com.br/hc/article_attachments/18585757990423)Após os ajustes, acesse novamente o sistema.
