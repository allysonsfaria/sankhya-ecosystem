---
id: "44012112565655"
titulo: "Como configurar as maquinetas de cartão?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012112565655-Como-configurar-as-maquinetas-de-cart%C3%A3o"
trilha: "Magis5 > Magis5 ERP"
atualizado_em: "2026-10-05T19:20:09Z"
rotulos: ["sync_hc", "magis5", "magis5_204050497950", "sync_hash_142ca5064663"]
---

# Como configurar as maquinetas de cartão?

## O módulo "Maquinetas de Cartão" é utilizado para o cadastro e gerenciamento das máquinas de cartão de crédito ou débito utilizadas pelo empreendimento.

Antes de cadastrar uma maquineta, é necessário definir a estratégia de trabalho do empreendimento e como os juros serão cobrados. Existem duas opções disponíveis: cobrança por quantidade de parcelas ou por bandeira.

Se a cobrança for baseada na quantidade de parcelas, é necessário especificar as taxas de juros para cada faixa de parcelamento, bem como o limite máximo de parcelas permitido. Dessa forma, o sistema será capaz de calcular automaticamente os valores dos juros de acordo com o número de parcelas escolhido pelo cliente durante uma venda.

Por outro lado, se a cobrança for por bandeira, é necessário informar as taxas de juros associadas a cada bandeira de cartão. Isso permitirá que o **Artemis5** aplique as taxas corretas ao processar as transações de acordo com a bandeira do cartão utilizado.

Ao cadastrar as máquinas de cartão de crédito ou débito no módulo correspondente, o empreendimento terá todas as informações necessárias para realizar as transações de pagamento de forma correta e precisa, garantindo o controle adequado das taxas de juros, limites de parcelamento e demais aspectos relacionados ao uso das maquinetas.

---

Após definir o modelo de cobrança de juros, na barra de menus, clique em: Financeiro → Cadastro - Maquinetas de Cartão:

![Imagem 1: Após definir o modelo de cobrança de juros, na barra de menus, clique em: Financeiro → Cadastro - Maquinetas de Cartão:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/07/image-24-1024x243.png)

No módulo “Maquinetas”, clique em “Nova Maquineta”:

![Imagem 2: No módulo “Maquinetas”, clique em “Nova Maquineta”:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-562-1024x145.png)

**JUROS POR PARCELA**

Para configurar a maquineta considerando o juros por parcela, preencha os passos abaixo:

![Imagem 3: Para configurar a maquineta considerando o juros por parcela, preencha os passos abaixo:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-563-1024x265.png)

- **Número de Série:** Informe o número de série da maquineta (ou apenas o nome, para identificação);

- **Conta:** Informe em qual conta será creditado o valor recebido;

- **Dias p/ Lanç. Débito/Voucher:** Informe em quantos dias será creditado vendas no débito;

- **Dias p/ Lanç. Crédito:** Informe em quantos dias será creditado vendas no crédito;

- **Taxa Débito:** Informe qual a taxa cobrada para transações no débito;

- **ID Externo:** Informe o ID utilizado em outro sistema, caso possua.

Após preencher todas as informações, em “Taxas de Crédito”, clique em (+) para configurar o parcelamento da maquineta, por exemplo:

![Imagem 4: Após preencher todas as informações, em “Taxas de Crédito”, clique em (+) para configurar o parcelamento da maquineta,…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-564-1024x267.png)

Após finalizar as configurações, clique em “Salvar”.

**JUROS POR BANDEIRA:**

Para configurar a maquineta considerando o juros por bandeira, é necessário que esta configuração esteja habilitada nas configurações gerais do empreendimento. Para isso, em: Configurações → Configurações Gerais → Financeiro, selecione "Sim" para "Taxa de Maquineta por Bandeira?" e clique em "Salvar":

![Imagem 5: Para configurar a maquineta considerando o juros por bandeira, é necessário que esta configuração esteja habilitada nas…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/07/image-25-1024x164.png)

Após habilitar a taxa de maquineta por bandeira, volte ao módulo de cadastro de maquinetas e siga os passos abaixo:

![Imagem 6: Após habilitar a taxa de maquineta por bandeira, volte ao módulo de cadastro de maquinetas e siga os passos abaixo:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-565-1024x265.png)

- **Número de Série:** Informe o número de série da maquineta (ou apenas o nome, para identificação);

- **Conta:** Informe em qual conta será creditado o valor recebido;

- **ID Externo:** Informe o ID utilizado em outro sistema, caso possua.

Após preencher todas as informações, em “Bandeira”, clique em (+) para configurar o parcelamento da maquineta, por exemplo:

![Imagem 7: Após preencher todas as informações, em “Bandeira”, clique em (+) para configurar o parcelamento da maquineta, por…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-567-1024x214.png)

Preencha os campos abaixo referente a cada bandeira e suas respectivas parcelas e taxas de juros, por exemplo:

![Imagem 8: Preencha os campos abaixo referente a cada bandeira e suas respectivas parcelas e taxas de juros, por exemplo:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-566-1024x465.png)

Realize este procedimento a cada bandeira. Após finalizar a primeira bandeira preenchida, clique em “Adicionar”:

![Imagem 9: Realize este procedimento a cada bandeira. Após finalizar a primeira bandeira preenchida, clique em “Adicionar”:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-568-1024x467.png)

Ao finalizar todas as parametrizações, segue um exemplo de como ficará:

![Imagem 10: Ao finalizar todas as parametrizações, segue um exemplo de como ficará:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-569-1024x260.png)

Clique em “Salvar” para salvar as configurações realizadas.

[![Universidade Magis5](https://ajuda.sankhya.com.br/hc/article_attachments/44012151556887)](https://download.magis5.com.br/universidade-magis5?utm_source=central_de_ajuda&utm_medium=link&utm_campaign=central_de_ajuda&hsLang=pt-br)
