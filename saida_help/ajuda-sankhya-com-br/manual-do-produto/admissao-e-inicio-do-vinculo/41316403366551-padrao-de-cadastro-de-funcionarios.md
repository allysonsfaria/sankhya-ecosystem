---
id: "41316403366551"
titulo: "Padrão de Cadastro de Funcionários"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/41316403366551-Padr%C3%A3o-de-Cadastro-de-Funcion%C3%A1rios"
trilha: "Manual do Produto > Pessoas+ > Colaboradores > Admissão e Início do Vínculo"
atualizado_em: "2026-10-19T13:37:03Z"
rotulos: ["Configuração", "Funcionários", "Admissão", "eSocial", "requisição de admissão", "ID: br.com.sankhya.rh.PadroesCadFuncionarios", "Padrão de Cadastro Funcionários", "Cadastro", "Pessoal+"]
---

# Padrão de Cadastro de Funcionários

**Módulo:** Pessoal+
**Caminho de Acesso:** Pessoal+ > Cadastros
**ID da Tela:** br.com.sankhya.rh.PadroesCadFuncionarios

---

## Descrição e Usabilidade

A rotina **Padrão de Cadastro Funcionários** permite criar modelos de admissão com informações previamente definidas para agilizar o cadastro de novos colaboradores.

Os padrões podem conter dados contratuais, organizacionais, sindicais, bancários, de ponto e demais informações que serão utilizadas durante a admissão, reduzindo o preenchimento manual e promovendo maior padronização dos cadastros.

Além do cadastro direto de colaboradores, esses padrões também podem ser utilizados na **Requisição de Admissão**, auxiliando no preenchimento automático das informações do colaborador.

Por meio desta rotina é possível criar diferentes modelos de cadastro de acordo com o tipo de contratação da empresa, como:

- Colaborador CLT;
- Aprendiz;
- Estagiário;
- Intermitente;
- Diretor;
- Autônomo.

As informações configuradas em cada padrão poderão ser reaproveitadas em novas admissões, proporcionando mais agilidade e reduzindo inconsistências cadastrais.

Quando um padrão é selecionado durante a **Requisição de Admissão**, o sistema utiliza as informações configuradas no modelo para complementar os dados do colaborador.

A aplicação dos dados ocorre da seguinte forma:

- Campos preenchidos no padrão substituem os valores existentes na requisição;
- Campos vazios ou zerados no padrão não sobrescrevem informações já preenchidas;
- Dados informados pelo solicitante ou recebidos por integração são preservados quando o campo correspondente estiver vazio no padrão;
- A remoção do padrão não apaga os dados já preenchidos na requisição.

### 2. Pré-requisitos

Antes de utilizar esta rotina, é necessário:

- Possuir acesso à tela **Padrão de Cadastro Funcionários** (Pessoal+ > Cadastros).

  Essa liberação é feita na tela **Acessos** (Configurações > Controle de Acesso), pelo administrador do sistema.
- Ter os cadastros auxiliares previamente configurados, como cargos, funções, departamentos, sindicatos, bancos e jornadas;
- Definir quais informações deverão ser padronizadas para cada tipo de contratação.

### 3. Jornada de Uso

