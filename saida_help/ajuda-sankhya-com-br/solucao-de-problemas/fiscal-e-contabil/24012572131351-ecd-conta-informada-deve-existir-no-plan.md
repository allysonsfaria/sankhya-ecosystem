---
id: "24012572131351"
titulo: "ECD - Conta Informada deve existir no plano de contas e ser analítica"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/24012572131351-ECD-Conta-Informada-deve-existir-no-plano-de-contas-e-ser-anal%C3%ADtica"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-24T12:42:19Z"
rotulos: ["Configuração", "ECD", "SPED", "Fiscal", "Sped Fiscal", "Contabilidade", "Financeiro", "Plano de Contas", "Erro"]
---

# ECD - Conta Informada deve existir no plano de contas e ser analítica

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/24012572106263) **MENSAGEM:**

Conta Informada deve existir no plano de contas e ser analítica.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/24012572119959)CAUSA:**

Quando na geração do arquivo ECD há contas do Plano de Contas que não possuem registros de movimentações e saldos referente ao período de geração do ECD.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/24012560284567)SOLUÇÃO:**

Para os registros que estão sendo criticados com o erro "Conta Informada deve existir no plano de contas e ser analítica" podemos realizar algumas análises para solucionar o problema:

![Imagem 4: A primeira opção seria dentro do próprio PVA, onde deve ser selecionado o registro que contém essa crítica. Após…](https://ajuda.sankhya.com.br/hc/article_attachments/24071407564823) A primeira opção seria dentro do próprio PVA, onde deve ser selecionado o registro que contém essa crítica. Após selecionado o erro, o PVA levará para outra tela contendo o erro e o código da conta que está sendo criticada.

![Imagem 5: A primeira opção seria dentro do próprio PVA, onde deve ser selecionado o registro que contém essa crítica. Após…](https://ajuda.sankhya.com.br/hc/article_attachments/24071360851991)

Copiar o código da conta, e dentro da mesma tela selecionar a opção "Plano de Contas", conforme imagem abaixo:

![Imagem 6: Copiar o código da conta, e dentro da mesma tela selecionar a opção "Plano de Contas", conforme imagem abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/24071360854295)

Pesquisar a conta na opção "Plano de Contas", selecionando como pesquisa a opção "Código da conta analítica/grupo de contas." Se a conta pesquisada não for apresentada no PVA, então deve busca-la no Registro que está sendo criticado, nesse exemplo está sendo criticada no Registro I155, então dentro do arquivo gerado deverá buscar por essa conta no registro I050 e I155.

![Imagem 7: Pesquisar a conta na opção "Plano de Contas", selecionando como pesquisa a opção "Código da conta analítica/grupo de…](https://ajuda.sankhya.com.br/hc/article_attachments/24071407573399)

Nesse exemplo realmente a conta não existe no plano de contas no registro I050, e para ela estar corretamente no I155, a mesma deve existir no I050. Caso a conta não seja apresentada no SPED seguir o próximo passo:

![Imagem 8: Nesse exemplo realmente a conta não existe no plano de contas no registro I050, e para ela estar corretamente no I155,…](https://ajuda.sankhya.com.br/hc/article_attachments/24071360860823)

![Imagem 9: Devemos recompor os saldos das contas contábeis com período do ano inteiro "01/01 a 31/12" tela "Preferências da…](https://ajuda.sankhya.com.br/hc/article_attachments/24071360864535) Devemos recompor os saldos das contas contábeis com período do ano inteiro "01/01 a 31/12" tela "Preferências da Empresa(Contabilidade)"

Lembrando de validar as seguintes datas:

![Imagem 10: Lembrando de validar as seguintes datas:](https://ajuda.sankhya.com.br/hc/article_attachments/24071407579159)

 
**Observações importantes:**

Se dentro do período de geração a marcação "Gerar I050 somente para contas com movimento ou com saldo?" estiver habilitada na tela Geração de Arquivo - ECD, e existirem períodos em que as contas não  tiveram movimentos nenhum ou iniciaram sem movimentos e terminaram o período sem movimento, ao importar o ECD no PVA a registro que tiver essa marcação habilitada será criticado.

A geração do I050 se dá para todas as contas que constam no plano de contas da empresa, independente se houve movimentações ou saldos durante o período de geração do ECD. O que impedirá das contas sem movimento não serem criticadas no PVA é a marcação desabilitada. 
No caso da contar possuir apenas um período que contenha um crédito e um débito, e a conta iniciou-se com saldo zero e encerrou com saldo zero, a marcação desabilitada irá fazer com que essas contas não seja levadas ao arquivo.
