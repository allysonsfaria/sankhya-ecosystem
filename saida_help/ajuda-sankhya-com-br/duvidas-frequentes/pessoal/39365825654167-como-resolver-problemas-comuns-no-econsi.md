---
id: "39365825654167"
titulo: "Como resolver problemas comuns no eConsignado?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39365825654167-Como-resolver-problemas-comuns-no-eConsignado"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-07-29T13:29:08Z"
rotulos: ["Configuração", "Eventos", "Crédito", "Folha de Pagamento", "eConsignado", "Artigo criado KCS", "Sankhya RH - KCS"]
---

# Como resolver problemas comuns no eConsignado?

O **Crédito do Trabalhador (eConsignado)** é uma funcionalidade que permite o desconto automático de parcelas de empréstimos consignados diretamente na folha de pagamento. Durante sua utilização, podem ocorrer situações que impedem o correto cálculo ou desconto das parcelas. Este artigo apresenta as principais dificuldades encontradas e suas respectivas soluções.

### Parcela não descontada na folha mensal

Quando a parcela do eConsignado não é descontada na folha, mesmo havendo lançamento no movimento, verifique se a situação está relacionada à margem consignável ou à configuração dos eventos utilizados no cálculo.

O sistema calcula automaticamente a base de margem, correspondente a 35% da remuneração do trabalhador. Caso os descontos já existentes ultrapassem esse limite, a parcela do eConsignado poderá não ser descontada integralmente.

Para que o cálculo seja realizado corretamente, é necessário que os eventos que compõem a remuneração estejam configurados com a base de cálculo **“BASE MARGEM CRÉD. TRABALHADOR”**.

Para validar essa configuração:

**(1)**Acesse a tela **“Eventos”** (Pessoal > Cadastros > Eventos);

**(2)**Selecione o evento desejado;

**(3)**Acesse a aba **“Bases de Cálculo”**;

**(4)**Verifique se a base **“BASE MARGEM CRÉD. TRABALHADOR”** está cadastrada para o evento.

![Imagem 1: (4) Verifique se a base “BASE MARGEM CRÉD. TRABALHADOR” está cadastrada para o evento.](https://ajuda.sankhya.com.br/hc/article_attachments/40796438506007)

Caso a **BASE MARGEM CRÉD. TRABALHADOR** não esteja cadastrado basta incluir conforme abaixo:

[GIF animado: Imagem 2: Caso a BASE MARGEM CRÉD. TRABALHADOR não esteja cadastrado basta incluir conforme abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/40796408876695)

### Desconto não aparece no cálculo de férias

Para que o **provisionamento do eConsignado** seja calculado automaticamente nas férias, é necessário que a parcela do mês de férias já esteja lançada como **movimento mensal** na tela **"Lançamento de Movimentos"** (Pessoal+ >> Rotinas Folha >> Lançamento de Movimentos).

O sistema identifica automaticamente que o colaborador está em férias e calcula o **valor proporcional** do desconto. Posteriormente, o valor é apresentado na folha mensal como demonstrativo.

### Desconto não aparece no cálculo de rescisão

Quando o desconto do eConsignado **não aparece na rescisão**, verifique se a **base de cálculo** está com valor positivo. A base é composta pela remuneração do trabalhador e garante que o desconto não ultrapasse **35% desse valor**.

Se a base estiver **negativa** devido a outros descontos (como INSS, por exemplo), não haverá remuneração disponível para o desconto da parcela do eConsignado. Nesse caso, oriente o colaborador a **buscar a instituição financeira responsável** para regularização da parcela, pois não havia margem suficiente para o desconto.

### Parcela não descontada não aparece no holerite

Quando a parcela do eConsignado não é descontada por falta de margem, o valor deve ser apresentado como demonstrativo no holerite. Caso essa informação não esteja sendo exibida, verifique a configuração do parâmetro “Relatório de Holerite” **(FPRELATHOLERITE)** na tela “Preferências” (Configurações » Avançado » Preferências).

Atualmente, os relatórios de holerite são gerados pelo padrão do sistema. Portanto, se existir algum relatório customizado vinculado ao parâmetro **FPRELATHOLERITE**, recomenda-se deixar o parâmetro com o campo 'Inteiro' sem preenchimento ou com valor zerado.

![Imagem 3: Atualmente, os relatórios de holerite são gerados pelo padrão do sistema. Portanto, se existir algum relatório…](https://ajuda.sankhya.com.br/hc/article_attachments/40796438508695)

Após realizar esse ajuste, a informação da parcela não descontada passará a ser apresentada corretamente no holerite, conforme o modelo abaixo:

![Imagem 4: Após realizar esse ajuste, a informação da parcela não descontada passará a ser apresentada corretamente no holerite,…](https://ajuda.sankhya.com.br/hc/article_attachments/40796438509207)
