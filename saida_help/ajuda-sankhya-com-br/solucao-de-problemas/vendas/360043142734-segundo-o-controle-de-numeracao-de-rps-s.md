---
id: "360043142734"
titulo: "Segundo o controle de numeração de RPS's da prefeitura, o próximo RPS a ser enviado ou inutilizado é o número XXXXX"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043142734-Segundo-o-controle-de-numera%C3%A7%C3%A3o-de-RPS-s-da-prefeitura-o-pr%C3%B3ximo-RPS-a-ser-enviado-ou-inutilizado-%C3%A9-o-n%C3%BAmero-XXXXX"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:04:11Z"
rotulos: ["#revisadohugo", "Configuração", "TOP", "CORE_E00551", "Prefeituras", "NFS-e", "RPS a ser enviado ou inutilizado é o número XXXXX", "Erro ao emitir NFS-e com mensagem", "Atualize \"Último Código\" em \"Controle de Numeração\" e reemita a NFS-e", "Erro"]
---

# Segundo o controle de numeração de RPS's da prefeitura, o próximo RPS a ser enviado ou inutilizado é o número XXXXX

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16145077944087) MENSAGEM:**

[CORE\_E00551] Segundo o controle de numeração de RPS's da prefeitura, o próximo RPS a ser enviado ou inutilizado é o número XXXXX.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16145077948055) SITUAÇÃO:**

Ao tentar emitir uma NFS-e, ocorre a seguinte mensagem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16145077949719) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 4: Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/article_attachments/16145070458391) Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP

- Botão: **"Outras Opções"** » **"Controle de Numeração"**.
- Selecione a respectiva linha que corresponde a Empresa, Tipo de Numeração e série.
- No campo **"Último Código":** preencha com o código, correspondente ao anunciado na mensagem

![Imagem 5: No campo "Último Código": preencha com o código, correspondente ao anunciado na mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/14633967130519)

![Imagem 6: No campo "Último Código": preencha com o código, correspondente ao anunciado na mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/12147803812759)

![Imagem 7: Salve o registro e transmita novamente a NFS-e. É necessário lançar uma nova NFS-e para que a mesma assuma a nova…](https://ajuda.sankhya.com.br/hc/article_attachments/16145070459927) Salve o registro e transmita novamente a NFS-e.
É necessário lançar uma nova NFS-e para que a mesma assuma a nova numeração configurada na TOP. Com a ressalva que, caso tenha uma NFS-e lançada no sistema para a Empresa/Série, mesmo que rejeitada e/ou cancelada, o sistema vai pular a numeração.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16145077957527) CAUSA:**

Ocorre quando uma NFS-e antes de ser transmitida para prefeitura é excluída do sistema, gerando uma numeração, neste caso se faz necessário ajustar o controle de numeração da TOP.
