---
id: "35267365074199"
titulo: "CORE_E01695 - Não é possível excluir este servidor de impressão, pois ele ainda possui X trabalho(s) de impressão"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35267365074199-CORE-E01695-N%C3%A3o-%C3%A9-poss%C3%ADvel-excluir-este-servidor-de-impress%C3%A3o-pois-ele-ainda-possui-X-trabalho-s-de-impress%C3%A3o"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:25:45Z"
rotulos: ["Configuração", "Impressão", "não apagar", "Erro", "trabalhos de impressão", "E01695", "excluir servidor impressão", "impressão exclusão", "trabalho(s) de impressão", "Não é possível excluir este servidor de impressão", "pois ele ainda possui X trabalho(s) de impressão", "CORE_E01695"]
---

# CORE_E01695 - Não é possível excluir este servidor de impressão, pois ele ainda possui X trabalho(s) de impressão

**MENSAGEM**

[CORE\_E01695] Não é possível excluir este servidor de impressão, pois ele ainda possui X trabalho(s) de impressão.

**SITUAÇÃO**

Na tela **"Servidores de Impressão"** (Configurações » Avançado » Impressão » Servidores de Impressão), ao tentar excluir um servidor de impressão, o sistema apresenta a mensagem de erro informando que ainda existem trabalhos de impressão pendentes vinculados ao servidor.

**SOLUÇÃO**

**(1)** Acesse a tela **"Trabalhos de Impressão"** (Configurações » Avançado » Impressão » Trabalhos de Impressão).

**(2)** Localize os **trabalhos pendentes** vinculados ao servidor que deseja excluir.

**(3)** Aguarde até que todas as **impressões pendentes** sejam concluídas.

**(4)** Caso a impressora configurada esteja **indisponível**, utilize uma impressora substituta para finalizar o trabalho de impressão.

**(5)** Após não haver mais impressões pendentes, retorne à tela **"Servidores de Impressão"** e realize a exclusão do servidor.

**CAUSA**

Este erro ocorre quando se tenta excluir um **servidor de impressão** que ainda possui trabalhos de impressão associados a ele. O sistema impede a exclusão para manter a **integridade referencial dos dados** e evitar que trabalhos de impressão fiquem órfãos no sistema.
