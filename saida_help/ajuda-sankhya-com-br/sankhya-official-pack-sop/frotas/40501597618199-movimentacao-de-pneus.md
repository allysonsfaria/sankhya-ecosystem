---
id: "40501597618199"
titulo: "Movimentação de Pneus"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/40501597618199-Movimenta%C3%A7%C3%A3o-de-Pneus"
trilha: "Sankhya Official Pack - SOP > Frotas"
atualizado_em: "2026-08-27T19:34:25Z"
rotulos: ["Configuração", "Regras de Negócio", "Estoque", "Movimentação de Pneus", "Leitura do Chassi", "Montar um Pneu", "Enviar para Recape", "Pré Go Live", "Controle de Pneus", "Contadores de Estoque", "Sulco Atual e Alerta de Desgate", "KM Acumulado", "Go Live", "Gestão de Frotas", "Logística"]
---

# Movimentação de Pneus

A tela Movimentação de Pneus é o ponto central de operação do módulo **TCF – Controle de Pneus** no Sankhya SOP Logística. Por meio dela, o operador executa todas as ações do ciclo de vida dos pneus — montar, desmontar, enviar para recape, descartar, realizar rodízios, medir sulcos e aferir pressão —, mantendo rastreabilidade completa de cada evento com data, hora, quilometragem e usuário responsável.

#### Acesso á Tela

**(1)** Acesse a tela **''Movimentação de Pneus''** (Logística > Gestão de Frotas > Pneus > Controle de Pneus).

O identificador interno da tela é: **br.com.sankhya.soplogistica.mov.controlepneu**.

