---
id: "14947767278999"
titulo: "Uso do campo \"Data Pedido de Compra\" na rotina de Planejamento de Produção (MRP I)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/14947767278999-Uso-do-campo-Data-Pedido-de-Compra-na-rotina-de-Planejamento-de-Produ%C3%A7%C3%A3o-MRP-I"
trilha: "Solução de Problemas > Produção"
atualizado_em: "2026-07-22T14:57:44Z"
rotulos: ["Produtos", "Configuração", "Estoque", "Planejamento de Produção", "Defina \"Lead time\" e tempos de atividade", "Configure MPS e tipos de demanda", "Ajuste o campo \"Previsão de Entrega\" no Layout", "MRP I"]
---

# Uso do campo "Data Pedido de Compra" na rotina de Planejamento de Produção (MRP I)

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16610864642199) SITUAÇÃO:**

Para que serve e como usar o campo Data Pedido de Compra?

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16610864645015) SOLUÇÃO:**

Para que este campo funcione corretamente, realize algumas configurações em outras telas.

![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16610844021911) Acesse: Configurações » Cadastros » Produtos » Produtos

Selecione o produto que faz parte do Plano Mestre de Produção, aba **"Medidas e Estoque"**, selecione a sub aba **"Estoque"** e no campo **"Lead time de compra"** (este campo, indica o tempo que o produto leva para ser entregue) informe um valor numérico em dias.

![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/14961956802455)

![Imagem 5: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16610844023191) Acesse: Produção » Cadastros » Processo Produtivo - Nova

Configure o tempo das atividades:  insira o código do processo Processo Produtivo. Acesse o Roteiro, aba **"Geral",** no campo **"Tempo da atividade"** insira o tempo da sua atividade  e no campo **"Unidade de Tempo"**, insira o tempo.

Pode ser feito também pela Composição do Produto: Produção » Cadastros » Composição do Produto, aba **"Tempo de Processamento"**, conforme abaixo:

![Imagem 6: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/14961965163415)

**![Imagem 7: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16610864652055) IMPORTANTE:**

Com esta configuração (Tela **"Composição do Produto"**), este tempo será apenas para o produto selecionado.

![Imagem 8: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16610844030999) Acesse: Produção » Rotinas » Planejamento de Produção (MRP I), realize a configuração através do botão **"Configuração"**.

![Imagem 9: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/14962014394391)

Verifique qual MPS será utilizado, então configure este registro. O importante é verificar se o **"Tipo de demanda"** está como: **"Pedidos Firmes"** e o **"Tipo de período"** está como: **"Previsão de Entrega (Nota)"** ou **"Previsão de Entrega (Itens)".** Esta configuração indica de qual data da nota fiscal o cálculo será feito.

![Imagem 10: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/14961975782423)

**![Imagem 11: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16610864656279) OBSERVAÇÕES:**

**(2)** O pedido de venda precisa ter a previsão de entrega da Nota ou do Item, de acordo com a configuração do  MPS (conforme passo anterior).

**(2)**Caso o campo **"Previsão de Entrega"** não esteja em seu Layout, o mesmo pode ser inserido utilizando a tela: **"Configurador de Layout da Nota"**.

**(2)**Após todas estas configurações realizadas, então é possível ir no Planejamento de Produção e clicar no botão "MRP" para gerar as datas de compra.

**![Imagem 12: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16610864658967) CAUSA:**

Ao clicar no botão de MRP na tela **"Planejamento de Produção (MRP I)"** é gerada a tela **"Necessidade de Materiais"**, que traz uma grid com o campo **"Data Pedido de Compra",** que informa a data indicada para realizar a compra dos materiais, considerando na data tempos de processamento de produção, tamanhos de lote e lead time.

![Imagem 13: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/14961878792855)
