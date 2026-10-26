---
id: "43548537816215"
titulo: "Por que uma ordem de produção finalizada em \"Ordens de Produção - Nova\" não aparece na \"Análise de Custos de Produção\"?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43548537816215-Por-que-uma-ordem-de-produ%C3%A7%C3%A3o-finalizada-em-Ordens-de-Produ%C3%A7%C3%A3o-Nova-n%C3%A3o-aparece-na-An%C3%A1lise-de-Custos-de-Produ%C3%A7%C3%A3o"
trilha: "Dúvidas Frequentes > Produção"
atualizado_em: "2026-10-09T11:28:40Z"
rotulos: ["Artigo criado KCS", "Produção - KCS"]
---

# Por que uma ordem de produção finalizada em "Ordens de Produção - Nova" não aparece na "Análise de Custos de Produção"?

Ao finalizar uma Ordem de Produção (OP) na tela **Ordens de Produção - Nova** (Produção » Rotinas » Ordens de Produção - Nova), é esperado que ela seja exibida no dia seguinte na tela **Análise de Custos de Produção** (Produção » Consultas » Análise de Custos de Produção), para acompanhamento e análise dos custos envolvidos.

Em alguns casos, a OP finalizada não aparece na análise, o que gera dúvidas sobre a consistência das informações entre as duas rotinas.

![Imagem 1: Em alguns casos, a OP finalizada não aparece na análise, o que gera dúvidas sobre a consistência das informações entre…](https://ajuda.sankhya.com.br/hc/article_attachments/44009747474839)

O comportamento normalmente está relacionado aos filtros, ao tipo de processo produtivo, à geração das notas de produção ou à configuração do custo previsto. Os principais motivos são:

**(1)** Se a OP estiver fora do período, empresa, produto, grupo de produtos ou número de OP filtrados, ela não será exibida.

**(2)** A tela exibe os dados conforme o tipo de análise escolhido **(por Nota ou por OP)**. Conferir se o tipo selecionado é o esperado evita a impressão de que a OP não foi carregada.

**(3)** Atualmente a rotina **não atende** processos produtivos de:

- Desmonte
- Reprocesso
- Produção Conjunta
- Produção para Terceiros

OPs desses processos não são analisadas nessa tela. Além disso, notas de produção de subprodutos por perda/refugo ainda não são consideradas (previsto para atualizações futuras).

**(4)** A análise depende das notas de produção e dos apontamentos de consumo. Se a OP não está finalizada, se há apontamentos ou movimentações pendentes, ou se a nota de produção não foi gerada ou está inconsistente, a OP pode não aparecer ou aparecer com dados incompletos.

**(5)** O custo previsto é calculado por um **JOB (serviço)** que roda diariamente e considera o dia anterior. Ele depende do parâmetro `PRDCUSTOPREVPRD` ativo, e a geração retroativa respeita o parâmetro `PRDDIASRETRCUS` (padrão de 90 dias). Por isso, produções mais antigas ou muito recentes podem não ter o custo previsto disponível.

**Obs.:** O **JOB** roda **todo dia**, a partir da **00h.**

**(7)** O usuário precisa ter acesso à tela em Configurações » Controle de Acessos » Acessos.

**(8)** Valide personalizações existentes nos cabeçalhos e itens de quaisquer notas/pedidos, pois para apresentação dos custos na tela, sistema cria notas fakes das notas de produção.

### Como a tela funciona

Antes de investigar, vale lembrar dois pontos que influenciam o que é exibido:

- **Tipo de análise:** a tela pode ser consultada **por Nota de Produção** ou **por Ordem de Produção**. Na análise por OP, a grade superior mostra as OPs, somando os itens fabricados nas notas de produção de cada uma. Na análise por nota, mostra as notas individualmente.
- **Origem dos dados:** o custo previsto vem da ficha técnica do produto (tela **Composição do Produto**). O custo realizado vem dos apontamentos de consumo e das notas de produção geradas.

Caso após toda análise realizada, a nota ou OP ainda não seja apresentada, é necessário acionar o Service Desk para uma análise mais aprofundada do cenário.
