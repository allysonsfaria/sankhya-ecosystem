---
id: "360044606594"
titulo: "Agendamento de Remessa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606594-Agendamento-de-Remessa"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-09-22T14:33:39Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Agendamento", "Financeiro", "Remessa Bancária", "Agendamento de Remessa", "br.com.sankhya.mgefin.agendador.geracao.remessa.bancaria", "Agendamento de Remessa manual", "Agendamento remessa bancária", "Configuração automática", "Filtros histórico e geração manual", "EDI Bancário"]
---

# Agendamento de Remessa

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312366690071) Módulo: Financeiro > EDI Bancário
```

---

A rotina de Agendamento de Remessa Bancária permite que você configure a geração do arquivo de remessa bancária de forma automática. Esta ferramenta faz muito sentido no cenário de cobranças registradas, visto que é preciso manter os dados de cobrança (boletos) atualizados junto à instituição financeira a qual a empresa pertence. Deste modo, ocorrendo dos dados de pagamento informados pelo cliente estarem diferentes dos dados de cobrança junto ao banco, esta rejeitará o pagamento.

**Nota:** esta rotina é responsável apenas por gerar o arquivo de remessa, conforme definição e filtro de títulos. A função de enviar o arquivo ao banco, continua sendo manual por parte de um responsável ou sua empresa pode optar por adquirir uma aplicação de terceiros denominados VANS (empresas que possuem contrato exclusivo com as instituições financeira).

![Imagem 2: Nota: esta rotina é responsável apenas por gerar o arquivo de remessa, conforme definição e filtro de títulos. A função…](https://ajuda.sankhya.com.br/hc/article_attachments/8495512669591)

O campo **"Código"** poderá ser alimentado de forma manual ou automática; esta definição é feita pelo botão ![Imagem 3: O campo "Código" poderá ser alimentado de forma manual ou automática; esta definição é feita pelo botão "Configuração…](https://ajuda.sankhya.com.br/hc/article_attachments/16343195063959) **"Configuração da tela"** localizado no lado direito do topo da tela. Informa-se neste campo, a numeração identificadora do arquivo.

O nome do agendamento que está sendo criado é indicado por meio do campo **"Descrição"**.

Através da marcação **"Ativa"** você aponta se o agendamento está ativo ou não.

| [Aba Configurações de Remessa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606594-Agendamento-de-Remessa#abaconfiguraesderemessa) |  | [Aba Filtros de Títulos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606594-Agendamento-de-Remessa#abafiltrosdettulos) |
| --- | --- | --- |
| [Aba Histórico de Remessa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606594-Agendamento-de-Remessa#abahistricoderemessa) |  | [Botão Gerar Remessa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606594-Agendamento-de-Remessa#botogerarremessa) |

##

## Aba Configurações de Remessa

Configure nesta aba, os dados pertinentes ao arquivo gerado periodicamente.

![Imagem 4: Configure nesta aba, os dados pertinentes ao arquivo gerado periodicamente.](https://ajuda.sankhya.com.br/hc/article_attachments/8495515768215)

Defina por meio do campo **"Conta Bancária"**, qual será a conta utilizada para gerar o arquivo, sendo que o sistema utiliza a conta como base para geração de alguns dados do arquivo, como, por exemplo, número da remessa, nosso número, linha digitável.

Através do campo **"Layout"**, especifique qual layout deve ser utilizado para a geração do arquivo. Os Layouts disponíveis deverão ser cadastrados na rotina de [Configuração Arquivo de Remessa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110273).

A nomenclatura do arquivo é indicada no campo **"Nome arquivo"**. Localizado ao lado, temos o botão de auxílio para construção do nome do arquivo de forma dinâmica no momento da geração. Ao acioná-lo, é exibido o pop-up **"Construtor Nome Arquivo"** conforme imagem abaixo, que permite elaborar o nome do arquivo por meio de variáveis calculadas durante a geração.

![Imagem 5: A nomenclatura do arquivo é indicada no campo "Nome arquivo" . Localizado ao lado, temos o botão de auxílio para…](https://ajuda.sankhya.com.br/hc/article_attachments/8495572393879)

Ao acionar a marcação **"Usar nome arquivo do layout"**, o arquivo será gerado com o nome definido no layout utilizado. O referido layout é configurado na tela [Configuração Arquivo de Remessa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110273), aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110273-Configura%C3%A7%C3%A3o-Arquivo-de-Remessa#abapropriedades), campo **"Iniciais do arquivo para nome automático"**. Assim, o campo **"Nome arquivo"** será desabilitado e os dados contidos no mesmo ignorados.

O diretório onde serão armazenados os arquivos gerados, deve ser indicado no campo **"Diretório destino"**.

**Importante:** essa rotina utiliza o repositório de arquivos do sistema, então, o diretório especificado neste campo corresponde à um diretório dentro do repositório de arquivos. Dessa forma, sofrendo influência do parâmetro **"Diretório base para o repositório de arquivos - FREPBASEFOLDER"** da seguinte maneira:

- Se o parâmetro estiver preenchido, significa que a raiz do repositório de arquivos será o caminho indicado no mesmo;
- Caso não esteja preenchido, a raiz do repositório de arquivos será um diretório chamado **".sw\_file\_repository"** no diretório home do usuário (<home\_user>\.sw\_file\_repository).

O campo **"Alterar Tipo de Título para"** permite que você defina um novo tipo de título para os títulos que compõem o arquivo gerado, ou seja, ao gerar o arquivo de remessa, o sistema altera o tipo de título original dos títulos para o tipo de título especificado.

Por meio da marcação **"Alterar banco dos títulos para banco da conta"**, temos a funcionalidade de definir que, ao ser gerado o arquivo, seja alterado o banco dos títulos que compuseram a remessa para o mesmo banco da conta da geração.

Para realizar a geração do nosso número dos títulos, ative a marcação **"Gerar nosso número"**.

A geração da linha digitável dos títulos é executada ao acionar a marcação **"Gerar linha digitável"**.

Habilitando a marcação **"Agrupar pagamentos"**, fará com que sejam reunidos os títulos de despesas. Para isto, deverão ser configuradas as premissas abaixo:

- No [Cadastro do Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros), aba [Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abaidentificao), o campo **"Agrupar Pagamentos na geração p/Banco"** deverá estar acionado e o campo **"Banco"** preenchido;
- Os títulos a serem agrupados devem possuir o mesmo parceiro e a mesma data de vencimento;
- Por se tratar do agrupamento de pagamentos, na aba [Filtro de Títulos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606594-Agendamento-de-Remessa#abafiltrosdettulos) desta rotina, o campo **"Receita/Despesa"** deve estar marcado como **"Despesa"**.

No campo **"Intervalo de geração (min)"**, configure o espaço de tempo em minutos ao qual será gerado o arquivo de remessa. O valor informado não pode ser menor ou igual a 0 (zero).

O campo **"Dh. última geração"** exibe o período e horário em que foi efetuada a última geração

Determine nos campos **"Hora inicial p/ envio de remessa"** e **"Hora final p/ envio de remessa"** os períodos de restrição de execução no agendamento de remessa; informe um intervalo de tempo em que o agendamento será executado. A execução do agendamento de remessa não irá acontecer fora do período definido na configuração destes campos. A configuração destes campos visa auxiliar às empresas que trabalham com bancos que recebem as remessas de cobrança até determinada hora do dia, de modo que sejam evitados processamentos com erros.

**Nota:** lembre-se que o horário inicial deve ser menor e o horário final, maior, por exemplo:

Informe no campo Hora inicial p/ envio de remessa o horário às 06:00 da manhã e no campo Hora final p/ envio de remessa, o horário às 23:59 da noite.

Desse modo, o sistema irá utilizar como hora de início, a hora da execução em relação à hora final e inicial.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606594-Agendamento-de-Remessa#top)

## Aba Filtros de Títulos

Nesta aba, configure os filtros para os títulos que deverão fazer parte do arquivo a ser gerado.

![Imagem 6: Nesta aba, configure os filtros para os títulos que deverão fazer parte do arquivo a ser gerado.](https://ajuda.sankhya.com.br/hc/article_attachments/8495598870295)

Através do campo **"Receita/Despesa"**, determine o tipo de movimento do título que irá compor o arquivo.

No campo **"Tipo de Período"** é definido se o período de filtro será baseado na data de negociação ou data de vencimento dos títulos.

Uma vez definido o tipo de período, é necessário que você defina a data inicial e data final baseado na data da geração. Por meio dos campos **"Data atual (-)"** e **"Data atual (+)"** executa-se a referida definição. Sendo que, ao informar o valor 0 (zero), serão utilizados apenas os títulos com a data atual. Trouxemos abaixo um exemplo desta funcionalidade:

Tipo de Período = Vencimento;

Data Atual (-) = 0;

Data Atual (+) = 10;

Data da geração do arquivo = 07/09/2017;

O filtro de títulos irá retornar títulos cuja data de vencimento esteja entre 07/09/2017 e 10/09/2017.

Para que na geração do arquivo sejam utilizados apenas os títulos que contenham o número de remessa vazio ou o nosso número preenchido, acione a marcação **"Títulos com Nro. Remessa vazio"** e **"Títulos com Nosso Número preenchido"**, respectivamente.

A marcação **"Permite provisão"**, quando habilitada, fará com que sejam utilizados títulos de provisão na geração do arquivo.

Você pode ainda, criar um filtro personalizado com configurações específicas, clicando no botão ![Imagem 7: Você pode ainda, criar um filtro personalizado com configurações específicas, clicando no botão "Filtro personalizado" .](https://ajuda.sankhya.com.br/hc/article_attachments/16082081219991) **"Filtro personalizado"**.

**Sub-aba Contas**

Nesta aba, devem ser informadas as Contas Bancárias, caso deseje filtrar títulos para uma conta específica, restringindo assim os títulos que farão parte do arquivo gerado. Caso não seja informada nenhuma conta, não será adicionado o item **"Conta Bancária"** ao critério de filtro da consulta.

**Sub-aba Empresas**

Indique nesta aba as Empresas, caso queira filtrar títulos pertencentes à empresas específicas, limitando assim os títulos que irão fazer parte do arquivo gerado. Ocorrendo de não ser informada nenhuma conta, o item **"Empresa"** não será adicionado no critério de filtro da consulta.

**Sub-aba Tipos de Títulos**

Assinale nesta aba Tipos de Títulos caso pretenda filtrar títulos de Tipos de Títulos específicos, reduzindo assim os títulos que farão parte do arquivo gerado. Na hipótese de não você não informar nenhuma conta, não será adicionado o item **"Tipo de Título"** no critério de filtro da consulta.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606594-Agendamento-de-Remessa#top)

## Aba Histórico de Remessa

Esta aba comporta os registros de histórico com os respectivos dados e a descrição do arquivo gerado.

![Imagem 8: Esta aba comporta os registros de histórico com os respectivos dados e a descrição do arquivo gerado.](https://ajuda.sankhya.com.br/hc/article_attachments/8495800093335)

Através do botão ![Imagem 9: Através do botão "Outras opções" , opção "Manter apenas registros recentes" , você configura a limpeza automática nos…](https://ajuda.sankhya.com.br/hc/article_attachments/16081997762839) **"Outras opções"**, opção **"Manter apenas registros recentes"**, você configura a limpeza automática nos registros de histórico.

Através do parâmetro **"Período p/ manter log de histórico de remessa - PERMANTHISTREM"**, você define em dias, o período ao qual os registros de histórico serão armazenados. Ou seja, definindo o referido parâmetro com valor 10, a limpeza automática será realizada para os arquivos com mais de 10 dias de geração. Mantendo

**Nota:** se o agendamento for desativado e a marcação **"Manter apenas registros recentes"** estiver habilitada, a limpeza automática continuará sendo executada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606594-Agendamento-de-Remessa#top)

## Botão Gerar Remessa

Localizado no topo da tela, o botão ![Imagem 10: Localizado no topo da tela, o botão "Gerar Remessa" desempenha a função de geração do arquivo de remessa bancária de…](https://ajuda.sankhya.com.br/hc/article_attachments/16081878608407) **"Gerar Remessa"** desempenha a função de geração do arquivo de remessa bancária de forma manual.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606594-Agendamento-de-Remessa#top)
