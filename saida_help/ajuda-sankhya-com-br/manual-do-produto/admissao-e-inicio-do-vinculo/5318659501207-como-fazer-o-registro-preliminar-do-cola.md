---
id: "5318659501207"
titulo: "Como fazer o registro preliminar do colaborador"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/5318659501207-Como-fazer-o-registro-preliminar-do-colaborador"
trilha: "Manual do Produto > Pessoas+ > Colaboradores > Admissão e Início do Vínculo"
atualizado_em: "2026-10-02T15:04:16Z"
rotulos: ["Configuração", "Admissão", "br.com.sankhya.rh.RegistroPreliminar", "Registro Preliminar", "eSocial", "FPUTILIZACBO", "Cadastro", "Cadastro de Registro Preliminar", "Pessoal+"]
---

# Como fazer o registro preliminar do colaborador

**Módulo:** Pessoal+
**Caminho de Acesso:** Pessoal+ > Cadastros
**Versão Mínima:** 4.9
**ID da Tela:** br.com.sankhya.rh.RegistroPreliminar

---

## Descrição e Usabilidade

### 1. Descrição da Funcionalidade

O **Registro Preliminar (S-2190)** é um evento opcional do eSocial utilizado quando a empresa ainda não dispõe de todas as informações necessárias para realizar o cadastro completo do trabalhador e enviar os eventos **S-2200** ou **S-2300**.

O registro preliminar permite informar os dados disponíveis no momento da admissão ou do início da prestação de serviços. Posteriormente, o cadastro completo do trabalhador deve ser realizado conforme o processo de admissão aplicável.

Nesta tela, podem ser cadastradas informações de trabalhadores que ainda não possuem o cadastro completo no **Pessoas+**. Após a conclusão do processo de contratação, os dados poderão ser utilizados no cadastro do funcionário, quando aplicável.

### 2. Pré-requisitos

- Ter acesso à tela **Registro Preliminar** (Pessoal+ > Cadastros). Essa liberação é feita na tela **Acessos** (Configurações > Controle de Acesso), pelo administrador do sistema.
- Possuir os dados necessários para o preenchimento do registro, conforme os campos disponíveis na tela.
- Para o envio ao eSocial, as informações devem estar preenchidas de acordo com as regras aplicáveis ao evento **S-2190** **-** **Registro Preliminar do Trabalhador**.

### 3. Jornada de Uso

