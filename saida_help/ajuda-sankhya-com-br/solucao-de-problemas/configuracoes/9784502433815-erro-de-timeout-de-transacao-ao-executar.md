---
id: "9784502433815"
titulo: "Erro de timeout de transação ao executar alguma rotina"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9784502433815-Erro-de-timeout-de-transa%C3%A7%C3%A3o-ao-executar-alguma-rotina"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:06:07Z"
rotulos: ["Configuração", "Administração do Servidor", "não apagar", "Ajuste de Timeout em Transações de Sistema", "Erro", "Timeout"]
---

# Erro de timeout de transação ao executar alguma rotina

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16778981384471) MENSAGEM**:

ARJUNA0... The transaction is not active

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16778995853463) SOLUÇÃO:**

Acesse a tela **"Administração do Servidor"** (Caminho de acesso: Configurações » Avançado » Administração do Servidor)
Na aba **"Avançado",** insira um intervalo em minutos no campo "**Timeout em minutos**", por exemplo: 120 minutos e clique em Aplicar.

![Imagem 3: Acesse a tela "Administração do Servidor" (Caminho de acesso: Configurações » Avançado » Administração do Servidor) Na…](https://ajuda.sankhya.com.br/hc/article_attachments/9784499608471)

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16778981397271) CAUSA:**

Mensagem apresentada quando uma transação ultrapassa o tempo limite determinado.
