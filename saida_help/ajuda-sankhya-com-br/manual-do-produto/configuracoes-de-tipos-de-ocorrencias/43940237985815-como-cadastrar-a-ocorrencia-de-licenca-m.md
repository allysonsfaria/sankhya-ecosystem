---
id: "43940237985815"
titulo: "Como cadastrar a ocorrência de licença-maternidade"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43940237985815-Como-cadastrar-a-ocorr%C3%AAncia-de-licen%C3%A7a-maternidade"
trilha: "Manual do Produto > Pessoas+ > Afastamentos e Ocorrências > Configurações de Tipos de Ocorrências"
atualizado_em: "2026-10-09T17:34:29Z"
rotulos: ["Ocorrências", "br.com.sankhya.rh.LancamentoOcorrencias", "FPCODHISESTABIL", "FPOCOPRORROGADO", "Licença Maternidade", "Licença Maternidade Cidadã", "FPPROVISLICGEST"]
---

# Como cadastrar a ocorrência de licença-maternidade

**Módulo:** Pessoal+
**Caminho de Acesso:** Pessoal+ > Rotinas Folha > Ocorrências > Cadastro
**ID da Tela:** br.com.sankhya.rh.LancamentoOcorrencias

---

### O que é e para que serve

A ocorrência de **licença-maternidade** deve ser cadastrada uma única vez na aba **Cadastro** da tela **Ocorrências**. Depois do cadastro, ela fica disponível na aba **Lançamento** para registrar o afastamento das funcionárias.

É possível cadastrar ocorrências diferentes conforme a situação atendida pela empresa, como licença-maternidade de 120 dias, prorrogação pelo Programa Empresa Cidadã, adoção, aborto não criminoso e antecipação ou prorrogação por atestado.

### Antes de começar

Confira os seguintes requisitos antes de cadastrar a ocorrência:

- Você precisa ter permissão para acessar e alterar a aba **Cadastro** da tela **Ocorrências**.

  Essa liberação é feita na tela **Acessos** (Configurações > Controle de Acesso), pelo administrador do sistema.
- Os motivos de afastamento do eSocial utilizados pela empresa devem estar disponíveis e vigentes.
- Os códigos de **FGTS**, **RAIS** e **Causa** utilizados na ocorrência devem estar cadastrados na tela **Código de Afastamento** (Pessoal+ > Cadastros).
- Se a empresa utilizar o controle de estabilidade da gestante, verifique a configuração da ocorrência de estabilidade cujo código deve ser informado no parâmetro **Cód. Hist. Ocorr. para Estabilidade -** **FPCODHISESTABIL**.
- Se a empresa utilizar os parâmetros **Dias afastados altera fim do período concessivo -** **FPOCOPRORROGADO** ou **Gera provisão para Licença Gestante - FPPROVISLICGEST**, confira também essas configurações antes de cadastrar a ocorrência.

  | **⚠️** **Atenção**  A ocorrência **LICENCA MATERNIDADE - ADOÇÃO** pode já existir na sua base porque é criada automaticamente por uma atualização do sistema. Confira a lista de ocorrências antes de criar uma nova. |
  | --- |

### Cadastrar a ocorrência

1. Acesse a tela **Ocorrências** (Pessoal+ > Rotinas Folha).
2. Informe a **Empresa** e o **Tipo de Filtro** e clique em **Pesquisar**.
3. Selecione a aba **Cadastro**.
4. Clique em **Adicionar novo tipo de ocorrência**.

   Ao criar uma ocorrência, o sistema inicia o cadastro com o tipo **Não é afastamento** e as propriedades desmarcadas.
5. Na seção **Geral**, selecione o **Tipo de afastamento**, selecione a opção correspondente à situação que será cadastrada:

   | Situação | Tipo de afastamento | Motivo eSocial |
   | --- | --- | --- |
   | Licença-maternidade de 120 dias | **Licença maternidade** | **17** |
   | Prorrogação de 60 dias – Empresa Cidadã | **Licença Maternidade Cidadã** | **18** |
   | Aborto não criminoso | **Licença maternidade** | **19** |
   | Adoção ou cônjuge sobrevivente | **Licença maternidade** | **20** |
   | Antecipação ou prorrogação por atestado | **Licença maternidade** | **35** |

   | **⚠️** **Atenção**  Utilize **Licença Maternidade Cidadã** somente para a prorrogação de 60 dias do Programa Empresa Cidadã. Para as demais situações da tabela, utilize **Licença maternidade**. |
   | --- |
