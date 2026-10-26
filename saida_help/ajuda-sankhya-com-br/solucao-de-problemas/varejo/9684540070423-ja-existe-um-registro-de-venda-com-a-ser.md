---
id: "9684540070423"
titulo: "Já existe um registro de venda com a SERIENOTA X e o NUMNOTA X na TGFCAB"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9684540070423-J%C3%A1-existe-um-registro-de-venda-com-a-SERIENOTA-X-e-o-NUMNOTA-X-na-TGFCAB"
trilha: "Solução de Problemas > Varejo"
atualizado_em: "2026-07-22T15:06:27Z"
rotulos: ["Configuração", "TOP", "Financeiro", "CHK_E00011", "Numeração de nota duplicada", "Verificar série e numeração na TGFCAB", "Configurar \"Último código\" corretamente", "Erro"]
---

# Já existe um registro de venda com a SERIENOTA X e o NUMNOTA X na TGFCAB

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16778137475735) MENSAGEM:**

[CHK\_E00011]: Já existe um registro de venda com a SERIENOTA X e o NUMNOTA X na TGFCAB.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16778151637911) SITUAÇÃO:**

Ao tentar receber algumas vendas realizadas no Checkout a mensagem é apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16778137482647) SOLUÇÃO:**

![Imagem 4: Verifique se já existem notas com a mesma Série e numeração na TGFCAB.](https://ajuda.sankhya.com.br/hc/article_attachments/16778151643927) Verifique se já existem notas com a mesma Série e numeração na TGFCAB.

Confira no cadastro do **"Tipo de operação-TOP"** (Caminho de acesso: Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP) o **"Controle de numeração"** que foi configurado para a Empresa e Série em questão.

![Imagem 5: Confira no cadastro do " Tipo de operação-TOP" (Caminho de acesso: Financeiro » Arquivos » Cadastros » Tipos de…](https://ajuda.sankhya.com.br/hc/article_attachments/16778137485591)

![Imagem 6: Confira no cadastro do " Tipo de operação-TOP" (Caminho de acesso: Financeiro » Arquivos » Cadastros » Tipos de…](https://ajuda.sankhya.com.br/hc/article_attachments/9684414306711)

![Imagem 7: No campo " Último código " deverá um "Valor" para que seja identificado que a partir do próximo lançamento aquela…](https://ajuda.sankhya.com.br/hc/article_attachments/16778151648919) No campo "**Último código**" deverá um **"Valor"** para que seja identificado que a partir do próximo lançamento aquela determinada numeração e com isso acabou gerando a duplicidade.

**Exemplo:**

Se a última nota gerada com a Série 16 na Empresa 3 no Sankhya /w foi a "50", deveria ter sido configurado no checkout a última numeração que foi utilizada para que o sistema seguisse a sequência corretamente. Abaixo um Print de onde deveria ser configurado essa numeração.

![Imagem 8: Se a última nota gerada com a Série 16 na Empresa 3 no Sankhya /w foi a "50", deveria ter sido configurado no checkout…](https://ajuda.sankhya.com.br/hc/article_attachments/16778151650455)

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16778151652119)CAUSA:**

Numeração repetida no Checkout.
