---
id: "360045115053"
titulo: "Geração de Lote GNRE"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115053-Gera%C3%A7%C3%A3o-de-Lote-GNRE"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-07-29T14:43:52Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "XML", "Geração de Lote GNRE", "Impostos", "GNRE", "Financeiro", "c39_camposExtras", "br.com.sankhya.geracao.lote.gnre", "Geração de Lote GNRE manual", "Nota Cálculos ST Lote XML", "utomático Portal GNRE Online XML upload/download", "Estados Preferências Empresa Tipos de Título", "USANUPROTAMBIMP", "Documentos Eletrônicos"]
---

# Geração de Lote GNRE

```
 Módulo: Financeiro > Rotinas
```

---

Oprocesso de geração da Guia Nacional de Recolhimento de Tributos Estaduais - GNRE no sistema é automático. Empresas que possuem como procedimento obrigatório, o recolhimento de ST para acompanhamento das notas para vendas fora do estado, que não tenham convênio com estado do destinatário (do cliente), possuem a necessidade de recolher ST (Imposto da Substituição Tributária) através da guia GNRE que acompanha a NF-e.

Hoje, existe um portal chamado **"GNRE Online"**, onde pode ser feito o envio via upload das GNRE's via XML. A geração do arquivo XML possibilita o envio através do portal via upload para que, posteriormente, seja possível atualizar as informações do retorno no financeiro, e consequentemente o pagamento destas. Portanto, as funcionalidades são:

- Geração do XML da GNRE para envio (upload) no site;
- Baixa do XML (Essa opção baixa o XML já gerado);
- Importação de arquivo para pagamento. Essa opção possibilita a importação do arquivo de retorno do site para atualização do código de barras e linha digitável, assim como outros dados possibilitando assim o pagamento via internet banking, entre outros.

