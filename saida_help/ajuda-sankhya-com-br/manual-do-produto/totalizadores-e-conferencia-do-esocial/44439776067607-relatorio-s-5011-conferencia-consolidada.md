---
id: "44439776067607"
titulo: "Relatório S-5011 (Conferência consolidada das contribuições sociais)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44439776067607-Relat%C3%B3rio-S-5011-Confer%C3%AAncia-consolidada-das-contribui%C3%A7%C3%B5es-sociais"
trilha: "Manual do Produto > Pessoas+ > eSocial > Totalizadores e Conferência do eSocial"
atualizado_em: "2026-10-22T16:56:03Z"
rotulos: ["S-5011 - Conferência Consolidada das Contribuições Sociais", "Valor Sistema", "Valor eSocial", "S-1260", "br.com.sankhya.mgepes.rh.DashEsocial5011", "Empresa Matriz", "Comercialização Rural"]
---

# Relatório S-5011 (Conferência consolidada das contribuições sociais)

**Módulo:** Pessoal+
**Versão Mínima:** 5.135.0
**Caminho de Acesso:** Pessoal+ > Consultas
**ID da Tela:** br.com.sankhya.mgepes.rh.DashEsocial5011

---

### O que é a Conferência Consolidada das Contribuições Sociais e para que serve

A tela **S-5011 - Conferência Consolidada das Contribuições Sociais** compara os valores de contribuição previdenciária e de PIS/PASEP calculados pela Folha de Pagamento do Pessoas+ com os valores consolidados devolvidos pelo eSocial no evento S-5011 — Informações das contribuições sociais consolidadas por contribuinte.

O eSocial gera o S-5011 após processar o fechamento dos eventos periódicos (S-1299). Esse retorno reúne as bases de cálculo, as contribuições do segurado, as deduções e as contribuições devidas pelo empregador, organizadas por estabelecimento, lotação tributária, categoria e código de receita.

Na conferência, você visualiza lado a lado:

- **Valor Sistema:** valor apurado pela Folha de Pagamento para a referência selecionada, com base nos cadastros do Pessoas+.
- **Valor eSocial:** valor consolidado devolvido pelo eSocial no evento S-5011.
- **Diferença:** resultado da comparação entre o Valor Sistema e o Valor eSocial.

Utilize a conferência antes de gerar a DCTFWeb ou de realizar uma retificação. Assim, você identifica em quais estabelecimentos, lotações, categorias e códigos de receita existem diferenças e pode investigar a necessidade de ajustes na Folha de Pagamento.

