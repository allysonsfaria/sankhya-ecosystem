---
id: "40476707180951"
titulo: "KM Acumulado de Pneus"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/40476707180951-KM-Acumulado-de-Pneus"
trilha: "Sankhya Official Pack - SOP > Frotas"
atualizado_em: "2026-07-22T13:27:21Z"
rotulos: ["Configuração", "Relatórios Gerenciais", "Rotina de KM Acumulado de Pneus", "hodômetro", "Cadastro de Pneus", "Movimentação de Pneus", "Controle de Abastecimentos", "KM Acumulado Total", "Recape e Reforma", "Checklist Operacional", "Pneus", "TCF", "Controle de Frotas", "Logística"]
---

# KM Acumulado de Pneus

A Rotina de KM Acumulado de Pneus é o mecanismo central do módulo TCF — Controle de Frotas (Sankhya SOP Logística) responsável por registrar, calcular e manter atualizado o total de quilômetros rodados por cada pneu da frota. Sem esse controle, não é possível saber quando trocar um pneu, quanto ele custou por quilômetro rodado, ou se foi descartado prematuramente.

Do ponto de vista operacional, o mecanismo funciona de forma transparente: cada vez que um operador informa
o hodômetro do veículo em alguma tela do sistema (abastecimento, checklist de viagem, ordem de serviço ou portaria), o sistema armazena essa leitura. Quando o analista de pneus realiza qualquer movimentação — um rodízio, uma troca, um envio para recape — o sistema captura a leitura atual do hodômetro e calcula automaticamente quantos quilômetros o pneu rodou desde o último evento.

O resultado alimenta dois contadores independentes por pneu: o KM Acumulado Total ( KMACUM — somatório de toda a vida do pneu) e o KM da Vida Atual ( KMVIDAATUAL — quilômetros desde o último recape, que zera a cada nova vida).

#### Acesso à Tela

**(1)** Acesse a tela **''Controle de Pneus''** (Logística > Gestão de Frotas > Gestão de Pneus > Controle de Pneus).

Documento: TCF-PNU-001 | Versão: v25.17.0+ | Tabelas: TCFPNU, TMSVEIHKM, TCFPNUVIDA, TCFPNUHIST, TCFITEPNU

**OBSERVAÇÃO**: Esta tela funciona como centro de operações do controle de pneus. Todos os eventos registrados aqui (rodízio, envio para estoque, recape, descarte) disparam cálculos automáticos de KM e alimentam os indicadores de gestão.

#### Tabelas e Campos Principais

##### O cálculo de KM acumulado envolve as seguintes tabelas do banco de dados:

| Tabela | Descrição |
| --- | --- |
| TCFPNU | Tabela principal do pneu — armazena os campos **KMACUM** (total de km de todas as vidas), **KMVIDAATUAL** (km da vida atual) e **VIDA** (número da vida atual: 1 = novo, 2 = 1º recape). |
| TMSVEIHKM | Histórico centralizado de hodômetro do veículo — contém os campos **CODVEICULO**, **KM**, **ORIGEM** (ABT/OS/PORT/CHECK) e **DHALTER**. |
| FC\_KMATUAL\_TMS() | Função Oracle responsável por retornar o hodômetro mais recente do veículo, consultando a tabela **TMSVEIHKM**. |
| TCFPNUHIST | Histórico de eventos do pneu — utiliza o campo **KMMOVIMENTACAO** para registrar o hodômetro do veículo no momento de cada movimentação/evento. |
| TCFPNUVIDA | Controle de vidas do pneu — armazena os campos **KMINI**, **KMFIM**, **KMRODADO** (km rodado em cada vida) e **CODBANDAROD** (banda de rodagem). |
| TCFITEPNU | Relacionamento entre pneu, posição e veículo — utiliza o campo **KMMONTAGEM** para registrar o hodômetro do veículo no momento da montagem do pneu. |
| TCFBANDAROD | Cadastro de bandas de rodagem — define o km previsto por vida para cada tipo de pneu, servindo como base para alertas e cálculo de custo por km. |
| TCFCONF | Configurações do módulo de Frotas — armazena os parâmetros **ATUALIZAKM**\* responsáveis por ativar as fontes de atualização do hodômetro do veículo. |

