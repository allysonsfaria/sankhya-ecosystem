---
id: "38911679393175"
titulo: "Como incluir ou alterar a carga horária do colaborador"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38911679393175-Como-incluir-ou-alterar-a-carga-hor%C3%A1ria-do-colaborador"
trilha: "Manual do Produto > Pessoas+ > Colaboradores > Manutenção Cadastral e Continuidade do Vínculo"
atualizado_em: "2026-10-02T15:19:21Z"
rotulos: ["Histórico", "Carga Horária", "br.com.sankhya.cadastro.funcionarios", "eSocial", "Configuração Funcionários", "Cadastro", "Histórico de Carga Horária", "Pessoal+"]
---

# Como incluir ou alterar a carga horária do colaborador

**Módulo:** Pessoal+
**Caminho de Acesso:** Pessoal+ > Cadastros > Configuração Funcionários
**ID da Tela:** br.com.sankhya.cadastro.funcionarios

---

## Descrição e Usabilidade

### 1. Descrição da Funcionalidade

A **Carga Horária** define a jornada de trabalho do colaborador e é utilizada pelo sistema para controle de ponto, cálculo de horas trabalhadas, atrasos, horas extras e envio das informações ao **eSocial**.

No cadastro do colaborador, a carga horária pode ser definida:

- **No momento da admissão**, durante o cadastro do funcionário;
- **Posteriormente**, por meio da **aba Histórico de Carga Horária**, que registra todas as alterações realizadas na jornada do colaborador.

Após definida, o campo **Carga Horária** na aba **Configurações de Ponto** passa a ser preenchido automaticamente com base nas informações registradas no histórico.

### 2. Pré-requisitos

Antes de incluir ou alterar a carga horária de um colaborador, verifique:

- Se a **Carga Horária já está cadastrada** na tela Carga Horária (Pessoal+ > Cadastros).
- Se o colaborador **não está marcado como Dispensado do Ponto**.
- Se a **data informada no histórico não é anterior à data de admissão**.

### 3. Jornada de Uso

#### 3.1 Informar carga horária em novas admissões

[GIF animado: Imagem 1: 3.1 Informar carga horária em novas admissões](https://ajuda.sankhya.com.br/hc/article_attachments/38912332451863)

Para novos colaboradores, a carga horária deve ser definida durante o cadastro de admissão.

1. Na tela **Configuração Funcionários**, durante o processo de admissão, vá até a aba **Configurações de Ponto**.
2. No campo **Carga Horária**, selecione a jornada correspondente ao colaborador.
3. Salve o cadastro.

Após a inclusão, o sistema registra automaticamente essa informação na **aba Histórico de Carga Horária.**

⚠️ Se a opção **Dispensado do Ponto** estiver marcada, o campo **Carga Horária** ficará **bloqueado para edição**.

#### 3.2 Alterar carga horária de colaboradores já cadastrados

[GIF animado: Imagem 2: 3.2 Alterar carga horária de colaboradores já cadastrados](https://ajuda.sankhya.com.br/hc/article_attachments/38912361761175)

Para colaboradores com admissões já registradas, a inclusão ou alteração da carga horária deve ser realizada na **aba Histórico de Carga Horária**.

Essa aba registra todas as mudanças realizadas na jornada do colaborador.

1. Na tela **Configuração Funcionários**, abra a aba **Histórico de Carga Horária**.
2. Clique em **Cadastrar Histórico de Carga Horária**.
3. Preencha os campos:

   - **Data**
   - **Carga Horária**
   - **Data de Início**
   - **Data de Folga**
4. Clique em **Salvar**.

Após salvar, a nova carga horária será aplicada conforme a data informada.

#### 3.3 Preenchimento automático do histórico

A aba **Histórico de Carga Horária** pode ser preenchida automaticamente nas seguintes situações:

- Inclusão de carga horária na **Requisição de Admissão**;
- Alteração pela **Requisição de Alteração Temporária de Carga Horária**;
- Cadastro ou alteração na **tela Padrão de Cadastro de Funcionários**;
- Importação realizada pelo **Importador de Folha**;
- Inclusão realizada na aba **Configurações de Ponto**.

### 4. Pontos de Atenção

Para o cadastro de carga horária histórica, o sistema aplica as seguintes regras:

- Não é permitido informar **data anterior à admissão do colaborador**.
- Se a carga horária for cadastrada **na mesma data da admissão**, o sistema atualiza automaticamente o campo **Carga Horária** na aba **Configurações de Ponto**.
- Se a inclusão for realizada **após a data de admissão**, a nova carga horária será aplicada **na data informada para início**.

Além disso:

- A alteração da carga horária impacta diretamente o **controle de ponto e cálculos de jornada**.
- Recomenda-se registrar corretamente as datas de início das alterações para evitar inconsistências nos cálculos.

### 5. Dicas de Usabilidade

- Utilize o **Histórico de Carga Horária** sempre que houver mudança na jornada do colaborador.
- Evite alterar diretamente a carga horária sem registrar o histórico, pois isso pode comprometer rastreabilidade das alterações.
- Revise as datas informadas antes de salvar para garantir a aplicação correta da jornada.

## Artigos Relacionados

- [Cadastro de Funcionários](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639)
- [Cadastro de Carga Horária](https://ajuda.sankhya.com.br/hc/pt-br/articles/38858116404503)
- [Requisição de Alteração Temporária de Carga Horária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360059085273-Requisi%C3%A7%C3%B5es#Altera%C3%A7%C3%A3oTempor%C3%A1riadeCargaHor%C3%A1ria)
- [Requisição de Admissão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360059085273-Requisi%C3%A7%C3%B5es#admissao)
