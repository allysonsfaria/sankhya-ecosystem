---
id: "43548298829207"
titulo: "Produto acabado não aparece no MPS de demanda por giro"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43548298829207-Produto-acabado-n%C3%A3o-aparece-no-MPS-de-demanda-por-giro"
trilha: "Dúvidas Frequentes > Produção"
atualizado_em: "2026-09-30T13:23:08Z"
rotulos: ["Artigo criado KCS", "Produção - KCS"]
---

# Produto acabado não aparece no MPS de demanda por giro

Por que o produto acabado não é exibido no MPS quando ocorre a realização da análise de giro?

Ao realizar a configuração de Demanda por Giro no MPS (Plano Mestre de Produção), pode ocorrer de determinados produtos acabados não aparecerem na listagem de itens do plano. Essa situação normalmente está relacionada a configurações específicas do processo produtivo, filtros aplicados ou ausência de dados necessários para o cálculo do giro no período analisado.

### Principais motivos para o produto não aparecer

O produto acabado pode não aparecer no MPS de análise de giro devido a:

**(1)** Ausência de vínculo do produto a um **"Processo Produtivo Padrão"**. Apenas produtos vinculados a um processo produtivo definido como padrão ou padrão por produto são inseridos automaticamente no plano.

**(2)** Produto sem **"Movimentação (giro)"** no período analisado. Se o produto não teve vendas, transferências ou outras movimentações consideradas no giro.

**(3)** Filtros aplicados na **configuração do MPS**. É necessário verificar se não está com algum impeditivo no filtro, como exemplo, selecionar alguma marca em específico do produto, local de estoque diferente ou grupo de produtos.

**(4)** Utilização do **período do planejamento** incorreto, que não contempla movimentações recentes do produto acabado.

### Considerações finais e dicas

Mantenha os processos produtivos atualizados e publicados, garantindo que todos os produtos acabados estejam corretamente vinculados.

Revise periodicamente os filtros e parâmetros utilizados na configuração do MPS, ajustando-os conforme a necessidade do seu processo produtivo e das movimentações do estoque, para garantir que todos os produtos relevantes sejam considerados no MPS.