#### Como o KM é transferido para o pneu por meio do veículo

##### Na vida real, um pneu não possui um contador de quilômetros embutido — ele simplesmente roda junto com o veículo onde está montado. Por isso, o sistema não mede diretamente os quilômetros do pneu: ele herda os quilômetros do veículo a partir da tabela TMSVEIHKM.

#####

##### Quando um evento de pneu é registrado, o sistema obtém o hodômetro atual do veículo e subtrai o hodômetro do último evento do pneu — salvo em TCFPNUHIST.KMMOVIMENTACAO. A diferença é o incremento de KM que será somado ao acumulado.

| **Fórmula de Cálculo**: Incremento de KM = Hodômetro Atual do Veículo − Hodômetro do Último Evento do Pneu. O hodômetro atual é salvo no histórico para servir de base para o próximo cálculo. |
| --- |

#### Fontes de atualização do KM do veículo

Antes de chegar ao pneu, o hodômetro do veículo precisa ser informado ao sistema. Existem cinco formas de atualizar o histórico de KM em TMSVEIHKM, cada uma controlada por um parâmetro em **TCFCONF**:

**(1)** **Abastecimento**: O operador informa o hodômetro ao registrar o abastecimento. O sistema grava automaticamente a informação na tabela **TMSVEIHKM** com origem **ABT**.

**(2)** **Checklist Operacional**: O hodômetro é coletado durante a inspeção pré ou pós-viagem. Esta é a fonte mais frequente e recomendada como principal, pois ocorre a cada viagem realizada.

**(3)** **Ordem de Serviço**: O km é informado na abertura ou encerramento da manutenção. O sistema grava automaticamente o registro com origem **OS**.

**(4)** **Controle de Portaria**: O hodômetro é coletado na entrada ou saída do pátio. O sistema grava automaticamente a informação com origem **PORT**.

**(5)** **GPS Rastreador**: O rastreador integrado atualiza o hodômetro automaticamente em intervalos regulares. É a fonte com maior granularidade temporal, indicada para frotas com telemetria. Quando configurado, o valor pode ser propagado para todos os veículos da composição.

| **Crítico**: Pelo menos um dos 5 parâmetros deve estar ativo. Se todos estiverem desativados, a tabela TMSVEIHKM não receberá novas leituras e o sistema não conseguirá calcular o KM acumulado dos pneus. Recomenda-se combinar GPS com Checklist para garantir redundância. |
| --- |

#### Fluxo Operacional Completo — 6 Etapas

O fluxo completo do cálculo de KM acumulado percorre seis etapas, desde a coleta do hodômetro até a disponibilização dos indicadores:

- **Coleta do hodômetro pelo operador**

O hodômetro do veículo é coletado por meio das fontes configuradas, como Abastecimento, Checklist Operacional, Ordem de Serviço ou Controle de Portaria. Em frotas com telemetria, a atualização pode ocorrer automaticamente via GPS.

- **Repositório centralizado — TMSVEIHKM**

A leitura é gravada automaticamente na tabela **TMSVEIHKM**, registrando veículo, KM, origem da informação e data/hora da atualização. O KM atual do veículo corresponde sempre ao último registro disponível.

- **Tela Controle de Pneus — Diagrama de Eixos**

Nesta tela o analista seleciona o veículo e visualiza o diagrama com os pneus por posição e o hodômetro atual. Em seguida, escolhe o pneu e o evento que será realizado.

- **Cálculo automático do incremento de KM**

O sistema calcula automaticamente o incremento de quilometragem utilizando a fórmula:

Incremento = Hodômetro Atual − Hodômetro do Último Evento