| [Configurações para geração da GNRE](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115053-Gera%C3%A7%C3%A3o-de-Lote-GNRE#configura%C3%A7%C3%B5esparagera%C3%A7%C3%A3odagnre) | [Lançamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115053-Gera%C3%A7%C3%A3o-de-Lote-GNRE#lan%C3%A7amento) |
| --- | --- |
| [Geração de lote GNRE](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115053-Gera%C3%A7%C3%A3o-de-Lote-GNRE#gera%C3%A7%C3%A3odelotegnre) | [Botão Novo Lote](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115053-Gera%C3%A7%C3%A3o-de-Lote-GNRE#bot%C3%A3onovolote) |
| [Botão Baixar XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115053-Gera%C3%A7%C3%A3o-de-Lote-GNRE#bot%C3%A3obaixarxml) | [Botão Importar arquivo para pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115053-Gera%C3%A7%C3%A3o-de-Lote-GNRE#bot%C3%A3oimportararquivoparapagamento) |
| [Botão Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115053-Gera%C3%A7%C3%A3o-de-Lote-GNRE#bot%C3%A3ooutrasop%C3%A7%C3%B5es...) | [Geração da GNRE](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115053-Gera%C3%A7%C3%A3o-de-Lote-GNRE#gera%C3%A7%C3%A3odagnre) |
| [Parâmetros que influenciam esta rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115053-Gera%C3%A7%C3%A3o-de-Lote-GNRE#Par%C3%A2metrosqueinfluenciamestarotina) |  |

![Imagem 1: Parâmetros que influenciam esta rotina](https://ajuda.sankhya.com.br/hc/article_attachments/360083746753)

**Nota:** para a geração do XML, os financeiros deverão estar previamente gerados no sistema.

Abaixo, temos uma apresentação da sequência lógica do processo e o comportamento esperado do sistema.

## Configurações para geração da GNRE

**Importante:** antes de prosseguir com a geração do lote, certifique-se de que a guia já possui a respectiva autenticação associada. O sistema exige que a associação da guia (vínculo do comprovante de pagamento ao documento) tenha sido realizada previamente para que a transmissão do lote ocorra com sucesso.

Caso ainda não tenha feito este processo, acesse o guia: [Associar autenticação do DAE e GNRE](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606014-Associar-autentica%C3%A7%C3%A3o-do-DAE-e-GNRE).

![Imagem 2: Na tela de cadastro de Estados , abas Geral e GNRE Unidade Federativa , configure os campos abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/16284344747031) Na tela de cadastro de Estados, abas [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601294-Estados#abageral) e [GNRE Unidade Federativa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601294-Estados#abagnreunidadefederativa), configure os campos abaixo:

- Cód. Parceiro Secretaria da Receita Estadual;
- Código da Receita (GNRE);
- Código Detalhamento Receita (GNRE);
- Código do Produto (GNRE);

![Imagem 3: Para que as tags <receita> e <produto> no XML da GNRE sejam preenchidas corretamente, o sistema verifica os campos…](https://ajuda.sankhya.com.br/hc/article_attachments/26276962628887) Para que as tags **<receita>** e **<produto>** no XML da GNRE sejam preenchidas corretamente, o sistema verifica os campos **"Código da Receita (GNRE)"** e **"Código do Produto (GNRE)"** nas telas abaixo, na seguinte ordem:

1. [Fórmula p/ Parcelas Independentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045912733-F%C3%B3rmula-p-Parcelas-Independentes): o sistema verifica primeiro as informações desta tela, porém elas só serão aplicadas se o usuário utilizar fórmulas independentes no cálculo das parcelas da nota.
2. [Estados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601294-Estados): se não houver dados na primeira tela, o sistema busca as informações configuradas para o respectivo estado.
3. [Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo): por fim, se as informações anteriores não estiverem preenchidas, o sistema utilizará os códigos configurados para o tipo de título.

![Imagem 4: Tipos de Título : por fim, se as informações anteriores não estiverem preenchidas, o sistema utilizará os códigos…](https://ajuda.sankhya.com.br/hc/article_attachments/12723970242711)

**Nota:** a marcação **"Utiliza webservice para GNRE"** deverá ser efetuada para casos em que se utilize o serviço webservice.

---

![Imagem 5: Nas Preferências da Empresa , aba Livros Fiscais , a marcação "Gerar GNRE?" deverá estar realizada para a empresa da…](https://ajuda.sankhya.com.br/hc/article_attachments/16284353113623) Nas Preferências da Empresa, aba [Livros Fiscais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abalivrosfiscais), a marcação **"Gerar GNRE?"** deverá estar realizada para a empresa da nota negociada.

![Imagem 6: Nas Preferências da Empresa , aba Livros Fiscais , a marcação "Gerar GNRE?" deverá estar realizada para a empresa da…](https://ajuda.sankhya.com.br/hc/article_attachments/4414458171031)

Além disso, na aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abapropriedades), os campos abaixo devem estar configurados da seguinte forma:

O campo **"Ambiente p/ GNRE"** com a opção **"Homologação"** ou **"Produção"** selecionada.

A **"Versão GNRE"** deve ser **"2.0"**.

A empresa geradora do GNRE deve ser informada no campo **"Empresa certificado (GNRE)"**.

---

![Imagem 7: Na tela Tipos de Título , aba Geral , os campos "Código da Receita (GNRE)" , "Código Detalhamento Receita (GNRE)" ,…](https://ajuda.sankhya.com.br/hc/article_attachments/16284353118359) Na tela Tipos de Título, aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abageral), os campos **"Código da Receita (GNRE)"**, **"Código Detalhamento Receita (GNRE)"**, **"Código do Produto (GNRE)"** deverão ser preenchidos para a geração do XML da GNRE.

![Imagem 8: Na tela Tipos de Título , aba Geral , os campos "Código da Receita (GNRE)" , "Código Detalhamento Receita (GNRE)" ,…](https://ajuda.sankhya.com.br/hc/article_attachments/4414476158999)

**Observação:** o campo Código da Receita (GNRE) é de preenchimento obrigatório para a geração. Já os campos Código Detalhamento Receita (GNRE) e Código do Produto (GNRE), deverão ser preenchidos de acordo com a necessidade da UF, pois existem UF's como o **"Distrito Federal - DF"** que exigem que estes campos sejam gerados no XML.

O Código Detalhamento Receita (GNRE) trata-se do Código definido pela SEFAZ (Secretaria da Fazenda do Estado), para designar um determinado tipo de pagamento que, neste caso, será referente à GNRE.

O Código do Produto (GNRE) deverá ser informado conforme tabela da SEFAZ/UF, de acordo com a exigência ou não desta.

- Configure o parâmetro **"Tipo de Título p/indicar GNRE p/S.T. - TIPTITGNREST"**, onde você deve informar o tipo de título que caracteriza o financeiro como GNRE.

---

![Imagem 9: Na tela Tipos de Operação - TOP , aba "Validações" , o campo "Gerar GNRE p/ ST" deverá estar marcado para a TOP…](https://ajuda.sankhya.com.br/hc/article_attachments/16284344768151) Na tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba **"Validações"**, o campo **"Gerar GNRE p/ ST"** deverá estar marcado para a TOP utilizada na nota negociada.

---

![Imagem 10: Na tela Observações para Notas , a marcação "Vincular DAE/GNRE" deve estar efetuada para a observação que será…](https://ajuda.sankhya.com.br/hc/article_attachments/16284353122839) Na tela [Observações para Notas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596474-Observa%C3%A7%C3%B5es-para-Notas), a marcação **"Vincular DAE/GNRE"** deve estar efetuada para a observação que será utilizada na nota negociada.

**Observação:** após configurar a observação para a nota, a mesma deverá ser informada no campo Observação Padrão na Central, para que os títulos financeiros sejam apresentados corretamente; caso contrário, o registro não será apresentado na tela.

![Imagem 11: Observação: após configurar a observação para a nota, a mesma deverá ser informada no campo Observação Padrão na…](https://ajuda.sankhya.com.br/hc/article_attachments/4414482697623)

![Imagem 12: Na tela Tipos de Negociação , aba Parcelas , crie duas parcelas, sendo que, a primeira parcela será usada para gerar o…](https://ajuda.sankhya.com.br/hc/article_attachments/16284344773527) Na tela Tipos de Negociação, aba [Parcelas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abaparcelas), crie duas parcelas, sendo que, a primeira parcela será usada para gerar o valor da nota no financeiro. Dessa forma, informe o **"Tipo de Título"** que será utilizado na negociação e escolha a opção **"Usar da TOP"** no **"Tipo de Financeiro (REC/DESP)"**.

A segunda parcela será usada para gerar o valor do GNRE, sendo assim, informe o Tipo de Título que será utilizado na tela [Fórmula p/ Parcelas Independentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045912733). Em **"Natureza da operação"** indique uma natureza para o GNRE que tenha característica de Despesa e no campo Tipo de Financeiro(REC/DES) selecione a opção **"Usar da Natureza Padrão"**.

**Nota:** nessa segunda parcela, o Tipo de Título deve ser informado no parâmetro **"Tipo de Título p/indicar GNRE p/S.T. - TIPTITGNREST"**.

![Imagem 13: Nota: nessa segunda parcela, o Tipo de Título deve ser informado no parâmetro "Tipo de Título p/indicar GNRE p/S.T. -…](https://ajuda.sankhya.com.br/hc/article_attachments/12725685740311)

---

![Imagem 14: Na Alíquota de ICMS , aba Geral , configure a alíquota com uma "Tributação" que não possua relação com Substituição…](https://ajuda.sankhya.com.br/hc/article_attachments/16284344775575) Na [Alíquota de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#abageral), configure a alíquota com uma **"Tributação"** que não possua relação com Substituição Tributária, informe a **"Alíquota"** e a **"Alíquota FCP"**. Além disso, na aba [Substituição Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#abasubstituiotributria), preencha o valor da **"Margem Lucro (MVA)"** e da **"Alíq.Subst. Tributária"**, efetue também a marcação **"Calcula ST extra nota com base em MVA na VENDA"**.

![Imagem 15: Na Alíquota de ICMS , aba Geral , configure a alíquota com uma "Tributação" que não possua relação com Substituição…](https://ajuda.sankhya.com.br/hc/article_attachments/12726676602263)

---

![Imagem 16: Na tela Fórmula p/ Parcelas Independentes , quando o estado for RJ, o sistema irá apresentar dois campos de fórmula; um…](https://ajuda.sankhya.com.br/hc/article_attachments/16284353146007) Na tela [Fórmula p/ Parcelas Independentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045912733), quando o estado for RJ, o sistema irá apresentar dois campos de fórmula; um para informar o valor principal do ICMS e o outro para informar o valor principal do FCP.

![Imagem 17: Na tela Fórmula p/ Parcelas Independentes , quando o estado for RJ, o sistema irá apresentar dois campos de fórmula; um…](https://ajuda.sankhya.com.br/hc/article_attachments/12726620928919)

---

![Imagem 18: Geração da GNRE para CTe](https://ajuda.sankhya.com.br/hc/article_attachments/16284357137687) **Geração da GNRE para CTe**

As configurações realizadas acima também se aplicam para a geração do GNRE para CT-e, porém, com as seguintes modificações:

1. Informe no parâmetro **"Tipo de Título p/indicar GNRE p/ CTE - TIPTITGNRECTE"**, o Tipo de Título que caracteriza o financeiro como GNRE.
2. Depois, na tela [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173), aba [Parcelas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abaparcelas), crie duas parcelas, uma com a fórmula **"VLRCTE"** (esta primeira parcela poderá ter qualquer tipo de título) e a outra com o Tipo de Título informado no parâmetro TIPTITGNRECTE.
3. Agora, na tela [Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#abageral), selecione no campo **"Tributação"** a opção **"90- Outros"**. Nesta mesma aba, preencha a **"Observação"** para nota e habilite a marcação **"ICMS devido à UF de origem da prestação, quando diferente da UF do emitente"**.

Com estas configurações efetuadas, você poderá realizar o lançamento da nota.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115053-Gera%C3%A7%C3%A3o-de-Lote-GNRE#top)

## Lançamento

Realize o lançamento de uma nota contendo Empresa, Parceiro, TOP, Tipo de Negociação e Observação configurados de acordo com as instruções acima. Essa nota deverá gerar dois financeiros, sendo um, o financeiro da nota e o outro, o financeiro da GNRE. Após a confirmação da nota, prossiga com o processo de geração de GNRE em lotes via XML.

O financeiro do título referente à GNRE será gerado seguindo os seguintes cálculos:

```
 (Valor dos produtos + (Valor dos produtos * MVA/100)) = Base de ST
```

```
 (Base de ST * alíquota de ST/100) – Valor do ICMS = Valor do ST
```

Neste caso (seguindo-se as configurações feitas na Alíquota de ICMS), como o ST será gerado na GNRE, o sistema lança um financeiro com o tipo de título de GNRE contendo o valor de desdobramento igual ao valor de ST calculado para o parceiro informado no campo **"Cód. Parceiro Secretaria da Receita Estadual"** no Cadastro de Estados (UF do parceiro da nota).

![Imagem 19: Para os lançamentos manuais, o sistema não gera lote de GNRE.](https://ajuda.sankhya.com.br/hc/article_attachments/26276962628887) Para os lançamentos manuais, o sistema não gera lote de GNRE.

Exemplo:

Um cliente possui uma configuração onde o financeiro não é gerado automaticamente, pois a configuração é destinada apenas à expedição de mercadorias, sendo que o financeiro já foi gerado anteriormente. Neste cenário, ele deseja registrar manualmente a GNRE apenas no financeiro, esperando que esse lançamento permita a geração de um lote. No entanto, o sistema não realiza essa operação devido às diversas configurações que influenciam essa rotina.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115053-Gera%C3%A7%C3%A3o-de-Lote-GNRE#top)

## Geração de Lote GNRE

Nesta tela será possível gerar o XML, baixá-lo e realizar a importação do arquivo. Esta, visa um gerenciamento dos lotes gerados e também de todos os financeiros que compõem o lote. Assim, torna-se possível identificar os financeiros que foram aprovados e os financeiros que foram reprovados.

No lado superior esquerdo da tela, é possível realizar a criação de filtros que serão aplicados às grades para apresentação dos registros de acordo com a necessidade. Além disso, você pode utilizar dos campos **"Período"**, **"Número Lote"**, **"Número Financeiro"** e **"Número Único da Nota"** para filtragem e apresentação de registros mais específicos.

![Imagem 20: No lado superior esquerdo da tela, é possível realizar a criação de filtros que serão aplicados às grades para…](https://ajuda.sankhya.com.br/hc/article_attachments/360083737533)

Na parte superior da tela, temos os botões que irão executar as ações, como gerar Novo Lote, Baixar XML e Importar arquivo para pagamento.

Logo abaixo destes botões, temos a grade que exibirá os lotes gerados de acordo com o filtro definido.

Na grade inferior, serão apresentados os financeiros que fazem parte do lote selecionado na grade superior.

**Nota:** em uma nota de venda que possui ICMS ST extra nota, ocorrerá geração de movimento da GNRE no financeiro; na geração do XML do lote da GNRE, existe a tag **<c39\_camposExtras>**, onde consta a chave de acesso da nota, nos casos em que os parceiros forem dos seguintes estados:

- **AC -** Acre = 076;
- **AL -** Alagoas = 090;
- **AM -** Amazonas = 012;
- **GO -** Goiás = 102;
- **MA -** Maranhão = 094;
- **MS -** Mato Grosso do Sul = 027;
- **PB -** Paraíba= 030;
- **PE -** Pernambuco = 009;
- **RO -** Rondônia = 083;
- **RR -** Roraima = 036;
- **RS -** Rio Grande do Sul = 074;
- **SC -** Santa Catarina = 084;
- **SE -** Sergipe = 077;
- **TO -** Tocantins = 080.

**Observação:** quando existirem UF's com versões diferentes de layout, ao gerar o XML, o sistema irá agrupar as GNRE's com a mesma versão e gerará um XML para cada versão.

**Nota:** existindo na lista de arquivos desta tela, alguma nota com data de pagamento inferior à data atual do servidor, ao gerar um **"Novo Lote"**, o sistema apresentará um alerta questionando se você deseja manter a data que consta no arquivo ou se deseja alterá-la.

**Observação:** quando você preencher os campos **"Tipo de documento"** e **"Tipo da informação"** na tela [Estados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601294-Estados) (abas **"Geral"** e **"GNRE Unidade Federativa"**), os valores inseridos neste serão identificados na Geração do XML da GNRE. Sendo que, a informação a ser preenchida no campo Tipo de documento deve ser aquela que será gerada na tag <**documentoOrigem**> e estar de acordo com a regra de cada Estado.

**Importante:** ao efetuar a geração do lote, se houverem registros sem carimbo no período selecionado será apresentado o aviso:

**"Você possui registros de notas ou financeiras que infringem as regras e condições de uso do Sankhya Om e podem comprometer a integridade e segurança do EIP.**

**Para que as movimentações sejam normalizadas exclua os documentos sem origem reconhecida ou comunique o administrador da aplicação para que o padrão de governança seja seguido"**

Para conferir sobre como corrigir os registros, acesse o artigo [Registros não identificados](https://ajuda.sankhya.com.br/hc/pt-br/articles/15935553131671).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115053-Gera%C3%A7%C3%A3o-de-Lote-GNRE#top)

## Botão Novo Lote

Ao clicar no botão **"Novo Lote"**, o pop-up **"Gerar XML do Lote de GNRE"** será apresentado:

[GIF animado: Imagem 21: Ao clicar no botão "Novo Lote" , o pop-up "Gerar XML do Lote de GNRE" será apresentado:](https://ajuda.sankhya.com.br/hc/article_attachments/360083920394)

**Observação:** as colunas **"Nome + UF (Cidade de Destino)"** e **"Nome + UF (Cidade de Origem)"** são preenchidas com base nas informações dos campos **"Cód. Cid. Fim CT-e"** e **"Cód. Cid. Início CT-e"**, respectivamente, localizados na grade [Cabeçalho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradecabealho) da [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) ao emitir um documento fiscal do tipo CT-e.

É por meio do pop-up Gerar XML do Lote de GNRE que os XML's serão gerados. Porém, apenas financeiros que obedeçam as condições abaixo serão apresentados na mesma.

Premissas:

- Preferências da Empresa, aba Fiscal, campo **"Gerar GNRE p/ST"** marcado;
- Parâmetro do tipo de título TIPTITGNREST informado (código do tipo de título utilizado);
- Ser um documento do financeiro de despesa **TGFFIN.RECDESP = -1**;
- Não ser um documento do financeiro de Provisão **TGFFIN.PROVISAO = 'N'**;
- A nota estar confirmada **= TGFITE.STATUSNOTA = 'L'**;
- A Observação da Nota com a marcação de vincular DAE/GNRE **TGFOBS. VINCDOCARREC = 'S'**.

Ou

```
SELECT

FIN.*

 FROM TGFFIN FIN

 INNER JOIN TGFITE ITE ON(ITE.NUNOTA = FIN.NUNOTA)

 INNER JOIN TGFOBS OBS ON(OBS.CODOBSPADRAO = ITE.CODOBSPADRAO)

 FIN.RECDESP = -1

 AND ITE.STATUSNOTA = 'L'

 AND FIN.CODTIPTIT = :PARAM(TIPTITGNREST)

 AND FIN.PROVISAO = 'N'

 AND OBS.VINCDOCARREC = 'S'

 AND FIN.DHBAIXA IS NULL
```

A consulta acima é o filtro básico para apresentação dos financeiros a serem gerados. O mesmo poderá ser incrementado com as opções de filtros visíveis na tela, como Empresa, Parceiro, Período (Data de vencimento do financeiro), UF (Unidade Federativa) e também ao selecionar a marcação **"Incluir títulos com lote"**, que fará com que títulos que já estejam presentes em outro lote possam ser gerados novamente.

**Observação:** a Observação encontra-se vinculada à Observação registrada no [Cadastro de Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934).

**Nota:** esta observação também deverá ser informada nos Itens e no Cabeçalho da Nota.

É possível também **"Remover Registros Selecionados"** e **"Registros Não Selecionados"**, fazendo com que seja gerado o lote apenas com os financeiros desejados.

**Observação:** através deste botão também será possível gerar o XML da GNRE DIFAL.

Ao tentar gerar o XML sem nenhum financeiro que atenda aos filtros básicos especificados acima, o sistema impossibilitará a geração e a seguinte mensagem de erro será apresentada:

**"Não existem financeiros para serem gerados que obedeçam as condições de filtros incrementados na tela".**

Ao clicar em **"OK"**, será gerado o XML com os financeiros, podendo salvá-los normalmente.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115053-Gera%C3%A7%C3%A3o-de-Lote-GNRE#top)

## Botão Baixar XML

Se o botão **"Baixar XML"** for acionado, o sistema verificará se existe lote selecionado na grade. Caso nenhum lote seja encontrado, a seguinte mensagem será exibida:

**"Nenhum lote foi encontrado para ser baixado".**

Caso um lote esteja selecionado na tela, e você clicar no botão Baixar XML, o sistema irá fazer o download do mesmo, permitindo assim, que este seja salvo na máquina.

Após todo o processo e o retorno atualizado com sucesso, os financeiros envolvidos para as GNRE's terão as informações do código de barras e da linha digitável em seus respectivos financeiros, possibilitando assim, o pagamento destes via processo de integração bancária.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115053-Gera%C3%A7%C3%A3o-de-Lote-GNRE#top)

## Botão Importar arquivo para pagamento

Após a geração do arquivo XML com Lote de GNRE's, o arquivo poderá ser transmitido via upload no portal GNRE online. Feito o processamento do lote no portal, será disponibilizado um arquivo de retorno para o processamento no Sankhya Om.

Com esse arquivo em mãos, você aciona o botão **"Importar arquivo para pagamento"**. Ao acioná-lo, uma tela será apresentada para selecionar o arquivo desejado (no caso o arquivo de retorno que foi baixado do site da GNRE).

![Imagem 22: Com esse arquivo em mãos, você aciona o botão "Importar arquivo para pagamento" . Ao acioná-lo, uma tela será…](https://ajuda.sankhya.com.br/hc/article_attachments/360082567434)

Clicando-se em **"Selecionar Arquivo"**, teremos a seguinte tela:

![Imagem 23: Clicando-se em "Selecionar Arquivo" , teremos a seguinte tela:](https://ajuda.sankhya.com.br/hc/article_attachments/360082567474)

Clicando-se em **"Selecionar o arquivo"**, será aberta uma tela para localização do arquivo na máquina; definindo o arquivo a ser importado, clique no botão **"Enviar"**.

![Imagem 24: Clicando-se em "Selecionar o arquivo" , será aberta uma tela para localização do arquivo na máquina; definindo o…](https://ajuda.sankhya.com.br/hc/article_attachments/360083737833)

Caso o ambiente em que o arquivo foi gerado seja Homologação, será apresentada uma mensagem para que se fique ciente que o registro que está sendo importado, foi gerado em ambiente de teste, sendo esta:

**"O arquivo está sendo importado em ambiente de homologação. Deseja continuar?".**

Caso a opção escolhida seja **"NÃO"**, a importação será cancelada.

Se a opção escolhida for **"SIM"**, a importação prosseguirá. Caso o arquivo ainda não tenha sido importado para o sistema, a importação será realizada e informada no painel de avisos. Neste painel serão informados quantos lotes foram processados, quantos registros foram importados com erro e a quantidade de registros importados com sucesso.

Se o arquivo selecionado já tiver sido importado, ou seja, o lote a ser importado já possuir número de protocolo, a seguinte mensagem será apresentada:

**"Não é possível importar lote de protocolo: xxx. Lote já foi importado!".**

O sistema conta com um recurso que permite a alimentação automática da tela [Obrigações do ICMS e ICMS ST a Recolher](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116133-Obriga%C3%A7%C3%B5es-do-ICMS-e-ICMS-ST-a-Recolher) por meio dos procedimentos realizados na tela Geração de Lote GNRE. Para maiores detalhes sobre este processo, acesse o link [Geração Automática - Obrigações do ICMS e ICMS ST a Recolher](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109513).

**Importante:** ao realizar a emissão da GNRE para os estados da **"Paraíba - PB"**, **"Pernambuco - PE"**, **"Rio Grande do Sul - RS"**, **"Santa Catarina - SC"** e **"Sergipe SE"**, a guia contempla a chave da NF-e, de acordo com a legislação destes Estados. A tag **<codigo>** será alimentada com respectivo código de cada estado. A saber:

- Paraíba = 30
- Pernambuco = 9
- Rio Grande do Sul = 74
- Santa Catarina = 84
- Sergipe = 77

Mesmo que a nota contenha Observação no cabeçalho, caso a UF do Parceiro seja alguma das mencionadas acima, as tag's serão apresentadas juntamente a campos extras da chave da NFe. Abaixo temos um exemplo:

```
<c39_camposExtras>
   <campoextra>
      <codigo>9</codigo>
      <tipo>T</tipo>
      <valor>12839182938928391829389182398129</valor>
   </campoextra>
</c39_camposExtras>
```

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115053-Gera%C3%A7%C3%A3o-de-Lote-GNRE#top)

## Botão Outras opções...

Por meio desse botão, teremos as opções para a geração do Lote GNRE:

![Imagem 25: Por meio desse botão, teremos as opções para a geração do Lote GNRE:](https://ajuda.sankhya.com.br/hc/article_attachments/1500001990642)

**Enviar Lote GNRE:** Utilize essa opção para enviar o lote GNRE. Após o envio, o sistema exibirá um pop-up informando que o lote foi enviado com sucesso; além disso, você poderá consultar a situação e seu status por meio das colunas **"Status do Lote"** e **"Situação atual do Lote"**.

**Nota:** caso o Lote possua algum dos status a seguir, este poderá ser reenviado:

- Processado com pendência;
- Erro no processamento do lote;
- Com erro de Validação;
- Não enviado.

**Observação:** para o Envio do Lote GNRE, é necessário que você preencha o campo **"Empresa certificado (GNRE)"** da tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893) (aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abapropriedades)).

**Consultar status GNRE:** Se o lote for enviado com sucesso, sua situação pode ser consultada por meio desta opção; assim o sistema atualizará o **"Status do Lote"** e **"Rejeições"** e, após a finalizar a operação, você poderá visualizar o pop-up **"Acompanhamentos"**, sendo que, caso houverem rejeições, estas serão apresentadas na grade **"Rejeições por guia"**:

![Imagem 26: Consultar status GNRE: Se o lote for enviado com sucesso, sua situação pode ser consultada por meio desta opção; assim…](https://ajuda.sankhya.com.br/hc/article_attachments/1500001990762)

Uma vez que o Lote foi enviado e processado com sucesso, ao utilizar novamente a opção Consultar Status GNRE, o pop-up Acompanhamentos será exibido para o informar que lote já foi processado.

**Observação:** ao Consultar status GNRE de uma guia de GNRE que foi gerada a partir de um dia após a emissão da nota fiscal e esta guia possuir juros e multa, os valores correspondentes serão incluídos nos campos **"Vlr. Juros"** e **"Vlr. Multa"** presentes na aba [Lançamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874#abalanamento) da Movimentação Financeira.

**Ver acompanhamentos:** Se a geração do Lote já tiver sido realizada, ao clicar nessa opção o sistema exibirá o pop-up Acompanhamentos com as informações exibidas na opção acima.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115053-Gera%C3%A7%C3%A3o-de-Lote-GNRE#top)

## Geração da GNRE

Ao considerar segmentos caracterizados como substitutos tributários, o sistema permitirá que seja realizada a antecipação do recolhimento dos impostos, sendo necessário que as guias de GNRE geradas acompanhem a nota fiscal de venda, para que, desse modo, a mercadoria possa transitar legalmente.

Assim, você pode utilizar na geração da GNRE a opção **"ICMS ST"**, sendo esta, pertinente à pagamentos. Além disso, o sistema também possibilita que seja configurada a opção **"FCP ST"** no processo em referência. Desta forma, as guias mencionadas anteriormente poderão ser geradas unificadas ou separadas.

**Nota:** a geração do tipo de apuração será realizada de maneira automática na tela Obrigações do ICMS e ICMS ST a Recolher nos impostos listados no campo **"Tipo Apuração"** quando o lote GNRE estiver com o Status do Lote **"Lote processado com sucesso"**.

![Imagem 27: Para saber mais sobre, acesse o artigo Geração Automática - Obrigações do ICMS e ICMS ST a Recolher .](https://ajuda.sankhya.com.br/hc/article_attachments/21710090565911) Para saber mais sobre, acesse o artigo [Geração Automática - Obrigações do ICMS e ICMS ST a Recolher](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109513).

- **Guias Unificadas**

No processo de geração de guias unificadas, será necessário apenas criar o título para a GNRE conforme a tela [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o).

- **Guias Separadas**

É relevante mencionar que alguns Estados exigem que as guias (ICMS ST / FCP ST) sejam recolhidas separadamente, portanto, para atender à essas determinâncias, haverão alterações nos registros C100, C112 e C190 pertinentes à tela [EFD - Escrituração Fiscal Digital - ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607614).

Quando considerada a emissão de guias separadas, você deverá preencher os campos **"Tipo de Título p/ indicar GNRE p/ FCP S.T."** e **"Código da Receita (GNRE) p/ FCP ST"** (tela [Estados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025390853-Estados), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025390853-Estados#abageral)). Após esse procedimento, será gerado o registro C100, sendo que para cada GNRE (ICMS ST / FCP ST) será necessário gerar também dois registros no C112, desse modo, serão devidamente consideradas as mercadorias transitadas legalmente.

**Nota:** é indispensável que os campos destacados acima estejam configurados, para que assim, o sistema identifique suas respectivas informações e proceda com a geração da guia GNRE ao considerar o tipo de título para gerar o financeiro.

O cálculo do valor do desdobramento do financeiro considera o parâmetro **"Tipo de Título p/indicar GNRE p/S.T. - TIPTITGNREST"** e os registros contidos no campo **"Tipo de Título"** ([Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas), grade [Rodapé](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#graderodap), aba [Financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#abafinanceiro)). Desse modo, considere os seguintes pontos:

1. A chave de parâmetro TIPTITGNREST tem influência nessa rotina, uma vez que suas configurações se referem ao código do tipo de título que representa as movimentações com a Guia Nacional de Recolhimento Estadual - GNRE.
2. Sobre a geração do GNRE, nos casos em que o tipo de título do financeiro considerado, seja o tipo de título da UF do parceiro, a receita será o código do campo **"Código da Receita (GNRE) p/FCP ST"** no arquivo XML. Caso contrário, seguirá a regra já existente.
3. Com relação ao EFD Fiscal, ao gerar o registro C112, serão considerados também os financeiros cujo tipos de títulos forem iguais ao Tipo de Título p/indicar GNRE p/ FCP ST da UF do parceiro da nota.

**Importante:** após considerar as informações mencionadas nesta tela, bem como, suas configurações gerais para a efetiva Geração de Lote GNRE, é relevante mencionar que é importante realizar a Geração GNRE e o Processamento de Lote por meio do [Portal GNRE](http://www.gnre.pe.gov.br/gnre "http://www.gnre.pe.gov.br/gnre").

**Nota:** para operações que geram o financeiro, é necessário que as configurações a seguir sejam efetuadas:

- Habilite o parâmetro **"Hab. opç. que perm. fin. menor que o vlr. da nota - HABOPCFINMENNOT"** para que a marcação **"Permite financeiro menor que o valor total da nota"** da [TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [Financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abafinanceiro)possa ser habilitada.
- Na tela Tipos de Operação - TOP, selecione a opção para atualização no financeiro, e acione a marcação Permite financeiro menor que o valor total da nota, para que assim, a nota possa ser gerada no financeiro.
- Crie um novo [Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o) com uma única parcela de 100% com a fórmula do GNRE ST ou DIFAL para que seja gerado a parcela.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115053-Gera%C3%A7%C3%A3o-de-Lote-GNRE#top)

## Parâmetros que influenciam esta rotina

**Usa núm de prot. e tp de amb. da import. do txt. - USANUPROTAMBIMP:** ao ser ativado, este parâmetro recupera o número de protocolo do arquivo importado nas posições (17,30). Quando desativado, o número de protocolo é recuperado das posições (17,26).

Além disso, com o parâmetro ativado, o número do ambiente de importação é recuperado na posição (31,31). Quando desativado, essa informação é obtida na posição (27,27).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115053-Gera%C3%A7%C3%A3o-de-Lote-GNRE#top)
