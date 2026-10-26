---
id: "9783634198551"
titulo: "Parâmetro SERVDIRMOD não informado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9783634198551-Par%C3%A2metro-SERVDIRMOD-n%C3%A3o-informado"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:06:10Z"
rotulos: ["Configuração", "NF-e", "Movimentação Financeira", "Preferências", "CORE_E02120", "Título: Erro ao Confirmar NF-e: Parâmetro SERVDIRMOD Não Informado", "Erro"]
---

# Parâmetro SERVDIRMOD não informado

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19552122404375) MENSAGEM:**

[CORE\_E02120] Parâmetro SERVDIRMOD não informado.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19552122413207) SITUAÇÃO:**

Ao confirmar uma NF-e a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19552122418071) CAUSA:**

Ocorre quando o modelo não existe no caminho informado no parâmetro **SERVDIRMOD**-Pasta de modelos para impressão.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19552160215959) SOLUÇÃO:**

Acesse a tela **Preferências** (Caminho de acesso à tela: Configurações » Avançado » Preferências) e verifique o caminho informado no parâmetro '**SERVDIRMOD**-Pasta de modelos para impressão'.

![Imagem 5: Acesse a tela Preferências (Caminho de acesso à tela: Configurações » Avançado » Preferências) e verifique o caminho…](https://ajuda.sankhya.com.br/hc/article_attachments/19552122428567)

Esse parâmetro é utilizado na impressão de recibos na baixa de títulos na tela de Movimentação Financeira. O usuário coloca o modelo do recibo no servidor e informa o caminho no parâmetro, por exemplo, o parâmetro está configurado da seguinte forma: /home/mgeweb/modelos/, nesta pasta do servidor se encontra o modelo utilizado para impressão do recibo.

Portanto, se acessar esse caminho o modelo precisa de fato existir.
