---
id: "41410388331159"
titulo: "(Em andamento) Dashboard CPK e Custos de Pneus"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/41410388331159--Em-andamento-Dashboard-CPK-e-Custos-de-Pneus"
trilha: "Sankhya Official Pack - SOP > Frotas"
atualizado_em: "2026-07-22T13:26:38Z"
rotulos: ["Custos", "Dashboards", "Análise", "gestão de frotas", "Dashboard CPK", "Análise Sintetica", "Custos de Pneus", "Drawer de Filtros", "Análise Analítica", "Pneus", "CPK"]
---

# (Em andamento) Dashboard CPK e Custos de Pneus

O Dashboard CPK e Custos de Pneus é o painel analítico do módulo de Gestão de Frotas Sankhya dedicado ao acompanhamento do custo por quilômetro (CPK), vida útil, recapagem, sulco e calibragem dos pneus da frota. Apresenta três visões integradas — Sintético, Analítico e Ranking — com filtros dinâmicos por Empresa, Local de Estoque, Sulco Crítico, Periodicidade de Alerta e busca textual. Permite navegação direta para os cadastros relacionados (Pneus, Veículos, Bandas de Rodagem, Notas) e exportação de CSV/Excel.

### Acesso á Tela

O dashboard é acessado pelo menu de Dashboards do Sankhya OM. Caminho recomendado: Logística Gestão de Frotas Dashboards CPK e Custos de Pneus.

Também pode ser incorporado como gadget na área de trabalho do Sankhya OM por meio do recurso de dashboards customizados (Preview de Dashboard).

