---
id: "42424940981911"
titulo: "Relatório S-5013 (Conferência consolidada FGTS)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42424940981911-Relat%C3%B3rio-S-5013-Confer%C3%AAncia-consolidada-FGTS"
trilha: "Manual do Produto > Pessoas+ > eSocial > Totalizadores e Conferência do eSocial"
atualizado_em: "2026-10-22T16:53:14Z"
rotulos: ["br.com.sankhya.CentraleSocial", "Central do eSocial", "Relatório S-5013 – Conferência Consolidada de FGTS do eSocial", "Conferência Consolidada de Tributos", "Base de Cálculo do FGTS", "Valor de FGTS a ser Depositado", "br.com.sankhya.mgepes.rh.ConferenciaS5013"]
---

# Relatório S-5013 (Conferência consolidada FGTS)

**Módulo:** Pessoal+
**Versão Mínima:** 5.134.0
**Caminho de Acesso:** Pessoal+ > Consultas
**ID da Tela:** br.com.sankhya.mgepes.rh.ConferenciaS5013

---

### O que é a Conferência Consolidada FGTS e para que serve

A tela **S-5013 - Conferência Consolidada FGTS** compara os valores do Fundo de Garantia do Tempo de Serviço (FGTS) calculados pela Folha de Pagamento do Pessoas+ com os valores consolidados devolvidos pelo eSocial no evento S-5013 — Informações do FGTS consolidadas por contribuinte.

O eSocial gera o S-5013 após processar o fechamento dos eventos periódicos (S-1299). Esse retorno reúne as bases de cálculo e os valores de depósito do FGTS do empregador, organizados por estabelecimento, lotação tributária e tipo de valor.

Na conferência, você visualiza lado a lado:

- **Valor Apurado Sistema:** valor calculado pela Folha de Pagamento para a referência selecionada.
- **Valor Retorno eSocial:** valor consolidado devolvido pelo eSocial no evento S-5013.
- **Diferença:** resultado da subtração do Valor Retorno eSocial do Valor Apurado Sistema.

Utilize a conferência antes de gerar a guia no FGTS Digital ou de realizar uma retificação. Assim, você identifica em quais estabelecimentos, lotações e tipos de valor existem diferenças de base de cálculo ou de depósito do FGTS e pode investigar a necessidade de ajustes na Folha de Pagamento.

