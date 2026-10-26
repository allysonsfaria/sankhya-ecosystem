---
id: "360043356953"
titulo: "Não foi possível obter conexão com a internet"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043356953-N%C3%A3o-foi-poss%C3%ADvel-obter-conex%C3%A3o-com-a-internet"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:05:40Z"
rotulos: ["#PUBLIFER", "Configuração", "NF-e", "Atualização", "CORE_E03975", "Não foi possível obter conexão com a internet", "Sem conexão com a internet", "URL incorreta no console do SanNFe", "Erro", "Documentos Eletrônicos"]
---

# Não foi possível obter conexão com a internet

**MENSAGEM:**

Não foi possível obter conexão com a internet.

**SITUAÇÃO:**

Mensagem retornada na emissão de nota fiscal eletrônica.

**SOLUÇÃO:**

**(1)** Mantenha a versão SANNFE atualizada, conforme versão banco/aplicação atuais. Para consulta de versões disponíveis acesse: **"[Downloads Sankhya](http://downloads.jiva.com.br/)".**

**(2)** Acesse a tela **"CONSOLE NF-e"**, na aba **"Status do Serviço"**, verifique se existe URL configurada em **"Configuração e teste de conectividade com a internet"**:

![Imagem 1: (2) Acesse a tela "CONSOLE NF-e" , na aba "Status do Serviço" , verifique se existe URL configurada em "Configuração e…](https://ajuda.sankhya.com.br/hc/article_attachments/14532618744087)

**(3)** Em caso positivo, remova os links inseridos e teste uma nova geração de lote.

**CAUSA**

Ocorre quando no console do SanNFe, na aba: Status do Serviço, no campo URL para teste, foi informado alguma URL e foi deixada, neste caso é preciso removê-la.
