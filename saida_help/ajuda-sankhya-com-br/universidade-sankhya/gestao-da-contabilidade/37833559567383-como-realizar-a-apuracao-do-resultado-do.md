---
id: "37833559567383"
titulo: "Como realizar a apuração do Resultado do Exercício"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37833559567383-Como-realizar-a-apura%C3%A7%C3%A3o-do-Resultado-do-Exerc%C3%ADcio"
trilha: "Universidade Sankhya > Gestão da Contabilidade "
atualizado_em: "2026-07-22T14:07:17Z"
rotulos: ["Configuração", "Relatórios", "Impostos", "Contabilidade", "Financeiro"]
---

# Como realizar a apuração do Resultado do Exercício

| Categoria |
| --- |
| [O que é a Apuração do Resultado do Exercício?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37833559567383-Como-realizar-a-apura%C3%A7%C3%A3o-do-Resultado-do-Exerc%C3%ADcio#h_01KFGQW46T6ZFGT06QV2Y8G4XN) |
| [Quais problemas este recurso resolve?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37833559567383-Como-realizar-a-apura%C3%A7%C3%A3o-do-Resultado-do-Exerc%C3%ADcio#h_01KFGQWH4NSEYP7Q3FGCST5YA3) |
| [Demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37833559567383-Como-realizar-a-apura%C3%A7%C3%A3o-do-Resultado-do-Exerc%C3%ADcio#h_01KFGQWR53Y7ZTT102N40QNPAW) |
| [Cenário de aplicação](https://ajuda.sankhya.com.br/hc/pt-br/articles/37833559567383-Como-realizar-a-apura%C3%A7%C3%A3o-do-Resultado-do-Exerc%C3%ADcio#h_01KFGQX64DJSS6V7E2265WVVCB) |
| [É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37833559567383-Como-realizar-a-apura%C3%A7%C3%A3o-do-Resultado-do-Exerc%C3%ADcio#h_01KFGQXCJEFYR1Y112FV79C7TS) |

## Apuração do Resultado do Exercício

#### O que é a Apuração do Resultado do Exercício?

A Apuração do Resultado do Exercício é uma rotina contábil essencial para identificar se a empresa obteve lucro ou prejuízo em um determinado período, geralmente anual. Esse processo envolve o encerramento (zeramento) das contas de resultado — receitas e despesas — após a devida conciliação contábil, permitindo a elaboração de demonstrações como a DRE e o Balanço Patrimonial. O resultado obtido é fundamental para análise de desempenho, cálculo de impostos e definição de estratégias. Para garantir a apuração correta, é imprescindível realizar o fechamento mensal de todos os períodos envolvidos, especialmente o de dezembro, que encerra oficialmente o exercício social.

#### Quais problemas este recurso resolve?

- **Falta de visibilidade sobre o desempenho financeiro da empresa**, permitindo identificar se houve lucro ou prejuízo no período.
- **Dificuldade na tomada de decisões estratégicas**, já que o resultado apurado serve como base para decisões de investimento, corte de gastos e planejamento futuro.
- **Inconsistências nas demonstrações contábeis**, como DRE e Balanço Patrimonial, que dependem do correto encerramento das contas de resultado.
- **Erros no cálculo de tributos**, pois a apuração incorreta pode impactar diretamente os impostos devidos com base no resultado fiscal.
- **Problemas na transição entre exercícios contábeis**, que podem ocorrer caso os fechamentos mensais e o encerramento do exercício (dezembro) não sejam executados corretamente.
- **Acúmulo indevido de saldos em contas de resultado**, comprometendo a integridade das informações contábeis do novo exercício.
- **Falta de conformidade com normas contábeis e fiscais**, que exigem o encerramento adequado das contas ao final do exercício.

#### Demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1118228023)

#### Cenário de aplicação

A empresa Axis LTDA., do segmento atacadista, finalizou o exercício fiscal e precisa elaborar suas demonstrações contábeis com base no resultado do ano. Para isso, é necessário realizar no ERP Sankhya o encerramento das contas de resultado, garantindo que todas as receitas e despesas sejam devidamente zeradas. Esse procedimento assegura a correta apuração do lucro ou prejuízo do período e viabiliza a geração de relatórios como o DRE e o Balanço Patrimonial.

**Tarefa:** assista ao vídeo de demonstração prática e siga o passo a passo abaixo para configurar o sistema e executar o encerramento das contas de resultado. Certifique-se de que todos os meses do exercício estejam previamente fechados, em especial o mês de dezembro, que consolida o encerramento oficial do período.

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

1. Acesse a tela **Empresa**
   **Menu:** Contabilidade » Preferências » Empresa

**Aba Plano de Contas**

- Preencha o campo **Conta Contábil de Encerramento de Resultado** com o código da conta contábil que será utilizada para encerramento do resultado, sendo uma conta transitória.
  Ex.: 3080 - APURACAO DO RESULTADO DO EXERCICIO
- Salve a alteração.

2. Acesse a tela **Zeramentos de Contas**
   **Menu:** Contabilidade » Rotinas » Zeramentos de Contas

- Na janela Procurando por Empresa, selecione o registro da empresa.
- Preencha no campo **Número do Lote** o número do lote contábil onde serão registrados os lançamentos de apuração do resultado.
  Ex.: 999 (Normalmente o mesmo código é atribuído à todos os lotes)
- Informe no campo **Data do Movimento** o último dia do  mês referente ao zeramento contábil.
- Preencha o campo **Histórico** com conteúdo que será utilizado nos lançamentos contábeis.
  Ex.: ZERAMENTO DE CONTAS DE RESULTADO (Previamente cadastrado na rotina Histórico Padrão)

**Intervalo de grupos para zeramento**

- Defina nos campos **Grupo Inicial** e **Grupo Final**, o intervalo das contas que serão zeradas. 
  Valide na rotina Plano de Contas a primeira e ultima conta contábil do grupo RESULTADO.

**Contas para o resultado final**

- Informe a **Conta prejuízo** e **Conta lucro** para as quais serão transferidos os saldos após o encerramento.
- Acione o botão ”**Salvar Configurações**”.
- Clique no botão **Efetuar Zeramento** e confirme o processo no pop-up que irá se abrir.

3. Acesse a tela **Lotes Contábeis**

**Menu:** Contabilidade  »  Arquivos »  Lotes Contábeis

- **Filtros rápidos**
- No Intervalo de Lotes informe o lote gerado na rotina Zeramento de Contas
  Ex.: 999
- Aplique o filtro para buscar o lançamento.
- Nas colunas é possível verificar:

  - **Usuário responsável pela contabilização**
  - **Nro. Lote**
  - **Referência**
  - **Data do Movimento**
  - **Total do Lote**
  - **Situação**
- Caso seja necessário reverter o zeramento das contas, realize a exclusão do lote correspondente por meio da tela **Lotes Contábeis.**
