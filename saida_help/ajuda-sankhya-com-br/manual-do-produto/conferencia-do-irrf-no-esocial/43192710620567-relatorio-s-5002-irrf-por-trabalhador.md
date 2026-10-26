---
id: "43192710620567"
titulo: "Relatório S-5002 (IRRF por trabalhador)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43192710620567-Relat%C3%B3rio-S-5002-IRRF-por-trabalhador"
trilha: "Manual do Produto > Pessoas+ > Encargos e Obrigações Legais > Nova DIRF e Informe de Rendimentos > Conferência do IRRF no eSocial"
atualizado_em: "2026-10-15T15:47:18Z"
rotulos: ["ID: br.com.sankhya.mgepes.rh.DashEsocial5002", "Tipo de Valores IRRF", "Relatório S-5002 – Conferência de Imposto de Renda Retido na Fonte por Trabalhador", "Histórico da Rubrica S-1010", "S-5002 - Conferência IRRF"]
---

# Relatório S-5002 (IRRF por trabalhador)

**Módulo:** Pessoal+
**Versão Mínima:** 5.121
**Caminho de Acesso:** Pessoal+ > Consultas
**ID da Tela:** br.com.sankhya.mgepes.rh.DashEsocial5002

---

### Sumário

[Descrição e Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/43192710620567-Relat%C3%B3rio-S-5002-IRRF-por-trabalhador#h_01M1HJ96GAJW14H8P4FV1VJ7KC)
  [1. Descrição da Funcionalidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/43192710620567-Relat%C3%B3rio-S-5002-IRRF-por-trabalhador#h_01M1HJ96GAWPDB1CQT8850SWS3)
  [2. Pré-requisitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/43192710620567-Relat%C3%B3rio-S-5002-IRRF-por-trabalhador#h_01M1HJ96GV4ZMJFG850047VE8J)
  [3. Jornada de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/43192710620567-Relat%C3%B3rio-S-5002-IRRF-por-trabalhador#h_01M1HJ96H4XV21XZXKJ49FJ5MH)
  [4. Pontos de Atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/43192710620567-Relat%C3%B3rio-S-5002-IRRF-por-trabalhador#h_01M1HJ96PVYK5H4B6J19EB4TXT)
  [5. Dicas de Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/43192710620567-Relat%C3%B3rio-S-5002-IRRF-por-trabalhador#h_01M1HJ96Q1J0888J1221P78QJJ)
[Perguntas Frequentes (FAQ)](https://ajuda.sankhya.com.br/hc/pt-br/articles/43192710620567-Relat%C3%B3rio-S-5002-IRRF-por-trabalhador#h_01M1HJ96Q8BRCNMNB7F0R0XY79)
[Artigos Relacionados](https://ajuda.sankhya.com.br/hc/pt-br/articles/43192710620567-Relat%C3%B3rio-S-5002-IRRF-por-trabalhador#h_01M1HJ96QJQ3HVHQS15CSV73EE)

---

## Descrição e Usabilidade

[Vídeo: tutorial do artigo](https://www.loom.com/embed/319818c64bfa4429904b3d9fdd0ea0ae)

### 1. Descrição da Funcionalidade

O **Relatório S-5002 – Conferência de Imposto de Renda Retido na Fonte por Trabalhador** permite comparar os valores de IRRF calculados pelo Pessoal+ com os valores retornados pelo eSocial no evento **S-5002 – Imposto de Renda Retido na Fonte por Trabalhador**.

A conferência é realizada por **Tipo de Valores IRRF**, permitindo identificar rapidamente diferenças entre:

- **Valor Sistema:** calculado a partir das informações da folha de pagamento;
- **Valor eSocial:** retornado pelo evento S-5002;
- **Diferença:** resultado da comparação entre os dois valores.

Quando houver diferença, o relatório permite aprofundar a análise até as rubricas que compõem o valor do sistema e os valores retornados pelo eSocial.

O detalhamento também permite consultar o **Histórico da Rubrica S-1010**, ajudando a verificar a incidência de IRRF considerada para a rubrica na respectiva vigência.

Além disso, a tela de **Informações Complementares** reúne informações relacionadas a:

- Dedução de dependentes e pensão alimentícia;
- Previdência complementar;
- Processos;
- Plano de saúde e reembolso médico.

| **⚠️** **Atenção**  Os os dados do relatório dependem do retorno do eSocial por meio do evento **S-5002**, gerado após o envio das informações de pagamento no **S-1210**. Portanto, apenas calcular a folha não é suficiente para que os valores sejam apresentados no relatório. |
| --- |

O relatório utiliza um processo de consolidação executado em segundo plano para reunir informações provenientes de:

- Folha de pagamento, utilizada para composição do **Valor Sistema**;
- Retorno do eSocial, utilizado para composição do **Valor eSocial**.

Quando necessário, a consolidação pode ser reprocessada para atualizar os dados apresentados no relatório.

### 2. Pré-requisitos

#### Permissões de acesso

Para utilizar o dashboard S-5002, é necessário:

- Acesso liberado para a tela **S-5002 - Conferência IRRF**. Essa liberação é feita na tela **Acessos** (Configurações > Controle de Acesso), pelo administrador do sistema.

  Para usuários DP que já possuem acesso às telas de **Configuração Funcionários**, **Gerenciador de Folhas** e **Central do eSocial**, o acesso ao relatório é liberado automaticamente conforme as regras de permissão do sistema.

#### Condições para consulta

Antes da consulta, é necessário que:

- A folha de pagamento esteja calculada;
- Todas as empresas dos trabalhadores consultados, inclusive as filiais, tenham a **Classificação Tributária** preenchida na tela **Empresas** (Configurações > Cadastros), aba **Informações Fiscais**;
- O evento **S-1210 – Pagamentos de Rendimentos do Trabalho** tenha sido enviado ao eSocial;
- O eSocial tenha retornado o evento **S-5002**;
- O processamento das informações pelo eSocial esteja concluído.

| **⚠️** **Atenção**  Sem o retorno do S-5002, não haverá dados do eSocial para comparação. |
| --- |

### 3. Jornada de Uso

**3.1. Acessar o relatório**

O dashboard **S-5002 - Conferência de Imposto de Renda Retido na Fonte por Trabalhador** (Pessoal+ > Consultas) pode ser acessado de duas formas:

1. Pela barra de pesquisa do Sankhya Om;

   ![Imagem 1: Pela barra de pesquisa do Sankhya Om;](https://ajuda.sankhya.com.br/hc/article_attachments/43194082159383)
2. Pela **Central do eSocial** (Pessoal+ > Rotinas Folha), clicando no menu **Conferência de Tributos** ou no botão de **mesmo nome**, localizado no canto inferior direito da tela.

   [GIF animado: Imagem 2: Pela Central do eSocial (Pessoal+ > Rotinas Folha), clicando no menu Conferência de Tributos ou no botão de mesmo nome…](https://ajuda.sankhya.com.br/hc/article_attachments/43194082165527)

**3.2. Preencher os filtros**

Antes da consulta, informe os filtros desejados.

| Campo | Obrigatório | Funcionalidade |
| --- | --- | --- |
| **Empresa Matriz** | Sim | Define a empresa matriz utilizada como referência para a consulta. O eSocial retorna os dados consolidados por empregador.  **⚠️** Quando o **CPF** não for informado, o relatório apresenta os trabalhadores da empresa matriz e de suas respectivas filiais para o período selecionado. |
| **Período de Apuração** | Sim | Define o mês que será utilizado na consulta. Deve ser informado no formato MM/AAAA.  A apuração é feita **apenas por referência mensal**. |
| **CPF** | Não | Permite restringir a consulta a um trabalhador específico para realizar **consulta anual**.  Informe apenas os números do CPF.  **⚠️** O mesmo **CPF** pode aparecer em linhas separadas quando o trabalhador possuir múltiplos contratos com categorias do eSocial diferentes que resultem em códigos de receita distintos. |
| **Apenas com diferença** | Não | Quando marcada, apresenta somente os registros em que a **diferença** seja diferente de zero. |

Depois de preencher os filtros, clique em **Consultar**.

**Limpar Filtros**

O botão **Limpar Filtros** restaura os campos para o estado inicial e remove os filtros aplicados nas colunas da grade.

A lateral de filtros pode ser recolhida para ampliar a área disponível para a grade. Recolher ou expandir a lateral não limpa os filtros preenchidos.

**3.3. Consultar os dados**

Após preencher os filtros, clique em **Consultar** para carregar os dados do relatório.

Ao realizar a consulta, o sistema:

1. Carrega os dados disponíveis;
2. Verifica se existe uma consolidação em andamento para o mesmo contexto;
3. Inicia ou acompanha a consolidação das informações, quando necessário.

Esse processo garante que as informações exibidas no dashboard sejam atualizadas com os dados mais recentes da folha e do eSocial.

A consulta considera os dados da empresa matriz e suas filiais relacionadas.

**3.4. Tela principal – Resumo S-5002**

A tela principal apresenta uma grade de resumo com os tipos de valores de IRRF retornados pelo S-5002.

Cada linha corresponde a um **Tipo de Valores IRRF (**`tpInfoIR`**)** encontrado para o trabalhador e o período consultado.

| Campo | Funcionalidade |
| --- | --- |
| **Nome** | Exibe o nome do trabalhador. |
| **CPF** | Exibe o CPF do trabalhador. |
| **Nº Recibo Original** | Exibe o número do recibo do evento S-1210 relacionado ao pagamento. |
| **Código Receita** | Identifica o código de receita correspondente ao retorno do eSocial. |
| **Categoria Incidência IRRF** | Exibe a categoria do trabalhador relacionada à apuração do IRRF. |
| **Tipo Valores IRRF** | Exibe o código `tpInfoIR` retornado no S-5002. |
| **Descrição Tipo Valores IRRF** | Apresenta a descrição correspondente ao `tpInfoIR`. |
| **Valor eSocial** | Exibe o valor retornado pelo eSocial no S-5002. |
| **Valor Sistema** | Exibe o valor calculado pelo Pessoal+ para o tipo de valor de IRRF. |
| **Diferença** | Exibe a diferença entre o Valor eSocial e o Valor Sistema. Ela é calculada da seguinte forma:  **Diferença = Valor eSocial − Valor Sistema**  A apresentação visual indica o resultado da conferência:   - **Diferença = 0,00:** apresentada em **verde**; - **Diferença diferente de 0,00:** apresentada em **vermelho**.   Quando houver divergência, utilize o detalhamento para identificar a origem da diferença. |

**Tipos de Valores IRRF**

Os tipos de `tpInfoIR` são apresentados somente quando houver valor correspondente no retorno do S-5002.

Para trabalhadores com múltiplos contratos no mesmo empregador, categorias do eSocial diferentes que componham códigos de receita distintos podem ser apresentadas em linhas separadas.

**Códigos de Receita (CR) considerados**

| Código de Receita | Descrição |
| --- | --- |
| **056107** | IRRF mensal, férias e 13º salário sobre trabalho assalariado |
| **356201** | IRRF sobre Participação nos Lucros ou Resultados (PLR) |
| **188901** | Rendimentos Recebidos Acumuladamente (RRA) |
| **061001** | IRRF sobre transporte rodoviário internacional – residente no Paraguai |
| **056111** | IRRF – Segurado especial |
| **056112** | IRRF – Segurado especial – 13º salário |
| **056113** | IRRF – Segurado especial – 13º salário rescisório |
| **047301** | IRRF – Residentes no exterior |

| **⚠️** **Atenção**  Em em situações que envolvam **Rendimentos Recebidos Acumuladamente (RRA)** não são apurados pelo totalizador do evento **S-5002** na tag **vlrIndResContrato**do grupo **consolidApurMen**, pois se referem a rendimentos isentos e não possuem correlação com um Código de Receita (CR) de RRA. Por esse motivo, esses valores não são apresentados para conferência no Dashboard S-5002.  Para mais informações sobre as regras de totalização do evento S-5002, consulte o [**Manual de Orientação do eSocial (MOS)**](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-versao-s-1-3-nt-06-2026-rev-09-04-2026/index.html#r_5002_ideTrabalhador_dmDev_totApurMen). |
| --- |

**3.5. Aplicar filtros nas colunas**

As colunas da grade possuem o ícone **≡**, que permite aplicar ordenação e filtros diretamente sobre os dados apresentados.

[GIF animado: Imagem 3: As colunas da grade possuem o ícone ≡ , que permite aplicar ordenação e filtros diretamente sobre os dados apresentados.](https://ajuda.sankhya.com.br/hc/article_attachments/43216628147095)

Ao clicar no ícone são apresentadas as opções:

- Ordenar Ascendentes;
- Ordenar Descendentes;
- Filtrar;
- Agrupar;
- Fixar Coluna.

Os filtros aplicados em diferentes colunas funcionam de forma acumulativa.

Quando um filtro estiver ativo, o ícone **≡** será destacado visualmente.

O botão **Limpar Filtros** da lateral também remove os filtros aplicados diretamente nas colunas.

**3.6. Acessar o detalhamento**

O detalhamento permite analisar individualmente um **Tipo Valores IRRF**.

Existem duas formas de abrir o detalhamento:

- **Pelo numeral na coluna Tipo Valores IRRF**

  Clique uma vez no código exibido na coluna **Tipo Valores IRRF**.
- **Pela linha da grade**

  Também é possível dar **duplo clique** em qualquer área da linha, fora do badge.

Ao abrir o detalhamento, o sistema apresenta:

- **Detalhamento Valor Sistema**;
- **Detalhamento Valor eSocial**;
- **Histórico da Rubrica S-1010**, quando aplicável.

Ao retornar para a tela principal, os filtros aplicados são preservados.

**3.7. Configurar grade para exibição das colunas**

As colunas exibidas em cada painel podem ser personalizadas por meio do botão **Configurar grade**.

Ao acioná-lo:

- Clique em **Seleção de coluna**.
- Na seção **Colunas disponíveis**, selecione as colunas desejadas.
- Mova as colunas para o quadro **Colunas selecionadas**.
- Clique em **Salvar** para aplicar as alterações.

  [GIF animado: Imagem 4: Clique em Salvar para aplicar as alterações.](https://ajuda.sankhya.com.br/hc/article_attachments/43213073266967)

**3.8. Detalhamento Valor Sistema**

O painel de **Detalhamento Valor Sistema** apresenta as rubricas da folha que compõem o valor calculado para o `tpInfoIR` selecionado.

Para ver o painel completo, minimize os outros painéis.

[GIF animado: Imagem 5: Para ver o painel completo, minimize os outros painéis.](https://ajuda.sankhya.com.br/hc/article_attachments/43218096424855)

O objetivo é permitir a conferência da composição do valor **item a item**.

**Campos apresentados**

| Campo | Funcionalidade |
| --- | --- |
| **Referência Folha** | Exibe a referência da folha utilizada na composição. |
| **Dt. Pagamento** | Exibe a data de pagamento considerada para a apuração. |
| **Categoria** | Exibe a categoria eSocial do trabalhador. |
| **Tipo Folha** | Identifica o tipo da folha considerada. |
| **Evento** | Exibe o código da rubrica. |
| **Descrição** | Exibe a descrição da rubrica. |
| **Tipo Evento** | Identifica se a rubrica é Vencimento, Desconto ou Informativa. |
| **Natureza da Rubrica** | Exibe a natureza da rubrica configurada. |
| **Vlr. Evento** | Exibe o valor da rubrica considerado no cálculo. |
| **Incidência IRRF** | Exibe a incidência de IRRF utilizada para a rubrica. |
| **Base Líquido** | Indica a configuração utilizada para a base líquida. |

No topo do painel é apresentado um resumo com:

- **Tipo Valores IRRF**;
- **Descrição**;
- **Valor Sistema**.

**Tipos de folha considerados**

A composição do **Valor Sistema** pode considerar, conforme o cenário:

| Tipo de Folha | Descrição |
| --- | --- |
| **Mensal** | Folha mensal |
| **Rescisão** | Folha de rescisão |
| **Férias** | Folha de férias |
| **Férias 1** | Tipo de folha de férias |
| **Férias 2** | Tipo de folha de férias |
| **13º Salário** | Folha de décimo terceiro |
| **Adiantamento** | Adiantamento |
| **Rescisão Complementar** | Rescisão complementar |
| **Dissídio** | Dissídio |
| **PLR** | Participação nos Lucros ou Resultados |

**Vigência da incidência de IRRF**

Para composição do valor, o sistema considera a configuração da incidência de IRRF correspondente à vigência da rubrica na referência da folha.

Por isso, alterações futuras na configuração da rubrica não devem alterar a composição de uma referência anterior.

**3.9. Detalhamento Valor eSocial**

O painel **Detalhamento Valor eSocial** apresenta as informações retornadas no S-5002 que compõem o valor do `tpInfoIR` selecionado.

Seu objetivo é permitir a conferência das informações efetivamente retornadas pelo eSocial.

![Imagem 6: Seu objetivo é permitir a conferência das informações efetivamente retornadas pelo eSocial.](https://ajuda.sankhya.com.br/hc/article_attachments/43219425460887)

Para ver o painel completo, minimize os outros painéis.

**Campos apresentados**

| Campo | Funcionalidade |
| --- | --- |
| **Período** | Período relacionado à informação retornada. |
| **Evento Origem** | Evento de remuneração que originou a informação, como S-1200, S-2299 ou S-2399. |
| **Categoria** | Categoria eSocial do trabalhador. |
| **ideDmDev** | Identificador da demonstração de valores conforme apresentado no S-1210. |
| **Rubrica** | Código da rubrica informado pelo eSocial. |
| **Descrição** | Descrição da rubrica. |
| **Tipo da Rubrica** | Tipo da rubrica retornado pelo eSocial. |
| **Natureza da Rubrica** | Natureza da rubrica. |
| **Vlr. Rubrica** | Valor retornado para a rubrica. |
| **Incidência IRRF** | Incidência de IRRF relacionada à informação. |
| **Nº Recibo da Remuneração** | Recibo do evento de remuneração mais recente relacionado à informação. |

O campo **Tipo da Rubrica** apresenta as seguintes descrições:

| Código | Descrição |
| --- | --- |
| **1** | Vencimento |
| **2** | Desconto |
| **3** | Informativa |
| **4** | Informativa dedutora |

Cada linha representa uma rubrica associada a um `ideDmDev` do S-1210.

**Dedução de dependentes**

Para tipos de `tpInfoIR` relacionados à **Dedução de Dependentes** de remuneração mensal, 13º salário ou férias, o detalhamento apresenta também:

| Campo | Funcionalidade |
| --- | --- |
| **Dependente** | Nome do dependente relacionado ao valor. |
| **CPF do Dependente** | CPF do dependente. |
| **Tipo de Dependência** | Tipo de dependência cadastrado. |
| **Valor da Dedução** | Valor da dedução informado no retorno do eSocial. |
| **Nº do Recibo** | Número do recibo correspondente. |

Os dados do card são obtidos a partir do retorno mais recente do S-5002 disponível para o período consultado.

**3.10. Histórico da Rubrica S-1010**

O painel **Histórico da Rubrica S-1010** permite consultar as configurações da rubrica utilizadas para a conferência do valor.

Para ver o painel completo, minimize os outros painéis.

![Imagem 7: Para ver o painel completo, minimize os outros painéis.](https://ajuda.sankhya.com.br/hc/article_attachments/43218218122519)

O histórico ajuda a identificar qual incidência de IRRF estava configurada para a rubrica e qual informação foi enviada ao eSocial.

**Informações apresentadas**

| Campo | Funcionalidade |
| --- | --- |
| **Início Validade** | Início da vigência da configuração. |
| **Término Validade** | Final da vigência da configuração, quando existente. |
| **Rubrica** | Código da rubrica. |
| **Descrição** | Descrição da rubrica. |
| **Natureza** | Natureza da rubrica. |
| **Tipo** | Tipo da rubrica. |
| **Incidência INSS** | Incidência de INSS configurada. |
| **Incidência IRRF** | Incidência de IRRF configurada. |
| **Incidência FGTS** | Incidência de FGTS configurada. |
| **Nº Recibo eSocial (S-1010)** | Número do recibo do S-1010 correspondente à configuração. |
| **Data de Envio** | Data do envio da configuração ao eSocial. |

O número do recibo S-1010 permite rastrear a configuração da rubrica enviada ao eSocial.

**Ausência de histórico**

Quando não houver histórico do S-1010 para a rubrica selecionada, o sistema apresenta a mensagem:

**"Nenhum histórico do S-1010 foi encontrado para a rubrica selecionada. Para o cálculo do valor, o sistema considerou a incidência atual do evento."**

Nesse cenário, o **Valor Sistema** é calculado considerando a incidência atual da rubrica.

O painel também apresenta um resumo com:

- **Rubrica**;
- **Vigência utilizada**;
- **Incidência IRRF**.

| **⚠️** **Atenção**  O Histórico da Rubrica S-1010 é somente para consulta e não permite editar as informações. |
| --- |

**Dedução de dependentes**

O painel **Histórico da Rubrica S-1010** não é apresentado para os tipos de `tpInfoIR` relacionados à **Dedução de Dependentes** de remuneração mensal, 13º salário ou férias.

**3.11. Informações Complementares**

O botão **Informações Complementares** pode ser acessado na tela principal e também na tela de detalhamento.

[GIF animado: Imagem 8: O botão Informações Complementares pode ser acessado na tela principal e também na tela de detalhamento.](https://ajuda.sankhya.com.br/hc/article_attachments/43218383540887)

Essa tela reúne informações adicionais retornadas pelo S-5002 que ajudam na conferência do IRRF.

No topo, o sistema apresenta o contexto da consulta com:

- Empresa Matriz;
- Trabalhador, com CPF e nome;
- Período de Apuração.

As informações são organizadas em quatro cards.

**Dedução de Dependentes e Pensão Alimentícia**

Apresenta:

| Campo | Funcionalidade |
| --- | --- |
| **Informação** | Identifica a informação apresentada. |
| **Tipo de Rendimento** | Identifica o tipo de rendimento relacionado. |
| **Dependente** | Nome do dependente ou beneficiário. |
| **CPF** | CPF do dependente ou beneficiário. |
| **Data de Nascimento** | Data de nascimento. |
| **Tipo de Dependência** | Tipo de dependência. |
| **Valor Sistema** | Valor identificado no sistema. |
| **Valor eSocial** | Valor retornado no eSocial. |
| **Diferença** | Diferença entre os valores. |

**Previdência Complementar**

Apresenta:

| Campo | Funcionalidade |
| --- | --- |
| **Tipo de Previdência** | Tipo da previdência complementar. |
| **CNPJ da Entidade de Previdência** | CNPJ da entidade. |
| **Valor Sistema** | Valor calculado pelo sistema. |
| **Valor eSocial** | Valor retornado pelo eSocial. |
| **Diferença** | Diferença entre os valores. |

Os códigos de incidência relacionados à previdência complementar considerados no relatório são:

**46, 47, 48, 61, 62, 63, 64, 65 e 66.**

**Informações de Processo**

Apresenta:

| Campo | Funcionalidade |
| --- | --- |
| **Tipo Processo** | Tipo do processo relacionado à apuração. |
| **Nº Processo** | Número do processo. |
| **Código Suspensão** | Código de suspensão informado. |
| **Indicativo Apuração** | Indicativo relacionado à apuração. |
| **Valor Não Retido** | Valor não retido. |
| **Valor Dep. Judicial** | Valor de depósito judicial. |
| **Valor Comp. Ano Calendário** | Valor de compensação do ano-calendário. |
| **Valor Comp. Ano Anterior** | Valor de compensação do ano anterior. |
| **Valor Rend. Suspenso** | Valor de rendimento suspenso. |

**Plano de Saúde e Reembolso Médico**

Apresenta:

| Campo | Funcionalidade |
| --- | --- |
| **Informação** | Identifica a informação apresentada. |
| **CNPJ Operadora** | CNPJ da operadora de plano de saúde. |
| **Registro ANS** | Registro da operadora na ANS. |
| **Dependente** | Nome do dependente, quando aplicável. |
| **CPF Dependente** | CPF do dependente. |
| **Data de Nascimento** | Data de nascimento do dependente. |
| **Tipo de Dependência** | Tipo de dependência. |
| **Valor Sistema** | Valor identificado no sistema. |
| **Valor eSocial** | Valor retornado pelo eSocial. |
| **Diferença** | Diferença entre os valores. |

**Plano de saúde**

Para que os valores sejam reconhecidos corretamente, os eventos utilizados na folha devem estar configurados de acordo com as regras de incidência previstas para o relatório.

| **⚠️** **Atenção**  Uma configuração incorreta da rubrica pode resultar em diferença entre o valor calculado no sistema e o valor retornado pelo eSocial. |
| --- |

**Reembolso de despesas médicas**

Os valores de reembolso são apresentados separadamente para:

- Titular;
- Dependentes.

O relatório considera as informações relacionadas ao pagamento e ao retorno do eSocial.

**Voltar**

Clique em **‹ Voltar** para retornar à tela de origem.

Quando o acesso tiver sido feito a partir do detalhamento, o sistema retorna para o detalhamento. Quando tiver sido feito a partir da tela principal, retorna para a tela principal.

**3.12. Exportar os dados**

As telas do relatório possuem opção para exportar os dados em formato **.xlsx**.

![Imagem 9: As telas do relatório possuem opção para exportar os dados em formato .xlsx .](https://ajuda.sankhya.com.br/hc/article_attachments/43219528360215)

A exportação mantém as informações dos cards e grades disponíveis na tela no momento da exportação.

**Exportação do detalhamento**

O arquivo pode conter as seguintes abas:

1. Detalhamento Valor Sistema
2. Detalhamento Valor eSocial
3. Histórico da Rubrica S-1010, quando disponível

**Exportação de Informações Complementares**

O arquivo pode conter as abas:

1. Dedução de Dependentes e Pensão Alimentícia
2. Previdência Complementar
3. Informações de Processo
4. Plano de Saúde e Reembolso Médico

Cada aba recebe o nome correspondente ao card, facilitando a identificação das informações exportadas.

A exportação inclui os cabeçalhos das colunas e os dados apresentados na tela no momento da exportação.

**3.13. Reprocessar a consolidação**

[GIF animado: Imagem 10: 3.13. Reprocessar a consolidação](https://ajuda.sankhya.com.br/hc/article_attachments/43214182672919)

Quando necessário, é possível executar uma nova consolidação das informações utilizando o botão **Reprocessamento da Consolidação**.

Após confirmar o reprocessamento, será apresentado um banner informativo com a indicação:

**Consolidação em andamento**

Clique em **Clique aqui para acompanhar** para visualizar o andamento do processamento.

O reprocessamento atualiza os dados provenientes:

- da folha de pagamento;
- do retorno do eSocial.

As informações são atualizadas automaticamente até a conclusão da consolidação. Após, a finalização, clique em **Fechar**.

Quando houver mais de um processo de consolidação em andamento, o sistema permite navegar entre os processos.

| **⚠️** **Atenção**  O botão fica indisponível quando Empresa Matriz ou Período de Apuração não estiverem preenchidos. |
| --- |

**3.14 Reprocessar Eventos (versão => 5.129)**

Quando o retorno do **S-5002** tiver sido recebido do eSocial, mas as informações não tiverem sido registradas corretamente no sistema, é possível solicitar o reprocessamento diretamente pelo relatório.

Para realizar o procedimento:

1. Informe a **Empresa Matriz**.
2. Informe a **Referência** que deseja reprocessar.
3. Clique em **Reprocessar Eventos**.
4. Confirme a operação, quando solicitado.

O sistema processará novamente os retornos do S-5002 correspondentes ao **empregador e à referência selecionados** e gravará as informações necessárias para a consulta do relatório.

| 💡 **Dica**  O **Reprocessar Eventos** e o **Reprocessar Consolidação** possuem finalidades diferentes:   - **Reprocessar Eventos:** processa novamente os retornos recebidos do eSocial para registrar as informações no sistema. - **Reprocessar Consolidação:** atualiza a consolidação das informações utilizadas na conferência do relatório.   Utilize **Reprocessar Eventos** quando o retorno do eSocial já tiver sido processado, mas os valores não estiverem disponíveis no relatório. Para situações que exigem uma nova consolidação das informações, utilize **Reprocessar Consolidação**. |
| --- |

### 4. Pontos de Atenção

- **Retorno do S-5002**

  O relatório depende do retorno do evento S-5002. Se o S-1210 ainda não tiver sido processado pelo eSocial ou o S-5002 não estiver disponível, não haverá informações suficientes para a conferência.
- **Diferença entre os valores**

  Uma diferença entre Valor Sistema e Valor eSocial não significa necessariamente erro no cálculo da folha.

  Antes de realizar ajustes, verifique:

  - Data de pagamento considerada;
  - Configuração da rubrica;
  - Incidência de IRRF;
  - Categoria do trabalhador;
  - Evento de remuneração relacionado;
  - Retificações ou reprocessamentos realizados;
  - Retorno mais recente do eSocial.
- **Classificação Tributária da empresa**
  O **Valor Sistema** depende da **Classificação Tributária** informada no cadastro da empresa do trabalhador. A consulta é feita pela Empresa Matriz, mas cada filial também precisa ter o campo preenchido. Quando ele está vazio, a coluna Valor Sistema é apresentada zerada em todos os tipos de valores de IRRF dos trabalhadores dessa empresa, mesmo com as incidências de IRRF dos eventos configuradas corretamente. Nesse caso, o reprocessamento da consolidação, sozinho, não corrige a situação.
- **Histórico da Rubrica S-1010**

  O histórico permite identificar a incidência da rubrica de acordo com sua vigência.

  Quando não houver histórico S-1010 para a rubrica, o sistema poderá utilizar a incidência atual do evento para composição do Valor Sistema.
- **Múltiplos contratos**

  O mesmo CPF pode aparecer em linhas distintas quando houver contratos com categorias eSocial diferentes que componham códigos de receita distintos.
- **RRA**

  Para **Rendimentos Recebidos Acumuladamente (RRA)**, determinados valores classificados como `tpInfoIR = 74` podem não ser apresentados para conferência devido às regras de totalização do eSocial.
- **Permissões**

  A ausência de dados pode estar relacionada às permissões de acesso do usuário.
- **Consolidação em andamento**

  Após consultar ou reprocessar o relatório, aguarde a conclusão da consolidação para analisar os dados atualizados.
- O **reprocessamento de eventos** considera somente o **Empregador** e a **Referência** informados na operação. Antes de executar o procedimento, confira os dados selecionados.

### 5. Dicas de Usabilidade

- **Comece pela tela principal**

  Utilize a coluna **Diferença** para localizar rapidamente os tipos de IRRF que precisam de análise.
- Use o filtro **Apenas com diferença**

  Quando o objetivo for investigar divergências, marque **Apenas com diferença** para ocultar os registros sem diferença.
- **Use os filtros das colunas**

  Combine filtros para localizar rapidamente um conjunto específico de informações, como:

  - determinado Código de Receita;
  - determinado Tipo Valores IRRF;
  - determinado trabalhador.
- **Aprofunde a análise**

  Quando encontrar uma divergência:

  1. Abra o detalhamento do Tipo Valores IRRF;
  2. Consulte o **Valor Sistema**;
  3. Compare com o **Valor eSocial**;
  4. Se necessário, selecione uma rubrica;
  5. Consulte o **Histórico da Rubrica S-1010**;
  6. Utilize as **Informações Complementares** quando a divergência estiver relacionada a dependentes, pensão, previdência, processos ou plano de saúde.
- **Use o reprocessamento quando necessário**

  Quando houver atualização recente da folha ou do retorno do eSocial, utilize **Reprocessamento da Consolidação** para atualizar as informações do relatório.
- **Exporte para análises externas**

  Utilize a exportação `.xlsx` quando precisar compartilhar, arquivar ou realizar análises complementares dos dados apresentados no relatório.

## Perguntas Frequentes (FAQ)

**1. Por que o relatório não apresenta dados?**

O relatório depende do retorno do evento S-5002. Verifique se o S-1210 foi enviado e processado pelo eSocial e se o retorno do S-5002 já está disponível.

**2. Por que existe diferença entre Valor Sistema e Valor eSocial?**

A diferença pode estar relacionada à configuração das rubricas, incidência de IRRF, data de pagamento, categoria do trabalhador, informações transmitidas ao eSocial ou a algum processamento/retificação posterior.

Utilize o detalhamento para identificar a origem da diferença.

**3. O que significa Valor Sistema?**

É o valor calculado pelo Pessoal+ com base nas informações da folha de pagamento consideradas para o período.

**4. Por que a coluna Valor Sistema aparece zerada?**

Verifique se a empresa do trabalhador, seja a matriz ou uma filial, tem a **Classificação Tributária** preenchida na tela **Empresas** (Configurações > Cadastros > Empresas), aba **Informações Fiscais**. Sem essa informação, o relatório não compõe o Valor Sistema, mesmo que as incidências de IRRF dos eventos estejam corretas.

Para corrigir:

1. Acesse a tela **Empresas** e selecione a empresa em que o trabalhador está registrado. Se a consulta envolver filiais, repita a verificação para cada uma delas.
2. Na aba **Informações Fiscais**, preencha o campo **Classificação Tributária** com a classificação correspondente ao enquadramento da empresa.
3. Salve o cadastro.
4. No relatório S-5002, clique em **Reprocessar Consolidação** e aguarde a conclusão.
5. Consulte novamente o relatório e confira a coluna **Valor Sistema**.

| **⚠️ Atenção**  Informe a classificação que corresponde ao enquadramento real da empresa, conforme a tabela de Classificação Tributária do eSocial. Essa informação também é usada no evento S-1000 e em outras obrigações. Em caso de dúvida sobre o enquadramento, consulte o responsável contábil ou fiscal da empresa. |
| --- |

**5. O que significa Valor eSocial?**

É o valor retornado pelo eSocial no evento S-5002 para o trabalhador e período consultados.

**6. Como identificar quais rubricas formaram o Valor Sistema?**

Abra o detalhamento do Tipo Valores IRRF e consulte o card **Detalhamento Valor Sistema**.

**7. Como verificar qual incidência de IRRF foi considerada para uma rubrica?**

Selecione a rubrica no card **Detalhamento Valor Sistema** e consulte o **Histórico da Rubrica S-1010**.

**8. Por que o Histórico da Rubrica S-1010 não aparece?**

Esse card não é apresentado para os tipos de `tpInfoIR` relacionados à Dedução de Dependentes.

Para outras rubricas, ele também pode não apresentar registros quando não houver histórico S-1010 disponível.

**9. O que acontece quando não existe histórico S-1010 da rubrica?**

O sistema considera a incidência atual do evento para a composição do Valor Sistema e informa essa condição na tela.

**10. Por que o mesmo CPF aparece mais de uma vez?**

Isso pode acontecer quando o trabalhador possui múltiplos contratos com categorias eSocial diferentes que resultem em códigos de receita distintos.

**11. Posso consultar somente os trabalhadores com divergências?**

Sim. Marque o filtro **Apenas com diferença** antes de clicar em **Consultar**.

**12. Posso filtrar informações diretamente nas colunas?**

Sim. Utilize o ícone **≡** disponível no cabeçalho das colunas para aplicar filtros.

**13. Posso exportar o detalhamento para Excel?**

Sim. O relatório permite exportar os dados em formato `.xlsx`, organizados em abas de acordo com os cards disponíveis.

**14. Quando devo usar o Reprocessamento da Consolidação?**

Utilize o reprocessamento quando precisar atualizar a consolidação das informações da folha e do eSocial, especialmente após alterações ou atualizações recentes dos dados.

**15. O relatório permite alterar as informações exibidas?**

Não. O relatório é destinado à consulta e conferência dos dados. Ajustes devem ser realizados nas respectivas rotinas de origem.

**16.** **O que fazer quando o retorno do S-5002 foi processado pelo eSocial, mas os valores não aparecem no relatório?**

Utilize a opção **Reprocessar Eventos**. Informe o **Empregador** e a **Referência** e execute o reprocessamento. O sistema processará novamente os retornos do S-5002 correspondentes aos dados informados e gravará as informações no sistema.

**17. Qual é a diferença entre Reprocessar Eventos e Reprocessar Consolidação?**

O **Reprocessar Eventos** processa novamente os retornos recebidos do eSocial para registrar as informações no sistema.

O **Reprocessar Consolidação** atualiza a consolidação das informações utilizadas na conferência do relatório.

Utilize **Reprocessar Eventos** quando os retornos do eSocial não estiverem registrados corretamente no sistema. Para atualizar a consolidação das informações já disponíveis, utilize **Reprocessar Consolidação**.

## Artigos Relacionados

- [Cadastro de Empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913)
- [Central do eSocial](https://ajuda.sankhya.com.br/hc/pt-br)
- [Relatório S-5001 – Contribuições Sociais (INSS e PIS)](https://ajuda.sankhya.com.br/hc/pt-br)
- [Relatório S-5003 – Conferência de Informações do FGTS por Trabalhador](https://ajuda.sankhya.com.br/hc/pt-br)
- [S-1210 – Pagamentos de Rendimentos do Trabalho](https://ajuda.sankhya.com.br/hc/pt-br)
