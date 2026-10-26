---
id: "39123464898199"
titulo: "Cadastro do Registro Fiscal"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39123464898199-Cadastro-do-Registro-Fiscal"
trilha: "Manual do Produto > Pessoas+ > Configurações e Cadastros > Estrutura da Empresa"
atualizado_em: "2026-10-22T12:59:54Z"
rotulos: ["Configuração", "Impostos", "eSocial", "Folha de Pagamento", "br.com.sankhya.rh.RegistroFiscal", "Registro Fiscal", "PIS sobre a Folha de Pagamento", "FGTS", "Pessoal+"]
---

# Cadastro do Registro Fiscal

**Módulo:** Pessoal+
**Caminho de acesso:** Pessoal+ > Cadastros
**ID da tela:** br.com.sankhya.rh.RegistroFiscal

---

### Sumário

- [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/39123464898199-Cadastro-do-Registro-Fiscal#o-que-e)
- [Antes de começar](https://ajuda.sankhya.com.br/hc/pt-br/articles/39123464898199-Cadastro-do-Registro-Fiscal#antes-de-comecar)
- [Jornada de uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/39123464898199-Cadastro-do-Registro-Fiscal#jornada)
  1. [Reunir os dados fiscais da empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/39123464898199-Cadastro-do-Registro-Fiscal#etapa1)
  2. [Cadastrar o Registro Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/39123464898199-Cadastro-do-Registro-Fiscal#etapa2)
  3. [Configurar a aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/39123464898199-Cadastro-do-Registro-Fiscal#etapa3)
  4. [Configurar a aba Desoneração da Folha](https://ajuda.sankhya.com.br/hc/pt-br/articles/39123464898199-Cadastro-do-Registro-Fiscal#etapa4)
  5. [Configurar as abas Contabilização e Processos de Terceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/39123464898199-Cadastro-do-Registro-Fiscal#etapa5)
  6. [Vincular o Registro Fiscal à empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/39123464898199-Cadastro-do-Registro-Fiscal#etapa6)
  7. [Conferir os encargos e consultar o histórico](https://ajuda.sankhya.com.br/hc/pt-br/articles/39123464898199-Cadastro-do-Registro-Fiscal#etapa7)
- [Pontos de atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/39123464898199-Cadastro-do-Registro-Fiscal#pontos-de-atencao)
- [Perguntas frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/39123464898199-Cadastro-do-Registro-Fiscal#faq)

---

### O que é e para que serve

O **Registro Fiscal** reúne as informações tributárias e previdenciárias utilizadas no cálculo dos encargos da Folha de Pagamento, na geração das guias de recolhimento e no envio de informações ao eSocial.

Nesse cadastro, são configurados, entre outros dados:

- **Percentuais de contribuição:** INSS patronal, FGTS, Risco Ambiental do Trabalho (RAT), Fator Acidentário de Prevenção (FAP) e contribuições destinadas a terceiros.
- **Enquadramento tributário:** opção pelo Simples Nacional e desoneração da folha.
- **Códigos fiscais:** Fundo de Previdência e Assistência Social (FPAS), Classificação Nacional de Atividades Econômicas (CNAE), código de terceiros e código da Guia da Previdência Social (GPS).
- **PIS sobre a folha:** incidência e informações relacionadas à contribuição.
- **Informações de inscrição:** CNPJ, CEI, Cadastro Nacional de Obras (CNO) ou Cadastro de Atividade Econômica da Pessoa Física (CAEPF).

Cada empresa deve ter um Registro Fiscal vinculado ao seu cadastro. Conforme a configuração e a necessidade da empresa, também podem ser utilizados Registros Fiscais específicos para departamentos, lotações tributárias e obras.

Essas informações devem refletir o enquadramento fiscal e previdenciário da empresa, considerando a legislação aplicável, incluindo a Lei nº 8.212/1991, a Lei nº 8.036/1990, a Lei nº 12.546/2011, a Lei nº 14.973/2024 e as regras do eSocial.

### Antes de começar

Antes de cadastrar ou alterar um Registro Fiscal:

- **Permissão de acesso:** confirme se você tem acesso à tela Registro Fiscal. A liberação é feita pelo administrador do sistema na tela **Acessos** (Configurações > Controle de Acesso).
- **Dados fiscais:** reúna as informações da empresa com o contador ou o responsável tributário, incluindo percentuais, códigos e enquadramento fiscal.
- **Processos de terceiros:** se a empresa possui processos administrativos ou judiciais que alteram ou suspendem contribuições destinadas a terceiros, cadastre esses processos antes de configurar o Registro Fiscal.

| **💡 Dica**  Utilize o botão **Configuração da Tela** para reorganizar os campos e ocultar os que não se aplicam à empresa. Na janela, selecione a aba desejada, mova os campos a partir do painel **Campos disponíveis** e clique em **Salvar**. Para ocultar um campo, faça a operação inversa.  [GIF animado: Imagem 1: Utilize o botão Configuração da Tela para reorganizar os campos e ocultar os que não se aplicam à empresa. Na janela,…](https://ajuda.sankhya.com.br/hc/article_attachments/39148872700951) |
| --- |

### Jornada de uso

#### 1. Reunir os dados fiscais da empresa

Antes de iniciar o cadastro, obtenha com a contabilidade os dados necessários para preencher o Registro Fiscal.

A tabela abaixo apresenta um exemplo dos tipos de informação que podem ser necessários. Os valores são ilustrativos e não devem ser utilizados como referência para o enquadramento de outra empresa.

| Dados gerais | Percentuais | Atividade e códigos | RAT – agentes nocivos |
| --- | --- | --- | --- |
| Cidade: Uberlândia | Taxa Terceiros – INSS: 5,8 | CNAE: 6203100 | 15 anos: 12 |
| CNPJ: 26.314.062/0001-61 | INSS Empresa: 20% | IRF: 561 | 20 anos: 9 |
| Não optante pelo Simples | Taxa de Seguro: 3% | FPAS: 515 | 25 anos: 6 |
| Não desonera a folha | FGTS: 8% | INSS Terceiros: 115 |  |
| ISS: 1 – Prestador de serviço | FGTS Menor Aprendiz: 2% | SAT: 62031 |  |
|  | FAP: 1 | GPS: 2100 |  |

| **💡 Dica**  Confirme os dados com o responsável tributário antes de salvar o cadastro. Não utilize percentuais ou códigos de outra empresa sem verificar se são aplicáveis ao enquadramento fiscal da empresa em questão. |
| --- |

#### 2. Cadastrar o Registro Fiscal

Crie o registro que reunirá as informações fiscais utilizadas pela empresa, departamento ou obra.

[GIF animado: Imagem 2: Crie o registro que reunirá as informações fiscais utilizadas pela empresa, departamento ou obra.](https://ajuda.sankhya.com.br/hc/article_attachments/39125315332631)

1. Acesse a tela **Registro Fiscal** (Pessoal+ > Cadastros).
2. Clique em **+** **Cadastrar Registro Fiscal**.
3. No campo **Cód. Registro**, informe o código do Registro Fiscal. Ele pode ser digitado manualmente ou gerado automaticamente, conforme a opção **Numeração**, disponível no botão **Configuração da Tela**.
4. No campo **Descrição**, informe um nome de fácil identificação, como a razão social da empresa ou "Registro Fiscal – Obra X".
5. Clique em **Salvar** (F7).

Após salvar, o Registro Fiscal será criado e as abas de configuração ficarão disponíveis.

#### 3. Configurar a aba Geral

Na aba **Geral**, informe os dados fiscais utilizados no cálculo dos encargos, na geração das guias e no envio de informações ao eSocial.

**Identificação**

- **Cidade:** município da empresa, utilizado em regras fiscais e obrigações acessórias.
- **Código das opções pelo Simples:** indica se a empresa é optante pelo Simples Nacional.
- **Indicador de contribuição Simples Nacional:** indica se a contribuição previdenciária é substituída integralmente, não substituída ou parcialmente substituída.
- **Indicativo de substituição da Contribuição Previd. Patronal:** indica se a contribuição patronal é integralmente ou parcialmente substituída, conforme a Lei nº 12.546/2011. Essa informação é enviada ao eSocial no evento S-1280 – Informações Complementares aos Eventos Periódicos.

**Percentuais**

- **Taxa Terceiros - INSS:** percentual das contribuições destinadas a terceiros (outras entidades e fundos).
- **Percentual de INSS:** percentual da contribuição patronal ao INSS. Quando a empresa informa o percentual da receita bruta na aba **Desoneração da Folha**, esse campo é calculado automaticamente e fica desabilitado. Veja a [etapa 4](https://ajuda.sankhya.com.br/hc/pt-br/articles/39123464898199-Cadastro-do-Registro-Fiscal#etapa4).
- **Taxa de seguro:** percentual do Seguro de Acidente do Trabalho (SAT), também chamado de RAT.
- **Fator Acidentário de Prevenção (FAP):** fator que ajusta o percentual do RAT, divulgado anualmente pelo governo.
- **Percentual FGTS:** percentual do FGTS sobre a remuneração. O padrão é 8%.
- **Percentual do FGTS para Menor Aprendiz:** percentual reduzido do FGTS para aprendizes, de 2%.
- **Percentual do FGTS Verde Amarelo:** percentual do FGTS para contratos na modalidade Verde e Amarelo.
- **Percentual Isenção Filantropia:** percentual de isenção de contribuições para entidades filantrópicas beneficiárias.
- **ISS Autônomo-Responsável pela retenção:** indica quem recolhe o Imposto Sobre Serviços (ISS) dos autônomos: **1 – Prestador de serviço** ou **2 – Empresa Tomadora**.
- **INSS Emp. Func** e **INSS Emp. C. Indiv.:** indicam se o INSS patronal é calculado para empregados e para contribuintes individuais.
- **Salário mínimo vigente:** valor do salário mínimo.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **ℹ Nota – adicional do SENAI na Taxa Terceiros**  A partir da competência **05/2026**, o sistema ajusta automaticamente o campo **Taxa Terceiros - INSS** das empresas que atendem simultaneamente às seguintes condições:   - FPAS `507` (indústria) ou `833` (agroindústria). - Código de terceiros (INSS Terceiros) `0079`.   O sistema contabiliza os empregados das categorias `1XX` do eSocial com folha calculada na competência, somando a matriz e as filiais cadastradas no sistema.  A taxa aplicada depende da quantidade de empregados:   | Quantidade de empregados | Taxa de terceiros | | --- | --- | | Mais de 500 | 6,0 (5,8 + 0,2 do adicional do SENAI) | | Até 500 | 5,8 |   O ajuste ocorre somente em competências abertas. Quando as condições são atendidas, não é necessário alterar manualmente o campo. |

**Inscrição**

Os campos dessa seção identificam a inscrição utilizada no Registro Fiscal.

- **Tipo CNPJ/CEI:** tipo de inscrição: **CNPJ**, **CEI**, **CNO** (Cadastro Nacional de Obras) ou **CAEPF** (Cadastro de Atividade Econômica da Pessoa Física).
- **CNPJ/CEI:** número da inscrição. Quando o tipo é CNPJ, o sistema valida o número e apresenta a mensagem "CNPJ CNPJ/CEI inválido. Verifique o número informado" se ele estiver incorreto.
- **Tipo de CAEPF:** quando a inscrição for CAEPF, indica se o titular é contribuinte individual, produtor rural ou segurado especial.
- **Obra Própria?:** exibido somente quando o tipo de inscrição é **CNO**. Marque quando a obra pertence à própria empresa.
- **CNPJ Responsável:** exibido e obrigatório quando o tipo de inscrição é CNO e a opção **Obra Própria?** está marcada. Informe o CNPJ do responsável pela obra, conforme as regras do eSocial. Se o número estiver incorreto, o sistema apresenta a mensagem "CNPJ Responsável inválido. Verifique o número informado".

**Atividade**

- **CNAE/IBGE:** atividade econômica da empresa, utilizada no enquadramento fiscal, no RAT e no eSocial.
- **IRF:** código de retenção do Imposto de Renda Retido na Fonte (IRRF).
- **Cód. FPAS:** código do FPAS, que classifica a atividade para as contribuições previdenciárias e de terceiros.

**Códigos**

- **INSS Terceiros:** código de terceiros, que identifica as entidades e os fundos para os quais a empresa contribui (por exemplo, 0115 ou 0079).
- **SAT:** código de classificação para o cálculo do Seguro de Acidente do Trabalho.
- **GPS:** código de pagamento utilizado na Guia da Previdência Social.

**RAT – agentes nocivos**

Informe os percentuais adicionais relacionados à aposentadoria especial dos colaboradores expostos a agentes nocivos, conforme o tempo de exposição aplicável:

- **15 anos**
- **20 anos**
- **25 anos**

Confirme os percentuais com o responsável tributário antes de preencher esses campos.

**PIS sobre a folha**

Configure a incidência do PIS sobre a folha de pagamento, quando aplicável à empresa.

- **Empresa contribuinte:** marque essa opção quando a empresa contribui para o PIS sobre a folha.
- **Alíquota:** informe a alíquota aplicável. O campo fica habilitado somente quando **Empresa contribuinte** está marcada.
- **Cód. da Receita:** informe o código da receita. O campo também fica habilitado somente quando **Empresa contribuinte** está marcada.

📚 Para saber mais, consulte: [PIS sobre a folha de pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/28240000315543).

Depois de preencher os campos aplicáveis, confira as informações da aba Geral e salve o cadastro.

#### 4. Configurar a aba Desoneração da Folha

Utilize a aba **Desoneração da Folha** quando a empresa estiver enquadrada na contribuição previdenciária sobre a receita bruta.

Preencha separadamente as informações referentes à folha mensal e ao 13º salário.

- **Percentual da Receita Bruta para INSS:** percentual da receita bruta sujeito à contribuição substitutiva.
- **Valor do INSS da Receita Bruta:** valor da contribuição sobre a receita bruta. O sistema não calcula esse valor. Informe o valor apurado pela contabilidade.

**Regra de cálculo do Percentual de INSS**

Quando o campo **Percentual da Receita Bruta para INSS** está preenchido, o sistema calcula automaticamente o **Percentual de INSS** da aba Geral e desabilita sua edição.

Conforme a regra de reoneração gradual descrita no cadastro, o cálculo considera o ano da competência e o percentual aplicável sobre a parcela da receita bruta:

| Ano da competência | Percentual aplicado sobre a parcela da receita bruta |
| --- | --- |
| 2025 | 5% |
| 2026 | 10% |
| 2027 | 15% |
| 2028 em diante | 20% |

A fórmula utilizada é:

`Percentual de INSS = ((100 − percentual da receita bruta) ÷ 100) × 20 + (percentual da receita bruta ÷ 100) × percentual do ano`

**Exemplo:** considerando 40% de receita bruta em 2026:

`Percentual de INSS = (60 ÷ 100 × 20) + (40 ÷ 100 × 10)`

`Percentual de INSS = 12 + 4 = 16%`

| **⚠️ Atenção**  Se a empresa não estiver enquadrada na desoneração, deixe o campo **Percentual da Receita Bruta para INSS** em branco. Enquanto ele estiver preenchido, o campo **Percentual de INSS** não poderá ser editado manualmente. |
| --- |

Essas informações impactam o Resumo da Folha, a GPS e o evento S-1280 do eSocial.

📚 Para saber mais, consulte os artigos [Como configurar a desoneração da folha](https://ajuda.sankhya.com.br/hc/pt-br/articles/14355845772311) e [Reoneração da folha: o que muda e como configurar](https://ajuda.sankhya.com.br/hc/pt-br/articles/31031737058839).

#### 5. Configurar as abas Contabilização e Processos de Terceiros

Essas abas permitem configurar regras de contabilização e informar processos que afetam as contribuições destinadas a terceiros.

**Aba Contabilização**

Configure os campos conforme as regras utilizadas pela empresa:

- **Provisionar Eventos pela Média:** define se os eventos são provisionados pela média.
- **Em caso de Férias Antecipadas, realizar a baixa antecipada:** define se a baixa da provisão deve ser realizada antecipadamente quando há férias antecipadas.

**Aba Processos de Terceiros**

Utilize essa aba quando a empresa possui processos administrativos ou judiciais que suspendem contribuições destinadas a terceiros.

1. Confirme se o processo administrativo ou judicial já foi cadastrado no sistema.
2. Acesse a aba **Processos de Terceiros**.
3. Informe o processo correspondente.

Os códigos de terceiros com contribuição suspensa são enviados ao eSocial no evento **S-1020 – Tabela de Lotações Tributárias**.

#### 6. Vincular o Registro Fiscal à empresa

Depois de configurar o Registro Fiscal, vincule-o ao cadastro da empresa para definir qual registro será utilizado no cálculo da folha.

A forma de utilização depende do parâmetro **Onde utiliza o Registro Fiscal? - FPREGFISCAL**.

- **Empresas:** o cálculo utiliza o Registro Fiscal da empresa;
- **Departamentos:** o cálculo utiliza o Registro Fiscal informado no departamento do colaborador.

Se a configuração estiver definida como **Departamentos**, confira se os departamentos utilizados pelos colaboradores possuem o Registro Fiscal correspondente.

📚 Para saber mais, consulte os artigos [Cadastro da Empresa para a Folha de Pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/37988711948311) e [Cadastro de Departamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/38506849096599).

#### 7. Conferir os encargos e consultar o histórico

Após concluir a configuração, valide os dados utilizados no cálculo da folha.

1. Calcule a folha da competência.
2. Confira os encargos no **Resumo da Folha**.
3. Consulte as informações correspondentes na **Central do eSocial**, quando aplicável.
4. Se encontrar divergências, confira os percentuais, os códigos fiscais, o enquadramento da empresa e o Registro Fiscal efetivamente utilizado no cálculo.

**Aba Histórico Registro Fiscal**

No fechamento da folha, o sistema grava na aba **Histórico Registro Fiscal** os valores do Registro Fiscal utilizados na competência, como percentuais de INSS, FGTS, RAT, FAP, terceiros e PIS sobre a folha.

Essa aba é destinada à consulta e não permite edição.

**Regra aplicada:** quando uma competência já possui histórico, os cálculos dessa competência utilizam os valores gravados nesse histórico, e não os valores atuais do Registro Fiscal.

| **🚨 Risco operacional**  Alterar o Registro Fiscal não recalcula automaticamente as competências já calculadas nem atualiza as competências já fechadas.   - **Competência calculada, mas ainda não fechada:** exclua o cálculo, calcule a folha novamente e confira os valores no Resumo da Folha. - **Competência já fechada:** os valores permanecem registrados no histórico e continuam sendo utilizados nos novos cálculos dessa competência.   Para evitar retrabalho e divergências, atualize o Registro Fiscal antes de calcular a folha da competência. |
| --- |

### Pontos de atenção

- **Vínculo com a empresa:** toda empresa deve ter um Registro Fiscal vinculado. Registros adicionais podem ser utilizados para departamentos, lotações tributárias e obras, conforme a configuração e a necessidade.
- **Atualização antes do cálculo:** revise o FAP, o RAT, os percentuais e os códigos fiscais antes de calcular a folha da competência.
- **Histórico das competências:** competências com histórico utilizam os valores registrados para aquele período. Alterar o cadastro atual não substitui automaticamente esses valores.
- **Desoneração da folha:** quando o percentual da receita bruta está preenchido, o sistema calcula o Percentual de INSS automaticamente. O Valor do INSS da Receita Bruta deve ser informado com base no valor apurado pela contabilidade.
- **Adicional do SENAI:** para empresas com FPAS 507 ou 833 e código de terceiros 0079, a Taxa Terceiros é ajustada automaticamente a partir da competência 05/2026, conforme a quantidade de empregados.
- **PIS sobre a folha:** confirme com a contabilidade se a empresa é contribuinte e quais informações devem ser preenchidas.
- **Enquadramento tributário:** valide as opções do Simples Nacional, a desoneração e as demais informações fiscais com o responsável tributário antes de salvar o cadastro.

### Perguntas frequentes

**1. Posso usar mais de um Registro Fiscal?**

Sim. Cada empresa deve ter um Registro Fiscal vinculado ao seu cadastro. Também podem ser cadastrados registros específicos para departamentos, lotações tributárias e obras, conforme a necessidade e a configuração do sistema. Para utilizar o Registro Fiscal por departamento, o parâmetro **FPREGFISCAL** deve estar configurado como **Departamentos**.

**2. Alterei o Registro Fiscal, mas o Resumo da Folha continua com os valores anteriores. O que fazer?**

Verifique a situação da competência:

- Se a folha foi calculada, mas ainda não foi fechada, exclua o cálculo, calcule novamente e confira o Resumo da Folha.
- Se a competência já foi fechada, os cálculos utilizam os valores gravados no histórico. A alteração do cadastro atual não substitui automaticamente esses valores.

**3. Recebi um novo FAP. Quando devo atualizar no sistema?**

Atualize o campo **Fator Acidentário de Prevenção (FAP)** antes de calcular a folha da competência em que o novo índice passa a valer. Confirme o índice aplicável à empresa com o responsável tributário.

**4. Por que o campo Percentual de INSS não permite alteração?**

Porque o campo **Percentual da Receita Bruta para INSS**, na aba **Desoneração da Folha**, está preenchido. Nessa situação, o sistema calcula automaticamente o Percentual de INSS.

Se a empresa não estiver enquadrada na desoneração, deixe o campo de percentual da receita bruta em branco, conforme a orientação da contabilidade.

**5. Onde informo o INSS sobre a receita bruta?**

Na aba Desoneração da Folha, no campo Valor do INSS da Receita Bruta, separadamente para a folha mensal e para o 13º salário. O sistema não calcula esse valor.

**6. Preciso alterar manualmente a Taxa Terceiros por causa do adicional do SENAI?**

Não, quando a empresa atende às condições previstas pelo sistema: FPAS 507 ou 833 e código de terceiros 0079. A partir da competência 05/2026, o ajuste é automático nas competências abertas e considera a quantidade de empregados da matriz e das filiais cadastradas no sistema.

**7. Quando devo revisar o Registro Fiscal?**

Sempre que houver alteração de FAP, mudança legal ou tributária, mudança de enquadramento (como desoneração ou Simples Nacional) ou orientação da contabilidade.
