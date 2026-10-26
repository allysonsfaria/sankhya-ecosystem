---
id: "360043715134"
titulo: "Data da baixa fora do período permitido. A data limite para retroação é xx/xx/xxxx"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043715134-Data-da-baixa-fora-do-per%C3%ADodo-permitido-A-data-limite-para-retroa%C3%A7%C3%A3o-%C3%A9-xx-xx-xxxx"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T16:00:25Z"
rotulos: ["#RevisadoGui", "Configuração", "Movimentação Financeira", "Financeiro", "CORE_E02191", "CORE_E02191: Baixa Retroativa", "Ajuste nas Configurações", "Permissão de Retroação", "Erro"]
---

# Data da baixa fora do período permitido. A data limite para retroação é xx/xx/xxxx

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/17293222655383) MENSAGEM:**

[CORE\_E02191]: Data da baixa fora do período permitido. A data limite para retroação é xx/xx/xxxx.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17293222663319) SOLUÇÃO:**

A validação ocorre pois foi definido para o usuário responsável pela baixa do respectivo título uma permissão para dias de retroação da baixa inferior ao desejado nessa operação.

Caso seja avaliado que o título realmente precise ser baixado de forma retroativa por esse usuário, é necessário que o ajuste abaixo seja realizado:

![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17293222666391) Acesse: a tela **"Usuários"** (Caminho de acesso: Configurações >> Controle de Acesso >> Usuários)

Botão: **Outras Opções >> Configurações Usuário**

Campo **"Dias para retroação da baixa":** altere o valor deste campo

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17293222672791) CAUSA:**

Ocorre quando um usuário tenta efetuar a baixa de um título com data retroativa maior que o permitido em suas configurações, sendo necessário aumentar o valor neste campo.
