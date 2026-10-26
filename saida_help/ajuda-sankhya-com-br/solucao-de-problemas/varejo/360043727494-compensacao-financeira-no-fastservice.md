---
id: "360043727494"
titulo: "Compensação financeira no FastService"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043727494-Compensa%C3%A7%C3%A3o-financeira-no-FastService"
trilha: "Solução de Problemas > Varejo"
atualizado_em: "2026-07-22T15:59:39Z"
rotulos: ["Configuração", "Parceiro", "Fast Service", "Movimentação Financeira", "Crédito", "Preferências", "Falha na compensação de crédito", "Configurações de preferências", "Identificação incorreta do parceiro"]
---

# Compensação financeira no FastService

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16363411758487) SITUAÇÃO:**

Ao efetuar o lançamento de um cupom fiscal para um parceiro que possui um crédito, a compensação financeira não ocorre.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16363411761559) SOLUÇÃO:**

![Imagem 3: Acesse a tela "Preferências" (Caminho de acesso: Configurações » Avançado):](https://ajuda.sankhya.com.br/hc/article_attachments/16363434709015) Acesse a tela **"Preferências"** (Caminho de acesso: Configurações » Avançado):

- Parâmetro **"TIPTITCREDCLI-Tipo de título para compensação de Crédito":** informe neste parâmetro um título que foi criado para simbolizar Crédito de Cliente;

- Parâmetro: **"AVISARCREDCLI-Avisar que o cliente possui Crédito?":**ligado

![Imagem 4: Acesse: FastService » Menu » Preferências » Todas as Preferências](https://ajuda.sankhya.com.br/hc/article_attachments/16363411764247) Acesse: FastService  » Menu » Preferências » Todas as Preferências

Aba: **"Miscelânia"**

- Avisar que o cliente possui crédito: marcado
- Tipo de Titulo para compensação de crédito/troca: informe o código do tipo de titulo

![Imagem 5: Acesse: FastService » Menu » Preferências » Todas as Preferências](https://ajuda.sankhya.com.br/hc/article_attachments/16363434715031) Acesse: FastService » Menu » Preferências » Todas as Preferências

Aba: **"Cupom Modelo"**

- Nas preferências do FastService, cadastramos as notas modelo. Nessas, é possível identificar várias informações pertinentes ao processo de venda, compensação e etc;
- Essas configurações são encontradas na aba Cupom Modelo. A atenção que temos que tomar nesse momento é referente ao parceiro.
- Isso se dá visto que nesse processo é identificado o parceiro padrão das vendas (no caso de nota modelo de venda). Caso o parceiro identificado no ato da despesa for o mesmo identificado na nota modelo, a compensação não será questionada. O parceiro identificado na nota modelo é o 'Consumidor final'.

![Imagem 6: Tipo de título identificado na nota de 'Despesa' lançada para a empresa identificando o parceiro receptor desse valor:](https://ajuda.sankhya.com.br/hc/article_attachments/16363434716183) Tipo de título identificado na nota de 'Despesa' lançada para a empresa identificando o parceiro receptor desse valor:

- Por último, temos a preocupação de identificação do tipo de título no ato do lançamento da despesa para o parceiro identificado. Esse lançamento pode ser efetuado através de mais de uma forma. Para exemplificar, vamos mostrar o lançamento de uma movimentação financeira;
- Tomamos o cuidado de identificar o tipo de título de crédito na Despesa para a empresa. Isso se faz necessário para definir os títulos que devem ser compensados. Ou seja, podemos efetuar o lançamento de despesas para a empresa em questão que não serão compensados e, para isso, é só identificar um tipo de título diferente do parâmetro **"TIPTITCREDCLI";**
- Após esse processo, será possível efetuar a compensação de crédito no FastService. É só identificar o parceiro (sendo diferente do parceiro identificado na nota modelo) no ato da venda e a mensagem **'Esse parceiro possui um crédito de R$\_\_,\_\_. Deseja compensar o valor de R$\_\_,\_\_?';**
- Caso o botão 'Sim' seja clicado, a compensação do crédito será efetuada.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16363411774999)CAUSA:**

A compensação de crédito na venda é utilizada quando é identificado uma despesa lançada para a empresa da nota modelo para um parceiro identificado neste ato.
