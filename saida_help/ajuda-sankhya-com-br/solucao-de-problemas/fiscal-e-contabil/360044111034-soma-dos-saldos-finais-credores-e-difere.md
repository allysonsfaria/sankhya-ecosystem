---
id: "360044111034"
titulo: "Soma dos saldos finais credores é diferente da soma dos saldos finais devedores no período informado nos registros de Saldos Periódicos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044111034-Soma-dos-saldos-finais-credores-%C3%A9-diferente-da-soma-dos-saldos-finais-devedores-no-per%C3%ADodo-informado-nos-registros-de-Saldos-Peri%C3%B3dicos"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:52:35Z"
rotulos: ["#balancete", "#saldo anterior diferente", "Configuração", "Relatórios", "ECD", "Contabilidade", "Financeiro", "Solução: Feche todos os lotes e meses contábeis e recomponha saldos.", "Mensagem: Diferença entre saldos credores e devedores no ECD.", "Verificação: Confira saldo final saldo inicial e transmita o ECD novamente.", "Erro", "Artigo atualizado KCS", "Fiscal/Contábil - KCS"]
---

# Soma dos saldos finais credores é diferente da soma dos saldos finais devedores no período informado nos registros de Saldos Periódicos

Erros de validação no PVA relacionados a saldos iniciais e finais, realize procedimentos de correção. Este artigo apresenta as causas e soluções para tais inconsistências.

**MENSAGEM:**

Soma dos saldos finais credores é diferente da soma dos saldos finais devedores no período informado nos registros de Saldos Periódicos.

Soma dos saldos iniciais credores é diferente da soma dos saldos iniciais devedores no período informado nos registros de Saldos Periódicos.

### Principais Situações de Saldo Indevido

- **Saldo anterior não transferido:** O saldo final de um mês não aparece como saldo inicial do mês seguinte.
- **Divergência entre saldo anterior e saldo atual:** Diferenças significativas nos totalizadores que deveriam estar zeradas ou com valores correspondentes.
- **Conta não exibida:** Conta com movimentação que não aparece no balancete mensal, mas consta no acumulado.
- **Erros na ECD:** "Soma dos saldos finais/iniciais credores diferente da soma dos devedores".

### Verificações Necessárias Antes da Correção

- **Análise de lançamentos:** Verifique se todos os lotes estão **"Fechados"**, se não há lançamentos incompletos e se as datas estão corretas.
- **Configuração de contas:** No **"Plano de Contas"** (Contabilidade >> Cadastros >> Plano de Contas), verifique o campo **"Referência de Ativação"** e se a conta está **"Ativa"** e **"Analítica"**.
- **Fechamento:** Assegure que os Lotes e o Fechamento do Mês (Contabilidade >> Arquivos >> Lotes Contábeis) foram processados corretamente.

### Solução: Recomposição de Saldos

A recomposição recalcula todos os saldos das contas a partir de uma data específica:

1. Acesse **"Empresa"** (Contabilidade >> Preferências >> Empresa).
2. Clique no botão **"Outras Opções (...)"** e selecione **"Recompor Saldos"**.
3. No campo **"Referência p/ recomposição"**, informe o último dia do mês anterior ao que apresenta o problema (ex: para erro em fevereiro, informe 31/01/YYYY).
4. Confirme a operação e aguarde o processamento.
5. Caso o problema persista, acesse a aba **"Exercício"** e execute a recomposição a partir do **"Início do Período Contábil"**.

### Verificação Pós-Correção

- Gere novamente o **"Balancete de Verificação"** e confira se o saldo inicial do mês coincide com o saldo final do anterior.
- Para casos de ECD, após a recomposição, acesse **"Geração de Arquivo - ECD"** (Contabilidade >> Conexão >> ECD >> Geração de Arquivo - ECD) e transmita novamente ao PVA.
- **Observação:** Se utilizar Consolidação de Empresas, o procedimento deve ser feito empresa a empresa antes da consolidação final.

### Situações Especiais

- **Navegador:** O Navegador Sankhya pode acumular cache. Caso a recomposição falhe, tente executar o procedimento via Google Chrome.
- **Divergência em conta específica:** Analise se não houve zeramento parcial de contas de resultado ou lançamentos sem contrapartida.
- Problema nos lançamentos:

  Partida Dobrada × Múltiplas Partidas nos lançamentos contábeis

Todo lançamento respeita o método das partidas dobradas (débitos = créditos). O que muda entre as modalidades é como o sistema numera as linhas, por meio de dois campos: **Número do Lançamento (NUMLANC)**, que identifica o fato contábil, e **Sequência (SEQUENCIA)**, que numera as linhas dentro dele.

## Partida Dobrada

Um débito e um crédito de mesmo valor, formando um par fechado:

- As 2 linhas tem um Número do Lançamento diferente e a Sequência fica **zerada (0)**;
- A cada novo lançamento, o número do lançamento avança (101, 102…).

Ex.: pagamento de duplicata de R$ 5.000 → lançamento 101, seq. 0: débito Fornecedores / → lançamento 102, seq. 0: crédito Banco.

É o formato padrão da contabilização automática (notas, financeiro).

## Múltiplas Partidas

Um fato contábil envolvendo 3 ou mais contas (rateios, desdobramentos):

- Todas as linhas têm o **mesmo Número do Lançamento**;
- A **Sequência é incrementada** (1, 2, 3…);
- O equilíbrio é no conjunto: soma dos débitos = soma dos créditos.

Ex.: folha de R$ 10.000 → lançamento 205: seq. 1 débito Despesas com Salários 10.000; seq. 2 crédito INSS 1.200; seq. 3 crédito IRRF 800; seq. 4 crédito Salários a Pagar 8.000.

Usada em lançamentos manuais com rateio e, opcionalmente, na contabilização.

## Identificação rápida

- Sequência = 0 → partida dobrada;
- Sequência 1, 2, 3… repetindo o mesmo nº de lançamento → múltiplas partidas.

## Configurações (ambas desligadas por padrão)

- **USALANCPARTDOB** ("Usa lançamento contábil como partida dobrada?"): muda apenas a exibição/digitação — a consulta mostra débito e crédito do par em uma única linha.
- **CTBZMULTPART** ("Utiliza contabilização para múltiplas partidas"): a contabilização agrupa as partidas de um mesmo documento sob um único nº de lançamento, sequenciando-as.

|  | Dobrada | Múltiplas |
| --- | --- | --- |
| Contas | 2 (1D × 1C) | 3 ou mais |
| Nº Lançamento | igual no par; avança por lançamento | igual em todas as linhas |
| Sequência | sempre 0 | 1, 2, 3… |
| Equilíbrio | no par | no conjunto |
