---
id: "38015389196695"
titulo: "Como lançar um CT-e Redespacho"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38015389196695-Como-lan%C3%A7ar-um-CT-e-Redespacho"
trilha: "Universidade Sankhya > Jornada de Distribuição > Jornada de Conhecimento de Transporte Eletronico (CT-e)"
atualizado_em: "2026-07-22T14:02:35Z"
rotulos: ["CT-e", "Fiscal", "Central de Vendas", "Transporte", "Impostos", "Sankhya", "Documentos Eletrônicos"]
---

# Como lançar um CT-e Redespacho

## CT-e Redespacho

O CT-e de Redespacho é utilizado quando uma transportadora contrata outra para executar parte do transporte originalmente contratado. Essa atuação pode ocorrer no início do percurso, levando a mercadoria do remetente até um ponto definido do trajeto, ou no final, conduzindo a carga de um ponto até o destinatário. Ao assumir essa etapa do transporte, a segunda transportadora emite o CT-e de Redespacho, tendo como tomador do serviço a transportadora que a contratou. Esse documento deve fazer referência ao CT-e original e conter corretamente as informações do remetente, do destinatário e do percurso realizado. A emissão correta do CT-e garante a conformidade fiscal da operação, evita cobranças duplicadas de imposto e assegura a rastreabilidade de todo o processo de transporte.

