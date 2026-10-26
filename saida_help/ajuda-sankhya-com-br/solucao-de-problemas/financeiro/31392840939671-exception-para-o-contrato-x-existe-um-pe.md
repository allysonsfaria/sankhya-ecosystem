---
id: "31392840939671"
titulo: "Exception: Para o contrato X existe um período anterior não faturado. Para faturar esta referência, fature antes a referência anterior faltante ou remova este contrato da grade"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31392840939671-Exception-Para-o-contrato-X-existe-um-per%C3%ADodo-anterior-n%C3%A3o-faturado-Para-faturar-esta-refer%C3%AAncia-fature-antes-a-refer%C3%AAncia-anterior-faltante-ou-remova-este-contrato-da-grade"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T14:33:17Z"
rotulos: ["Configuração", "Faturamento", "Contrato", "Financeiro", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Para faturar esta referência", "fature antes a referência anterior", "remova este contrato da grade", "Para o contrato", "existe um período anterior", "não faturado", "Erro"]
---

# Exception: Para o contrato X existe um período anterior não faturado. Para faturar esta referência, fature antes a referência anterior faltante ou remova este contrato da grade

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/31392831648023) **MENSAGEM:**

Exception: Para o contrato X existe um período anterior não faturado. Para faturar esta referência, fature antes a referência anterior faltante ou remova este contrato da grade.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/31392840920983)SOLUÇÃO:**

Quando o parâmetro **"FATCONSEQ - Faturamento de Contratos Mensais com Referência Sequencial"** estiver habilitado, o sistema impedirá o faturamento de um contrato caso o mês anterior não tenha sido faturado. Nesse caso, uma mensagem de alerta será exibida informando que há um período pendente.

Essa configuração garante que o faturamento siga uma sequência mensal.

Além disso, caso um contrato esteja sendo faturado sem respeitar a sequência de meses, ele será destacado em vermelho na tela **Faturamento de Contratos**, indicando que há um mês anterior sem faturamento.

![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/31392831651863)

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/31392831652375)CAUSA:**

Ocorre quando o parâmetro **"FATCONSEQ - Faturamento de Contratos Mensais com Referência Sequencial"** está habilitado, pois ele exige que o faturamento dos contratos seja realizado de forma contínua, sem a possibilidade de pular meses.