**Exemplo:**
Veículo com 58.000 km e último evento do pneu registrado em 50.000 km:
Incremento = 8.000 km

- **Atualização do cadastro do pneu (TCFPNU)**

Quatro registros são atualizados: (a) KMACUM += incremento; (b) KMVIDAATUAL += incremento; (c) evento gravado em histórico; (d) em caso de recape: KM da vida anterior é fechado.

- **Indicadores disponíveis nos dashboards**

Custo por KM, % de vida consumida, previsão de troca, ranking de marcas e alertas de pneus críticos atualizados em tempo real nos painéis gerenciais.

#### Eventos que disparam o cálculo do KM do pneu

O KM do pneu não é atualizado em tempo real — a atualização ocorre somente quando o analista registra um
evento de movimentação. Os principais eventos são:

| Evento | Quando ocorre | KM Total | KM Vida Atual | Observação |
| --- | --- | --- | --- | --- |
| Rodízio | Troca de posição entre pneus do mesmo ou de diferentes veículos | Atualiza | Atualiza | Registra o KM do veículo de origem para o pneu transferido. |
| Envio para estoque | Pneu retirado do veículo e armazenado em estoque | Atualiza | Atualiza | O pneu fica disponível para nova montagem em qualquer veículo. |
| Recape/Reforma | Pneu enviado para recapar ou reformar | Atualiza | Fecha vida atual | O KM da vida anterior é registrado e o campo KMVIDAATUAL é zerado na próxima vida. |
| Sucata/Descarte | Pneu descartado definitivamente da frota | KM final registrado | Encerra | O pneu fica inativo, mantendo todo o histórico disponível para análise. |
| Evento avulso | Registro manual de dano, corte, impacto ou desgaste irregular | Atualiza | Atualiza | Registra a ocorrência sem movimentação física do pneu. |
| Medição de sulco | Inspeção periódica do desgaste das bandas | Atualiza | Atualiza | Os sulcos são registrados em milímetros (mm) por posição da banda. |
| Aferição de pressão | Calibragem do pneu por posição no veículo | Não altera | Não altera | Registra apenas a pressão (PSI/kgf), sem impacto no controle de KM. |

| **Nota Importante**: A aferição de pressão é uma ação de manutenção preventiva, não um evento de movimentação de quilômetros. O sistema registra a pressão medida, mas não considera esse momento como um marco de quilometragem. |
| --- |

#### Controle por Vida — Recape e Reforma

Um pneu pode ter múltiplas "vidas". A primeira vida começa quando o pneu é novo. A cada recape ou reforma aprovado, inicia-se uma nova vida:

- **1º Vida — Pneu Novo**

Pneu cadastrado com KMACUM = 0 e VIDA = 1. Ao ser montado no veículo, o hodômetro é registrado — ponto de partida para o primeiro cálculo de incremento.

- **Operação — KM sendo acumulado**

A cada evento (rodízio, evento avulso, medição), o incremento é somado a KMACUM e KMVIDAATUAL. O analista acompanha o percentual de vida consumida comparando KMVIDAATUAL com o KM previsto da banda de rodagem.

- **Envio para Recape**

Analista retira o pneu e o envia para recape. O sistema: (1) calcula o incremento final da vida; (2) atualiza KMACUM e KMVIDAATUAL; (3) registra KM total da vida no histórico; (4) salva data, NF, valor e motivo.

- **Pneu em recape/reforma**

Pneu aguarda o processo sem acumular KM. O valor de KMACUM é preservado.

- **Retorno do Recape → 2a Vida**

Pneu aprovado e registrado com nova banda de rodagem. Ao ser montado novamente, KMVIDAATUAL = 0, mas KMACUM continua de onde parou, preservando o histórico completo.

- **Fim da vida útil → Sucata/Descarte**

Analista descarta via "Sucata/Descarte". O sistema registra o KM final, motivo, desconto residual e valor. O pneu fica inativo com histórico completo disponível para análise.

