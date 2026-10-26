---
id: "44011162924567"
titulo: "[TMS] - Tela de Auditoria de Fretes do TMS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011162924567--TMS-Tela-de-Auditoria-de-Fretes-do-TMS"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T18:56:24Z"
rotulos: ["sync_hc", "lincros", "sync_hash_a7ef68f48bd4", "lincros_13439315"]
---

# [TMS] - Tela de Auditoria de Fretes do TMS

## 1 - Problema Relatado pelo Cliente

O cliente precisa realizar a auditoria dos CT-es que foram importados com sucesso, mas que apresentam divergência entre o valor calculado pelo TMS através da Tabela de Frete, e o valor informado pela transportadora no CT-e. Além disso, deseja compreender como utilizar corretamente todos os filtros disponíveis na tela de Auditoria de Fretes para localizar e analisar os documentos de forma precisa.

---

## 2 - Passo a Passo para Resolver o Problema

## Acessar a Auditoria de Fretes

1. **Acessar o menu:**

   - Operacional > Processos > Auditoria de fretes.
2. **Visualizar os CT-es com divergência:**

   - Na tela serão exibidos todos os CT-es que:

     - Foram importados com sucesso no TMS.
     - Apresentam divergência entre o valor calculado pelo TMS e o valor realizado pela transportadora, informado no CT-e.

**Considerações importantes:**

- A tela de auditoria de fretes apresenta, por padrão, os CT-es com divergência de cálculo.
- Para que os CT-es sejam listados nesta tela, não podem ter erros de importação de XML.

---

## Analisar e corrigir as divergências

1. **Expandir as informações:**

   - Clique na seta localizada no início de cada linha do CT-e desejado.
2. **Verificar os detalhes do CT-e:**

   - Identifique o Pré-conhecimento vinculado ao CT-e.
   - Consulte informações da carga, como peso e valor da Nota Fiscal.
   - Detalhe e compare os componentes calculados com os realizados para identificar onde está a divergência de valor. Os componentes podem ser listados sem correlação entre o componente proveniente do CT-e, e o componente do TMS informado na Tabela de Frete. Para que haja correlação, e o valor calculado e realizado sejam exibidos na mesma linha, o cadastro de de/para de componente deve ser feito previamente ([consulte aqui o artigo sobre cadastro de de/para de componente de frete](https://lincros.movidesk.com/kb/pt-br/article/537421/como-realizar-o-de-para-de-componentes-de-frete))
3. **Realizar as correções:**

   - Após identificar a divergência, faça as correções necessárias.
   - Muitas divergência entre o frete calculado pelo TMS e o frete realizado pela Transportadora, se devem a dados diferentes informados no pré-conhecimento e CT-e. Para isso, sempre confira:

     - Se o peso considerado para cálculo informado no pré-conhecimento e no CT-e da transportadora é o mesmo
     - Se o ICMS está sendo distribuído entre os componentes, ou se está sendo destacado
     - Se a rota buscada para cálculo do frete está correta.
     - Se a origem e/ou destino do pré-conhecimento são os mesmos informados no CT-e.
     - Se a cubagem está correta, e se é a mesma informada tanto no pré-conhecimento, quanto no CT-e.
     - Se há taxas que a transportadora cobrou a mais ou a menos, ou se há taxas divergentes na tabela de frete do TMS.
     - Se a tabela de frete utilizada para o cálculo do frete no TMS está correta e possui todas as faixas de peso informadas corretamente, ou se os valores mínimos ou fixos estão informados de acordo com a negociação com a transportadora.
     - Se há restrições de busca na tabela de frete buscada para cálculo do frete do pré-conhecimento.

---

## Ajuste de Filtro - CT-es do tipo Tomador = Destinatário

1. **Verificação de CT-es não listados:**

   - Caso o CT-e seja do tipo **Tomador = Destinatário** e não apareça na tela de Auditoria de Fretes, altere o filtro de busca.
   - Por padrão, o sistema lista os CT-es do tipo **'CIF'**. Para localizar esse tipo de CT-e, altere o filtro para **'FOB'**.

---

## Utilização e explicação dos filtros de pesquisa da tela de Auditoria de Fretes

A tela de Auditoria de Fretes conta com diversos filtros que auxiliam na localização e análise dos CT-es. A seguir, a explicação de cada campo disponível:

- **Unidade:** permite filtrar os CT-es por uma unidade específica.
- **Grupo de Unidades:** possibilita selecionar um grupo de unidades previamente configurado.
- **Transportadora:** define qual transportadora será considerada na pesquisa.
- **Emissão:** intervalo de datas de emissão do CT-e.
- **Data resolução pendência:** permite filtrar por data de resolução das pendências de divergência.
- **Frete calc.:** define um critério para o valor do frete calculado (igual, maior, menor etc.).
- **Frete:** define um critério para o valor do frete informado pela transportadora.
- **Número da fatura:** permite buscar CT-es vinculados a um número específico de fatura.
- **Somente divergentes:** ao marcar, exibe apenas os CT-es com divergência entre o valor calculado e o informado.
- **Somente resolvidas:** ao marcar, exibe apenas os CT-es cujas divergências já foram resolvidas.
- **Tolerância por transportadora:** se marcada, considera a tolerância de divergência configurada individualmente por transportadora.
- **Utiliza valor da transportadora:** define se a auditoria considera:

  - **Todos:** exibe todos os CT-es, independentemente de considerar ou não o valor da transportadora.
  - **Sim:** exibe apenas os CT-es que utilizam o valor da transportadora.
  - **Não:** exibe apenas os CT-es que não utilizam o valor da transportadora.
- **Tolerância geral:** permite definir uma margem de tolerância de valor absoluto para a auditoria.
- **Percentual de tolerância:** define uma margem de tolerância percentual para divergências.
- **Marcadores do conhecimento:** filtro para buscar CT-es conforme marcadores específicos atribuídos ao conhecimento.
- **Marcadores do remetente:** busca CT-es com marcadores atribuídos ao remetente.
- **Marcadores do destinatário:** busca CT-es com marcadores atribuídos ao destinatário.
- **Natureza de operação:** possibilita filtrar CT-es por natureza de operação.
- **Forma de negociação:** define a forma de negociação do frete. Por padrão, o sistema utiliza o tipo **'CIF'**, mas pode ser alterado para **'FOB'** conforme a necessidade.
- **Tipo de operação:** permite selecionar o tipo de operação desejada (ex.: entrada, saída)
