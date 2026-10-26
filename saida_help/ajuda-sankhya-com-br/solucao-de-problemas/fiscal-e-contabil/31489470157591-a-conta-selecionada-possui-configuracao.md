---
id: "31489470157591"
titulo: "A conta selecionada possui configuração inválida"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31489470157591-A-conta-selecionada-possui-configura%C3%A7%C3%A3o-inv%C3%A1lida"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:32:58Z"
rotulos: ["Configuração", "Contas", "Projeto", "Centro de Resultado", "Financeiro", "CTB_E00173", "A conta selecionada possui configuração inválida"]
---

# A conta selecionada possui configuração inválida

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/31959593483799) MENSAGEM:**

[CTB\_E00173] A conta selecionada possui configuração inválida

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/31959579470231) SITUAÇÃO:**

Ao realizar o processo de [Zeramento de Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116453-Zeramento-de-Contas) é possível se deparar com esse erro.

(1)**Primeiramente, confira  a regra de negócio que nos leva a este cenário:**

![Imagem 3: O sistema realiza a validação das contas informadas na tela de " Zeramento de contas" , nos campos:](https://ajuda.sankhya.com.br/hc/article_attachments/31959579479959) O sistema realiza a validação das contas informadas na tela de "**Zeramento de contas"**, nos campos:

- Conta prejuízo
- Conta lucro

![Imagem 4: Conta lucro](https://ajuda.sankhya.com.br/hc/article_attachments/31489860619287)

![Imagem 5: Em seguida, o sistema faz outra validação. Que consiste em verificar, na tela "Plano de contas", os seguintes campos…](https://ajuda.sankhya.com.br/hc/article_attachments/31959593501719) Em seguida, o sistema faz outra validação. Que consiste em verificar, na tela **"Plano de contas",** os seguintes campos destas contas contábeis identificadas no passo 1:

- Centro de Resultado obrigatório
- Projeto obrigatório

![Imagem 6: Projeto obrigatório](https://ajuda.sankhya.com.br/hc/article_attachments/31489860622999)

**Se estes campos estiverem com as marcações acionadas,** o sistema apresentará a mensagem de alerta citada acima, porque as contas de Resultado do Exercício não podem obrigar estas informações.

**![Imagem 7: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/31489907650711)SOLUÇÃO:**

**Assim, se faz necessário desativar tais marcações na tela de Plano de Contas.**
