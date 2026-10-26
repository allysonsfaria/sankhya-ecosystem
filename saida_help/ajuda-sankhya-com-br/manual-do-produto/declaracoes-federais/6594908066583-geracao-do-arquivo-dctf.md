---
id: "6594908066583"
titulo: "Geração do Arquivo DCTF"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Escriturações e Declarações   > Declarações federais"
atualizado_em: "2026-09-15T17:35:05Z"
rotulos: ["Configuração", "Livros Fiscais", "Impostos", "Financeiro", "br.com.sankhya.mgeliv.mov.dctf", "Inclui DARF movimentação financeira e códigos de receita", "Processar reprocessar e gerar arquivo .txt com histórico", "Declaração fiscal mensal de tributos e contribuições. Geração do arquivo eletrônico", "DCTF"]
---

# Geração do Arquivo DCTF

```
 Módulo: Livros Fiscais > Conexão           Versão disponível: A partir da 4.13
```

---

A DCTF é uma declaração fiscal obrigatória para diferentes tipos de empresas. A sigla significa Declaração de Débitos e Créditos Tributários Federais e deve ser enviada mensalmente para declarar diversos tributos e contribuições. Assim, através dessa tela você poderá gerar o arquivo eletrônico para entrega da DCTF.

A geração nativa da DCTF tem as vantagens de mais rapidez na geração, conferência e entrega da obrigação e mais confiabilidade nas informações.

**Essa documentação abordará os seguintes tópicos:**

