---
id: "42228740888727"
titulo: "Como fazer a integração contábil da provisão de férias e 13º"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42228740888727-Como-fazer-a-integra%C3%A7%C3%A3o-cont%C3%A1bil-da-provis%C3%A3o-de-f%C3%A9rias-e-13%C2%BA"
trilha: "Manual do Produto > Pessoas+ > Integração Contábil e Financeira > Execução das Integrações Contábil e Financeira"
atualizado_em: "2026-10-02T17:51:11Z"
rotulos: ["br.com.sankhya.rh.GerenciadorFolha", "Integração Contábil da Provisão de Férias e 13º Salário", "Provisão de Férias e 13º"]
---

# Como fazer a integração contábil da provisão de férias e 13º

**Módulo:** Pessoal+
**Caminho de Acesso:** Pessoal+ > Rotinas Folha > Gerenciador de Folhas > Provisão de Férias e 13º
**ID da Tela**: br.com.sankhya.rh.GerenciadorFolha

---

### Sumário

[Descrição e Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/42228740888727-Como-fazer-a-integra%C3%A7%C3%A3o-cont%C3%A1bil-da-provis%C3%A3o-de-f%C3%A9rias-e-13%C2%BA#h_01KYDTBVW1SD3PEBAK36ENRDKA)

1. [Pré-requisitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/42228740888727-Como-fazer-a-integra%C3%A7%C3%A3o-cont%C3%A1bil-da-provis%C3%A3o-de-f%C3%A9rias-e-13%C2%BA#h_01KYDTBVW2RNTT4QSQ2M9RY65B)
2. [Jornada de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/42228740888727-Como-fazer-a-integra%C3%A7%C3%A3o-cont%C3%A1bil-da-provis%C3%A3o-de-f%C3%A9rias-e-13%C2%BA#h_01KYDTBVW47RBFTA3Q0Q3BFXW9)
   [2.1 Realizar a Integração Contábil de Provisões](https://ajuda.sankhya.com.br/hc/pt-br/articles/42228740888727-Como-fazer-a-integra%C3%A7%C3%A3o-cont%C3%A1bil-da-provis%C3%A3o-de-f%C3%A9rias-e-13%C2%BA#h_01KYDTFVVF7VFT5GZV59Q8V73B)
   [2.2 Conferir o relatório de provisões](https://ajuda.sankhya.com.br/hc/pt-br/articles/42228740888727-Como-fazer-a-integra%C3%A7%C3%A3o-cont%C3%A1bil-da-provis%C3%A3o-de-f%C3%A9rias-e-13%C2%BA#h_01KYDTSMY55E2J1DSRNECPYT7Z)
3. [Pontos de Atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/42228740888727-Como-fazer-a-integra%C3%A7%C3%A3o-cont%C3%A1bil-da-provis%C3%A3o-de-f%C3%A9rias-e-13%C2%BA#h_01KYDTBVWA3Q2DMVPT1DN0TD61)
4. [Dicas de Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/42228740888727-Como-fazer-a-integra%C3%A7%C3%A3o-cont%C3%A1bil-da-provis%C3%A3o-de-f%C3%A9rias-e-13%C2%BA#h_01KYDTBVWC98RX0YNNJRD7AN4R)

[Perguntas Frequentes (FAQ)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42228740888727-Como-fazer-a-integra%C3%A7%C3%A3o-cont%C3%A1bil-da-provis%C3%A3o-de-f%C3%A9rias-e-13%C2%BA#h_01KYDTBVWDPD8GN6MNJVTXXFMS)

---

## Descrição e Usabilidade

As provisões são valores reservados para atender despesas futuras com férias, 13º salário e rescisão dos colaboradores. Esse cálculo acontece automaticamente: sempre que a folha de pagamento é calculada, o sistema calcula também as provisões correspondentes, com base nas configurações contábeis e nas fórmulas de cálculo associadas a cada tipo de provisão.

As provisões podem ser conferidas de duas formas: de modo coletivo, pelo Gerenciador de Folhas, ou individualmente, dentro do cálculo da folha de cada colaborador.

Depois que a folha de pagamento já foi integrada com a contabilidade, é possível realizar também a integração contábil específica das provisões de férias e 13º salário. Essa etapa é normalmente utilizada por quem é responsável pela contabilização da folha, em conjunto com as regras definidas pela equipe de contabilidade da empresa.

| 🚨 **Nota de atualização**  A partir da **versão 5.111**, o acesso à integração contábil das provisões deixou de ser um botão isolado no **Gerenciador de Folhas** e passou a fazer parte do menu unificado **Calcular Provisão em Lote**, junto com o cálculo da provisão e o acompanhamento da execução. A funcionalidade de integração em si não mudou — apenas o local de acesso.   | **Antes** | **Depois** | | --- | --- | | [GIF animado: Imagem 1: Depois](https://ajuda.sankhya.com.br/hc/article_attachments/42438209317911) | [GIF animado: Imagem 2: GIF animado: Imagem 1: Depois](https://ajuda.sankhya.com.br/hc/article_attachments/42438356110871) | |
| --- | --- | --- | --- | --- |

### 1. Pré-requisitos

Antes de realizar a integração contábil das provisões, verifique se:

- a folha de pagamento da referência já foi calculada, pois é nesse momento que as provisões são geradas;
- o cálculo da provisão de férias e 13º salário da referência já foi executado (via menu **Calcular Provisão em Lote**) — sem isso, os valores não aparecem na tela de integração;
- os saldos iniciais de provisão dos colaboradores já foram cadastrados, quando aplicável (consulte o artigo Saldos de Provisão);
- as fórmulas contábeis dos eventos de provisão estão corretamente configuradas.

### 2. Jornada de Uso

[GIF animado: Imagem 3: 2. Jornada de Uso](https://ajuda.sankhya.com.br/hc/article_attachments/42439143472791)

#### 2.1 Realizar a Integração Contábil de Provisões

1. Acesse a tela **Gerenciador de Folhas** (Pessoal+ > Rotinas Folha);
2. Clique no menu **Provisão de Férias e 13º**;
3. No pop-up **Provisões de Férias e 13º Salário**, selecione **Integração Contábil Provisões**.
4. Informe o código da **Empresa** e a **Referência**;

   O sistema utiliza essas informações para localizar as provisões já calculadas na folha da referência informada.
5. Em **Considerar provisão**, marque **Férias** e/ou **13º Salário** — a contabilização de ambos pode ser feita no mesmo lote ou separadamente: essa decisão depende das regras definidas pela contabilidade da empresa, e não de uma regra fixa do sistema;
6. Informe o **Lote Contábil** (normalmente indicado pela contabilidade) e a **Data Movimento Contábi**l;
7. Em **Contabilizar por**, selecione como as provisões serão agrupadas nos lançamentos contábeis: por **Empresa**, **Funcionário**, **Departamento** ou **Centro de Resultado** (opção mais utilizada).
8. Marque as opções que devem compor o histórico contábil dos lançamentos.

   As opções disponíveis variam conforme o critério escolhido na etapa anterior:

   - **Empresa** ou **Centro de Resultado**: permite apenas **Histórico Padrão**, **Referência** e **Descrição Evento**;
   - **Funcionário**: permite todas as composições disponíveis;
   - **Departamento**: permite todas, exceto **Nome do Funcionário**.
9. Use o botão **Filtros** para restringir os dados que serão contabilizados por **Departamentos**, **Cargos**, **Vínculos** ou **Funcionários**.

   Para contabilizar apenas colaboradores específicos, selecione o filtro **Funcionários** e clique em **+**, marque os colaboradores desejados e clique em **Aplicar Filtros**.

   É possível combinar vários filtros ou não aplicar nenhum, quando a contabilização deve considerar todos os colaboradores da referência.
10. Clique em **Gerar**.

    O sistema exibirá um resumo em tela com todos os lançamentos contábeis das provisões, permitindo a conferência antes da efetivação.

    | ℹ️ **Nota**  O crédito da provisão é sempre lançado no tipo de contabilização de Provisão de Férias ou de Provisão de 13º Salário, e a baixa é sempre lançada no tipo de contabilização normal. Essa associação é fixa e não pode ser alterada nesta tela. |
    | --- |
11. Após conferir os lançamentos, clique em **Efetivar**. A integração contábil das provisões de férias e 13º salário fica concluída para a empresa e referência informadas.

    | 🚨 **Risco operacional**  A efetivação gera os lançamentos contábeis das provisões na empresa informada. Confira atentamente o resumo antes de efetivar, pois o processo tem impacto direto na contabilidade da empresa. |
    | --- |
12. Para **recalcular provisões de uma competência, respeite a ordem cronológica dos cálculos.**

    Caso existam provisões calculadas em competências posteriores à referência que será recalculada, exclua primeiro as provisões das referências futuras, seguindo a ordem inversa dos períodos.

    Após excluir as provisões posteriores, exclua a provisão da competência que precisa ser corrigida e realize novamente o cálculo.

    Essa sequência é necessária para que o sistema considere corretamente os saldos anteriores das provisões e mantenha a consistência das informações apresentadas no cálculo e nos relatórios.

    **Exemplo:**

    Se for necessário recalcular a provisão de **06/2026** e já existirem provisões calculadas para **07/2026 e 08/2026**, a exclusão deve ocorrer nesta ordem:

    1. Excluir a provisão de **08/2026**;
    2. Excluir a provisão de **07/2026**;
    3. Excluir a provisão de **06/2026**;
    4. Recalcular a provisão de **06/2026**;
    5. Calcular novamente as competências posteriores, seguindo a ordem cronológica.

#### 2.2 Conferir o relatório de provisões

[GIF animado: Imagem 4: 2.2 Conferir o relatório de provisões](https://ajuda.sankhya.com.br/hc/article_attachments/42439251574295)

Para conferência das provisões calculadas:

12. Retorne à tela principal do **Gerenciador de Folhas** e clique em **Gerar Relatório Décimo Terceiro ou Férias**;
13. Informe **Empresa** e **Referência**;
14. Selecione o tipo de **Provisão** (**Décimo Terceiro** ou **Férias**);
15. Defina também o **formato de impressão** e a **ordenação**;
16. Clique em **Confirmar** para gerar o relatório da provisão selecionada.

    | **⚠️** **Atenção**  A coluna **Bx. Provisão** do relatório de provisão de férias só é preenchida corretamente quando existe, na configuração do evento, um cálculo por fórmula associado ao tipo de contabilização Provisão de Férias. Sem essa configuração, a coluna pode ficar em branco ou apresentar valores incorretos. |
    | --- |

### 3. Pontos de Atenção

- O crédito da provisão sempre utiliza o tipo de contabilização de provisão de férias/13º; a baixa sempre utiliza o tipo de contabilização normal.
- O cálculo da provisão precisa ter sido executado com sucesso antes da integração; provisões não calculadas não aparecem na tela, mesmo sem mensagem de erro explícita.
- Divergências entre saldo inicial cadastrado e saldo apresentado no relatório costumam estar ligadas ao cadastro de Saldos de Provisão, não à integração em si.

### 4. Dicas de Usabilidade

- Utilize os filtros por Departamento, Cargo, Vínculo ou Colaborador quando a contabilização precisar seguir regras diferentes para grupos específicos, em vez de gerar tudo em um único lote.
- Sempre confira o resumo de lançamentos antes de efetivar.
- Utilize o relatório de conferência (Décimo Terceiro/Férias) após a efetivação para validar os valores.
- Em caso de relatório de provisão zerado ou com valores incorretos, verifique primeiro se o cálculo da provisão da referência foi executado.
- Realize a integração contábil das provisões somente depois de concluir a integração contábil da própria folha de pagamento, garantindo que os dois processos fiquem consistentes na contabilidade.

## Perguntas Frequentes (FAQ)

**1. Preciso calcular a provisão antes de integrar com a contabilidade?**

Sim. Se o cálculo da provisão de férias e 13º salário da referência não for executado antes, os valores não aparecem na tela de Integração Contábil Provisões.

**2. Onde encontro o botão de Integração Contábil Provisões agora?**

A partir da versão 5.111, ele está dentro do menu "Calcular Provisão em Lote", no Gerenciador de Folhas, e não mais como botão isolado.

**3. O relatório de Provisão de 13º/Férias está saindo zerado ou com erro ao gerar. O que fazer?**

Verifique se o cálculo da provisão da referência foi realizado e se os campos de valor (ex.: VLRPARCELA) estão preenchidos; pode ser necessário excluir e recalcular as provisões da referência.

**4. O saldo inicial de provisão de um funcionário está divergente. Onde corrijo?**

O saldo inicial é cadastrado na tela de Saldos de Provisão, não na tela de integração contábil.

**5. Valores variáveis (ex.: comissões, médias) entram na base de cálculo da provisão?**

Depende da configuração "Considera valores variáveis nas provisões" na Regra de Cálculo — quando marcada, o sistema usa a média dos últimos 12 meses.

**6. É obrigatório contabilizar férias e 13º salário no mesmo lote?**

Não. A tela permite selecionar as duas opções juntas ou separadamente. A definição de contabilizar em um mesmo lote ou em lotes distintos depende das regras estabelecidas pela contabilidade da empresa, não de uma exigência do sistema.

**7. Qual a diferença entre contabilizar por Centro de Resultado e por Funcionário?**

O critério define como os lançamentos contábeis são agrupados e quais opções de histórico contábil ficam disponíveis. Contabilizar por Funcionário libera todas as composições de histórico, incluindo o nome do colaborador; por Centro de Resultado ou Empresa, apenas Histórico Padrão, Referência e Descrição do Evento ficam disponíveis.

**8. É possível contabilizar as provisões de apenas alguns colaboradores?**

Sim. Utilize o botão "Filtros" e selecione o filtro "Funcionários" para restringir a contabilização a colaboradores específicos, ou combine com filtros de Departamento, Cargo ou Vínculo.

**9. Posso alterar em qual tipo de contabilização o crédito ou a baixa da provisão são lançados?**

Não. O crédito da provisão é sempre lançado no tipo de contabilização de Provisão de Férias ou de Provisão de 13º Salário, e a baixa é sempre lançada no tipo de contabilização normal. Essa associação é fixa nesta tela.