| ℹ️ **Nota**  A conferência apresenta valores consolidados por empregador, estabelecimento e lotação. Para conferir os valores de um colaborador específico, utilize o [Relatório S-5001 (Contribuições sociais por trabalhador)](https://ajuda.sankhya.com.br/hc/pt-br/articles/36419467638551). |
| --- |

### Antes de começar

Verifique os pré-requisitos a seguir antes de acessar a conferência.

- Acesso liberado para a tela **S-5011 - Conferência Consolidada das Contribuições Sociais** (Pessoal+ > Consultas) e para a **Central do eSocial** (Pessoal+ > Rotinas Folha).

  O acesso é concedido automaticamente aos usuários do Departamento Pessoal (DP) que já têm acesso às telas **Funcionários**, **Gerenciador da Folha** ou **Central do eSocial**. Para os demais usuários, a liberação é feita na tela **Acessos** (Configurações > Controle de Acesso), pelo administrador do sistema.
- O usuário deve pertencer ao Departamento Pessoal (DP).

  A conferência apresenta valores de contribuição de toda a empresa e, por isso, é restrita aos usuários do DP/RH.
- Ter o fechamento da Folha de Pagamento processado pelo eSocial.

  O evento S-1299 — Fechamento dos Eventos Periódicos da referência que será conferida deve ter sido processado com sucesso pelo eSocial.

  O S-5011 é gerado pelo eSocial como retorno do fechamento. Portanto, ele não é enviado diretamente pelo empregador.

  Se o período for reaberto e fechado novamente, o eSocial gera um novo S-5011, que substitui o anterior. A conferência sempre considera o retorno do fechamento mais recente.
- O campo **Empresa Matriz** deve estar preenchido corretamente no cadastro de todas as empresas do grupo:
  - a própria matriz deve apontar para o seu próprio código;
  - as filiais devem apontar para o código da matriz correspondente.

    Exemplo:

    | Empresa | Empresa Matriz |
    | --- | --- |
    | Empresa 1 (Matriz) | 1 |
    | Empresa 2 (Filial) | 1 |
    | Empresa 3 (Filial) | 1 |
- As empresas que fazem parte da conferência devem estar marcadas para uso no eSocial.

  | **⚠️** **Atenção**  Empresas com o campo Empresa Matriz preenchido incorretamente, ou que não estão marcadas para uso no eSocial, podem ficar fora da consolidação. O campo Empresa Matriz também é utilizado por outras rotinas do Pessoas+. |
  | --- |

### Jornada de Uso

[GIF animado: Imagem 1: Jornada de Uso](https://ajuda.sankhya.com.br/hc/article_attachments/44441746613783)

#### 1. Acessar a Conferência Consolidada das Contribuições Sociais

A tela **S-5011 - Conferência Consolidada das Contribuições Sociais** (Pessoal+ > Consultas) pode ser acessada de duas formas:

- **Pela barra de pesquisa do Sankhya Om**;
- **Pela Central do eSocial:** clique no menu lateral ou botão **Conferência de Tributos**, localizado no canto inferior direito da tela, e selecione **S-5011 - Conferência Consolidada das Contribuições Sociais**.

As duas opções abrem a mesma tela, com os mesmos filtros e dados.

Ao acessar, o sistema exibe a mensagem **"Selecione a matriz, a referência e o indicativo de apuração e clique em Pesquisar para gerar a conferência."** até que os filtros obrigatórios sejam preenchidos.

#### 2. Informar os filtros e pesquisar

Preencha os filtros na barra superior, nesta ordem:

| Filtro | O que informar |
| --- | --- |
| Matriz (obrigatório) | Empresa matriz do empregador. A lista apresenta somente as empresas matriz marcadas para uso no eSocial. A conferência considera a matriz e as filiais vinculadas a ela. |
| Estabelecimento | Filiais que serão conferidas. O filtro é habilitado após a escolha da matriz e permite selecionar mais de um estabelecimento. Quando nenhum ou todos estão selecionados, o botão exibe **Estabelecimento: Todos** e a conferência considera o empregador inteiro. |
| Indicativo de Apuração (obrigatório) | Tipo de apuração da Folha de Pagamento: **Mensal**, para a folha mensal da referência, ou **13º Salário**, para a folha anual do 13º salário. |
| Referência (obrigatório) | Competência que será conferida. É habilitada após a escolha da matriz e do indicativo de apuração. No indicativo **Mensal**, informe o mês e o ano (exemplo: 06/2026). No indicativo **13º Salário**, informe somente o ano (exemplo: 2026). Não é possível selecionar competências futuras nem anteriores a 2018. |
| Mostrar somente divergências | Com essa opção ativa, o sistema oculta os itens sem diferença e mantém visíveis somente os itens divergentes. Os totais consolidados permanecem iguais, independentemente da aplicação desse filtro. |

Depois de preencher os filtros, clique em **Pesquisar**. O botão é habilitado somente quando Matriz, Indicativo de Apuração e Referência estão preenchidos.

Considere também estes comportamentos dos filtros:

- Ao trocar a **Matriz**, o sistema limpa o Estabelecimento e a Referência.
- Ao trocar o **Indicativo de Apuração**, a Referência é convertida automaticamente: de 06/2026 (Mensal) para 2026 (13º Salário), e de 2026 (13º Salário) para 12/2026 (Mensal).
- Qualquer alteração de Matriz, Estabelecimento, Indicativo de Apuração ou Referência limpa o resultado da tela. Clique em **Pesquisar** novamente para atualizar a conferência. A opção **Mostrar somente divergências** é aplicada imediatamente, sem nova pesquisa.

O sistema verifica se existe um fechamento S-1299 processado com sucesso pelo eSocial para a matriz, a referência e o indicativo de apuração informados.

Se não houver um retorno válido, nenhum valor será apresentado e o sistema exibirá a seguinte mensagem:

**"Não encontramos um retorno do eSocial processado para essa matriz e referência. Verifique se o fechamento já foi processado ou selecione outra referência."**

Essa mensagem também pode aparecer quando o período foi reaberto pelo evento S-1298 — Reabertura dos Eventos Periódicos e ainda não foi enviado um novo S-1299 válido.

Para resolver, acesse a **Central do eSocial** e confirme se o fechamento da referência foi transmitido e processado. Se o período tiver sido reaberto, envie novamente o fechamento e aguarde o retorno do eSocial antes de pesquisar novamente.

#### 3. Analisar os totais consolidados

Após a pesquisa, o sistema apresenta três indicadores no topo da tela:

- **Total apurado Sistema:** total das contribuições sociais calculadas pela Folha de Pagamento.
- **Total consolidado eSocial:** total das contribuições sociais devolvidas pelo eSocial no S-5011.
- **Diferença Total:** resultado da comparação entre o Total apurado Sistema e o Total consolidado eSocial.

Os dois totais seguem a mesma fórmula:

**Total = (Segurados + Patronal + Terceiros + PIS/PASEP) − (Salário-família + Salário-maternidade + Valores com exigibilidade suspensa)**

| Componente | O que considera |
| --- | --- |
| Segurados | Valor total das contribuições descontadas dos segurados. |
| Patronal | Códigos de receita da contribuição patronal e do GILRAT. |
| Terceiros | Códigos de receita de outras entidades e fundos, incluindo o Adicional SENAI. |
| PIS/PASEP | PIS/PASEP incidente sobre a folha de pagamento, a partir da referência 01/2025. |
| Salário-família e Salário-maternidade | Deduções informadas no bloco **Deduções**. |
| Valores com exigibilidade suspensa | Linhas **- Suspenso** dos códigos de receita patronais e de terceiros. |

Os valores da aba **Comercialização Rural** não fazem parte desses totais, pois têm um totalizador próprio.

A **Diferença Total** é apresentada em vermelho quando há divergência e em verde quando os valores conferem.

Para entender exatamente o que cada indicador considera, posicione o cursor sobre o ícone de informação ao lado do nome do indicador.

| ℹ️ **Nota**  Uma **Diferença Total** igual a zero não significa, necessariamente, que todos os códigos de receita estejam conciliados individualmente. O detalhamento por estabelecimento, lotação, categoria e código de receita permite investigar as diferenças específicas. |
| --- |

#### 4. Consultar os dados do empregador e as informações complementares

O bloco **Empregador** identifica o retorno do eSocial utilizado na conferência.

| Campo | O que apresenta |
| --- | --- |
| Empresa | Razão social da empresa matriz. |
| CNPJ ou CPF | Número de inscrição do empregador. O nome do campo varia conforme o tipo de inscrição. |
| Número do recibo do fechamento | Recibo do evento S-1299 que originou o S-5011. |
| Indicativo de existência de valores | Informa se o eSocial apurou contribuições na referência: **1 - Há informações com apuração de contribuições sociais**, **2 - Há movimento, mas sem apuração de contribuições sociais** ou **3 - Não há movimento no período**. |
| Data e hora do processamento | Data e hora em que o eSocial processou o S-5011. |

Quando o indicativo de existência de valores é **2** ou **3**, o Valor eSocial e a Diferença são exibidos como "-" e não são sinalizadas divergências. O Valor Sistema continua sendo apresentado.

O bloco **Informações Complementares** apresenta os dados do empregador considerados pelo eSocial na apuração, conforme o retorno do S-5011:

- Classificação tributária.
- Indicativo de Cooperativa.
- Indicativo de Substituição da Contribuição Previdenciária Patronal.
- Indicativo de Construtora.
- Indicador de tributação sobre a folha de pagamento para o PIS/PASEP.
- Percentual de contribuição social do estabelecimento.
- Percentual não substituído pela CPRB.
- Fator Mês e Fator 13º, exibidos somente para empresas do Simples Nacional com tributação parcialmente substituída (classificação tributária 03).

#### 5. Conferir a contribuição do segurado e as deduções

O bloco **Contribuição do Segurado** compara:

- **Valor total calculado relativo às contribuições do segurado:** contribuição que deveria ser descontada dos colaboradores, conforme a apuração do eSocial.
- **Valor total das contribuições descontadas do segurado:** contribuição efetivamente descontada na Folha de Pagamento.

O bloco **Deduções** compara:

- **Valor total do salário família.**
- **Valor total do salário maternidade.**

Cada item apresenta o Valor Sistema, o Valor eSocial e a Diferença.

| ℹ️ **Nota**  O bloco **Contribuição do Segurado** sempre considera o empregador inteiro, mesmo quando o filtro **Estabelecimento** está aplicado. |
| --- |

**Como o sistema calcula a contribuição do segurado**

O valor apresentado é o total do empregador. Para chegar a esse total, a contribuição é calculada para cada colaborador e, em seguida, os valores são somados:

- **Empregados:** aplicação da tabela progressiva do INSS sobre a base, limitada ao teto.
- **Contribuintes individuais (categorias 7xx):** alíquota de 11%. Em situações específicas previstas pelo eSocial, como cooperados (categoria 731) e contribuintes de entidades com classificação tributária 04, 70 ou 80, a alíquota é de 20%.
- **Colaboradores com múltiplos vínculos:** quando há remuneração em outras empresas, a base é limitada ao saldo do teto e a tabela progressiva continua a partir da faixa em que a outra empresa parou. No 13º salário, é considerada somente a remuneração de outras empresas lançada para o 13º.
- **SEST/SENAT:** é somado à contribuição do segurado somente para transportadores autônomos (categorias 711, 712 e 734) contratados por empregador com CNPJ.

Em algumas situações, o eSocial considera o valor calculado igual ao valor descontado, como em processos judiciais e em valores de períodos anteriores. A conferência segue a mesma regra.

#### 6. Conferir os valores por estabelecimento e lotação

A seção **Estabelecimentos** apresenta cada estabelecimento vinculado à matriz que possui retorno do eSocial ou Folha de Pagamento calculada na referência. O primeiro estabelecimento é exibido expandido.

Clique na seta ao lado do estabelecimento, da lotação ou da categoria para expandir ou recolher o detalhamento.

| Nível | O que apresenta |
| --- | --- |
| Estabelecimento | Nome, inscrição (CNPJ, CPF, CAEPF ou CNO), CNAE preponderante, Alíquota RAT, FAP, Alíquota RAT ajustada e, quando houver, CNPJ Responsável. Esses dados são exibidos conforme o retorno do eSocial. |
| Lotação | Código da lotação tributária, FPAS, Código de Terceiros e Código de Terceiros com Recolhimento Suspenso. Para lotações de operador portuário, também são apresentados o CNPJ, o FAP e a Alíquota RAT ajustada do Operador Portuário. |
| Categoria | Categoria eSocial e código de incidência, com a comparação dos valores de bases, contribuições do segurado e deduções. |

No nível de **Categoria**, podem ser apresentados os seguintes itens:

- Segurado empregado/avulso.
- Aposentadoria especial - 15, 20 e 25 anos.
- Suspensão por decisão judicial.
- Suspensão de aposentadoria especial - 15, 20 e 25 anos.
- SEST e SENAT - valor descontado e valor calculado.
- Salário Família.
- Salário Maternidade.

Para empresas com desoneração da folha, também é apresentado o grupo **13º salário - Empresas desoneradas**, com as bases e suspensões referentes ao 13º salário.

Itens sem valor no sistema e no eSocial não são apresentados. Categorias e lotações sem itens também ficam ocultas.

#### 7. Analisar as abas de bases e contribuições

Na parte inferior da tela, as abas apresentam a comparação em grade, com as colunas **Valor sistema**, **Valor eSocial** e **Diferença** e, no rodapé, os totais.

| Aba | O que apresenta |
| --- | --- |
| Bases de Cálculo | Base de cálculo previdenciária normal, bases de aposentadoria especial (15, 20 e 25 anos), bases suspensas por decisão judicial, base de cálculo do PIS/PASEP e base suspensa do PIS/PASEP. |
| Empresa Desonerada | Bases de cálculo previdenciária do 13º salário das empresas com desoneração da folha. A aba é exibida somente quando a matriz é desonerada e a referência está entre 01/2025 e 12/2027. |
| Contribuições Sociais por CR | Contribuições por código de receita, no formato "código - descrição". Quando o eSocial informa valor com exigibilidade suspensa, é exibida uma linha adicional com o sufixo **- Suspenso**. |
| Comercialização Rural | Comercialização da produção rural do produtor rural pessoa física ou do segurado especial. Veja os detalhes a seguir. |

As bases do PIS/PASEP são apresentadas como **Não aplicável** quando a referência é anterior a 01/2025, quando o empregador não tributa o PIS/PASEP sobre a folha de pagamento ou quando a matriz não é inscrita por CNPJ.

**Aba Comercialização Rural**

A aba **Comercialização Rural** confere as informações da comercialização da produção rural, enviadas ao eSocial pelo evento **S-1260**. Ela é exibida somente quando:

- a empresa matriz está classificada como **produtor rural pessoa física** (classificação tributária 21) ou **segurado especial** (classificação tributária 22);
- o indicativo de apuração é **Mensal**, pois a comercialização não é apurada no 13º salário;
- existem notas de comercialização na referência ou valores de comercialização no retorno do S-5011.

Para os demais empregadores, a aba não é exibida.

Os itens são apresentados para cada indicativo de comercialização:

| Item | O que compara |
| --- | --- |
| Indicativo de comercialização | Tipo de venda informado nas notas e no retorno do eSocial. A coluna Diferença exibe **Confere** ou **Diverge**. |
| Valor da base de cálculo da comercialização da produção rural | Soma do valor bruto das notas de comercialização da produção rural. |
| Valor da contribuição previdenciária com exigibilidade suspensa | Contribuição previdenciária (FUNRURAL) da nota × percentual de suspensão do processo judicial vinculado. Código de receita 1654-01 para produtor rural pessoa física ou 1145-01 para segurado especial. |
| Valor da contribuição para GILRAT com exigibilidade suspensa | GILRAT da nota × percentual de suspensão do processo judicial vinculado. Código de receita 1653-01 ou 1647-01. |
| Valor da contribuição para o SENAR com exigibilidade suspensa | SENAR da nota × percentual de suspensão do processo judicial vinculado. Código de receita 1213-05 ou 1213-01. |

Ao final da grade, o totalizador da aba soma somente as três contribuições com exigibilidade suspensa. O indicativo e a base de cálculo não entram nesse total.

Considere também estas regras:

- **Notas consideradas:** notas de venda confirmadas, com NF-e autorizada quando aplicável, de produtos marcados como comercialização agrícola e com o indicativo de comercialização informado no cadastro do parceiro.
- **Sem processo judicial vinculado ou sem percentual de suspensão:** as contribuições suspensas ficam com Valor Sistema igual a zero.
- **Contribuições comparadas conforme o tipo de venda:** a contribuição previdenciária e o GILRAT são comparados somente na venda direta no varejo, a consumidor final ou a outro produtor rural pessoa física. O SENAR também é comparado na venda isenta (Lei 13.606/2018) e na venda ao mercado externo. Nos demais tipos de venda, os itens são exibidos com 0,00.
- **Produtor rural optante pela contribuição sobre a folha:** somente o SENAR é comparado.

**Códigos de receita exibidos na conferência**

| Grupo | Códigos de receita |
| --- | --- |
| Contribuição patronal | 1138-01 a 1138-08 |
| GILRAT | 1141-01, 1141-02, 1141-05, 1646-01, 1646-02 e 1646-09 |
| Terceiros (outras entidades e fundos) | 1170-01, 1176-01, 1176-02, 1181-01, 1184-01, 1191-01, 1196-01, 1200-01, 1200-02, 1205-01, 1209-01, 1218-01, 1218-02, 1221-01, 1221-02 e 1225-01 |
| Adicional SENAI | 1664-01 |
| Contribuição do segurado | 1082-01 a 1082-05, 1082-07, 1099-01 e 1099-02 |

**Como o sistema calcula o Valor Sistema**

O Valor Sistema é calculado a partir da Folha de Pagamento e dos cadastros do Pessoas+, e não a partir do retorno do eSocial. Dessa forma, a conferência identifica diferenças de parametrização.

- **Bases de cálculo:** soma dos eventos da Folha de Pagamento conforme o código de incidência da contribuição previdenciária (CP) do evento, a categoria eSocial e o grau de exposição a agentes nocivos do colaborador. Para o PIS/PASEP, é considerado o código de incidência do PIS/PASEP enviado no evento S-1010.
- **Contribuição patronal:** base × percentual patronal informado no Registro Fiscal. Algumas alíquotas são fixas: 2,5% de adicional para instituições financeiras, 3% para MEI (1138-07) e 8% para empregador doméstico (1138-08).
- **GILRAT:** base × alíquota RAT × FAP do estabelecimento. O adicional para aposentadoria especial considera o grau de exposição do colaborador.
- **Terceiros:** alíquotas conforme o FPAS e o código de terceiros da lotação tributária.
- **SEST/SENAT do transportador autônomo:** 20% do valor bruto do serviço, para as categorias 711, 712 e 734.
- **Adicional SENAI (1664-01):** a partir da competência 05/2026, contribuição adicional de 0,2% sobre a base do SENAI para empresas com mais de 500 empregados. A contagem considera a empresa como um todo, e não cada filial, e inclui somente os colaboradores com remuneração na própria competência. Esse valor é apresentado em um código de receita próprio, separado da contribuição normal ao SENAI.
- **Simples Nacional com tributação parcialmente substituída:** os valores são multiplicados pelo Fator Mês ou pelo Fator 13º.

Para empresas não desoneradas, o 13º salário anual é conferido com o indicativo **13º Salário**. Na referência de dezembro, o indicativo **Mensal** não considera a folha de 13º salário, e o indicativo **13º Salário** considera somente essa folha. O 13º salário pago em rescisões permanece na apuração mensal.

**Como o sistema identifica uma divergência**

Os valores são truncados em duas casas decimais, sem arredondamento. A diferença de cada linha é calculada da seguinte forma:

**Diferença = Valor Sistema − Valor eSocial**

A linha é sinalizada como divergente quando o valor absoluto da diferença é **maior que R$ 0,01**. A diferença é exibida em valor absoluto, e a divergência é indicada pela cor: vermelho quando há divergência e verde quando os valores conferem.

Considere também estas situações:

- **Somente um dos lados possui valor:** o lado sem valor é considerado 0,00, e a diferença é calculada normalmente.
- **Nenhum dos lados possui valor:** a linha não é apresentada.

| **💡 Dica**  **O que verificar quando houver divergência**   1. O código de incidência da contribuição previdenciária e do PIS/PASEP dos eventos da Folha de Pagamento. 2. O Registro Fiscal da empresa, especialmente os percentuais patronal e de RAT. 3. O FPAS e o código de terceiros da lotação tributária. 4. A categoria eSocial e o grau de exposição a agentes nocivos dos colaboradores. 5. Os processos judiciais vinculados aos eventos, quando houver valores suspensos. |
| --- |

Depois de realizar qualquer ajuste, recalcule a Folha de Pagamento da referência e, se necessário, transmita novamente os eventos ao eSocial. Para identificar o colaborador que originou a diferença, utilize o [Relatório S-5001](https://ajuda.sankhya.com.br/hc/pt-br/articles/36419467638551).

#### 8. Exportar a conferência em PDF ou Excel

Para exportar os dados, clique em **Download** e selecione **PDF (.pdf)** ou **Excel (.xlsx)**.

O arquivo considera os filtros informados, inclusive a opção **Mostrar somente divergências**. Os totais consolidados não são afetados por esse filtro.

| Formato | Conteúdo |
| --- | --- |
| PDF | Abre em uma nova aba do navegador. Apresenta os filtros aplicados, os dados do empregador, os totais, a contribuição do segurado, as deduções, as informações complementares, o detalhamento completo por estabelecimento, lotação e categoria e as bases e contribuições por código de receita. |
| Excel | Contém as abas **Resumo**, **Estabelecimentos e Lotações**, **Bases de Cálculos**, **Contribuições por Cód. Receita** e, quando aplicáveis, **Empresa Desonerada** e **Comercialização Rural**. Os valores são exportados como números, permitindo utilizar somas e fórmulas no Excel. |

### Pontos de atenção

- **Diferenças que não indicam necessariamente erro de cálculo**

  O eSocial não considera valores negativos por trabalhador. Por isso, valores negativos são considerados como zero antes da soma, e a soma dos códigos de receita do segurado pode ser diferente do valor total descontado.

  Também podem existir pequenas diferenças de centavos. O eSocial sempre trunca os valores em duas casas decimais, sem arredondar: R$ 100,567 é considerado R$ 100,56, e nunca R$ 100,57. Quando a Folha de Pagamento arredonda em alguma etapa do cálculo, como nas faixas da tabela progressiva do INSS, o resultado final pode ficar com 1 ou 2 centavos de diferença. Nesse caso, não se trata de erro de cálculo.
- **Filiais que enviam o eSocial por outro sistema**

  O Valor Sistema considera as filiais do grupo marcadas para uso no eSocial. Se uma filial envia o eSocial por outro sistema, ou se essa marcação foi alterada após o fechamento, a conferência pode apresentar diferença para essa filial.
- **A conferência não altera os dados do eSocial**

  A tela é destinada à consulta. Ela não altera, reenvia nem retifica eventos do eSocial.

  Quando houver necessidade de ajuste, corrija os dados na Folha de Pagamento e, se necessário, transmita novamente os eventos ao eSocial.
- **Os valores não são individualizados por colaborador**

  A conferência não apresenta CPF, matrícula ou salário dos colaboradores. Os valores são consolidados por estabelecimento, lotação e categoria.

  Para investigar a diferença de um colaborador específico, utilize o Relatório S-5001.
- **Risco operacional: gerar a DCTFWeb sem tratar as divergências**

  **Risco:** transmitir a DCTFWeb sem analisar as diferenças apontadas na conferência.

  **Impacto:** recolhimento a menor, sujeito a multa e juros, ou recolhimento a maior, que pode gerar crédito a compensar.

  **Como evitar:** confira a Diferença Total antes de transmitir a DCTFWeb, analise as linhas divergentes e, se necessário, corrija a Folha de Pagamento e retransmita os eventos ao eSocial.

### Perguntas frequentes

**1. A Conferência Consolidada das Contribuições Sociais compara os valores do sistema com os do eSocial?**

Sim. A tela apresenta o Valor Sistema, o Valor eSocial e a Diferença por estabelecimento, lotação, categoria e código de receita, além dos totais consolidados da matriz.

**2. Quando devo usar o S-5011 e quando devo usar o S-5001?**

Utilize a **Conferência Consolidada das Contribuições Sociais (S-5011)** para conferir as contribuições do empregador por estabelecimento, lotação e código de receita.

Utilize o **Relatório S-5001** quando precisar investigar os valores de um colaborador específico.

**3. Como confiro as contribuições do 13º salário?**

No filtro **Indicativo de Apuração**, selecione **13º Salário**, informe o ano na Referência e a Matriz e clique em **Pesquisar**. Para conferir a Folha de Pagamento mensal, selecione **Mensal**.

**4. Por que aparece a mensagem de que não foi encontrado um retorno do eSocial?**

Isso ocorre quando o fechamento S-1299 da referência ainda não foi processado pelo eSocial ou quando o período foi reaberto por um S-1298 sem que um novo fechamento válido tenha sido processado.

Confira o fechamento na Central do eSocial, transmita-o novamente se necessário e aguarde o retorno antes de pesquisar.

**5. Por que não encontro a tela no menu ou recebo a mensagem de acesso negado?**

A conferência é restrita aos usuários do Departamento Pessoal (DP). Solicite ao administrador do sistema a inclusão do seu usuário no DP e a liberação da tela em **Acessos**.

**6. Por que alguns estabelecimentos não aparecem na conferência?**

Verifique o campo **Empresa Matriz** no cadastro das empresas e se elas estão marcadas para uso no eSocial. A matriz deve apontar para o próprio código, e cada filial deve apontar para o código da matriz correspondente.

Estabelecimentos sem Folha de Pagamento calculada e sem retorno do eSocial na referência também não são apresentados.

**7. Por que a base do PIS/PASEP aparece como "Não aplicável"?**

A base do PIS/PASEP é conferida a partir da referência 01/2025, somente para empregadores inscritos por CNPJ que tributam o PIS/PASEP sobre a folha de pagamento.

**8. Por que a aba Comercialização Rural não aparece?**

A aba é exibida somente para empresa matriz classificada como produtor rural pessoa física ou segurado especial, com o indicativo de apuração **Mensal** e com comercialização da produção rural na referência.

**9. Por que a aba Empresa Desonerada não aparece?**

A aba é exibida somente quando a matriz possui desoneração da folha e a referência está entre 01/2025 e 12/2027.

**10. Por que uma linha apresenta 0,00 no Sistema ou no eSocial?**

Isso indica que apenas um dos lados possui valor para aquele item. Por exemplo, o eSocial pode ter devolvido um valor enquanto a Folha de Pagamento não possui eventos com a incidência correspondente na mesma lotação e categoria.

**11. Por que existe diferença de poucos centavos entre o Sistema e o eSocial?**

O eSocial trunca os valores em duas casas decimais, sem arredondar. Se a Folha de Pagamento arredondar em alguma etapa do cálculo, o resultado pode ficar com 1 ou 2 centavos de diferença. A conferência tolera diferenças de até R$ 0,01 em cada linha.
