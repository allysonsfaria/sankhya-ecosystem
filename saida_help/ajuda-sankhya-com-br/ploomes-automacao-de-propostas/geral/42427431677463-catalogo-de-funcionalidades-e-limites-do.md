---
id: "42427431677463"
titulo: "Catálogo de funcionalidades\ne limites do Ploomes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427431677463-Cat%C3%A1logo-de-funcionalidades-e-limites-do-Ploomes"
trilha: "PLOOMES: Automação de propostas  > Geral"
atualizado_em: "2026-08-14T13:26:54Z"
rotulos: ["sync_hc", "ploomes", "ploomes_11459376", "sync_hash_844d997bab6f"]
---

# Cadastros / Tabelas

## Clientes

Embora essa tabela se chame “Clientes” (e seu nome não seja alterável), ela é, na realidade, um cadastro de empresas e pessoas (cada um com um formulário específico). As pessoas podem ser vinculadas a empresas (mapeando, assim, contatos de pessoas jurídicas) ou podem ser clientes finais. Com isso, podemos trabalhar vendas para pessoas físicas e jurídicas no Ploomes.

Utilizando as funcionalidades descritas no tópico “**formulários e campos**” (exibições e obrigatoriedades condicionais) é possível armazenar diversos tipos de cadastros, como: prospects, leads, clientes, ex-clientes, transportadoras, concessionárias, entre outros.

Os itens armazenados neste cadastro podem ser visualizados no formato de tabela (separados por abas) e no mapa (caso os campos nativos “Latitude” e “Longitude” estejam preenchidos). Quando a visualização por mapa estiver ativada, o Ploomes exibe, no máximo, 300 clientes simultaneamente.

É possível, vincular empresas entre si, criando, assim, a visualização de matrizes e filiais dentro do Ploomes.

Ao acessar o cadastro de um cliente, o usuário visualizará todos os dados cadastrais (que estejam liberados para sua visualização), o histórico de interações (registros de interação vinculados a este cliente), tarefas em aberto, cards / negócios, propostas, documentos, vendas, produtos do cliente, anexos e formulários externos vinculados a este cliente.

Caso o cliente acesso seja do tipo “Empresa”, o usuário visualizará também as pessoas vinculadas àquela empresa (caso existam), bem como as filiais cadastradas (caso existam).

Além disso, caso o usuário tenha configurado a integração de disparo de e-mails (via SMTP), ele poderá enviar e-mails dentro dessa mesma tela.

A estrutura da tela de clientes não é personalizável, isto é, não é possível configurar quais informações serão exibidas (com exceção dos campos, que possuem configurações específicas explicadas no tópico “**formulários e campos**”).

O usuário, ao visualizar o histórico de registros de interação, pode optar por: exibir todas as atividades (todas as interações feitas naquele cliente, desde que ele possa visualizar atividades de outros usuários) ou apenas as suas atividades (registros de interação criados pelo seu próprio usuário). Por fim, o usuário ainda pode escolher exibir interações de apenas determinados **tipos** (explicados no tópico “**registros de interação**”).

Atualmente é possível armazenar até 200.000 (duzentos mil) itens nesta tabela (todos os tipos de cadastro são levados em consideração);

Em cada cliente do tipo empresa é possível vincular, no máximo, 1000 clientes do tipo pessoa.

Não é possível vincular pessoas a outras pessoas.

## Cards / Negócios

O cadastro de cards / negócios é uma das funcionalidades mais personalizáveis do Ploomes e seu objetivo principal é organizar e controlar diversos fluxos de trabalho, embora possua outras aplicações que serão exemplificadas mais para frente.

É importante destacar que, assim como a tabela “Produtos do cliente”, esse cadastro também pode ter seu nome alterado.

É nessa funcionalidade que seus funis / processos são acompanhados e controlados. Um funil / processo é, basicamente, um fluxo de trabalho dividido em etapas com atividades, regras, aprovações, passagens de bastão, entre outros. Para facilitar o entendimento, citamos os exemplos abaixo:

- **Funil de vendas:** processo de vendas com etapas que guiam o vendedor e trazem visibilidade ao gestor da situação das negociações que estão em andamento;
- **Licitações:** processos burocráticos que envolvem múltiplos colaboradores, fluxos de documentos, alertas de prazos, entre outros;
- **Vendas complexas:** processos que podem envolver múltiplas equipes:

  - Levantamento técnico com pré-vendas;
  - Desenvolvimento de projeto por equipe de engenharia;
  - Estudo de viabilidade pela equipe financeira;
  - Entre outros.
- **Renovação de contratos:** alertas automáticos a partir de prazos de renovação, processos de assinatura e envolvimento de equipe jurídica para adição de cláusulas;
- **Implantação:** o Ploomes trabalha não somente com funis / processos relacionados a vendas, mas qualquer funil / processo relacionado a clientes (pós-vendas, por exemplo). A passagem de bastão da equipe de vendas para uma equipe técnica é muito comum. Falamos aqui de visitas de vistoria, instalação, entre outros;
- **Chamados técnicos:** chamados técnicos, muito comumente, são processos simples. Neste caso, o Ploomes trabalha como repositório centralizador de solicitações, facilitando e organizando a passagem de bastão entre as equipes.

O objetivo desta funcionalidade é trazer maior gestão e eficiência para seus fluxos de trabalho, além de melhorar a colaboração entre sua equipe. Na prática, esta é a funcionalidade onde seus colaboradores vão passar a maior parte do tempo.

Durante a configuração de cada processo, existem diversas regras que organizam e controlam como o fluxo de trabalho será executado pelo CRM, como:

- **Nomenclaturas:** para cada funil, determinamos o seu nome (Funil de Vendas, por exemplo), bem como o nome dos itens que serão armazenados nele (como “Negócios” ou “Oportunidades”, por exemplo).
- **Layout:** aqui escolhemos um ícone que represente aquele processo que está sendo parametrizado. O Ploomes conta com uma biblioteca padrão de ícones e não é possível optar por ícones que não estejam nessa biblioteca. Além disso, podemos definir qual será a cor desse ícone (cores selecionadas pelo usuário usando o código hexadecimal da mesma).
- **Opções de visualização:** os processos podem ser vistos de em dois formatos:

  - Tabela - Neste tipo de visualização, os cards / negócios são listados para os usuários no **sistema de abas** do Ploomes.
  - Funil/Kanban - Já neste formato, os cards / negócios são exibidos no tradicional Kanban, alocando-os de acordo com as etapas nas quais se encontram.
- **Acessos:** para cada funil, definimos quem poderá visualizá-lo, liberando para determinados usuários, determinadas equipes ou todos da empresa. Não é possível liberar para “equipe A, equipe B e usuário 1”. Neste cenário, o “usuário 1” precisará estar alocado a uma equipe e, essa, liberada para visualizar o processo.
- **Etapas dos funis / processos:** definição de quais serão as etapas do processo e seus respectivos nomes (com limite de 100 caracteres);
- **Formulário para criação do item:** usando a funcionalidade de **formulários e campos**, definiremos as regras para a criação de cards / negócios neste processo;
- **Regras:** dentro de cada um dos funis / processos do Ploomes, existem regras que podem ser configuradas para cada etapa: a passagem por todos os estágios é obrigatória? É proibido voltar de estágio? Só se pode finalizar um processo no último estágio? Um pedido de venda deve ser gerado automaticamente quando uma oportunidade de negócio for dada como ganha? Podemos gerar vendas, documentos ou propostas neste processo? Se sim, existe algum filtro de quais modelos de vendas, documentos ou propostas podem ser gerados?
- **Ações de ganhar e perder:** Os processos podem ser ganhos ou perdidos e é possível customizar o nome dessas ações, escolhendo a nomenclatura que mais se adeque ao funil que está sendo configurado. O Ploomes possui uma biblioteca não manipulável de nomes e cores para a personalização dessas ações.
- **Motivos de perda:** caso um card / negócio seja perdido, o Ploomes solicitará, obrigatoriamente, ao usuário, o preenchimento do motivo de perda. O administrador poderá cadastrar os motivos de perda para cada processo (com limite de 50 caracteres para cada motivo). A ação de perder abrirá uma janela e o usuário verá um formulário para escolher o motivo. Este formulário não é customizável (não é possível adicionar perguntas com base no motivo selecionado, por exemplo);

### Checklists

Com essa funcionalidade, podemos definir dentro de cada etapa de cada funil / processo, uma lista de campos que devem ser preenchidos para que o processo avance de estágio. O objetivo dessa funcionalidade é garantir a qualidade das informações e direcionar melhor a operação dos usuários durante cada fase do processo.

Os checklists, portanto, são como um questionário específico de cada etapa. Esse questionário é configurado pelo administrador e, nele, podemos inserir campos de três entidades:

- **Clientes:** Suponha que estejamos configurando o seu Funil de Vendas para novos clientes. Para que o processo seja concluído, é preciso inserir o CNPJ da empresa, mas você não quer travar o processo nos momentos iniciais. Diante desse cenário, podemos manter o campo CNPJ como **não obrigatório** no formulário de “Nova empresa”, mas podemos inseri-lo como **obrigatório** na última etapa deste Funil de Vendas;
- **Contatos:** Caso o card / negócio possua um contato vinculado (os cards / negócios do Ploomes possuem apenas **um** contato principal), é possível incluir campos do cadastro deste contato no questionário (como e-mail, telefones etc);
- **Cards / Negócios:** Podemos adicionar campos do próprio processo nos questionários, fazendo com que as informações sejam solicitadas apenas nos momentos pertinentes. Suponha que você tenha um campo chamado “Previsão de fechamento”, que só deveria ser preenchido pelo usuário na etapa “Apresentação da proposta”. Diante desse cenário, podemos alocar este campo no formulário de criação de cards / negócios como um campo não obrigatório, mas torná-lo mandatório quando o card / negócio chegar na etapa correta.

Como os checklists são referências ao sistema de **formulários e campos** do Ploomes, é possível combinar funcionalidades a fim de personalizar e controlar ainda mais processos complexos, como aprovações.

Imagine que exista uma etapa no seu processo chamada “Análise de crédito” e que, nela, um questionário (checklist) será exibido com um campo chamado “Análise aprovada?”. Agora imagine que este campo tem sua **edição** permitida apenas para usuários da “Equipe Financeira”. Com essa arquitetura, conseguimos garantir que apenas os usuários corretos preenchem informações específicas, garantindo a qualidade da coleta das informações, bem como a idoneidade dos dados armazenados no sistema.

### Automações de funil

Assim como os checklists, podemos configurar automações para cada uma das etapas do processo / funil. Automações são ações disparadas quando determinados gatilhos são “puxados”. Exemplo: quando um lead entra em uma determinada etapa, disparar e-mail alertando a equipe de marketing. As automações podem ser disparadas nas seguintes situações:

- Quando um processo for iniciado;
- Quando um processo atingir determinada etapa;
- Quando um processo for finalizado com sucesso;
- Quando um processo for finalizado com fracasso;
- Quando um processo for reaberto.

Com relação às ações (executadas após o disparo de um gatilho), temos os seguintes tipos:

- Edição de dados e propriedades do processo, do cliente, entre outros;
- Criação de nova tarefa para um ou mais usuários;
- Adição de observação no histórico do processo;
- Criação de um novo processo vinculado;
- Disparo de e-mail.

Alguns casos de uso comuns:

- **Conexão entre funis / processos:** pelo Ploomes, podemos fazer os processos 'conversarem'. Exemplo: os itens bem-sucedidos do processo comercial devem ser enviados para o processo de pós-vendas? Com processos bem conectados, garantimos a amarração completa de todas as atividades envolvidas, evitando perdas de informações ao longo do andamento de cada processo.

- **Conexão entre equipes:** quando falamos de conexão entre equipes, falamos de passagem de bastão. Além de tornar as equipes envolvidas mais eficientes e organizadas, incluí-las no Ploomes com conexões claras é uma técnica excelente para garantir o engajamento na plataforma. Exemplo: o seu time financeiro pode ser incluído em uma etapa do funil de vendas para realizar aprovações de preço, limite de crédito, entre outros. Pelo Ploomes, conseguimos limitar o preenchimento de campos e aprovações para determinados usuários, garantindo um processo seguro e controlado.

### Limitações importantes

Os códigos sequenciais dos cards/negócios no Ploomes são atribuídos automaticamente pelo sistema com base na ordem cronológica de criação, independentemente do processo ou funil ao qual pertencem. Isso significa que o código é gerado com base na data de criação, sem diferenciar os processos/funis.

Por exemplo, considerando dois funis (A e B), o cenário de criação de cards seria assim:

1. Card criado no funil A - Código 1
2. Card criado no funil B - Código 2
3. Card criado no funil A - Código 3
4. Card criado no funil A - Código 4
5. Card criado no funil B - Código 5

Embora o funil B tenha dois cards / negócios, seus códigos são 2 e 5, e não seguem uma numeração separada para cada funil, já que o sistema atribui os códigos de forma contínua, independente do funil de origem.

Atualmente, no Ploomes, é possível armazenar até 200.000 (duzentos mil) itens nesta tabela (todos os tipos de cadastro são levados em consideração);

Durante a duplicação de cards / negócios, as suas propostas, vendas e documentos não são enviadas para o card / negócio duplicado.

As cores principais dos cards, quando visualizados no formato Kanban, são sempre baseadas na sua **situação**:

- Em aberto - card sempre será exibido com o fundo branco;

- Ganhos - card sempre será exibido com a cor escolhida nas regras de “Ações de ganhar e perder” daquele processo / funil;

- Perdidos - card sempre será exibido com a cor escolhida nas regras de “Ações de ganhar e perder” daquele processo / funil;

Todos os cards / negócios do Ploomes possuem um contador de “Dias no estágio”. Esse contador é automático e contabiliza sempre dias **corridos**, não sendo permitido a sua alteração para dias úteis.

É possível criar até 100 automações por estágio de cada processo / funil.

## Produtos

Esta tabela é responsável pelo cadastro de produtos, serviços e suas respectivas tabelas de preços. Os itens registrados aqui devem ser agrupados pela propriedade "Grupo", isto é, todo produto criado precisa, obrigatoriamente, ter um grupo relacionado a ele.

Além disso, os "Grupos" podem ser organizados por meio da propriedade "Família". Nesse contexto, uma "Família" pode conter vários "Grupos", e cada "Grupo" pode ter múltiplos "Produtos". No entanto, um "Produto" pertence a apenas um "Grupo", e cada "Grupo" está associado a uma única "Família".

Grupos de produto possuem níveis de acesso, podendo ter sua visão limitada a determinados usuários, equipes ou liberada para todos da empresa. Caso um usuário não tenha acesso ao grupo de produto, ele não verá nenhum dos produtos dentro do CRM, seja no módulo de produtos, na geração de documentos ou no preenchimento de campos do tipo produto.

Essas permissões são exemplificadas na imagem a seguir:

![Imagem 1: Essas permissões são exemplificadas na imagem a seguir:](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1541706275/58e12c9e793da32c94705053fa6a/prod1.png?expires=1786860000&signature=fc1fa31ab5a49de4a35eaf54d2cd8241568d3ab86825ebf2c67509b8b723d785&req=dSUjF85%2Bm4NYXPMW3nq%2BgWPODSr5Lb9GqGg85eCfODglClTXUyjK5t1ZfFGU%0Aot32R0QjihMgq5yvODNKQG30UlI%3D%0A)

