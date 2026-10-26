---
id: "9291198908183"
titulo: "O Tamanho do Registro xxxxxxxx, é diferente do especificado para o arquivo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9291198908183-O-Tamanho-do-Registro-xxxxxxxx-%C3%A9-diferente-do-especificado-para-o-arquivo"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T15:09:08Z"
rotulos: ["Configuração", "Layout", "Financeiro", "CORE_E00732", "Tamanho do registro incorreto", "Verifique e ajuste conforme manual bancário", "Layout não corresponde ao tamanho esperado", "Erro", "EDI Bancário"]
---

# O Tamanho do Registro xxxxxxxx, é diferente do especificado para o arquivo

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16699251187863) MENSAGEM:**

[CORE\_E00732]: O Tamanho do Registro xxxxxxxx, é diferente do especificado para o arquivo.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16699298321431) SITUAÇÃO:**

Ao tentar gerar uma remessa a mensagem é apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16699251201687)SOLUÇÃO:**

![Imagem 4: Acesse o layout selecionado na tela "Configuração Arquivo de Remessa" (Caminho de acesso: Financeiro » EDI Bancário »…](https://ajuda.sankhya.com.br/hc/article_attachments/16699251207063) Acesse o layout selecionado na tela **"Configuração Arquivo de Remessa"** (Caminho de acesso: Financeiro » EDI Bancário » Configuração Arquivo de Remessa), confira o campo **"Tamanho"** e compare com o Tamanho atual do registro que é apresentado ao lado conforme imagem abaixo:

![Imagem 5: Acesse o layout selecionado na tela "Configuração Arquivo de Remessa" (Caminho de acesso: Financeiro » EDI Bancário »…](https://ajuda.sankhya.com.br/hc/article_attachments/16699298333463)

![Imagem 6: Identifique o registro que está com o tamanho incorreto, poderá ser no detalhe, header, ou trailer de acordo com o…](https://ajuda.sankhya.com.br/hc/article_attachments/16699298339607) Identifique o registro que está com o tamanho incorreto, poderá ser no detalhe, header, ou trailer de acordo com o manual do banco. Veja:

![Imagem 7: Identifique o registro que está com o tamanho incorreto, poderá ser no detalhe, header, ou trailer de acordo com o…](https://ajuda.sankhya.com.br/hc/article_attachments/16699251218583)

![Imagem 8: Identifique o registro que está com o tamanho incorreto, poderá ser no detalhe, header, ou trailer de acordo com o…](https://ajuda.sankhya.com.br/hc/article_attachments/16699251233175)

![Imagem 9: O Tamanho atual do registro precisa ser igual ao campo Tamanho, que seguirá a definição do manual do banco. Caso…](https://ajuda.sankhya.com.br/hc/article_attachments/16699251236247) O Tamanho atual do registro precisa ser igual ao campo Tamanho, que seguirá a definição do manual do banco. Caso **'Tamanho atual do registro'** esteja diferente, identifique nesse registro qual campo está com tamanho incompatível ao definido para o mesmo no manual do banco e redefina seu **'Tamanho'** no registro identificado, podendo ser header, detalhe ou trailer.

**![Imagem 10: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16699298349335) CAUSA:**

Ocorre quando o layout está com o tamanho diferente do manual do banco.
