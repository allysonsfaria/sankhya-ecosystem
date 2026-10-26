---
id: "360044606914"
titulo: "Geração Arquivo de Remessa - Configurações"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606914-Gera%C3%A7%C3%A3o-Arquivo-de-Remessa-Configura%C3%A7%C3%B5es"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-09-04T14:00:09Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Contas", "AGTITRECGERCEDI", "EDI", "Financeiro", "Arquivo de Remessa", "Geração Arquivo de Remessa", "Geração Arquivo de Remessa manual", "SOMATXVLRBAIXA", "br.com.sankhya.geracao.arquivo.remessa", "safra", "Conta bancária período situação tipo", "Layout nome arquivo agrupar pagamentos", "Direta validação bancária histórico downloads", "EDI Bancário"]
---

# Geração Arquivo de Remessa - Configurações

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312383496599) Módulo: Financeiro > EDI Bancário
```

---

A geração de remessa é a opção na qual serão informados ao sistema quais títulos financeiros deverão compor o arquivo de remessa que será gerado.

| [Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606914-Gera%C3%A7%C3%A3o-Arquivo-de-Remessa-Configura%C3%A7%C3%B5es#filtros) |  | [Configurações Geração Arquivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606914-Gera%C3%A7%C3%A3o-Arquivo-de-Remessa-Configura%C3%A7%C3%B5es#configura%C3%A7%C3%B5esgera%C3%A7%C3%A3oarquivo) |
| --- | --- | --- |
| [Geração Direta do Arquivo de Remessa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606914-Gera%C3%A7%C3%A3o-Arquivo-de-Remessa-Configura%C3%A7%C3%B5es#gera%C3%A7%C3%A3odiretadoarquivoderemessa) |  | [Validação de Arquivo Remessa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606914-Gera%C3%A7%C3%A3o-Arquivo-de-Remessa-Configura%C3%A7%C3%B5es#valida%C3%A7%C3%A3odearquivoremessa) |
| [Botão Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606914-Gera%C3%A7%C3%A3o-Arquivo-de-Remessa-Configura%C3%A7%C3%B5es#bot%C3%A3ooutrasop%C3%A7%C3%B5es) |  | [Parâmetros que influenciam a rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606914-Gera%C3%A7%C3%A3o-Arquivo-de-Remessa-Configura%C3%A7%C3%B5es#par%C3%A2metrosqueinfluenciamarotina) |

![Imagem 2: Parâmetros que influenciam a rotina](https://ajuda.sankhya.com.br/hc/article_attachments/10093268892951)

## Filtros

Além do **"Assistente para Criação de Filtros"**, esta tela apresenta na parte superior esquerda, alguns campos que poderão ser utilizados como filtros estáticos para selecionar os títulos desejados.

No campo **"Conta bancária"**, defina a conta bancária que será utilizada para gerar o **"Arquivo de Remessa"**. Na Geração do Arquivo de Remessa, se a Conta Bancária escolhida for exclusiva de uma determinada empresa, serão listados apenas os lançamentos que pertencerem àquela empresa. Se não for exclusiva, o sistema irá exibir todos os lançamentos e permitirá sua geração. 

**Importante:** ao informar a Conta bancária, apenas serão apresentados os layouts vinculados à conta bancária informada. Para vincular um Layout à uma conta, acesse a tela [Configuração de Arquivo de Remessa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110273-Configura%C3%A7%C3%A3o-Arquivo-de-Remessa) e selecione o layout. Na aba **"Detalhes para geração do arquivo"**, clique na sub-aba **"Parâmetros"**  e desmarque a marcação **"Usa parâmetros informados na tela de geração"**. Nesse momento, é habilitada a aba **"Contas para Geração"**, onde você informará a conta a ser vinculada ao layout.

Informe nos campos **"Período de Negociação"**, o período de lançamento dos títulos a serem apresentados.

Teremos que no campo **"Situação"** possui três opções de filtros para exibição dos títulos. São eles:

- **Pendentes:** Apenas os títulos pendentes serão apresentados;
- **Baixados:** Selecionando esta opção, apenas os baixados serão exibidos;
- **Ambos:** Serão apresentados tanto os títulos pendentes quanto os baixados na tela.

O campo **"Tipo"** também possui três opções de escolha, que são:

- **Receitas:** O sistema irá apresentar apenas os títulos de Receita;
- **Despesas:** Serão exibidos apenas os títulos de Despesa
- **Ambos:** Definindo esta opção, serão apresentados os títulos de Receita e de Despesa.

Referente à **"Remessa Vazia"**, serão selecionados dentro do período estipulado, os títulos cujo campo **"Número de Remessa"** esteja vazio.

Se a opção **"Nosso Número Preenchido"** for marcada, serão apresentados na grade apenas os títulos que possuam o campo **"Nosso Número"**, dentro do período estipulado.

**Observação:** devido a grande quantidade de registros, podem ocorrer erros ao aplicar o filtro na Geração Arquivo de Remessa; para que os erros não ocorram, é necessário melhorar o filtro para que traga somente os registros necessários para a geração do arquivo ou então alterar as configurações do servidor de aplicação, disponibilizando mais memória para que ele possa processar a grande quantidade de registros vindo do banco de dados.

**Observação:** se houverem títulos vinculados a uma conta monitorada, todas as alterações realizadas serão apresentadas na tela de Geração Arquivo de Remessa independente dos filtros aplicados, assim, o sistema indicará que esses títulos foram alterados e que precisam ser enviados ao banco. Assim, os títulos com ocorrências serão aqueles apresentados na tela, de forma que, quando gerada uma nova remessa, os títulos gerados sumirão.

![Imagem 3: Quando um financeiro possuir mais de uma ocorrência e pelo menos uma delas estiver presente na seleção, será gerado um…](https://ajuda.sankhya.com.br/hc/article_attachments/24076034181655) Quando um financeiro possuir mais de uma ocorrência e pelo menos uma delas estiver presente na seleção, será gerado um Arquivo de Remessa buscando todas as ocorrências do respectivo financeiro.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606914-Gera%C3%A7%C3%A3o-Arquivo-de-Remessa-Configura%C3%A7%C3%B5es#top)

## Configurações Geração Arquivo

A parte inferior esquerda da tela, traz os campos que deverão ser configurados para a geração da remessa.

[Layout](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025392953-Configura%C3%A7%C3%A3o-Arquivo-de-Remessa): Neste campo, informe o arquivo de layout que foi configurado na tela [Configuração Arquivo Remessa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108753-Configura%C3%A7%C3%A3o-Arquivo-Remessa), para geração das remessas.

**Nota:** na Geração Arquivo de Remessa, quando for informado um **"Layout"** que tenha a aba **"Detalhes para Geração de Arquivo"** configurada, serão desabilitadas as opções desta tela e utilizadas as configurações detalhadas no layout ([Configuração Arquivo de Remessa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110273)).

**Nome do arquivo:** Informe neste campo a descrição do **"Arquivo de Remessa"** que será gerado pelo sistema, sendo que, suas informações irão sobrepor os dados configurados no campo **"Nome arquivo"** da tela [Configuração Arquivo de Remessa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110273).

**Importante:** se ao gerar o arquivo de remessa o campo **"Nro máx. p/ seq. remessa alternativa"** da tela [Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas), aba [Intercâmbio Eletrônico de Dados (EDI)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas#abaintercmbioeletrnicodedadosedi) estiver vazio, quando o campo **"Sequência remessa"** (tela Contas) atingir a sequência 999, o sistema irá recomeçar a contagem com o valor 1, o que poderá gerar conflitos.

![Imagem 4: Atualmente, o arquivo de remessa não segue uma regra lógica de ordenação das linhas.](https://ajuda.sankhya.com.br/hc/article_attachments/24076034181655) Atualmente, o arquivo de remessa não segue uma regra lógica de ordenação das linhas.

**Observação:** para gerar o **"Nome do Arquivo"** de remessa automaticamente, dois passos deverão ser seguidos:

- O campo Nome do Arquivo deve estar em branco;
- Na tela Configuração Arquivo de Remessa, o campo "Nome Arquivo" não pode conter informações.

**Nota:** abaixo trouxemos alguns exemplos para a criação de nomes de arquivos gerados:

&pdes('AD\_CONVENIO2','TSICTA','CODCTABCOINT='+&CODCTABCOINT)©(&CODCTABCO,1,5)IF(DHGERMM<10,COPY(DHGERMM,2,1),IF(DHGERMM=10,'O',IF(DHGERMM=11,'N','D')))&DHGERDD.CRM

e
COPY(&CODCTABCO,1,5)IF(DHGERMM<10,COPY(DHGERMM,2,1),IF(DHGERMM=10,'O',IF(DHGERMM=11,'N','D')))&DHGERDD.CRM"

**Observação:** a extensão **".REM"** é padrão para a geração do arquivo de remessa. Caso ocorra a necessidade de alterar a extensão do arquivo, basta acrescentá-la no campo Nome arquivo, na rotina Configuração Arquivo de Remessa.

Através da opção **"Gerar nosso número"**, é possível gerar o **"Nosso Número"** do título, no momento da geração do arquivo de remessa.

Quando marcada, a opção **"Registrar Banco da Conta"** alterará o banco do título de acordo com a conta bancária escolhida na geração. Se estiver desmarcada, o sistema mantém o banco informado no título, alterando apenas a conta bancária da geração.

Referente à marcação **"Gerar linha digitável"**, pode-se gerar a **"Linha Digitável"** do título, no momento da geração do arquivo de remessa. O sistema só irá gerar a **"Linha Digitável"**, se o **"Nosso Número"** já estiver gerado. Portanto, se o "Nosso Número" não estiver gerado e for necessário gerar a Linha Digitável, na geração do arquivo de remessa, deve-se marcar as duas opções: **"Gerar nosso número"** e **"Gerar linha digitável"**.

**Nota:** quando o Banco da conta for Safra (422) e houver a marcação para Gerar Nosso Número ou a Gerar Linha Digitável, se o parceiro do financeiro estiver com o CEP dentro do intervalo informado na tela de contas, será gerado o nosso número ou a linha digitável de acordo com o banco Safra, se o CEP estiver fora desse intervalo será criado o nosso número ou a linha digitável de acordo com o banco Bradesco (237).

Acesse mais detalhes sobre **"Intervalo de CEPs"** em [Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas), aba [Boleto(s)/Duplicatas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas#ababoletosduplicatas).

**Agrupar Pagamentos:** Quando marcada, agrupará títulos de mesmo **"Parceiro"** e mesmo **"Vencimento"** para a geração do arquivo de remessa. Ao agrupar os títulos, será registrada no **"Financeiro"**, no campo Nosso Número dos títulos agrupados, a informação: **"PG + o Nro. único de um dos títulos"**.

Habilitando a marcação de agrupar pagamentos, a geração do arquivo de remessa só ocorrerá para títulos de despesa, que não estejam baixados e que não possuam o **"Nosso Número"** preenchido com **"PG + o Nro único de um dos títulos"**. Caso alguma dessas situações não sejam satisfeitas, o sistema emitirá uma mensagem de alerta e não fará a geração do arquivo.

**Observação:** quando o Parceiro for Pessoa Física e a marcação Agrupar Pagamentos estiver habilitada, o agrupamento será realizado observando o CPF e não o CNPJ.

Se o processo de geração for interrompido, será necessário inicializar o processo novamente, já que vários títulos poderão ter preenchido o campo Nosso Número durante a corrida. Logo, é preciso que você veja qual título teve problema.

**Importante:** para que o agrupamento dos pagamentos ocorra, é necessário que o parceiro do título seja diferente de "0" (zero) e na aba [Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abaidentificao) do [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros), a opção **"Agrupar Pagamentos na geração p/Banco"** esteja habilitada. Ao efetuar a geração do Arquivo de Remessa de pagamento, efetuando a marcação Agrupar Pagamento e existindo na grade títulos pertinentes à Parceiros que não agrupam (marcação Agrupar Pagamentos na geração p/Banco não realizada), o arquivo será gerado com todos os títulos que se encaixarem nessa situação. É essencial mencionar que os títulos são agrupados se possuírem o mesmo Vencimento, Banco, Agência, Conta, Radical do CGC para Parceiros que permitem agrupamento, além dos títulos que possuem a mesma linha digitável.

**Observação:** considerando que a marcação Agrupar Pagamentos na geração p/Banco esteja acionada, é relevante mencionar que os campos especificados abaixo necessariamente devem apresentar informações idênticas em todos os títulos financeiros a serem agrupados; somente mediante este procedimento, será possível realizar o devido agrupamento de pagamentos na geração de arquivo de remessa. São estes:

- CNPJ / CPF;
- Banco;
- Agência bancária;
- Conta bancária parceiro;
- Nome da agência;
- Dt. Vencimento;
- Vlr Multa;
- Vlr Juros;
- Tipo Juro;
- Tipo Multa;
- Vlr ISS;
- ISS Retido;
- Linha Dig. Receb.

**Nota:** os referidos campos estão vinculados as tabelas **"TGFPAR"** e **"TGFFIN"** localizadas na tela [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294).

Ao efetivar a marcação **"Alterar o tipo de título no financeiro?"**, e selecionar o **"Tipo de Título"**, o título no **"Financeiro"** será alterado pelo escolhido na tela.

Para gerar o arquivo, escolha o **"Layout"**, informe o **"Nome do Arquivo"**, defina a configuração das demais opções comentadas acima e clique em **"Aplicar"**. O sistema exibirá na grade os títulos selecionados de acordo com os filtros. Você pode ainda **"Remover"** títulos para os quais não deseja gerar a remessa, bastará utilizar os botões **"Remover Selecionados"** ou **"Remover não Selecionados"**. Estando na grade apenas os títulos para os quais se deseja gerar a remessa, bastará clicar no botão **"Gerar Remessa"**.

**Observação:** quando você selecionar mais de um registro na grade e clicar em Gerar Remessa, caso algum título possua antecipação não paga, o sistema exibirá um aviso informando quais títulos se encontram nesta situação para que você realize a correção.

Ao confirmar a geração, o sistema apresentará o **"Número da Remessa"** e posteriormente a janela para **"Download"** do arquivo, permitindo que você salve-o onde desejar (a janela de Download será apresentada de acordo com o navegador de internet utilizado).

**Observação:** a extensão **".REM"** é padrão para a geração do arquivo de remessa. Caso ocorra a necessidade de alterar a extensão do arquivo, basta acrescentá-la no campo **"Nome arquivo"**, na rotina [Configuração Arquivo de Remessa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110273).

A marcação **"Utilizar Conta Bancária do Título"** faz com que a conta bancária da rotina seja ou não atualizada, ou seja, quando estiver habilitada, manterá a conta bancária do título.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606914-Gera%C3%A7%C3%A3o-Arquivo-de-Remessa-Configura%C3%A7%C3%B5es#top)

## Geração direta do Arquivo de Remessa

Pelo fato do plugin do Flash não suportar a visualização de vários registros, podendo ocasionar o travamento do sistema na geração do arquivo de remessa do financeiro, o sistema disponibiliza, a partir da versão 3.0, a opção de gerar a remessa em arquivo, sem visualizar os títulos na grade desta tela.

**Importante:** antes de efetuar a atualização do sistema, é necessário configurar no servidor as seguintes alterações:

Setando Transaction Timeout do JBOSS

A partir da raiz do JBoss\server\default\conf\jboss-service.xml:

| 1  2  3  4  5  6 | <mbean code="org.jboss.tm.TransactionManagerService"         name="jboss:service=TransactionManager"         xmbean-dd="resource:xmdesc/TransactionManagerService-xmbean.xml">              <attribute name="TransactionTimeout">10800</attribute>              <!-- ... --> |
| --- | --- |

O padrão é 300, utilizamos 10800 para a Contabilização, a qual também requer mudança do time out do Jape.

A definição do Timeout do Jape é feito via parâmetro, passado para a VM:

Pasta do Jboss\bin\run.bat

JAVA\_OPTS=-Djape.session.timeout=10800000

[GIF animado: Imagem 5: JAVA\_OPTS=-Djape.session.timeout=10800000](https://ajuda.sankhya.com.br/hc/article_attachments/4750058494231)

Depois de efetuadas estas alterações, levantar o servidor:

Na tela Geração Arquivo de Remessa, ao informar os filtros obrigatórios e **"Aplicar"**, o sistema questionará se você deseja aplicar o filtro e visualizar os títulos ou **"Geração direta do arquivo"**.

Se você selecionar a marcação de **"Geração direta do arquivo"**, será gerado o arquivo da remessa, sem que os títulos sejam apresentados na grade.

Se a opção **"Ver os totais antes de gerar o arquivo"**, for selecionada será apresentada, antes da geração, a janela **"Totais geração arquivo"** será exibida, nela teremos:

![Imagem 6: Se a opção "Ver os totais antes de gerar o arquivo" , for selecionada será apresentada, antes da geração, a janela…](https://ajuda.sankhya.com.br/hc/article_attachments/10093281896599)

Se selecionar a marcação de **"Aplicar o filtro e visualizar os títulos"**, o sistema mostrará na grade os títulos provenientes dos filtros selecionados. Se exceder a quantidade de 500 títulos o sistema o questionará se ele deseja ou não visualizar todos, se o parâmetro **"Usar Paginação de registros - USAPAGINACAOREG"** estiver desabilitado.

**Importante:** se solicitado para visualizar todos os títulos e estes excederem mais de 5000 títulos, poderá ocorrer travamento da tela.

Se você selecionar a marcação de **"Geração direta do arquivo"**, será gerado o arquivo da remessa, sem que os títulos sejam apresentados na grade.

**Observação:** uma vez solicitada a geração em arquivo, esta só poderá ser cancelada com o fechamento da tela. Quando a tela estiver em geração não será possível cancelar.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606914-Gera%C3%A7%C3%A3o-Arquivo-de-Remessa-Configura%C3%A7%C3%B5es#top)

## Validação de Arquivo Remessa

Na implantação do Sankhya Om, antes de gerar a primeira remessa e transmiti-la oficialmente para o banco, é necessário validar o **"Arquivo de Remessa"** junto ao banco responsável pela cobrança. O implantador (empresa) deve verificar junto ao banco a rotina para validação deste arquivo.

Geralmente, o banco disponibiliza um ambiente de teste, para que a empresa gere um **"Arquivo de Remessa de Teste"** e o banco possa validá-lo, caso encontre inconsistências no Arquivo de Remessa de Teste, o banco retornará estas inconsistências à empresa, para que sejam corrigidas. Após as correções, gere um novo Arquivo de Remessa de Teste e transmita-o novamente ao banco até que o mesmo valide o arquivo enviado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606914-Gera%C3%A7%C3%A3o-Arquivo-de-Remessa-Configura%C3%A7%C3%B5es#top)

## Botão Outras Opções...

Ao acionar a opção **"Histórico de remessas geradas para download"** localizada no Botão Outras Opções..., você poderá realizar o download de todos os arquivos de remessas após o preenchimento dos filtros **"Conta Bancária"** e **"Período de Geração"** dentro de um período menor que 30 dias no pop-up **"Histórico de remessas geradas para dowload"**.

**Nota:** em uma pasta de Remessa de fácil localização, salve o arquivo com o nome **"arquivosRemessa"** apresentado pelo sistema, sendo este salvo em formato Zip, assim, após localizá-lo realize a extração dos arquivos de remessa que devem ser encaminhados para o banco.

![Imagem 7: Nota: em uma pasta de Remessa de fácil localização, salve o arquivo com o nome "arquivosRemessa" apresentado pelo…](https://ajuda.sankhya.com.br/hc/article_attachments/10093273874967)

Dessa forma, é possível também utilizar os botões **"Remover selecionados"** e **"Remover não selecionados"** para que o download dos arquivos selecionados possam ser executados. Além disso, se o resultado da pesquisa possuir 10 ou mais linhas, estes serão baixados em uma pasta zip no seu computador.

| ![Imagem 8: Dessa forma, é possível também utilizar os botões "Remover selecionados" e "Remover não selecionados" para que o…](https://ajuda.sankhya.com.br/hc/article_attachments/42312360626583) | Caso queira um período filtrado menor que 30 dias, basta informar a quantidade desejada no parâmetro **"Período p/ manter histórico de remessa - MANTHISTREM"**. |
| --- | --- |

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606914-Gera%C3%A7%C3%A3o-Arquivo-de-Remessa-Configura%C3%A7%C3%B5es#top)

## Parâmetros que influenciam a rotina

Quando o parâmetro **"Agrup. titulos receita na geração remessa edi - AGTITRECGERCEDI"** estiver habilitado, ao mandar gerar um arquivo de remessa e por ventura algum título de recebimento fizer parte de um agrupamento de boletos, será gerada apenas uma linha do arquivo de remessa que será enviado para o banco. Esse arquivo irá contemplar a somatória dos valores dos títulos individuais, bem como a somatória dos descontos (quando existirem).

**Nota:** quando o parâmetro Agrup. titulos receita na geração remessa edi - AGTITRECGERCEDI estiver ligado, o sistema estará apto à realizar o processamento de títulos agrupados desde que sejam consideradas as informações contidas no campo NUFIN, campo este que está inserido no layout de retorno e no arquivo de retorno [Processamento do Arquivo de Retorno](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115573). 

**Nota:** o parâmetro acima, é ignorado na geração de arquivos em cobranças do tipo Pix CNAB, ou seja, os títulos não serão agrupados para geração de cobrança nessa modalidade.

Ao receber o arquivo de retorno do banco com apenas uma linha de registro, caso o sistema identifique que o título faz parte de algum agrupamento, será feita a verificação de quais títulos fazem parte do agrupamento, onde estes serão baixados separadamente, e será criada apenas uma movimentação bancária para esse agrupamento.

Habilitando o parâmetro **"Somar (e zerar) taxa ao valor da baixa no ret.banc. - SOMATXVLRBAIXA"**, será realizado o Processamento de Arquivo de Retorno, fazendo com que o sistema some o valor da Taxa Administrativa enviada pelo banco no valor da baixa, nesta situação a soma será feita de forma proporcional.

Se o parâmetro **"Exige Autoriz.Pagto p/remessa de Despesa? - EXIGAUTREMDESP"** estiver habilitado, ao filtrar as **"Despesas"** no campo **"Tipo"** dessa tela, serão apresentados para a geração da remessa apenas os títulos que estiverem totalmente autorizados.

**Nota:** esse comportamento referente ao parâmetro Exige Autoriz.Pagto p/remessa de Despesa? - EXIGAUTREMDESP só está disponível para o layout HTML5.

**Observação:** caso você filtre as **"Receitas"** com o parâmetro acima ligado, serão exibidas todas as receitas para a geração da remessa, independente se estão autorizadas ou não. Se o filtro for feito para **"Ambos"**, será apresentada a mensagem abaixo:

**"Com o parâmetro "Exige Autoriz.Pagto p/remessa de Despesa?" ligado, não é possível gerar a remessa de receitas junto com despesas".**

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606914-Gera%C3%A7%C3%A3o-Arquivo-de-Remessa-Configura%C3%A7%C3%B5es#top)
