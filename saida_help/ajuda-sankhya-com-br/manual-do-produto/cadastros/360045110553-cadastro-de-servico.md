---
id: "360045110553"
titulo: "Cadastro de Serviço"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o"
trilha: "Manual do Produto > Configurações e Cadastros > Cadastros"
atualizado_em: "2026-09-28T11:25:28Z"
rotulos: ["Produtos", "Promoção", "manual", "Configuração", "Serviço", "Parceiro", "VLRCALIRRF", "Gerente", "Desconto máximo", "Serviços", "Impostos", "Vendas", "Apontamentos", "Preço", "Componentes", "Comissão", "Consultiva", "Controle de estoque", "Curinga", "Desconsiderar", "Disponibilidade diária", "Faturamento de Contrato", "Kits", "Perfil de Consumo", "SubOS", "br.com.sankhya.core.cad.servicos", "Serviço manual", "Venda", "Cadastro de Serviços: Gerenciando Prestações de Serviços"]
---

# Cadastro de Serviço

```
 Módulo: Configurações > Cadastros > Produtos
```

---

Esta rotina é semelhante à tela de [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos), mas existem algumas particularidades que são específicas para se trabalhar com prestação de serviços.

Através do campo **"Código"** insira um código único para cada serviço cadastrado. Seu preenchimento pode ser manual ou automático, conforme a opção **"Numeração"** do botão **"Configuração da tela"** presente no topo da tela. O referido código também pode ser utilizado para realizar a consulta dos serviços já cadastrados por meio do assistente de pesquisa **"Pesquisar"**.

O campo **"Descrição"** tem seu preenchimento obrigatório, o mesmo é utilizado para inserir a descrição do serviço que está sendo cadastrado.

A marcação **"Ativo"** tem a funcionalidade de indicar que o atual serviço está disponível para ser comercializado.

O campo **"Data de Alteração"** será preenchido automaticamente indicando a data e a hora em que o serviço foi cadastrado ou alterado pela última vez.