| ℹ️ **Nota**  a conferência apresenta valores consolidados por empregador, estabelecimento e lotação. Para conferir os valores de um colaborador específico, utilize o [Relatório S-5003 (FGTS por trabalhador)](https://ajuda.sankhya.com.br/hc/pt-br/articles/36626761293591). |
| --- |

### Antes de começar

Verifique os pré-requisitos a seguir antes de acessar a conferência.

- Acesso liberado para a tela **S-5013 - Conferência Consolidada FGTS** (Pessoal+ > Consulta) e **Central do eSocial** (Pessoal+ > Rotinas Folha).

  Essa liberação é feita na tela **Acessos** (Configurações > Controle de Acesso), pelo administrador do sistema.
- Ter o fechamento da Folha de Pagamento processado pelo eSocial.

  O evento S-1299 — Fechamento dos Eventos Periódicos da referência que será conferida deve ter sido processado com sucesso pelo eSocial.

  O S-5013 é gerado pelo eSocial como retorno do fechamento. Portanto, ele não é enviado diretamente pelo empregador.
- O campo **Empresa Matriz** deve estar preenchido corretamente no cadastro de todas as empresas do grupo:
  - a própria matriz deve apontar para o seu próprio código;
  - as filiais devem apontar para o código da matriz correspondente.

    Exemplo:

    | Empresa | Empresa Matriz |
    | --- | --- |
    | Empresa 1 (Matriz) | 1 |
    | Empresa 2 (Filial) | 1 |
    | Empresa 3 (Filial) | 1 |

    | **⚠️** **Atenção**  Empresas com o campo Empresa Matriz preenchido incorretamente podem ficar fora da consolidação. Esse campo também é utilizado por outras rotinas do Pessoas+. |
    | --- |

### Jornada de Uso

[GIF animado: Imagem 1: Jornada de Uso](https://ajuda.sankhya.com.br/hc/article_attachments/44363096425751)

#### 1. Acessar a Conferência Consolidada FGTS

1. O dashboard **S-5013 Conferência consolidada FGTS** (Pessoal+ > Consultas) pode ser acessado de duas formas:

- **Pela barra de pesquisa do Sankhya Om**;
- Pela **Central do eSocial**: clique no menu ou botão **Conferência de Tributos**, localizado no canto inferior direito da tela.

As duas opções abrem a mesma tela, com os mesmos filtros e dados.

Ao acessar, o sistema disponibiliza os filtros de **referência**, **empresa** **matriz** e **tipo de folha para apuração**.

#### 2. Informar os filtros e pesquisar

Preencha os filtros conforme a conferência que deseja realizar.

| Filtro | O que informar |
| --- | --- |
| Referência | Mês e ano da competência que será conferida. Exemplo: 06/2026. |
| Matriz | Empresa matriz do empregador. A conferência considera a matriz e todos os estabelecimentos e lotações vinculados a ela. |
| Indicativo de Apuração | Tipo de apuração da Folha de Pagamento: **1 - Mensal**, para a folha mensal da referência, ou **2 - 13º salário**, para a folha do 13º salário. |
| Mostrar somente divergências | Com essa opção ativa, o sistema oculta os estabelecimentos, as lotações e as linhas sem diferença, mantendo visíveis somente os itens divergentes.  Os três totais consolidados permanecem iguais, independentemente da aplicação desse filtro. Se não houver divergências para os filtros informados, o sistema exibirá a mensagem:  **Nenhuma divergência encontrada para os filtros atuais.** |

**Filtros disponíveis por tributo** **consolidado na Central do eSocial**

| Tributo | Lotações tributárias | Estabelecimentos | Funcionários |
| --- | --- | --- | --- |
| INSS (S-5011) | ✅ | ✅ | ❌ |
| IRRF (S-5012) | ❌ | ❌ | ❌ (retorno é só por CNPJ Matriz e Código de Receita) |
| FGTS (S-5013) | ✅ | ✅ | ❌ (aba sempre desabilitada no consolidado) |
| **⚠️** **Atenção**  A aba **Funcionários** existe na tela, mas fica **desabilitada para qualquer tributo consolidado** — o filtro por trabalhador só está disponível no relatório **analítico** (S‑5001/S‑5002/S‑5003). | | | |

Depois de preencher os filtros, clique em **Pesquisar**.

O sistema verifica se existe um fechamento S-1299 processado com sucesso pelo eSocial para a matriz e a referência informadas.

Se não houver um retorno válido, nenhum valor será apresentado e o sistema exibirá a seguinte mensagem:

**"Não encontramos um retorno do eSocial processado para essa matriz e referência. Verifique se o fechamento já foi processado ou selecione outra referência."**

Essa mensagem também pode aparecer quando o período foi reaberto pelo evento S-1298 — Reabertura dos Eventos Periódicos e, ainda não foi enviado um novo S-1299 válido.

Para resolver, acesse a **Central do eSocial** e confirme se o fechamento da referência foi transmitido e processado. Se o período tiver sido reaberto, envie novamente o fechamento e aguarde o retorno do eSocial antes de pesquisar novamente.

| ℹ️ **Nota**  A lista de matrizes dessa tela não é restringida pelo **Grupo de Decisores** parametrizado no **Painel de Configuraçõe**s. Como o FGTS é consolidado por empregador, apresentar somente parte dos estabelecimentos poderia gerar totais incorretos. |
| --- |

#### 3. Analisar os totais consolidados

Após a pesquisa, o sistema apresenta três indicadores no topo da tela:

- **Total Depósito FGTS — Sistema:** soma dos valores de depósito do FGTS calculados pela Folha de Pagamento.
- **Total Depósito FGTS — eSocial:** soma dos valores de depósito do FGTS devolvidos pelo eSocial no S-5013.
- **Diferença Total:** resultado da subtração do Total Depósito FGTS — eSocial do Total Depósito FGTS — Sistema.

Os totais consideram os depósitos de todos os estabelecimentos, lotações e tipos de valor vinculados à matriz, incluindo valores do período corrente e do período anterior.

**Como interpretar a Diferença Total**

| Resultado | Interpretação |
| --- | --- |
| Valor negativo | O eSocial apurou um depósito maior que o calculado pela Folha de Pagamento. |
| Valor positivo | A Folha de Pagamento calculou um depósito maior que o apurado pelo eSocial. |
| Valor zero | Não há divergência entre os valores totais de depósito do sistema e do eSocial. |

Para entender exatamente o que cada indicador considera, posicione o cursor sobre o ícone de informação ao lado do nome do indicador.

| ℹ️ **Nota**  Uma **Diferença Total** igual a zero não significa, necessariamente, que todos os tipos de valor estejam conciliados individualmente. O detalhamento por estabelecimento, lotação e tipo de valor permite investigar as diferenças específicas. |
| --- |

| **⚠️** **Atenção**  Diferença entre os relatórios S-5003 e S-5013   | S-5003 | S-5013 | | --- | --- | | Analítico | Consolidado | | Por trabalhador | Por empregador | | Permite comparar Sistema × eSocial | Exibe apenas valores consolidados do eSocial | | Auxilia na identificação de divergências individuais | Auxilia na conferência dos valores oficiais consolidados |   Sempre que houver necessidade de investigar diferenças entre os valores calculados na folha e os valores retornados pelo eSocial, utilize o relatório **S-5003**. |

#### 4. Consultar os dados do empregador

O bloco **Empregador** identifica o retorno do eSocial utilizado na conferência.

| Campo | O que apresenta |
| --- | --- |
| Empresa | Nome da empresa matriz. |
| Inscrição do empregador | Número de inscrição devolvido pelo eSocial. O nome do campo varia conforme o tipo de inscrição: CNPJ, CPF, CAEPF (Cadastro de Atividade Econômica da Pessoa Física) ou CNO (Cadastro Nacional de Obras). |
| Número do recibo do fechamento | Recibo do evento S-1299 que originou o S-5013. |
| Indicativo de existência de FGTS | Informa se o eSocial encontrou dados de FGTS na referência. Exemplo: **1 - Há informações de FGTS**. |
| Data e hora do processamento | Data e hora em que o eSocial processou o S-5013. |

Essas informações ajudam a identificar o empregador e o fechamento relacionado aos valores apresentados.

#### 5. Conferir os valores por estabelecimento e lotação

A seção **Estabelecimentos** apresenta cada estabelecimento vinculado à matriz, com seu nome e número de inscrição (CNPJ, CPF, CAEPF ou CNO).

Dentro de cada estabelecimento, o sistema apresenta as lotações tributárias, identificadas por:

- Código da lotação.
- Tipo da lotação.
- Inscrição do estabelecimento ao qual a lotação pertence.

Clique na seta ao lado do estabelecimento ou da lotação para expandir ou recolher o detalhamento.

Ao expandir uma lotação, o sistema apresenta uma linha para cada tipo de valor do FGTS, separando os valores do **período corrente** e do **período anterior**.

Em cada linha, são comparados os valores do sistema e do eSocial para:

- Base de cálculo do FGTS.
- Valor de depósito do FGTS.
- Diferença entre os valores.

**Como o sistema calcula o Valor Apurado Sistema**

O cálculo depende da base de cálculo, da categoria eSocial e do tipo de valor do FGTS.

**Base de cálculo do FGTS:** corresponde à soma dos eventos da Folha de Pagamento com incidência de FGTS, conforme a categoria eSocial do colaborador.

**Valor de depósito do FGTS:** é calculado com base na base de cálculo e na alíquota aplicável ao tipo de valor:

- **8%:** categorias gerais.
- **2%:** aprendiz e Contrato Verde e Amarelo, nas categorias 103, 107 e 108.
- **3,2% adicional:** empregado doméstico, categoria 104.

**Trabalhador avulso não portuário:** para o tipo de valor 19, o cálculo considera a contratação do trabalhador avulso não portuário informada no evento S-1270, com alíquota de 8%. Nesse caso, o valor não é calculado a partir dos eventos da Folha de Pagamento.

O sistema considera somente colaboradores das categorias para as quais o eSocial calcula o FGTS. Colaboradores de outras categorias não são apresentados na conferência.

**Como o sistema identifica uma divergência**

A diferença de cada linha é calculada da seguinte forma:

**Diferença = Valor Apurado Sistema − Valor Retorno eSocial**

O resultado é truncado em duas casas decimais, sem arredondamento.

A linha é sinalizada como divergente quando o valor absoluto da diferença é **maior que R$ 0,01**.

Considere também estas situações:

- **Somente um dos lados possui valor:** o lado sem valor é apresentado como 0,00, e a diferença é calculada normalmente.
- **Nenhum dos lados possui valor:** a linha não é apresentada, pois não há valores a conferir.

**Indicador de incidência do FGTS**

Cada linha apresenta o indicador de incidência devolvido pelo eSocial.

| Código | Significado |
| --- | --- |
| 1 - Normal | O valor entra no cálculo do depósito do FGTS. |
| 9 - Incidência suspensa por decisão judicial | O valor permanece visível na base de cálculo, mas não é considerado pelo eSocial no depósito de FGTS a recolher. |

Para o tipo de valor 19, referente ao trabalhador avulso não portuário, o indicador é sempre apresentado como **1 - Normal**.

**Informações do período anterior**

No bloco de período anterior, o sistema apresenta o motivo informado ao eSocial para a apuração de valores de competências anteriores.

| Código | Motivo |
| --- | --- |
| E | Conversão de licença saúde em acidente de trabalho. |
| H | Declaração de base de cálculo do FGTS anterior ao início do FGTS Digital. |
| I | Sentença judicial, exceto reclamatória trabalhista. |

Se o eSocial devolver um código diferente desses, o sistema apresenta o código recebido com a indicação de descrição não confirmada.

| ℹ️ **Nota**  Os campos **Notificação FGTS** e **Natureza da Rubrica** existem somente no período corrente. Eles são exibidos conforme o retorno do eSocial, inclusive quando estão vazios, até que exista regulamentação específica sobre seu preenchimento. |
| --- |

**Dica: o que verificar quando houver divergência**

Uma das possíveis causas de divergência é a parametrização do Registro Fiscal utilizado pelo evento 995 (FGTS Normal).

Verifique os seguintes itens:

1. O parâmetro **FPREGFISCAL**, que define se o Registro Fiscal é obtido pela Empresa ou pelo Departamento.
2. O Registro Fiscal correspondente.
3. O Percentual de FGTS informado nesse Registro Fiscal.

Depois de realizar qualquer ajuste, recalcule a Folha de Pagamento da referência.

#### 6. Exportar a conferência em PDF ou Excel

Para exportar os dados, clique em **Download** e selecione o formato desejado.

O arquivo considera os mesmos dados exibidos na tela no momento da exportação, inclusive a opção **Mostrar somente divergências**.

| Formato | Conteúdo |
| --- | --- |
| PDF | Apresenta o cabeçalho com o nome do relatório, empregador, inscrição, referência, indicativo de apuração, número do recibo do fechamento e data e hora de geração. Também inclui os três totais e o detalhamento por estabelecimento e lotação, sempre expandido e com o período anterior. Quando o filtro de divergências está ativo, essa condição é informada no cabeçalho. |
| Excel | Contém a aba **Resumo**, com os totais e os dados de identificação, e a aba **Detalhamento**, com uma linha por estabelecimento, lotação, tipo de valor e origem (Sistema, eSocial e Diferença). Os valores são exportados como números, permitindo utilizar somas e fórmulas no Excel. |

**Tipos de valor do FGTS exibidos na conferência**

O eSocial separa os valores do FGTS conforme a natureza da remuneração, a categoria do colaborador e o período de apuração.

A tabela apresenta os grupos de tipos de valor que podem aparecer na conferência.

| Tipos de valor | Grupo | Categorias | Alíquota |
| --- | --- | --- | --- |
| 11 a 14 | Mensal e 13º salário — período corrente e anterior | Categorias gerais | 8% |
| 15 a 18 | Mensal e 13º salário de aprendiz e Contrato Verde e Amarelo | 103, 107 e 108 | 2% |
| 19 | Trabalhador avulso não portuário | 202 | 8% |
| 21 a 26 | Rescisão: mês da rescisão, 13º salário e aviso prévio indenizado | Categorias gerais | 8% |
| 27 a 32 | Rescisão de aprendiz e Contrato Verde e Amarelo | 103, 107 e 108 | 2% |
| 41 a 50 | Indenização compensatória do empregado doméstico — mensal, 13º salário e rescisão | 104 | 3,2% adicional |

📚 Para saber mais, consulte o [**Manual de Orientação do FGTS Digital**](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/manual-e-documentacao-tecnica/manual-de-orientacao-do-fgts-digital-versao-1-70-12-06-2026.pdf), disponível no portal gov.br.

### Pontos de atenção

- **Diferenças que não indicam necessariamente erro de cálculo**

  O FGTS Digital não aceita valores negativos em um tipo de valor e não compensa valores entre tipos de valor diferentes. A compensação ocorre somente dentro do mesmo tipo de valor.

  Por isso, podem existir diferenças legítimas entre o sistema e o eSocial, mesmo quando a Folha de Pagamento está correta.

  Valores com incidência suspensa por decisão judicial também não entram no depósito do FGTS a recolher.
- **Multa rescisória do FGTS**

  A multa rescisória não é apresentada na conferência, pois é calculada diretamente pelo FGTS Digital, no módulo Remunerações para Fins Rescisórios, e não faz parte do evento S-5013.
- **A conferência não altera os dados do eSocial**

  A tela é destinada à consulta. Ela não altera, reenvia nem retifica eventos do eSocial.

  Quando houver necessidade de ajuste, corrija os dados na Folha de Pagamento e, se necessário, transmita novamente os eventos ao eSocial.
- **Os valores não são individualizados por colaborador**

  A conferência não apresenta CPF, matrícula ou salário dos colaboradores. Os valores são consolidados por estabelecimento e lotação, e os arquivos exportados seguem a mesma restrição de acesso da tela.

  Para investigar a diferença de um colaborador específico, utilize o Relatório S-5003.
- **Risco operacional: gerar a guia sem tratar as divergências**

  **Risco:** gerar a guia no FGTS Digital sem analisar as diferenças apontadas na conferência.

  **Impacto:** recolhimento a menor, sujeito a multa e juros, ou recolhimento a maior, que pode gerar crédito não aproveitado.

  **Como evitar:** confira a Diferença Total antes de gerar a guia, analise as linhas divergentes e, se necessário, corrija a Folha de Pagamento e retransmita os eventos ao eSocial.

### Perguntas frequentes

**1. A Conferência Consolidada FGTS compara os valores do sistema com os do eSocial?**

Sim. A tela apresenta o Valor Apurado Sistema, o Valor Retorno eSocial e a Diferença por estabelecimento, lotação e tipo de valor, além dos totais consolidados da matriz.

**2. Quando devo usar o S-5013 e quando devo usar o S-5003?**

Utilize a **Conferência Consolidada FGTS (S-5013)** para conferir os valores do FGTS do empregador por estabelecimento e lotação.

Utilize o **Relatório S-5003** quando precisar investigar os valores de um colaborador específico.

**3. Como confiro o FGTS do 13º salário?**

No filtro **Indicativo de Apuração**, selecione **2 - 13º salário**, informe a Referência e a Matriz e clique em **Pesquisar**. Para conferir a Folha de Pagamento mensal, selecione **1 - Mensal**.

**4. Por que aparece a mensagem de que não foi encontrado um retorno do eSocial?**

Isso ocorre quando o fechamento S-1299 da referência ainda não foi processado pelo eSocial ou quando o período foi reaberto por um S-1298 sem que um novo fechamento válido tenha sido processado.

Confira o fechamento na Central do eSocial, transmita-o novamente se necessário e aguarde o retorno antes de pesquisar.

**5. Por que não encontro a Conferência Consolidada FGTS no menu?**

O menu e o atalho da Central do eSocial são exibidos somente para usuários do grupo Departamento Pessoal (DP). Solicite ao administrador do sistema a inclusão do seu usuário nesse grupo.

**6. Por que alguns estabelecimentos não aparecem na conferência?**

Verifique o campo **Empresa Matriz** no cadastro das empresas. A matriz deve apontar para o próprio código, e cada filial deve apontar para o código da matriz correspondente.

**7. Por que uma linha apresenta 0,00 no Sistema ou no eSocial?**

Isso indica que apenas um dos lados possui valor para aquele tipo de valor. Por exemplo, o eSocial pode ter devolvido um valor enquanto a Folha de Pagamento não possui eventos com incidência de FGTS para a mesma lotação e o mesmo tipo de valor.

**8. Por que existe diferença mesmo quando a Folha de Pagamento está correta?**

O FGTS Digital não aceita valores negativos nem compensa valores entre tipos de valor diferentes. Além disso, valores com incidência suspensa por decisão judicial não entram no depósito a recolher. Essas situações podem gerar diferenças legítimas.

**9. A multa rescisória do FGTS aparece na conferência?**

Não. A multa rescisória é calculada diretamente no FGTS Digital e não faz parte do retorno do evento S-5013.
