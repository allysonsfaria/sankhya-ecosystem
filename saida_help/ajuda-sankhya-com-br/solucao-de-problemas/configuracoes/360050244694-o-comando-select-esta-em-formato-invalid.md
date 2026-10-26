---
id: "360050244694"
titulo: "O comando SELECT está em formato inválido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360050244694-O-comando-SELECT-est%C3%A1-em-formato-inv%C3%A1lido"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:30:52Z"
rotulos: ["Configuração", "Relatórios", "Parâmetro", "Corrigindo Formato Inválido do Comando SELECT", "WildFly", "Erro"]
---

# O comando SELECT está em formato inválido

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18585675007895) MENSAGEM:**

O comando SELECT está em formato inválido.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18585675014167) CAUSA:**

Utilização de querys em relatórios/dashboards que utilizam a expressão WITH.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18585690091287) SOLUÇÃO:**

![Imagem 4: Acesse o servidor onde o Wildfly está instalado e na pasta WILDFLY_HOME/standalone/bin localize o seguinte arquivo:](https://ajuda.sankhya.com.br/hc/article_attachments/18585675034903) Acesse o servidor onde o Wildfly está instalado e na pasta WILDFLY\_HOME/standalone/bin localize o seguinte arquivo:

- Se o sistema operacional for Linux, abrir para edição o arquivo **standalone.conf**
- Se Windows, o arquivo a ser editado é o **standalone.conf.bat**

![Imagem 5: Localize então em tal arquivo, o argumento: -Djape.jdbc.check.select=true e alterá-lo para false, ficando:…](https://ajuda.sankhya.com.br/hc/article_attachments/18585675043479) Localize então em tal arquivo, o argumento: **-Djape.jdbc.check.select=true** e alterá-lo para false, ficando: **-Djape.jdbc.check.select=false**

![Imagem 6: Em seguida reinicie o sistema a partir do próprio servidor para que a alteração entre em vigor.](https://ajuda.sankhya.com.br/hc/article_attachments/18585675053847) Em seguida reinicie o sistema a partir do próprio servidor para que a alteração entre em vigor.