#### Regras de Negócio

- **R1 — O KM acumulado nunca pode diminuir**

Uma vez registrado, o KMACUM de um pneu não pode ser revertido ou reduzido. O sistema bloqueia qualquer tentativa de registrar um evento com hodômetro inferior ao KM atual do pneu**.**

- **R2 — Pelo menos uma fonte de KM deve estar configurada**

Para que o cálculo funcione, pelo menos um parâmetro **ATUALIZAKM**\* deve estar ativo em TCFCONF. Operações sem registro de hodômetro criam "gaps" no histórico, distorcendo o incremento calculado.

- **R3 — O KMVIDAATUAL zera a cada nova vida**

Ao retornar de um recape ou reforma, o pneu inicia nova vida com KMVIDAATUAL = 0. Isso permite comparar o desempenho real de cada vida com o KM previsto pela banda de rodagem. A vida anterior é preservada no histórico.

- **R4 — O KM previsto da banda define o alerta de troca**

Cada banda possui um KM previsto por vida. O sistema calcula: % Vida = KMVIDAATUAL ÷ KM\_previsto × 100. Quando esse percentual atinge 80%, o sistema alerta o analista para planejar a substituição.

- **R5 — Composições: cada veículo tem histórico independente**

Em composições (cavalo + semirreboque + dolly), cada veículo mantém seu próprio registro em TMSVEIHKM. Quando um pneu é transferido, o sistema usa o hodômetro do veículo de origem para calcular o KM final daquela montagem.

- **R6 — GPS rastreador atualiza TMSVEIHKM automaticamente**

Quando ativado, o rastreador integrado envia leituras para TMSVEIHKM em intervalos regulares. Para frotas com alto volume de viagens curtas — onde o checklist pode não ser registrado com regularidade —, o GPS garante que o incremento sempre terá dados recentes.

#### Mapa de Telas Envolvidas

| # | Tela | Papel na rotina de KM | Parâmetro (TCFCONF) |
| --- | --- | --- | --- |
| 1 | Abastecimento | Coleta o hodômetro no abastecimento e alimenta a tabela **TMSVEIHKM** via trigger. | `ATUALIZAKMVEIABAST = S` |
| 2 | Checklist Operacional | Coleta o hodômetro na inspeção pré/pós-viagem, sendo a fonte mais frequente e recomendada. | `ATUALIZAKMVEICHECK = S` |
| 3 | Ordem de Serviço | Registra o hodômetro na manutenção e alimenta a **TMSVEIHKM** via trigger. | `ATUALIZAKMVEIOS = S` |
| 4 | Controle de Portaria | Coleta o hodômetro na entrada/saída do pátio e grava na **TMSVEIHKM** via trigger. | `ATUALIZAKMVEIPORT = S` |
| 5 | Controle de Pneus | Tela principal da rotina — exibe o diagrama de eixos, registra eventos e dispara o cálculo de incremento de KM. | — |
| 6 | Cadastro de Pneus | Permite consultar **KMACUM**, **KMVIDAATUAL**, histórico de vidas e histórico de eventos do pneu. | — |
| 7 | Histórico KM Veículo | Consulta a tabela **TMSVEIHKM**, exibindo todas as leituras com data, hora, usuário e origem. | — |
| 8 | Configurações Frotas | Define os parâmetros **ATUALIZAKM**\* na tabela **TCFCONF**, ativando ou desativando cada fonte de atualização de KM. | Acesso admin |
| 9 | Bandas de Rodagem | Define o KM previsto por vida para cada tipo de pneu, servindo como base para alertas e custo por KM. | Acesso config |
| 10 | Dashboards Gestão de Pneus | Exibe indicadores como ranking de marcas, custo por KM, pneus críticos, sucatas prematuras e previsão de investimento. | — |

#### Indicadores Gerados pela Rotina

A correta alimentação do KM acumulado é o alicerce de todos os indicadores de gestão de pneus. Sem hodômetros atualizados com regularidade, os indicadores abaixo perdem confiabilidade:

| Indicador | Fórmula / Fonte | Decisão suportada |
| --- | --- | --- |
| Custo por KM Rodado (R$/km) | Valor pago pelo pneu ÷ **KMACUM** da vida | Permite comparar o custo entre marcas e modelos de pneus. |
| % Vida Consumida | **KMVIDAATUAL ÷ KM previsto (banda) × 100** — alerta quando ≥ 80% | Auxilia no planejamento antecipado da substituição dos pneus. |
| KM Total Acumulado | Campo **TCFPNU.KMACUM** — soma de todas as vidas do pneu | Permite realizar benchmark de durabilidade entre marcas. |
| Previsão de Troca | **KM previsto (banda) − KMVIDAATUAL** | Auxilia no planejamento de compras e gestão de estoque. |
| Ranking de Marcas | KM médio por marca, modelo e banda de rodagem | Apoia decisões de compra com base na performance real dos pneus. |
| Sucatas Prematuras | Pneus descartados com **KMACUM** inferior ao KM previsto | Identifica rotas ou condições que geram desgaste excessivo. |

| **Boas Práticas**:   - Atualize o hodômetro dos veículos com frequência mínima semanal. - Utilize o Checklist Operacional como principal fonte de atualização de KM. - Revise mensalmente o histórico de hodômetros para identificar intervalos superiores a 7 dias sem atualização, pois isso pode indicar que alguma fonte não está sendo utilizada corretamente. |
| --- |

#### Perguntas Frequentes (FAQ)

- **Por que o sistema herda o KM do veículo em vez de medir direto do pneu?**

O pneu não possui um contador próprio de quilômetros. Por isso, o sistema utiliza o hodômetro do veículo onde o pneu está montado para calcular a quilometragem rodada.

A cada evento do pneu, como rodízio, recape ou descarte, o sistema consulta o KM atual do veículo e calcula automaticamente o incremento rodado. Isso garante rastreabilidade, histórico auditável e integração com indicadores operacionais baseados em KM.

- **O que acontece se nenhuma fonte de atualização de KM estiver ativada?**

Se todos os parâmetros **ATUALIZAKM**\* estiverem desativados na tabela **TCFCONF**, a tabela **TMSVEIHKM** deixará de receber leituras de hodômetro.

Nessa situação, o sistema não conseguirá identificar o KM atual do veículo no momento dos eventos de pneus, impedindo o cálculo do incremento de KM e comprometendo a rotina de gestão de pneus.

Recomenda-se manter pelo menos uma fonte ativa, preferencialmente **Checklist Operacional** ou **GPS**.

- **Como funciona o recape? O KM acumulado é perdido?**

O KM acumulado do pneu (**KMACUM**) nunca é perdido ou zerado. Quando ocorre um recape, o sistema encerra apenas o KM da vida atual (**KMVIDAATUAL**) e registra essas informações no histórico de vidas do pneu.

Após o retorno do pneu recapado, inicia-se uma nova vida com o **KMVIDAATUAL zerado**, enquanto o **KMACUM** continua acumulando normalmente. Isso permite acompanhar separadamente o desempenho de cada vida do pneu sem perder o histórico total.

- **Qual é a diferença entre KMACUM e KMVIDAATUAL?**

**KMACUM**: representa o total de quilômetros acumulados em todas as vidas do pneu. Esse valor nunca diminui.

**KMVIDAATUAL**: representa apenas os quilômetros rodados na vida atual do pneu, desde o último recape ou reforma.

Sempre que um recape é realizado, o **KMVIDAATUAL** é reiniciado para a nova vida, enquanto o **KMACUM** permanece acumulado.

**Exemplo:**
KMACUM = 200.000 km
KMVIDAATUAL = 35.000 km

- **Como corrigir um hodômetro informado incorretamente?**