Durante a geração de documentos, o usuário pode visualizar o cadastro de itens de produtos e pode inseri-los (item a item) no que chamamos de “bloco” de produtos.

Para cada bloco, conseguimos determinar quais produtos podem ser exibidos e escolhidos nele, com base nos seguintes filtros:

- Por grupo de produto;
- Por família de produto;
- Por marcador de produto;
- Pela presença dos produtos no cliente vinculado ao documento que está sendo gerado.

## Opcionais

É possível associar produtos, grupos ou marcadores de produto como "vínculos" entre produtos, permitindo aos usuários parametrizar a relação entre eles. Durante a configuração de documentos, essa funcionalidade permite que, ao selecionar um item, os produtos vinculados a ele sejam também sugeridos, possibilitando a composição de produtos personalizados e a customização da proposta comercial.

Além disso, é possível criar categorias de opcionais, que funcionam como tipos específicos de vínculos, oferecendo maior flexibilidade na personalização durante a geração de propostas, vendas e documentos. Essas categorias proporcionam uma organização mais eficiente durante a configuração dos produtos e, posteriormente, na criação de documentos.

Abaixo, uma imagem que representa a relação entre os produtos, opcionais e as regras entre vínculos:

![Imagem 2: Abaixo, uma imagem que representa a relação entre os produtos, opcionais e as regras entre vínculos:](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1541710009/ed240d2a3d388808ef7c0baa2fff/prod2.png?expires=1786860000&signature=8e9b446d0d6da9695e0f9369dd3d3e6d7f8b8c6f3bdf404bf99ab041f110a4fb&req=dSUjF85%2FnYFfUPMW3nq%2BgSK4IuUNb33DzUaFXLa8rbPYA8NfuHfNVBVUrdmS%0AWDgStoVBNFlV1B1Gl3ITJSnZJQk%3D%0A)

Os opcionais são, na verdade, produtos vinculados a outros produtos. Quando selecionados em uma proposta, venda ou documento, eles permitem ao usuário montar versões personalizadas do produto principal, como cores ou variações específicas.

Os opcionais também possuem regras de sugestão, obrigatoriedade ou bloqueio entre si. Isso significa que a inclusão de determinados produtos pode sugerir, exigir ou impedir a seleção de outros produtos vinculados, proporcionando maior controle na criação de propostas.

Na imagem de exemplo, o “Produto opcional 1” foi selecionado pelo criador do documento e, com isso, o “Produto opcional 2” e “Produto opcional 3” foram impedidos e não serão exibidos no documento final.

Além disso, pelo fato do “Produto opcional 1” ter sido escolhido”, o “Produto opcional 4” foi sugerido (incluído automaticamente, mas pode ser removido pelo criador do documento), o “Produto opcional 5” foi obrigado (não pode ser removido, já que o 1 exige o 5) e o “Produto opcional 6” foi impedido e também não será exibido no documento final.

## Limitações importantes

É possível armazenar até 200.000 produtos (lembre-se que um opcional também é considerado um produto).

## Propostas, Vendas e Documentos

Essa funcionalidade permite a criação de modelos de documentos, como propostas comerciais, pedidos de venda, contratos, aditivos, entre outros.

Modelos são como “padrões” e consistem na exibição de textos (fixos ou variáveis), que podem incluir informações do Ploomes, como dados de clientes, contatos, processos, produtos, além de imagens, tabelas e elementos de formatação, como cabeçalhos e rodapés.

Para melhorar a organização dos mais diversos tipos de documentos que podem ser gerados, o Ploomes separa seus modelos em três categorias:

- Propostas;
- Vendas;
- Documentos (de cliente e de cards / negócios).

Os modelos podem ter sua visualização limitada para determinados usuários, equipes, ou liberados para que todos da empresa possam vê-lo. É possível restringir quais modelos de documentos podem ser gerados em cada funil ou processo.

As propostas podem ser revisadas, gerando e guardando suas versões anteriores. Ao excluir propostas revisadas, o documento automaticamente é transformado na sua última versão. As propostas são, obrigatoriamente, vinculadas a cards / processos.

Já as vendas podem ser geradas a partir de uma proposta ou de forma direta (sem a necessidade de um processo / card). Além disso, possuem um campo nativo chamado “Estágio”, que pode ter suas opções personalizadas. Apesar da presença deste campo, as vendas não podem ser visualizadas em Kanban, apenas em tabela (através do sistema de abas).

Por fim, os documentos gerados podem ser vinculados diretamente a clientes ou também associados a cards / negócios.

Vendas e documentos não possuem a funcionalidade de revisão, ou seja, podem apenas ser editados, sem guardar a versão de como eram anteriormente.

Além da possibilidade de revisão (para propostas) e de edição (para todas as categorias), o Ploomes ainda conta com a funcionalidade “Modificação visual”. Essa funcionalidade permite ao usuário visualizar o documento gerado através de um editor de texto e imagens, podendo fazer correções e alterações que ficarão salvas apenas naquele item gerado, não afetando o modelo em si. A modificação visual é útil para pequenas correções, mas suas alterações não ficarão salvas em nosso banco de dados e, caso o item seja revisado ou alterado, todas as alterações serão perdidas.

A modificação visual só estará disponível para a utilização caso não existam **fluxos de aprovação** configurados na conta.

Fluxos de aprovação são uma forma de controle de políticas comerciais para os documentos gerados no Ploomes. Alguns exemplos comuns de regras que podem ser gerenciadas pelos fluxos são:

- Alçadas de desconto, dando liberdade aos usuários de gerarem propostas alterando seus valores até certo limite que, caso excedidos, precisarão passar por uma (ou mais) aprovações;
- Bloqueio na emissão de documentos que quebrem regras regulatórias (venda de produtos especiais para clientes que não possuem autorização, por exemplo);

Um fluxo de aprovação sempre se baseia em um critério lógico que será verificado através de um ou mais campos do Ploomes. Caso esse critério seja satisfeito, o fluxo será disparado e uma das ações abaixo acontecerá:

- Bloqueio - impede que a proposta, venda ou documento seja criado;
- Aprovação - a proposta, venda ou documento será enviada aos usuários aprovadores (é possível determinar mais de um nível de aprovação) e ficará congelada (não poderá ser compartilhada) até que o usuário aprove. Os itens também poderão ser reprovados e usuários aprovadores poderão escrever comentários a respeito de sua decisão no campo “Comentários”;
- Alerta - o criador da proposta, venda ou documento será alertado no momento de salvar o item, mas ele será gerado normalmente e poderá ser compartilhado.

Todos os documentos gerados podem ser compartilhados das seguintes formas:

- Download do material em PDF;
- Via e-mail:

  - Opção disponível para usuários com a integração de envio de e-mails habilitada. Ao clicar no compartilhamento por e-mail, é possível escolher um modelo de e-mail. O PDF do material é automaticamente anexado no e-mail, bem como um link para visualização das propostas.
- Via Link Web:

  - Opção nativa do Ploomes que envia um e-mail para o cliente que pode visualizar online o documento gerado. Além de visualizar, o cliente consegue aceitar / recusar o documento e interagir (assincronamente) com o criador do material. O aceite não tem validade jurídica, mas dispara ao criador avisos sempre que o link for aberto e, também, sempre que um comentário é feito. O cliente também recebe notificações por e-mail quando um comentário do criador é feito.
- Via WhatsApp:

  - Essa opção abrirá um chat no WhatsApp Web com o telefone do contato daquele documento (caso exista), ou o usuário poderá digitar um telefone. Ao compartilhar o documento por WhatsApp, um link é enviado e, sempre que for aberto, o usuário é notificado pelo Ploomes.

### Limitações importantes

É possível armazenar até 200.000 propostas, 200.000 vendas e 200.000 documentos no Ploomes.

É possível armazenar até 150 produtos por proposta, venda ou documento, caso cada produto possua 4 campos ou menos. Para cada novo campo, o limite é reduzido em 8 (oito) produtos por proposta, por venda e por documento. Este limite é garantido para computadores que possuam 8GB de memória RAM. A performance do sistema durante a criação e edição de propostas, vendas e documentos poderá reduzir à medida que o limite se torna mais próximo.

Os modelos do Ploomes são sempre gerados no modo retrato e não possuem a funcionalidade de sumarização e paginação.

As únicas fórmulas disponibilizadas com o módulo “Automação de propostas e documentos” são:

- Cálculo do “Total” de um produto, que multiplica o campo “Quantidade” (nativo) pelo campo “Valor unitário” (nativo) e remove o “Desconto” (nativo, dado sempre em porcentagem);
- Cálculo do “Total” de um bloco de produtos, que soma o campo “Total” dos produtos inseridos naquele bloco e remove o “Desconto” (nativo, sempre dado em porcentagem e que altera apenas o “Total” do bloco, não afetando valores dos produtos inseridos no bloco);
- Cálculo do “Valor” da proposta, venda ou documento, que é a soma do campo “Total” dos blocos, removendo também o “Desconto”, com o mesmo comportamento do campo “Total” do bloco.

Por fim, o Ploomes possui uma tabela nativa de parcelas, que pode ser inserida nos modelos e permite ao usuário fragmentar o “Valor” da proposta, selecionando o número de parcelas e suas respectivas datas (manualmente). O cálculo de cada parcela é feito automaticamente. Não é possível criar propriedades na tabela de parcelas (como formas de pagamento para cada parcela), bem como não há a possibilidade de alterar o cálculo do valor de cada parcela (sempre será o “Valor” da proposta dividido pela quantidade de parcelas).

### Fórmulas de CPQ

Além da possibilidade de configuração de opcionais, como descrito no tópico **“Opcionais” de Produtos,** com fórmulas, é possível a execução de:

- **Cálculos simples:** utilizando JavaScript é possível construir funções que usem (ou não) outras propriedades (campos) do Ploomes que serão executadas no momento da geração dos documentos e retornarão o valor para um campo específico;
- **Fórmulas condicionais:** é possível determinar cenários e, para cada um deles, funções em JavaScript que serão executadas caso o critério do cenário seja satisfeito;
- **Fórmulas integradas:** realização de consultas externas a APIs para o retorno de informações relevantes para a geração do documento;
- **Consulta à planilhas de Excel / Google Sheets:** conseguimos utilizar planilhas como motor de cálculo, mapeando no Ploomes campos que serão entradas para células específicas e retornarão, em determinado campo do Ploomes, resultados calculados pela planilha.

## Produtos do cliente

A tabela de Produtos do cliente permite o relacionamento entre as tabelas “Clientes” e “Produtos”. Ela foi criada para armazenar os ativos (produtos) em posse dos clientes.

Justamente por isso, ao criar um novo produto do cliente, o Ploomes demanda que ele seja vinculado a um produto da base. Ex.: se possuo um Equipamento X em minha base de produtos, eu posso criar números de série dele para cada cliente meu.

Além do vínculo com clientes, os Produtos do Cliente podem ser vinculados a cards / negócios, possibilitando a utilização de workflows do Ploomes como ferramenta de gestão de Assistência Técnica.

Também é possível selecionar Produtos do Cliente durante a geração de documentos. Isso permite, principalmente, a negociação e oferta de equipamentos usados (já que, embora o nome do módulo seja Produtos do Cliente, eu consigo, mesmo assim, ter um número de série avulso, ou seja, não vinculado a cliente algum, o que permite uma gestão simplificada de ativos em estoque).

Assim como outras tabelas do Ploomes, em Produtos do Cliente é possível a criação de propriedades dinâmicas, abas e tabelas customizáveis, extração de relatórios, automações, entre outros.

Dada sua flexibilidade e a possibilidade, além das citadas acima, de alteração do nome da tabela para o que você quiser, os Produtos do Cliente passaram a ser usados de diversas formas diferentes:

- Gestão de contratos, onde cada produto do cliente é um contrato de serviço ou um equipamento coberto pela manutenção preventiva de um contrato;
- Gestão de tabela de preços por cliente, onde cada produto do cliente é justamente o preço especial que aquele cliente paga por aquele produto;
- Gestão de produtos que o cliente compra e forma recorrente ou que possui licença para comprar;

## Limitações importantes

Atualmente, no Ploomes, é possível armazenar até 200.000 (duzentos mil) itens nesta tabela (todos os tipos de cadastro são levados em consideração);

## Registros de interação

Registros de interação são anotações que podem estar vinculados a tabela de clientes e negócios / cards. Os registros são separados em sete tipos: simples, visita, ligação, e-mail, reunião, conferência e WhatsApp.

É possível limitar os tipos de registros de interação que podem ser criados, mas não é possível criar novos tipos de registro de interação.

Os registros podem ser preenchidos através da funcionalidade “speech to text”, na qual o texto é automaticamente inserido através da fala do usuário.

É possível armazenar anexos dentro dos registros de interação, com a limitação de 25 mb para cada arquivo.

Ao digitar “@“ durante a criação de um registro de interação existe a opção de marcar um ou mais usuários selecionando-os na lista suspensa, que varia de acordo com o perfil de cada usuário - que determina quais usuários são visíveis para cada acesso.

Usuários marcados em registros de interação recebem notificações do sistema.

Os registros são exibidos no formato de linha do tempo, do mais recente para o mais antigo.

## Limitações importantes

Não é possível fixar registros de interação (exibindo, por exemplo, registros mais antigos no topo da tela).

## Usuários e equipes

É nesta tabela que estarão cadastrados usuários e equipes.

Durante o cadastro de um usuário, é sempre obrigatório definir o seu perfil, mas outras propriedades podem ser configuradas pelo administrador seguindo as regras e funcionalidades descritas no tópico “**formulários e campos**”.

Os usuários podem ser inativados pelo administrador, perdendo acesso imediato à ferramenta - o histórico do usuário é preservado, mas ele passa a não ser exibido em filtros que listam usuários (como filtros que utilizam o campo “responsável”, por exemplo).

Ao trocar o nome de um usuário todo o histórico possuirá o novo nome do usuário. Por isso, em caso de substituição de usuários, é recomendável a inativação da licença e a ativação de uma nova na sequência, a fim de preservar a integridade dos dados históricos.

O usuário pode, através do seu perfil, escolher algumas preferências de utilização do sistema, como: a linguagem, a usabilidade de múltiplos funis, a usabilidade de modelos de propostas e documentos e, também, o uso ou não da autenticação multifator.

Um usuário pode pertencer a múltiplas equipes.

Uma equipe nada mais é do que a possibilidade de agrupamento de um ou mais usuários. É importante ressaltar que os usuários e equipes são de extrema importância para a gestão de níveis de acesso no Ploomes, assunto explicado detalhadamente no tópico “**Perfis de usuário**”, da seção "**Ferramentas de manipulação de cadastros / tabelas**".

## Sua empresa

Esta tabela armazena os dados da sua companhia, como nome, razão social, CNPJ, logotipo, entre outros.

Por ser uma tabela que registra apenas um item, nela é possível armazenar também propriedades genéricas, que podem ser acessadas por outras funcionalidades do sistema, principalmente fórmulas.

