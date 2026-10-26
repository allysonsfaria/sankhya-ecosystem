---
id: "31879921856663"
titulo: "Erro: O comando SELECT está em formato inválido - Metas Gerenciais"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31879921856663-Erro-O-comando-SELECT-est%C3%A1-em-formato-inv%C3%A1lido-Metas-Gerenciais"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:32:18Z"
rotulos: ["SQL", "Configuração", "Relatórios Gerenciais", "O comando SELECT", "Metas Gerenciais", "está em formato inválido", "Erro"]
---

# Erro: O comando SELECT está em formato inválido - Metas Gerenciais

**(1)** Ao validar a sintaxe das querys na tela Metas Gerenciais, é apresentado o erro "**O comando SELECT está em formato inválido.**". Consequentemente, ao ser executado no horário agendado também apresenta o mesmo erro no Serverlog.

![Imagem 1: (1) Ao validar a sintaxe das querys na tela Metas Gerenciais, é apresentado o erro " O comando SELECT está em formato…](https://ajuda.sankhya.com.br/hc/article_attachments/31879936918807)

**(2)** O erro de validação do SQL ocorre, pois por padrão não é permitido execução de query que não comecem com **SELECT** ou **WITH**. Este comportamento é nativo do sistema e não tem sido alterado desde a versão 4.20.

**(2)**Essa trava existe pois caso contrário pode abrir brechas para execuções inadvertidas de comandos como INSERT/UPDATE por exemplo. O recomendado é redefinir a query das metas de modo que seja aceita pela validação (iniciando com SELECT ou WITH).