| [Configurações Iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#configura%C3%A7%C3%B5esiniciais) | [Preenchimentos Iniciais na DCTF](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#preenchimentosiniciaisnadctf) |
| --- | --- |
| [Aba Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#abaconfigura%C3%A7%C3%B5es) | [Aba R10 - Débitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#abar10-d%C3%A9bitos) |
| [Aba T9 - Total de Registros](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#abat9-totalderegistros) | [Botões da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#bot%C3%B5esdatela) |

---

### Configurações Iniciais

Para realizar a geração dos registros da DCTF, é necessário que primeiramente você faça algumas configurações nas telas abaixo.

Inicialmente, acesse a tela [Códigos de Receita - DARF](https://ajuda.sankhya.com.br/hc/pt-br/articles/6217174835095-Cadastro-de-Receita-DARF) e faça o cadastro de todos os códigos de receita que serão informados nos financeiros referentes aos DARFs:

![Imagem 1: Inicialmente, acesse a tela Códigos de Receita - DARF e faça o cadastro de todos os códigos de receita que serão…](https://ajuda.sankhya.com.br/hc/article_attachments/6596865225879)

Em seguida, na tela de [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela), pesquise todos os financeiros referentes aos DARFs dos impostos federais que serão informados no arquivo da DCTF. Esses financeiros devem ser informados nos campos **"Período de referência"** e **"Código receita Darf"** da aba [Lançamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#abalanamento):

![Imagem 2: Em seguida, na tela de Movimentação Financeira , pesquise todos os financeiros referentes aos DARFs dos impostos…](https://ajuda.sankhya.com.br/hc/article_attachments/6730757878039)

![Imagem 3: O campo Período de referência deve ser sempre o dia 01 de cada mês, da maneira que é gravado na tela de geração da DCTF…](https://ajuda.sankhya.com.br/hc/article_attachments/16311984652055) O campo Período de referência deve ser sempre o dia 01 de cada mês, da maneira que é gravado na tela de geração da DCTF. Caso queira informar um dia diferente deste, pode-se habilitar o parâmetro **"Permite edição do período de referência na Movimen - EDTPERREFMOV"**

O conteúdo do campo Período de Referência será usado para preenchimento do campo Período de Apuração da sub-aba [R11 - Pagamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#sub-abar11-pagamentos) da aba [R10 - Débitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#abar10-d%C3%A9bitos), que será utilizado no arquivo da DCTF associado a cada tributo do validador. 

Caso o campo Período de Apuração esteja vazio, a data a ser utilizada no registro R11 do arquivo DCTF, será àquela informada no campo Referência do cabeçalho dessa tela.

**Observação:** também pode-se alterar a data a ser levada no arquivo DCTF diretamente no campo Período de Apuração sem que haja a necessidade de ser alterada a data do campo Período de Referência da [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753). 

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#top)

---

### Preenchimentos Iniciais na DCTF

Após cadastrar todos os códigos de receitas utilizados na emissão dos DARFs no recolhimento dos impostos e já terem sido lançados no campo Código receita Darf e informado o período referente ao recolhimento do imposto, podemos dar início à Geração do Arquivo DCTF.

![Imagem 4: Após cadastrar todos os códigos de receitas utilizados na emissão dos DARFs no recolhimento dos impostos e já terem…](https://ajuda.sankhya.com.br/hc/article_attachments/6730774750487)

Informe a **"Empresa"** que será utilizada na geração do arquivo DCTF, sendo que, ela deverá ser a matriz caso haja matriz e filiais.

Defina no campo **"Referência"** o período à que se refere a obrigação.

**Nota:** caso queira uma data diferente do dia 01 do mês, configure-a no campo **"Período de Referência"** da sub-aba [R11 - Pagamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#sub-abar11-pagamentos) da aba [R10 - Débitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#abar10-d%C3%A9bitos), após ligar o parâmetro EDTPERREFMOV.

A marcação **"Retificadora?"** refere-se ao campo **"Tipo de Declaração do layout"**; assim, quando estiver realizada, gravará **"1"** e quando estiver desmarcada gravará **"0"**.

Informe o **"Número do Recibo"** de entrega da DCTF a ser retificada, ou seja, esse campo só estará disponível para edição se a marcação Retificadora? estiver feita.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#top)

---

### Aba Configurações

![Imagem 5: Aba Configurações](https://ajuda.sankhya.com.br/hc/article_attachments/6796915247383)

Nessa aba, temos as seguintes sub-abas:

| [Sub-aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#sub-abageral) | [Sub-aba Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#sub-abaparceiros) |
| --- | --- |
| [Sub-aba Códigos de Receita](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#sub-abac%C3%B3digosdereceita) |  |

---

#### Sub-aba Geral

Nessa sub-aba, faça as configurações que se enquadram com a Empresa selecionada, conforme descrevemos abaixo:

Os campos **"Representante da PJ"** e **"Responsável pelo Preenchimento"** têm a opção de **"Contador"** ou **"Signatário"**. Para utilizar a opção Contador, você deverá cadastrá-lo na aba [Contador](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608114-Empresa#abacontador) da tela [Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608114-Empresa) anteriormente e, para usar a opção Signatário, seu cadastro também deve ser previamente feito na aba [Signatários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608114-Empresa#abasignatrios).

Os campos **"Signatário"** serão habilitados se a opção de mesmo nome for definida nos campos acima mencionados. Além disso, nesse campo serão filtrados apenas os Signatários que estiverem com a marcação **"Responsável Legal da empresa junto a RFB"** da tela Empresa, aba Signatários realizada.

No campo **"Situação da Empresa"** você define uma dentre as opções abaixo:

- Cisão Parcial;
- Cisão Total;
- Extinção;
- Fusão;
- Incorporação / Incorporada;
- Incorporação / Incorporadora;
- Normal.

O campo **"Data do Evento"** será habilitado e de preenchimento obrigatório caso o campo Situação da Empresa for diferente de Normal.

O campo **"Forma de Tributação do Lucro"** tem as seguintes opções:

- Arbitrado;
- Declarante não é Contribuinte do IRPJ;
- Imune do IRPJ;
- Isenta do IRPJ;
- Não preenchido;
- Presumido;
- Real / Estimativa;
- Real / Trimestral;

A **"Qualificação da Pessoa Jurídica"** pode ser:

- Agências de Fomento e demais entidades elencadas no § 1º do art. 22 da Lei nº 8.212/1991;
  Autarquia ou Fundação Pública;
- Cooperativa de Crédito;
- Emp. Pública, Soc. de Economia Mista, demais PJ de que trata o Inc. III Art. 34 Lei nº 10.833/2003;
- Entidade Fechada de Previdência Complementar ou Entid. Aberta de Prev. Compl. (sem fins lucrativos);
- Estado, Distrito Federal, Município ou Órgão Público da Administração Direta;
- Mais de uma qualificação durante o mês;
- PJ em Geral;
- Sociedade Cooperativa;
- Sociedade Cooperativa de Produção Agropecuária ou de Consumo;
- Sociedade Corretora de Seguros;
- Sociedade Seguradora e de Capitaliz. ou Entid. Aberta de Previd. Complementar (com fins lucrativos).

Realize a marcação **"PJ com débitos de SCP a serem declarados?"** apenas se a Empresa PJ tiver débitos de SCP (sociedade em conta de participação) a serem declarados.

Se a Empresa for optante pelo Simples Nacional faça a marcação **"PJ optante pelo Simples Nacional?"**.

Caso a Empresa seja optante pela Contribuição Previdenciária sobre a Receita Bruta, realize a marcação **"PJ optante pela CPRB?"**.

Com a marcação **"PJ inativa no mês da declaração?"** efetuada você informa que a Empresa está inativa no mês da declaração.

O campo **"Critério Rec. Variações Monet. Taxa de Câmbio"** refere-se ao critério de reconhecimento das variações monetárias, dos direitos de crédito e das obrigações do contribuinte, em função da taxa de câmbio. Nesse campo, temos as opções:

- Não preenchido;
- Não se aplica;
- Regime de Caixa;
- Regime de Caixa - Elevada oscilação da taxa de câmbio;
- Regime de Competência;
- Sem alteração do regime.

O **"Regime de Apuração da Contribuição para o PIS/Pasep e/ou da Cofins"** pode ser:

- Cumulativo;
- Não-cumulativo;
- Não-cumulativo e Cumulativo;
- Não preenchido;
- Não se aplica;

O campo **"Situação da PJ no mês da declaração"** tem as opções abaixo:

- PJ foi excluída do Simples no mês da declaração;
- PJ não se enquadra em nenhuma das situações anteriores no mês da declaração;
- PJ teve sua inscrição no CNPJ efetivada ou entrou em atividade no mês da declaração;
- Surgimento de nova PJ em razão de fusão ou cisão no mês da declaração.

Faça a marcação **"Balanço de Redução?"** se a Empresa se encontrar em situação de apresentação de Balanço de Redução.

Se o saldo do débito for dividido em cotas, efetue a marcação **"O saldo deste débito será dividido em quotas?"**.

Escolha se o **"Débito de SCP/INC"** é **"INC"**, **"Não é SCP nem INC"** ou **"SCP"**.

Caso a CPRB tenha que ser enviada na DCTF, realize a marcação **"Enviar CPRB na DCTF?"**.

Sendo a empresa optante pela CPRB, habilite a marcação **"PJ optante pela CPRB?"**.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#abaconfigura%C3%A7%C3%B5es)

---

#### Sub-aba Parceiros

Nessa sub-aba você deve configurar os Parceiros que se referem aos parceiros no financeiro lançado relacionado aos DARFs.

![Imagem 6: Nessa sub-aba você deve configurar os Parceiros que se referem aos parceiros no financeiro lançado relacionado aos…](https://ajuda.sankhya.com.br/hc/article_attachments/6796955812887)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#abaconfigura%C3%A7%C3%B5es)

---

#### Sub-aba Códigos de Receita

Configure aqui todos os Códigos de Receitas que forem utilizados nos financeiros referentes aos DARFs.

**Observação:** caso você queira fazer uma inserção de vários Códigos de Receita de uma só vez, acione o botão **"Inserção em massa"**.

![Imagem 7: Observação: caso você queira fazer uma inserção de vários Códigos de Receita de uma só vez, acione o botão "Inserção em…](https://ajuda.sankhya.com.br/hc/article_attachments/6796946044311)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#abaconfigura%C3%A7%C3%B5es) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#top)

---

#### Aba R10 - Débitos

O Registro R10 será a somatória de todas as despesas por Código de Receita, da(s) movimentação(ões) financeira(s) com as características abaixo:

**(1)** A Data Referência deve estar dentro do período selecionado para geração da DCTF;

**(1)** O Tipo Natureza da Receita/Despesa deve ser Despesa, mesmo que seja uma vinculada à uma compensação de uma Receita e tenha o Parceiro e a Natureza nas configurações da DCTF;

**(1)** O título deve estar baixado;

**(1)** Os Parceiros e as Receitas deverão ser as que estiverem configuradas nas sub-abas [Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#sub-abaparceiros) e [Códigos de Receita](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#sub-abac%C3%B3digosdereceita) da aba [Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#abaconfigura%C3%A7%C3%B5es) da DCTF;

**(1)** Buscar todos os financeiros da empresa indicada e de todas as filiais cuja empresa selecionada seja matriz. Aqui será considerado o CNPJ da matriz.

Quando a marcação **"Digitado"** for habilitada, ao realizar o processamento novamente com os campos preenchidos, as informações destes serão conservadas quando o processamento for finalizado, de forma que nenhum deles será substituído.

**Observação:** a marcação Digitado das sub-abas [R11 - Pagamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#sub-abar11-pagamentos), [R12 - Compensações](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#sub-abar12-compensa%C3%A7%C3%B5es) e [R14 - Suspensões c/ Depósitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#sub-abar14-suspens%C3%B5esc/dep%C3%B3sitos) terão o mesmo comportamento.

![Imagem 8: Observação: a marcação Digitado das sub-abas R11 - Pagamentos , R12 - Compensações e R14 - Suspensões c/ Depósitos…](https://ajuda.sankhya.com.br/hc/article_attachments/6796958867351)

Nessa aba, temos as seguintes sub-abas:

| [Sub-aba R11 - Pagamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#sub-abar11-pagamentos) | [Sub-aba R12 - Compensações](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#sub-abar12-compensa%C3%A7%C3%B5es) |
| --- | --- |
| [Sub-aba R14 - Suspensões c/ Depósitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#sub-abar14-suspens%C3%B5esc/dep%C3%B3sitos) |  |

---

#### Sub-aba R11 - Pagamentos

Será gerado um Registro R11 - Pagamentos a despesa por Código de Receita (vinculado a cada R10 com a mesma Receita) da(s) movimentação(ões) financeira(s) com as seguintes características:

**(1)** A Data Referência deve estar dentro do período selecionado para geração da DCTF;

**(1)** O Tipo Natureza da Receita/Despesa deve ser Despesa que não seja vinculada à uma compensação de Receita;

**(1)** Com a marcação **"Depósito Judicial?"**(tela [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#abageral)) desabilitada;

**(1)** O título deve estar baixado;

**(1)** Os Parceiros e as Receitas deverão ser as que estiverem configuradas nas sub-abas [Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#sub-abaparceiros) e [Códigos de Receita](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#sub-abac%C3%B3digosdereceita) da aba [Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#abaconfigura%C3%A7%C3%B5es) da DCTF;

**(1)** Buscar todos os financeiros da empresa indicada e de todas as filiais cuja empresa selecionada seja matriz.

![Imagem 9: (1) Buscar todos os financeiros da empresa indicada e de todas as filiais cuja empresa selecionada seja matriz.](https://ajuda.sankhya.com.br/hc/article_attachments/6797337777175)

A informação do campo **"Código da Receita do DARF"** será incorporada ao arquivo da DCTF e irá preencher o campo **"Código da Receita"** da aba R10 - Débitos correspondente a cada tributo no validador.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#abar10-d%C3%A9bitos)

---

#### Sub-aba R12 - Compensações

Será gerado um Registro R12 - Compensações a receita por Código de Receita (vinculado a cada R10 com a mesma Receita), da(s) movimentação(ões) financeira(s) com as características abaixo:

**(1)** A Data Referência deve estar dentro do período selecionado para geração da DCTF;

**(1)** O Tipo Natureza da Receita/Despesa deve ser Receita e ter sido lançada em compensação à uma ou mais Despesas, que tenha o Parceiro e a Natureza nas configurações da DCTF e que possua a marcação Depósito Judicial? realizada;

**(1)** O campo **"Nº Processo Administrativo/Judicial"** (tela Movimentação Financeira, aba Geral) deve estar informado e ser uma Receita;

**(1)** O título deve estar baixado;

**(1)** Os Parceiros e as Receitas deverão ser as que estiverem configuradas nas sub-abas [Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#sub-abaparceiros) e [Códigos de Receita](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#sub-abac%C3%B3digosdereceita) da aba [Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#abaconfigura%C3%A7%C3%B5es) da DCTF;

**(1)** Buscar todos os financeiros da empresa indicada e de todas as filiais cuja empresa selecionada seja matriz.

![Imagem 10: (1) Buscar todos os financeiros da empresa indicada e de todas as filiais cuja empresa selecionada seja matriz.](https://ajuda.sankhya.com.br/hc/article_attachments/6797338971415)

**Nota:** Se tratando de Compensação, devem ser lançados os mesmos dados de Código de Receita e Período de referência nos títulos compensados (Receitas e Despesas) que se referem às compensações, bem como informar o nº da DCOMP ou do Processo Administrativo Judicial, quando for o caso. Após a geração desse registro, você deve informar registro por registro o campo **"Formalização do Pedido"** dessa sub-aba.

![Imagem 11: O sistema não contempla compensação entre filias, em que a DCTF esteja sendo gerada pela matriz. Por exemplo: Gerando…](https://ajuda.sankhya.com.br/hc/article_attachments/16311984652055) O sistema não contempla compensação entre filias, em que a DCTF esteja sendo gerada pela matriz. Por exemplo: Gerando DCTF pela Empresa 1 Matriz, mas tem compensação lançada entre as empresas filial 2 e filial 3, essa compensação não será contemplada na geração da DCTF.

**Observação:** caso você faça lançamentos de compensação e informe Código de Receita e Período de referência nos títulos compensados (Receitas e Despesas) que se referem as compensações, poderá ser gerado a parte do débito no R10 e ser gerado a parte da receita no R12, fazendo com que os valores do R10 não sejam a somatória dos registros R11, R12 e R14. Para que isso não aconteça, é necessário observar a regra para a geração do registro R12, ou seja, deverão ser lançados os mesmos dados de Código de Receita e Período de referência nos títulos compensados que se referem as compensações.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#abar10-d%C3%A9bitos)

---

#### Sub-aba R14 - Suspensões c/ Depósitos

É gerado um Registro R14 - Suspensões c/ Depósitos a despesa por Código de Receita (vinculado a cada R10 com a mesma Receita), da(s) movimentação(ões) financeira(s) com as seguintes características:

- A Data Referência deve estar dentro do período selecionado para geração da DCTF;
- O Tipo Natureza da Receita/Despesa deve ser Receita e ter sido lançada em compensação à uma ou mais Despesas, que tenha o Parceiro e a Natureza nas configurações da DCTF e que possua a marcação Depósito Judicial? realizada;
- O campo Nº Processo Administrativo/Judicial deve estar informado e ser uma Despesa;
- O título deve estar baixado;
- Os Parceiros e as Receitas deverão ser as que estiverem configuradas nas sub-abas [Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#sub-abaparceiros) e [Códigos de Receita](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#sub-abac%C3%B3digosdereceita) da aba [Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#abaconfigura%C3%A7%C3%B5es) da DCTF;
- Buscar todos os financeiros da empresa indicada e de todas as filiais cuja empresa selecionada seja matriz.

![Imagem 12: Buscar todos os financeiros da empresa indicada e de todas as filiais cuja empresa selecionada seja matriz.](https://ajuda.sankhya.com.br/hc/article_attachments/6797406995095)

**Nota:** se tratando de Suspensão, devem ser lançados os dados nos títulos que se referem as suspensões, bem como informar o nº do Processo Administrativo Judicial a que se refere, e além dos campos já mencionados, a marcação Depósito Judicial? deve estar realizada.

Após a geração desse registro, você deve informar registro por registro os campos **"Motivo da Suspensão"**, **"Depósito"**, **"Vara"** e **"Identificação do Depósito"** dessa sub-aba e o **"Código de Receita darf"** com o código de receita (DJE) de acordo com a tabela publicada pela RFB **"ATO DECLARATÓRIO EXECUTIVO CODAC Nº 24, DE 13 DE SETEMBRO DE 2016"**.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#abar10-d%C3%A9bitos) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#top)

---

#### Aba T9 - Total de Registros

A **"Quantidade de Registros"** dessa aba é igual ao total de registros R10, R11, R12 e R14.

![Imagem 13: A "Quantidade de Registros" dessa aba é igual ao total de registros R10 , R11 , R12 e R14 .](https://ajuda.sankhya.com.br/hc/article_attachments/6796990316183)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#top)

---

#### Botões da tela

Acione o botão ![Imagem 14: Acione o botão "Processar" para iniciar a geração dos registros na tela:](https://ajuda.sankhya.com.br/hc/article_attachments/26885805662999) **"Processar"** para iniciar a geração dos registros na tela:

![Imagem 15: Acione o botão "Processar" para iniciar a geração dos registros na tela:](https://ajuda.sankhya.com.br/hc/article_attachments/26887246111895)

Caso seja necessário realizar alguma alteração, inclusão ou exclusão, utilize a opção **"Reprocessar totalizadores"** do botão ![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/15524341459479) **"Outras Opções"**:

![Imagem 17: Caso seja necessário realizar alguma alteração, inclusão ou exclusão, utilize a opção "Reprocessar totalizadores" do…](https://ajuda.sankhya.com.br/hc/article_attachments/26887595915159)

Clicando no botão ![Imagem 18: Clicando no botão "Histórico de Gerações" , será apresentado o pop-up "Processos" onde é possível consultar o histórico…](https://ajuda.sankhya.com.br/hc/article_attachments/26885974885911) **"Histórico de Gerações"**, será apresentado o pop-up **"Processos"** onde é possível consultar o histórico de Geração do arquivo DCTF:

![Imagem 19: Clicando no botão "Histórico de Gerações" , será apresentado o pop-up "Processos" onde é possível consultar o histórico…](https://ajuda.sankhya.com.br/hc/article_attachments/26887619946007)

Após concluir as etapas anteriores, o arquivo .txt pode ser gerado. Para isso, clique no botão ![Imagem 20: Após concluir as etapas anteriores, o arquivo .txt pode ser gerado. Para isso, clique no botão "Gerar arquivo" . Uma…](https://ajuda.sankhya.com.br/hc/article_attachments/6796779790743) **"Gerar arquivo"**. Uma mensagem de confirmação será exibida, clicando em **"Sim"**, uma nova janela aparecerá, permitindo acompanhar o progresso da geração do arquivo. Clique em ![Imagem 21: Após concluir as etapas anteriores, o arquivo .txt pode ser gerado. Para isso, clique no botão "Gerar arquivo" . Uma…](https://ajuda.sankhya.com.br/hc/article_attachments/26887495064087) **"Baixar Arquivo"** para fazer o download do arquivo (.zip).

**Observação:** o nome do arquivo será sugerido, contendo CNPJ e o Ano/Mês referentes ao arquivo gerado, por exemplo: **"DCTF\_12345678000199\_202201.zip"**.

O botão **"Gerar Arquivo MIT"** só vai aparecer quando a data do fato gerador for igual ou após 1º de janeiro de 2025. Isso significa que, se a data for anterior a essa, o botão não vai estar disponível no sistema. Quando a geração for permitida, o sistema vai criar automaticamente um arquivo no formato JSON, seguindo o padrão exigido pela Receita Federal. Esse arquivo precisa ser validado. Para realizar a validação acesse o Portal e-CAC utilizando a conta GOV.BR, por meio da opção Declarações e Demonstrativos, em seguida Assinar e Transmitir DCTFWeb, feito isso o MIT estará disponível na tela inicial no canto superior direito Módulo de Inclusão de Tributos.

**Observação**: na tela de [Movimentação Financeira (Seção Geral)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#filtros:~:text=da%20Empresa.-,Se%C3%A7%C3%A3o%20Geral%C2%A0,-O%20campo%20%22), você encontrará a seção **MIT**, que reúne as informações utilizadas na geração do arquivo do Módulo de Inclusão de Tributos. Nela, há o campo **Período de Referência MIT**, onde você deve informar a **data de apuração** à qual o débito específico se refere.

Você deve preencher este campo caso a data de apuração do débito seja diferente da data inicial padrão de geração do arquivo DCTF. Se o campo for deixado em branco, o sistema utilizará automaticamente a data inicial da geração.

O nome do arquivo também será montado automaticamente pelo sistema. Ele será formado pelo CNPJ raiz do contribuinte, que tem 8 dígitos, seguido de “-MIT-”, depois o período da apuração no formato ano e mês (AAAAMM), e por fim, a extensão “.json”. Por exemplo, se o CNPJ for 87654321 e o período de apuração for abril de 2025, o nome do arquivo será **“87654321-MIT-202504.json”**.

É importante saber que o sistema não permite a geração de arquivos JSON com datas de fato gerador anteriores a 1º de janeiro de 2025. Do mesmo modo, a geração de arquivos TXT não será permitida para datas iguais ou posteriores a essa data. Assim, o sistema se adapta automaticamente conforme o período informado, garantindo que os arquivos sejam gerados corretamente.

![Imagem 22: É importante saber que o sistema não permite a geração de arquivos JSON com datas de fato gerador anteriores a 1º de…](https://ajuda.sankhya.com.br/hc/article_attachments/26887420786967)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#top)
