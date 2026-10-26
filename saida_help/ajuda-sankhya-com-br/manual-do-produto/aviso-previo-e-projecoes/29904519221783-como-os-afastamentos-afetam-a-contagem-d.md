---
id: "29904519221783"
titulo: "Como os afastamentos afetam a contagem do aviso prévio"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/29904519221783-Como-os-afastamentos-afetam-a-contagem-do-aviso-pr%C3%A9vio"
trilha: "Manual do Produto > Pessoas+ > Rescisão > Aviso Prévio e Projeções"
atualizado_em: "2026-10-02T15:44:37Z"
rotulos: ["Configuração", "Folha de Pagamento", "Aviso Prévio", "Pessoal+", "Legislação Trabalhista"]
---

# Como os afastamentos afetam a contagem do aviso prévio

**Módulo:** Pessoal+
**Caminho de Acesso:** Pessoal+ > Rotinas Folha > Ocorrências
**ID da Tela:** br.com.sankhya.rh.LancamentoOcorrencias

---

## Descrição e Usabilidade

### 1. Descrição da Funcionalidade

A Lei nº 12.506/2011 estabelece que o aviso prévio pode ser acrescido de **3 dias por ano completo de serviço**, limitado a 90 dias.

Em determinadas situações, períodos de afastamento do colaborador não devem ser considerados na contagem do aviso prévio. No Pessoal+, essa regra é controlada pela propriedade **Deduz dias de Aviso prévio lei 12.506/2011**, configurada no [**cadastro do tipo de ocorrência**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044610494).

Quando essa propriedade está habilitada, o sistema considera os dias do afastamento na contagem do aviso prévio e realiza o ajuste automaticamente no cálculo.

### 2. Pré-requisitos

- Permissão de acesso à tela **Ocorrências** (Pessoal+ > Rotinas Folha). Essa liberação é feita na tela **Acessos** (Configurações > Controle de Acesso), pelo administrador do sistema.
- Tipo de ocorrência de afastamento previamente cadastrado.
- Propriedade **Deduz dias de Aviso prévio lei 12.506/2011** habilitada para o tipo de ocorrência.

### 3. Jornada de Uso

![Imagem 1: 3. Jornada de Uso](https://ajuda.sankhya.com.br/hc/article_attachments/29904686811927)

1. Acesse a tela **Ocorrências** (Pessoal+ > Rotinas Folha).
2. Informe a **Empresa** e o **Tipo de Filtro** e clique em **Pesquisar.**
3. Selecione a aba **Cadastro**.
4. Localize e selecione o tipo de ocorrência de afastamento que deverá interferir na contagem do aviso prévio.
5. Na seção **Propriedades da Ocorrência**, marque **Deduz dias de Aviso prévio lei 12.506/2011**.
6. Clique em **Confirmar alterações**.

   Após essa configuração, ao informar a **Data início do Aviso Prévio** no [cadastro do aviso prévio](https://ajuda.sankhya.com.br/hc/pt-br/articles/38693057310487) ou no cálculo da rescisão, o sistema verifica os afastamentos do colaborador que possuem essa propriedade habilitada e ajusta a contagem do aviso prévio.

   - Cadastro aviso prévio:

     ![Imagem 2: Cadastro aviso prévio:](https://ajuda.sankhya.com.br/hc/article_attachments/42315307060887)
   - Cálculo rescisão:

     ![Imagem 3: Cálculo rescisão:](https://ajuda.sankhya.com.br/hc/article_attachments/42315343927575)

     O ajuste é realizado automaticamente pelo sistema, sem necessidade de lançamento manual dos dias a serem deduzidos.

### 5. Pontos de Atenção

- A dedução não é aplicada a todos os afastamentos automaticamente. O tipo de ocorrência precisa estar configurado com a propriedade **Deduz dias de Aviso prévio lei 12.506/2011**.
- A configuração é feita no **tipo de ocorrência**, portanto, afeta os lançamentos realizados com esse tipo.
- Confira a configuração da ocorrência antes de calcular o aviso prévio ou a rescisão.
- A propriedade está relacionada especificamente à aplicação da **Lei nº 12.506/2011** na contagem do aviso prévio.

### 6. Dicas de Usabilidade

- Utilize uma descrição clara para os tipos de ocorrência que possuem essa propriedade habilitada.
- Antes de calcular uma rescisão, confira se os afastamentos do colaborador estão corretamente lançados e configurados.
- Se o aviso prévio apresentar uma quantidade de dias diferente da esperada, verifique as ocorrências do colaborador e a configuração da propriedade **Deduz dias de Aviso prévio lei 12.506/2011**.

## Perguntas Frequentes (FAQ)

**1. Todos os afastamentos são descontados da contagem do aviso prévio?**

Não. A dedução depende da configuração do tipo de ocorrência. Somente as ocorrências com a propriedade **Deduz dias de Aviso prévio lei 12.506/2011** habilitada são consideradas para essa regra.

**2. Preciso informar manualmente os dias que devem ser descontados?**

Não. Após a configuração da ocorrência, o sistema realiza o ajuste automaticamente ao informar a **Data início do Aviso Prévio**.

**3. Onde configuro essa regra?**

No cadastro do tipo de ocorrência, em **Pessoal+ > Rotinas Folha > Ocorrências > Cadastro**, na seção **Propriedades da Ocorrência**.

**4. A configuração vale para todos os afastamentos?**

Não. A propriedade é configurada individualmente em cada tipo de ocorrência.

**5. Em quais rotinas o sistema considera essa configuração?**

A validação ocorre ao informar a **Data início do Aviso Prévio** no cadastro do aviso prévio ou no cálculo da rescisão.
