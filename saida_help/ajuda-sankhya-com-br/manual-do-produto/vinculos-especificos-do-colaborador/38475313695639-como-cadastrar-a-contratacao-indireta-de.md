---
id: "38475313695639"
titulo: "Como cadastrar a contratação indireta de jovem aprendiz"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38475313695639-Como-cadastrar-a-contrata%C3%A7%C3%A3o-indireta-de-jovem-aprendiz"
trilha: "Manual do Produto > Pessoas+ > Colaboradores > Vínculos Específicos do Colaborador"
atualizado_em: "2026-10-02T15:05:02Z"
rotulos: ["Configuração", "Contrato", "ID: br.com.sankhya.cadastro.funcionarios", "eSocial", "FPCODFUNCPOREMP", "Configuração Funcionários", "Pessoal+", "Contratação indireta Aprendiz", "Menor Aprendiz"]
---

# Como cadastrar a contratação indireta de jovem aprendiz

**Módulo:** Pessoal+
**Caminho de acesso:** Pessoal+ > Cadastros > Configuração Funcionários 
**ID da Tela:** br.com.sankhya.cadastro.funcionarios

---

## Descrição e Usabilidade

A **contratação indireta de jovem aprendiz** ocorre quando o profissional é contratado por **entidades formadoras** (sem fins lucrativos ou entidades de prática desportiva), mas prestam serviço para a empresa responsável pelo cumprimento da cota de aprendizagem.

Essa configuração permite:

- Atender à legislação da aprendizagem profissional.
- Registrar corretamente o vínculo no sistema.
- Garantir o envio adequado das informações ao eSocial.

Nesse modelo, a empresa que recebe o aprendiz **não é a empregadora direta**, mas deve informar corretamente a relação com a entidade contratante.

### 1. Descrição da Funcionalidade

Ao configurar a contratação indireta:

- O vínculo do colaborador será definido como **Menor Aprendiz**.
- Será necessário informar os dados da **entidade empregadora**.
- O sistema ajustará o comportamento dos eventos enviados ao eSocial.

Nessa modalidade:

- A empresa responsável pela cota **não envia o evento S-2200** do aprendiz.
- Apenas informa o vínculo por meio do **CNPJ da entidade contratante no evento S-1005**.

### 2. Pré-requisitos

Antes de realizar o cadastro:

- Ter os dados completos da entidade empregadora.
- Possuir o CNPJ da entidade formadora ou de prática desportiva.
- Definir corretamente o vínculo como **Menor Aprendiz**.

### 3. Jornada de Uso

Siga os passos abaixo para realizar o cadastro:

**(1)** Na tela de cadastro de funcionários: **Configuração Funcionários** (Pessoal+ > Cadastros).

1. Clique no botão **Cadastrar Funcionário**.
2. Escolha se deseja fazer o cadastro utilizando um padrão ou sem padrão.
3. Preencha o **CP**F e o **Nome** do colaborador.
4. Selecione a **Empresa**.

**Importante:**

- O preenchimento da **Matrícula** depende da configuração do campo **Gera Matrícula do Funcionário automaticamente**, disponível na aba **Informações Gerais** da tela **Empresas**.
- O campo **Código** pode ser preenchido automaticamente ou manualmente, conforme a configuração definida no botão **Configuração da Tela**, opção **Numeração**.

  Ao ativar o parâmetro **Utiliza Sequência do Cód. Funcionário por Empresa? – FPCODFUNCPOREMP**, o sistema gera uma sequência de códigos exclusiva para cada empresa. Caso contrário, será única para todas as empresas.

![Imagem 1: Ao ativar o parâmetro Utiliza Sequência do Cód. Funcionário por Empresa? – FPCODFUNCPOREMP , o sistema gera uma…](https://ajuda.sankhya.com.br/hc/article_attachments/38475495770007)

**(2)**  Preencha normalmente **todas as abas** e dê atenção especial aos campos abaixo.

- Aba **Admissão**:

  - **Código de Categoria para o eSocial**: 103 - Empregado Aprendiz;
  - **Situação no eSocial**: Oficial (S-2200/S-2300);
  - **Vínculo**: 55 - Menor Aprendiz;
  - **Data Término do Contrato**;
  - **Tabela de Categoria [FGTS]**: 07 Menor aprendiz.

![Imagem 2: Tabela de Categoria (FGTS) : 07 Menor aprendiz.](https://ajuda.sankhya.com.br/hc/article_attachments/38476003997975)

- Aba **Contrato**:

  - Marque a opção **Contratação indireta para Aprendiz**;
  - Preencha o **Tipo de Inscrição** e **Número de Inscrição** da instituição empregadora;
  - Se necessário, informe o **CNPJ Entidade Prática** onde serão realizadas as atividades práticas.

![Imagem 3: Se necessário, informe o CNPJ Entidade Prática onde serão realizadas as atividades práticas.](https://ajuda.sankhya.com.br/hc/article_attachments/38477233113751)

**(3)** Salve o cadastro.

### 4. Pontos de Atenção

- Na contratação indireta, é obrigatório informar os dados completos da **instituição empregadora**.
- O estabelecimento que cumpre a cota **não envia o evento S-2200** do aprendiz.
- Ele apenas informa o **CNPJ da entidade contratante no evento S-1005**.

### 5. Dicas de Usabilidade

- Valide previamente os dados da entidade formadora.
- Revise o vínculo e categoria antes de salvar o cadastro.
- Garanta que o contrato esteja alinhado com a legislação de aprendizagem.
- Realize um cálculo teste para validar os encargos e eventos gerados.

## Perguntas Frequentes (FAQ)

**1. Quem é o empregador do jovem aprendiz na contratação indireta?**

A entidade formadora ou entidade de prática desportiva.

**2. A empresa deve enviar o evento S-2200?**

Não. Na contratação indireta, o envio não é responsabilidade da empresa que cumpre a cota.

**3. O que a empresa deve informar ao eSocial?**

Deve informar o **CNPJ da entidade contratante no evento S-1005**.

**4. Posso cadastrar como aprendiz sem marcar a contratação indireta?**

Sim, mas apenas quando a empresa for a empregadora direta.

## Artigos relacionados

- [Cadastro do Funcionário](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639)
