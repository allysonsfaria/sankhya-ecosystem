---
id: "38506849096599"
titulo: "Cadastro de Departamentos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38506849096599-Cadastro-de-Departamentos"
trilha: "Manual do Produto > Pessoas+ > Configurações e Cadastros > Estrutura da Empresa"
atualizado_em: "2026-10-22T11:16:35Z"
rotulos: ["Configuração", "Centro de Resultado", "FPMASCDEP", "FPREGFISCAL", "eSocial", "Cadastro", "Pessoal+", "ID: br.com.sankhya.pes.cad.departamentos", "Cadastro de Departamentos", "Máscara para Departamentos"]
---

# Cadastro de Departamentos

**Módulo:** Pessoal+
**Caminho de acesso:** Pessoal+ > Cadastros > Departamentos
**ID da tela:** br.com.sankhya.pes.cad.departamentos

---

### Sumário

- [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/38506849096599-Cadastro-de-Departamentos#o-que-e)
- [Antes de começar](https://ajuda.sankhya.com.br/hc/pt-br/articles/38506849096599-Cadastro-de-Departamentos#antes-de-comecar)
- [Jornada de uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/38506849096599-Cadastro-de-Departamentos#jornada)
  1. [Definir a máscara dos departamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/38506849096599-Cadastro-de-Departamentos#etapa1)
  2. [Cadastrar o departamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/38506849096599-Cadastro-de-Departamentos#etapa2)
  3. [Configurar a aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/38506849096599-Cadastro-de-Departamentos#etapa3)
  4. [Configurar o departamento como tomador de serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/38506849096599-Cadastro-de-Departamentos#etapa4)
  5. [Vincular colaboradores ao departamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/38506849096599-Cadastro-de-Departamentos#etapa5)
  6. [Inativar um departamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/38506849096599-Cadastro-de-Departamentos#etapa6)
- [Pontos de atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/38506849096599-Cadastro-de-Departamentos#pontos-de-atencao)
- [Perguntas frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/38506849096599-Cadastro-de-Departamentos#faq)

---

### O que é e para que serve

Os **Departamentos** representam as divisões internas da empresa, como áreas, setores ou locais de trabalho. Cada colaborador é vinculado a um departamento, que determina como ele será organizado na estrutura da empresa e pode influenciar o cálculo da Folha de Pagamento, a integração contábil e o envio de informações ao eSocial.

No Pessoas+, os departamentos são utilizados para:

- Organizar os colaboradores na estrutura hierárquica da empresa.
- Definir o Registro Fiscal utilizado no cálculo da Folha de Pagamento e na geração da Guia da Previdência Social (GPS), quando a empresa utiliza Registro Fiscal por departamento.
- Definir o Centro de Resultado utilizado na integração contábil.
- Identificar o tomador de serviço e a lotação tributária enviados ao eSocial, quando a empresa trabalha com cessão de mão de obra ou obras de construção civil.
- Filtrar e agrupar informações em relatórios e rotinas da Folha de Pagamento.

Uma estrutura de departamentos bem planejada facilita a organização da empresa e ajuda a manter a consistência dos cálculos, das guias e das informações enviadas ao eSocial.

### Antes de começar

Antes de cadastrar os departamentos, confira as configurações e os cadastros necessários:

- **Máscara dos departamentos:** defina o formato dos códigos e a quantidade de níveis da hierarquia no parâmetro **Máscara para Departamentos - FPMASCDEP**.
- **Registro Fiscal:** defina se será utilizado por empresa ou por departamento no parâmetro **Onde utiliza o Registro Fiscal? - FPREGFISCAL**. Se a configuração for por departamento, cadastre os Registros Fiscais antes de criar os departamentos.
- **Centro de Resultado:** se a empresa controla custos e resultados por departamento, cadastre os centros de resultado antes de criar os departamentos.
- **Projetos:** se a empresa controla informações por projeto, cadastre os projetos antes de criar os departamentos.
- **Parceiros tomadores de serviço:** se a empresa trabalha com cessão de mão de obra ou obras de construção civil, cadastre os parceiros tomadores antes de criar os departamentos.

📚 Para saber mais, consulte [Parâmetros do Pessoas+](https://ajuda.sankhya.com.br/hc/pt-br/articles/38767444361239) e [Cadastro do Registro Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/39123464898199).

### Jornada de uso

#### 1. Definir a máscara dos departamentos

A máscara determina o formato dos códigos dos departamentos e a quantidade de níveis da estrutura hierárquica. Defina-a antes de cadastrar o primeiro departamento.

1. Acessea tela **Preferências** (Configurações > Avançado).
2. Localize o parâmetro **Máscara para Departamentos - FPMASCDEP**.
3. Configure a máscara conforme a estrutura desejada.

Na máscara:

- Cada `9` representa um dígito do código.
- `\.` (barra invertida seguida de ponto) representa o separador entre os níveis.
- `;0` deve ser mantido ao final da máscara.

Por exemplo, a máscara `99\.99;0` define uma estrutura com dois níveis de dois dígitos cada, permitindo códigos como `01.00` e `01.01`.

Considere esta estrutura de departamentos:

| Código | Departamento | Tipo |
| --- | --- | --- |
| 1.0.00 | Administrativo | Sintético |
| 1.3.00 | Financeiro | Sintético |
| 1.3.01 | Contas a Pagar | Analítico |
| 1.3.02 | Contas a Receber | Analítico |

Para criar essa estrutura, a máscara deve ser `9\.9\.99;0`.

Se o último nível precisar de três dígitos, como em `1.3.001` — Contas a Pagar, utilize a máscara `9\.9\.999;0`.

![Imagem 1: Se o último nível precisar de três dígitos, como em 1.3.001 — Contas a Pagar, utilize a máscara 9\.9\.999;0 .](https://ajuda.sankhya.com.br/hc/article_attachments/38522780930711)

| **🚨 Risco operacional**  Não altere a máscara depois que existirem departamentos cadastrados. A alteração pode comprometer a hierarquia existente e exigir a reestruturação de departamentos já vinculados a colaboradores, centros de resultado, relatórios, histórico de movimentações e integrações contábeis. Planeje a máscara considerando o crescimento da empresa. |
| --- |

Após salvar a configuração, o sistema passa a aceitar códigos de departamento no formato definido.

#### 2. Cadastrar o departamento

![Imagem 2: 2. Cadastrar o departamento](https://ajuda.sankhya.com.br/hc/article_attachments/38522780929943)

Depois de definir a máscara e preparar os cadastros relacionados, crie o departamento na estrutura da empresa.

1. Acesse a tela **Departamentos** (Pessoal+ > Cadastros).
2. Clique em + **Cadastrar Departamentos**.
3. Informe o código no campo **Departamento**, respeitando a máscara configurada.
4. Preencha a **Descrição** do departamento.
5. Continue o preenchimento conforme as orientações da aba Geral e, quando aplicável, da configuração como tomador de serviço.
6. Salve o cadastro.

O código informado determina a posição do departamento na hierarquia.

#### 3. Configurar a aba Geral

Na aba **Geral**, defina como o departamento será utilizado na Folha de Pagamento, na contabilidade e na geração de guias.

**Status do departamento**

- **Ativo:** quando marcado, o departamento pode ser utilizado.
- **Analítico:** quando marcado, indica que o departamento é utilizado operacionalmente, ou seja, pode receber colaboradores e movimentações. Quando desmarcado, o departamento é **sintético** e serve apenas para organizar e consolidar a hierarquia.

| **⚠️ Atenção**  Vincule colaboradores somente a departamentos **ativos e analíticos**. Na integração contábil, o sistema apresenta a inconsistência "Departamento inativo e/ou não analítico" quando existem colaboradores sendo contabilizados em departamentos inativos ou sintéticos. |
| --- |

**Endereço**

Informe **Endereço**, **Número** e **Complemento** da localização física do departamento.

**Centro de Resultado**

Informe o centro de resultado do departamento quando a empresa controla custos e resultados por departamento.

O centro de resultado do departamento pode ser substituído por um centro de resultado informado em um nível mais específico. A ordem de prioridade é:

1. Movimento;
2. Funcionário;
3. Evento;
4. Departamento;
5. Empresa.

Na integração contábil, quando o departamento não tem centro de resultado, o sistema utiliza o centro de resultado da empresa.

📚 Para saber mais, consulte: [Como configurar a integração contábil](https://ajuda.sankhya.com.br/hc/pt-br/articles/10137196517783).

**Registro fiscal**

Informe o Registro Fiscal do departamento conforme a configuração do parâmetro **Onde utiliza o Registro Fiscal? - FPREGFISCAL**:

| Configuração do FPREGFISCAL | Comportamento do sistema |
| --- | --- |
| Empresas | O cálculo da Folha de Pagamento e a GPS utilizam o Registro Fiscal da empresa. A geração das guias é feita somente por empresa. |
| Departamentos | O cálculo da Folha de Pagamento utiliza o Registro Fiscal do departamento do colaborador, e a GPS pode ser gerada por departamento. No cadastro da empresa, o campo **Reg. Fiscal Apro/Guia** fica desabilitado. |

| **⚠️ Atenção**  Quando o parâmetro FPREGFISCAL está configurado como **Departamentos**, todos os departamentos utilizados na Folha de Pagamento devem ter um Registro Fiscal preenchido.  Se o departamento do colaborador não tiver Registro Fiscal, o cálculo da folha apresentará a mensagem:  "A folha está configurada para utilizar o registro fiscal vinculado ao departamento e o departamento do funcionário não possui registro fiscal vinculado."  Para resolver, informe o Registro Fiscal no departamento e calcule a folha novamente. |
| --- |

**Projeto**

Informe o projeto ao qual o departamento está vinculado, quando a empresa controla informações por projeto. Os projetos são cadastrados na tela **Projetos** (Configurações > Cadastros > Gerencial > Projetos).

Após preencher os campos aplicáveis, o departamento estará configurado para uso no cadastro de colaboradores, no cálculo da folha e na integração contábil.

#### 4. Configurar o departamento como tomador de serviço

Quando a empresa trabalha com cessão de mão de obra ou obras de construção civil, o departamento pode identificar o tomador de serviço dos colaboradores vinculados a ele.

O tomador de serviço é o parceiro que contrata os serviços terceirizados e assume a corresponsabilidade pelo contrato de trabalho do colaborador vinculado à prestação de serviço. Esse tipo de departamento também é chamado de departamento externo.

Na configuração do departamento:

1. No campo **Cód. Parceiro**, informe o parceiro que representa o tomador de serviço.
2. No campo **Tipo Lotação**, selecione o tipo de lotação tributária correspondente, conforme a Tabela 10 do eSocial. A lista apresenta somente os tipos permitidos para departamentos.
3. Quando o tipo de lotação for **2 — Obra de Construção Civil (Empreitada/Subempreitada)**, preencha, quando aplicável, as abas:
   - **Inscrição do proprietário do CNO:** informe o tipo de inscrição e o número do CNPJ ou CPF do proprietário, quando ele não estiver identificado no CNO.
   - **Inscrição do contratante:** informe o tipo de inscrição e o número do CNPJ ou CPF do contratante, quando a empresa atuar em regime de empreitada parcial ou subempreitada.
4. Salve o cadastro.

Observe as seguintes regras:

- Observe as seguintes regras:
- **Vínculo do tomador:** o sistema identifica o tomador pelo departamento em que o colaborador está lotado. Informe o Cód. Parceiro no próprio departamento, pois o sistema não busca o parceiro informado somente no departamento superior.
- **Atualização do tomador:** com o parâmetro **Consiste Tomador com Departamento? - FPTOMADORDEP** ligado, o tomador acompanha o departamento. Na admissão, o sistema inclui o tomador vinculado ao departamento; quando o colaborador é transferido para outro departamento com tomador diferente, o sistema atualiza o tomador correspondente.
- **Informações fiscais:** no envio do S-1020 — Tabela de Lotações Tributárias, o Registro Fiscal do departamento define o código do Fundo de Previdência e Assistência Social (FPAS) e os códigos de terceiros da lotação.
- **Departamentos vinculados ao mesmo parceiro:** se mais de um departamento estiver vinculado ao mesmo parceiro, o sistema utiliza os dados do departamento de menor código.

| **⚠️ Atenção**  Confira se o parceiro e o tipo de lotação estão corretos. Dados incorretos podem gerar inconsistências na lotação enviada ao eSocial e na identificação da obra ou do tomador na guia do FGTS Digital. |
| --- |

Os colaboradores lotados no departamento passam a ser vinculados ao tomador de serviço informado.

📚 Para ver exemplosde configuração de obra, consulte [Como configurar a obra como tomador de serviço e informar o CNO no eSocial e no FGTS Digital](https://ajuda.sankhya.com.br/hc/pt-br/articles/28337059458455).

#### 5. Vincular colaboradores ao departamento

O departamento de cada colaborador é informado no cadastro do colaborador, na aba **Lotação**.

Utilize somente departamentos ativos e analíticos.

Se o departamento não existir, estiver inativo ou não puder ser utilizado, o sistema apresenta a mensagem:

"Departamento não existe ou está inativo ou não pode ser usado aqui."

Para resolver, confira o cadastro do departamento e, se necessário, marque as opções **Ativo** e **Analítico**.

📚 Para saber mais, acesse: [Configuração de Funcionários](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639).

#### 6. Inativar um departamento

Quando um departamento deixar de ser utilizado, prefira inativá-lo em vez de excluí-lo. Dessa forma, é possível preservar o histórico relacionado ao cadastro.

Antes de inativar o departamento, transfira os colaboradores ativos para outro departamento.

| **🚨 Risco operacional**  Não exclua departamentos que tenham colaboradores vinculados, histórico em folhas já calculadas ou lançamentos contábeis associados. A exclusão pode comprometer relatórios, recálculos e a rastreabilidade das informações. Prefira desmarcar a opção **Ativo**. |
| --- |

### Pontos de atenção

- **Máscara:** defina o formato antes de cadastrar o primeiro departamento. Evite alterá-lo depois que a estrutura estiver em uso.
- **Departamentos sintéticos e analíticos:** os sintéticos organizam a hierarquia; os analíticos podem receber colaboradores e movimentações.
- **Registro Fiscal por departamento:** quando o `FPREGFISCAL` estiver configurado como Departamentos, todos os departamentos utilizados na folha precisam ter Registro Fiscal. A ausência dessa informação impede o cálculo do colaborador.
- **Centro de Resultado:** o Centro de Resultado do departamento pode ser substituído pelo informado no movimento, no funcionário ou no evento. Padronize o nível de controle adotado pela empresa para evitar divergências.
- **Tomador de serviço:** o parceiro e o tipo de lotação do departamento influenciam as informações enviadas nos eventos S-1020 e S-1200 e a identificação do tomador na guia do FGTS Digital.
- **Lotações Tributárias da empresa:** os departamentos também podem ser vinculados às lotações cadastradas na aba Lotações Tributárias do cadastro da empresa. Nesse caso, todos os colaboradores do departamento são vinculados à lotação.

### Perguntas frequentes

**1. Qual a diferença entre departamento sintético e analítico?**

O departamento sintético organiza a hierarquia e agrupa outros departamentos. O departamento analítico é o último nível da estrutura e é o único que pode receber colaboradores e movimentações.

**2. Como devo escrever a máscara dos departamentos?**

Use 9 para cada dígito, \. para separar os níveis e mantenha ;0 no final. Por exemplo, 9\.9\.99;0 gera códigos como 1.3.01.

**3. Posso alterar a máscara dos departamentos depois de cadastrá-los?**

Não é recomendado. A alteração pode comprometer a hierarquia existente e exigir a reestruturação dos departamentos e das integrações contábeis.

**4. Por que o cálculo da folha informa que o departamento não possui registro fiscal?**

O parâmetro FPREGFISCAL está configurado como Departamentos e o departamento do colaborador não tem Registro Fiscal. Informe o Registro Fiscal no departamento e calcule a folha novamente.

**5. Por que não consigo vincular o colaborador a um departamento?**

O departamento pode estar inativo, ser sintético ou não existir. Confira se as opções Ativo e Analítico estão marcadas no cadastro do departamento.

**6. O departamento herda o tomador de serviço do departamento superior?**

Não. Informe o Cód. Parceiro no próprio departamento em que os colaboradores estão lotados.

**7. Posso excluir um departamento que não uso mais?**

Se ele tiver colaboradores, histórico de folha ou lançamentos contábeis, não. Nesses casos, desmarque a opção Ativo.