![Imagem 1: O identificador interno da tela é: br.com.sankhya.soplogistica.mov.controlepneu .](https://ajuda.sankhya.com.br/hc/article_attachments/40645902407319)

#### Pré-Requisitos

Antes de utilizar a tela de Movimentação de Pneus, certifique-se de que os itens a seguir estão devidamente
configurados:

**(1)** O módulo **Gestão de Frotas – Controle de Pneus** deve estar devidamente habilitado na licença do Sankhya SOP Logística.

**(2)** Os pneus que serão utilizados nas movimentações precisam estar previamente cadastrados na tela **Cadastro de Pneus**, contendo o respectivo número de fogo vinculado.

**(3)** Os veículos devem estar cadastrados no módulo **Gestão de Frotas**, com eixos e posições configurados corretamente para garantir o funcionamento adequado das movimentações e controles.

**(4)** As **Bandas de Rodagem** e seus respectivos limites mínimos de sulco devem estar cadastrados para possibilitar o monitoramento de desgaste e a geração correta de alertas.

**(5)** Os parâmetros de configuração do módulo, como **Utiliza Pneu Sucata** e **Exige Sulco**, devem estar devidamente definidos na tela **''Configurações Frotas''** **(**Configurações » Gestão de Frotas » Configurações Gestão de Frota**)**.

**(6)** O usuário responsável pela operação deve possuir permissão de acesso à tela, configurada previamente no gerenciamento de perfis do sistema.

#### Visão Geral da Tela

A tela de Movimentação de Pneus concentra em uma única interface todos os recursos necessários para operar o ciclo de vida dos pneus da frota.

Ao selecionar um veículo, o sistema carrega automaticamente o diagrama visual do chassi com todos os eixos e posições, os contadores de estoque em tempo real e as informações de odômetro e horímetro. Os principais recursos disponíveis são:

- **Diagrama Visual do Chassi:** Representação interativa de todos os eixos e posições de pneu do veículo selecionado.
- **9 Tipos de Eventos:** Montagem, desmontagem, recape, descarte, rodízio, evento avulso, medição de sulco, aferição de pressão e retorno de recape.
- **Contadores em Tempo Real:** Exibição de pneus disponíveis em estoque, em recape e descartados, atualizados a cada operação.
- **Medição de Sulco por Canal:** Registro de 1 a 6 posições de canal em milímetros, com alertas automáticos de desgaste.
- **Suporte a Composições:** Cavalo mecânico e implementos são exibidos em abas separadas, permitindo operar cada veículo individualmente.
  **Histórico Completo:** Cada evento é gravado com usuário, data/hora, KM e detalhes da operação.

**IMPORTANTE**: Esta tela é o ponto único de operação de pneus. A inclusão de novos pneus no sistema é realizada exclusivamente na tela ''Cadastro de Pneus'' (Logística » Gestão de Frotas » Pneus » Cadastro de Pneus). Toda a movimentação subsequente ao cadastro é gerenciada aqui.

#### Diagrama Axial - Leitura do Chassi

Ao selecionar um veículo, a tela exibe o diagrama axial, que representa visualmente todos os eixos e posições de pneu do chassi. Cada slot no diagrama corresponde a uma posição física no veículo. Abaixo, o exemplo de um cavalo mecânico 6×2 com três eixos:

| Eixo | Tipo | Posições |
| --- | --- | --- |
| Eixo 1 | Direcional | P1 — P2 |
| Eixo 2 | Tração | P3 — P4 — P5 — P6 |
| Eixo 3 | Auxiliar | P7 — P8 |

A tabela a seguir descreve os elementos visuais do diagrama e como interagir com cada um deles:

| Elemento | O que representa | Como interagir |
| --- | --- | --- |
| Slot verde | Posição com pneu montado. Exibe o número de fogo ao passar o mouse. | Clique para ver detalhes: sulco, KM acumulado, marca, modelo e vida atual. |
| Slot vazio (tracejado) | Posição sem pneu — disponível para montagem. | Com ação "Estoque" selecionada, clique para montar um pneu. |
| Barra de eixo | Representa o eixo físico do veículo. | Apenas visual; identifica o grupo de posições do mesmo eixo. |
| Abas de placa | Em composições (cavalo + implemento), cada veículo tem uma aba própria. | Clique na aba para alternar entre os veículos da composição. |
| Odômetro / Horímetro | KM e horas atuais do veículo, exibidos no painel lateral. | Preenchido automaticamente. Pode ser ajustado antes de confirmar o evento. |

| **NOTA:** O sistema identifica automaticamente se a placa informada segue o padrão **Mercosul** (com letras e números intercalados) ou o modelo antigo. Essa identificação influencia diretamente a forma de exibição visual da placa nas abas de composição do sistema. |
| --- |

#### Tipos de Movimentações (Eventos)

Cada operação realizada na tela gera um evento gravado no histórico do pneu com data/hora, KM do veículo e usuário. Os nove tipos de eventos disponíveis são:

- **Montar do Estoque**: Selecione **"Estoque"**, clique em posição vazia e informe o número de fogo do pneu a montar. Sistema registra KM e data de montagem.
- **Desmontar → Estoque**: Com pneu selecionado, clique em "Estoque" para desmontá-lo. Informe sulcos medidos e motivo da desmontagem.
- **Enviar para Recape**: desmonta e envia o pneu à recapadora. Abre popup com campos de NF, valor, parceiro e nova banda de rodagem.
- **Descartar (Sucata)**: encerra definitivamente o pneu. Permite registrar desconto, sulcos finais e motivo de descarte. Ação irreversível.
- **Rodízio de Posição**: selecione um pneu e clique em outra posição para realizar a troca. Gera dois eventos: saída e entrada.
- **Registrar Evento Avulso**: permite registrar qualquer evento sem movimentar o pneu fisicamente. Útil para reparo e registros administrativos.
- **Medição de Sulco**: popup para registrar profundidade de cada canal (1 a 6 posições) em milímetros. Atualiza o cadastro do pneu.
- **Aferição de Pressão**: registra pressão inicial e pressão corrigida em PSI por posição. Mantém histórico de calibrações.
- **Retorno de Recape**: registra pneu retornando da recapadora com nova banda de rodagem e abre nova vida se configurado.

| **ATENÇÃO**: O parâmetro **''Utiliza Pneus da Sucata''** controla se os painéis de Estoque, Recape e Sucata funcionam como origens independentes. Quando inativo, as movimentações só são realizadas via diagrama do veículo. |
| --- |

#### Fluxo Operacional - Montar um Pneu

##### Siga os passos abaixo para montar um pneu em uma posição do veículo:

##### **(1)** Pesquise o veículo por placa ou código no campo de busca. O diagrama de eixos e os contadores de estoque, recape e sucata são carregados automaticamente. Odômetro e horímetro aparecem no painel lateral.

##### **(2)** No painel lateral, clique no botão Estoque. Ele ficará destacado, indicando que o modo "Montar do estoque" está ativo.

##### **(3)** No diagrama do chassi, clique no slot vazio (tracejado) que receberá o pneu.

- ##### O sistema abrirá o popup de montagem.

##### **(4)** No popup de montagem, informe o número de fogo do pneu a montar. O sistema preenche automaticamente o KM/horímetro e data/hora. Confirme ou ajuste conforme necessário e informe o motivo.

##### **(5)** Clique em ''Concluir'' para confirmar. Sistema grava o evento no histórico, associa o pneu à posição, atualiza o registro do pneu e redesenha o diagrama com o slot preenchido em verde.

#### Fluxo Operacional - Enviar para Recape

Siga os passos abaixo para desmontar um pneu e enviá-lo à recapadora:

**(1)** Selecione o veículo e clique no slot verde da posição que contém o pneu a recapar. Informações do pneu (sulco atual, KM acumulado, vida) aparecem no painel lateral.

**(2)** Com pneu selecionado, clique no botão Recape no painel lateral. Sistema abre o popup de recape.

**(3)** Preencha os dados: data/hora, KM, motivo, NF do recape (número, série, valor, parceiro) e nova banda de rodagem. Se configurado, solicitará medição de sulcos antes do envio.

**(4)** Clique em Confirmar. O sistema fecha a vida atual se configurado, altera o estoque do pneu para **"recape"** e remove o pneu da posição do veículo e atualiza o contador de recape.

#### Fluxo Operacional - Realizar Rodízio

Siga os passos abaixo para trocar a posição de pneus no diagrama:

**(1)** Clique no slot verde do pneu que será movido. Ele ficará destacado com borda especial, indicando que está selecionado como origem do rodízio.

**(2)** Clique na posição de destino (com ou sem pneu). Se ambas tiverem pneu, o sistema realizará a troca simultaneamente.

**(3)** No popup de confirmação, verifique data/hora e KM do rodízio. Sistema grava dois eventos no histórico (saída e entrada) e atualiza o diagrama em tempo real.

#### Indicadores de Acompanhamento

**1. Contadores de Estoque**

Exibidos e atualizados a cada operação no painel lateral:

- **Estoque**: pneus disponíveis para montagem.
- **Recape**: pneus em processo de recapagem.
- **Sucata**: pneus descartados definitivamente.

**IMPORTANTE**: Quando o parâmetro **“Controla estoque de Pneus por Empresa?”** está ativo, os contadores são segregados por empresa. 

**2. Sulco Atual e Alerta de Desgaste**

Ao clicar em um pneu no diagrama, o painel lateral exibe o sulco atual em mm. Compare com o sulco mínimo configurado na banda de rodagem:

| Sulco Medido | Status |
| --- | --- |
| 12 mm | Bom |
| 5 mm | Atenção |
| 2 mm | Abaixo do mínimo — desmontar imediatamente |

**3. KM Acumulado e Vida Útil Restante**

O painel lateral exibe, para o pneu selecionado:

- KM total acumulado ao longo de todas as vidas do pneu.
- KM rodado na vida atual (diferença entre desmontagem e montagem).
- Vida útil restante: calculada como (KM previsto − KM atual) / KM previsto × 100%.
- Custo por KM: valor total investido no pneu dividido pelo KM acumulado.

**4. Vida Atual e Número de Recapes**

- O campo **''Vida''** indica quantas recapagens o pneu já teve: Vida 1 = pneu novo; Vida 2 = após primeiro recape.
- O sistema controla o histórico de cada vida separadamente, permitindo comparar rendimento de cada recapagem.

#### Regras de Negócio

- **R1 — Posição deve estar vaga para montagem:** Não é possível montar um pneu em posição que já tenha outro. Sistema bloqueia e exibe alerta.
- **R2 — Número de Fogo único por empresa:** Cada pneu é identificado por número de fogo exclusivo. Não é permitido duplicar. Alteração só via serviço específico.
- **R3 — KM não pode regredir:** KM informado deve ser igual ou maior ao KM da última movimentação do veículo. Sistema rejeita KM retroativos.
- **R4 — Nova vida no recape:** Ao retornar do recape, sistema pode abrir nova vida (incrementando campo VIDA), associando nova banda de rodagem.
- **R5 — Sulcos obrigatórios na sucata (parametrizável):** Quando **''Exige sulco na Saída da sucata?''**, exige medição de sulcos ao enviar para sucata. **''Quando Exige Sulco na entrada para sucata?''**, exige sulcos ao receber da sucata.
- **R6 — Controle por empresa (parametrizável):** Parâmetro **''Utiliza controle de Pneus por Empresa?''** determina se estoque, recape e sucata são segregados por empresa. Quando ativo, campo empresa é obrigatório.
- **R7 — Painel de estoque/recape/sucata (parametrizável):** Parâmetro **''Utiliza Pneus do Recape e Sucata?''** controla se painéis funcionam como origens independentes. Quando inativo, movimentações só via diagrama do veículo.
- **R8 — Alteração de profundidade em estoque (parametrizável):** Parâmetro **''Altera profundidade na movimentação de Pneus?''** determina se operador pode alterar sulco de pneus que estão no estoque do veículo durante a movimentação. Quando inativo, apenas pneus ativos podem ter sulco editado.

| **CRÍTICO**: Pneus com sulco abaixo do mínimo configurado devem ser desmontados imediatamente e avaliados para recape ou descarte. Ignorar esse alerta compromete a segurança da operação e pode gerar passivos de manutenção. |
| --- |

#### Boas Práticas Operacionais

- **Registre eventos no momento certo:** Toda movimentação deve ser registrada no dia em que ocorre, com KM real do odômetro. Atrasos geram inconsistências no histórico.
- **Meça sulcos periodicamente:** Estabeleça uma rotina (por exemplo, a cada 10.000 km ou mensalmente) para medir sulcos de todos os pneus. Isso alimenta alertas automáticos.
- **Planeje rodízios pelos indicadores:** Use KM acumulado e sulco atual de cada posição para planejar rodízios preventivos. Pneus em eixos de tração desgastam mais rápido.
- **Confirme o número de fogo antes de montar:** Verifique fisicamente o número de fogo antes de informar no sistema. Um número de fogo trocado compromete todo o histórico.
- **Calibre e registre a pressão:** Sempre registre pressão inicial e pressão corrigida no sistema. Pneus descalibrados aumentam consumo de combustível e aceleram desgaste.
- **Acompanhe o custo por KM:** Após 6 meses de operação, analise custo por KM por marca e modelo. Essa métrica é mais confiável que preço de compra.
- **Consulte o histórico antes de descartar:** Antes de enviar para sucata, consulte histórico do pneu. Se estiver na vida 1 com pouco KM, pode ser candidato a recape em vez de descarte.
- **Atenção às composições:** Em composições (cavalo + semirreboque), cada veículo tem sua aba e seus pneus independentes. Certifique-se de estar na aba correta.

####

#### Perguntas Frequentes (FAQ)

- **Qual é a diferença entre desmontar para estoque e enviar para recape?**

Desmontar para estoque significa que o pneu foi removido do veículo e está disponível para ser montado novamente em qualquer posição, sem nenhum reparo. Enviar para recape significa que o pneu foi desmontado, será enviado a um parceiro especializado para ter a banda de rodagem trocada/recapada e voltará como "nova vida" do mesmo pneu. O custo operacional do recape é muito menor que comprar um pneu novo, por isso é importante registrar corretamente qual é o destino do pneu desmontado.

- **O que acontece quando o descarte (sucata) é registrado?**

O descarte é uma ação irreversível. Uma vez que um pneu é enviado para sucata, o sistema marca-o como inativo e ele não pode mais ser montado, desmontado ou recapado. O pneu fica no histórico apenas para análise de desempenho e benchmarking de marcas. Por isso é crítico consultar o histórico e indicadores (KM acumulado, número de vidas, sucatas prematuras) antes de confirmar um descarte, especialmente em pneus que ainda têm potencial de recape.

- **Como funciona um rodízio? Ambas as posições precisam ter pneu?**

Um rodízio é a troca de posição entre dois pneus. Se ambas as posições tiverem pneu, o sistema realiza uma troca cruzada. Se a posição de destino estiver vazia, o sistema move o pneu de origem para lá. O sistema grava dois eventos no histórico: saída da posição original (com KM/data do rodízio) e entrada na nova posição (com o mesmo KM/data). Rodízios são operações preventivas essenciais para equalizar o desgaste entre pneus — recomenda-se planejar rodízios a cada 50.000-80.000 km.

- **Qual é a diferença entre "Vida 1" e "Vida 2" de um pneu?**

Vida 1 é quando o pneu é novo (recém-cadastrado e montado). Após rodar uma certa quilometragem e ser enviado para recape, o pneu retorna como Vida 2 com uma nova banda de rodagem. O sistema mantém registro separado de cada vida em uma tabela específica, permitindo analisar se a segunda vida (após recape) rendeu mais ou menos KM que a primeira. Alguns pneus podem ter Vida 3, Vida 4, etc., dependendo do número de recapagens. O KM acumulado total (KMACUM) preserva todo o histórico, enquanto o KM da vida atual (KMVIDAATUAL) zera a cada novo recape.

- **O que fazer se montar um pneu com número de fogo errado?**

Se descobrir que montou o pneu errado logo após confirmar a operação, desmonte-o imediatamente e registre um novo rodízio com o pneu correto. O erro fica no histórico (para auditoria), mas a prática correta é verificar o número de fogo fisicamente antes de informar no sistema. Se o erro for descoberto muito depois (dias/semanas), será necessário investigar qual pneu estava realmente montado naquela posição durante esse período, pois o histórico de KM acumulado estará associado ao número de fogo errado.

- **Como o sistema calcula a "vida útil restante" de um pneu?**

A vida útil restante é calculada comparando o KM rodado na vida atual com o KM previsto configurado na banda de rodagem. Fórmula: (KM previsto − KM rodado na vida atual) / KM previsto × 100%. Exemplo: se a banda prevê 100.000 km e o pneu já rodou 80.000 km, a vida útil restante é 20%. Quando esse indicador chega a 0% (ou quando o sulco atinge o mínimo configurado), o sistema alerta que o pneu deve ser enviado para recape ou descarte. Este indicador é essencial para planejamento preventivo de substituições e evitar pneus "presos" em veículos após vencer sua vida útil.

- **Qual é o impacto de não medir sulcos com regularidade?**

Sem medições regulares de sulco, o sistema não consegue disparar alertas automáticos de desgaste. Isso pode levar a duas situações perigosas: (1) pneus com desgaste inferior ao mínimo seguro permanecem montados, comprometendo a segurança; (2) pneus são descartados prematuramente porque ninguém acompanha o desgaste e o gestor não consegue fazer decisões baseadas em dados reais. Recomenda-se medir sulcos no mínimo mensalmente ou a cada 10.000 km rodados. Essas medições alimentam indicadores como "custo por km" e "ranking de marcas", que são essenciais para decisões de compra de pneus.

#### Regras Críticas de Go Live

| **Regra 1 - Todos os Pneus Cadastrados Corretamente:** Antes de Go Live, todos os pneus da frota devem estar cadastrados em "Cadastro de Pneus" com número de fogo, marca, modelo, banda de rodagem e valor. Pneus não cadastrados não podem ser movimentados. Faça auditoria completa e crie evento de "Movimentação Inicial" para todos os pneus já montados. |
| --- |

| **Regra 2 - Configuração de Bandas de Rodagem Completa**: Todas as bandas usadas na frota devem estar cadastradas com KM previsto por vida configurado. Sem isso, o sistema não consegue calcular alertas de desgaste (80% de vida consumida) e indicadores de custo por KM. Valide que cada banda tem sulco mínimo definido. |
| --- |

| **Regra 3 - Parâmetros de Configuração Ativados**: Os parâmetros **''Utiliza pneus da sucata''**, **''Utiliza Empresa no controle de Pneus''**, **''Exige Sulco nas movimentações de pneus?''**, **''Altera profundiade dos pneus?''** devem estar configurados conforme a política operacional antes de Go Live. Alterações pós-Go Live podem desabilitar fluxos que estão em uso. |
| --- |

| **Regra 4 - Número de Fogo Único por Pneu**: Cada pneu deve ter um número de fogo único e exclusivo (por empresa, se Utiliza controle de pnus por empresa estiver ligado). Antes de montar pela primeira vez, operador deve verificar fisicamente o número de fogo no pneu e confirmar que corresponde ao cadastro no sistema. Números de fogo duplicados ou incorretos distorcem todo o histórico de KM acumulado |
| --- |

| **Regra 5 - Treinamento em Rodízio e Recape**: Operadores devem ser treinados na diferença entre desmontar para estoque, enviar para recape e descartar para sucata. Confundir essas operações causa pneus "perdidos" no sistema ou recapes registrados como descartes, comprometendo indicadores. Teste os três fluxos em homologação com um veículo real antes de Go Live. |
| --- |

| **Regra 6 - Responsável Designado para Acompanhamento de Sulcos**: Designar um responsável (analista de pneus ou supervisor) pela medição regular de sulcos (recomendado: semanal ou a cada 10.000 km). Sem medições, alertas de desgaste não funcionam e decisões de troca/recape são baseadas em achismo. Documente a frequência de medição e comunicar aos operadores. |
| --- |

#### Checklist de Configuração Pré-Go-Live

##### Cadastro Auxiliares (5 itens)

- Todos os pneus da frota cadastrados em "Cadastro de Pneus" (Logística » Gestão de Frotas » Pneus » Cadastro de Pneus) com número de fogo, marca, modelo e banda.
- Todas as bandas de rodagem cadastradas com KM previsto por vida e sulco mínimo definido.
- Todos os veículos cadastrados com eixos e posições de pneu configuradas corretamente.
- Módulo TCF – Controle de Pneus habilitado na licença do Sankhya.
- Grupos de usuários de operadores de pneus criados no sistema com permissões corretas.

**Configuração de Parâmetro (5 itens)**

- Configure o parâetro **“Utiliza Pneus de Sucata?”** conforme a política da operação, (habilita painéis de estoque, recape e sucata como origens).
- Utiliza empresa no **''Controle de Pneus?''** configurado conforme estrutura (multi-empresa ou empresa única)
- **''Exige Sulcos na Saída da Sucata?''**e **''Exige Sulcos na Entrada da Sucata?''** ativados se exigir medição de sulco em sucata
- Altera profundidade do **''Pneus no Veículo?'**' ativado se permitir edição de sulco em pneus em estoque do veículo.
- Parâmetros de KM (Atualização de KM por Módulo\*) devem ser revisados na tela de  "Configurações Frotas" **(**Configurações » Gestão de Frotas » Configurações Gestão de Frota**)** e poderão ser validados para que tabela para que a rotina registre o histórico de KM no cadastro de veículos.

**Operações e Fluxos (6 itens)**

- Teste a montagem de pneu do estoque em posição vazia no diagrama.
- Teste a desmontagem de pneu para o estoque em posição com pneu montado.
- Teste o envio de pneu para recape com registro de NF e banda de rodagem.
- Teste o rodízio entre duas posições, com e sem pneus montados nas posições.
- Teste a medição de sulco com registro de 1 a 6 canais em milímetros.
- Teste o descarte (sucata) do pneu e valide que a operação é irreversível.

**Indicadores e Rastreabilidade (4 itens)**

- Valide se o histórico de eventos dos pneus está sendo gravado corretamente com usuário, data/hora, KM e detalhes da movimentação.
- Confirme se os contadores de estoque, recape e sucata estão sendo atualizados em tempo real.
- Faça o teste do cálculo de sulco atual, KM acumulado e vida útil restante apresentados no painel lateral.
- Coloque um responsável (analista de pneus) para realizar a medição periódica dos sulcos e valide a frequência das aferições.

#### Telas Relacionadas

- **Cadastro de Pneus (**Logística » Gestão de Frotas » Pneus » Cadastro de Pneus)**:** Realize a inclusão e manutenção do cadastro de pneus com número de fogo, marca, modelo e banda de rodagem.
- **Configurações Gestão Frotas (**Logística » Gestão de Frotas » Configurações Gestão Frotas)**:** Defina os parâmetros ''Utiliza pneus do Recape e Sucata?'', ''Utiliza Empresa no Controle de Pneus?'', ''Exige Sulco nas movimentações?'', ''Altera profundidade dos Pneus?'' e ''Atualização de KM dos Módulos''.
- **Eventos de Pneu (**Logística » Gestão de Frotas » Pneus » Eventos de Pneu): Configure os tipos de eventos avulsos disponíveis para registro nas movimentações.
- **Bandas de Rodagem (**Logística » Gestão de Frotas » Pneus » Bandas de Rodagem)**:** Cadastre as bandas com definição de sulco mínimo e KM previsto por vida útil.
- **Histórico de Movimentação Pneus** (Logística » Gestão de Frotas » Pneus » Movimentação de Pneus)**:** Consulte detalhadamente todos os eventos registrados por pneu, veículo ou período.