O sistema não permite registrar eventos de pneus utilizando um hodômetro inferior ao KM atual já registrado. Caso o KM tenha sido informado incorretamente, a correção deve ser realizada diretamente na origem da informação, como abastecimento, checklist, ordem de serviço e controle de portaria.

Após a correção, o sistema utilizará automaticamente o valor atualizado no próximo cálculo. O histórico dos pneus não pode ser excluído, garantindo rastreabilidade e auditoria.

- **Como o sistema sabe o KM atual do veículo no momento do evento de pneu?**

Sempre que um hodômetro é informado em abastecimentos, checklists, ordens de serviço ou controles de portaria, o sistema grava automaticamente a leitura na tabela **TMSVEIHKM**.

Ao registrar um evento de pneu, o sistema consulta a função: `FC_KMATUAL_TMS(codveiculo)`

Essa função retorna o último KM registrado para o veículo. Caso a tabela esteja sem atualizações recentes ou sem registros, o cálculo do incremento poderá ser comprometido.

- **Qual o impacto de um descarte prematuro de pneu?**

Quando um pneu é descartado com KM muito abaixo do previsto para sua banda de rodagem, ele passa a ser identificado como uma sucata prematura nos indicadores gerenciais.

Esse cenário pode indicar problemas como desgaste excessivo, alinhamento inadequado, condições severas de rota e condução inadequada do veículo.

Todo o histórico do pneu permanece disponível para análise, incluindo eventos, rodízios e medições realizadas ao longo da sua utilização.

#### Regras Críticas de Go Live

- **Regra 1 - Pelo Menos Uma Fonte de KM Ativada**

Antes de iniciar os lançamentos operacionais, ative pelo menos um parâetro **ATUALIZAKM**\* na tabela **TCFCONF**. Recomenda-se utilizar o **Checklist Operacional** em conjunto com o **GPS**, garantindo maior frequência e redundância nas atualizações.

Sem uma fonte ativa, o histórico de KM não será alimentado e o cálculo de incremento dos pneus não funcionará corretamente.

- **Regra 2 - Checklist como Fonte Primária Recomendada**

O **Checklist Operacional** é a fonte mais recomendada para atualização de KM, pois normalmente é preenchido a cada viagem por motoristas ou inspetores.

Antes do Go Live, configure o parâmetro: `ATUALIZAKMVEICHECK = S`

Quando apenas o GPS é utilizado, veículos com trajetos curtos podem permanecer dias sem atualização de hodômetro.

- **Regra 3 - Validação de Bandas de Rodagem Configuradas**

Todas as bandas de rodagem cadastradas na tabela ''**TCFBANDAROD''** devem possuir o KM previsto por vida preenchido.

Sem essa informação, o sistema não conseguirá calcular alertas de troca e indicadores de vida consumida. Antes do Go Live, revise se todas as bandas utilizadas pela frota possuem o KM previsto configurado.

- **Regra 4 - Histórico TMSVEIHKM Sem Gaps Superiores a 7 Dias**

Revise periodicamente o histórico da tabela TMSVEIHKM para identificar períodos superiores a 7 dias sem atualização de hodômetro.

Gaps podem indicar fontes de atualização não utilizadas, falhas operacionais, ausência de registro pelos operadores.

Essas inconsistências impactam diretamente o cálculo de incremento de KM e os indicadores de gestão de pneus.

- **Regra 5 - Restrição de Acesso ao Cadastro de Bandas**

Permita o acesso ao cadastro de bandas de rodagem apenas para gestores responsáveis ou administradores.

Alterações indevidas no KM previsto podem comprometer os alertas de troca e os indicadores de vida útil dos pneus de toda a frota.

- **Regra 6 - Histórico de Pneus Inviolável**

Após o registro de um evento, como rodízio, recape ou descarte, o histórico do pneu não deve ser alterado ou removido. O sistema mantém essas informações para auditoria, rastreabilidade e análise de desempenho.

Caso um evento seja registrado incorretamente, realize um novo lançamento corretivo, preservando o histórico original.

