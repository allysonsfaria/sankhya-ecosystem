---
id: "25939506530327"
titulo: "Como calcular a folha em segundo plano"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/25939506530327-Como-calcular-a-folha-em-segundo-plano"
trilha: "Manual do Produto > Pessoas+ > Folha Mensal > Cálculo da Folha"
atualizado_em: "2026-10-02T15:35:19Z"
rotulos: ["Configuração", "Preferências", "Folha de Pagamento", "Pessoal+", "Rotinas Folha"]
---

# Como calcular a folha em segundo plano

#### **(1)** Objetivo:

Proporcionar aos usuários uma gestão mais eficiente e visível das folhas de pagamento, facilitando o acompanhamento e o controle dos processos de cálculo e gravação dessas folhas.

#### **(1)** Em qual versão está disponível?

A funcionalidade será liberada para todos os clientes a partir da versão 5.18 do Pessoal +. 
Para utilização em versões anteriores é necessário ligar o parâmetro: "FPCALCFOLASYNC".

![Imagem 1: A funcionalidade será liberada para todos os clientes a partir da versão 5.18 do Pessoal +. Para utilização em versões…](https://ajuda.sankhya.com.br/hc/article_attachments/25939506509719)

#### **(1)** Como realizar o processo?

Para efetuar o cálculo, siga o processo normal pela tela de **"Cálculos"** (Pessoal+ » Rotinas Folha » Cálculos). Na opção **"Coletivo"** selecione o tipo de cálculo que deseja realizar, clicando no devido card. Preencha as abas de acordo com a necessidade para o cálculo que deseja fazer e clique em calcular:

![Imagem 2: Para efetuar o cálculo, siga o processo normal pela tela de "Cálculos" (Pessoal+ » Rotinas Folha » Cálculos). Na opção…](https://ajuda.sankhya.com.br/hc/article_attachments/25939506512023)

Com essa nova funcionalidade, terá a apresentação da seguinte tela com estatísticas:

![Imagem 3: Com essa nova funcionalidade, terá a apresentação da seguinte tela com estatísticas:](https://ajuda.sankhya.com.br/hc/article_attachments/25939489626007)

**Botão Parar:** responsável pelo processo de cálculo. Fazendo esta ação as folhas que já foram calculadas e gravadas permanecem. 

**Botão Processos:** fornece o acompanhamento dos cálculos que estão sendo gerados no sistema, por usuário e tipo de folha. Tem-se uma melhor análise de performance a depender dos processos que estão sendo executados no sistema e melhora a comunicação entre setores.

![Imagem 4: Botão Parar: responsável pelo processo de cálculo. Fazendo esta ação as folhas que já foram calculadas e gravadas…](https://ajuda.sankhya.com.br/hc/article_attachments/25939506515351)

#### **(1)** O que acontece se fechar a tela?

Ao fechar a tela de cálculo, o processo não é encerrado, ele continua a ação. Para retornar ao dash de cálculo em andamento, existe o botão na barra lateral para acompanhamento. Ou seja, o processo não é perdido.

![Imagem 5: Ao fechar a tela de cálculo, o processo não é encerrado, ele continua a ação. Para retornar ao dash de cálculo em…](https://ajuda.sankhya.com.br/hc/article_attachments/25939506517655)

#### **(1)** Consigo visualizar as folhas que já foram calculadas?

Sim, mesmo que ainda existam cálculos em andamento, é possível conferir os que já foram processados.
Para isso, acesse o **"Gerenciador de Folhas"** (Pessoal+ » Rotinas Folha » Gerenciador de Folhas) e selecione a folha desejada:

![Imagem 6: Sim, mesmo que ainda existam cálculos em andamento, é possível conferir os que já foram processados. Para isso, acesse…](https://ajuda.sankhya.com.br/hc/article_attachments/25939506519703)

Em seguida clicando no card é possível visualizar todas folhas que já foram concluídas e realizar as conferências desejadas:

![Imagem 7: Em seguida clicando no card é possível visualizar todas folhas que já foram concluídas e realizar as conferências…](https://ajuda.sankhya.com.br/hc/article_attachments/25939820567063)

Retornando a tela de Cálculos, ao concluir todos os processos, serão apresentadas as informações do cálculo concluído:

![Imagem 8: Retornando a tela de Cálculos , ao concluir todos os processos, serão apresentadas as informações do cálculo concluído:](https://ajuda.sankhya.com.br/hc/article_attachments/25939794711063)

#### **(1)** Se alguma folha apresentar erro, devo refazer todo processo?

Caso alguma folha apresentar erro, será demonstrado na tela:

![Imagem 9: Caso alguma folha apresentar erro, será demonstrado na tela:](https://ajuda.sankhya.com.br/hc/article_attachments/25939794712599)

Nesta situação, acesse a tela de Cálculos e calcule somente as folhas que apresentaram erro. Para isso, marque a opção **“Apenas folhas não calculadas”**:

![Imagem 10: Nesta situação, acesse a tela de Cálculos e calcule somente as folhas que apresentaram erro. Para isso, marque a opção…](https://ajuda.sankhya.com.br/hc/article_attachments/25939820573079)

**Observação:** essa opção poderá ser utilizada também nos casos em que optar por calcular somente uma parte das folhas e desejar calcular o restante posteriormente. Assim, marque a opção que serão demonstradas apenas as folhas que não possuem cálculo na referência selecionada.

#### **(1)** Consigo definir o número de processos e lotes a serem processados?

Sim! Nesta funcionalidade existem dois parâmetros (Configurações » Avançado » Preferências), que podem ser personalizados para melhor distribuição de memória na hora de executar o cálculo:

**Nome:** **FPQTDPROCALCFOL**
**Descrição:** Qtd. Max. processos para cálculo de folha
**Padrão:** 10
**Objetivo:** define a quantidade máxima de processos paralelos para o cálculo da folha. Ou seja, haverá no máximo N processos rodando cálculo

**Nome:** **FPTAMLOTCALCFOL**
**Descrição:** Tamanho do lote para cálculo de folha
**Padrão**: 20
**Objetivo:** define o tamanho do lote de folhas para o cálculo. Ou seja, cada processo irá calcular no máximo N folhas por vez.
