---
id: "43548018874647"
titulo: "Ordem de produção finalizada sem baixa de matéria-prima no estoque."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43548018874647-Ordem-de-produ%C3%A7%C3%A3o-finalizada-sem-baixa-de-mat%C3%A9ria-prima-no-estoque"
trilha: "Solução de Problemas > Produção"
atualizado_em: "2026-10-13T21:11:17Z"
rotulos: ["Artigo criado KCS", "Produção - KCS"]
---

# Ordem de produção finalizada sem baixa de matéria-prima no estoque.

Entenda por que a baixa de matéria-prima pode não ocorrer ao finalizar uma Ordem de Produção e saiba como corrigir.

Ao finalizar uma Ordem de Produção (OP) no Sankhya, é esperado que o sistema já tenha realizado automaticamente a baixa das matérias-primas utilizadas no processo produtivo. No entanto, em alguns cenários, a OP é finalizada e o estoque das matérias-primas não é baixado, gerando inconsistências no controle de insumos e no saldo do estoque. Este artigo apresenta as principais causas para esse comportamento, orienta como identificar o problema e detalha as melhores práticas para garantir que a baixa ocorra corretamente.

A ausência da baixa de matéria-prima pode impactar diretamente o controle de estoque, a rastreabilidade dos insumos e a acuracidade dos custos de produção. Por isso, é fundamental revisar as configurações do processo produtivo, das operações de estoque e dos tipos de operação (TOP) envolvidos na produção, especialmente em cenários de industrialização para terceiros ou uso de estoque de terceiros em poder da empresa.

### Principais causas da OP sem baixa de matéria-prima

A falha na baixa de matéria-prima ao finalizar uma OP pode ocorrer por diversos motivos, sendo os principais:

**(1)** **Configuração inadequada do tipo de operação (TOP):** a **TOP** utilizada para a baixa deve estar configurada para atualizar o estoque corretamente, aba **"Estoque"**, campo **"Atualiza Estoque MP = Baixar".**

**Obs.:** Avaliar se a **TOP** for para estoque de terceiros, deve estar devidamente configurada na aba **"Estoque de Terceiros".** Se a MP for de estoque de terceiros, na tela de "**Composição do Produto"** (Produção » Cadastros » Composição do Produto), tem a marcação **"Estoque de Terceiros"**, que precisa ser realizada, senão o sistema tenta baixar o estoque próprio do produto.

**(2)** **Erro de versão:** Caso seja analisado toda a configuração e processo, e mesmo assim o sistema não realizar a baixa das MPs em novas OPs, é necessário abrir um chamado com o **Service Desk**, para análise do cenário.

### Como corrigir o problema

Caso identificadas as OPs que não ocorreram baixa de MPs, siga o passo a passo abaixo:

**(1)** Caso identificado a falta de configuração em alguma parte do processo, é necessário que realize as alterações necessárias, para as novas OPs ou novas notas geradas, seguirem a configuração atual.

**(2)**  Caso a OP tenha sido finalizada, não há como nativamente reabrir a Ordem de Produção, desta forma será necessário realizar um ajuste de estoque, para gerar a saída das MPs do estoque.

**(3)** Se a OP não foi finalizada, verifique se o apontamento que gerou a nota de produção pode ser apagado, se sim, depois é somente realizar um novo apontamento após apagar o anterior.

### Boas práticas para evitar o problema

Para evitar que a OP seja finalizada sem a baixa de matéria-prima, siga estas melhores práticas:

**(1)** Mantenha a TOP de Produção **(TIPMOV: F - PRODUÇÃO)** sempre atualizada e alinhada com o fluxo de estoque desejado, principalmente em operações com/de terceiros.

**(2)** Realize periodicamente a conferência dos saldos de matéria-prima no estoque e nas movimentações acessórias para identificar possíveis inconsistências.

**(3)** Validar também as demais **configurações relacionadas ao controle de estoque**, incluindo a validação de estoque no **grupo de produtos**, o **local de estoque**, o **controle por lote**, a **data de validade** e o **status do lote**, garantindo que todas estejam configuradas corretamente e de acordo com as regras do processo.

Seguindo essas orientações, é possível garantir que a baixa de matéria-prima ocorra corretamente ao gerar o apontamento da nota de produção, mantendo o controle de estoque preciso e evitando retrabalhos no processo produtivo.
