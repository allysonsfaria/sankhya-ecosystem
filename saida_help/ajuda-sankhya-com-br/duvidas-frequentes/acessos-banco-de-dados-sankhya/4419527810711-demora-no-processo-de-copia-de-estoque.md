---
id: "4419527810711"
titulo: "Demora no processo de Copia de Estoque"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4419527810711-Demora-no-processo-de-Copia-de-Estoque"
trilha: "Dúvidas Frequentes > Acessos/Banco de Dados - Sankhya"
atualizado_em: "2026-07-22T15:19:55Z"
rotulos: ["Configuração", "Estoque", "#validadoJoaogomes", ".", "Performance", "Solução para lentidão", "Parâmetro \"ALTOVOLCOPIAEST\"", "Desempenho do sistema", "Parâmetro", "otimização parâmetro MERGE"]
---

# Demora no processo de Copia de Estoque

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16257793419671)  MENSAGEM**:

Sem mensagem de erro.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16257805812375) CAUSA:**

Por padrão vai ser executado o comando MERGE (parâmetro desligado) e que em alguns bancos de dados esse comando torna o processo lento. Ao ligar o parâmetro, o sistema deixará de utilizar o MERGE e utilizará as instruções de INSERT e UPDATE (processamento será mais rápido).

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16257805809303)  SOLUÇÃO:**

Ative o parâmetro **"ALTOVOLCOPIAEST"**, caso o mesmo esteja desabilitado.