![Imagem 1: Também pode ser incorporado como gadget na área de trabalho do Sankhya OM por meio do recurso de dashboards…](https://ajuda.sankhya.com.br/hc/article_attachments/41410388311319)

### Pré-Requisitos

Antes de utilizar o dashboard, certifique-se de que os itens a seguir estão devidamente configurados:

**(1)** Os pneus da frota devem estar cadastrados na tela **''Cadastro de Pneus''** (Logística » Gestão de Frotas » Pneus » Cadastro de Pneus) com número de fogo, marca, modelo e banda de rodagem.

**(2)** Os veículos devem estar cadastrados na tela **Cadastro de Veículos** com eixos, posições, placa e identificação de cavalo mecânico/reboque (campo CAVALO).

**(3)** As Bandas de Rodagem devem estar cadastradas com sulco mínimo, pressão recomendada e KM previsto por vida.

**(4)** O ciclo de pneus deve ter sido operado em Movimentação de Pneus (montagens, recapes, medições de sulco e aferições) para gerar dados históricos.

**(5)** Os parâmetros operacionais devem estar definidos em Configurações Frotas.

**(6)** Atualização de quilometragem e horímetro do veículo (Movimentações TMS) ativa, alimentando as leituras usadas no cálculo de CPK e indicadores de uso.

**(7)** Usuário com permissão de acesso ao gadget de dashboard no gerenciamento de perfis do sistema.

### Visão Geral do Dashboard

O dashboard concentra em uma única interface a leitura completa da saúde da frota sob a ótica de pneus. Ao carregar, exibe a visão Sintético com indicadores agregados; permite alternar para as visões Analítico (listas detalhadas) e Ranking (comparativo por dimensão). Recursos principais:

- **Cabeçalho fixo:** Título, alternador de visões (Sintético/Analítico/Ranking), botão de exportar CSV, botão de filtros (drawer lateral) e botão de tema claro/escuro.
- **Drawer de Filtros:** Barra lateral esquerda recolhível com busca por texto, Empresa, Local de Estoque, Sulco Crítico (mm), Periodicidade de Alerta (dias) e atalho “Somente Críticos”. Inicia oculta e é ativada pelo ícone de funil no cabeçalho.
- **KPIs Hero:** Blocos coloridos no topo da visão Sintético com CPK Frota, Custo Total de Pneus, KM acumulado de pneus, KM rodado do veículo, horímetro, ativos, fase crítica e pneus sem medição recente.
- **Cards de Pneus por Posição:** Aplicado, Estoque, Recape, Sucata — exibindo quantidade e custo total acumulado.
- **Gráficos comparativos:** CPK médio por marca, KM acumulado médio por marca, distribuição por vida.
- **11 sub-abas na visão Analítico:** CPK & Custos, Por Veículo, Eixos x Aplicados, Fase Crítica, Sem Medição Sulco, Acompanha PSI, Ranking Marca, KM por Vida, Custo por Vida, Histórico de Aplicação e Gráficos.
- **Totalizadores nas listas:** Valor Total e Valor Médio em R$ exibidos sobre cada listagem da visão Analítico.
- **Ordenação e Filtro por coluna:** Menu de três pontinhos em cada cabeçalho permite ordenar ascendente, ordenar descendente e filtrar valores em estilo checklist (similar ao Excel).
- **Exportação CSV/Excel:** Exporta a lista visível com BOM UTF-8 e separador ponto-e-vírgula (compatível Excel PT-BR).
- **Links de navegação:** Nos códigos de pneu, veículo, banda e nota fiscal de compra, abre o respectivo cadastro/movimento no Sankhya OM.

| **IMPORTANTE**: O dashboard é apenas analítico. Toda inclusão/movimentação de pneu deve ser feita nas telas operacionais (Movimentação de Pneus, Cadastro de Pneus). Os indicadores refletem o estado atual da base operacional. |
| --- |

### Visões Disponíveis

##### O alternador no cabeçalho controla qual visão está em uso. As três visões compartilham o mesmo conjunto de filtros do drawer lateral

| Visão | Propósito | Conteúdo |
| --- | --- | --- |
| **Sintético** | Leitura rápida da saúde global da frota. | Cards de Pneus por Posição, KPIs hero e gráficos comparativos. |
| **Analítico** | Investigação detalhada por dimensão. | Listas em sub-abas (CPK & Custos, Por Veículo, Fase Crítica, Vidas, Custo, Histórico e Gráficos Avançados). |
| **Ranking** | Comparativo por dimensão escolhida. | Lista ordenada por CPK Médio com agrupador alternável por Marca, Modelo ou Banda. |

![Imagem 2: Lista ordenada por CPK Médio com agrupador alternável por Marca, Modelo ou Banda.](https://ajuda.sankhya.com.br/hc/article_attachments/41410424343319)![Imagem 3: Lista ordenada por CPK Médio com agrupador alternável por Marca, Modelo ou Banda.](https://ajuda.sankhya.com.br/hc/article_attachments/41410424344087)![Imagem 4: Lista ordenada por CPK Médio com agrupador alternável por Marca, Modelo ou Banda.](https://ajuda.sankhya.com.br/hc/article_attachments/41410388323351)

### Drawer de Filtros

##### O painel lateral esquerdo concentra os filtros globais aplicados às três visões. Inicia oculto. Para abrir, clique no ícone de funil no cabeçalho. Para fechar, clique novamente ou use a aba lateral.

![Imagem 5: O painel lateral esquerdo concentra os filtros globais aplicados às três visões. Inicia oculto. Para abrir, clique no…](https://ajuda.sankhya.com.br/hc/article_attachments/41410388324887)

| Filtro | Função |
| --- | --- |
| **Buscar** | Busca textual por número de fogo, placa, marca e modelo. Aplicação em tempo real. |
| **Empresa** | Restringe a base aos pneus de uma empresa específica. |
| **Local de Estoque** | Restringe a base aos pneus de um local de estoque específico. |
| **Sulco Crítico (mm)** | Define o limite de sulco abaixo do qual o pneu é tratado como crítico. Padrão: **3 mm**. |
| **Periodicidade Alerta (dias)** | Define o número de dias após o qual a ausência de medição/aferição gera alerta. Padrão: **30 dias**. |
| **Somente Críticos** | Filtra exclusivamente pneus em fase crítica de sulco. |
| **Aplicar / Limpar** | **Aplicar:** fecha o painel de filtros e atualiza listas, KPIs e gráficos. **Limpar:** redefine todos os filt |

### Fluxo Operacional - Análise Sintetica

Use a visão Sintético para uma leitura rápida da saúde da frota antes de mergulhar em detalhes.

**(1)** Abra o dashboard. A visão Sintético é exibida por padrão.

**(2)** Leia os cards de Pneus por Posição (Aplicado, Estoque, Recape, Sucata) — eles mostram quantidade e custo total em R$ por situação.

**(3)** Analise os KPIs hero: CPK Frota, Custo Total, KM Pneus, KM Veículo (TMS), Horímetro, Pneus Ativos, Fase Crítica e Sem Medição.

**(4)** Consulte os gráficos comparativos de CPK médio por marca, KM acumulado médio por marca e distribuição por vida para identificar tendências.

**(5)** Se quiser refinar a análise, abra o drawer lateral pelo ícone de funil, aplique filtros e observe a recalibração imediata dos indicadores.

### Fluxo Operacional - Análise Analítica

Use a visão Analítico para investigar casos individuais e tomar decisões operacionais.

**(1)** No cabeçalho, clique em **''Analítico'**'. A sub-aba **''CPK & Custos''** é exibida por padrão.

**(2)** Escolha a sub-aba desejada conforme o tipo de análise:

- **CPK & Custos** — visão geral por pneu com vida atual, KM acumulado, projeção, custo total e CPK.
- **Por Veículo** — pneus aplicados detalhados por placa, eixo e posição.
- **Eixos x Aplicado**s — veículos com posições sem pneu (gap de cobertura).
- **Fase Crítica** — pneus com sulco igual ou inferior ao limite definido.
- **Sem Medição Sulco** — pneus aplicados que estão há mais dias que a periodicidade sem medição.
- **Acompanha PSI** — pneus aplicados com aferição de pressão atrasada.
- **Ranking Marca** — agregado por marca com KM Vida, KM Proj, % Performance, CPK Real e CPK Prev.
- **KM por Vida** — detalhe por vida do pneu (1ª, 2ª, 3ª…) com KM rodado, projetado e CPK.
- **Custo por Vida** — valor de compra/recapa, reparo e total por vida do pneu.
- **Histórico de Aplicação** — movimentações registradas no ciclo do pneu.
- **Gráficos** — análises gráficas avançadas com toggle Global/Por Veículo/Por Marca.

**(3)** Leia os totalizadores acima da lista (Valor Total R$ e Valor Médio R$) — eles refletem a soma e a média do custo na aba ativa.

**(4)** Use o menu de três pontinhos no cabeçalho da coluna para ordenar (ascendente/descendente) ou filtrar (checklist com busca e “Selecionar todos”). Colunas com filtro ativo são destacadas com fundo verde claro.

![Imagem 6: (4) Use o menu de três pontinhos no cabeçalho da coluna para ordenar (ascendente/descendente) ou filtrar (checklist com…](https://ajuda.sankhya.com.br/hc/article_attachments/41424946462103)![Imagem 7: (4) Use o menu de três pontinhos no cabeçalho da coluna para ordenar (ascendente/descendente) ou filtrar (checklist com…](https://ajuda.sankhya.com.br/hc/article_attachments/41424933030935)

**(5)** Clique nos códigos sublinhados (número de fogo, placa, banda, NF de compra) para navegar diretamente ao cadastro/movimento correspondente no Sankhya OM. Por exemplo, ao clicar no Número de Fogo, o sistema abre a tela ''Cadastro de Pneus'' (Logística » Gestão de Frotas » Pneus » Cadastro de Pneus) já posicionada no registro selecionado, permitindo conferir marca, modelo, banda, local de estoque, vidas, valor e demais campos sem sair do contexto da análise.

![Imagem 8: (5) Clique nos códigos sublinhados (número de fogo, placa, banda, NF de compra) para navegar diretamente ao…](https://ajuda.sankhya.com.br/hc/article_attachments/41424946464407)

| **DICA**: A mesma lógica se aplica para os demais links da lista — clique na placa para abrir o Cadastro de Veículos, na banda para abrir Bandas de Rodagem e na NF de Compra para abrir a Central de Compras — sempre posicionado no registro correto. |
| --- |

![Imagem 9: DICA : A mesma lógica se aplica para os demais links da lista — clique na placa para abrir o Cadastro de Veículos, na…](https://ajuda.sankhya.com.br/hc/article_attachments/41424933033111)

**(6)** Se desejar exportar a lista atual, clique no ícone de download no cabeçalho ou no botão Exportar CSV/Excel. O arquivo gerado é compatível com Excel PT-BR.

### Fluxo Operacional - Ranking

##### Use a visão Ranking para identificar a melhor e a pior marca/modelo/banda da frota em termos de CPK Médio.

**(1)** Clique em Ranking no cabeçalho. A lista é exibida ordenada por CPK Médio (melhor no topo).

**(2)** Alterne entre as dimensões Marca, Modelo e Banda pelos botões segmentados no topo da lista.

**(3)** Compare as colunas Pneus, CPK Médio, KM Médio/Vida, barra de performance e Custo Total para decisões de compra.

### Indicadores de Acompanhamento

#### 1. KPIs Hero (Sintético)

| KPI | Significado |
| --- | --- |
| **CPK Frota** | Custo total acumulado dos pneus ÷ KM acumulado total. Expressa quanto custa cada quilômetro rodado em termos de pneus. |
| **Custo Total Pneus** | Soma do valor investido em todos os pneus (compras, recapagens e reparos). |
| **KM Pneus (acum)** | Soma dos quilômetros rodados acumulados por todos os pneus. |
| **KM Rodado Veic (TMS)** | Soma das leituras mais recentes de odômetro de cada veículo da base filtrada. |
| **Horímetro Veic (TMS)** | Soma das leituras mais recentes de horímetro de cada veículo. |
| **Pneus Ativos** | Quantidade de pneus não descartados (status diferente de SUCATA). |
| **Fase Crítica** | Quantidade de pneus com sulco igual ou inferior ao limite configurado no filtro. |
| **Sem Medição** | Quantidade de pneus aplicados com medição de sulco ou aferição de pressão atrasada acima da periodicidade configurada. |

#### 2. Cards de Pneus por Posição

Quatro blocos coloridos exibem a distribuição da frota de pneus por situação operacional:

| Card | O que representa |
| --- | --- |
| **Aplicado** | Pneus atualmente montados em veículos. |
| **Estoque** | Pneus disponíveis no estoque para montagem. |
| **Recape** | Pneus em processo de recapagem. |
| **Sucata** | Pneus descartados (encerrados). |

#### 3. Totalizadores nas Listas (Analítico)

Acima de cada lista da visão Analítico, dois indicadores resumem o conteúdo da aba ativa:

- **Valor Total R$** — soma do custo dos pneus listados (compra + recapagem + reparo).
- **Valor Médio R$** — média de custo por pneu.

Nas abas KM por Vida e Custo por Vida, a fonte são os valores de cada vida do pneu (recapas e reparos individuais).

#### 4. Gráficos Comparativos

Em três níveis crescentes de profundidade:

- **Sintético**: CPK médio por marca, KM acumulado médio por marca, distribuição por vida.
- **Analítico Gráficos Global:** medições de sulco e aferições de PSI por mês, sulco médio e PSI médio, distribuição por vida e por posição.
- **Analítico Gráficos Por Veículo:** melhor CPK por veículo, custo total, pneus e críticos por veículo.
- **Analítico Gráficos Por Marca**: % performance KM (Vida/Projeção) por marca, CPK médio, custo total, KM médio e pneus por marca.

![Imagem 10: Analítico Gráficos Por Marca : % performance KM (Vida/Projeção) por marca, CPK médio, custo total, KM médio e pneus por…](https://ajuda.sankhya.com.br/hc/article_attachments/41424933034391)

### Regras de Negócio

- **R1 — CPK calculado por vida atual**: o CPK exibido na coluna principal usa o valor por KM rodado registrado na vida ativa do pneu. CPK Previsto reflete a expectativa de custo configurada na banda.
- **R2 — Fase Crítica parametrizável:** um pneu é considerado em fase crítica quando o sulco atual for igual ou inferior ao limite definido no drawer (default 3 mm).
- **R3 — Sem Medição / Sem Aferição:** um pneu aplicado é considerado “sem medição” quando o número de dias desde a última medição de sulco (ou aferição de PSI) for superior à periodicidade configurada no drawer (default 30 dias).
- **R4 — Tipo de Veículo:** veículos com flag cavalo ativa são exibidos como Automotor; demais são Reboque. Em automotores, o primeiro eixo é destacado como direcional, e um pneu com vida superior a 1 no eixo direcional é sinalizado como recap-direcional (situação de risco).
- **R5 — % Performance KM**: calculado como (KM Vida / KM Projetado) × 100. Acima de 100% indica que o pneu superou a projeção da banda; entre 70 e 100% é atenção; abaixo de 70% é crítico.
- **R6 — Eixos x Aplicados:** baseline de 2 pneus por eixo. Um veículo entra na aba quando há posições sem pneu ou eixos cadastrados sem cobertura completa.
- **R7 — Status Aplicado/Estoque/Recape/Sucata:** derivado do status do pneu e da existência de veículo associado. Pneus com status SUCATA não entram no contador de Ativos; pneus em status “REC…” sem veículo associado são contabilizados como Recape.
- **R8 — Composição de custo:** Custo Total = soma de Valor de Pneu + Valor de Reparo de todas as vidas. Valor da Vida é (Vlr Compra/Recapa + Vlr Reparo) da vida específica.
- **R9 — Atualização em tempo real:** a aplicação do drawer recalcula KPIs, cards de posição, gráficos e listas no mesmo evento. Não há recarga de tela.
- **R10 — Ordenação independente por aba:** a ordenação e o filtro de coluna aplicados em uma aba são mantidos enquanto a aba estiver ativa e voltam ao padrão quando se troca de aba

| **Crítico**: O dashboard depende de operação consistente no Cadastro de Pneus, Cadastro de Veículos, Bandas de Rodagem e Movimentação de Pneus. Inconsistências nesses cadastros (pneu sem banda, veículo sem eixos, status divergente) provocam distorções nos indicadores. Antes de tomar decisão com base no CPK, valide a integridade dos cadastros. |
| --- |

### Boas Práticas Operacionais

- **Verifique o painel diariamente:** A leitura de KPIs e cards de posição em rotina diária antecipa picos de custo e ajuda a planejar manutenções.
- **Use o atalho “Somente críticos”:** Ao chegar no Analítico, filtre pelos pneus em fase crítica antes de qualquer ação operacional.
- **Compare CPK Real x CPK Previsto:** Grandes diferenças indicam pneus que não rendem o esperado pela banda — investigue uso ou rota.
- **Acompanhe a % Performance KM:** Tags vermelhas/amarelas na coluna “% Atg” identificam pneus distantes da projeção. Use isso para revisar contratos com fornecedor.
- **Exporte para análise externa:** use o botão Exportar CSV/Excel para levar dados ao Excel/Power BI quando precisar de análise mais profunda.
- **Use o Ranking ao decidir compra:** Escolha marcas/modelos no topo do ranking por CPK Médio, sempre considerando volume mínimo de pneus para evitar viés estatístico.
- **Configure Empresa e Local antes de operações multi-filial:** Filtre pela empresa correta quando o ambiente possuir múltiplas empresas para evitar leitura cruzada.
- **Calibre o limite de sulco crítico por veículo/região:** Regiões com chuva intensa podem exigir limites maiores (ex.: 4 mm). Ajuste o drawer conforme política da operação.

### Perguntas Frequentes

- **Por que o CPK Frota difere do CPK exibido na coluna do pneu?**

O CPK da coluna é o valor da vida atual do pneu (custo por KM rodado nessa vida específica). O CPK Frota é uma média ponderada: soma do custo total de todos os pneus dividido pela soma de KM acumulado total. São métricas diferentes — uma é por pneu, a outra é agregada da frota.

- **Os filtros do drawer afetam todas as visões ao mesmo tempo?**

Sim. O drawer é único para o dashboard. Ao aplicar um filtro, ele se propaga para Sintético (KPIs, cards e gráficos), Analítico (listas e gráficos) e Ranking. A única exceção são os filtros por coluna na visão Analítico — esses são locais à coluna/aba e não se propagam para outras visões.

- **Como funciona o filtro por coluna estilo Excel?**

Clique no ícone de três pontinhos no cabeçalho da coluna. Aparecem três opções: Ordenar Ascendente, Ordenar Descendente e Filtrar. Ao escolher Filtrar, abre um popover com checklist dos valores distintos da coluna, busca e botão “Selecionar todos”. Marque/desmarque os valores e clique em Aplicar. Colunas com filtro ativo ficam com fundo verde claro. Para limpar, abra o filtro novamente e clique em Limpar.

- **Por que alguns veículos aparecem sem placa nas listas?**

Quando o cadastro de veículo não tem placa preenchida, o dashboard exibe a célula em branco em vez de substituir por um código genérico. Isso facilita identificar cadastros incompletos. Para corrigir, edite o veículo no Cadastro de Veículos.

- **O que significa “Recap Direcional!” na lista de Fase Crítica?**

É uma sinalização de risco quando um pneu recapado (vida superior a 1) está aplicado no eixo direcional de um veículo automotor. Em muitas operações, pneus recapados não devem ser usados no eixo de direção. Confirme a política da sua operação e remova o pneu se necessário.

- **Como o dashboard sabe quanto KM o veículo rodou?**

A leitura mais recente de odômetro (KM) e horímetro de cada veículo é trazida das movimentações TMS (rotinas que atualizam quilometragem do veículo após viagens). Se a operação não usa essas rotinas, esses KPIs ficarão zerados — corrija registrando KM em Configurações Frotas / Movimentações de Veículo.

- **Posso usar o dashboard para criar/excluir pneus?**

Não. O dashboard é apenas analítico. Para criar pneus use Cadastro de Pneus. Para movimentar (montar, desmontar, recapar, descartar, medir sulco, aferir pressão) use a tela Movimentação de Pneus. Os links nos códigos do dashboard abrem essas telas operacionais com o registro já selecionado.

- **Os totalizadores Valor Total e Valor Médio mudam conforme o filtro de coluna?**

Os totalizadores são calculados a partir do conjunto de pneus filtrado pelo drawer global; eles não respondem ao filtro de coluna local. Os filtros de coluna afetam apenas o que aparece na tabela. Se quiser reduzir os totalizadores, aplique o filtro no drawer.

### Regras Críticas de Go Live

- **Regra 1 — Base de Cadastro Completa:** Antes do Go Live, todos os pneus da frota devem estar cadastrados, com banda de rodagem associada e valor de compra registrado. Pneus sem banda não geram projeção de KM nem CPK Previsto. Pneus sem valor distorcem todos os totalizadores.
- **Regra 2 — Bandas com KM Previsto e Sulco Mínimo:** Cada banda de rodagem deve ter KM previsto por vida e sulco mínimo definidos. Sem isso, indicadores de % Performance e Fase Crítica ficam comprometidos.
- **Regra 3 — Veículos com Eixos Configurados:** Cada veículo deve ter eixos e posições cadastrados. A aba Eixos x Aplicados depende dessa configuração para detectar gaps de cobertura.
- **Regra 4 — Movimentação de Pneus Operada:** Sem operação consistente no fluxo de Movimentação de Pneus (montagem, desmontagem, recape, sulco, PSI), os indicadores ficarão vazios ou distorcidos. Treine os operadores e estabeleça rotina antes do Go Live.
- **Regra 5 — Integração com KM Veicular (TMS):** KPIs de KM Veículo e Horímetro dependem de leituras atualizadas em rotinas TMS. Se a operação não utiliza esses módulos, comunique aos usuários que esses KPIs ficarão zerados.
- **Regra 6 — Treinamento em Leitura de Indicadores:** Garantir que gestores e analistas entendam a diferença entre CPK Real, CPK Previsto, KM Vida, KM Projeção e % Performance. Erros de interpretação levam a decisões de compra equivocadas.

### Checklist de Configuração Pré-Go-Live

**Cadastros Auxiliares**

- Todos os pneus cadastrados em Cadastro de Pneus com banda, marca, modelo e valor
- Todas as bandas em Bandas de Rodagem com KM previsto por vida e sulco mínimo
- Todos os veículos em Cadastro de Veículos com eixos, posições e flag de cavalo
- Empresas em Cadastro de Empresas com nome fantasia definido (aparece no filtro)
- Locais de estoque em Cadastro de Locais com descrição (aparecem no filtro)

**Operação e Movimento**

- Rotina de Movimentação de Pneus operada por pelo menos 30 dias antes do Go Live
- Medições de sulco registradas em frequência consistente
- Aferições de pressão (PSI) registradas em frequência consistente
- Atualização de KM e horímetro do veículo ativa nas rotinas TMS

**Permissões e Acessos**

- Grupo de usuários gestores com permissão de acesso ao dashboard
- Grupo de usuários operacionais com permissão de leitura nos cadastros relacionados (Pneus, Veículos,
- Bandas, Central de Compras)
- Definida política de Sulco Crítico (mm) por região/operação
- Definida política de Periodicidade de Alerta (dias) por região/operação

**Validação Funcional**

- Testou alternância entre as três visões (Sintético, Analítico, Ranking)
- Testou abertura e fechamento do drawer de filtros
- Testou aplicação e limpeza de filtros, com recalibração imediata
- Testou ordenação ascendente, descendente e filtro de coluna (checklist) em pelo menos três sub-abas
- Testou clique nos códigos (fogo, placa, banda, NF) e validou abertura do cadastro correto
- Testou exportação CSV/Excel e abertura do arquivo no Excel PT-BR sem caracteres quebrados

### Telas Relacionadas

- **Cadastro de Pneus:** inclusão e manutenção dos pneus com número de fogo, marca, modelo, banda de rodagem, valor e local de estoque. Aberta automaticamente ao clicar no número de fogo das listas.
- **Cadastro de Veículos:** cadastro dos veículos da frota com eixos, posições, placa, flag de cavalo, marca, modelo e quantidade de eixos. Aberta automaticamente ao clicar na placa nas listas.
- Bandas de Rodagem: cadastro das bandas com sulco mínimo, pressão recomendada e KM previsto por vida. Aberta automaticamente ao clicar no nome da banda nas listas.
- **Movimentação de Pneus:** tela operacional para montar, desmontar, enviar para recape, descartar, rodízio, medir sulco e aferir pressão. Alimenta os indicadores do dashboard.
- **Central de Compras:** consulta da nota fiscal de compra do pneu (cabeçalho, itens, totais, parceiro). Aberta automaticamente ao clicar no número da NF nas listas.
- **Configurações Frotas:** parâmetros operacionais do módulo de pneus (sulco mínimo, exigências, multiempresa, atualização de KM).
- **Cadastro de Empresas:** empresas usadas como filtro do drawer.
- **Cadastro de Locais de Estoque:** locais usados como filtro do drawer.