6. No campo **Descrição**, informe o nome da ocorrência.

   Essa é a descrição que será apresentada na lista de ocorrências no momento do lançamento.

   O campo permite até **40 caracteres**.

   Sugestões de descrição:

   - `LICENCA MATERNIDADE`
   - `LIC MATERNIDADE CIDADA`
   - `LIC MATERNIDADE ABORTO`
   - `LICENCA MATERNIDADE - ADOÇÃO`
   - `LIC MATERNIDADE ATESTADO`
7. No campo **Descrição eSocial**, pesquise e selecione o motivo correspondente à situação.

   A pesquisa apresenta somente os motivos que ainda estão vigentes no eSocial.

   | **⚠️** **Atenção**  Se o motivo configurado tiver sido descontinuado pelo eSocial, ele não deverá ser utilizado para novos lançamentos. Se o sistema apresentar a mensagem **"Motivo de afastamento p/ eSocial da ocorrência escolhida foi descontinuado pelo eSocial"**, selecione um motivo válido. |
   | --- |
8. Preencha os campos:

   - **Descrição FGTS**
   - **Descrição RAIS**
   - **Descrição Causa**

   Para isso, clique na lupa e selecione os códigos correspondentes cadastrados previamente na tela **Código de Afastamento** (Pessoal+ > Cadastros).

   Esses códigos são utilizados pelo sistema nos processos que dependem das informações de afastamento da funcionária.
9. Marque **Aparece no Portal RH** caso a ocorrência possa ser solicitada pelos colaboradores via Portal RH/App Pessoas+.

   Para exigir o envio de um documento, marque também **Necessita de anexo no Portal RH**.

   | **⚠️** **Atenção**  Quando **Necessita de anexo no Portal RH** estiver marcado, a ocorrência não será apresentada quando várias funcionárias forem selecionadas ao mesmo tempo. Nesse caso, faça o lançamento de uma funcionária por vez. |
   | --- |
