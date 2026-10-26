---
id: "11062613737111"
titulo: "Servidor de Acessos conectando com o banco de dados, tente mais tarde"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/11062613737111-Servidor-de-Acessos-conectando-com-o-banco-de-dados-tente-mais-tarde"
trilha: "Solução de Problemas > Acessos/Banco de Dados"
atualizado_em: "2026-07-22T15:02:08Z"
rotulos: ["Configuração", "Segurança", "Atualização", "Financeiro", "Problemas de Conexão do Servidor de Acessos ao Banco de Dados", "Conexão servidor de acessos Problemas de comunicação Solução divergência de horário", "Horário de Brasília Atualização Comunicação de Rede", "Erro"]
---

# Servidor de Acessos conectando com o banco de dados, tente mais tarde

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16913810974743) MENSAGEM:**

Servidor de Acessos conectando com o banco de dados, tente mais tarde.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16913816189463) CAUSA:**

Possíveis causas de problemas com o SAS:

- Horário do servidor de aplicação divergente do fuso horário padrão de Brasília (UTC-3/GMT-3). Exceto os estados que não participam do fuso horário de Brasilia.
- Versão defasada do SAS.
- Falha na comunicação da rede interna entre o servidor onde encontra-se o SAS instalado e o banco de dados.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16913810982039) SOLUÇÃO:**

Como nosso hub de licença valida com o horário de Brasília, qualquer divergência na data e hora, impede do SAS se comunicar com nosso hub. Sendo assim é necessário a hora do servidor de aplicação, normalizando os acessos.

Caso o erro seja causado pela versão defasada do SAS é necessário atualização do mesmo.

Em casos de falha na rede interna, se faz necessário acionar o T.I responsável pela infraestrutura para garantir a comunicação entre os servidores.