[GIF animado: Imagem 1: 3. Jornada de Uso](https://ajuda.sankhya.com.br/hc/article_attachments/41316963912087)

1. Acesse a tela **Padrão de Cadastro Funcionários** (Pessoal+ > Cadastros);
2. Para iniciar um cadastro, clique no botão (+) **Cadastrar Padrão de Cadastro de Funcionários**;
3. Selecione o **Tipo de Cadastro** conforme o vínculo que será utilizado;
4. A marcação **Padrão do Sistema** será habilitada automaticamente após a gravação do cadastro;
5. O campo **Código** identifica o padrão criado e poderá ser preenchido automaticamente ou manualmente, conforme a configuração definida para a tela.

📚 Para saber mais, acesse [Definição da Numeração dos Cadastros no Pessoal+](https://ajuda.sankhya.com.br/hc/pt-br/articles/41317860396823).

6. Informe uma **Descrição** para facilitar a identificação do modelo.

|  |
| --- |
| **⚠️** **Atenção** Recomenda-se preencher apenas as informações que realmente devem ser padronizadas para todos os colaboradores que utilizarão esse modelo. Campos deixados em branco não removerão informações já existentes na Requisição de Admissão. |

7. Configure as abas conforme a necessidade do padrão e salve o cadastro.

#### 🔹Aba Admissão

Nesta aba, informe os dados relacionados ao vínculo do colaborador com a empresa.

| Campo | Finalidade |
| --- | --- |
| **Indicativo de Admissão** | Identifica se a admissão ocorreu de forma normal ou em decorrência de ação fiscal ou decisão judicial, conforme exigência do eSocial. |
| **Categoria para o eSocial** | Identifica a categoria do trabalhador perante o eSocial. |
| **Situação no eSocial** | Determina quais eventos admissionais serão gerados para o eSocial. |
| **Vínculo** | Define a natureza jurídica da relação de trabalho. |
| **Regime Trabalhista** | Indica a legislação aplicada ao contrato. |
| **Regime Previdenciário** | Define o enquadramento previdenciário do trabalhador. |
| **Regime de Jornada** | Identifica o tipo de controle de jornada adotado. |
| **Tabela de Categoria FGTS** | Define o enquadramento do trabalhador para recolhimento do FGTS. |
| **Tabela de Ocorrência FGTS** | Identifica situações relacionadas à exposição a agentes nocivos. |
| **Optante pelo FGTS** | Indica se haverá recolhimento de FGTS para o trabalhador. |
| **Período de Experiência** Os campos relacionados ao período de experiência definem previamente a duração do contrato de experiência que será sugerida durante a admissão do colaborador. Essa configuração é utilizada para preencher automaticamente os períodos inicial e de prorrogação do contrato quando o **Vínculo** selecionado permitir contrato de experiência. - contrato temporário (50); - menor aprendiz (55); - prazo determinado - pessoa jurídica ou física, urbano ou rural (60, 65, 70, 75). Para os demais vínculos, como estagiário, servidor público, autônomo, pensionista, diretor sem vínculo empregatício, funcionário avulso (02, 10, 15, 20, 25, 30, 31, 35, 40, 80, 90, 99), não será necessário o preenchimento desses campos,  pois o contrato de experiência não se aplica. |  |

#### 🔹Aba Pessoal

Informe os dados pessoais que deverão ser aplicados automaticamente aos novos colaboradores.

| Campo | Finalidade |
| --- | --- |
| **Nacionalidade** | Define a nacionalidade padrão dos colaboradores vinculados ao modelo. |

#### 🔹Aba Contrato

Defina as informações relacionadas relacionadas à remuneração e condições contratuais.

| Campo | Finalidade |
| --- | --- |
| **Salário Base** | Define o salário inicial sugerido na admissão. |
| **Horas Semanais** | Indica a carga horária contratual semanal. |
| **Remuneração Mínima Assegurada** | Define o valor mínimo garantido ao trabalhador. |
| **Tipo de Salário** | Determina a forma de cálculo da remuneração. |
| **Tipo de Remuneração** | Define se o colaborador recebe salário fixo, variável ou ambos. |
| **Tipo de Recebimento** | Indica como o pagamento será realizado. |
| **% Adiantamento** | Define o percentual de adiantamento salarial. |
| **% Periculosidade** | Define o adicional de periculosidade. |
| **% Insalubridade** | Define o adicional de insalubridade. |
| **Participa do Programa de Alimentação do Trabalhador** | Indica participação no Programa de Alimentação do Trabalhador. |

#### 🔹Aba Banco

Informe os dados bancários padrão utilizados para pagamento dos colaboradores.

| Campo | Finalidade |
| --- | --- |
| **Banco** | Define a instituição financeira padrão. |
| **Agência** | Define a agência bancária utilizada. |

#### 🔹Aba Lotação

Configure as informações organizacionais, como departamento, cargo, função e cidade de trabalho.

| Campo | Finalidade |
| --- | --- |
| **Departamento** | Define a área de atuação do colaborador. |
| **Cargo** | Define o cargo padrão da admissão. |
| **Função** | Define a função exercida pelo trabalhador. |
| **Categoria** | Define a categoria interna utilizada pela empresa. |
| **Cidade de Trabalho** | Define o local de prestação dos serviços. |
| **Filiado ao Sindicato de Classe** | Indica se os colaboradores admitidos por meio desse padrão são representados por um sindicato de classe. Ao habilitar essa opção, o sistema permite informar o sindicato que será associado automaticamente ao cadastro do colaborador durante a admissão. |
| **Sindicato** | Define a representação sindical utilizada em rotinas relacionadas às obrigações sindicais, convenções coletivas e demais processos trabalhistas aplicáveis à categoria profissional. |

#### 🔹Aba Configurações

Defina parâmetros utilizados nos cálculos de férias, provisões e demais regras do colaborador.

| Campo | Finalidade |
| --- | --- |
| **Tipo de Tabela de INSS/IRRF/Salário Família** | Determina as tabelas de cálculo utilizadas. |
| **Dias de Férias por Ano** | Define a quantidade padrão de dias de férias. |
| **Provisiona 13º Salário** | Indica se haverá provisão contábil do 13º salário. |
| **Provisiona Férias** | Indica se haverá provisão contábil de férias. |

#### 🔹Aba Configurações de Ponto

Configure as informações relacionadas ao controle de ponto, como:

| Campo | Finalidade |
| --- | --- |
| **Utiliza Ponto Manual/Mecânico** | Define a forma de controle de ponto. |
| **Dia de Início da Apuração** | Determina a data inicial do período de apuração do ponto. |
| **Carga Horária** | Define a jornada padrão utilizada no controle de ponto. |

---

|  |
| --- |
| **⚠️** **Atenção** Quando o Padrão de Cadastro for utilizado em uma Requisição de Admissão, campos desta aba somente substituirão informações já existentes se possuírem valor configurado no padrão. Caso contrário, os dados informados pelo solicitante ou recebidos por integração serão preservados. |

**Exemplo**

A requisição possui os seguintes dados:

- **Cargo**: Analista Administrativo
- **Carga Horária**: 220 horas

O padrão selecionado possui:

- **Cargo**: Supervisor Administrativo
- **Carga Horária**: Não informado

Resultado após aplicação do padrão:

- **Cargo**: Supervisor Administrativo
- **Carga Horária**: 220 horas

Nesse cenário, apenas o campo Cargo é atualizado, pois possui valor configurado no padrão.

### 4. Ponto de Atenção

- Os campos vazios ou zerados no Padrão de Cadastro não removem informações já existentes na Requisição de Admissão.
- Informações preenchidas manualmente pelo solicitante ou recebidas por integrações externas serão preservadas sempre que o campo correspondente não possuir valor definido no padrão.
- Ao remover um padrão já selecionado na Requisição de Admissão, os dados preenchidos no formulário permanecem disponíveis e não são apagados automaticamente.

### 5. Dicas de Usabilidade

- Preencha apenas os campos que realmente devem ser padronizados para todos os colaboradores daquele perfil.
- Evite cadastrar informações muito específicas em padrões genéricos.
- Crie modelos separados para diferentes tipos de contratação ou unidades da empresa.
- Revise periodicamente os padrões para garantir que cargos, jornadas e configurações estejam atualizados.

## Perguntas Frequentes (FAQ)

**1. Se um campo estiver vazio no padrão, ele apagará o valor existente na requisição?**

Não. Campos vazios ou zerados não substituem informações já preenchidas.

**2. O padrão pode substituir dados recebidos por integração?**

Sim. Porém, somente quando o campo correspondente estiver preenchido no padrão.

**3. O que acontece ao remover um padrão já selecionado?**

Os dados já preenchidos permanecem na requisição e não são apagados automaticamente.

**4. Posso utilizar vários padrões para o mesmo tipo de contratação?**

Sim. É possível criar quantos padrões forem necessários para atender diferentes processos de admissão.

## Artigos Relacionados

- [Requisição de Admissão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360059085273-Requisi%C3%A7%C3%B5es#admissao)
- [Cadastro de Funcionários](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639)
- [Configuração de Cargo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611994)
- [Configuração de Função](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118393)
- [Configuração de Departamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/38506849096599)
