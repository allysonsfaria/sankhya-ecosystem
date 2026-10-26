---
id: "1500003322601"
titulo: "Endereço do site da UF da Consulta por chave de acesso diverge do previsto"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003322601-Endere%C3%A7o-do-site-da-UF-da-Consulta-por-chave-de-acesso-diverge-do-previsto"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:25:08Z"
rotulos: ["Configuração", "NF-e", "Atualização", "SEFAZ", "NFC-e", "não apagar", "878", "Atualização de URL para Consulta NFC-e", "Erro"]
---

# Endereço do site da UF da Consulta por chave de acesso diverge do previsto

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16334679450135) MENSAGEM**:

[Rejeição 878]: Endereço do site da UF da Consulta por chave de acesso diverge do previsto.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16334695082903) SOLUÇÃO:**

**(1)** É importante **manter a versão do sistema atualizada**, garantindo que a URL (**urlChave)** enviada para a SEFAZ esteja devidamente atualizada.  Para tal verifique as versões disponíveis, acessando: <http://downloads.sankhya.com.br/versoes-anteriores>

**(1)** Além disso, realize a **atualização das URL´s** através da tela **"Console NF-e":**

**(1)** Realizada a atualização, refaça o faturamento. Caso o problema persista, acione o Service Desk Especializado para uma análise detalhada de possíveis alterações de URL no Estado emissor.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16334695084951) CAUSA:**

A rejeição é apresentada quando é emitida uma NFC-e (modelo 65) e o endereço de consulta (Campo: urlChave - ID: ZX03) está divergente do usado pela Sefaz Autorizadora.