Um exemplo de propriedade genérica é a cotação do dólar. Os administradores podem armazenar essa informação nesta tabela (atualizando-a sempre que quiserem) e durante a geração de uma proposta comercial, fórmulas que calculam preços podem consultar este dado para realizar esse tipo de operação.

# Ferramentas de manipulação de cadastros / Tabelas

As ferramentas para manipulação e visualização de dados do Ploomes são:

- Formulários e campos;
- Automações;
- Abas e tabelas dinâmicas;
- Filtros;
- Importação de Excel;
- Exportação de Excel;
- Edição em massa;
- Perfis de usuário;
- Automações.

Como as ferramentas de manipulação de dados estão presentes em todo o sistema, documentaremos a seguir os comportamentos padrões de todas elas, sabendo que, dependendo de cada entidade ou objeto satélite, podem existir comportamentos específicos.

## Formulários e campos

Para cada cadastro / tabela do Ploomes, existe um formulário que é a maneira através da qual um item (empresa, pessoa, produto, entre outros) é inserido e salvo na base de dados do sistema.

Os formulários, portanto, são um aglomerado de campos (propriedades) referentes àquela tabela específica. Na configuração de um formulário, é possível agrupar campos em seções (um agrupamento de “Localização”, por exemplo, pode conter campos de endereço, número, complemento, etc.).

Os campos podem ser categorizados em duas categorias:

- **Campos nativos**

  - Não podem ter seu “Título” alterado (exemplo: o campo “Nome” da entidade “Empresa” sempre se chamará “Nome”);
  - Não podem ter seu “Tipo” alterado (exemplo: o campo “Segmento” da entidade “Empresa” sempre será do tipo “Opções pré-cadastradas”);
  - Não podem ser deletados.
- **Campos personalizados**

  - Criados sob medida, a fim de trazer mais personalização e customização para o armazenamento de dados dentro do CRM;
  - Podem ter seu “Título” alterado (a qualquer momento);
  - Podem ter seu “Tipo” alterado (apenas durante a sua criação);
  - Podem ser deletados a qualquer momento (por administradores).

### Configurações de campos

No momento da criação de uma nova propriedade, a primeira decisão a ser tomada por parte do Administrador é o tipo do campo. No Ploomes, existem os seguintes tipos:

|  |  |
| --- | --- |
| - Texto simples | - Texto multilinha |
| - Número inteiro | - Moeda |
| - Número com casas decimais ilimitadas | - Opções pré-cadastradas |
| - Data | - Horário |
| - Checkbox | - CPF |
| - CNPJ | - Porcentagem |
| - Endereço | - Imagem |
| - Anexo | - Cor |
| - Assinatura DocuSign | - Desenvolvedor |
| - Usuário | - Produto |
| - Cliente | - Símbolo de moeda |
| - Assinatura |  |

#### Configurações básicas:

- **Título do campo:**

  - É o "Nome" da propriedade e tem limite de 60 caracteres. Pode ser armazenada em quatro línguas diferentes:

    - Português - Brasil;
    - Inglês;
    - Português - Portugal;
    - Espanhol - México.
- **Valor padrão:**

  - O "Valor padrão" é utilizado para pré-preencher automaticamente um campo com um valor específico durante o processo de cadastro de um novo item no sistema. Quando um valor padrão é definido, ele será sugerido pelo sistema, agilizando o preenchimento de informações e mantendo a consistência dos registros;
  - Por exemplo, se o campo "Contribuinte ICMS?" (do tipo Checkbox) tiver o valor padrão definido como "Sim" (true), ao cadastrar uma nova empresa, esse campo já aparecerá automaticamente marcado como "Sim". O usuário ainda terá a opção de alterar esse valor, se necessário.
- **Campo chave:**

  - Um "Campo chave" é utilizado para garantir a unicidade de determinados dados no sistema. Quando um campo é definido como "Chave", o sistema Ploomes realiza uma verificação automática na base de dados. Isso impede que um novo registro seja criado com um valor duplicado no mesmo campo em que outro registro já existe;
  - Por exemplo, se o campo "ID da Empresa no ERP" for definido como chave, e já houver uma empresa cadastrada com o valor "1" nesse campo, ao tentar cadastrar uma nova empresa com o mesmo valor "1", o sistema exibirá uma mensagem de erro. Essa mensagem informará que já existe um registro com esse valor no banco de dados, evitando a duplicidade de informações;
  - Apenas campos do tipo “Texto simples”, “Número inteiro”, “Moeda”, “Número com casas decimais ilimitadas”, “CPF” e “CNPJ” podem ser marcados como chave.
- **Campo de duas colunas:**

  - Os formulários do Ploomes possuem duas colunas e é possível definir se um campo ocupará uma ou duas destas. O objetivo desta configuração é único e exclusivamente para harmonizar o design do formulário no momento que o mesmo for aberto para os usuários.
- **Campo múltiplo:**

  - Ao habilitar esta opção, é possível incluir mais de um valor no preenchimento de um campo;
  - Por exemplo, se o campo "Segmento" (do tipo "Opções pré-cadastradas") estiver configurado como múltiplo, será possível escolher vários segmentos ao cadastrar uma empresa, em vez de limitar-se a uma única opção;
  - Apenas os campos do tipo “Opções pré-cadastradas”, “Anexo”, “Usuário”, “Produto”, “Cliente” e “Símbolo de moeda” podem ser marcados como múltiplos.

#### Configurações avançadas:

- **Fórmulas:**

  - É possível criar fórmulas utilizando Javascript para realizar cálculos e/ou preenchimentos automáticos de campos com base em outras variáveis (fixas ou dinâmicas) do Ploomes;

    - As fórmulas não estão disponíveis nos cadastros / tabelas habilitadas com a contratação do módulo “Automação de propostas e documentos”.
- **Marcar como dado de pessoa física:**

  - Caso essa opção seja marcada no campo, os dados contidos nesse campo serão assinalados como "dados de pessoa física" e, caso a conta seja excluída, serão excluídos permanentemente, sem possibilidade de restauração.
- **Limitar itens listados:**

  - Em campos que possuem uma tabela de opções cadastradas, é possível limitar quais itens serão listados (apenas no momento da criação ou quando o formulário estiver aberto para edição). Essa filtragem é feita através de Javascript.
- **Exibir como interruptor:**

  - Em campos do tipo “Checkbox”, essa opção pode ser marcada para alterar o design do campo (deixa de ser “Sim” ou “Não” e passa a ser um interruptor).

#### Configurações de obrigatoriedade do campo:

Antes de parametrizar as regras de obrigatoriedade, é possível definir para quais usuários, equipes ou perfis de usuário essas regras serão aplicadas. Portanto, campos podem ser condicionalmente obrigatórios a depender do usuário que está preenchendo o formulário.

Existem duas formas de parametrizar essas regras:

- **Torná-lo obrigatório por padrão:**

  - Obrigue o preenchimento deste campo em formulários, abas e cadastros para os usuários selecionados acima.
- **Torná-lo obrigatório por fórmula:**

  - Configure uma fórmula para alterar a obrigatoriedade em formulários para os usuários selecionados acima;
  - As fórmulas são utilizadas para condicionar a obrigatoriedade do campo a partir de outras variáveis e são construídas usando Javascript. Por exemplo, o campo “SUFRAMA” só é obrigatório quando o campo “ESTADO” tem o valor “Amazonas”, “Acre”, “Rondônia”, “Roraima” ou “Amapá”;
  - Fórmulas só são disparadas quando um formulário está aberto, isto significa que edições in-line e edições dentro de abas não considerarão a fórmula parametrizada nos campos.

#### Configurações de edição e bloqueio do campo:

Assim como a obrigatoriedade, as regras de edição e bloqueio do campo também podem ser condicionadas inicialmente para determinados usuários, equipes ou perfis de usuário.

Existem duas formas de parametrizar essas regras:

- **Torná-lo bloqueado por padrão:**

  - Não permita que o campo seja editado em formulários, abas e cadastros para os usuários selecionados acima.
- **Torná-lo bloqueado por fórmula:**

  - Configure uma fórmula para alterar o bloqueio ou edição do campo em formulários para os usuários selecionados acima;
  - As fórmulas são utilizadas para condicionar a liberação do preenchimento do campo a partir de outras variáveis e são construídas usando Javascript. Por exemplo, o campo “SUFRAMA” só é editável quando o campo “ESTADO” tem o valor “Amazonas”, “Acre”, “Rondônia”, “Roraima” ou “Amapá”;
  - Fórmulas só são disparadas quando um formulário está aberto, isto significa que edições in-line e edições dentro de abas não considerarão a fórmula parametrizada nos campos.

#### Configurações de visualização do campo

A visualização de campos segue, também, as mesmas regras de parametrização que a obrigatoriedade e a edição / bloqueio. Portanto, podemos definir quais usuários, equipes ou perfis de usuário podem visualizar cada um dos campos do Ploomes.

Existem duas formas de parametrizar essas regras:

- **Torná-lo oculto por padrão:**

  - Não permita que o campo seja visto em formulários, abas e cadastros para os usuários selecionados acima.
- **Torná-lo oculto por fórmula:**

  - Configure uma fórmula para liberar ou não a visualização do campo em formulários para os usuários selecionados acima;
  - As fórmulas são utilizadas para condicionar a visualização do campo a partir de outras variáveis e são construídas usando Javascript. Por exemplo, o campo “SUFRAMA” só é visível quando o campo “ESTADO” tem o valor “Amazonas”, “Acre”, “Rondônia”, “Roraima” ou “Amapá”;
  - Fórmulas só são disparadas quando um formulário está aberto, isto significa que edições in-line e edições dentro de abas não considerarão a fórmula parametrizada nos campos.

#### Observações importantes

Como os campos podem ter as três regras acima configuradas de forma paralela, é importante que haja consistência na arquitetura programada, para que não existam inconsistências como “há um campo obrigatório que não está visível”, pois isso pode afetar a experiência do usuário final, levando-o a acreditar que o sistema não está funcionando corretamente quando, na verdade, as regras parametrizadas estão em conflito.

Para facilitar a manutenção e gestão dos campos do tipo "Opções pré-cadastradas", existe uma tela dedicada onde os administradores podem gerenciá-los de forma centralizada.

Essa funcionalidade permite ao administrador visualizar todos os campos deste tipo do sistema, além de criar, editar e excluir opções individualmente. No entanto, não é possível realizar essas ações de maneira massiva.

#### Limitações específicas de campos

- **Texto simples:**

  - Aceita até 250 caracteres.
- **Número inteiro:**

  - Aceita no máximo 9 dígitos.
- **Opções pré-cadastradas:**

  - Aceita no máximo o cadastro de 1000 opções.

## Abas e tabelas dinâmicas

Para cada cadastro / tabela da ferramenta (exceto Sua Empresa), os dados podem ser visualizados em formato de tabela e segmentados através do sistema de abas.

Esse sistema tem como objetivo compartimentalizar dados e exibi-los na tela dos usuários que têm acesso àquela aba no formato de uma tabela dinâmica. Durante a criação de uma aba, portanto, é possível determinar critérios para que o CRM exiba apenas os dados que satisfaçam as condições exigidas. No módulo “Clientes”, por exemplo, é possível criar uma aba que exiba apenas os cadastros que o campo “TIPO” seja igual a “Empresa” e que sejam do “ESTADO” de “São Paulo”.

Com isso, é correto dizer que o sistema de abas é, também, um sistema de filtros. Portanto, as abas têm como finalidade filtrar os itens da tabela que está sendo acessada pelo usuário e não inserir novos itens nesta tabela.