![Imagem 1: O CT-e de Redespacho é utilizado quando uma transportadora contrata outra para executar parte do transporte…](https://ajuda.sankhya.com.br/hc/article_attachments/38015389196439)

#### Cenário de aplicação prática

A Shift Logistica foi contratata para realizar o transporte de 20 unidades de filtro de ar e 10 caixas de peças mecânicas da Dinâmica Peças para a Prumo Comercial, mas realizara somente o trecho entre Curitiba/PR até Gioânia/GO. A Move Transportes irá assumir o trecho final da entrega até o destinatário. Para formalizar essa continuidade do serviço, a Move deve emitir o **CT-e de Redespacho**, documento que registra a participação da segunda transportadora na conclusão do percurso. Esse tipo de emissão é utilizado quando a responsabilidade do transporte é parcialmente transferida, garantindo que cada etapa fique devidamente documentada e em conformidade com a legislação fiscal.

A emissão correta do CT-e de Redespacho no ERP Sankhya assegura a rastreabilidade da carga, evita bitributação entre as transportadoras envolvidas e mantém o controle dos custos, responsabilidades e informações operacionais.

**Tarefa:** assista ao vídeo de demonstração prática e siga o passo a passo para emitir um CT-e de Redespacho, preenchendo os campos obrigatórios e salvando o documento conforme o exemplo apresentado.

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

1. **Para lançar um CT-e Redespacho**

- Acesse a tela **Portal de Vendas**
- **Menu:** Comercial » Consulta » Portal de Vendas
- Acima do menu de filtros, selecione **Conhecimento de Transporte** no campo ”**Tipo** **de Movimento**”.
- Abra as opções de documento clicando na seta ao lado do botão “**+**” (**Novo** **documento**).
- Selecione o tipo de operação **CT-E DE REDESPACHO** com um duplo clique.
  Ao selecionar o tipo de operação, o sistema redirecionará o usuário para a Central de Vendas.
- Preencha as informações essenciais para o lançamento da nota:

**Cabeçalho**

- Empresa - **Transportadora prestadora de serviço**
- Parceiro - **Tomador do serviço de transporte, transportadora que contratou a empresa para realizar o redespacho.** Ex.: Shift Logistica
- Tipo Negociação - **Definido conforme configurações do parceiro tomador mas pode ser editado de acordo com a negociação**
- Produto Predominante - **Descrição que identifique a mercadoria que está sendo transportada**
- Parceiro Remetente - **Parceiro que emitiu as notas fiscais referentes aos produtos que a transportadora está deslocando**
- Parceiro Destinatário - **Parceiro que receberá as mercadorias remetidas pelo parceiro remetente**
- Consignatário (Expedidor) - **Expedidor da mercadoria do CT-e anterior.** Ex.: Shift Logistica
- Redespacho (Recebedor) - **Este campo será preenchido em emissão de Redespacho intermediário**
- Série da nota - **Informe a série definida**
- Lotação - **Marque a opção "Lotação" quando o CT-e caracterizar uma lotação (mercadorias ocuparem todo o espaço do veículo)**
- Veículo de Tração - **Veículo de tração que realizará o transporte da mercadoria. Se possuir reboque, deve preencher os campos: "Reboque 1", "Reboque 2" e "Reboque 3"**
- Previsão de entrega - **Data prevista da entrega da mercadoria ao destinatário**
- Cód. Cid. Inicio CT-e: **cidade de Origem do CT-e.** Ex.: Goiânia/GO
- Cód. Cid. Fim CT-e - **cidade de Destino do CT-e.**
  **Observação:**
  **Se o local de entrega coincidir com o endereço do Parceiro Destinatário, o preenchimento não é necessário.**
  No caso de lançamento de CT-e de Terceiros, as cidades de início e fim devem ser obrigatoriamente preenchidas
- Centro Resultado - **Defina o responsável pela receita emitida**
- Natureza - **Informe a classificação da receita emitida**
- Salve o registro.

**Itens**

- Informe o código do serviço prestado no campo “**Produto**”.
- Determine a quantidade e valide o valor unitário.
- Salve as informações.

**Aba Rodapé**

Valide as informações das abas apresentadas:

**Aba Impostos** 

- Confira a incidência dos impostos.
  Os dados nesta aba são reflexos das configurações realizadas no Serviço/Produto, Empresa/Parceiro e alíquotas de impostos.

**Aba Unidades de Medida**
Nesta aba, obrigatoriamente, você deverá informar quais as unidades de medida das mercadorias em transporte. Um mesmo documento pode possuir mais de uma unidade de medida.

- Clique no botão “**+**” (**Cadastrar** **Unidade de Medida**)
- Informe **Unidade de Medida**, **Tipo da Medida** e **Quantidade na medida** e salve as informações.

**Atenção**
Caso estes dados não sejam informados, será apresentada a seguinte mensagem no momento da confirmação do documento:

"**É necessário informar a(s) unidade(s) de carga na aba Unidades de Medida.**"

**Aba Notas do Conhecimento de Transporte**
Nesta aba, obrigatoriamente, você deverá informar as notas que pertencem ao conhecimento de transporte. É importante ressaltar que, quando informada mais de uma nota, estas devem possuir o mesmo emitente (remetente) e destinatário.

- Clique no botão “**+**” (**Cadastrar** **Notas Conhecimento Transporte**)
- Para o modelo de documento fiscal "**1**", os seguintes campos devem ser informados:

  - Número: **Informa-se o número da nota fiscal.**
  - Dh. emissão: **Preenche-se a data e hora da emissão da nota fiscal.**
  - Série: **Informa-se a série da nota fiscal.**
  - Valor da nota: **Este campo destina-se ao preenchimento do valor da nota fiscal.**
  - Modelo Documento: **Se tratando de notas no modelo convencional, informa-se neste caso o modelo de documento igual a "1".**
  - Base ICMS: **Informa-se aqui, o valor da base de cálculo do ICMS da nota fiscal. Caso não exista, informa-se o valor 0,00.**
  - Valor ICMS: **Preenche-se aqui, o valor do ICMS da nota fiscal. Caso não exista, informa-se o valor 0,00.**
  - Base Substit.: **Informa-se aqui, o valor da base de cálculo do ICMS ST da nota fiscal. Caso não exista, informa-se o valor 0,00.**
  - Valor Substit.: **Preenche-se este campo com o valor do ICMS ST da nota fiscal. Caso não exista, informa-se o valor 0,00.**
  - Valor Total dos Produtos: **Este campo deve ser preenchido com o valor total dos produtos da nota fiscal.**
  - CFOP: **Informa-se neste campo, qual a CFOP predominante da nota fiscal.**
- Salve as informações
- No caso do modelo de documento fiscal "**55**", deve-se preencher os seguintes campos:

  - Número: **Informa-se o número da NF-e.**
  - Dh. emissão: **Preenche-se a data e hora da emissão da NF-e.**
  - Série: **Informa-se a série da NF-e.**
  - Valor da nota: **Este campo destina-se ao preenchimento do valor da NF-e.**
  - Modelo Documento: **Como se tratam de Notas Fiscais Eletrônicas, informa-se neste campo, o modelo de documento fiscal "55".**
  - Chave NF-e: **Informa-se neste campo, a chave de acesso da NF-e.**
- Salve as informações
- Para importar a NF acione o botão “**...**” (**Outras** **opções…**) localizado no menu da aba Notas do Conhecimento de Transporte

**Atenção**

Caso os dados nesta aba não sejam preenchidos, o sistema irá apresentar a seguinte mensagem na confirmação:

“**É necessário informar ao menos um tipo de documento a ser transportado na aba Notas de Conhecimento de Transporte**".

**Aba Seguros de Transporte**
Nesta aba você fará o registro das informações relacionadas ao Seguro de Transporte. Em um único CT-e, pode-se ter mais de um responsável pelo seguro da carga.

- Clique no botão “**+**” (**Cadastrar Seguro de Transporte**)
- Selecione o “**Responsável pelo Seguro**” entre as opções **Tomador de Serviço**, **Emitente do CT-e**, **Remetente** ou **Destinatário**.
- Se aplicável, informe:

  - Nome da Seguradora -**Informe o nome da seguradora que irá acobertar o seguro da carga transportada** Ex.: Seguradora
  - Nro. Apólice - **É destinado ao número da apólice de seguro feita pela seguradora que está acobertando o seguro da carga** Ex.: 15879654
  - Nro. Averbação - **Informe o valor da carga, este deve ser preenchido apenas se o valor da carga acobertada for diferente do somatório do valor total das notas fiscais informadas na aba "Notas do Conhecimento de Transporte".** Ex.: 1236547
    Caso não seja necessário preenchê-lo, o sistema irá considerar o valor da carga como sendo o somatório do valor total das notas fiscais transportadas.
- Salve as informações.

**Aba Motorista**
Nesta aba, você poderá informar o motorista que realizará o transporte da carga. Em um mesmo CT-e pode-se ter mais de um motorista, podendo-se com isso, nesta aba, informar um ou mais motoristas.

- Clique no botão “**+**” (**Cadastrar Motorista CT-e**)
- Informe o código do “**Parceiro** **Motorista**” e salve as informações.

**Atenção**

Serão aceitos somente lançamentos de parceiros que estão identificados como "Motorista" em seu cadastro (Cadastro de Parceiros, aba Identificação, campo Tipo).

**Aba Vale Pedágio**
A transportadora adquire o pedágio junto à fornecedora, que informa o valor e o número da compra conforme a rota e o veículo. Esses dados são lançados na aba do CT-e para destacar o vale-pedágio.

- Clique no botão “**+**” (**Cadastrar Vale Pedágio**)
- Selecione entre as opções disponíveis quem é o “**Pagante** **do Pedágio**”.
- Informe o **Nro. Compra** correspondente à aquisição.
- Se aplicável, informe o “**Parceiro** **Pagante**”.

Para mais informações do preenchimento da aba Vale Pedágio acesse [Ajuda Sankhya - Lançamento do CT-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e#abavalepedgio)

**Aba Coleta/Entrega**
Informe nesta aba os dados referentes à coleta ou entrega diferentes do endereço de origem e destino do CT-e, se assim a empresa desejar.

- Neste tipo de CT-e e subcontratação serão considerados

  - Origem: **Parceiro Expedidor**
  - Destino: **Parceiro Destinatário**
- Clique em “**+**” (**Cadastrar Coleta e Entrega por Nota**).
- Realize o preenchimento dos campos com os dados solicitados:

  - Tipo: **Informe aqui se o tipo será destinado a caracterizar uma "Coleta" ou "Entrega".**
  - Tipo transporte: **Defina qual o tipo de transporte que será realizada a coleta ou entrega. O sistema atualmente atende apenas o modal "Rodoviário".**
  - Cód. Parceiro: **Neste campo você informará o parceiro a ser considerado para realizar a coleta ou entrega. Nesta situação, o endereço de coleta ou entrega será o endereço do parceiro informado.**
- Salve as informações.

**Atenção**

Caso nenhuma informação seja inserida neste campo relacionada à coleta ou entrega, para a emissão do CT-e o sistema irá considerar o endereço do "Parceiro Remetente" como "Coleta" e o endereço do "Parceiro Destinatário" como "Entrega".

**Aba Documentos Anteriores**
O documento anterior consiste em informar qual ou quais CT-e's foram emitidos antes do que está sendo gerado no momento. Informar o CT-e normal emitido anteriormente. Os documentos anexos devem **possuir o mesmo** **parceiro**, **destinatário** e **remetente**.

- Clique em “**+**” (**Cadastrar Documento Anterior**)
- Informe o **Parceiro Emissor do Documento**
- Preencha o campo indicado com a chave de acesso do documento anterior.

**Atenção**

Caso esteja-se utilizando um Tipo de Operação caracterizado com o serviço Redespacho, Redespacho Intermediário ou Subcontratação, e no mínimo um documento anterior não tiver sido informado nesta aba, o sistema irá exibir um alerta com as seguintes informações:

"**Para CT-e de Redespacho, Redespacho Intermediário ou Subcontratação, o(s) documento(s) anterior(es) deve(m) ser informado(s).**"

**Aba Financeiro**

- Valide se as informações preenchidas automaticamente condizem com a configuração da TOP e do Tipo de Negociação selecionados no cabeçalho.
- Após todas as validações e o preenchimento correto das informações solicitadas, acione o botão “**Confirmar**” para finalizar o lançamento do CT-e de Redespacho.

**Atenção!**

O preenchimento da aba Lacre é OBRIGATÓRIO apenas em transportes de medicamentos ou combustíveis.
