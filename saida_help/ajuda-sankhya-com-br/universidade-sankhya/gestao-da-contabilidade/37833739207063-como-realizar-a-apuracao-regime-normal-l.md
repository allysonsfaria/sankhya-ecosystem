---
id: "37833739207063"
titulo: "Como realizar a Apuração Regime Normal - Lucro Real"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37833739207063-Como-realizar-a-Apura%C3%A7%C3%A3o-Regime-Normal-Lucro-Real"
trilha: "Universidade Sankhya > Gestão da Contabilidade "
atualizado_em: "2026-07-22T14:07:16Z"
rotulos: ["Configuração", "ECF", "Fiscal", "Impostos", "Financeiro", "DCTF", "Lucro Real"]
---

# Como realizar a Apuração Regime Normal - Lucro Real

| **Categoria** |
| --- |
| [O que é a Apuração Regime Normal - Lucro Real?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37833739207063-Como-realizar-a-Apura%C3%A7%C3%A3o-Regime-Normal-Lucro-Real#h_01KFGR2PG606ZGSWT8T2PJX20R) |
| [Quais problemas este recurso resolve?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37833739207063-Como-realizar-a-Apura%C3%A7%C3%A3o-Regime-Normal-Lucro-Real#h_01KFGR30RMYY5J8VZ0JPPJE7ZA) |
| [Demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37833739207063-Como-realizar-a-Apura%C3%A7%C3%A3o-Regime-Normal-Lucro-Real#h_01KFGR376VHN62Q1KTH49ZHVQC) |
| [Cenário de aplicação](https://ajuda.sankhya.com.br/hc/pt-br/articles/37833739207063-Como-realizar-a-Apura%C3%A7%C3%A3o-Regime-Normal-Lucro-Real#h_01KFGR3GX82Z0HZ0XMP8BTARA1) |
| [É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37833739207063-Como-realizar-a-Apura%C3%A7%C3%A3o-Regime-Normal-Lucro-Real#h_01KFGR3PJXSR8MJV3KHZ57JR3W) |

## Apuração Regime Normal - Lucro Real

#### O que é a Apuração Regime Normal - Lucro Real?

A apuração do Lucro Real é uma rotina contábil e fiscal adotada por empresas que optam por esse regime tributário, no qual os tributos são calculados com base no lucro efetivamente apurado, considerando receitas, despesas, custos e ajustes fiscais. Realizada anualmente, essa apuração exige o fechamento do balanço contábil ao final do ano calendário e o cumprimento de obrigações acessórias como ECF e DCTF. Mensalmente, as empresas devem recolher IRPJ e CSLL por estimativa, com base no lucro real ajustado, que envolve adições e exclusões ao lucro contábil, compensação de prejuízos fiscais e aplicação de alíquota adicional quando os lucros ultrapassam certos limites.

#### Quais problemas este recurso resolve?

- **Inadequação no cálculo dos tributos**: Garante que IRPJ e CSLL sejam calculados com base no lucro efetivo, evitando pagamentos indevidos ou insuficientes.
- **Inconsistências entre contabilidade e fiscal**: Alinha o resultado contábil ao tributário por meio de ajustes, adições e exclusões.
- **Riscos de autuações fiscais**: Ao cumprir rigorosamente as exigências legais e entregar obrigações acessórias (como ECF e DCTF), reduz o risco de penalidades por descumprimento.
- **Dificuldade em aproveitar prejuízos fiscais**: Permite compensar prejuízos de períodos anteriores, otimizando a carga tributária.
- **Falta de controle sobre os impactos tributários de decisões operacionais**: Favorece o acompanhamento mais detalhado das operações e seus reflexos na tributação.
- **Desorganização no planejamento tributário**: Viabiliza um planejamento mais preciso, baseado em dados reais da empresa.

#### Demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1118227916)

#### Cenário de aplicação

A empresa Axis LTDA., do segmento atacadista, é enquadrada no regime tributário do Lucro Real em função de seu alto faturamento e da complexidade de suas operações. Com a proximidade do encerramento do exercício, a equipe fiscal precisa assegurar que todas as parametrizações estejam corretas no ERP Sankhya para possibilitar o cálculo adequado do IRPJ e da CSLL. Além disso, é necessário contemplar ajustes fiscais, controle de prejuízos compensáveis e o cumprimento das obrigações acessórias previstas em lei, como a ECF e a DCTF.

**Tarefa**: assista ao vídeo de demonstração prática e siga o passo a passo abaixo para configurar a apuração do Lucro Real no sistema. Garanta que os parâmetros fiscais estejam ajustados, que os critérios de compensação de prejuízos sejam corretamente aplicados e que os relatórios necessários para o envio das obrigações acessórias estejam devidamente habilitados.

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

1. Acesse a tela **Plano de Contas**

**Menu:** Contabilidade » Cadastros » Plano de Contas

**Aba e-LALUR Parte A**

- Em todas as contas de RESULTADO devem estar com o campo **Conta de Resultado** marcados nas seções **Classificação IRPJ** e **Classificação CSLL**.
- Em todas as contas de ADIÇÕES devem estar com o campo **( + ) Adições** marcados nas seções **Classificação IRPJ** e **Classificação CSLL**.
- Em todas as contas de EXCLUSÕES devem estar com o campo **( - ) Exclusões** marcados nas seções **Classificação IRPJ** e **Classificação CSLL**.
- Nas contas que representam ALIMENTAÇÃO DO TRABALHADOR do programa PAT devem estar com o campo **Conta de Resultado** marcados nas seções **Classificação IRPJ** e **Classificação CSLL** e na aba Geral o campo PAT 4% deve estar marcado também.
- A conta de RESULTADO DO EXERCICIO deve estar com o campo **Zeramento de** **Contas de Resultado** marcados nas seções **Classificação IRPJ** e **Classificação CSLL**.
  Nesta conta, todos os campos da aba e-LALUR Parte B também devem estar preenchidos.

2. Acesse a tela **Apuração do Regime Normal - Lucro Real**
   **Menu:** Contabilidade » Rotinas » Apuração do Regime Normal - Lucro Real

- Clique em “+” (Cadastrar Apuração)
- Defina nos campos indicados:

  - **Empresa**
  - **Referência**
  - **Forma de Apuração**
- Salve o registro e em seguida acione o botão “**Calcular**” e selecione **Calculo Imposto Parte A**.
- Insira um novo registro por meio do botão **Novo(+)** informe a **Empresa** e a **Referência** que deseja apurar, além de definir a **Forma de Apuração**, se Trimestral ou Mensal/Anual.

**Aba Apuração IRPJ apresenta:**

- **Lucro Antes IRPJ:** mostra o valor acumulado por competência, mês a mês, conforme os lançamentos contábeis das contas configuradas.
- **Total das Adições / Total das Exclusões:** apresentam os saldos das contas configuradas como adições ou exclusões no plano de contas, que podem ser incluídas, excluídas ou editadas nas abas específicas.
- **Resultado Líquido Ajustado:** é o primeiro totalizador da apuração, considerando os ajustes feitos a partir do lucro contábil.

**Aba Apuração CSLL apresenta:**

- **Lucro Antes CSLL:** apresenta o valor acumulado por competência, mês a mês, conforme os lançamentos contábeis das contas configuradas.
- **Total das Adições / Total das Exclusões:** mostram os saldos das contas configuradas como adições ou exclusões no plano de contas, podendo ser incluídas, excluídas ou editadas nas abas específicas.
- **Resultado Liquido Ajustado:** representa o primeiro totalizador desta apuração.

Mais informações e detalhamento dos cálculos realizados acesse [Ajuda Sankhya - Apuração do Regime Normal - Lucro Real](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607314-Apura%C3%A7%C3%A3o-do-Regime-Normal-Lucro-Real)
