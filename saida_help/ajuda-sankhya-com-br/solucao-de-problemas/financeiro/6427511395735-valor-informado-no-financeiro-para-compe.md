---
id: "6427511395735"
titulo: "Valor informado no financeiro para compensação maior que o crédito do cliente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/6427511395735-Valor-informado-no-financeiro-para-compensa%C3%A7%C3%A3o-maior-que-o-cr%C3%A9dito-do-cliente"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-30T19:37:47Z"
rotulos: ["Configuração", "TIPTITCREDCLI", "Crédito", "Financeiro", "CORE_E03745", "Valor no financeiro > crédito do cliente", "Ajustar tipo de título em TIPTITCREDCLI; confira configurações", "Parâmetro TIPTITCREDCLI = 0 e título na nota também = 0", "Erro"]
---

# Valor informado no financeiro para compensação maior que o crédito do cliente

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16461380501015)  MENSAGEM:**

[CORE\_E03745]  Valor informado no financeiro para compensação maior que o crédito do cliente.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16461380503063) SOLUÇÃO:**

Para a resolução do erro, o tipo de título informado no parâmetro **"TIPTITCREDCLI"** não pode ser o mesmo da nota e ele é padrão zero. Informando um tipo de título dentro do financeiro da nota ao confirmar o lançamento, o sistema apresenta a mensagem de compensação de crédito, sendo possível realizar a compensação corretamente. 
**Dica:** o ideal é que seja configurado um tipo de titulo no parâmetro TIPTITCREDCLI pra evitar que o erro ocorra novamente.

Segue mais detalhes das configurações e do funcionamento da rotina no seguinte artigo:
[Compensação de Crédito ou Débito em Compra ou Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601914-Compensa%C3%A7%C3%A3o-de-Cr%C3%A9dito-ou-D%C3%A9bito-em-Compra-ou-Venda)

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16461380505111)CAUSA:**

Quando o parâmetro TIPTITCREDCLI  = 0 e no financeiro da nota também estiver com o tipo de título = 0, o sistema não executa a compensação de crédito no lançamento.