![Imagem 1: 3. Jornada de Uso](https://ajuda.sankhya.com.br/hc/article_attachments/21574171476375)

#### Cadastrar o Registro Preliminar

1. Acesse a tela **Registro Preliminar** (Pessoal+ > Cadastros).
2. Informe a **Empresa** em que o trabalhador será admitido.
3. Preencha os dados do trabalhador:

   - **Matrícula**;
   - **Nome do Funcionário**;
   - **CPF**;
   - **Data de Nascimento**.

   | 💡**Dica:**  A **Matrícula** pode ser gerada automaticamente se no [**cadastro da Empresa**](https://ajuda.sankhya.com.br/hc/pt-br/articles/37988711948311), aba **Informações Gerais**, o campo **Gera Matrícula do Funcionário Automaticamente** estiver com a opção **Gera Matrícula do Funcionário Automaticamente com o seu código** ou **Gera Matrícula do Funcionário Automaticamente (Matriz/Filial)** selecionada. |
   | --- |
4. Informe a **Data de Admissão**, correspondente à data em que o trabalhador iniciará suas atividades na empresa.

   | **⚠️** **Atenção**  Caso a data seja alterada posteriormente no cadastro do funcionário, a **Data de Admissão** do registro preliminar também será alterada automaticamente. |
   | --- |
5. Selecione o **Código da Categoria para o eSocial**, conforme a categoria do trabalhador.

   | **⚠️** **Atenção**  Ao selecionar a categoria **103 - Empregado Aprendiz**, no campo **Vínculo** serão apresentadas somente as opções correspondentes a prazo determinado. |
   | --- |
6. Selecione o **Vínculo** correspondente ao trabalhador.

   As opções disponíveis são:

   - 02 - Estagiário;
   - 10 - Prazo indeterminado pessoa jurídica;
   - 15 - Prazo indeterminado pessoa física;
   - 20 - Prazo indeterminado rural (jurídica);
   - 25 - Prazo indeterminado rural (física);
   - 30 - Regime jurídico único;
   - 35 - Público não efetivo;
   - 40 - Funcionário avulso;
   - 50 - Contrato temporário;
   - 55 - Menor aprendiz;
   - 60 - Prazo determinado urbano (jurídica);
   - 65 - Prazo determinado urbano (física);
   - 70 - Prazo determinado rural (jurídica);
   - 75 - Prazo determinado rural (física);
   - 80 - Diretor sem vínculo empregatício;
   - 90 - Autônomo;
   - 99 - Pensionista.
7. Informe o **Código do Cargo do Funcionário** ou o **Código da Função do Funcionário**, conforme a configuração do parâmetro **Onde Utiliza o CBO? - FPUTILIZACBO**:

   - **Cargo:** o CBO será relacionado ao cargo;
   - **Função:** o CBO será relacionado à função.
8. Quando aplicável, informe a **Data Término Contrato**; geralmente esta data corresponde a data final do período de experiência.
9. Selecione a **Natureza da Atividade**:

   - **Urbano**;
   - **Rural**.
10. Selecione o **"Tipo de Salário"** conforme as opções abaixo:
    - Mensal;
    - Quinzenal;
    - Semanal;
    - Diarista;
    - Horista;
    - Tarefa.
11. Preencha o **Salário Base.**

    | **⚠️** **Atenção**  Para trabalhador com categoria de professor, informe o valor no campo **Salário Professor**. |
    | --- |
12. Clique em  ![Imagem 2: Clique em Salvar (F7) .](https://ajuda.sankhya.com.br/hc/article_attachments/21572612412823) **Salvar [F7]**.

#### Enviar o S-2190 ao eSocial

Após salvar o Registro Preliminar, realize o envio do evento **S-2190** **-** **Registro Preliminar do Trabalhador** ao eSocial conforme o processo de envio dos eventos do Pessoal+.

| **⚠️** **Atenção**  O Registro Preliminar é utilizado como informação inicial. Após a conclusão do processo de admissão ou contratação, realize o cadastro completo do trabalhador e o envio do evento correspondente, conforme o vínculo. |
| --- |

### 4. Pontos de Atenção

- O **S-2190** é um evento opcional e deve ser utilizado quando ainda não houver todas as informações necessárias para o envio do cadastro completo do trabalhador.
- Confira principalmente **CPF, Data de Nascimento, Data de Admissão, Categoria e Vínculo** antes de salvar e enviar o registro.
- A **Data de Término Contrato** deve ser preenchida quando aplicável ao vínculo informado.
- A disponibilidade dos campos **Código do Cargo do Funcionário** e **Código da Função do Funcionário** depende da configuração do parâmetro **FPUTILIZACBO**.
- O cadastro do Registro Preliminar não substitui o cadastro completo do trabalhador quando este for necessário para o vínculo.
- Se o colaborador desistir da admissão antes de ela ser efetivada (pelos eventos S-2200 ou S-2300), e o evento S-2190 já tiver sido enviado ao eSocial, é necessário excluir esse evento no eSocial, não é suficiente apenas descartar ou excluir o registro no sistema, já que o eSocial já recebeu essa informação e a admissão não será concretizada.

### 5. Dicas de Usabilidade

- Confira os dados do trabalhador antes do envio para evitar inconsistências no eSocial.
- Após concluir a contratação, mantenha o cadastro do trabalhador atualizado com as informações completas exigidas para o vínculo.

## Perguntas Frequentes (FAQ)

**1. Quando devo utilizar o Registro Preliminar (S-2190)?**

Utilize o Registro Preliminar quando a empresa ainda não possuir todas as informações necessárias para realizar o cadastro completo do trabalhador e enviar os eventos **S-2200** ou **S-2300**.

**2. O Registro Preliminar substitui o cadastro do funcionário?**

Não. O Registro Preliminar é utilizado como informação inicial. Após a conclusão do processo de contratação, deve ser realizado o cadastro completo do trabalhador, quando aplicável.

**3. Por que o campo Código do Cargo não aparece?**

A exibição dos campos relacionados a cargo e função depende da configuração do parâmetro **Onde Utiliza o CBO? - FPUTILIZACBO**. Quando configurado para **Cargo**, será apresentado o campo de cargo; quando configurado para **Função**, será apresentado o campo de função.

**4. A matrícula pode ser gerada automaticamente?**

Sim. A matrícula pode ser gerada automaticamente conforme a configuração realizada no cadastro da empresa, em **Informações Gerais**, no campo **Gera Matrícula do Funcionário Automaticamente**.

## Artigos Relacionados

- [Configuração Funcionários](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639)
- [Central do eSocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/7064222145175)