Em cada uma das abas é possível determinar quais são as colunas (campos) a serem exibidos na tabela visualizada pelos usuários. Campos nativos do sistema podem ser ordenados (alfabeticamente, em casos de campos do tipo “Texto simples” e “Opções pré-cadastradas”,“mais recente / mais antigo” em casos de campos do tipo “Data” e “crescente / decrescente” em casos de campos do tipo “Número inteiro”.

### Relação entre tabelas em abas (field-paths)

Como existem relações entre as tabelas do Ploomes (um card / negócio, por exemplo, pode estar vinculado a um cliente), a depender da tabela que está sendo acessada pelo usuário, é possível adicionar colunas com informações de outros cadastros na mesma aba. Um exemplo: podemos criar uma aba de cards / negócios e, nela, adicionar colunas com a informação dos clientes vinculados aquele card / negócio. Esse conceito é conhecido como field-path e é importante entender que nem todas as informações podem ser exibidas em todas as abas.

Imagine que as informações do seu CRM são como uma grande biblioteca, onde cada seção representa um tipo de dado diferente — como clientes, negócios, e propostas. Essas seções são conectadas por caminhos, como corredores da biblioteca. Esses caminhos são o que chamamos de "field-path".

Quando você está numa seção específica da biblioteca, por exemplo, a seção dos "clientes", você consegue enxergar algumas informações que estão em outras seções próximas, como os negócios que esses clientes têm. No entanto, como os corredores são estreitos, você só consegue ver o último livro (ou seja, a última informação) daquela outra seção. Assim, se um cliente tiver vários negócios, você verá apenas o mais recente, como se esse fosse o único livro que conseguisse tirar da estante.

Se quiser ver mais detalhes sobre os negócios desse cliente, precisará caminhar para a seção dos "negócios". Lá, você poderá acessar informações mais amplas sobre cada um. Portanto, para ter uma visão detalhada e abrangente, você às vezes precisa visitar a seção mais específica da biblioteca.

Em outras palavras, o field-path funciona como esses corredores da biblioteca: ele conecta as seções, mas com algumas limitações sobre quantos detalhes de uma seção você pode enxergar a partir da outra. Essa estrutura nos ajuda a organizar e simplificar as informações, garantindo uma navegação mais prática, mas, por outro lado, não permite visualizar múltiplas informações ao mesmo tempo se elas estiverem muito longe no "mapa da biblioteca".

### Limitações importantes

Campos personalizados não possuem ordenação dinâmica.

É possível adicionar até 30 colunas na configuração de uma aba.

Não existem abas de opcionais de produtos de documentos, seções (blocos) de documentos e sua empresa.

## Filtros

Durante o uso do CRM, é comum necessitar afunilar a visualização dos dados, mesmo que já estejamos dentro de uma aba, ou de um processo específico.

Uma aba de “Empresas de São Paulo” (que já possui dois critérios de filtragem) pode ser útil para segmentar sua carteira de clientes de forma macro, mas abas como “Empresas de São Paulo que não compram há 30 dias” podem ser úteis para uma micro segmentação e consequentes ações pontuais (como exportar esses dados para uma ferramenta de Marketing / planilha de Excel).

Os filtros seguem a mesma lógica de criação e de funcionamento das abas e são úteis para uma melhor organização do CRM, já que não seria amigável ao usuário navegar entre dezenas de abas, quando há a possibilidade de utilização de filtros rápidos.

Esses filtros podem ser aplicados ou salvos e o mecanismo para a criação destes segue a mesma lógica da criação de abas (tanto em relação à usabilidade quanto às funcionalidades - é possível definir um nome e quais usuários visualizarão este filtro).

A diferença entre aplicar e salvar um filtro é bem simples: na primeira, você perderá a configuração após a atualização da tela ou caso navegue dentro do Ploomes e retorne à tela que estava previamente filtrada. Já na segunda opção, o filtro ficará salvo (podendo ser removido e editado), sendo útil para consultas comuns.

Existe um filtro especial para a tela de cards / negócios, chamado “Filtro simples”. Essa filtragem mostra ao usuário o formulário de criação de cards / negócios daquele funil específico e não exige que o usuário faça toda a criação do critério de filtragem, basta inserir o valor a ser filtrado no campo desejado.

Esse filtro é apenas aplicável, não pode ser salvo e não está disponível na tela “Tabelas com todos os cards”.

## Importação de Excel

O Ploomes possui uma ferramenta nativa para a migração de dados de planilhas de Excel para algumas tabelas, a fim de facilitar o cadastro de informações de maneira massiva. Esta funcionalidade está disponível para nas seguintes tabelas:

- Clientes (empresas e pessoas);
- Negócios / cards;
- Produtos (grupos, famílias, produtos e opcionais)
- Produtos do cliente;
- Registros de interação.

Para as demais tabelas, não existe uma ferramenta nativa para importação de dados. Por isso, importações como o histórico de propostas comerciais, pedidos e anexos, por exemplo, precisam ser avaliadas pela equipe de atendimento da Ploomes para indicar o melhor caminho de migração deste tipo de dado.

É importante, antes de iniciar a migração de dados, que os campos que serão alimentados já estejam criados no Ploomes. Por exemplo, se na sua planilha de clientes existir uma coluna chamada “Número de vidas”, este campo precisa ser criado no Ploomes previamente (com um “Tipo” compatível com o dado que será importado).

‍

**Regras gerais para importações de dados:**

- O único formato aceito pelo Ploomes é o .xlsx (Excel);
- A planilha importada deve conter apenas uma aba, não deve conter caracteres especiais e fórmulas;
- Cada linha da planilha deve representar um cadastro e, cada coluna, uma propriedade (campo) deste cadastro;
- Se sua planilha definir um responsável para cada cadastro (caso seja pertinente à entidade principal), seu nome precisa estar escrito exatamente como no Ploomes. Caso contrário, o cadastro será importado sem responsável.

**Regras específicas da importação de clientes:**

- No cadastro de clientes o tabela de “Cidade” possui comportamentos específicos que devem ser levados em consideração quando a importação prevê a carga deste tipo de informação (Cidade, Estado, País e Código IBGE):

  - Ao mapear cidades, a detecção de duplicado por Nome é obrigatória;
  - Ao mapear o nome da cidade, o preenchimento do Nome é obrigatório;
  - Para evitar que cidades com o mesmo nome, mas estados diferentes, sejam importadas como uma só, é preciso mapear o campo Estado e marcar a opção “Detectar duplicado por este campo”;
  - Para mapear o Estado da Cidade, é necessário que os dados estejam formatados de acordo com a ISO 3166-1 (Por exemplo: São Paulo deve ser SP e Rio Grande do Norte deve ser RN);
  - Para mapear o País da Cidade, é necessário que os dados estejam formatados de acordo com a ISO 3166-1 (Por exemplo: Brasil deve ser BRA e Estados Unidos deve ser USA);
- As “Pessoas” do Ploomes podem ter ou não vínculos com empresas. Para realizar a importação de pessoas vinculadas à empresas, cada linha da planilha deve representar um contato e uma das colunas deve conter um campo único para a identificação da empresa (como o Nome ou CNPJ, por exemplo);

**Regras específicas da importação de registros de interação:**

- Os registros de interação são sempre ordenados na linha do tempo pela **data de criação**, uma propriedade inalterável e preenchida pelo Ploomes no momento que o item é inserido em nosso banco de dados. Por isso, a importação desses registros sempre vai ser carregada ao CRM com a data na qual a planilha está sendo importada. Por conta disso, é importante ordenar as linhas da planilha da maneira correta, colocando os registros mais antigos no topo e os mais recentes, no final. Isso porque a importação verifica e insere as linhas da planilha da primeira para a última, ou seja, dessa forma os itens mais antigos serão carregados primeiro para o CRM. É recomendável customizar o campo “Descrição” do registro de interação com a “data original” do registro, para que os usuários possam visualizar qual foi a data verdadeira daquele registro.

## Exportação de Excel

Uma das características das abas e tabelas dinâmicas do Ploomes é a capacidade de serem exportadas, gerando uma planilha de Excel (.xlsx). Essa funcionalidade permite que os dados inseridos no CRM sejam tratados para quaisquer finalidades fora do sistema.

Ressaltamos que a exportação de dados é uma permissão definida em cada um dos perfis da conta, ou seja, os administradores determinam quais perfis podem ou não exportar dados do Ploomes.

O Excel gerado é um espelho exato da aba que está sendo exportada. Isso significa que ele leva em consideração até mesmo filtros aplicados a abas, bem como as colunas que estão configuradas para serem exibidas.

Essa exportação possui um limite aproximado de 50 mil linhas e 30 colunas, podendo ser menor a depender dos tipos de campos que estão sendo exibidos nas colunas.

É possível exportar abas de forma paralela e elas ficam disponíveis para consulta no menu “Suas exportações” do usuário que solicitou a exportação. Uma vez que a exportação é concluída, o arquivo gerado fica armazenado por 2 dias, e pode ser baixado a qualquer momento pelo usuário.

Para exportar informações de cards / negócios, é preciso que o usuário esteja na visualização de “tabela”.

Não é possível exportar dados como: notificações, opcionais de propostas, opcionais de vendas, opcionais de documentos, arquivos da Biblioteca, anexos e nenhum tipo de metadado (como as configurações e regras de negócio configuradas no sistema). As informações de propostas, vendas e documentos podem ser exportadas massivamente apenas no formato de dados, a exportação no formato de PDF é feita individualmente.

Relatórios podem ser exportados apenas na funcionalidade atualmente chamada “Relatórios beta”, e devem ser exportados um a um, não existe exportação de painéis.

Não é possível exportar e-mails da tela “E-mails”, embora seja possível exportar registros de interação do tipo e-mail. ‍

## Edição em massa

Uma das funcionalidades presentes nas aba do Ploomes (com exceção das abas de Documentos e Usuários) é a edição em massa. Ao acessar este menu, o usuário verá todos os campos daquela entidade principal e poderá selecionar aqueles que deseja alterar de forma massiva.

Ao escolher uma propriedade, o usuário definirá uma das operações:

- Substituir por - para alterar o valor deste campo em todos os itens da aba;
- Limpar - para remover o valor deste campo em todos os itens da aba, deixando o vazio.

Além disso, este tipo de edição permite a exclusão em massa dos itens da aba, deletando-os do sistema, de maneira **irreversível**.

É importante atentar-se às relações entre tabelas do sistema: os cards e documentos do Ploomes, por exemplo, podem estar vinculados a clientes. Se um cliente for excluído todos os seus negócios e documentos serão excluídos também. ‍

## Anexos

Através desta funcionalidade, o usuário poderá armazenar no CRM arquivos que possuam as seguintes extensões:

'.doc', '.docx', '.xlsx', '.xls', '.csv', '.png', '.jpg', '.jpeg', '.pdf', '.txt', '.odt', '.ppt', 'pptx', '.odp', '.gif', '.mp4', '.mp3', '.zip', '.rar', '.wmv', '.mov', '.bmp', '.tiff', '.mkv', '.avi', '.aac', '.flac', '.rm', '.rmvb', ‘.kmz’, ‘.kml’, ‘.dwg’, ‘.gpx’, ‘.bak’ e ‘.fld’.

Os anexos podem estar vinculados a clientes, cards / negócios, tarefas, e-mails (pontualmente) e a registros de interação.

Não existe uma forma de exportação em massa de anexos, ou seja, caso o usuário precise extrair arquivos do Ploomes, é preciso fazer o download manualmente de todos os materiais armazenados.

O tamanho máximo suportado pelo Ploomes é de 25 MB por arquivo. Cada usuário da conta possui 5 GB de armazenamento. ‍

## Perfis de usuário

Entre as ferramentas disponíveis para manipulação e visualização de dados no Ploomes, destaca-se o perfil de usuário. Até o momento, nós falamos sobre as funcionalidades do CRM para manuseio dos dados, mas os perfis de usuário permeiam o sistema completo, incluindo essas funcionalidades.

É no perfil de usuário que definimos as regras de permissão da plataforma. As regras são baseadas em dois pilares:

- **Permissões gerais:** perfis de usuário e equipes;
- **Permissões específicas:** abas, filtros, painéis de relatórios e metas, funis, modelos de documento e e-mail, seções de formulários, campos de formulários, pastas da biblioteca e grupos de produto.

### Permissões gerais

Primeiro, criamos um novo “Perfil” de usuário, que nada mais é do que um conjunto de regras que definem o que os usuários com aquele perfil podem ou não fazer no Ploomes. Este perfil, então, pode ser aplicado a um ou mais usuários.

Antes de entendermos as regras que o Ploomes permite configurar, é importante definirmos um conceito chamado **CRUD:** esta sigla vem das possibilidades de manipulação de dados de um cadastro dentro do Ploomes, que são:

- **C**reate: criação de um novo cadastro;
- **R**ead: visualização de um determinado cadastro;
- **U**pdate: edição de um cadastro já existente;
- **D**elete: exclusão de um cadastro já existente;

Grande parte das regras de perfil do Ploomes estão relacionadas à possibilidade ou não de um usuário realizar o CRUD para uma determinada entidade principal. Geralmente, a possibilidade de um usuário realizar ou não cada uma das 4 ações é separada, ou seja, é possível permitir que um perfil crie clientes, mas não edite.

‍

As regras do perfil são separadas por entidade e são configuradas da seguinte forma:

- **Equipes:**

  - Usuários do Ploomes podem ser alocados em uma ou mais equipes. Elas trabalham junto das regras de perfil de usuário para ampliar as possibilidades de nível de acesso.
- **Regras de cliente:**

  - **Visualização do módulo:** os usuários com este perfil podem visualizar o módulo de clientes?
  - **C (Create):** os usuários com este perfil podem criar novos clientes?
  - **RUD (Read, Update e Delete):** quais clientes este perfil poderá visualizar? e quais ele poderá editar? E quais poderá excluir? Neste caso, as permissões são baseadas em três propriedades: campo de responsável do cliente, campo de usuários colaboradores do cliente e campo de equipe do usuário. É possível restringir, por exemplo, a visualização dos clientes para somente aqueles que o usuário é responsável. Também é possível restringir a visualização para somente os clientes cujo responsável seja um membro de sua equipe;
  - **Responsável e Usuário colaborador:** é importante ressaltar que um cliente pode ter somente um responsável. Entretanto, o campo de usuários colaboradores é múltiplo e permite a seleção de vários usuários. Mas qual a diferença entre estes dois campos? Vamos imaginar o seguinte cenário: o Usuário A e o Usuário B possuem o mesmo perfil e estão dentro da mesma equipe. Este perfil diz que ambos podem visualizar somente os clientes que estejam sob responsabilidade de membros de sua equipe. Assim, se eu colocar o Cliente X sob a responsabilidade do Usuário A, tanto o Usuário A quanto o Usuário B conseguirão visualizá-lo. Entretanto, se eu colocar o Usuário A como Usuário Colaborador do Cliente X, somente o Usuário A conseguirá visualizá-lo. O Usuário B não;
  - **Comportamentos específicos:**

    - Se eu consigo visualizar um cliente, eu também consigo ver todas as pessoas, produtos do cliente e anexos vinculados a ele. Registros de interação e tarefas, no entanto, possuem um comportamento especial: caso estejam vinculados somente ao cliente, eu poderei visualizá-las caso eu tenha acesso ao cliente. Se estiverem vinculadas a um card / negócio, eu conseguirei visualizá-las somente se eu também conseguir visualizar o card / negócio (que, lembrando, possuem nível de acesso independente de clientes);
    - Se eu consigo visualizar um cliente, eu conseguirei visualizar todos os seus dados cadastrais, a menos que eu crie uma restrição de visualização de campos (explicado acima, no tópico “Formulários e campos”);
    - Para usuários que estiverem limitados a visualizar somente os clientes sob sua responsabilidade, clientes sem responsável ou clientes cujos responsáveis estiverem inativos também aparecerão para eles.
  - **Limitações:**

    - O Ploomes não possui um nível de permissões baseado em hierarquia. Vamos tomar o seguinte exemplo: temos 1 gerente, 2 coordenadores abaixo dele e 4 vendedores abaixo de cada coordenador. A estrutura mais comum é criar um perfil para cada cargo. No caso dos vendedores, definiríamos que eles poderiam visualizar somente seus clientes. Já para os coordenadores, faz mais sentido que eles visualizem os clientes de todos os seus vendedores. Para tanto, criamos uma equipe para cada coordenador, alocamos os seus vendedores dentro dela, e definimos que o perfil de coordenador pode visualizar clientes sob responsabilidade de membros de sua equipe. Mas e para o gerente? O que o Ploomes permite é usar o mesmo nível de acesso do coordenador, e alocá-lo nas duas equipes, assim ele consegue acompanhar o trabalho de todos os vendedores e coordenadores. Entretanto, como o gerente agora faz parte das duas equipes, caso ele tenha clientes sob sua responsabilidade, os dois coordenadores poderão ver seus clientes também;
    - Não é possível alocar uma equipe como responsável por um cliente, somente usuários. Entretanto, o Ploomes permite a criação de usuários sem login e sem custo. É possível, portanto, criar um usuário sem login com o nome de uma equipe e torná-lo responsável por um cliente. Desta forma, você pode alocar este usuário dentro de uma equipe com outros usuários e, dependendo do nível de acesso deles, poderiam visualizar o cliente em questão.
- **Regras de produto do cliente:**

  - **Dependência das permissões de cliente:** as permissões de produto do cliente dependem das permissões de cliente. Isso significa que, se eu não consigo visualizar o cliente, eu não consigo visualizar ou manipular os produtos vinculados a ele;
  - **Visualização do módulo:** os usuários com este perfil podem visualizar o módulo de produtos do cliente?
  - **CRUD simples:** os usuários com este perfil podem criar novos produtos de cliente? Podem ver produtos de cliente? Podem atualizar produtos de cliente? Podem deletar produtos de cliente? A diferença entre (I) CRUD de produtos do cliente e o (II) CRUD de clientes é que, no caso (I), a resposta é simples (SIM ou NÃO). No caso (II), a resposta é complexa (dentro da resposta SIM, ainda é possível definir QUAIS).
- **Regras de card / negócio:**

  - **Regras similares a clientes:** as regras que regem cards / negócios são basicamente as mesmas de clientes. Da mesma forma, os cards / negócios possuem um campo de responsável e um de usuários colaboradores;
  - **Visualização atrelada a clientes:** a primeira diferença está em uma regra especial para cards / negócios. Por ela, eu consigo definir que, caso eu visualize o cliente, eu também poderei visualizar todos os seus cards / negócios, independente se sou ou não responsável ou usuário colaborador do card / negócio;
  - **Ações específicas de cards / negócios:** a segunda diferença é poder definir se o usuário que contém um determinado perfil pode finalizar um negócio (seja ganhando, seja perdendo) ou reabrir um negócio já finalizado;
  - **Obs.:** as permissões de card / negócio e de cliente são independentes, ou seja, é possível visualizar um card / negócio vinculado a um cliente ao qual não tenho acesso.
- **Regras de proposta e documento de card / negócio:**

  - **Dependência das permissões de card / negócio:** as permissões de propostas e documentos de negócio dependem das permissões de card / negócio. Isso significa que, se eu não consigo visualizar card / negócio, eu não consigo visualizar ou manipular suas propostas e documentos. E o contrário é verdadeiro;
  - **Visualização do módulo:** os usuários com este perfil podem visualizar o módulo de propostas e de documentos?
  - **CRUD simples;**
  - **Ações específicas:** os usuários com este perfil podem compartilhar propostas e documentos?
- **Regras de documento de cliente:**

  - **Dependência das permissões de cliente:** as permissões de documento do cliente dependem das permissões de cliente. Isso significa que, se eu não consigo visualizar o cliente, eu não consigo visualizar ou manipular seus documentos. Do lado oposto, caso eu consiga visualizar o cliente, eu conseguirei visualizar seus documentos obrigatoriamente;**‍**
  - **Visualização do módulo:** os usuários com este perfil podem visualizar o módulo de documentos?**‍**
  - **CRUD simples;**
  - **Ações específicas:** os usuários com este perfil podem compartilhar documentos?
- **Regras de venda:**

  - **Regras similares a clientes:** as regras que regem vendas são basicamente as mesmas de clientes. Entretanto, vendas possuem somente um campo de responsável, usuários colaboradores não;
  - **CRUD simples;**
  - **Ações específicas:** os usuários com este perfil podem compartilhar vendas?
- **Regras de produto, grupos de produto e famílias de produto:**

  - **Visualização do módulo:** os usuários com este perfil podem visualizar o módulo de produtos?
  - **CRUD simples;**
  - **Obs.:** o Ploomes permite ocultar produtos de determinados grupos a usuários selecionados, mas isso será explicado em Permissões Específicas.
- **Outras configurações dentro de permissões gerais:**

  - Além das regras acima, o Ploomes possui possibilidade de configuração de outras regras mais específicas. Você pode verificá-las criando uma conta de testes de nossa ferramenta ou solicitando uma apresentação ao seu consultor Ploomes. Caso tenha alguma necessidade específica, você deve solicitar ao seu consultor Ploomes para que ele a descreva nesta proposta comercial, confirmando a capacidade do Ploomes em atendê-lo. Em hipótese alguma, a Ploomes será responsável por entregar qualquer configuração fora das limitações de nossa plataforma.

### Permissões específicas

As permissões específicas não ocorrem de forma geral, mas de forma pontual nos seguintes locais:

- Abas e filtros de clientes, cards / negócios, produtos, entre outras entidades que se utilizam da tabela dinâmica do Ploomes;
- Painéis de relatórios e metas;
- Metas específicas;
- Funis;
- Modelos de propostas, vendas e documentos;
- Modelos de e-mail;
- Seções e campos de formulários;
- Biblioteca;
- Grupos de produtos.

Todas as permissões acima são relacionadas à visualização de cada um dos itens. Para cada um dos itens acima, o padrão é a visualização estar disponível para toda a empresa. Entretanto, eu tenho a possibilidade de limitar esta visualização a somente alguns usuários ou a algumas equipes. Em alguns casos, também é possível restringir a visualização a determinados perfis de usuário.

Exemplo: eu posso criar uma nova aba na tela de clientes e definir que ela poderá ser visualizada somente por mim. Com isso, quando outros usuários entrarem na tela de clientes, esta aba não estará disponível para eles. É importante ressaltar que, caso eu crie uma aba para visualizar clientes de São Paulo, por exemplo, se eu não tiver nenhum cliente sob minha responsabilidade em São Paulo e meu perfil determinar que só posso visualizar clientes sob minha responsabilidade, a minha aba aparecerá vazia, ou seja, as Permissões Gerais são sempre prioritárias com relação às permissões específicas.

## Automações gerais

Ao contrário das automações de funil, as automações gerais não são disparadas de acordo com a movimentação dos cards / negócios dentro de um processo, mas, sim, com base em gatilhos que podem ser configurados nos seguintes cadastros / tabelas:

- Clientes;
- Cards / negócios;
- Vendas;
- Propostas;
- Produtos;
- Tarefas;
- Usuários;
- Registros de interação;
- Documentos;
- Produtos do cliente.

Assim como as automações de funil, as gerais possuem a mesma lógica de construção: definimos sempre um gatilho, filtros e, por fim, ações que acontecerão caso esse gatilho seja disparado.

No entanto, nesta funcionalidade possuímos outros tipos de gatilhos:

- **Quando um item for criado:** significa que a ação será disparada sempre que um item novo for inserido neste cadastro / tabela (uma nova empresa foi criada, por exemplo);
- **Quando um item for alterado:** significa que a ação será disparada sempre que um item deste cadastro / tabela for alterado (alteração do CNPJ de uma empresa, por exemplo);
- **Quando um item for excluído:** ação disparada quando o item é deletado do Ploomes - novamente, exclusões não são reversíveis, mas podemos, por exemplo, enviar um e-mail com os dados do item que está sendo excluído para facilitar recuperações manuais;
- **Quando um card / negócio for ganho:** esse gatilho é exclusivo para cards / processos. Significa que a ação será disparada quando um card / negócio for ganho;
- **Quando um card / negócio for perdido:** esse gatilho é exclusivo para cards / processos. Significa que a ação será disparada quando um card / negócio for perdido;
- **Quando um card / negócio for reaberto:** esse gatilho é exclusivo para cards / processos. Significa que a ação será disparada quando um card / negócio for reaberto;
- **Periodicamente:** esse tipo de automação afeta todos os itens do cadastro / tabela que satisfaçam a condição presente nos filtros configurados na automação. Esse tipo de automação é uma rotina criada com o objetivo de identificar determinados itens que satisfaçam determinados requisitos e, caso encontre algum, faça determinada ação. Um exemplo muito comum são os follow-ups automáticos ao longo do processo comercial: podemos criar uma rotina que, todos os dias, verifica os cards / negócios parados há 7 dias em determinada etapa do funil e, caso encontre algum, cria uma tarefa automática para o responsável do card / negócio.
- **Quando a proposta, venda ou documento for aprovada ou reprovada:** a finalização de um fluxo de aprovação (explicada no tópico **Documentos > Fluxos de aprovação**), seja ela positiva ou negativa, pode servir como gatilho para o disparo de ações;
- **Quando a proposta, venda ou documento for aprovada ou reprovada (online):** Como visto no tópico **Documentos**, é possível compartilhar documentos do Ploomes através da funcionalidade **Link Web**. Esse link possui dois botões de ação (aceitar / recusar) que, quando clicados, podem servir como gatilhos para o disparo de ações.
- **Quando a tarefa for finalizada:** ação disparada quando uma tarefa é finalizada;
- **Quando a tarefa for reaberta:** ação disparada quando uma tarefa é reaberta;

As ações disponíveis variam de acordo com o cadastro / tabela na qual a automação está sendo configurada, mas são elas:

- **Edição de dados:** a automação fará o preenchimento de um campo escolhido pelo usuário. Existem três formas de editar um campo

  - Com um valor fixo - significa que sempre que a ação for disparada, o mesmo valor será enviado ao campo editado;
  - Puxando a informação de um campo - significa que quando a ação for disparada, o valor enviado ao campo editado puxará o valor de outro campo;
  - Preenchimento com uma fórmula - significa que quando a ação for disparada, uma fórmula (JavaScript) será disparada e seu retorno será enviado como valor ao campo editado.
- **Enviar e-mail:** ação similar à descrita no tópico **automações de funil**;
- **Criar tarefa:** a automação criará uma tarefa. Durante a parametrização deste tipo de ação, o formulário de nova tarefa será exibido ao usuário, que deve preenchê-lo com as regras específicas daquela tarefa que será criada (determinando o usuário responsável, horário, entre outras informações da tarefa);
- **Criar negócio:** similar à criação de tarefas, mas, nesta ação, o usuário deve selecionar o processo / funil no qual o card / negócio será criado e, na sequência, preencher o formulário exibido;
- **Criar registro de interação:** similar à criação de tarefas e negócios, mas, agora, é exibido ao usuário o formulário de registro de interação;
- **Perder negócio:** quando disparada, essa ação fará com que o card / negócio seja perdido. O usuário pode determinar um motivo de perda durante a configuração deste tipo de ação;

### Limitações e comportamentos específicos de automações gerais

É possível criar até 100 automações para cada cadastro / tabela.

O histórico de automações pode ser consultado pelo administrador da conta. É possível filtrar o histórico com base no período, descrição da automação ou pelo ID do item que sofreu alguma alteração. Através deste histórico é possível visualizar o horário que a ação foi executada, bem como o resultado da mesma (sucesso ou fracasso);

Não é possível construir automações que sejam disparadas com a edição de um campo específico.

Não existe maneira de consultar a construção das automações que não seja na tela “Automações” da “Administração” (como fluxogramas).

Não é possível visualizar de forma geral quais campos são editados por automações, quais campos servem como filtros para automações. Para isso, é preciso que o usuário acesse automação por automação a fim de analisar o comportamento da mesma. ‍

## API e Webhook

Nossa API REST utiliza-se do protocolo OData para a manipulação das respostas. Em todas as requisições há a possibilidade de se utilizar as seguintes querystrings: $top, $skip, $select, $expand, $orderby e $filter.

**Limites importantes:**

- Processamento de até 120 requisições por minuto, considerando todos os usuários de integração da conta em conjunto, portanto, em caso de a sua solução precisar executar muitas requisições simultâneas, esteja preparado para processar respostas HTTP 429 - Too Many Requests;
- Algumas entidades possuem um limite de recursos que pode ser obtido em uma solicitação GET. Esse limite é de 300 itens para as entidades: Contacts, Deals, Cities, Tasks, Orders e Quotes;
- O máximo payload aceito pela API é de 10MB.

**Boas práticas:**

- Sempre use $top e $skip para paginação (tente limitar em páginas de até 100 itens) e $select para pegar apenas os dados essenciais;
- Assuma que sua aplicação irá competir por cotas, taxas e recursos de concorrência com outros aplicativos e defina limites de uso conservadores;
- Evite fazer chamadas de API simultâneas se o seu caso de uso não se beneficiar;
- Sempre que possível utilize requisições assíncronas para as API, assim você poderá lidar melhor com os limites e erros.

**Campos personalizados:**

- Como explicado no tópico **campos e formulários**, é possível criar propriedades dinâmicas no Ploomes, que também são disponibilizadas em nossa API. Caso uma tabela / cadastro tenha campos personalizados criados, eles serão listados em nossa API através de uma propriedade chamada “OtherProperties”;
- É possível consultar todos os campos (inclusive os personalizados) via API, utilizando a querystring $expand=OtherProperties.

A documentação completa da API da Ploomes pode ser encontrada em <https://developers.ploomes.com/>.

Nossos webhooks permitem a comunicação automatizada entre o Ploomes e outros sistemas, onde um evento no CRM dispara uma notificação (em forma de requisição HTTP) para outro sistema, permitindo a integração de informações em tempo real. É como um "aviso" enviado assim que algo relevante acontece, sem a necessidade de consultas manuais.

Na Ploomes, webhooks não possuem um front-end para configuração. Isso significa que a parametrização e o gerenciamento são feitos diretamente em nossa API, exigindo que o cliente defina manualmente os endpoints e parâmetros relevantes para a integração.

# Outras funcionalidades

## Resumo

É a tela inicial do Ploomes e seu objetivo é consolidar algumas informações relevantes que são cadastradas no restante do sistema. Sua estrutura não é alterável e ela possui as seguintes informações / funcionalidades:

- Indicadores (valor e quantidade) de negócios criados, propostas geradas e vendas realizadas;
- Publicações

  - São postagens exibidas na tela inicial e podem ser direcionadas para todos os usuários ou para equipes específicas. Essas postagens podem conter apenas textos e anexos (não suporta imagens, por exemplo).
  - As postagens podem receber comentários (notificando usuários, caso tenham sido marcados com “@”).
- Tarefas do dia

  - Nesta janela é exibido para o usuário quais são as suas tarefas atrasadas (cuja data é anterior a “hoje”) e, também, as suas tarefas do dia, nesta ordem;
  - Caso não exista nenhuma tarefa sendo exibida nesta janela, é possível clicar neste resumo para criar uma nova atividade.
- Situação dos negócios / cards

  - O usuário pode selecionar um funil (dentre os funis que possua visão) para exibir um resumo com as seguintes informações:

    - Quantidade de negócios / cards;
    - Valor total dos negócios / cards;
  - Essas informações são agrupadas por **estágio** do funil;
  - O usuário pode optar por exibir negócios “Em andamento” e/ou “Ganhos” e/ou “Perdidos”, bem como por apenas aqueles pelos quais é responsável ou, também, que estejam sob responsabilidade de outros usuários (desde que ele tenha permissão para visualizar esses negócios / cards);
  - Por fim, o usuário ainda pode optar por criar filtros, utilizando outras propriedades para afunilar sua visualização.
- Atividades

  - Essa tela centraliza todas as atividades realizadas no Ploomes e as exibe em formato de linha do tempo, através de um scroll infinito. Os usuários podem escolher visualizar apenas as suas atividades ou todas as atividades (desde que tenham permissão para visualizá-las).

## Relatórios básicos

O Ploomes, por padrão, conta com gráficos pré-configurados, que não podem ser excluídos e editados sem a contratação do módulo “Analytics”.

‍

## Analytics

Os relatórios e metas do Ploomes se comportam como um consultor de dados armazenados nas diversas tabelas do CRM, agregando-os e exibindo-os para os usuários a fim de trazer informações relevantes para a operação do dia a dia.

As agregações disponíveis são: soma, média, máximo, mínimo e contagem. Ou seja, o Ploomes não gera tendências e não faz contas específicas para cálculo de taxas.

As metas estão disponíveis para consulta na tela “Resumo”. Já os relatórios possuem uma tela específica, que pode ser acessada no menu lateral esquerdo.

Durante a construção de metas, criamos painéis e definimos quais usuários poderão visualizá-los. Para cada painel, parametrizamos as metas em si, que são um conjunto de regras que visam indicar ao Ploomes qual é o resultado a ser atingido e como ele será metrificado.

Esse conjunto de regras inicia-se com a definição do dado que será monitorado e como ele será agregado (valor dos negócios, quantidade de propostas, quantidade de registros de interação, entre outros). Em seguida, definimos quais usuários ou equipes deverão atingir essa meta, bem como o papel que eles devem desempenhar para que um item seja contabilizado nesta meta.

Um exemplo é a meta de visitas, na qual o dado monitorado pelo Ploomes são os **registros de interação do tipo visita**, e o responsável pela meta é o usuário X, desempenhando o papel de **criador** ou **usuário** da visita realizada.

Na sequência, definimos períodos para a meta (diárias, semanais, mensais, anuais etc) e os respectivos resultados esperados para cada período. Por fim, podemos organizar os painéis adicionando cores específicas para cada meta criada.

Embora o painel possua níveis de acesso, cada meta também possui sua própria regra de permissão. Ou seja, um usuário pode visualizar um painel, mas não todas as metas configuradas nele.

Não é possível importar e exportar metas do Ploomes.

A única forma de visualização das metas é a barra horizontal. Não existem outras formas de visualização (como velocímetro, por exemplo).

As metas não são atualizadas automaticamente, é sempre necessário uma atualização na tela do usuário.

Os cadastros / tabelas disponíveis para a construção de metas são:

- Clientes;
- Cards / negócios;
- Venda;
- Proposta;
- Documento;
- Produto da venda;
- Produto da proposta;
- Produto do documento;
- Tarefa;
- Registro de interação

Não é possível, por exemplo, configurar metas relacionadas a opcionais de propostas, vendas e documentos.

De forma semelhante às metas, os relatórios também são divididos em painéis com níveis de acesso (quem pode visualizar, editar e / ou excluir o painel). No entanto, nesta tela, os gráficos criados serão visíveis para todos os usuários que possam ver o painel, porém, os dados exibidos para cada usuário depende do nível de acesso do seu perfil.

Os gráficos disponíveis para criação são:

- Análise histórica do funil;
- Gráfico de área;
- Gráfico de barra;
- Gráfico de donut;
- Gráfico de funil;
- Gráfico de linha;
- Gráfico de pizza;
- Indicador;
- Mapa;
- Tabela.

Assim como para as metas, durante a construção dos gráficos, precisamos selecionar qual cadastro / tabela do sistema será utilizado como fonte de dados (ex: vendas). Na sequência, devemos escolher qual será a agregação dos dados. A terceira etapa consiste em escolher o campo do cadastro / tabela que será utilizado na operação matemática definida (ex: soma de valor da venda). No caso da agregação "contagem", não existe esta etapa porque a contagem é feita diretamente em cima da entidade selecionada. Podemos, ainda, definir filtros que reduzem e afunilam os dados que serão agregados no gráfico desejado. Por fim, escolhemos a forma de agrupar os dados (por cliente, por data, por responsável etc).

Os painéis de relatórios possuem um mecanismo de filtragem diferente do restante do Ploomes, chamados “Filtros rápidos”. Durante a criação de um filtro rápido, o usuário escolhe um tipo de campo (dentre as opções listadas no tópico **formulários e campos**) e, na sequência, escolhe o campo deste tipo que será filtrado em cada um dos gráficos que utilizam campos deste tipo em sua construção.

Os dados são sincronizados de 15 em 15 minutos, mas o usuário pode forçar a atualização individual dos gráficos clicando no ícone de atualização.

Os gráficos possuem a opção de visualização detalhada (drill down), que exibe os itens que compõem o resultado do gráfico. A tela de detalhamento e seus comportamentos não são customizáveis.

Os gráficos também podem ser exportados no formato csv.

Gráficos de tabela exibem até 10.000 linhas. Caso o retorno do agrupamento seja selecionado, o gráfico é exibido com uma mensagem de erro.

O gráfico “Análise histórica do funil” não é customizável, isto é, os dados exibidos são sempre fixos e podem, no máximo, serem filtrados durante a sua criação. Esse gráfico tem dois tipos de visualização: por quantidade (contagem de cards / negócios) ou por valor (soma do campo “Valor” dos cards / negócios). A taxa de conversão exibida para o usuário é a divisão dos negócios ganhos pela soma dos negócios ganhos com os negócios perdidos e sua alteração não é possível.

Limites do módulo de Analytics:

![Imagem 3: Limites do módulo de Analytics:](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2270835756/ae29d5d347b9d04786b9b09bb2e1/Captura+de+tela+2026-04-13+153551.png?expires=1786860000&signature=129e3639ee9edc99d8111d10a1389a234dd966f7c911a6abe37bc37f153bdbed&req=diIgFsF9mIZaX%2FMW3nq%2BgdazHl5DwUlw6e680XSL%2FQVBTZCBYNDim6Drlr4U%0AwOH62gD6GRCZ0gC4bEqLZNbtHzw%3D%0A)

## E-mail

O Ploomes pode ser integrado com seu servidor de e-mails para envio (SMTP) e recebimento de mensagens (IMAP) automaticamente dentro do CRM, facilitando o armazenamento do histórico de relacionamento com seus clientes.

A integração é sempre realizada por cada um dos usuários, isto é, cada uma das licenças deve realizar as configurações necessárias para habilitar o envio e / ou recebimento dos e-mails.

Caso a integração seja com o Gmail ou Outlook, é essencial que os usuários criem senhas de segurança específicas nestes aplicativos, para que o servidor de e-mails da Ploomes se torne autorizado.

O provedor de emails Gmail limita o número de conexões simultâneas para o uso do IMAP e SMTP em 20 conexões simultâneas.

Uma vez que a integração de e-mails esteja habilitada, é possível vincular os e-mails recebidos aos clientes (com atenção às regras de permissão destacadas no tópico **“Perfis de usuário”**), bem como configurar uma assinatura padrão, utilizada pelo Ploomes quando o usuário enviar um e-mail de dentro do CRM.

É possível criar um endereço de encaminhamento específico para o Ploomes, usando o domínio @mail.ploomes.com. Esse encaminhamento fará com que os e-mails recebidos por esse endereço customizado sejam direcionados para a Caixa de Entrada do usuário no CRM.

No Ploomes, conseguimos configurar modelos de e-mails, que nada mais são do que templates pré-prontos, úteis para poupar tempo durante o cotidiano dos usuários É possível, portanto, criar modelos que façam conexão entre equipes, follow-ups, entre outros. Os modelos podem ser restritos para determinados usuários ou equipes. Na construção desses templates, conseguimos adicionar propriedades variáveis, que serão substituídas automaticamente pelo sistema, como “Nome do cliente” e outros campos de cards / negócios e de contatos.

Com a integração parametrizada, os usuários podem criar e excluir pastas, para melhor organizar os e-mails recebidos dentro do próprio CRM.

Os e-mails podem ser buscados por assunto, anexo, destinatário, remetente, cópia ou cópia oculta. Além disso, podem ser filtrados com base nas propriedades do e-mail, como: data, se o e-mail foi lido ou não, card / negócio ou cliente vinculado ao e-mail entre outras.

Ao enviar e-mails pelo Ploomes, o usuário pode optar por ocultar o conteúdo. Dessa forma, o registro de interação criado ficará visível apenas para o remetente.

## Notificações

Durante o uso do CRM, diversas ações geram notificações aos usuários com a finalidade de avisá-los sobre marcações, novos itens sob sua responsabilidade, entre outros avisos que sejam pertinentes à execução de suas atividades do dia a dia.

As notificações ficam centralizadas no “sino”, localizado sempre no canto superior direito da tela do usuário, com comportamento similar às notificações de diversas redes sociais.

Ao clicar neste ícone, o usuário consegue acessar a tela “todas as notificações”, que as exibe no formato de tela cheia, permitindo também a exibição apenas das notificações não lidas, facilitando a visualização do usuário dos itens que ainda não foram checados.

‍

Todas as notificações que chegam através do “sino” são nativas do sistema, isto é, não é possível configurar novas notificações, tampouco customizar a mensagem que o usuário visualiza ao clicar no “sino”.

## Calendário e tarefas

É através dessa funcionalidade que os usuários podem acompanhar seus próximos passos, agendar compromissos e tarefas, bem como consultar a disponibilidade e agenda de outros usuários (sempre com base nas permissões do seu perfil).

As tarefas podem estar vinculadas a clientes e / ou a cards / negócios. Quando esse vínculo existir, será possível acessar o item através da tarefa e, quando estiver na tela do item, essa atividade será exibida no início da linha do tempo, na seção chamada “Tarefas em aberto”.

Tarefas finalizadas são automaticamente transformadas em Registros de interação.

Caso uma tarefa não possua vínculo com nenhum cliente, ela será visível apenas para os usuários da tarefa, mesmo administradores não poderão visualizá-la. Esse comportamento específico faz com que seja possível a gestão até mesmo de tarefas pessoais dentro do Ploomes.

O calendário pode ser integrado com o Google Calendar ou com o Outlook 365 Web. Caso uma dessas integrações esteja habilitada (isso é feito por cada um dos usuários, não pela conta como um todo) e o usuário tenha selecionado “Contatos relacionados” na tarefa, ele poderá disparar um convite para os e-mails desses contatos. Tarefas integradas ganham um destaque visual no calendário, indicando ao usuário o sucesso ou fracasso da integração daquele compromisso com a ferramenta integrada.

As tarefas possuem um formulário que não pode ser alterado. Assim como os “Registros de interação”, as tarefas também possuem os mesmos “tipos”. Por isso, é possível apenas escolher quais são os tipos de tarefas que podem ser criados (sempre excluindo os indesejados e nunca criando novos tipos de tarefas).

Cada “tipo” possui uma cor específica, que não pode ser alterada.

O campo “Endereço”, ao ser preenchido, fará com que a tarefa possa ser visualizada no mapa, assim como no cadastro de clientes.

As tarefas possuem a seção “Comentários”, na qual o usuário pode incluir anotações, inclusive marcando outros usuários.

Usuários marcados em comentários não são adicionados como usuários da tarefa, mas usuários marcados no campo “Descrição” da tarefa são.

Pela tarefa é possível visualizar dados do cliente. Caso o cliente seja uma empresa, o usuário verá a lista de pessoas vinculadas àquela empresa. Caso o cliente seja uma pessoa, o usuário verá os dados cadastrais daquela pessoa (e-mail e telefone, apenas).

Ademais, caso a tarefa esteja vinculada a um cliente (independente do seu tipo), as Atividades (linha do tempo) daquele cliente pode ser visualizada na tela da própria tarefa.

Não é possível customizar as ações que acontecem na tela do usuário ao finalizar uma tarefa (por exemplo, não é possível abrir o formulário de “Nova tarefa” quando uma tarefa é finalizada). Ao finalizar uma tarefa, o usuário é automaticamente redirecionado para a última tela acessada (geralmente, o próprio calendário).

Existem duas maneiras de finalizar tarefas:

- Finalizar com observações - um pequeno formulário é exibido ao usuário, obrigando-o a preencher uma descrição, que será levada ao histórico;
- Finalizar - neste caso, a tarefa é simplesmente finalizada, sem a necessidade do preenchimento obrigatório da descrição.

As tarefas criadas são visualizadas de diversas formas, sendo a mais comum dela, o calendário. Embora as tarefas possam ser filtradas como os demais cadastros / tabelas do Ploomes, nessa tela existe um botão especial chamado “Exibir”, no qual o usuário pode escolher por visualizar apenas as suas tarefas (e / ou a de outros usuários - caso seu perfil permita), bem como por visualizar apenas tarefas em aberto e / ou finalizadas.

Na visualização de calendário, o usuário ainda pode optar por ver as tarefas de três formas:

- Mês - visão na qual todos os compromissos do mês atual serão exibidos na tela, podendo o usuário navegar entre meses anteriores e futuros;
- Semana - visão na qual apenas os compromissos da semana, podendo o usuário navegar entre semanas anteriores e futuras;
- Agenda - visão semelhante à semanal, porém com uma dimensão adicional: os horários do dia. Tarefas sem horário definido ficam dispostas no topo da tela quando essa é a visão escolhida.

Já na visualização em lista, as tarefas são visualizadas linha a linha, da mais antiga para a mais recente. Por essa tela, o usuário consegue facilmente finalizar e / ou abrir as tarefas, clicando no círculo disponível na lateral esquerda de cada tarefa.

Por fim, é possível exibir as tarefas em abas, usando a visualização em tabela. Nessa visualização, as mesmas funcionalidades descritas em “**Abas e tabelas dinâmicas**” estarão disponíveis para o usuário, como, por exemplo, a escolha de colunas a serem exibidas e a exportação dos dados para uma planilha Excel.

Tarefas, assim como cards / negócios, podem ser reabertas. Tarefas reabertas não apagam o registro de interação criado em sua finalização.

A inclusão de usuários em uma tarefa é sempre feita de forma unitária. Portanto, não há como incluir todos da empresa ou equipes de forma massiva como usuários de uma tarefa.

O calendário do Ploomes não pode ser compartilhado externamente. Isso significa que não há como gerar um link público que permita a outras pessoas visualizarem as tarefas desse calendário ao acessá-lo.

## Cadastro de cidades

As cidades cadastradas no Ploomes possuem duas propriedades adicionais: Estado e País. Por padrão, o Ploomes já possui o cadastro de todos os municípios brasileiros, bem como seus respectivos estados.

Para possibilitar o cadastro de cidades estrangeiras, ao digitar o nome de uma cidade não existente, o usuário poderá indicar qual é o Estado e País daquela nova cidade. A fim de facilitar esse cadastro, nós já trazemos a lista de todos os países do mundo, mas os estados precisam ser cadastrados manualmente, exceto para os países: Estados Unidos, México e Portugal - estes já possuem seus estados nativamente cadastrados.

## Administração

### Configurações do sistema

O administrador pode determinar:

- Se os e-mails enviados pelo Ploomes por usuários com integração SMTP serão copiados na caixa de entrada deste usuário;
- Se no primeiro login de um usuário ele verá um vídeo tutorial (padrão para todos os clientes Ploomes) ou um formulário específico para a sua conta (para enriquecimento de dados do cadastro de “Usuários”);
- A linguagem geral do sistema dentre as seguintes possibilidades:

  - Português (Brasil);
  - Português (Portugal);
  - Inglês;
  - Espanhol (México).

    - Embora o administrador possa escolher a linguagem geral do sistema, cada usuário pode definir a sua linguagem preferida através do seu “Perfil” > “Configurações do usuário”.
- Quais serão as moedas disponíveis no sistema (são utilizadas, por exemplo, na tabela de cards / negócios para somar os valores das oportunidades);
- Qual será o fuso horário do sistema.

### Configurações de segurança

O administrador pode determinar:

- Se é obrigatório o cadastro de uma senha forte (8 ou mais caracteres, uma ou mais letras maiúsculas, uma ou mais letras minúsculas, um ou mais números e um ou mais caracteres especiais);
- Se as senhas devem expirar ou não. Em caso positivo, é possível determinar:

  - Quanto tempo cada senha dura;
  - Com quantos dias de antecedência o usuário deve ser notificado que a senha irá expirar?
  - O número máximo de senhas armazenadas (1 a 10).
- A política de acesso de suporte da Ploomes, optando entre:

  - Exigir a aprovação do acesso de membros do suporte pelos administradores da conta (determinando uma data limite para que o acesso expire);
  - Não é necessário aprovar o acesso dos membros do suporte.
- Autenticação multifator, optando entre:

  - Nenhuma;
  - E-mail;
  - Google Authenticator.
- Configuração de opções de login, optando entre:

  - Permitir todas as formas de login - por usuário Ploomes e via SSO (Single Sign-On), utilizando suas credenciais Microsoft, via Entra ID;
  - Permitir login apenas por SSO.

Para utilizar o login via SSO (Entra ID), existem os seguintes pré-requisitos:

- Ter o módulo habilitado no Ploomes;
- É necessário que o administrador da conta tenha permissões no ambiente Microsoft Entra ID;
- Os usuários devem estar previamente cadastrados na Microsoft com os dados corretos (nome, e-mail e telefone);
- Nas propriedades do Aplicativo Empresarial, deve ser marcado a opção “Atribuição Necessária” como SIM. Caso não seja marcada essa opção, não será possível localizar o usuário no fluxo de login do Ploomes;

**Obs: pode ser necessário realizar a autorização da integração no Ploomes (através do menu Integrações plug and play) para que a aplicação seja exibida na aba "Aplicativos Empresariais" dentro da plataforma da Microsoft.**

Sobre a sincronização de dados quando o login é feito via SSO:

- Alterações em nome, e-mail telefone devem ser feitas na Microsoft e serão sincronizadas no Ploomes de forma automática, podendo levar até 5 minutos para a atualização dos dados;
- Novos usuários criados na Microsoft e vinculados ao Entra ID serão importados e atribuídos a um novo perfil nomeado como “**MicrosoftSSO”**, com permissões equivalentes ao perfil padrão **Funcionário**;
- Se um e-mail já existir no Ploomes vinculado a um usuário, ele será atualizado. Caso esteja vinculado a outra conta, será exibido um alerta e o usuário não será criado;
- A sincronização ocorre via webhooks de forma automática, e o tempo para que a atualização dos dados ocorra no Ploomes pode levar até 5 minutos;
- A sincronização também pode ser acionada manualmente pelo usuário de perfil administrador através do botão “Atualizar integração”, e o tempo para que a atualização dos dados ocorra no Ploomes pode levar até 5 minutos;
- A alteração do status de um usuário (habilitar/desabilitar acesso) deve ser feito pela Microsoft, e o tempo para a atualização refletir no Ploomes pode levar até 5 minutos.

Sobre a ocultação de Fluxos Padrão com o login via SSO ativado:

- Os fluxos **“Recuperar Acesso”** e **“Alterar Senha”** são ocultados;
- Edição de dados cadastrais do usuário e desativação de acesso ao Ploomes só podem ser feitos via Microsoft;
- Ao desativar o SSO, os fluxos mencionados serão reexibidos no Ploomes.

Limitações da Integração Microsoft SSO (Entra ID):

- **Conflito de contas** - contas com o mesmo e-mail vinculadas a diferentes organizações não poderão ser integradas simultaneamente. O sistema exibirá uma mensagem listando as contas não integradas.
- **Desativação de um usuário** - ao desativar um usuário na Microsoft, o sistema levará cerca de 5 minutos para bloquear o acesso do usuário no Ploomes.
- **Atualizações de dados de um usuário** - ao atualizar um usuário na Microsoft, o sistema pode levar cerca de 15 minutos para atualizar as informações no Ploomes.

## Formulários externos

Formulários externos são páginas web geradas pelo Ploomes que permitem o preenchimento de dados por fora da ferramenta.

É possível criar formulários externos para duas entidades do Ploomes:

- **Clientes:** após preenchimento de um formulário externo, um cliente (pessoa ou empresa) é criado ou atualizado no Ploomes;
- **Cards / Negócios:** após preenchimento de um formulário externo, um negócio / card é criado. Como cards / negócios podem estar vinculados a clientes e contatos, uma empresa e uma pessoa também podem ser criadas juntas.

Existem dois tipos de formulário externo:

- **Atualização de dados:** este tipo de formulário existe para atualizar dados de clientes e cards / negócios. Dentro de um cliente, por exemplo, ao ligar seu formulário externo, o Ploomes vai gerar uma URL específica daquele formulário para aquele cliente. Quando preenchido, os dados do cliente presentes no formulário serão atualizados no Ploomes. Este tipo de formulário é ideal para o terceiro caso de uso citado acima (formulário de cadastro);
- **Criação de entidades:** diferente do caso acima, onde o formulário possui um link especial por cliente ou por card / negócio, os formulários de criação de entidades possuem uma única URL global. Portanto, este tipo de formulário, em vez de atualizar um cliente ou card / negócio já existente, cria um novo cliente ou card / negócio. Ainda sim, é possível criar regras para evitar a criação de cadastros duplicados. Vamos tomar como exemplo o primeiro caso de uso citado acima (captura de leads). Imagine que um lead preencha duas vezes o formulário pelo seu site. Não queremos que duas empresas sejam criadas no Ploomes. Portanto, podemos definir que o CNPJ, por exemplo, se transforme em um campo chave. Neste caso, em vez de criar um novo cliente, o formulário vai somente atualizar aquele cliente já existente.

Além dos comportamentos destacados acima, destacamos que:

- É possível selecionar de um Logotipo que vai aparecer com destaque no canto superior esquerdo do formulário;
- É possível definir um “Nome” para o formulário. Ele aparece em letras grandes logo abaixo do logotipo;
- É possível definir uma “Descrição” para o formulário. Ela aparece em letras menores abaixo do nome. A descrição permite a inclusão de códigos em HTML para maior capacidade de customização;
- É possível definir uma cor de fundo para o formulário;
- Para formulários de card / negócio, É possível definir a qual funil ele está relacionado;
- É possível definir um quais campos deverão ser preenchidos pelo formulário:
- Todo campo do formulário está relacionado a um campo do Ploomes;
- Não é possível listar dados do Ploomes no formulário (ex.: não consigo ter um campo no formulário externo que liste os clientes ou usuários de sua conta Ploomes);
- É possível alterar o nome do campo que aparece no formulário externo para ficar mais intuitivo a quem vai preencher. Também é possível escrever um texto de apoio que aparece em uma cor mais clara logo abaixo do nome do campo.
- Além dos campos preenchidos pelo formulário, existe a possibilidade de configurar o preenchimento de outros campos de forma automática, sem que eles apareçam no formulário. Exemplo: depois que o formulário externo de atualização for preenchido, eu posso fazer com que o estágio do meu card / negócio seja alterado para o estágio X;
- Por fim, para o caso de formulários de criação de entidades, o Ploomes gera um código especial que você pode copiar e colar dentro de uma página de seu site. Embora ele envie apenas os campos em um fundo branco, caso você queira customizar seu layout, você precisará trabalhar com Javascript para incluir estilizações no iFrame gerado por nosso código;
- Não é possível listar itens com suas respectivas informações como quantidade, valores e demais informações relacionadas ao produto;
- Não é possível armazenar tags de outros sites (como campanhas do Google) dentro dos formulários para trazer este dado ao Ploomes;

## Registros (logs)

Durante o uso do Ploomes, os administradores podem recorrer à tela de Registros para consultar criações, alterações e até mesmo deleções dos mais diversos itens, sendo útil para a investigação de possíveis erros que podem acontecer cotidianamente.

Essa tela é separada em dois tipos de visualização: registros de modificação e registros de navegação.

Registros de modificação são criados automaticamente sempre que uma ação é realizada dentro do CRM: criação, edição ou deleção de um item. Nessa tela o administrador poderá visualizar as seguintes informações:

- Usuário responsável pela ação;
- A ação em si;
- Entidade base (o cadastro / tabela);
- Id do item;
- Data e hora da ação.

Ao acessar um registro específico, o administrador verá um JSON com todos os dados existentes. Ao passar o cursor por cima de uma linha do JSON, o “Nome” do campo é mostrado na tela, para facilitar a visualização.

Ao acessar os registros de **edição** de algum item, o administrador verá o JSON do item antes da modificação e depois da modificação. Os campos que sofreram alterações são destacados em **negrito**, a fim de facilitar a identificação dos dados que foram alterados naquela ação.

Embora os registros de deleção de itens estejam disponíveis, não é possível realizar nenhum tipo de reversão (recuperação de dados).

Já os registros de navegação mostram ao administrador a relação de páginas acessadas por cada um dos usuários do sistema. Além disso, a página ainda mostra informações como:

- Data e hora;
- Plataforma (Web ou Mobile);
- IP.

Os dois tipos de registros podem ser filtrados por essas propriedades, potencializando pesquisas específicas:

- Data de início;
- Data de fim;
- Nome ou e-mail do usuário;
- ID do item.

O Ploomes guarda registros durante 6 meses. Após esse período eles expiram e não podem ser consultados. Registros não podem ser exportados (não é possível gerar uma planilha de Excel, por exemplo, com os registros do Ploomes).

## Biblioteca

Essa funcionalidade centraliza e organiza os anexos da conta através de uma estrutura de pastas hierarquizadas. Por ela é possível unificar o compartilhamento de apresentações, planilhas, imagens, vídeos e outros tipos de arquivos para os usuários do Ploomes.

Essa ferramenta pode ter seu ícone e nome alterados.

Antes de entrarmos nas regras e limitações específicas da Biblioteca, vamos destacar as extensões de arquivos aceitas pelo Ploomes:

'.doc', '.docx', '.xlsx', '.xls', '.csv', '.png', '.jpg', '.jpeg', '.pdf', '.txt', '.odt', '.ppt', 'pptx', '.odp', '.gif', '.mp4', '.mp3', '.zip', '.rar', '.wmv', '.mov', '.bmp', '.tiff', '.mkv', '.avi', '.aac', '.flac', '.rm', '.rmvb', ‘.kmz’, ‘.kml’, ‘.dwg’, ‘.gpx’, ‘.bak’ e ‘.fld’.

‍

Qualquer arquivo inserido fora desse padrão retornará uma mensagem de erro.

Além disso, o Ploomes possui um limite de 25MB para cada arquivo armazenado e cada usuário pode armazenar, no máximo, 5GB.

Dentro da Biblioteca, podemos criar pastas e, nelas, podemos criar sub-pastas e / ou subir arquivos.

É possível criar até 100 pastas-mãe (pastas que estão no primeiro nível da hierarquia). Cada pasta-mãe pode ter até 7 sub-pastas vinculadas a ela. Em cada pasta, podemos criar “Coleções”, que são agrupamentos de arquivos dentro daquela pasta.

Os arquivos podem ser armazenados de duas maneiras. A primeira consiste em clicar no botão “Criar” no topo da tela e depois escolher a opção de subida de arquivo [Criar > Upload de arquivos].

A segunda alternativa é abrir o gerenciador de arquivos do computador e arrastar os arquivos desejados para a tela do Ploomes. É necessário arrastar e soltar na tela que representa o interior da pasta. Se soltar em cima do nome da pasta, não funcionará.

Além disso, é possível subir mais de um arquivo de uma só vez. No gerenciador de arquivos do computador, selecione vários documentos arrastando o cursor por cima deles ou selecionando um por um com o botão CTRL.

Uma vez que os arquivos estão armazenados, temos as seguintes ações disponíveis:

- **Baixar**

  - Essa ação faz download dos itens selecionados no computador do usuário. Se uma coleção for baixada, todos os itens dentro dela são baixados.
- **Excluir**

  - Apaga os itens e as coleções selecionadas. A coleção é uma entidade que vincula vários itens como um só grupo. Ao excluir uma coleção, o que se perde é o vínculo entre os itens e não os arquivos em si. Esses arquivos continuarão na pasta onde foram subidos.
- **Enviar por e-mail**

  - Esta ação abre o modal de envio de e-mail com os itens selecionados anexados ao corpo do e-mail. Se uma coleção for enviada por e-mail, seus arquivos serão compactados e anexados no corpo do e-mail no formato zip.
- **Renomear**

  - Esta ação permite a mudança da nomenclatura dos itens e das coleções.
- **Mover**

  - Itens e coleções podem ser movidos para outras pastas que o usuário tenha permissão de acesso. Um usuário não poderá mover arquivos para pastas que não pode ver ou que não pode editar.

A Biblioteca possui uma rede de permissões complexa, a fim de preservar a integridade e o acesso aos arquivos com grande flexibilidade.

É possível determinar, para cada perfil de usuário, se ele poderá ou não (a) visualizar a Biblioteca e (b) se poderá criar pastas-mãe.

‍

**Permissões das pastas**

As permissões existentes para as pastas e seus arquivos são: visualização, edição e exclusão. Os usuários que puderem ver uma pasta, também têm permissão para visualizar e baixar os arquivos contidos naquela pasta. A permissão de edição permite a criação e a movimentação da pasta e de seus arquivos. Por fim, a permissão de exclusão permite que o usuário exclua a pasta e seus arquivos.

‍

**Hierarquia das permissões**

Cada pasta tem sua própria permissão, que é limitada sempre pelas regras de permissão da pasta anterior. Isso quer dizer que a pasta anterior à pasta que está sendo configurada sempre vai limitar as possibilidades de regras que poderá receber, mas as pastas-mãe, por serem as primeiras da hierarquia, têm mais flexibilidade de permissões e ditam o comportamento das demais pastas abaixo delas.

‍

**Hierarquia dos tipos de permissões**

Além disso, a pasta-mãe também tem o papel de ditar o tipo de permissão das suas sub-pastas; se é por usuário, por perfil ou por equipe. O tipo de permissão deve se manter o mesmo em toda árvore da pasta-mãe e o próprio sistema não vai permitir a mudança para outro tipo senão o definido como padrão.

Caso uma pasta-mãe possa ser vista apenas pelo usuário A e B, uma sub-pasta dessa pasta-mãe não poderá ser vista pelo usuário C.

‍

**Mudanças nas permissões**

É possível editar as permissões de pastas uma vez que as permissões de uma árvore de pastas já tenham sido criadas. O usuário deve proceder com cautela porque o tipo de modificação pode acarretar em propagações equivalentes nas sub-pastas da pasta editada.

‍

**Edição do tipo de permissão**

A alteração do tipo de permissão para outro propaga nas sub-pastas a mesma permissão nova. Exemplo: se uma estrutura está configurada com um tipo de permissão de perfil de usuário e o tipo for trocado para equipe, todas as sub-pastas terão a mesma alteração de permissão da pasta-mãe.

‍

**Edição de uma pasta pública para se tornar restrita**

Se uma estrutura de pastas estiver totalmente irrestrita e o usuário trocar a permissão da pasta-mãe para uma configuração restritiva, todas as suas sub-pastas herdarão a mesma restrição.

‍

**Edição de uma pasta restrita para se tornar pública**

Em uma árvore de pastas restritas, a liberação da permissão para todos da pasta-mãe não afeta as suas sub-pastas. Elas vão continuar com as mesmas restrições anteriores e se o usuário quiser, conseguirá liberar uma a uma.

‍

**Inserção e remoção de permissões**

Se uma nova alternativa for incluída ou se uma já existente for excluída na pasta-mãe, ela vai ser propagada e incluída/excluída em todas as sub-pastas.

‍

**Movimentar pastas e arquivos**

Os usuários do sistema têm a possibilidade de movimentar pastas, itens e coleções para outras localidades dentro do módulo, porém seguindo as suas permissões de visualização e edição. Os comportamentos esperados das movimentações são os seguintes:

**Manutenção das permissões** - As permissões das pastas movidas se manterão as mesmas quando:

- As pastas possuem o mesmo tipo de permissão;
- A pasta de origem possui uma restrição, mas a pasta de destino está com visualização para todos da empresa;
- A pasta origem possui restrições que estão contidas nas restrições da pasta destino.

**Perda de parte das permissões** - Há perda de parte das permissões quando:

- Pasta de origem for mais restrita do que a pasta de destino, sendo que a pasta de origem contém as permissões da pasta destino.

- **Perda completa das permissões** - A situação em que todas as permissões são perdidas e somente o administrador da conta terá acesso é:

  - Uma pasta e suas sub-pastas são movidas para dentro de uma pasta restrita.

**Utiliza as permissões da pasta superior** - As situações em que a pasta movida replica as permissões da nova pasta superior são:

- As pastas possuem o mesmo tipo de configuração de permissões, porém contém permissões não compatíveis;
- As pastas possuem configurações de tipos de permissões diferentes.

**Busca e filtros**

A Biblioteca conta com duas funcionalidades para auxiliar na busca de itens e coleções. A busca fica no canto superior esquerdo da tela e está presente em todas as suas páginas. O usuário pode pesquisar arquivos pelo nome e pelo formato (jpeg, pdf, ppt, etc.). Também é possível pesquisar pastas por nome.

Já os filtros se comportam igual aos componentes de filtros já existentes no Ploomes. Podemos filtrar os arquivos por nome, pelo tipo (item ou coleção), pelo formato (PDF, JPEG, etc.) ou pelos campos dinâmicos das coleções.

‍

**Vínculo da Biblioteca com outros cadastros / tabelas**

- **Comportamento do vínculo de anexos com itens:**

  - É possível subir anexos diretamente das tabelas de negócios, clientes e produtos tanto para o módulo quanto para a tabela escolhida. Vale salientar que os itens não vão herdar as regras de permissões de seus anexos de origem. Se um anexo inserido na página de um cliente restrito para somente o responsável for vinculado à Biblioteca e a pasta estiver aberta para todos da empresa, então todos os usuários verão este item na Biblioteca. As restrições configuradas devem ser rígidas quando o sistema de regras de perfil da conta for mais restritivo para assegurar a segurança dos dados.

- **Comportamento do vínculo de itens com coleções:**

  - A coleção é uma entidade que reúne vários itens num único agrupamento. Os itens da coleção podem ser da pasta de origem da coleção ou de outras pastas. As regras de permissões da coleção respeitam as configurações da pasta de origem e também as regras do item. Só poderá acessar a coleção quem tiver acesso à sua pasta. No entanto, mesmo quem puder ver a coleção precisará de acesso para ver os seus itens.

- **Comportamento do vínculo item com entidades fora da Biblioteca:**

  - Os arquivos, isto é, itens e coleções, podem ser vinculados a cadastros / tabelas de clientes, produtos e negócios. Uma vez disponibilizado nessas tabelas o arquivo será visualizado por quem tiver acesso aos itens daquele cadastro. É possível enviar tanto arquivos dessas tabelas para o módulo de biblioteca quanto do módulo até as tabelas.

## White Label

Uma das funcionalidades criadas para personalizar ainda mais a experiência dos usuários é o White Label. Através dele, o administrador pode alterar as cores e logotipos presentes na ferramenta, tornando o CRM um ambiente mais familiar, congruente com a identidade visual da marca que está utilizando o Ploomes.

A personalização do estilo é dividida da seguinte forma:

- Primeiro, eu defino as cores principais, divididas em dois tipos:

  - Cor do logo (altera o menu esquerdo da tela);
  - Cor de confirmação (altera todos os botões de confirmação do Ploomes - por exemplo: ao criar um cliente existe um botão de confirmação chamado “Salvar”);

    - As cores podem ser escolhidas através de um menu de seleção, ou da digitação do código hexadecimal da cor;
    - Caso uma cor muito clara seja selecionada, o próprio Ploomes pode ajustá-la automaticamente para uma cor mais escura, dentro da mesma palheta, devido à nitidez necessária para o Menu e Ícones/Botões.
- Depois, eu posso optar por usar logos personalizados. Existem três tipos:

  - Menu lateral esquerdo - altera a imagem presente no canto inferior esquerdo;
  - Favicon - altera a imagem do site na guia do navegador;
  - E-mails automáticos - e-mails automáticos enviados pela Ploomes vão, por padrão, com o nosso logotipo. Use essa funcionalidade para alterar essa informação.
- Ademais, é possível alterar o nome exibido na guia, indicando o valor desejado em um campo que possui limite de 250 caracteres. Essa configuração **não altera** a URL para acessar o sistema, apenas o nome da guia;
- Por fim, é possível sempre “resetar” o estilo, retornando as informações para o padrão da Ploomes.

# Versão Mobile

O Ploomes conta com um aplicativo disponível para download na Google Play e na App Store. O acesso ao aplicativo se dá pelas mesmas credenciais utilizadas para o acesso na versão web.

A usabilidade, isto é, a maneira de inserir, consultar, editar e excluir dados no aplicativo pode ser diferente da web, a depender do cadastro / tabela que esteja sendo acessado.

O aplicativo não possui todas as funcionalidades da versão web. Disponibilizamos, abaixo, a comparação entre as funcionalidades existentes entre a versão web e a versão mobile.

## Resumo

| **Funcionalidade** | **Mobile** | **Web** |
| --- | --- | --- |
| **Resumo** | - Tarefas do dia | - Filtros de negócios/propostas/vendas já criados - Publicações - Tarefas do dia - Prévia de relatório de situação dos negócios |
| **Atividades** | - Criação de registros de interação - Configuração de exibição de atividades | - Configuração de exibição de atividades |
| **Metas** | - Apenas visualização das metas criadas na Web | - Criação de painéis; - Criação de metas; - Visualização de especificidades das metas (“filtros rápidos”); |

## Clientes

É possível consultar produtos de cliente no APP

| **Funcionalidade** | **Mobile** | **Web** |
| --- | --- | --- |
| **Campo de busca** | - Lupa de busca por cliente; | - Campo de busca por clientes; |
| **Filtros** | - Apenas busca item por filtros já configurados na Web; | - Criação/Edição/Deleção de filtros Simples e Avançados; |
| **Abas** | - Apenas filtra por abas já configuradas na Web; | - Criação/Edição/Deleção/Duplicação de nova aba; - Configuração de filtros dentro da aba; - Exportação de abas; - Edição em massa; |
| **Tabela dinâmica** | - Não aplicável; | - Edição de dados de clientes via colunas da tabela; - Ordenação por campos nativos; - Configuração das colunas que aparecem para os usuários; - Configuração de itens por página; |
| **CRUD** | - É possível criar, editar e excluir clientes (empresas e pessoas); - Quando dentro da tela de um cliente, é possível:    - Criar registros de interação, com a possibilidade de check-in / check-out;   - Criar tarefas;   - Criar negócios;   - Criar documentos; | - CRUD completo; |
| **Modo de visualização** | - Não aplicável; | - Quebra por cliente ou produto do cliente; |
| **Mapa** | - Não aplicável; | - Visualização do mapa; |
| **Menu de configurações** | - Não aplicável; | - Importar clientes pelo Excel; - Configurar campos de clientes; - Configurar marcadores de cliente; - Configurar formulários externos; |

## Produtos do cliente

Disponível apenas para consulta.

## Tarefas

| **Funcionalidade** | **Mobile** | **Web** |
| --- | --- | --- |
| **Calendário** | - Calendário do mês atual; - Possibilidade de percorrer entre os meses, anteriores e futuros; - Visualização de tarefas do dia; - Visualização de tarefas finalizadas (após aplicação do filtro); - Visualização de tarefas agendadas em datas anteriores ou futuras (sinalizadas com um “pontinho” azul); | - Calendário do mês atual; - Possibilidade de trocar a visualização do calendário para, mês, semana ou agenda; - Possibilidade de percorrer entre os meses, anteriores e futuros; - Visualização de tarefas finalizadas (após aplicação do filtro); - Visualização de tarefas agendadas em datas anteriores ou futuras (sinalizadas com a cor do tipo de tarefa agenda); |
| **Configurações de exibição** | - Aplicação de filtros configurados previamente na Web; - Possibilidade de selecionar o tipo de tarefa a ser visualizada; - Visualização de tarefas abertas e/ou finalizadas; - Visualização de minhas tarefas ou tarefas de outros; | - Não aplicável (Esse formato de configuração está presente somente no Mobile); |
| **Visualização rápida** | - Não aplicável; | - Seleção para visualização de um ou mais tipos de tarefas; |
| **Mapa** | - Não aplicável; | - Visualização do mapa de regiões com tarefas agendadas; |
| **Menu de configurações** | - Não aplicável; | - Visualização de tarefas abertas e/ou finalizadas; - Visualização de minhas tarefas ou tarefas de outros; |
| **Botão Filtros** | - Não aplicável; | - Criação/Edição/Deleção de filtros Simples e Avançados; |
| **Modo de visualização** | - Não aplicável; | - Visualização em lista; - Visualização em tabela; - Visualização em calendário; - Acesso ao cadastro / tabela de Registros de interação; |
| **Menu** | - Não aplicável; | - Integrações de tarefas; - Configuração de marcadores de tarefas e registro de interação; - Configuração de tipos de tarefas e registros de interação; |
| **CRUD** | - CRUD completo; | - CRUD completo; |

## Cards / Negócios

| **Funcionalidade** | **Mobile** | **Web** |
| --- | --- | --- |
| **Listagem de funis** | - Listagem de funis ativos; | - Listagem de funis ativos e arquivados; |
| **Campos de busca** | - Campo de busca por Negócios; | - Campo de busca por Negócios; |
| **Seleção de funil** | - Não aplicável; | - Visualização em tabela de todos os negócios; - Botão para visualizar todos os funis; - Visualização de todos os funis disponíveis; - Campo de pesquisa por funis; |
| **Botão Exibir** | - Filtro (apenas visualização); - Ordenação; - Situação dos negócios; - Responsabilidades; | - Ordenação; - Situação dos negócios; - Responsabilidades; |
| **Filtros** | - Não aplicável; | - Criação/Edição/Deleção de filtros Simples e Avançados; |
| **Modo de visualização** | - Não aplicável; | - Tabela; - Funil; |
| **Menu** | - Não aplicável; | - Importação de negócios; - Configuração de marcadores; - Configuração de funis; - Configuração de formulários externos; |
| **CRUD** | - Visualização dos estágios do funil, um por vez (não é possível exibir mais de um estágio simultaneamente na versão mobile); - CRUD completo de cards / negócios; | - CRUD completo; |

## Documentos

| **Funcionalidade** | **Mobile** | **Web** |
| --- | --- | --- |
| **Campo de busca** | - Busca por Proposta/Venda/Documento; | - Busca por Proposta/Venda/Documento; |
| **Filtros** | - Apenas busca item por filtros já configurados na Web; | - Criação/Edição/Deleção de filtros Avançados; |
| **Menu** | - Não aplicável; | - Configuração de modelos de proposta/venda/documento; - Configuração de estágio da venda; |
| **Abas** | - Apenas filtra por abas já configuradas na Web; | - Criação/Edição/Deleção/Duplicação de nova aba; - Configuração de filtros dentro da aba; - Exportação; - Edição em massa; |
| **Modo de visualização** | - Não aplicável; | - Por proposta/venda/documento; - Por produtos; |
| **CRUD proposta** | - Visualização de proposta; - Consulta a dados do cliente e do negócio; - Criação de propostas sem opcionais; - Histórico da proposta; - Comentários; - Revisões da proposta; - Chat externo; - Botão “revisar”; - Botão “editar”; - Botão “compartilhar”; - Ganhar e perder negócio da proposta; - Atualizar dados e modelo; - Fazer download; - Excluir proposta; | - CRUD completo; |
| **CRUD venda** | - Visualização da venda; - Visualização dos estágios da venda; - Criação da venda sem opcionais; - Consulta a dados do cliente; - Histórico da venda; - Comentários; - Chat externo; - Botão “editar”; - Botão “compartilhar”; - Atualizar dados e modelo; - Fazer download; - Excluir venda; | - CRUD completo; |
| **CRUD documento** | - Visualização do documento; - Criação do documento sem opcionais; - Consulta a dados do cliente; - Histórico do documento; - Comentários; - Chat externo; - Botão “editar”; - Botão “compartilhar”; - Atualizar dados e modelo; - Fazer download; - Excluir documento; | - CRUD completo; |

## Produtos

Disponível apenas para consulta.

## Relatórios

Não aplicável à versão Mobile.

## Biblioteca IA

Pasta de arquivos não aplicável à versão Mobile. Perguntas para consulta à Biblioteca IA disponível na versão Mobile.

## Administração

Não aplicável à versão Mobile.

## White Label

O White Label só pode ser configurado pela versão Web. No entanto, as cores escolhidas são refletidas no aplicativo. Não é possível substituir o ícone do aplicativo.

## Limitações do Modo Offline

- Não é possível gerar html de propostas, vendas e documentos;
- Não é possível baixar e visualizar registros de interação e históricos de clientes e cards no modo offline, apenas dos que foram gerados;
- Não é possível disparar travas ou validações de fluxo de aprovação;
- Não é possível rodar fórmulas externas, mesmo para fazer buscas internas (GET em cadastro sincronizado no modo offline, por exemplo);
- Não é possível rodar fórmulas integradas com Excel;
- Não é possível anexar fotos ou anexos em campos, registros de interação e nas abas de cliente / negócio;
- Não é possível engatilhar automações de funil e genéricas;
- Não é possível aplicar regras de exibição condicional de checklists, então todos os checklists ficarão visíveis no modo offline;
- Não é possível visualizar metas;
- Não é possível acessar o suporte via Intercom;
- Não é possível trocar o idioma do usuário;
- Não é possível cadastrar endereços (clientes, tarefas) integrados com o Google (e desta forma os campos de latitude e longitude do cliente não são preenchidos automaticamente);
- Não é possível utilizar mecanismos de buscas e filtros (tanto a geral quanto as específicas das entidades) pelo modo offline. Desta forma, é preciso que os usuários naveguem pelas abas disponibilizadas no aplicativo para acessarem o cadastro desejado;
- Não é possível utilizar filtros de produto da base, de blocos de produtos de documentos e de blocos de opcionais de produtos de documentos no modlo offline;
- Não é possível compartilhar propostas, vendas e documentos;
- Não é possível acessar páginas específicas do Ploomes através de deeplink;
- A sincronização de clientes e negócios não remove do banco do celular cadastros que tenham sido excluídos, podendo retornar dados inconsistentes com a versão mais atualizada conectada à internet;
- Nenhuma integração plug & play e personalizadas funciona no modo offline.

## Observações finais

Funcionalidades não citadas na comparação entre as versões não existem no aplicativo.

# Assistente IA

- São liberados 100 créditos por dia por usuário
- Esse limite equivale a aproximadamente 225.000 tokens
- Em média, isso permite cerca de 30 interações por dia no chat

# Limites importantes

O Ploomes não possui ambiente de homologação. Todas as configurações e personalizações - como criação de campos, automações, funis e integrações - são realizadas diretamente no ambiente de produção. Por isso, é importante que as alterações sejam feitas com cautela e planejamento. Recomenda-se documentar previamente as mudanças e, quando possível, testá-las em registros não críticos antes de aplicá-las em larga escala.