#### Checklist de Configuração Pré-Go-Live

**Fontes de Atualização de KM (5 itens)**

- Ative o parâetro `ATUALIZAKMVEICHECK = S` para utilizar o Checklist Operacional como fonte principal de atualização de KM.
- Ative pelo menos uma fonte adicional (GPS, Abastecimento, Ordem de Serviço ou Portaria) para garantir redundância das leituras.
- Realize testes de coleta de hodômetro em todas as fontes ativas no ambiente de homologação.
- Valide se a tabela **TMSVEIHKM** está recebendo leituras regularmente e sem gaps de atualização.
- Configure o parâmetro `TEMPATUALIZAKM` caso utilize GPS, recomendando-se intervalo de atualização de 1 hora.

**Cadastro de Bandas de Rodagem (4 itens)**

- Cadastre todas as bandas de rodagem utilizadas pela frota na tabela **TCFBANDAROD**.
- Defina o KM previsto por vida para cada banda de rodagem, preferencialmente com base nas informações do fabricante ou fornecedor dos pneus.
- Vincule as bandas ao tipo de pneu e à posição de montagem correspondente (dianteira, traseira, direcional ou tração).
- Realize testes do alerta de troca, validando o comportamento do sistema quando o pneu atingir 80% da vida consumida.

**Fluxo Operacional de Pneus (5 itens)**

- Treine os analistas de pneus na utilização da tela **Controle de Pneus**, incluindo diagrama de eixos e registro de eventos.
- Realize testes com todos os eventos disponíveis: rodízio, envio ao estoque, recape, descarte, evento avulso e medição de sulco.
- Valide que o campo **KMACUM** nunca reduz valor, realizando testes de rodízio entre veículos.
- Valide que o campo **KMVIDAATUAL** é zerado corretamente após o recape, executando um ciclo completo de recape.
- Defina um processo de revisão periódica dos gaps na tabela **TMSVEIHKM**, incluindo responsáveis e frequência de acompanhamento.

**Indicadores e Dashboards (4 itens)**

- Acesse o dashboard de gestão de pneus e valide se os indicadores estão sendo calculados corretamente.
- Verifique se o indicador de Custo por KM está refletindo os valores reais pagos pelos pneus.
- Confirme se os alertas de troca (80% de vida consumida) estão sendo disparados corretamente para os pneus em operação.
- Defina a frequência de revisão do ranking de marcas junto à gestão de frotas, recomendando-se acompanhamento trimestral.

**Auditoria e Conformidade (3 itens)**

- Valide se o histórico de eventos da tabela **TCFPNUHIST** está sendo registrado corretamente com usuário, data, hora e KM da movimentação.
- Confirme se os casos de sucata prematura estão sendo monitorados e analisados pela operação.
- Documente a política de retenção dos dados de pneus, definindo por quanto tempo o histórico deverá ser mantido após o descarte.

#### Telas Relacionadas

- **Cadastro de Pneus** (Logística » Gestão de Frotas » Pneus » Cadastro de Pneus)**:** Utilizado para o cadastro inicial dos pneus, incluindo marca, modelo, banda de rodagem, valor e número de série.
- **Movimentação de Pneus** (Logística » Gestão de Frotas » Pneus » Movimentação de Pneus): Responsável pelo registro das entradas e saídas de pneus no estoque da empresa.
- **Checklist Operacional** — realiza a inspeção pré-viagem e coleta do hodômetro, alimentando a tabela **TMSVEIHKM**.
- **Controle de Abastecimentos** — registra abastecimentos com informação de hodômetro, alimentando a **TMSVEIHKM** via trigger.
- **Configurações Gestão de Frotas** — tela utilizada para configuração dos parâmetros **ATUALIZAKM**\* na tabela **TCFCONF**.
- **Dashboards Gestão de Pneus** — disponibiliza indicadores como ranking de pneus, custo por KM e alertas de substituição.
