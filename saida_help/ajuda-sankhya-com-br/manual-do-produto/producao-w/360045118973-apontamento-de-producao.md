---
id: "360045118973"
titulo: "Apontamento de Produção"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118973-Apontamento-de-Produ%C3%A7%C3%A3o"
trilha: "Manual do Produto > Produção > Produção/W"
atualizado_em: "2026-07-29T14:55:17Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "WMS", "Operações de Produção", "Apontamento", "APOTARIFAMAT", "Produção", "CAMPOLOGINAPONT", "br.com.sankhya.mgeprod.apontamentodeproducao", "Apontamento de Produção manual", "Simplificação do registro de produção", "Parametrização e uso de balança", "Movimentação de estoque vinculada"]
---

# Apontamento de Produção

```
 Módulo: Produção > Rotinas
```

---

Essa rotina é exclusiva para realização de Apontamentos de Produção, diferente da tela [Operações de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o) existente no pack 1, que além do apontamento, também possui outros recursos, tais como: Controle de Qualidade e Gerenciamento da Atividade (Aceitar/Iniciar/Rejeitar).

Já na tela Ponto de Apontamento é possível executar o apontamento sem a necessidade de gerenciar as atividades, ou seja, torna o processo de inclusão de dados do apontamento mais simples e ágil em um computador desktop. Aqui temos um login específico da rotina, ou seja, o sistema fica logado no Sankhya Om com um usuário (usuário Ponto de Apontamento) e os operadores logam com seus respectivos usuários para realizarem o apontamento. O segundo login no Ponto de Apontamento (login do operador) não consome uma segunda licença.

Em resumo, para cada computador usado para inserir os apontamentos, deve-se possuir uma licença Ponto de Apontamento, independente da quantidade de operadores.

Existem todos os tipos de apontamento da tela Operações de Produção, incluindo o Apontamento de Troca de Turnos e Apontamento por peso.

**Importante:** essa funcionalidade não está adequada para o uso mobile, uso off-line, coletores ou totens. Não contempla processos, regras e integrações com MES (Manufacturing Execution Systems).

**Importante:** esta tela só será apresentada se a empresa possuir em sua licença o produto **"30.751 - Ponto de Apontamento/W"**.

**Nota:** caso queira, pode-se realizar a criação de campos adicionais a essa tela. Basta fazê-lo por meio da tela [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294) nas tabelas abaixo:

- TPREIATV - Execução Atividade;
- TPRAPA - Apontamento PA;
- TPRAMP - Apontamento Materiais;
- TPRASP - Apontamento Sub Produto;
- TPRARW - Apontamento Recursos CT.

Devido à característica citada anteriormente, para iniciar a tela, é necessário realizar um login com usuário e senha válidos.

Acesse os links abaixo para facilitar sua navegação nas funcionalidades desta tela:

| [Informações Iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118973-Apontamento-de-Produ%C3%A7%C3%A3o#informa%C3%A7%C3%B5esiniciais) |  | [Aba Execução](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118973-Apontamento-de-Produ%C3%A7%C3%A3o#abaexecu%C3%A7%C3%A3o) |
| --- | --- | --- |
| [Aba Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118973-Apontamento-de-Produ%C3%A7%C3%A3o#abaitens) |  | [Aba Mov. Acessórias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118973-Apontamento-de-Produ%C3%A7%C3%A3o#abamov.acess%C3%B3rias) |
| [Confirmação do Apontamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118973-Apontamento-de-Produ%C3%A7%C3%A3o#confirma%C3%A7%C3%A3odoapontamento) |  | [Serviços de Pesagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118973-Apontamento-de-Produ%C3%A7%C3%A3o#servi%C3%A7osdepesagem) |
| [Execução da Operação Encadeada](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118973-Apontamento-de-Produ%C3%A7%C3%A3o#execu%C3%A7%C3%A3odaopera%C3%A7%C3%A3oencadeada) |  |  |

![Imagem 1: Execução da Operação Encadeada](https://ajuda.sankhya.com.br/hc/article_attachments/360095154954)

### Informações Iniciais

Caso necessário, através do parâmetro **"Campo p/ login em Apontamento de Produção - CAMPOLOGINAPONT"** você pode determinar o campo que será utilizado pelo sistema para localização de seu usuário, no momento em que realizar o login na tela de Apontamento de Produção. Nesta configuração, você pode trabalhar com a tabela de Usuários (TSIUSU), sendo possível utilizar um campo já existente na tabela ou mesmo um campo adicional que tenha sido nela criado (tela [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294)). Por exemplo, criando o campo adicional de nome AD\_CRACHA, e inserindo o mesmo no parâmetro de chave CAMPOLOGINAPONT, ao acessar a tela de Apontamento de Produção, você terá que informar no campo **"Usuário"** a numeração de seu crachá.

Esta tela foi criada com o intuito de simplificar o apontamento de atividades no âmbito industrial, não possuindo funcionalidades referentes ao controle de qualidade. Assim, para atividades relacionadas à controle de qualidade, os apontamentos devem ser realizados através da tela [Operações de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274).

**Observação:** ao acessar a rotina de Apontamento de Produção, caso este acesso esteja sendo feito com um usuário cuja configuração **"Seleciona Centro de Trabalho em Apontamento de Produção"** esteja realizada ([Cadastro de Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874), aba Geral), será apresentado o pop-up denominado **"Especificar Centro de Trabalho em uso"**, no qual serão exibidos os Centros de Trabalho disponíveis para a pessoa logada, a fim de que esta defina o Centro a ser utilizado no apontamento em questão.

Após o login, o próximo passo é filtrar a OP da qual você deseja realizar o apontamento. Por isso, você será direcionado para uma visão onde é possível digitar o número da OP. Após a digitação, são apresentados os dados da OP em um cabeçalho.

Ao filtrar uma Operação de Produção na tela Apontamento de Produção, e o sistema identificar que nesta OP exista uma ou mais atividades definidas com ciclo de controle de qualidade, uma das seguintes mensagens surgirá na tela:

Caso exista apenas uma atividade na OP filtrada:

**"A(s) atividade(s) ‘xx’ não foram apresentada(s), pois possuem configuração de Controle de Qualidade."**

Caso exista mais de uma atividade na OP filtrada:

**"A(s) atividade(s) 'xxx' não foram apresentada(s), pois possuem configuração de Controle de Qualidade. Isso ocorre porque a tela 'Apontamento de Produção' é destinada à realização de apontamentos e não deve ser utilizada para execução de atividades com Controle de Qualidade. As atividades com Controle de Qualidade devem ser executadas na tela 'Operações de Produção'."**

Na parte superior esquerda do cabeçalho, temos três botões que influenciam no comportamento desta rotina. São eles:

1. Por meio do botão ![Imagem 2: Por meio do botão "Exportar Grade para PDF" , além das opções de exportação de relatório, teremos a opção de visualizar…](https://ajuda.sankhya.com.br/hc/article_attachments/22891296322455) **"Exportar Grade para PDF"**, além das opções de exportação de relatório, teremos a opção de visualizar e imprimir Relatórios Formatados, para tal ação, basta você inserir a "Tela/Instância" do relatório desejado na tela [Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108573) e em seguida selecionar o **"Nro. da OP"** de sua preferência nesta tela.
2. O botão ![Imagem 3: O botão "Anexos Processo Produtivo" , ao ser acionado, exibirá um pop-up contendo os anexos ou link's configurados no…](https://ajuda.sankhya.com.br/hc/article_attachments/21156637563799) **"Anexos Processo Produtivo"**, ao ser acionado, exibirá um pop-up contendo os anexos ou link's configurados no Processo Produtivo, sendo possível efetuar o download destes arquivos anexados.
3. Já o botão ![Imagem 4: J á o botão "Ações" , permite que você acesse as ações personalizadas durante a execução de um apontamento. As Ações…](https://ajuda.sankhya.com.br/hc/article_attachments/16593996850583) **"Ações"**, permite que você acesse as ações personalizadas durante a execução de um apontamento. As Ações Personalizadas respondem à entidade/tabela InstanciaAtividade/TPRIATV. Através do parâmetro USUARIO\_LOGADO, é possível identificar qual pessoa logada na tela que executou a ação personalizada, sendo que, a pessoa logada na tela pode ser diferente da logada no sistema.

Na grade mais abaixo, são apresentadas todas as atividades disponíveis de execução (atividades Aguardando Aceite ou Aceita ou Iniciada) para que você selecione qual de fato deseja iniciar o apontamento.

**Importante:** caso exista apenas uma atividade disponível, o sistema a selecionará de forma automática. Então essa visão não será apresentada à você. Isso não é erro, é um comportamento do sistema.

![Imagem 5: Importante: caso exista apenas uma atividade disponível, o sistema a selecionará de forma automática. Então essa visão…](https://ajuda.sankhya.com.br/hc/article_attachments/360095157734)

**Importante:** a pessoa "dona" da atividade (seu candidato Executante), é aquela que realizou seu aceite ou a inicializou. Considerando uma única pessoa ou mesmo um grupo de pessoas, uma atividade poderá ser visualizada apenas pela própria pessoa que fez sua aceitação ou inicialização. O Gerente de Manufatura poderá visualizar todas as atividades, tendo elas passado ou não pelo aceite ou inicialização. Além disso, a finalização das atividades poderá ser realizada apenas pelo dono da atividade, ou ainda, pelo seu Gerente de Manufatura.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118973-Apontamento-de-Produ%C3%A7%C3%A3o#top)

### Aba Execução

Uma vez selecionada a atividade, você será direcionado para a visão de apontamento. Na aba Execução, é possível realizar o apontamento de execução da atividade onde é possível especificar um usuário executante, Dh. Início, Dh. Final e o Tipo da execução.

![Imagem 6: Uma vez selecionada a atividade, você será direcionado para a visão de apontamento. Na aba Execução, é possível…](https://ajuda.sankhya.com.br/hc/article_attachments/360095157774)

O campo **"Cód. Executante"** é habilitado para edição visto que o apontamento pode ser realizado por um supervisor de fábrica, representando o operador que executou aquela atividade. Já o campo **"Cód. Responsável"** sempre fica desabilitado para edição, pois o responsável pelo apontamento é sempre a pessoa que estiver logada na tela.

**Nota:** não será possível realizar alterações nos campos **"Dh. Início"** e **"Dh. Final"** quando a data e hora estiverem fora do período de início/fim da atividade.

Através do campo **"Tipo"** é possível indicar se a execução é do tipo **"Normal"**, **"Parada"** ou do tipo **"Fim de turno"**. Vejamos os seguintes pontos:

- Ao informar que a execução corresponde ao tipo Parada, será solicitado um motivo e observações a cerca da mesma;
- A opção Fim de turno só estará disponível se a atividade em questão estiver configurada para suportar Multi-turnos ([Configuração de Atividades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674) do Processo Produtivo, aba **"Geral"**, campo **"Multi-turno"**);
- Além disso, ao optar pela opção Fim de turno, o campo **"Motivo Parada"** será preenchido automaticamente com o motivo configurado na Configuração de Atividades do Processo Produtivo, aba Geral, campo **"Motivo de parada (fim de turno)"**;
- Os motivos de parada deverão estar previamente cadastrados na tela [Motivos de Parada](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611614).

**Observação:** o parâmetro **"É obrigatório selecionar um motivo para parada - OBRIGMOTIVPARAD"**, quando ligado, tornará obrigatório informar o motivo pelo qual a execução é do tipo Parada.

Ao continuar uma atividade que utiliza um Centro de Trabalho, o sistema irá realocar, automaticamente, o C.T à atividade, desde que este não esteja em uso por outra atividade.

Se a alocação da atividade utilizar um Centro de Trabalho específico ou por categoria que utiliza o Padrão da Categoria e ambos forem de uso exclusivo, caso estes estiverem alocados em outra atividade, não será possível dar continuidade, sendo assim, o sistema exibirá a mensagem:

**"Não será possível continuar a atividade, pois o Centro de Trabalho não é exclusivo e está sendo utilizado por outra atividade."**

Caso o Centro de Trabalho seja por categoria que utiliza o Tipo de Alocação = Inclusão de ordem ou Antecipado (no planejamento), e este for de uso exclusivo, caso o C.T. esteja alocado em outra atividade, será apresentado um pop-up para você selecionar outro Centro de Trabalho da mesma categoria que esteja disponível para uso.

**Importante:** o apontamento de execução é algo separado do apontamento de materiais, então é possível apontar execução sem de fato apontar materiais.

No campo **"Local de Baixa"** será exibido o local da baixa da MP, este local deve estar previamente definido no campo **"Local para baixa de MPs"** da aba **"Atividades"** das [Operações de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058418533-Processo-Produtivo-Nova#opera%C3%A7%C3%B5esdeestoque), tela [Processo Produtivo - Nova](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058418533-Processo-Produtivo-Nova). Além disso, esse campo poderá ser editado quando a marcação **"Permitir alterar local da baixa da MP"** da aba [Apontamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#abaapontamento) das [configurações das atividades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#abaapontamento), for habilitada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118973-Apontamento-de-Produ%C3%A7%C3%A3o#top)

### Aba Itens

O apontamento de materiais é realizado na aba **Itens**, onde se especifica a quantidade de PA do apontamento, a quantidade das matérias-primas gastas para a produção e a quantidade de subprodutos gerados na atividade.

> **Observações sobre o apontamento de materiais:**
>
> - **Sigilo de Composição:** Para casos em que o Operador de Produção não pode visualizar as matérias primas devido ao sigilo na composição do produto final, é possível configurar o sistema para inibir a visualização das MPs através da configuração **"Inibe acesso à matéria prima"** da aba **Segurança** do cadastro de **Usuários**.
> - **Produto como MP de si próprio:** Com o parâmetro **"Permitir definir produto como MP de si próprio. - PRODMPPROP"** habilitado, um produto pode ser apontado como Matéria-prima de um apontamento onde ele mesmo é o Produto Acabado (comumente utilizado em processos de reprocessamento/reparo).
> - **Local de Baixa:** Na sub-aba **Materiais**, o campo **"Local de Baixa"** exibe o local definido no campo **"Local para baixa de MPs"** (aba **Atividades** das [Operações de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058418533-Processo-Produtivo-Nova#opera%C3%A7%C3%B5esdeestoque), tela [Processo Produtivo - Nova](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058418533-Processo-Produtivo-Nova)). Este campo pode ser editado se a marcação **"Permitir alterar local da baixa da MP"** estiver habilitada na aba [Apontamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#abaapontamento) das [configurações das atividades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades), for habilitada.

Os registros de apontamento dos **Recursos de Centro de Trabalho** serão gerados automaticamente sempre que ocorrer a inserção de um apontamento para o PA (assim como acontece com as MP's).

Com o parâmetro **"Aponta Tarifa junto com Materiais. - APOTARIFAMAT"** ligado, a configuração das [Tarifas CIP](https://sankhya.zendesk.com/hc/pt-br/articles/360044611074) poderão ser realizadas através da tela [Composição do Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050836154-Composi%C3%A7%C3%A3o-do-Produto), aba [Matérias-Primas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050836154-Composi%C3%A7%C3%A3o-do-Produto#abamat%C3%A9rias-primas), e o apontamento de **Tarifas CIP** feito juntamente com o apontamento de materiais.

![Imagem 7: Com o parâmetro "Aponta Tarifa junto com Materiais. - APOTARIFAMAT" ligado, a configuração das Tarifas CIP poderão ser…](https://ajuda.sankhya.com.br/hc/article_attachments/360095157934)

Quando o campo **"Quantidade base para apontamento"** da aba [Apontamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058460853-Configura%C3%A7%C3%A3o-de-Atividades-Nova#abaapontamento) estiver configurado com a opção **"Não sugere"**, a coluna **"Qtd. apontada"** do PA será exibida com o valor igual a zero, dessa forma, o apontamento só será confirmado após a alteração desse valor. Caso o referido campo esteja com a opção **"Qtd. apontada de PA"** selecionada, o apontamento poderá ser confirmado sem a necessidade de editar o valor apresentado na coluna.

Na coluna **"Qtd. Total de Perda"** informe a quantidade correspondente à perda na execução da atividade, para posterior finalização da atividade.

Informe na coluna **"Qtd. de Motivos de Perda"** a quantidade total de motivos de perda. Se for inserida uma quantidade de motivos de perda maior do que 1, será aberto o pop-up de detalhamento de perda automaticamente: 

[GIF animado: Imagem 8: Informe na coluna "Qtd. de Motivos de Perda" a quantidade total de motivos de perda. Se for inserida uma quantidade de…](https://ajuda.sankhya.com.br/hc/article_attachments/6377188530199)

**Nota:** conforme exibido no gif acima, com uma quantidade de motivos de perda maior do que 1, também é habilitado o botão ![detalhar](https://ajuda.sankhya.com.br/hc/article_attachments/15524343576471) **"Detalhar Perdas"**. Através dele você informa o volume de perda por cada motivo durante o apontamento e, após salvá-lo, o botão seguirá habilitado para consultas. 

![Imagem 10: Informações adicionais:](https://ajuda.sankhya.com.br/hc/article_attachments/16593990898583) **Informações adicionais:**

- Se a Qtd. de Motivos de Perda informada no pop-up Detalhamento de Perdas for diferente do valor informado no campo, será exibida a mensagem abaixo:

**"Total de motivos de perda detalhado é diferente do valor X informado no campo Qtd. de Motivos de Perda. Por favor revisar os motivos informados e salvar novamente."**

- Quando for informada uma Qtd. Perda no pop-up Detalhamento de Perdas diferente da inserida no campo Qtd. Total de Perda, será apresentada a seguinte mensagem:

**"Total de perda confirmado é diferente do valor X informado no campo Qtd. Total de perda. Por favor revisar os volumes informados e salvar novamente."**

Após confirmar os apontamentos com os motivos de perdas, a aba [Detalhamento de Perdas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058023454-Ordens-de-Produ%C3%A7%C3%A3o-Nova#abadetalhamentodeperdas) na tela [Ordens de Produção - Nova](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058023454-Ordens-de-Produ%C3%A7%C3%A3o-Nova) será preenchida automaticamente. Também será gerada uma Nota de Produção para o Subproduto e Produto Acabado e os resultados apresentados na tela [Dashboard OEE](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405006529047-Dashboard-OEE). 

**Importante:** caso o parâmetro **"É obrigatório selecionar um motivo para perda - OBRIGMOTIVPERDA"** esteja ativado, ao iniciar a atividade e efetuar os apontamentos das unidades e suas respectivas perdas, torna-se obrigatório o preenchimento do Motivo da Perda; caso contrário, ao confirmar o procedimento, será apresentada a seguinte mensagem:

**"É obrigatório o usuário selecionar um motivo para perda sempre que apontar 'qdt. perda'"**

Por meio do botão **"Nro. Série"** será aberto o pop-up **"Número de série"** onde são apresentados os números de série do Produto Acabado. Neste pop-up, se a série foi configurada para ser gerada automaticamente, teremos apenas a visualização dos dados e estes não poderão ser editados. Caso a geração da série seja manual, será possível inserir e/ou excluir informações no pop-up.

Também no pop-up Número de série, existe a marcação **"Perda"** que, se assinalada, fará com que a série em questão corresponda à uma determinada quantidade apontada como perda do PA. Nestas situações, a quantidade de séries sinalizadas como perdas deve ser igual à quantidade definida como perda no apontamento.

Na sub-aba **"Materiais"** você poderá informar quando há a perda de matérias-primas durante a execução da atividade; para isso, ligue o parâmetro **"Habilita perda de Matéria Prima na produção - HABPERDAMPPROD"**. Assim, o sistema exibirá as colunas **"Qtd. Total de Perda"**, **"Qtd. de Motivos de Perda"** e **"Motivo(s) de Perda"**, onde será apontada a quantidade das perdas.

Considere ainda que, quando houver mais de um motivo de perda para a mesma matéria-prima, o botão Detalhar Perdas será habilitado para informar os detalhes das perdas.

Então, após realizar esse apontamento, você poderá conferi-lo na aba [Detalhamento de Perdas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058023454-Ordens-de-Produ%C3%A7%C3%A3o-Nova#abadetalhamentodeperdas) da tela [Ordens de Produção - Nova](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058023454-Ordens-de-Produ%C3%A7%C3%A3o-Nova).

**Observação:** ao habilitar o parâmetro **"É obrigatório selecionar um motivo para perda de Matéria Prima - OBRIGMOTPERDAMP"**, você deverá, obrigatoriamente, informar na coluna **"Qtd. Perda"**, o motivo da perda da matéria-prima quando este não for informado nos apontamentos com essa perda.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118973-Apontamento-de-Produ%C3%A7%C3%A3o#top)

### Aba Mov. Acessórias

![Imagem 11: Aba Mov. Acessórias](https://ajuda.sankhya.com.br/hc/article_attachments/360097452713)

Por meio do botão **"Nova Movimentação"** da aba **"Mov. Acessórias"** será possível realizar operações de estoque manuais, assim como nas rotinas de [Operações de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118973-Apontamento-de-Produ%C3%A7%C3%A3o#top)

### Confirmação do Apontamento

Uma vez realizado o apontamento, você deve então confirmá-lo a partir do botão **"Confirmar"**. Antes da confirmação, é possível especificar uma observação referente ao apontamento no campo **"Observação"**.

**Nota:** como a tela foi construída pensando em usabilidade e performance no chão de fábrica, então as informações do apontamento ficam em memória até que você confirme o apontamento. Então, caso a tela seja fechada antes da confirmação, o registro de apontamento será perdido.

Uma vez confirmado o apontamento, você precisa decidir sua próxima ação. Por isso, é apresentada uma lista com as possíveis opções:

- **Sair:** Será feito o logout da tela;
- **Finalizar Atividade:** Será finalizada a atividade a qual foi realizado o apontamento. Caso exista apenas uma execução em aberta e essa seja do usuário logado, então o sistema utiliza a data atual para finalizar a atividade e a execução;
- **Transferência Parcial:** Será apresentado o pop-up de transferência parcial para que você possa executar uma transferência parcial do produto para a próxima atividade. Esse botão fica habilitado apenas caso a atividade suporte apontamento parcial (evento de **"Apontamento Parcial"** anexado à atividade);
- **Novo Apontamento (Outra OP):** O usuário é direcionado para a visão de filtro de OP para iniciar o apontamento em outra ordem;
- **Novo Apontamento (Mesma OP):** Você será direcionado para a visão de filtro de atividade para iniciar o apontamento em outra atividade da mesma ordem;
- **Liberar C.T.:** Ao finalizar uma atividade que esteja configurada para liberar o Centro de Trabalho, proceda com a liberação por meio deste botão. Caso esteja operando uma atividade configurada apenas para liberar o Centro de Trabalho manualmente, o sistema verifica se o Centro de Trabalho vinculado à atividade foi liberado; caso negativo, não será permitida a finalização da atividade.

Quando uma atividade estiver pendente de dispensa, no campo **"Tipo"** desta tela, você deve selecionar a opção **"Parada"** e no campo **"Motivo Parada"** informar o motivo da parada da atividade.

**Observação:** ao parar uma atividade que utiliza Centro de Trabalho, o executante poderá liberá-lo, caso seja necessário.

Se a atividade estiver parada, você poderá realizar a liberação do Centro de Trabalho, porém, para executar esta ação, a atividade deve estar configurada para Liberar o C.T manualmente.

Ao clicar no botão **"Confirmar"**, o sistema apresentará um pop-up para confirmação, caso este seja confirmado, o botão Liberar C.T ficará desabilitado e, na tela [Centros de Trabalho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118793), a data e a hora desta liberação serão exibidas na aba **"Histórico de Uso"** na coluna **"Dh. Liberação"**.

**Nota:** quando você não confirmar o pop-up, o campo Tipo ficará desabilitado e a coluna Dh. Liberaçao (tela Centros de Trabalho, aba Histórico de Uso) ficará vazia.

![Imagem 12: Nota: quando você não confirmar o pop-up, o campo Tipo ficará desabilitado e a coluna Dh. Liberaçao (tela Centros de…](https://ajuda.sankhya.com.br/hc/article_attachments/360095158094)

**Importante:** ao tentar finalizar uma atividade, existindo Apontamentos Divergentes, ou seja, apontamentos que fujam dos desvios inferior ou superior ([Processo Produtivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611314), [aba Apontamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611314-Processo-Produtivo#abaapontamento)), no pop-up denominado Apontamentos Divergentes, será apresentada a seguinte mensagem:

**"Qtd. Apontada é menor/maior que a qtd. em operação para: <Descrição do Produto (PA)>. Deseja continuar a confirmação?".**

No pop-up mencionado, na coluna **"Qtd. Perda"**, informe a quantidade correspondente à perda na execução da atividade, para posterior finalização da atividade.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118973-Apontamento-de-Produ%C3%A7%C3%A3o#top)

### Serviços de Pesagem

Trabalhando na tela Apontamento de Produção, é possível que esta seja integrada ao processo de pesagem. Para tal, realize as seguintes parametrizações:

- Na tela de [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias), habilite o parâmetro **"Utiliza balança tela apontamento produção - UTILIZABALANCA"**; esta ação fará com que na tela Apontamento de Produção, o botão de Pesagem seja apresentado;
- No [Cadastro de Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874), aba Segurança, seção Controle, temos a marcação **"Pode usar pesagem manual"** que, ao ser realizada, será possível realizar manualmente a edição da pesagem do item em produção;
- No [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113), aba Medidas e estoque, sub-aba Estoque, existe a marcação **"Utiliza balança"** que, sendo efetuada, fará com que para o produto em questão seja necessário realizar a pesagem manual ao proceder com o apontamento. Esta é uma marcação feita produto a produto, pois podem existir itens para os quais não será necessário proceder com a pesagem manual.

Depois de realizadas as configurações mencionadas acima, você poderá trabalhar com os serviços de pesagem de maneira manual ou via balança. No Apontamento de Produção, após selecionar o Número da OP, teremos na parte superior das abas Itens, Materiais e Subprodutos, o botão ![Imagem 13: Depois de realizadas as configurações mencionadas acima, você poderá trabalhar com os serviços de pesagem de maneira…](https://ajuda.sankhya.com.br/hc/article_attachments/27243789569303) **"Pesagem"** que estará habilitado caso a opção **"Utiliza balança"** na tela de [Cadastro de Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos), aba [Medidas e estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abamedidaseestoque), sub-aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abaestoque), esteja habilitada. Clicando neste botão, será aberto o pop-up **"Registrar Pesagem Produto Acabado"**, onde serão exibidas todas as pesagens para o produto, bem como serão registradas as perdas. Além disso, no lado direito do pop-up, teremos o peso registrado na balança, a marcação **"Perdas"** que registra o peso aferido como perda.

Para registrar uma pesagem, clique no botão ![Imagem 14: Para registrar uma pesagem, clique no botão "Capturar Leitura" ; o botão "Excluir Leitura" , apaga um item selecionado…](https://ajuda.sankhya.com.br/hc/article_attachments/27244427392023) **"Capturar Leitura"**; o botão **"Excluir Leitura"**, apaga um item selecionado da grade; o botão **"Limpar Leitura"** exclui todos os itens da grade.

Caso clique no botão Capturar Leitura sem marcar a opção Perdas, o sistema apresenta a quantidade pesada na balança na grade de pesagem no campo **"Qtd Apontada"**. No entanto, se utilizar o botão e marcar a opção de Perdas, a quantidade será apresentada no campo **"Qtd. Perda"**.

O botão **"Finalizar Leitura"** encerra a pesagem, fecha o pop-up Registrar Pesagem Produto Acabado e atualiza as informações presentes nas seguintes colunas:

- Aba Itens

 – Qtd. apontada

 – Qtd. Perda

- Aba Materiais

 – Qtd. apontada

- Aba Subprodutos

 – Qtd. apontada

O Registro de Pesagem de Subprodutos é similar ao descrito para o pop-up Registrar Pesagem Produto Acabado. A diferença é que o registro de pesagem de subprodutos não conta com a pesagem para Perdas.

**Importante:** o processo de pesagem poderá ser realizado apenas com o uso da balança modelo 2124 e marca Toledo, cujo indicador é do modelo 9091 AC da mesma marca e se comunica via porta serial a um micro computador.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118973-Apontamento-de-Produ%C3%A7%C3%A3o#top)

### Execução da Operação Encadeada

Na tela Apontamentos de Produção, aba [Mov. Acessória](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118973-Apontamento-de-Produ%C3%A7%C3%A3o#abamov.acess%C3%B3rias), existe o botão **"Nova Movimentação"** que, ao ser acionado, exibirá a operação de estoque de acordo com as configurações da operação de estoque encadeada.
O botão será apresentado quando o **"Tipo de Execução"** da operação de estoque encadeada for **"Manual"**.

No Cabeçalho da Nota temos o campo **"Empresa de Origem"**, que representa a empresa da nota de produção.

O campo **"Empresa de Destino"** receberá o valor da operação encadeada.

**Observação:** este campo será habilitado somente se a TOP for de Transferência.

Ao clicar no botão **"Próximo"**, o pop-up seguirá para a próxima página de configurações, em que tem-se os campos:

O **"Saldo"** será o saldo do produto disponível para movimentação a partir da operação Encadeada. Sendo que, o valor deste campo é calculado como o total do produto em notas de produção subtraindo o valor movimentado por operação encadeada.

No campo **"Qtd. a Movimentar"**, informe a quantidade do produto que será movimentado na operação encadeada em questão.

**Nota:** a quantidade a ser inserida neste campo não poderá ser superior ao Saldo, e não aceitará valores negativos.

O **"Local de Destino"** será o local de destino da Operação Encadeada.

**Observação:** este campo será habilitado para edição somente se a TOP for do tipo T-Transferência.

**Nota:** a finalização da atividade não será permitida caso a Operação Encadeada não tenha sido executada e estiver marcada como Obrigatória.

Para saber mais sobre esta Operação, acesse o link [Configurações de Atividades do Processo Produtivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118973-Apontamento-de-Produ%C3%A7%C3%A3o#top)
