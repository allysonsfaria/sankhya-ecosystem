---
id: "https://gilded-nasturtium-6b64dd.netlify.app/release-notes/major-release-14-03-2025"
titulo: "Major Release 14/03/2025"
url: "https://gilded-nasturtium-6b64dd.netlify.app/release-notes/major-release-14-03-2025"
trilha: "Release Notes > Major Release 14 03 2025"
---

# Major Release 14/03/2025

14 de março de 2025 · 5 min para ler

## Versões disponibilizadas

- sankhya-bff: [2.0.0](https://gitlab.sankhya.com.br/erp/libraries/sankhya-bff/-/releases/v2.0.0) e [2.1.0](https://gitlab.sankhya.com.br/erp/libraries/sankhya-bff/-/releases/v2.1.0)
- sankhyacore: [6.0.0](https://gitlab.sankhya.com.br/dti/design-system/sankhyacore/-/releases/v6.0.0)
- ez-design: [6.0.0](https://gitlab.sankhya.com.br/dti/design-system/ez-design/-/releases/v6.0.0)
- ez-ui: [6.0.0](https://gitlab.sankhya.com.br/dti/design-system/ez-ui/-/releases/v6.0.0)
- sankhya-blocks: [9.0.0](https://gitlab.sankhya.com.br/dti/design-system/sankhya-blocks/-/releases/v9.0.0)

## Novidades:

### Destaques gerais:

- Inclusão de itens em Modo Grade KB-46574
- Herdar configuração nativa de grade e filtros personalizados de Flex ou HTML KB-41953
- Implementa cancelar paginação paralela na grade KB-80103
- Implementa ez-popover-plus KB-79444
- Aplica ez-popover-plus no ez-search - KB-76625
- Aplica ez-popover-plus no ez-combobox- KB-80686
- Aplica ez-popover-plus no EzDateInput/EzDateTimeInput KB-81491
- Implementação do componente de Árvore Hierárquica KB-63156
- Implementação do SidebarNavigator KB-61217
- Implementação do distinct-search KB-59038
- Disponibiliza modo grade no snk-pesquisa KB-78673
- Cria ez-tooltip e ajusta mensagem de erro do ez-text-input para melhorar espaçamento nas telas KB-74308
- Disponibilização do exportador de grade no snk-simple-crud KB-42648
- Ter "modo simplificado" do configurador do formulário para simple-crud KB-51327
- Ajustes gerais de tamanhos e espaçamentos KB-72630
- Melhorias no contraste de textos e botões - KB-74305
- Disponibiliza opção de cores zebradas na grade KB-75044
- Disponibilizar possibilidade de expandir text-area no formulario KB-80374
- Adicionando prop ShowSeconds em campos EzTimeInput KB-79636
- Implementação de formatação decimal dinâmica na grade KB-34470
- Apresentação dinâmica de um campo na grade e formulário KB-45452

### Features:

- DatasetStrategy: passa a ordenar campos LONGTEXT no frontend KB-55396
- Emite evento no resize dos itens do EzSplitPanel - KB-73149
- EzTextInput: Passa a selecionar texto quando focar no elemento com mouse ou tab KB-74234
- ajustes para possibilitar alteracao de tamanho dos inputs combo-box e number-input KB-75047
- Criacao de cacheManager e ServiceUtils KB-74224
- Implementa loading com lockmanager KB-74304
- Movimentação e refatoração do inMemoryLoader para o sankhyacore KB-83113
- Possibilitar duplo clique no ez-list - KB-51655
- Possibilitar a utilização de campos estáticos no formulário - KB-55365
- Validação de campos obrigatórios no DataUnit - KB-58741
- Adição dos métodos setValue e getValue no addCustomEditor em modo formulário - KB-61161
- Disponibilisa prop para scroll vertical do ez-popup KB-67792
- EzModal: Opção 'none' para o scrim do modal - KB-73518
- Adicao de load spin para o campo de search KB-74193
- melhoria no foco de itens da lista do combo-box KB-83282
- permitir alteração searchOptions através do SearchListener KB-47063
- Respeitar tamanho das colunas na exportação PDF - KB-60340
- Incluir opção 'todos os registros' na exportação quando há registros selecionados na grade - KB-60347
- Permitir manipular mensagens de toast de CRUD quando utilizado um InMemoryLoader KB-62331
- Implementa tratamento parâmetro UITabName do dicionario de dados sankhya - KB-68095
- Disponibilizando strategyExporter no snk-crud KB-83020

### Bug Fixes:

- Altera cor dos ícones das configuraçoes da grade KB-79214
- Ajustes no scroll da grade quando dentro de paineis KB-81333
- DataUnit: getSelectionInfo passa a retornar registros ordenados de acordo com a grade KB-53946
- Ajusta prettyFormatter para lidar com valor ZERO KB-63774
- DataUnit: Remove comparação indevida do hasEquivalentProps KB-66441
- Ajustes na seleção de registros da grade KB-75210
- Ajusta perda de filtros de coluna ao mudar de pagina KB-78381
- Previne load data quando houver apenas uma página - KB-79342
- Ajustes para manter seleção de registro apos inclusão KB-81421
- Ajuste no overflow da paginação da grade KB-88812
- Remove container da paginação quando inativa KB-59887
- Renderização dinâmica ao alterar abas - KB-59889
- Respeitar tamanho das colunas na exportação PDF KB-60340
- Tratando value como string no ez-search KB-60620
- Correcao no ciclo de vida do custom-form-input KB-65214
- Adapta componente EzCustomFormInput para tratar value no formato objeto KB-67354
- ezSearch - Ajusta o tratamento de cenários com value sem label KB-71115
- ajusta responsividade da taskbar KB-72272
- Ajuste de Modal e Popup para permitir teclas de atalho - KB-73981
- Remove shadowDom do EzList - KB-74383
- Ajustado chip de filtros com as bordas cortadas & Botões cortados - KB-74406
- Alteração largura scroll - KB-76031
- Ajuste espaçamento dialog e tamanho do titulo do popup - KB-77126
- ajuste na paginação ao adicionar ou copiar registros KB-77661
- Remoção altura fixa do popover de filtros - KB-78333
- EzActionsButton: Correção do dropdown saindo da tela à direita - KB-79020
- Adaptando filter column para lidar com array KB-80711
- Estiliza slot de footer do ezgrid KB-81350
- Remove bordas quando contém header na grade - KB-83703
- Ajustes z-index do popover KB-84596
- Limpando seleção de células ao limpar seleção de registros KB-88602
- Ajustes no calculo das colunas quando width igual a zero - KB-88891
- dataExporter: Corrige contagem de registros selecionados considerando PKs KB-47941
- Ajustando mensagem de registros removidos KB-55889
- Tratativa de mensagem de erro de usuário sem permissão de exportação - KB-60401
- Desabilitando botão de clonar quando nao há mais de um registro selecionado KB-60626
- MasterDetail: Corrige save de registro com PK pai tipo search e PK filha tipo Inteiro KB-61886
- Ajuste para exibir todas as colunas na exportação de planilhas - KB-66028
- SnkDataUnit: Corrige metadados sendo sobrescritos pelo loadDataUnit KB-67370
- Correção do comportamento ao inserir link e arquivo simultaneamente e 'Finalizar' sem salvar antes KB-67558
- Utilizando customConfigLoader para carregar items da filterBar KB-70564
- Criando util para paginação inMemory e para construir LoadDataResponse KB-71601
- SnkTaskBar: Desbloqueia o save quando ocorrer um SAVING\_CANCELED KB-72726
- SnkFormConfig: Corrige erro ao salvar quando formConfigOptions esta undefined KB-73324
- PersonalizedFilter: Correção de espaçamento dos botões de editar e excluir - KB-78454

### Performance:

- Utiliza aggrid modules KB-74182
- Correção de requisições desnecessárias - KB-75149
- remove listener da taskbar quando o componente é destruido KB-74182
- remocao da barra de carregamento no topo da tela para o getSuggestion KB-74193
- Estratégia de debounce para loading bar - KB-74201
- Criação cache parâmetros - KB-75149
