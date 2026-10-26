---
id: "25948428448535"
titulo: "Como lançar o movimento do autônomo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/25948428448535-Como-lan%C3%A7ar-o-movimento-do-aut%C3%B4nomo"
trilha: "Manual do Produto > Pessoas+ > Contratos Especiais > Contrato Autônomo"
atualizado_em: "2026-10-02T15:21:27Z"
rotulos: ["Eventos", "Cálculo", "eSocial", "Folha de Pagamento", "br.com.sankhya.rh.MovimentacoesFolha", "Autônomo", "Pessoal+", "Lançamento de Movimento para Cálculo de Autônomo"]
---

# Como lançar o movimento do autônomo

**Módulo:**Pessoal+
**Caminho de Acesso:** Pessoal+ > Rotinas Folha
**ID da Tela:**br.com.sankhya.rh.MovimentacoesFolha

---

## Descrição e Usabilidade

### 1. Descrição da Funcionalidade

A rotina **Lançamento de Movimento** permite registrar eventos para o cálculo da folha de um autônomo.

Para o cálculo de **RPA (Recibo de Pagamento Autônomo)**, os eventos podem ser lançados previamente nessa rotina e, posteriormente, considerados no cálculo do RPA.

Essa opção é útil quando os valores precisam ser registrados antes da realização do cálculo.

Também é possível lançar eventos de honorários diretamente na tela **Cálculos**, pelo botão **Honorários** disponível no cálculo do RPA.

Escolha apenas uma das formas de lançamento para evitar que o mesmo valor seja considerado duas vezes.

### 2. Pré-requisitos

- Ter acesso à rotina **Lançamento de Movimento**. Essa liberação é feita na tela **Acessos** (Configurações > Controle de Acesso), pelo administrador do sistema.
- Ter um autônomo cadastrado na tela **Configuração Funcionários**.
- O evento utilizado no lançamento deve estar configurado com a identificação 200 - Outros Eventos Suplementares.
- A folha da referência não pode estar calculada para o autônomo que receberá o lançamento.

### 3. Jornada de Uso

**Configurar o evento utilizado no lançamento**

Para que um evento utilizado no RPA seja considerado corretamente, ele deve possuir a identificação adequada.

Para eventos de honorários e outros eventos utilizados no cálculo, configure a **Identificação do evento** na aba **Básico** com a opção **200 - Outros Eventos Suplementares.**

![Imagem 1: Para eventos de honorários e outros eventos utilizados no cálculo, configure a Identificação do evento na aba Básico…](https://ajuda.sankhya.com.br/hc/article_attachments/43541473779991)

| **⚠️** **Atenção**  Antes de alterar a identificação de um evento já utilizado em outros cálculos, verifique seu uso. Quando necessário, prefira duplicar o evento e configurar a cópia especificamente para o cálculo do autônomo. |
| --- |

**Lançar o movimento do autônomo**

[GIF animado: Imagem 2: Lançar o movimento do autônomo](https://ajuda.sankhya.com.br/hc/article_attachments/43541473785239)

1. Acesse a tela **Lançamento de Movimento** (Pessoal+ > Rotinas Folha).
2. Clique na opção **Por funcionário**.
3. Filtre por **Empresa**, **Referência** e **Funcionário**.
4. Na aba **Funcionários**, marque o card do autônomo.
5. Clique na aba **Lançamento** e preencha os dados:
   - Em **Tipo de Movimento**, selecione **Mensal**.
   - Preencha o **Código do Evento** e o **Valor**.
   - Confirme no botão de salvar (✓) e clique em **Lançar Movimentos**.
6. Na aba **Visualização**, confira os eventos lançados.

**Calcular o RPA**

[GIF animado: Imagem 3: Calcular o RPA](https://ajuda.sankhya.com.br/hc/article_attachments/43541473787159)

1. Acesse a tela **Cálculos** (Pessoal+ > Rotinas Folha).
2. Selecione a opção **Autônomos**, o modo **Individual** ou **Coletivo** e o tipo de folha **RPA**.
3. Preencha os campos **Referência**, **Data de Pagamento**, **Empresa** e **Funcionário**.

   Como o honorário já foi lançado pelo **Lançamento de Movimento**, **não utilize o botão Honorários para lançar esse mesmo valor novamente**, isso geraria duplicidade.

   Use o botão apenas para consultar lançamentos já existentes ou lançar honorários que ainda não tenham sido registrados.
4. Clique em **Próximo** e depois em **Calcular**.
5. Se desejar registrar o processo de cálculo, marque **Gerar log completo**.
6. Confira os resultados e confirme o cálculo.

**Calcular a folha mensal**

Depois de calcular todos os RPAs da referência, realize o cálculo da folha **Mensal** do autônomo para consolidar os valores.

📚 Acesse o artigo [**Cálculo da folha de Autônomos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/43529821213335) para saber de todas as etapas do cálculo até o envio ao eSocial.

### 4. Pontos de Atenção

- Não lance o mesmo honorário duas vezes, uma pelo Lançamento de Movimento e outra pelo botão Honorários do cálculo RPA. Isso duplica o valor na folha.
- O cálculo mensal gera o evento 516 - Líquido Autônomos, que representa o valor já pago ao autônomo nos RPAs da referência, evitando duplicidade no resumo e na integração financeira. Para que esse evento zere corretamente o líquido, o evento de honorário lançado precisa estar com identificação 119 - Eventos Honorários ou 200 - Outros Eventos Suplementares (identificação 200 considerada nesse cálculo a partir da versão 5.109.8).
- Confira a Data de Pagamento informada no cálculo mensal para garantir que ela corresponda ao período em que os RPAs foram pagos.

### 5. Dicas de Usabilidade

- Use este caminho quando quiser lançar e revisar o valor do honorário antes de calcular a folha.
- Se preferir lançar o honorário direto durante o cálculo do RPA, sem passar pelo Lançamento de Movimento, veja o artigo "Cálculo da folha de Autônomos".

## Perguntas Frequentes (FAQ)

**1. Posso lançar o honorário pelo Lançamento de Movimento e também pelo botão "Honorários" no cálculo RPA?**

**Não. Escolha um dos dois caminhos. Lançar nos dois duplica o valor.**

**2. Posso lançar honorários diretamente no cálculo do RPA?**

Sim. Quando o honorário ainda não tiver sido registrado em **Lançamento de Movimento**, utilize o botão **Honorários** no cálculo do RPA.

**3. Por que o mesmo valor apareceu duas vezes no cálculo?**

Verifique se o honorário foi lançado tanto em **Lançamento de Movimento** quanto pelo botão **Honorários** no cálculo do RPA. O mesmo evento não deve ser lançado pelas duas opções.

**4. Por que o líquido da folha mensal não está zerando?**

Verifique se o evento de honorário utilizado está configurado com a identificação **119 - Eventos Honorários** ou **200 - Outros Eventos Suplementares**. A identificação 200 é considerada no cálculo do **516 - Líquido Autônomos** a partir da versão **5.109.8**.

📚 Para entender o processo completo de cálculo do autônomo, consulte o artigo [**Cálculo da folha de Autônomos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/43529821213335).

## Artigos Relacionados

- [Cálculo da folha de Autônomos](https://ajuda.sankhya.com.br/hc/pt-br/articles/43529821213335)
- [Como configurar o cálculo de ISS para autônomos no RPA](https://ajuda.sankhya.com.br/hc/pt-br/articles/39267510149527)
