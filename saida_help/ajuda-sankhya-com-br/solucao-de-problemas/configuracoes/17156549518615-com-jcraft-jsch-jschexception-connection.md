---
id: "17156549518615"
titulo: "com.jcraft.jsch.JSchException: connection is closed by foreign host"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/17156549518615-com-jcraft-jsch-JSchException-connection-is-closed-by-foreign-host"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:53:40Z"
rotulos: ["Configuração", "Segurança", "Erro de Conexão com Host Remoto", "JSchException", "host remoto", "Erro", "Rede", "Conexão"]
---

# com.jcraft.jsch.JSchException: connection is closed by foreign host

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/17156534202135) **MENSAGEM:**

com.jcraft.jsch.JSchException: connection is closed by foreign host.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17156517864983)SOLUÇÃO:**

**Quando o cliente possui mais de um link de internet para saída do servidor.**

Às vezes o cliente tem na empresa dois links de internet, nesse caso, pode acontecer dele mandar pacotes do acesso remoto pelos dois links, o que gera esse erro. Necessário que o TI da empresa seja acionado e configure para que deixe fixo a saída para o ip 52.67.170.56 por um dos dois links.
