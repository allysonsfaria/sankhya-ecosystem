---
id: "360044215433"
titulo: "Programa preparado para data a partir de DD/MM/AAAA"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044215433-Programa-preparado-para-data-a-partir-de-DD-MM-AAAA"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T16:00:38Z"
rotulos: ["#RevisadoBraga", "Configuração", "Contas", "Movimentação Financeira", "Financeiro", "Ajuste a data para no máximo 365 dias anteriores à data atual", "Data de saldo bancário deve ser dentro de 1 ano", "Data de saldo é maior que 365 dias da criação da conta", "Erro"]
---

# Programa preparado para data a partir de DD/MM/AAAA

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16199373226391) MENSAGEM:**

Programa preparado para data a partir de DD/MM/AAAA.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16199329253655) SOLUÇÃO:**

Considere o Comportamento da Aplicação, conforme abaixo:

![Imagem 3: A retroação máxima permitida para data de implantação de saldo bancário é 1 ano .](https://ajuda.sankhya.com.br/hc/article_attachments/16199373233175) A retroação máxima permitida para data de implantação de saldo bancário é **1 ano**.

**(1)** **EXEMPLO:**

Dia 28/03/2019 criada Conta Bancária 79, ao tentar implantar um saldo bancário com a data 25/03/2018 é apresentada a mensagem:

![Imagem 4: Dia 28/03/2019 criada Conta Bancária 79, ao tentar implantar um saldo bancário com a data 25/03/2018 é apresentada a…](https://ajuda.sankhya.com.br/hc/article_attachments/12826552847639)

![Imagem 5: Não trata-se de um "erro de sistema" ou uma configuração a ser ajustada. É um comportamento default que enquadra-se nas…](https://ajuda.sankhya.com.br/hc/article_attachments/16199373239319) Não trata-se de um "erro de sistema" ou uma configuração a ser ajustada. É um  comportamento default que enquadra-se nas**melhores práticas**, de forma a impedir inconsistências em fechamentos contábeis/fiscais anuais.

![Imagem 6: Como solução, ajuste a data informada em "Referência p/aceitar lançamentos" para uma data no máximo 365 dias anteriores…](https://ajuda.sankhya.com.br/hc/article_attachments/16199373241111) Como solução, ajuste a data informada em **"Referência p/aceitar lançamentos"** para uma data no **máximo 365 dias anteriores** a data atual.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16199373243543) CAUSA:**

Ocorre quando ao tentar implantar um saldo em conta é informado uma data maior que 365 da data de criação da conta bancaria.
