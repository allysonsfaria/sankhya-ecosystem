---
id: "44010986010391"
titulo: "[TMS] - Cadastro de tabela de fretes via tela do sistema"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010986010391--TMS-Cadastro-de-tabela-de-fretes-via-tela-do-sistema"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T18:52:14Z"
rotulos: ["sync_hc", "lincros", "lincros_13432703", "sync_hash_8a69c06b49ed"]
---

# [TMS] - Cadastro de tabela de fretes via tela do sistema

**Menu**: Cadastros Gerais > Transportadoras > Negociações > Tabelas de Frete

**Objetivo:** Como realizar o cadastro da tabela de fretes via tela do sistema.

## Considerações:

- Registrar as tarifas negociadas com as transportadoras para consulta prévia de custo do serviço de transporte, facilitando a escolha da melhor transportadora;
- Permitir auditar as cobranças de frete, fornecendo o valor negociado para comparação com o valor realizado pela transportadora.

**Pré-requisitos:** É necessário ter os cadastros abaixo antes de criar a tabela de fretes:

- [Possuir Regiões cadastradas](https://intercom.help/ajudalincros/pt-BR/articles/13432697-tms-cadastro-de-regioes)
- [Possuir Rotas cadastradas](https://intercom.help/ajudalincros/pt-BR/articles/13438746-tms-como-cadastrar-alterar-e-importar-rotas-de-transportadoras)

## Criando a Tabela de Fretes

Acesse o menu **Cadastros Gerais > Transportadoras > Negociações > Tabelas de Frete** e clique no botão **'Novo'**:

![Imagem 1: Acesse o menu Cadastros Gerais > Transportadoras > Negociações > Tabelas de Frete e clique no botão 'Novo' :](https://ajuda.sankhya.com.br/hc/article_attachments/44010957328407)

Ao clicar em 'Novo', você será direcionado para a aba **Cadastro da tabela de fretes**. Preencha os campos obrigatórios (marcados com asterisco) e clique em **'Salvar'** para liberar as demais abas. São campos obrigatórios: **Transportadora, De (data inicial da vigência), Nome** e **Modal do Transporte**.

![Imagem 2: Ao clicar em 'Novo', você será direcionado para a aba Cadastro da tabela de fretes . Preencha os campos obrigatórios…](https://ajuda.sankhya.com.br/hc/article_attachments/44010992814359)

## Aba Cadastro — principais campos

- **Código**: identificação da tabela na plataforma. Preenchido automaticamente após salvar;
- **Situação de aprovação**: inicia como "Aguardando aprovação". Pode ser Deferida (apta para uso) ou Indeferida (bloqueada). Preenchido automaticamente;
- **Unidade (multi-seleção):** define quais unidades da empresa a tabela atende. Sem seleção, vale para todas as unidades;
- **Transportadora (obrigatório):** transportadora da tabela de frete;
- **Contrato da tabela de frete**: contratos com as transportadoras e suas vigências, onde é definido o valor máximo a ser gasto com uma determinada transportadora;
- **Tabela base**: ao informar outra tabela neste campo, o sistema aplica o conceito de herança — os dados da tabela base também são considerados no cálculo de fretes;
- **De / Até**: início e fim da vigência da tabela. Fora da vigência, a tabela não aparece nas telas de consulta e seleção, e não é sugerida nas cotações. Ao atingir a data final sem uma próxima vigência cadastrada, a tabela é inativada automaticamente pelo sistema — Pré-conhecimentos já em andamento mantêm o cálculo original, mas novos cálculos não utilizam a tabela inativa;
- **Ativa**: indica se a tabela está ativa. Quando inativa, não aparece nas telas de consulta e seleção;
- **Nome (obrigatório):** nome da tabela de frete;
- **Tipo de negociação**: Embarque (carga fechada), Pré-conhecimento (carga fracionada) ou Ambos;
- **Negociação por item**: calcula o frete para cada item da NF separadamente e soma ao final;
- **Modelo de tabela de frete**: indica se a tabela é utilizada como modelo no BID de fretes;
- **Modal do transporte (obrigatório):** modal de frete padrão da tabela. O sistema busca o modal do cadastro da Transportadora (Empresa) e, caso não informado, busca do cadastro de Transportadora ou dos parâmetros da empresa;
- **Grupo de veículo do transporte**: grupo de veículo padrão. Busca o grupo de maior cubagem informado nas restrições;
- **Fluxo de transporte**: a busca por tabela passa a considerar o fluxo de transporte informado na carga, permitindo selecionar a negociação correta;
- **Marcadores**: quando informado, a tabela só calcula Pré-conhecimentos com o mesmo marcador;
- **Observação**: campo de texto livre;
- **Anexos**: formatos aceitos: \*.doc, \*.docx, \*.jpg, \*.jpeg, \*.pdf, \*.png, \*.rtf, \*.tiff, \*.txt, \*.xls, \*.xlsx, \*.xml. Recomenda-se anexar a proposta da transportadora para facilitar auditorias;
- **Justificativas de ação:** registra o motivo de indeferimento do contrato da tabela de frete.

**Atenção — vigência:** o sistema envia uma notificação automática ao responsável quando a vigência se aproxima do vencimento. Tabelas inativas não são utilizadas em novos cálculos, mas os Pré-conhecimentos já em andamento mantêm o cálculo original.

## Aba Restrições de Busca

![Imagem 3: Aba Restrições de Busca](https://ajuda.sankhya.com.br/hc/article_attachments/44010992977687)

Indica condições específicas em que a tabela será aplicada. Pode-se cadastrar apenas **um tipo de restrição por tabela**:

**Atendido**: o sistema considera as tabelas que contenham as marcações definidas.

**Exclusivo**: a tabela é exclusiva para aquela marcação, ignorando outras com o mesmo item como "atendido".

**Restrito**: a tabela é ignorada para aquela marcação específica, mesmo que outras condições sejam atendidas.

As informações que podem ser restritas são:

- **Modais**: permite selecionar modais diferentes do padrão da transportadora para a busca;
- **Pessoas**: permite selecionar CNPJs/CPFs para a busca. É possível importar pessoas via arquivo "xlsx". Para o modelo da planilha, acesse: Cadastros Gerais > Pessoas > Cadastro > botão Modelo:

![Imagem 4: Pessoas : permite selecionar CNPJs/CPFs para a busca. É possível importar pessoas via arquivo "xlsx". Para o modelo da…](https://ajuda.sankhya.com.br/hc/article_attachments/44010982498583)

- **Grupo de veículos**: permite selecionar grupos de veículos para a busca;
- **Produtos**: permite selecionar produtos para a busca.

## Aba Componentes por Rota

![Imagem 5: Aba Componentes por Rota](https://ajuda.sankhya.com.br/hc/article_attachments/44010993188887)

Reúne os principais elementos de cálculo de frete. Exibe as rotas que compõem a tabela e as faixas aplicadas a cada rota.

**(1) Selecione uma Rota:** você pode compor a tabela com rotas existentes ou criar novas diretamente pela tabela, pelos botões:

- **Incluir rota**: cria uma nova rota. Obrigatório informar descrição, origem e destino. É possível marcar a rota como **Bidirecional**, fazendo os valores valerem nos dois sentidos (origem → destino e destino → origem):

![Imagem 6: Incluir rota : cria uma nova rota. Obrigatório informar descrição, origem e destino. É possível marcar a rota como…](https://ajuda.sankhya.com.br/hc/article_attachments/44010972221591)

- **Buscar rotas**: busca rotas já cadastradas para a transportadora e as vincula à tabela:

![Imagem 7: Buscar rotas : busca rotas já cadastradas para a transportadora e as vincula à tabela:](https://ajuda.sankhya.com.br/hc/article_attachments/44011008559383)

**(2) Selecione as Faixas para cálculo:** define o critério e os valores validados no Pré-conhecimento para encontrar os componentes correspondentes. É obrigatório informar o valor inicial e final da faixa. Os tipos de faixa disponíveis são: Peso nominal, Peso cubado, Quantidade de volumes, Quantidade de itens, Valor de mercadoria, Metro cúbico, Peso excedente\*, Peso excedente intermediário, Quantidade motorista, Quilômetro e Quilômetro excedente.

\*Faixas de peso excedente são iniciadas a partir da última faixa de peso nominal, independente do valor informado.

**Faixas compostas**: permitem o cadastro de níveis de faixas, combinando critérios para determinar os componentes do cálculo. Para incluir uma faixa filha, clique no botão (+) em uma faixa já criada:

![Imagem 8: Faixas compostas : permitem o cadastro de níveis de faixas, combinando critérios para determinar os componentes do…](https://ajuda.sankhya.com.br/hc/article_attachments/44011002538775)

Os tipos de faixa que suportam faixas filhas são: Peso nominal, Peso cubado, Quantidade de volumes, Quantidade de itens, Valor da mercadoria, Metro cúbico, Quantidade motorista e Quilômetro. Faixas do tipo Peso excedente não podem ter nem ser faixa filha. Faixas filhas não disponíveis para tabelas marcadas como Modelo.

**Adicionar Componente**: ao selecionar uma rota e uma faixa, o botão Adicionar Componente fica disponível para inserir os componentes que farão parte do cálculo:

![Imagem 9: Adicionar Componente : ao selecionar uma rota e uma faixa, o botão Adicionar Componente fica disponível para inserir os…](https://ajuda.sankhya.com.br/hc/article_attachments/44010987151255)

Cada componente pode ser configurado como mínimo, máximo (customizado), fixo ou percentual. Ao adicionar um componente por rota, ele terá fator mandatório caso o mesmo componente esteja cadastrado na aba Generalidades.

## Aba Componentes com Restrição

![Imagem 10: Aba Componentes com Restrição](https://ajuda.sankhya.com.br/hc/article_attachments/44011002794135)

Permite incluir componentes (taxas) aplicados a CNPJs/CPFs específicos, como TDE (taxa de dificuldade de entrega), TAD (taxa de agendamento por destinatário), entre outros. É possível vincular pessoas individualmente ou via importação em lote. O mesmo componente pode ser adicionado mais de uma vez com valores diferentes, caso a negociação varie por CNPJ.

## Aba Generalidades

![Imagem 11: Aba Generalidades](https://ajuda.sankhya.com.br/hc/article_attachments/44010987453463)

Permite inserir componentes aplicados em **todas as rotas e faixas** da tabela, independente de origem, destino, peso ou valor. O sistema sugere automaticamente os componentes cadastrados na transportadora. Cada componente pode ser configurado como mínimo, máximo (customizado), fixo ou percentual.

## Botões disponíveis na Tela

![Imagem 12: Botões disponíveis na Tela](https://ajuda.sankhya.com.br/hc/article_attachments/44011017049495)

- **Clonar**: cria uma cópia idêntica da tabela, com o nome acrescido de "(CLONADA)";
- **Reajustar**: aplica, de forma estruturada, percentual ou valor de reajuste sobre rotas, faixas ou componentes (campos fixo, percentual, mínimo ou máximo). É possível pré-visualizar os valores antes de confirmar e selecionar apenas os registros desejados;
- **Criar tabela filha**: cria automaticamente uma tabela herdeira com a tabela atual como Tabela Base;
- **Deferir**: aprova a tabela, permitindo que seja utilizada na seleção de transportadora;
- **Indeferir**: rejeita a tabela, bloqueando seu uso na seleção de transportadora e nas simulações;
- **Aguardar aprovação**: retorna a situação para "Aguardando aprovação". A tabela ainda aparece nas simulações, mas não pode ser selecionada;
- **Recalcular pré-conhecimentos**: recalcula todos os Pré-conhecimentos que utilizam esta tabela.

**Obs.:** Os campos que aparecem em vermelho são de preenchimento obrigatório.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos."