| Funcionalidades da tela | |
| --- | --- |
| [Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abageral) | [Aba Status SubOS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abastatussubos) |
| [Aba Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abavenda) | [Aba Alíquotas de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaalquotasdeiss) |
| [Aba Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos) | [Aba Motivo SubOS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abamotivosubos) |
| [Aba Ordem de Serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaordemdeservio) | [Aba Controle de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abacontroleestoque) |
| [Aba Apontamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaapontamentos) | [Aba Componentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abacomponentes) |
| [Aba Outros Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaoutrosimpostos) | [Aba Disponibilidade diária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abadisponibilidadediria) |
| [Aba Perfil de Consumo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaperfildeconsumo) | [Aba Configurações por Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaconfiguraesporempresa) |
| [Aba Múltiplos Componentes...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abam%C3%BAltiploscomponentesdeservi%C3%A7o) | [Parâmetros que influenciam nesta rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#parmetrosqueinfluenciamnestarotina) |

### Aba Geral

![Imagem 1: Aba Geral](https://ajuda.sankhya.com.br/hc/article_attachments/9786101389207)

Por meio do campo **"Complemento"** informe qualquer informação a mais sobre o serviço. Configure a descrição deste campo configurando o parâmetro **"Descrição para Complemento - DESCRCOMPL"**.

Selecione no campo **"Grupo"** o nome do grupo que este serviço está inserido. O Grupo de Produtos/Serviços deve ser previamente cadastrado na tela [Cadastros de Grupos de Produtos/Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598294-Grupos-de-Produtos-Servi%C3%A7os).

Indique a unidade de medida que será utilizada para medir o serviço executado através do campo **"Unidade Padrão"**. As Unidades deveram ser antecipadamente cadastradas na rotina [Unidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597094-Unidades), temos abaixo alguns exemplos de unidades:

- Horas;
- Minutos;
- Dias.

Utilize o campo **"Parceiro Fornecedor Preferencial"** para informar o parceiro que tem preferência em fornecer o serviço que está sendo cadastrado. A informação deste campo será usada para geração de pedidos.

Informe no campo **"Referência do Fornecedor"** o código de referência do serviço. Normalmente informado pelo fornecedor, este corresponde ao código de cadastro do serviço na base de dados do fornecedor.

O código de referência do serviço é apontado no campo **"Referência"**, sendo que este código pode ser utilizado para código de barras.

O campo **"Localização"** será preenchido com o local onde o serviço será realizado, por exemplo, oficina.

No campo **"Seleção"** será apontada a classificação dos serviços em categorias, como por exemplo, A, B, C.

O tempo previsto para a execução do serviço é informado no campo **"Tempo Estimado"**.

As especificações do serviço são preenchidas no campo **"Características"**.

Quando marcada a opção **"Desconsiderar nos result. venda consultiva"**, o serviço selecionado não será considerado nos resultados apresentados na tela [Dashboard de resultados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604794-Dashboard-de-Resultados). Além de não serem exibidos os eixos dos gráficos, o mesmo irá ocorrer com os resultados referentes ao serviço marcado, ressaltando que as informações relacionadas a etapa de **"Suspects"** não serão apresentadas.

Por meio da opção **"Excluir do processo de conferência"** indicaremos que o serviço não deve fazer parte do processo de conferência.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#top)

### Aba Venda

![Imagem 2: Aba Venda](https://ajuda.sankhya.com.br/hc/article_attachments/9786105685527)

Através da opção **"Promoção"** definiremos se o serviço está ou não em promoção, sendo que ao marcar esta opção será suspensa a validação de desconto máximo.

Informe o percentual máximo de desconto permitido sobre o valor da prestação do serviço através do campo **"% Desconto máximo"**.

Quando o campo % Desconto máximo do cadastro de serviços estiver preenchido, ao se efetuar uma venda, se o usuário informar um percentual de desconto maior do que o configurado o comportamento dependerá do parâmetro **"Valida desconto máximo - VALDESCMAX"**, de acordo com as respectivas opções abaixo:

**NÃO VALIDA:** Com está opção configurada, o sistema não fará a validação permitindo lançar a nota de venda com **"% Desconto"** maior do que o **"% Desconto máximo"** cadastrado;

- **VALIDA E ACEITA:** O sistema validará, e se o **"% Desconto"** informado for maior do que o **"% Desconto máximo"** o sistema gerará um alerta para o usuário, porém permitirá lançar a nota sem liberação de limites;
- **VALIDA E NÃO ACEITA:** Através desta opção o sistema validará, e se o **"% Desconto"** informado for maior do que o **"% Desconto máximo"** o sistema solicitará a Liberação de Limites, independente de estar em promoção ou não;
- **VALIDA E NÃO ACEITA (EXCETO PROD. PROMOCAO):** O sistema validará, e se o **"% Desconto"** informado for maior do que o "% Desconto máximo" o sistema verificará se o serviço está em Promoção, se estiver, aceitará lançar a nota sem liberação de limites, se não estiver será solicitada a liberação de limites;
- **VALIDA E NAO ACEITA (SOMENTE NA CONFIRMACAO):** Definindo-se o parâmetro com esta marcação, será feita a validação do **"% Desconto máximo"** somente no momento da confirmação. O sistema passará a solicitar o evento **"2 - Desconto Produto"**, que trabalha da mesma maneira que o evento **"25 - Desconto Item"**. Com isso, será necessário configurar para os usuários liberadores, o evento **"2 - Desconto Produto"**.

Caso oserviço pertença a um Grupo de Serviços com descontos promocionais, o referido grupo será indicado no campo "Grupo Desconto".

Por meio da marcação **"Calcular comissão"**, serão definidos quais serviços calcularão Produtividade de OS. Para melhores informações ver documentos de apoio referentes à **"Cálculo de Comissão por OS"**.

A porcentagem da comissão a ser paga para o vendedor do serviço será especificada no campo **"Comissão vendedor"**.

No campo **"Comissão gerente"**, informe a porcentagem da comissão a ser paga para o gerente do vendedor.

No campo **"Moeda p/ preço"**, insira qual será a moeda utilizada para comercialização do serviço. Sendo que, a moeda deverá estar previamente cadastrada na rotina [Valores de Moedas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604754-Valores-de-Moedas).

Através do campo **"Digitação na nota"** aponta-se o modo como o serviço será lançado durante a digitação na nota, de acordo com as seguintes opções:

- **Quantidade -** Digite apenas a quantidade;
- **Valor Unitário -** Pode-se digitar apenas o preço do serviço;
- **Valor Total -** Somente o valor total do serviço poderá ser digitado;
- **Quant. e Valor Unitário -** Poderão ser alterados tanto a quantidade quanto o preço do serviço;
- **Quant. e Valor Total -** Altere a quantidade quanto o valor total do serviço.

Através do campo **"Decimais para o valor"** informe a fração de casas decimais que o sistema irá acolher para os valores do serviço, normalmente esta quantidade é duas para representar os centavos, como por exemplo R$10,55.

A quantidade de casas decimais que o sistema irá aceitar para a quantidade do serviço será descrita por meio do campo **"Decimais para quantidade"**. Vejamos abaixo um exemplo:

Se o serviço for medido em dias, para representar 0,5 dia (meio dia) de serviço, deverá ser cadastrada uma casa decimal para a quantidade.

A fórmula para o cálculo do preço do serviço deverá ser informada no campo **"Fórmula de Precificação"**. A referida fórmula deverá ser cadastrada na rotina de [Fórmulas de Custo/Preço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599874-F%C3%B3rmulas-de-Custo-Pre%C3%A7o)antecipadamente.

A marcação **"Hora Dobrada"** é utilizada tanto para o faturamento, quanto para cálculo de produtividade, pois podem existir serviços que são desenvolvidos internamente na empresa e mesmo que seja realizado fora do horário definido, não será faturado para o cliente com adicional de hora extra. Neste caso, a Produtividade Adicional também não será paga. Esta opção é ativada pelo parâmetro **"Contrato para software? - CONTSOFT"**.

O percentual de margem de lucro que se deseja aplicar será apontada no campo **"% Margem de lucro"**.

O campo **"Agrupamento mínimo"** é utilizado para definir a quantidade mínima de serviços a serem prestados, determinando também que as vendas deverão ser em quantidades múltiplas dele. Vejamos um exemplo:

Serviço: Consultoria - Agrupamento mínimo: 1 (significa que o serviço somente poderá ser realizado, considerando no mínimo uma hora de serviço).

Os três campos apresentados abaixo serão utilizados na questão de análises gerencias, sendo que deverão estar previamente cadastrados em suas respectivas rotinas [Centros de Resultado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606754-Centros-de-Resultado), [Cadastros de Projetos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109073-Projetos) e [Natureza de Receitas e Despesas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas).

No campo **"Centro Resultado"** informe o centro de resultado que será utilizado no serviço.

Por meio do campo **"Projeto"** indique o projeto empregado para o serviço.

A natureza do serviço será descrita através do campo **"Natureza"**.

A opção **"Aceitar venda fora do KIT"** quando marcada permitirá a venda separada de um produto que seja componente de um kit.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#top)

### Aba Impostos

![Imagem 3: Aba Impostos](https://ajuda.sankhya.com.br/hc/article_attachments/18251145985687)

A marcação **"Calcular ICMS"** define se no serviço selecionado irá incidir ICMS (Imposto sobre Circulação de Mercadorias e Serviços, de competência Estadual).

O tipo de tributação do ISS (Imposto Sobre Serviços De Qualquer Natureza) que irá ocorrer sobre o serviço selecionado é apontado por meio do campo **"Tem ISS"**. O referido campo possui as seguintes opções:

- **Isento:** utilizada quando não há o pagamento do imposto;
- **Não tributado:** aplica-se quando não existe a incidência do ISS sobre o serviço prestado;
- **Tributado:** para os serviços onde existe a incidência do ISS sobre o serviço prestado.

A opção **"Tem IRF"** quando marcada determinara que no serviço selecionado ocorrerá a incidência de IRF (Imposto de Renda).

Informe por meio do campo **"% IRF"** o percentual de incidência do IRF sobre o serviço.

No campo **"% Red Base IRF"** informe o percentual que será reduzido na base de cálculo do IR (imposto de Renda). Fato este, por existirem serviços como o de táxi para o qual a legislação prevê redução de base de IR de 40%.

Através da marcação **"Tem INSS"** será indicado a incidência de INSS (Instituto Nacional do Seguro Social) para o serviço selecionado.

O percentual de incidência do INSS sobre o serviço é apontado por meio do campo **"% INSS"**.

No campo **"Tipo de INSS Especial"** insira qual será o tipo de adicional incidente (15, 20 ou 25 anos), além da sua alíquota adicional do INSS no campo **"% INSS Especial"** para que, assim, seja considerado no cálculo do item na nota ou no financeiro.

No campo **"% Red Base INSS"** especificaremos o percentual ao qual deverá ser deduzido na base de cálculo do INSS. Derivando-se da existência de serviços como o de tradução, para o qual a legislação prevê redução de base de INSS de 20%.

Quando o parâmetro **"Calcular Funrural no lugar de INSS? - TEMFUNRURAL"** estiver habilitado, os campos **"Tem INSS"**, **"% INSS"** e **"% Red Base INSS"** não serão apresentados. No lugar destes campos, serão disponibilizados os campos **"Calcular FUNRURAL"**, **"% Funrural"** e **"% Red.Base Funrural"**. Vejamos a funcionalidade de cada um deles:

Por meio da marcação **"Calcular FUNRURAL"** defina a incidência do FUNRURAL (Fundo de Assistência ao Trabalhador rural) sobre o serviço.

No campo **"% FUNRURAL"** informe qual será o percentual do FUNRURAL à recair sobre o serviço.

O campo **"% Red Base FUNRURAL"** tem a funcionalidade de indicar o percentual que deverá ser reduzido na base de cálculo do FUNRURAL, pois existem alguns serviços que a legislação prevê uma na redução de base calculo do imposto.

```
 Cálculo do FUNRURAL:

Caso seja necessário calcular este imposto na empresa, deve-se realizar as seguintes
configurações:

1) Habilitar o parâmetro "Calcular Funrural no lugar de INSS? - TEMFUNRURAL";

2) No Cadastro de Serviço após a ativação deste parâmetro, configure os campos
"Calcular FUNRURAL", "% Funrural" e "% Red.Base Funrural";

3) No Cadastro do Tipo de Operação - TOP aba "Impostos", marque a opção
"Tem FUNFURAL/INSS";

4) Nas Preferências da empresa aba Propriedades, acione a marcação
"Calcula FUNRURAL/INSS?";

5) No Cadastro de Parceiros aba Fiscal, assinale a opção "Calcula FUNRURAL/INSS".
```

No campo **"Grupo de PIS"** deverão ser vinculados os grupos já cadastrados na tela Alíquotas de PIS. Os referidos grupos serão aplicados no calculo do PIS (Programa de Integração Social) na emissão do documento fiscal.

No campo **"Grupo de COFINS"** cadastre os grupos anteriormente cadastrados na rotina Alíquotas de COFINS. Sendo que, os referidos grupos serão empregados no calculo do COFINS (Contribuição para o Financiamento da Seguridade Social) na emissão do documento fiscal.

Associe os grupos previamente cadastrados na tela Alíquotas de CSLL ao campo **"Grupo de CSLL"**. Estes grupos serão utilizados para o calculo do CSLL (Contribuição social sobre o lucro líquido) na emissão do documento fiscal.

**Nota:** o sistema não permitirá a exclusão de um registro contido nos Cadastros de Alíquotas de PIS, COFINS e CSLL, quando o mesmo estiver vinculado com algum produto ou serviço.

Quando a marcação **"Serviço prestado por terceiro"** estiver acionada, a tag **<ValorTotalRecebido>** será inserida no arquivo XML enviado para a prefeitura e o serviço não irá influenciar no cálculo da tag **<ValorServicos>**. Sendo que, o acionamento desta opção afetará somente as NFS-e de Recife/PE e São Paulo/SP.

A marcação **"Tratar serviço como despesa não tributável no JSON"** habilitada fará com que o serviço daqueles municípios que estiverem com seus códigos configurados no campo **"Texto"** do parâmetro **"CodIBGE municípios p/despesas não tributáveis JSON - MUNDESPNTRIBJSO"** seja tratado no JSON como despesa não tributável.

**Nota:** com a marcação acima habilitada, a marcação **"Enviar itens de NFS-e separados no Json"** da aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abanfs-e) do cadastro da Cidade, não terá funcionalidade para esse serviço.

Quando a opção **"Tem Créd.PIS\COFINS sobre Deprec.mensal"** for acionada, ao se efetuar a entrada de um BEM como **"Imobilizado"**, será gerado o registro F120 correspondente a esta entrada com permissão PIS/COFINS do período correspondente.

O grupo de ICMS que será utilizado como exceção para buscar a alíquota de ICMS é indicado no campo **"Grupo de ICMS 2"**. Este campo tem sua aplicação especifica na configuração das alíquotas de ICMS, quando se fizer necessária à inclusão de um serviço que será envolvido por uma única alíquota, em um grupo específico, deve-se informar neste campo o determinado grupo.

O campo **"Tipo de Serviço"** será utilizado para vincular no serviço selecionado, o código do tipo de serviço que está sendo cadastrado. Este código deverá ser cadastrado previamente na rotina de [Cadastros de Lista de Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599414-Lista-de-Servi%C3%A7os).

**Importante:** o Sistema não permite mais de um serviço com códigos de tipo de Serviço diferentes na mesma nota, pois, o RPS só possui um campo de Código no XML de envio. Ou seja, a nota pode ter muitos serviços lançados, mas todos devem ter o mesmo código de tipo de serviço.

**Nota:** a nota só é enviada e aprovada se os serviços estiverem na mesma lista de serviços e o mesmo código de tributação de município.

Através do campo **"Classificação Cessão de M.d.Obra"**, indica-se qual será a classificação da cessão de mão de obra pertinente ao serviço selecionado.

Por meio do campo **"Obra de Construção Civil"**, pode-se apontar se a empresa em questão participa de uma obra de construção civil mantendo uma empreitada Parcial ou Total;

No campo **"Cód. Trib. Município NFS-e"** é descrito o Código de Tributação do Município. Este código será responsável por identificar no município o serviço a ser utilizado em uma nota fiscal de serviço. Cada cidade possui uma lista de códigos de serviço própria, a mesma deverá ser solicitada na prefeitura de cada uma.

O campo **“Código NBS”** registra o Código da **Nomenclatura Brasileira de Serviços (NBS)**. O preenchimento é essencial para a padronização e a comunicação com o Ambiente Nacional da NFS-e na Reforma Tributária. 

O CNAE (Classificação Nacional de Atividades Econômicas) será apontado por meio do campo **"CNAE"**.

O campo **"Nro do Processo Judicial/Adm (ISS)"** é utilizado especificamente pela prefeitura de Veranópolis/RS. Sua funcionalidade é informar o número de um processo judicial no qual um serviço esteja vinculado.

#### Seção Reforma Tributária

Com a Reforma Tributária (PEC 45/2019) e a iminente adoção do **Padrão Nacional da NFS-e**, o ERP Sankhya e sua integração com o **Nota Gateway** foram atualizados para incluir os novos campos fiscais (**IBS/CBS**, **codigoNBS**, etc.), garantindo a conformidade legal nos prazos estabelecidos.

Essa atualização assegura que a emissão da NFS-e continue simplificada, independentemente da variação dos layouts municipais.

Pensando nisso, utilize o campo **“Código Classificação Tributária Nacional”** para registrar a classificação tributária do serviço. Essa informação faz parte do grupo IBS/CBS e é crucial para o cálculo e a correta aplicação dos novos tributos.

Já o campo **"Código indicador da operação de fornecimento"** define globalmente o indicador da operação para este serviço.

**Dica:** o sistema utiliza este valor caso a aba [**Configurações por Empresa**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaconfiguraesporempresa) esteja vazia. Ele tem precedência sobre o valor configurado na TOP.

No campo **"Modalidade de Prestação"** indique como o serviço é prestado ao tomador no exterior, entre as opções 0 - Desconhecido, 1 - Transfronteiriço, 2 - Consumo no Brasil, 3 - Mov. Temp. Pessoas Físicas e 4 - Consumo no Exterior. A informação é utilizada na emissão da NFS-e Padrão Nacional para tomadores estrangeiros.

Já no campo **"Apoio/Fomento do Prestador"** informe o mecanismo de apoio ou fomento à exportação utilizado pelo prestador, conforme as opções apresentadas no campo.

**Nota:** os dois campos são apresentados vazios por padrão e servem como padrão para as notas do serviço. Eles podem ser sobrepostos pelo [Contrato](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774) ou pelo preenchimento manual na aba [Comércio Exterior da Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#h_01M3KVWJSRXXEXMMJPHNTY2HV6).

Para saber mais, acesse o link [Emissão de NFS-e no padrão nacional para tomadores no exterior](https://ajuda.sankhya.com.br/hc/pt-br/articles/43810824811799).

#### Seção Contabilidade

Os campos **"Conta contábil 1"**, **"Conta contábil 2"**, **"Conta contábil 3"** e **"Conta contábil 4"** tem a funcionalidade de indicar cada conta contábil para efeitos de contabilização.

Existe a possibilidade de criação de campos adicionais para determinar as contas contábeis, elas são criadas a partir da tela [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados), vinculando a tabela **"TGFPRO"** na tabela **"TCBPLA"** através da aba [Ligações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados#abaligaes).

![Imagem 4: Para mais informações acesse o artigo TOP Contabilização , no tópico Contas Flexíveis na Contabilização .](https://ajuda.sankhya.com.br/hc/article_attachments/23602908392599) Para mais informações acesse o artigo [TOP Contabilização](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608174-TOP-Contabiliza%C3%A7%C3%A3o#top), no tópico [Contas Flexíveis na Contabilização](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608174-TOP-Contabiliza%C3%A7%C3%A3o#contasflexveisnacontabilizao).

#### Seção EFD Fiscal/Contribuições/Reinf/Sintegra

O campo **"Código Natureza Rendimento"** buscará o código da natureza de rendimentos da tabela de cadastro natureza de rendimento - TGFNRR para gerar os eventos  do Bloco 4000 da EFD Reinf e seus detalhamentos.

Selecione a **"Tributação IRRF - Exterior REINF"** dentre as seguintes opções:

- 10-Retenção do IRRF - alíquota padrão;
- 11-Retenção do IRRF - alíquota da tabela progressiva;
- 12-Retenção do IRRF - alíquota diferenciada (países com tributação favorecida);
- 13-Retenção do IRRF - alíquota limitada conforme cláusula em convênio;
- 30-Retenção do IRRF - outras hipóteses.

**Observação:** este campo estará habilitado quando a marcação Tem IRF desta mesma aba for efetuada e o seu % IRF estiver preenchido.

Através da marcação **"Enquadrado no Reintegra/Prev."**, indique que o serviço em questão será inserido na geração do [Bloco P](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607674-EFD-Contribui%C3%A7%C3%B5es#geraodoblocop) no [EFD - Contribuições](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607674-EFD-Contribui%C3%A7%C3%B5es). Além de ser utilizada para indicar que o envio do evento R-2055 será realizado na tela [EFD-Reinf](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116553-EFD-Reinf#configura%C3%A7%C3%B5esparaoenviodoeventor-2055).

No campo **"Cód. Atividade CPRB (Reintegra/Prev.)"** aponta-se a atividade a ser relacionada ao serviço na geração do Bloco P no EFD - Contribuições. Esta atividade deverá estar previamente cadastrada na rotina [Cód. Atividades Produtos e Serviços p/ CPRB](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608314-C%C3%B3d-Atividades-Produtos-e-Servi%C3%A7os-p-CPRB). 

No campo **"Conta Contábil para EFD"**, defina qual conta contábil será gerada no [EFD - Contribuições](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607674-EFD-Contribui%C3%A7%C3%B5es). É necessário realizar previamente o cadastro das contas a serem utilizadas através da rotina [Plano de Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116393-Plano-de-Contas).

#### Seção PIS/COFINS/CSLL

Por meio do campo **"Cód. Natureza (PIS/COFINS M410/M810)"** um código específico será associado ao que será utilizado para gerar os valores que irão compor nos registros M410/M810 do EFD - Contribuições.

#### Seção NF-E

Os campos **"% Carga Média Trib. Nacional"**, **"% Carga Média Trib. Federal"** e **"% Carga Média Trib. Estadual"**, são preenchidos com os respectivos percentuais médios de tributação, são informações utilizadas nas configurações pertinentes à [Lei da Transparência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600174-Lei-da-Transpar%C3%AAncia).

Utiliza-se o campo **"Cód. Produto p/ NF-e"** para designar se no lançamento da NF-e, ao inserir um item o sistema vai buscar o código do produto ou a referência cadastrada.

Define-se através do campo **"EAN/GTIN Produto p/ NF-e"**, em qual cadastro o sistema buscará o código para gerar o EAN/GTIN do serviço que será apresentado na emissão da NF-e.

#### Seção ICMS/ST/FUNRURAL/INSS

A utilização do campo **"Tipo de Partilha/Anexo"** se dará para as empresas que utilizarem o regime de tributação Simples Nacional. Vincula-se aqui qual é o tipo de partilha que a empresa prestadora do serviço esta enquadrada. Pode-se definir dentre as seguintes opções:

- Anexo I - Comércio;
- Anexo II -Indústria;
- Anexo III - Rec. de locação de bens/móveis e prest. de serv. não relac. no § 5° - C do art. 18 da Lei;
- Anexo IV - Rec. decorrentes da prest. de serv. relacionados no § 5° - C do art. 18 da Lei;
- Anexo V - Rec. decorrentes da prest. de serv. relacionados no § 5° - I do art. 18 da Lei;
- Serviços de Atividades Físicas, Computação, Adm. e Loc. de Imóveis de Terceiros, Outros;
- Serviços da Atividade Intelectual como Medicina, Consultorias, Engenharia, Outros.

No campo **"Cód. Serviço de Telecomunicação"** indica-se o código de Classificação de serviços de Comunicação e/ou Telecomunicação a ser considerado na geração dos registros D600, D601 e D605 no [EFD - Contribuições](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607674-EFD-Contribui%C3%A7%C3%B5es). Este código deverá ser cadastrado previamente na rotina de [Cadastros de Lista de Serviços de Telecomunicação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112193-Lista-de-Servi%C3%A7os-de-Telecomunica%C3%A7%C3%A3o).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#top)

### Aba Ordem de Serviço

Esta aba possui campos que definem a ligação do **"Serviço"** entre o **"Status de OS"** e o **"Motivo de OS"**, que são utilizados na tela [Ordem de Serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603834-Ordem-de-Servi%C3%A7o).

![Imagem 5: Esta aba possui campos que definem a ligação do "Serviço" entre o "Status de OS" e o "Motivo de OS" , que são…](https://ajuda.sankhya.com.br/hc/article_attachments/9786212829335)

Em relação ao campo Status de OS, quando um registro de serviço for utilizado em uma Ordem de Serviço com esse campo informado, o sistema preencherá automaticamente o campo **"Status OS"** ao encerrar a OS, utilizando a informação deste campo. Caso o campo não esteja preenchido nesta tela (Cadastro de serviço), o sistema manterá o valor já atribuído ao campo Status OS no momento do fechamento da OS.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#top)

#### Aba Apontamentos

Esta aba é habilitada pelo parâmetro **"Fatura Contrato por Peso? - FATCONTPORPESO"**, e está diretamente ligada à rotina de **"Faturamento de Contrato de Locação por Peso/Dia"** do MGE Controle de Serviços.

![Imagem 6: Esta aba é habilitada pelo parâmetro "Fatura Contrato por Peso? - FATCONTPORPESO" , e está diretamente ligada à rotina…](https://ajuda.sankhya.com.br/hc/article_attachments/9786207372183)

Para utilização da referida rotina se faz necessário as seguintes configurações neste cadastro:

- Efetue o lançamento de um **"Serviço Curinga"**.
- Os demais serviços,que serão enviados/locados (remessa/retorno no Portal de Vendas), apontarão para esse Serviço Curinga, através do campo **"Produto/Serviço p/ agrupar apontamento"**. Este produto/serviço irá definir o valor a ser cobrado por peso locado.
- Cadastre os serviços que serão locados lembrando-se de colocar seu **"Peso Bruto"** na aba **"Medidas e Estoque"**, sub-aba **"Medidas"** do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-).

**Observação:** a Rotina **"Faturamento de Contrato de Locação por Peso/Dia"** ainda não está disponível no **Sankhya Om**. Esta aba está diretamente relacionada ao **"Cadastro de Produtos/Serviços"** e podem ser usados em processos específicos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#top)

### Aba Medicamentos

![Imagem 7: Aba Medicamentos](https://ajuda.sankhya.com.br/hc/article_attachments/9786262819223)

Nesta aba informe no **"Cód. ANVISA"** o código do registro que identifica que o medicamento está regularizado junto à ANVISA - Agência Nacional de Vigilância Sanitária.

No campo **"Motivo Isenção Anvisa"** o permitirá discriminar as informações adicionais referentes ao produto que corresponde a um medicamento, conforme detalhes da Anvisa.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#top)

### Aba Outros Impostos

Esta aba é utilizada para especificar os impostos e alíquotas que incidem sobre o serviço que está sendo cadastrado. Os dados aqui inseridos refletem diretamente nos [Cadastros de Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos), e assim vice versa.

![Imagem 8: Esta aba é utilizada para especificar os impostos e alíquotas que incidem sobre o serviço que está sendo cadastrado. Os…](https://ajuda.sankhya.com.br/hc/article_attachments/9786301668247)

Utilize o campo **"Imposto"** para vincular o imposto ao qual irá ocorrer à incidência no serviço selecionado.

No campo **"Redução de Base de Imposto"** informe a redução permitida pela Legislação na base de cálculo para que seja feito o cálculo, quando existente.

O campo **"Alíquota"** será preenchido com o percentual definido pela Legislação para o cálculo do imposto.

Os campos **"Na Nota"**, **"No Financeiro Origem Financeiro"** e **"No Financeiro de Origem Estoque"**, são integrantes da configuração de retenção de impostos por valor mínimo de imposto, ou seja, definem onde será a contenção, soma ou destaque dos impostos considerando o valor destes no Financeiro, destacando-os nos documentos fiscais, de modo que seja possível compensar títulos que possuam impostos a serem retidos, total ou parcialmente.

Estes três campos, são aplicados somente para impostos que possuem a marcação **"Calcular com Base Mensal"** presente nos [Cadastros de Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos).

**Observação:** quando o [Cadastro do Imposto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos) for por base mensal, não será exibida nesta aba a linha do imposto; caso altere para o valor mínimo, a linha será apresentada na grade.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#top)

### Aba Perfil de Consumo

![Imagem 9: Aba Perfil de Consumo](https://ajuda.sankhya.com.br/hc/article_attachments/9786305602327)

Esta aba é utilizada para se especificar o perfil dos consumidores do serviço que está sendo cadastrado. Este cadastro será utilizado na Central de Vendas, sendo uma forma de aumentar as vendas, uma vez que ele irá listar todos os serviços, que um determinado Perfil de Parceiro costuma comprar.

Por exemplo, para um Parceiro com perfil **"Informática"** que deseja contratar a manutenção de suas impressoras, pode-se oferecer vários outros produtos como formatação, recuperação de backups e entre outros, aumentando assim as vendas.

Para se configurar um perfil do parceiro, é necessário que este esteja cadastrado previamente na rotina [Cadastros de Perfil](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110753-Perfil)e o mesmo seja analítico.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#top)

### Aba Múltiplos Componentes de Serviço

Nesta aba será possível cadastrar múltiplos componentes conforme a sua necessidade.

![Imagem 10: Nesta aba será possível cadastrar múltiplos componentes conforme a sua necessidade.](https://ajuda.sankhya.com.br/hc/article_attachments/9786369079959)

Referente ao campo **"Cód. Componente"**, insira o Código do componente que será cadastrado na aba.

O campo **"Tipo de Componente"** dispõe das opções:

- **1 - Gerar Zero:** ao marcar esta opção, na geração do XML do CT-e será gerado o grupo de tags <**Comp**>, na tag <**xNome**> será informado a Descrição do componente de Serviço e a tag <**vComp**> será igual a 0;
- **2 - Gerar Variável:** caso selecione esta opção, na geração do XML do CT-e o sistema irá gerar o grupo de tags <**xNome**>, a Descrição do Componente de Serviço, e na tag <**vComp**> será informado o valor na confirmação do serviço de frete;
- **3 - Gerar Variável Diferente de Zero:** ao que se refere a esta opção, na montagem do XML do CT-e deverá ser gerado o grupo de tags <**Comp**>, o valor informado na confirmação do serviço de frete será informado na tag <**vComp**>, e quando o valor informado for 0 o grupo de tags não deverá ser gerado para este componente.

Referente ao campo **"Vlr. Padrão"**, caso neste seja informado, será sugerido na apresentação do popup da Central após um item ser incluído.

Na grade de itens das [Centrais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110973-Central-Compras-Vendas-Mov-Internas), menu [Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612234-Central-de-Vendas-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es) defina se o pop-up será exibido após salvar o item por meio da opção **"Exibir popup Mult. Comp Após Salvar?"**, caso não haja esta necessidade, a cada item incluso será necessário abrir o pop-up manualmente clicando na opção **"Consultar/Alterar Múltiplos Componentes"**, destaca-se ainda que nesta opção será possível atualizar os valores do componentes.

**Observação:** a opção Consultar/Alterar Múltiplos Componentes será habilitada somente se um item for selecionado.

No referido pop-up, defina o valor do complemento e/ou a exclusão de qualquer um deles, porém não será permitido adicionar um novo componente.

Caso o código de serviço seja atualizado, será necessário preencher os valores do componente referente ao novo serviço que foi informado no item.

Após o XML ser gerado, pode-se identificar os componentes gerados conforme a configuração do tipo do componente.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#top)

### Aba Status SubOS

Nesta aba, especifique qual status estará relacionado ao serviço prestado.

![Imagem 11: Nesta aba, especifique qual status estará relacionado ao serviço prestado.](https://ajuda.sankhya.com.br/hc/article_attachments/9786415144983)

No campo **"Status"** será informado o status cadastrado na tela **Contratos e Serviços > Arquivos > Cadastros > Configurações Ordem de Serviço > Status Sub-OS**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#top)

### Aba Alíquotas de ISS

ISS ou ISSQN é o Imposto Sobre Serviços de Qualquer Natureza de competência dos Municípios e do Distrito Federal, tem como fato gerador a prestação de serviços constantes da lista anexa à Lei Complementar 116/2003, ainda que esses não se constituam como atividade preponderante do prestador. Esta aba permite apresentar as alíquotas de ISS para os diversos serviços e cidades, permitindo inserir, alterar, ou excluir os dados.

![Imagem 12: ISS ou ISSQN é o Imposto Sobre Serviços de Qualquer Natureza de competência dos Municípios e do Distrito Federal, tem…](https://chat.google.com/u/0/api/get_attachment_url?url_type=FIFE_URL&content_type=image%2Fpng&attachment_token=AOo0EEXmqDij6V2oG7oZwNWdnZzAYsfIbIE%2FjIKZbAQ9CGam2HlGUGMyINBU%2Bjxc%2BrnCZk%2FNbGw9Dbo92XylHr2faBI0X0MweLXpWvGmWgdAEwEOooV6dEIoPRoZmv%2BgywR9Hj3lC%2BOzsWNE%2FhBSgflKWh2kQoY73Wjm8cUfjm0eruCu5ovMrAamySUxN4jVXLDPE9xRUFv76Sg%2FjFue8wzHxRomBJlsD0Sl5EA906g94Co4RxPp0MVHOXaM2u6O4FG36G51Epx5f71AB%2F2mMhHkL2wHae%2B0d753D3AJzFPdKpvc%2B%2FTC49yGwPtj82GORjYGnF3%2BZaLlf7pHUOlZodgwpY9BP6AuDLZNfM8EjoXwL1pk%2BL9%2B7sX3VAU%2BVUuAuZBwOQF4Le06CG%2FGsbAElSk1NA6lV6sE1r7EthB4nCHcQovpNldyboMo8BwcewXqRn6vsrCKzBCTqf2jzfcVnohDAHul%2FDOQmZK7%2BTL38RmMu9Xs8T2lJajsv1xOU1NjscH836lW61dyGBZe96LUk1k0QkXVeBej7n1rFOoGeH6MuntdlhifXd3DEK%2FqMcbJBr3wCm%2BKxO7JizVwUb7q&allow_caching=true&sz=w512)

O campo **"Cidade"** será utilizado para indicar o código da cidade em que incidirá o ISS.

Através do campo **"Empresa"** vincule o código da empresa a qual recairá o ISS de acordo com a cidade vinculada.

O percentual de ISS que será calculado na Nota fiscal será informado no campo **"Percentual de ISS"**.

**Nota:** o sistema permite a configuração para aceitar até 5 casas decimais na [alíquota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601014-Al%C3%ADquotas-de-ISS), garantindo precisão no cálculo para municípios específicos. Verifique se o parâmetro **“DECALIQISS - Decimais p/ alíquota de ISS”**está habilitado na tela [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias).

No campo **"Cód. Tributação ISS"** pode-se definir o tipo de código de tributação de ISS por meio das seguintes opções:

- 07 - Não Tributado;
- 06 - Isento;
- 00 - Tributado;
- 01 - Tributado com ISS Retido.

No campo **"Número de identificação do Benefício Municipal"**, informe o código numérico oficial (de até 14 posições) correspondente ao incentivo fiscal concedido pela prefeitura. O preenchimento deste campo atende ao Padrão Nacional (DPS) e garante a geração automática do grupo `beneficioMunicipal` no JSON enviado ao eNotas/NotaGateway.

Caso a legislação do município preveja abatimentos atrelados a este benefício ou ao serviço prestado, utilize o campo **"Perc. de dedução na base do ISS"** para informar o percentual que será reduzido na base de cálculo do imposto.

Através do campo **"Tipo de dedução de base do ISS"**, você especifica como essa dedução será aplicada e apresentada na nota.

(**Nota:** o motor de cálculo do sistema utiliza a combinação destes três campos para calcular a redução exata da base do ISS e gerar as tags de abatimento por valor ou por percentual detalhadamente no arquivo de integração com a prefeitura).

O campo **"Tipo de Serviço"** será utilizado para vincular no serviço selecionado o código do tipo de serviço que está sendo cadastrado. Este código deverá ser cadastrado previamente na rotina de [Cadastros de Lista de Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599414-Lista-de-Servi%C3%A7os).

No campo **"Cód. Trib. Município NFS-e"** é descrito o Código de Tributação do Município. Este código será responsável por identificar no município o serviço a ser utilizado em uma nota fiscal de serviço. Cada cidade possui uma lista de códigos de serviço própria, a mesma deverá ser solicitada na prefeitura de cada uma.

**Observação:** as configurações efetuadas nos campos Tipo de Serviço e Cód. Trib. Município NFS-e terão prioridade na utilização da NFS-e em relação as configurações realizadas nos campos de mesma descrição contidos na aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#top)

### Aba Motivo SubOS

Nesta aba são especificadas as ocorrências vinculadas ao referido serviço por meio do campo **"Ocorrência"**. Sendo que cada uma delas deverá estar previamente cadastradas na rotina de [Cadastro de Ocorrências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044610494-Ocorr%C3%AAncias).

![Imagem 13: Nesta aba são especificadas as ocorrências vinculadas ao referido serviço por meio do campo "Ocorrência" . Sendo que…](https://ajuda.sankhya.com.br/hc/article_attachments/9786493911319)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#top)

### Aba Controle estoque

![Imagem 14: Aba Controle estoque](https://ajuda.sankhya.com.br/hc/article_attachments/9786531853975)

Esta aba contém o painel **"Controle Adicional"**, que possibilita por exemplo a criação de um serviço  e no controle adicional configurar uma **"Lista"** com várias opções de identificação para este serviço, podendo variar seu custo e preço de venda por esse controle. Vejamos abaixo um exemplo:

- Serviço - Hora Técnica;
- Opções configuradas - Consultor, Monitor, Suporte, DBA, Programador, Analista.

O campo **"Controlar por"** apresenta as opções do controle de estoque:

- **Data da validade:** controlado pela data de validade;
- **Número do Lote:** controlado pelo número do lote;
- **Lista:** controlado pela lista de opções;
- **Livre:** terá controle livre;
- **Parceiro:** controlado por parceiro;
- **Série:** controlado pelo número de série;
- **Sem controle adicional:** não haverá controle adicional para o estoque.

Descreva no campo **"Título"** o nome do serviço para identificação no estoque.

Em **"Lista de opções"** insira as opções para identificação do serviço.

Para facilitar o lançamento dos itens nos Pedidos ou Notas, tanto de Compras quanto de Vendas, o sistema preencherá automaticamente o campo **"Vlr. unitário"** localizado no painel **"Itens"** da Nota ou Pedido, assim que for selecionado o Controle adicional, caso este produto o tenha.

Para exemplificar a utilização deste tipo de controle, pode-se imaginar o cadastro do produto Chinelo de Dedo. Dessa forma, o controle será titulado como "Tamanho", e a "Lista de opções" composta com as diferentes numerações de tamanho dos chinelos (34, 35, 37, 40, 42, 44). Sendo assim, no momento da venda/compra, especifica-se qual controle adicional estará sendo comercializado.

O Controle adicional poderá corresponder a um campo contendo todos os controles cadastrados para aquele produto.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#top)

### Aba Componentes

Esta aba ficará disponível quando o parâmetro **"Configuração para Kit Independente - CONFKITIND"** estiver desligado.

![Imagem 15: Esta aba ficará disponível quando o parâmetro "Configuração para Kit Independente - CONFKITIND" estiver desligado.](https://ajuda.sankhya.com.br/hc/article_attachments/9786628739095)

Esta será utilizada para se trabalhar com kit’s, a **"Validação de Componentes"** se dará da seguinte forma:

- **Opcional:** o sistema não fará a validação dos componentes.
- **Obrigatório:** a quantidade de componentes na Nota poderá ser maior ou igual à informada nesta aba.
- **Qtd Iguais:** a quantidade de componentes desta aba, tem que ser igual a quantidade de componentes que tiver na nota.

Indique no campo **"Matéria Prima"** quais serão as produtos que irão compor o kit.

O campo **"Referência (MP)"** será preenchido com a referência da matéria-prima.

Por meio do campo **"Qtd. Mistura"**insira a quantidade de cada produto será integrada ao kit.

No campo **"Unidade"** será descrito qual unidade irá será utilizada de cada produto, como por exemplo em um kit "Cesta Básica" será utilizada a unidade "Pacote" do produto "Macarrão".

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#top)

### Aba Disponibilidade diária

Nesta aba, insira a data e o local onde o serviço estará disponível para o usuário, ou onde e quando será executado. Aqui, também poderemos especificar em quantas horas diárias que o serviço será executado, e a quantidade máxima.

![Imagem 16: Nesta aba, insira a data e o local onde o serviço estará disponível para o usuário, ou onde e quando será executado.…](https://ajuda.sankhya.com.br/hc/article_attachments/9786632924951)

Informe no campo **"Controle"** um código único de controle para cada serviço.

O campo **"Local"** aponta a localidade onde o serviço será executado.

A data a qual o serviço será executado será preenchida no campo **"Data do movimento"**.

No campo **"Disp. diária"** informa-se a hora diária que o serviço estará disponível, ou durabilidade.

Indica-se através do campo **"Disp. diária max."** a quantidade máxima de horas que o serviço poderá ser executado diariamente.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#top)

### Aba Configurações por Empresa

![Imagem 17: Aba Configurações por Empresa](https://ajuda.sankhya.com.br/hc/article_attachments/9786636592151)

No campo **"Empresa"** associe a empresa para o qual o serviço possuirá as próximas configurações. As configurações abaixo afetarão somente a empresa vinculada.

O CNAE (Classificação Nacional de Atividades Econômicas) será apontado por meio do campo **"CNAE"**.

No campo **"Código indicador da operação de fornecimento"** informe a natureza da operação específica para esta unidade. Este campo é a **prioridade máxima** do sistema; se preenchido, ele ignora as configurações globais e da TOP na emissão da NFS-e Nacional.

Utilize o campo **"Tipo de Serviço"** para vincular no serviço selecionado o código do tipo de serviço que está sendo cadastrado. Este código deverá ser cadastrado previamente na rotina de [Cadastros de Lista de Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599414-Lista-de-Servi%C3%A7os).

No campo **"Cód. Trib. Município NFS-e"** é descrito o Código de Tributação do Município. Este código será responsável por identificar no município o serviço a ser utilizado em uma nota fiscal de serviço. Cada cidade possui uma lista de códigos de serviço própria, a mesma deverá ser solicitada na prefeitura de cada uma.

A utilização do campo **"Tipo de Partilha/Anexo"** se dará para as empresas que utilizarem o regime de tributação Simples Nacional. Vincule aqui qual é o tipo de partilha que a empresa prestadora do serviço esta enquadrada. Pode-se definir dentre as seguintes opções:

- Anexo I - Comércio;
- Anexo II -Indústria;
- Anexo III - Rec. de locação de bens/móveis e prest. de serv. não relac. no § 5° - C do art. 18 da Lei;
- Anexo IV - Rec. decorrentes da prest. de serv. relacionados no § 5° - C do art. 18 da Lei;
- Anexo V - Rec. decorrentes da prest. de serv. relacionados no § 5° - I do art. 18 da Lei;
- Serviços de Atividades Físicas, Computação, Adm. e Loc. de Imóveis de Terceiros, Outros;
- Serviços da Atividade Intelectual como Medicina, Consultorias, Engenharia, Outros.

No campo **"Conta Contábil para EFD"**, defina qual conta contábil será gerada no [EFD - Contribuições](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607674-EFD-Contribui%C3%A7%C3%B5es). É necessário realizar previamente o cadastro das contas a serem utilizadas através da rotina [Plano de Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116393-Plano-de-Contas).

Determine no campo **"Enquadrado no Reintegra/Prev."** para quais empresas deseja gerar o registro R2060 do [EFD REINF](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116553) por meio das opções abaixo:

- **Gerar:** ao escolher esta opção com o campo **"Cód. Atividade CPRB (Reintegra/Prev.)"** da aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113#abaimpostos "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113#abaimpostos") preenchido, o sistema irá gerar o registro R2060 do EFD-REINF com as informações cadastradas na rotina Cód. Atividades Produtos e Serviços p/ CPRB. Caso o campo Cód. Atividade CPRB (Reintegra/Prev.) esteja em branco, então o sistema irá verificar o campo **"Código Atividade Reintegra/Prev"** também da aba Impostos e buscará as informações na aba [Reintegra/Prev](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abareintegraprevidncia "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abareintegraprevidncia") do Cadastro de Empresas para gerar o registro R2060.
- **Não Gerar:** selecionando esta opção, o registro R2060 do EFD-REINF não será gerado mesmo se a marcação **"Enquadrado no Reintegra/Prev."** da aba Impostos estiver habilitada.
- **Em branco:** serão verificadas as configurações para geração do registro R2060 somente da aba Impostos.

Os campos **"% Carga Média Trib. Federal"**, **"% Carga Média Trib. Estadual"** e **"% Carga Média Trib. Municipal"** são utilizados para configurar a carga tributária aproximada da NFS-e para a empresa selecionada. Informe valores decimais (valores negativos não são aceitos). Sobre o preenchimento destes campos, considere as seguintes regras:

- **Hierarquia de Busca:** os percentuais definidos nesta aba funcionam como uma configuração prioritária. Caso estejam zerados ou nulos, o sistema buscará a carga tributária configurada de forma geral na aba Impostos deste mesmo serviço.
- **Regime Tributário:** o envio dessas informações no XML/JSON da nota varia conforme o regime da empresa. Se optante pelo **Simples Nacional** (ou Simples Nacional - SubLimite), o sistema somará os três percentuais para compor uma alíquota única. Se for do **Regime Normal**, os valores serão mantidos de forma segregada e detalhada.
- **Múltiplos Itens:** ao emitir uma NFS-e com mais de um serviço, o sistema exige que todos os itens possuam a mesma carga tributária aproximada. Caso haja divergência de percentuais entre os serviços da mesma nota, a geração do lote será bloqueada com a seguinte mensagem de erro: “A nota XXXX possui serviços com percentuais aproximados de tributos diferentes. Os seguintes dados devem ser iguais para todos os serviços da nota: % Carga Média Trib. Federal, % Carga Média Trib. Estadual e % Carga Média Trib. Municipal.”
- **Hierarquia da Carga Tributária (NFS-e):** os campos de Carga Média Tributária configurados nesta aba funcionam como uma regra geral para o serviço. No entanto, se você preencher os percentuais de forma específica na aba **Configurações por Empresa**, o sistema priorizará os valores daquela aba no momento da emissão da nota, ignorando a configuração geral.

O campo Regime esp. tributação ISS (NFS-e) define a regra tributária de forma restrita à natureza do serviço faturado, sobrepondo-se ao perfil do cliente.

**Quando usar:** Utilize quando um serviço específico exigir um regime diferente do padrão (ex: um serviço classificado estritamente como "Ato Cooperado").

**Como funciona:** Selecione a opção correspondente à legislação do serviço:

- Vazio (Padrão: Passa a decisão para o Parceiro/Empresa)
- 0 - Nenhum
- 1 - Ato Cooperado (Cooperativa)
- 2 - Estimativa
- 3 - Microempresa Municipal
- 4 - Notário ou Registrador
- 5 - Profissional Autônomo
- 6 - Sociedade de Profissionais
- 9 - Outros

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#top)

### Parâmetros que influenciam nesta rotina

**Valor mínimo para retenção de IRF - VLRCALIRRF:** através deste parâmetro realiza-se a definição do valor mínimo a ser retido para o imposto IRRF. Por exemplo, uma empresa precisa que o cálculo do IRRF seja feito somente quando o valor do imposto for maior ou igual a R$ 30,00; logo, este valor deve ser informado no parâmetro.

**Utiliza a coluna Controle para controlar o estoque - UTILIZACONTROLE:** este parâmetro influência no funcionamento da aba [Controle estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abacontroleestoque). Caso o mesmo se encontre desligado, não será possível fazer alterações nas opções desta aba, e torna seu funcionamento indisponível. Sendo assim, quando habilitado disponibilizará as opções desta aba para as devidas alterações.

**Atualiza estoque de serviço?’ - ATUALESTSERV:** quando este parâmetro estiver ligado, o sistema irá controlar o estoque de serviços da mesma forma que controla com os produtos. Caso o mesmo se encontre desabilitado, os serviços não terão controle de estoque.

**"Fatura Contrato por Peso? - FATCONTPORPESO":** este parâmetro quando habilitado, disponibilizará a aba [Apontamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaapontamentos).

**Calcular Funrural no lugar de INSS? - TEMFUNRURAL:** quando habilitado, os campos **"Tem INSS"**, **"% INSS"** e **"% Red Base INSS"** presentes na aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos) não serão apresentados. No lugar destes campos, serão disponibilizados os campos **"Calcular FUNRURAL"**, **"% Funrural"** e **"% Red.Base Funrural"**.

**Usar Lista de Serviços de Telecomunicação p/ D510? - USARTGFCITD510:** quando este parâmetro encontrar-se habilitado, o sistema utilizará a informação inserida no campo **"Cód. Serviço de Telecomunicação"** da aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos) desta tela para gerar o **"campo 04 - COD\_CLASS"** do Registro D510 na geração do arquivo [EFD - Escrituração Fiscal Digital - ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607614-EFD-Escritura%C3%A7%C3%A3o-Fiscal-Digital-ICMS-IPI).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#top)
