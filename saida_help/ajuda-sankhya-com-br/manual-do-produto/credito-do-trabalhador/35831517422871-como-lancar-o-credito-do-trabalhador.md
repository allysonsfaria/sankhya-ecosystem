---
id: "35831517422871"
titulo: "Como lançar o Crédito do Trabalhador"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35831517422871-Como-lan%C3%A7ar-o-Cr%C3%A9dito-do-Trabalhador"
trilha: "Manual do Produto > Pessoas+ > Crédito do Trabalhador"
atualizado_em: "2026-10-02T15:52:39Z"
rotulos: ["eSocial", "Folha de Pagamento", "Lançamento de Movimento", "Configuração Funcionários", "eConsignado", "Crédito do trabalhador (eConsignado)", "Pessoal+", "Crédito do Trabalhador", "Rubrica 9253"]
---

# Como lançar o Crédito do Trabalhador

No Pessoal+, a funcionalidade do Crédito do trabalhador (**eConsignado**) permite que o departamento pessoal registre esses empréstimos de forma estruturada, garantindo que os descontos sejam aplicados corretamente na folha de pagamento e enviados ao eSocial conforme as exigências legais.

Acesse os links abaixo para conhecer as funcionalidades desta rotina.

| [Pré-requisitos para lançamento do eConsignado](https://ajuda.sankhya.com.br/hc/pt-br/articles/35831517422871-Como-lan%C3%A7ar-o-Cr%C3%A9dito-do-Trabalhador#h_01HA4XHVW56P5CT9E03RHTNNV1) |
| --- |
| [Eventos do crédito do trabalhador](https://ajuda.sankhya.com.br/hc/pt-br/articles/35831517422871-Como-lan%C3%A7ar-o-Cr%C3%A9dito-do-Trabalhador#01JX37GRQ3Y6WF8P2WB55ZY7YN) |
| [Como lançar o empréstimo eConsignado](https://ajuda.sankhya.com.br/hc/pt-br/articles/35831517422871-Como-lan%C3%A7ar-o-Cr%C3%A9dito-do-Trabalhador#01JX37KE0B6ZM0YFPY0W7A0HH3) |
| [Como calcular a folha com o desconto do eConsignado](https://ajuda.sankhya.com.br/hc/pt-br/articles/35831517422871-Como-lan%C3%A7ar-o-Cr%C3%A9dito-do-Trabalhador#h_01K88Q6X5N96JJE6JB9VH470BQ) |
| [Modelo de Holerite para o eConsignado](https://ajuda.sankhya.com.br/hc/pt-br/articles/35831517422871-Como-lan%C3%A7ar-o-Cr%C3%A9dito-do-Trabalhador#h_01K88QMHC4P1Q2WRX5XXP41SMT) |
| [Envio da folha com o eConsignado para o eSocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/35831517422871-Como-lan%C3%A7ar-o-Cr%C3%A9dito-do-Trabalhador#h_01K88QC05E6H9YS8G26AW1ZYQ9) |
| [Reprocessamento do Crédito do Trabalhador](https://ajuda.sankhya.com.br/hc/pt-br/articles/36386300103063) |

## Pré-requisitos para lançamento do eConsignado

Antes de registrar o empréstimo consignado no sistema, certifique-se de que o colaborador está cadastrado corretamente, com o **Código de Categoria para o eSocial** igual a **101** ou **104** ou **721**, na aba [Admissão](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639-Configura%C3%A7%C3%A3o-Funcion%C3%A1rios#admisso), seção **Regime Trabalhista** do cadastro do funcionário.

Além disso, utilize os **eventos e fórmulas** padrão Sankhya que, já estão disponíveis para atualização.

**Diferença entre Eventos Padrão Sankhya e Eventos Personalizados**

**Eventos padrão** são identificados pelo ícone específico de um cadeado fechado e têm sua criação, atualização e exclusão sob responsabilidade da Sankhya.

![Imagem 1: Eventos padrão são identificados pelo ícone específico de um cadeado fechado e têm sua criação, atualização e exclusão…](https://ajuda.sankhya.com.br/hc/article_attachments/35831517358743)

Já os **eventos personalizados** não apresentam esse ícone e sua gestão é de inteira responsabilidade do cliente, incluindo alterações de parâmetros ou exclusão quando necessário.

![Imagem 2: Já os eventos personalizados não apresentam esse ícone e sua gestão é de inteira responsabilidade do cliente, incluindo…](https://ajuda.sankhya.com.br/hc/article_attachments/35831517360279)

Importante lembrar que o sistema precisa estar obrigatoriamente na versão 5.30.4 em diante para a atualização dos eventos e fórmulas.

## Eventos do crédito do trabalhador

Os eventos padrão Sankhya para serem utilizados no crédito do trabalhador nas folhas Mensal e Rescisão são:

**(2)** **Evento Desconto Crédito Trabalhador (desconto efetivo da parcela)**

![Imagem 3: (2) Evento Desconto Crédito Trabalhador (desconto efetivo da parcela)](https://ajuda.sankhya.com.br/hc/article_attachments/35831501379607)

Característica: **DESCCREDTRABALHADOR**

O evento será responsável por trazer o valor do desconto do crédito do trabalhador que será realizado na folha, considerando a margem consignável. Ou seja, este evento é o **desconto efetivo da parcela**.

| **⚠️** **Atenção**  Como **o evento utiliza uma fórmula que calcula o desconto com base na margem consignável, é imprescindível que o campo Unidade esteja configurado como Quantidade**. Caso contrário, a fórmula será desconsiderada. Mesmo com a Unidade parametrizada como Quantidade, o valor do desconto deverá ser informado no campo Valor durante o lançamento do movimento. |
| --- |

**(2)** **Evento Crédito do Trabalhador**

![Imagem 4: (2) Evento Crédito do Trabalhador](https://ajuda.sankhya.com.br/hc/article_attachments/35831517364375)

Característica: **CREDTRABALHADOR**

Esse evento é responsável por retornar o **valor exato da parcela do crédito do trabalhador sem considerar a margem consignável**, ou seja, o montante que deveria ser descontado. O valor presente nesse evento é o mesmo lançado no sistema através da comunicação feita pelo governo ao empregador.

**(2)** **Evento Parcela Não Descontada Crédito do Trabalhador**

![Imagem 5: (2) Evento Parcela Não Descontada Crédito do Trabalhador](https://ajuda.sankhya.com.br/hc/article_attachments/35831517365655)

Característica: **PARCCREDNAODESC**

O evento é responsável por retornar o **valor não descontado do trabalhador quando não há margem consignável suficiente para quitação total da parcela.** Quando o evento não for listado no cálculo, significa que o trabalhador possui margem consignável para o desconto total da parcela.

**(2)** **Base Margem Crédito do Trabalhador**

![Imagem 6: (2) Base Margem Crédito do Trabalhador](https://ajuda.sankhya.com.br/hc/article_attachments/35831517367319)

Característica: **BASEMARGEMCREDTRAB**

É o evento base de cálculo para a realização do cálculo da margem consignável de 35%. Ele é utilizado para verificar o valor que será descontado da parcela.

Para o provisionamento do crédito do trabalhador **nas férias**, será realizado um desconto na folha de férias de modo a garantir que o trabalhador terá saldo suficiente na folha mensal para o pagamento da parcela. Dessa forma, no pagamento da folha mensal, esse valor provisionado será ressarcido e descontado novamente com o valor da parcela efetiva.

**Importante:** o evento **Base Margem Crédito do Trabalhador** é fundamental para que o sistema calcule corretamente o desconto das parcelas do empréstimo eConsignado. Quando esse evento não está corretamente vinculado aos eventos utilizados no cálculo da remuneração disponível, o valor da parcela pode deixar de ser descontado. Por isso, sempre que o evento **Desconto Crédito Trabalhador** (identificado como **DESCCREDTRABALHADOR**) não aparecer no cálculo da folha mensal ou no cálculo da folha de rescisão, é necessário verificar se todos os eventos que compõem a remuneração disponível estão devidamente vinculados ao evento de base.

**Eventos Padrão Sankhya** já são automaticamente vinculados à base de cálculo.

No entanto, **eventos personalizados** — criados para atender situações específicas de cada empresa — precisam ser vinculados manualmente pelo cliente.

#### Provisão nas férias

**(2)** **Provisão Desconto Crédito do Trabalhador**

![Imagem 7: (2) Provisão Desconto Crédito do Trabalhador](https://ajuda.sankhya.com.br/hc/article_attachments/35831517372055)

Característica: **PROVCREDTRABFERIAS**

Esse evento é responsável por provisionar o desconto do crédito do trabalhador na folha de férias.

**(2)** **Ressarcimento Crédito do Trabalhador Férias**

![Imagem 8: (2) Ressarcimento Crédito do Trabalhador Férias](https://ajuda.sankhya.com.br/hc/article_attachments/35831501386775)

Característica: **RESSARCPROVCREDTRAB**

O evento é responsável por ressarcir a provisão do desconto do crédito do trabalhador feito na folha de férias.

#### Provisão no adiantamento

**A partir da versão 5.36**, será possível realizar o provisionamento do crédito do trabalhador no adiantamento de salário, também com o intuito de garantir que haja saldo suficiente na folha mensal para pagamento da parcela. No adiantamento, o evento de provisão será descontado e posteriormente ressarcido na folha mensal, onde ocorrerá o desconto efetivo da parcela.

**(2)** **Provisão de desconto no adiantamento**

![Imagem 9: (2) Provisão de desconto no adiantamento](https://ajuda.sankhya.com.br/hc/article_attachments/35831501389975)

Característica: **PROVDESCCREDTRABADTO**

Esse evento é responsável por provisionar o desconto do crédito do trabalhador na folha de adiantamento salarial.

**(2)** **Ressarcimento do crédito do trabalhador no adiantamento**

![Imagem 10: (2) Ressarcimento do crédito do trabalhador no adiantamento](https://ajuda.sankhya.com.br/hc/article_attachments/35831517376151)

Característica: **RESSDESCCREDTRABADTO**

O evento é responsável por ressarcir a provisão do desconto do crédito do trabalhador feito na folha de adiantamento

**Informações adicionais acerca da natureza da rubrica e código para FGTS**

Segundo o [Manual de Orientação do eSocialL – Versão S-1.3](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-3-consolidada-ate-a-no-s-1-3-03-2025.pdf), o recolhimento das parcelas descontadas do eConsignado será realizado por meio da guia do **FGTS Digital**. Para isso, a empresa deve registrar o desconto no eSocial utilizando os eventos **S-1200, S-2299 ou S-2399**, conforme o caso, em uma rubrica com **natureza 9253**. Dessa forma, o valor descontado será incluído no evento **S-5003** e integrado à guia de recolhimento do FGTS Digital.

Portanto, na aba **eSocial**, os campos, **Incidência p/ Previdencia**, **FGTS** e **Incidência p/ IRRF** estão preenchidos com os códigos **00**, **31** e **09**, respectivamente.

![Imagem 11: Portanto, na aba eSocial , os campos, Incidência p/ Previdencia , FGTS e Incidência p/ IRRF estão preenchidos com os…](https://ajuda.sankhya.com.br/hc/article_attachments/35831517379863)

As informações sobre o eConsignado devem ser enviadas desde o início da operação dessa modalidade de empréstimo, conforme estabelecido em normativas específicas.

## Como lançar o empréstimo eConsignado

**(1)** Para realizar o cadastro do crédito do trabalhador para o colaborador, acesse a **Central do eSocial** e **envie o evento S-1010 com a rubrica 9253**.

**(2)** O fluxo para **o lançamento do eConsignado no sistema** ocorrerá pela tela **Lançamento de Movimento** (Pessoal+ > Rorinas Folha).

| **⚠️** **Atenção**  **Quando houver mais de um empréstimo para o mesmo CPF, os eventos de desconto são ordenados na importação de dados conforme os critérios**:   - **1º**: os empréstimos são organizados pela data de início do contrato, do mais antigo para o mais recente; - **2º (desempate)**: se houver contratos com a mesma data de início, os empréstimos são ordenados pelos valores das parcelas, do maior para o menor.   **Importante**   - **Essa ordenação não ocorre em lançamentos manuais**. - Para lançar o desconto do crédito do trabalhador, **utilize apenas uma forma de lançamento e dê preferência ao importador do arquivo fornecido pelo Governo**. Assim, a ordenação dos descontos será registrada corretamente e você evita erros comuns em lançamentos manuais. |
| --- |

Pode ser lançado das seguintes formas:

| [Por importação dos dados via API](https://ajuda.sankhya.com.br/hc/pt-br/articles/35831517422871-Como-lan%C3%A7ar-o-Cr%C3%A9dito-do-Trabalhador#h_01K1X4BQZA1QZQWQ8PYETFW0FH) |
| --- |
| [Por importação do arquivo de empréstimo via planilha](https://ajuda.sankhya.com.br/hc/pt-br/articles/35831517422871-Como-lan%C3%A7ar-o-Cr%C3%A9dito-do-Trabalhador#h_01JR8PTPZE0CKK26PRWXEJP737) |
| [Manualmente](https://ajuda.sankhya.com.br/hc/pt-br/articles/35831517422871-Como-lan%C3%A7ar-o-Cr%C3%A9dito-do-Trabalhador#h_01JR8PCJB4DA1XCFVHKWCFFVS4) |

**Observação:** para **produtor rural pessoa física**, o sistema identifica automaticamente se a importação do Crédito do Trabalhador deve ser feita por **CNPJ ou CAEPF**, garantindo a correta alocação dos trabalhadores, mesmo quando há CNPJ cadastrado.

Acesse o artigo [**Importação do crédito do trabalhador para produtor rural Pessoa Física com CNPJ**](https://ajuda.sankhya.com.br/hc/pt-br/articles/37531124491287) para mais detalhes.

#### **(1)** Por importação dos dados via API

Essa funcionalidade permite importar, de forma automática e segura, as informações do **Crédito do Trabalhador** a partir da API disponibilizada pelo governo, diretamente para o sistema.

```
 Para utilizar essa importação, é necessário cadastrar um certificado digital válido no sistema. Esse certificado é o que garante a comunicação segura
com a API do governo. Sem ele, a importação não funcionará.
```

Na tela **Lançamento de Movimento**, selecione a opção **Por Funcionário** e escolha a **Empresa** e a **Referência** para o lançamento.

Acione o botão **Importação automática Crédito Trabalhador** e escolha a **empresa matriz** e a **referência**. Clique em **Importar** e confirme para prosseguir com a importação automática.

[GIF animado: Imagem 12: Acione o botão Importação automática Crédito Trabalhador e escolha a empresa matriz e a referência . Clique em Importar…](https://ajuda.sankhya.com.br/hc/article_attachments/35831501403415)

Durante o processo, o sistema exibirá o andamento da importação na tela. Caso o pop-up seja fechado, o botão **Acomp. Importação Crédito do Trabalhador** ficará visível; ao clicar nele, será possível acompanhar o status da importação em andamento.

**Importante**

- **O governo disponibilizou essa funcionalidade em versão beta** e, conforme [comunicado oficial](https://www.gov.br/trabalho-e-emprego/pt-br/assuntos/credito-do-trabalhador/empregador/comunicado-aos-empregadores/pdf-comunicado-empregador-web.pdf), atribui ao empregador e fornecedor de tecnologia a responsabilidade por eventuais inconsistências ou riscos. Sendo assim, **recomendamos atenção redobrada na validação dos dados importados**, garantindo que todas as informações estejam corretas antes do cálculo.
- **Para visualizar e utilizar a funcionalidade, é necessário que o sistema esteja na versão 5.46 ou superior e que seja liberada para utilização**. Entre em contato com a **Sankhya para liberação** da funcionalidade. Após entrada em produção pelo Governo, ela será disponibilizada para todos.
- A importação automática está disponível para empresas matrizes e suas filiais que tenham seus dados integrados e atualizados no sistema.
- **Se não houver dados disponíveis pelo governo** para a empresa ou referência escolhida, **o sistema mostrará uma mensagem** informando que a importação não pode ser feita.
- **Se já houver uma importação em andamento, o sistema não permitirá iniciar outra importação** para uma empresa ou referência diferente.

Caso seja necessário excluir um lançamento importado via API, se atente às seguintes regras do sistema:

- O lançamento pode ser excluído **somente quando não estiver vinculado a cálculo de rescisão ou mensal já processado na referência**.
- Antes da exclusão, o sistema solicita confirmação.
- Depois de excluído, o lançamento não pode ser recuperado pela própria tela; para utilizar novamente os dados, é necessário realizar uma nova importação via API.
- Se existir cálculo processado vinculado ao lançamento na referência, a exclusão será bloqueada.
- Além disso, quando os dados de Crédito do Trabalhador forem importados automaticamente durante uma simulação de rescisão e a rescisão não for confirmada, o sistema remove esses dados do **Lançamento de Movimento**. Se a rescisão for calculada novamente, os dados serão importados novamente de forma automática.

#### **(1)** Por importação do arquivo de empréstimo via planilha

Acesse o **Portal Emprega Brasil** e baixe a planilha disponibilizada pelo governo com os dados dos empréstimos na referência informada.

Depois, na tela **Lançamento de Movimentos**, indique a **Empresa** e a **Referência** para o lançamento.

Clique no botão **Importar Movimentos por Planilha**, escolha a opção **Crédito do Trabalhador (eConsignado)**, realize a importação da planilha no formato XLSX e confirme a operação.

[GIF animado: Imagem 13: Clique no botão Importar Movimentos por Planilha , escolha a opção Crédito do Trabalhador (eConsignado) , realize a…](https://ajuda.sankhya.com.br/hc/article_attachments/35831517399831)

Se estiver tudo certo, o sistema lançará os valores da planilha e preencherá os dados correspondentes na referência informada para serem utilizados no cálculo e nos documentos disponibilizados aos colaboradores mensalmente e na rescisão.

| **⚠️** **Atenção**  O sistema **lançará o valor da parcela apenas no mês selecionado**. Por isso, **é necessário importar mensalmente a planilha disponibilizada no portal Emprega Brasil**. Isso ocorre porque os valores das parcelas podem sofrer alterações devido a renegociações bancárias/portabilidade entre bancos. Além disso, não é possível corrigir dados e valores já enviados ao governo. |
| --- |

Caso já exista lançamento na referência para o mesmo colaborador, o sistema substitui os dados anteriores.

O sistema acrescentará zeros à esquerda do CPF do colaborador que tiver menos de 11 caracteres. Mesmo assim, se o colaborador não for localizado, a importação não será travada, pois ao final da importação ele será exibido nos registros não importados.

Além disso, se algum dado estiver incorreto, também será exibido o total de registros não importados.

![Imagem 14: Além disso, se algum dado estiver incorreto, também será exibido o total de registros não importados.](https://ajuda.sankhya.com.br/hc/article_attachments/35831517402647)

O sistema permite baixar a planilha para visualizar os colaboradores e seus respectivos erros de validação e orientações para corrigi-los. Os principais erros podem ser:

- CNPJ duplicado;
- funcionário com matrícula duplicada;
- folha calculada na referência do lançamento;
- código do banco do empréstimo não cadastrado.

Após a correção poderá utilizar a mesma planilha para importação dos dados pendentes, exclua apenas a coluna de erros.

Finalizada a importação, poderá seguir com o cálculo da folha.

#### **(1)** Manualmente

O **evento de desconto** deve ser lançado individualmente para cada colaborador na tela **Lançamento de Movimento** mensalmente.

![Imagem 15: O evento de desconto deve ser lançado individualmente para cada colaborador na tela Lançamento de Movimento mensalmente.](https://ajuda.sankhya.com.br/hc/article_attachments/35831501406999)

Nela, os campos abaixo devem ser preenchidos obrigatoriamente:

- **instituição financeira** (banco responsável pelo empréstimo);
- **número do contrato eConsignado** (identificação do contrato);
- **observação eConsignado** (detalhes adicionais).

O valor da parcela deve ser lançado mensalmente, conforme disponibilização pelo governo, por meio do arquivo de importação liberado no **Portal Emprega Brasil**.

| **⚠️** **Atenção**  **Não é possível** lançar eventos de eConsignado na modalidade **Por Evento** para vários colaboradores ao mesmo tempo, pois as informações a serem lançadas são únicas para cada colaborador. |
| --- |

Após o lançamento, calcule a folha.

## Como calcular a folha com o desconto do eConsignado

**(1)**  Realize o cálculo da folha do colaborador e confira o lançamento do desconto.

![Imagem 16: (1) Realize o cálculo da folha do colaborador e confira o lançamento do desconto.](https://ajuda.sankhya.com.br/hc/article_attachments/35831517404951)

**(2)** Após a confirmação da folha, libere-a para ser enviada ao eSocial por meio do botão **Liberação para eSocial** da tela [Gerenciador de Folhas](https://ajuda.sankhya.com.br/hc/pt-br/articles/4424800696599-Gerenciador-de-Folhas#Bot%C3%B5esdaTela).

[GIF animado: Imagem 17: (2) Após a confirmação da folha, libere-a para ser enviada ao eSocial por meio do botão Liberação para eSocial da tela…](https://ajuda.sankhya.com.br/hc/article_attachments/35831517405591)

**Notas:**

**(3)** Esse evento pode ser usado apenas nos tipos de movimento **Mensal** ou **Rescisão**.
**(3)** Não é permitido **lançar evento de desconto** de eConsignado **diretamente no cálculo da folha Mensal** ou de **Rescisão**.

Esse lançamento deve ser feito pela tela [Lançamento de Movimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/38268572935319).

## Modelo de Holerite para o eConsignado

O holerite deve apresentar, de forma clara e organizada, as informações relacionadas ao Crédito do trabalhador, permitindo que o colaborador acompanhe os descontos realizados em sua folha.

As informações exibidas são:

- Instituição financeira responsável pelo crédito consignado;
- Número do contrato vinculado ao desconto;
- Saldo não descontado, quando houver.

Caso exista saldo pendente, será exibida uma mensagem de aviso ao trabalhador destacando o valor ainda não quitado.

Se o saldo estiver totalmente pago, o campo correspondente será exibido com valor zerado.

[GIF animado: Imagem 18: Se o saldo estiver totalmente pago, o campo correspondente será exibido com valor zerado.](https://ajuda.sankhya.com.br/hc/article_attachments/35831876476823)

## Envio da folha com o eConsignado para o eSocial

**(1)** Agora, na tela [Central do eSocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/7064222145175), deve-se enviar o evento **S-1200** (Remuneração Mensal).

Em caso de rescisão, o evento correspondente ao tipo de desligamento, sendo o **S-2299** (Rescisão) ou **S-2399** (Rescisão por Término de Contrato).

Dessa forma, o desconto será informado no **grupo de Informações de Desconto de Empréstimo em Folha (descFolha)** do eSocial.

**(2)** Após o envio do respectivo evento, ainda na tela **Central do eSocial**, acione o botão **Conferência Analítica dos Tributos** e informe os dados necessários para gerar o relatório S-5003 e acompanhar os descontos do eConsignado.

![Imagem 19: (2) Após o envio do respectivo evento, ainda na tela Central do eSocial , acione o botão Conferência Analítica dos…](https://ajuda.sankhya.com.br/hc/article_attachments/35831501417751)

O evento S-5003 retorna as informações sobre o desconto da parcela do eConsignado quando nos eventos S-1200, S-2299 ou S-2399 houver um valor informado em rubrica com natureza [9253]. Esse valor será incluído automaticamente na guia de recolhimento do FGTS Digital.

No entanto, mesmo que o evento traga o valor descontado do eConsignado, ele **não será incluído** na guia do FGTS Digital nos seguintes casos:

- se for enviado **após o vencimento mensal** do consignado, que segue o mesmo vencimento do FGTS para aquela competência;
- se for **retificado após o vencimento mensal**, com inclusão ou alteração das informações do eConsignado;
- se for enviado **após o pagamento da parcela** do consignado referente àquela competência.

Considere ainda que, após o envio do evento de fechamento de eventos periódicos S-1299, o evento S-5013 retorna as informações com a soma dos valores apurados nos totalizadores por trabalhador (S-5003), exceto dos valores relativos ao eConsignado.

Se você ainda tem dúvidas sobre o funcionamento do crédito (eConsignado) do trabalhador, confira abaixo as perguntas mais frequentes e suas respostas.