10. Depois de preencher os dados, configure as **Propriedades da Ocorrência** conforme as orientações a seguir.

    As propriedades determinam como o sistema tratará a ocorrência em outros processos.

    Para uma ocorrência de licença-maternidade, a configuração padrão deve manter a maior parte das propriedades desmarcadas.

    | Propriedade | Configuração para licença-maternidade |
    | --- | --- |
    | **Indenização de Estabilidade** | Opcional. Se a empresa optar por controlar a estabilidade diretamente pela ocorrência de licença-maternidade, marque e informe a quantidade em **Quantos Meses de Estabilidade?**.  Os meses informados são contados a partir do **fim da licença**.  📚Para mais detalhes sobre essa marcação, acesse [Propriedades da ocorrência: o que cada opção faz](https://ajuda.sankhya.com.br/hc/pt-br/articles/42544737715479).  Além disso, o sistema não calcula automaticamente a estabilidade de cinco meses após o parto. Para utilizar a estabilidade no cálculo da rescisão, acesse [Como cadastrar ocorrências com estabilidade?](https://ajuda.sankhya.com.br/hc/pt-br/articles/42546913948055). |
    | **Baixa na Provisão** | Desmarcado. |
    | **Abate no Aviso Prévio** | Desmarcado. |
    | **Falta** | **Desmarcado.** Se marcado, a licença será tratada como falta, podendo afetar o DSR e o cálculo de ponto. |
    | **Absenteísmo** | **Marcado.** É o padrão para licença-maternidade. |
    | **Gera Ocorrência AFDT** | Desmarcado. |
    | **Tem Direito de Adiantamento** | Desmarcado. |
    | **Quita Férias em Licença Remunerada** | **Desmarcado.** A licença-maternidade não elimina o direito às férias. |
    | **Necessita de anexo no Portal RH** | Marque se a empresa exigir certidão ou atestado no lançamento pelo Portal RH. |
    | **Ocorrência de reajuste salarial sindical** | Desmarcado. |
    | **Quita Férias por Afastamentos - Art. 133 CLT** | **Desmarcado.** |
    | **Deduz dias de Aviso prévio lei 12.506/2011** | Desmarcado. Essa opção é destinada a situações de auxílio-doença. |

    | **⚠️** **Atenção**  A opção **Reduz dias Trabalhados** não aparece para o tipo **Licença-maternidade**, porque o próprio tipo de afastamento já considera a redução dos dias trabalhados. |
    | --- |
11. Em seguida, clique em **Salvar**.
12. Confirme a pergunta **"Tem certeza que deseja salvar as alterações?"**.

    A mensagem **"Ocorrência salva com sucesso!"** confirma o cadastro.

| ℹ️ **Configurações complementares**  Alguns parâmetros podem alterar o comportamento da licença em processos específicos.   - **Dias afastados altera fim do período concessivo - FPOCOPRORROGADO**  Quando habilitado, os dias de licença estendem o prazo para a funcionária usufruir as férias. - **Provisão de 13º na licença gestante - FPPROVISLICGEST**  Quando habilitado, os dias de licença não retiram avos de 13º no cálculo da provisão. |
| --- |

### Pontos de Atenção

- **O motivo de afastamento não aparece na pesquisa**

  A pesquisa de **Descrição eSocial** apresenta somente os motivos vigentes.

  Confira se o motivo necessário ainda é aceito pelo eSocial e se o sistema está atualizado.
- **O código de FGTS ou RAIS não aparece na pesquisa**

  Os códigos são obtidos do cadastro **Códigos de Afastamento**.

  Cadastre o código correspondente nessa tela e volte ao cadastro da ocorrência para realizar a pesquisa.
- **A ocorrência desaparece quando várias funcionárias são selecionadas**

  Verifique se a propriedade **Necessita de anexo no Portal RH** está marcada.

  Quando essa opção exige anexo, a ocorrência deve ser lançada para uma funcionária por vez.
- **A licença está fazendo a funcionária perder o DSR**

  Verifique se a propriedade **Falta** está marcada.

  Para licença-maternidade, essa opção deve permanecer desmarcada.

  Depois de corrigir a configuração, recalcule a folha.
- **As férias da funcionária foram quitadas**

  Verifique as propriedades:

  - **Quita Férias em Licença Remunerada**;
  - **Quita Férias por Afastamentos - Art. 133 CLT**.

  Para licença-maternidade, essas opções devem permanecer desmarcadas.
- **O sistema apresenta erro ao salvar o cadastro**

  Se ocorrer uma falha ao salvar, revise os campos preenchidos e tente novamente.

  Se o problema persistir, abra um chamado para análise.

### Perguntas Frequentes

**1. Preciso criar uma ocorrência diferente para cada tipo de licença-maternidade?**

Sim, quando sua empresa precisa tratar situações diferentes. Por exemplo, é possível ter uma ocorrência para a licença de 120 dias e outra para a prorrogação de 60 dias do Programa Empresa Cidadã.

**2. Qual tipo de afastamento devo usar para a licença-maternidade?**

Para a licença-maternidade de 120 dias, aborto não criminoso, adoção ou antecipação/prorrogação por atestado, utilize **Licença maternidade**.

Para a prorrogação de 60 dias do Programa Empresa Cidadã, utilize **Licença Maternidade Cidadã**.

**3. Posso usar qualquer motivo do eSocial?**

Não. O motivo deve corresponder à situação da ocorrência e estar vigente no eSocial.

**4. Por que o código de FGTS ou RAIS não aparece?**

Os códigos são pesquisados no cadastro **Códigos de Afastamento**. Se não estiverem cadastrados, não aparecerão na pesquisa da ocorrência.

**5. Preciso marcar a opção Falta?**

Não. Para licença-maternidade, **Falta** deve permanecer desmarcada.

**6. Como configurar a estabilidade da gestante?**

Você pode utilizar uma ocorrência específica de estabilidade vinculada ao parâmetro **FPCODHISESTABIL** ou marcar **Indenização de Estabilidade** na própria ocorrência de licença-maternidade.

**7. A licença-maternidade faz a funcionária perder as férias?**

Não. Por isso, as propriedades **Quita Férias em Licença Remunerada** e **Quita Férias por Afastamentos - Art. 133 CLT** devem permanecer desmarcadas.

### Artigos Relacionados

- [Como lançar a ocorrência de licença-maternidade para uma funcionária](https://ajuda.sankhya.com.br/hc/pt-br/articles/43877669306007)
- [Como cadastrar ocorrências com estabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/42546913948055)
- [Cadastro de Códigos de Afastamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/13729923854487)
- [Portal RH](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108433)
