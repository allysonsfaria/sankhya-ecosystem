---
id: "39447728136727"
titulo: "Como calcular a rescisão complementar"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39447728136727-Como-calcular-a-rescis%C3%A3o-complementar"
trilha: "Manual do Produto > Pessoas+ > Rescisão > Cálculo da Rescisão por Tipo de Desligamento"
atualizado_em: "2026-10-02T15:45:13Z"
rotulos: ["Configuração", "Eventos", "eSocial", "ID: br.com.sankhya.rh.CalculoIndFolha", "Folha de Pagamento", "Rescisão", "Rescisão complementar", "FPRELATHOLRESC", "Pessoal+"]
---

# Como calcular a rescisão complementar

**Módulo:** Pessoal+
**Caminho de Acesso:**Pessoal+ > Rotinas Folha
**ID da Tela:** br.com.sankhya.rh.CalculoIndFolha

---

## Sumário

[Descrição e Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/39447728136727-Como-calcular-a-rescis%C3%A3o-complementar#h_01KN4TQWF8WTVX0ANTR8BJ5K48)

1. [Descrição da Funcionalidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/39447728136727-Como-calcular-a-rescis%C3%A3o-complementar#h_01KN4TQK86956W37237VGPGH2H)
2. [Pré-requisitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/39447728136727-Como-calcular-a-rescis%C3%A3o-complementar#h_01KN4TQK8APPAJJJHKSBVQ8B7J)
3. [Jornada de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/39447728136727-Como-calcular-a-rescis%C3%A3o-complementar#h_01KN4TQK8KXYCDTSEV8RDKQG6A)
4. [Ponto de Atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/39447728136727-Como-calcular-a-rescis%C3%A3o-complementar#h_01KN4TQK9PTZAKECRWAHW2WFW6)
5. [Dicas de Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/39447728136727-Como-calcular-a-rescis%C3%A3o-complementar#h_01KN4TQK9Z0GE5P7WK9Q46Z5KX)

[Perguntas Frequentes (FAQ)](https://ajuda.sankhya.com.br/hc/pt-br/articles/39447728136727-Como-calcular-a-rescis%C3%A3o-complementar#h_01KN4TQKA48WR9FSMJ0ZJ294Z9)

[Artigos Relacionados](https://ajuda.sankhya.com.br/hc/pt-br/articles/39447728136727-Como-calcular-a-rescis%C3%A3o-complementar#h_01KN4TQKAQV0KJVR7KESREXT6S)

---

## Descrição e Usabilidade

A **Rescisão Complementar** é utilizada para complementar valores que não foram pagos corretamente no momento do desligamento do colaborador.

Ela é aplicada quando a rescisão original já foi concluída, mas posteriormente são identificadas **diferenças financeiras ou reflexos legais** que precisam ser pagos ao ex-colaborador.

Esse processo é muito comum em situações como:

- reajuste salarial coletivo após o desligamento;
- diferenças de dissídio;
- horas extras apuradas após a rescisão;
- comissões fechadas posteriormente;
- médias variáveis recalculadas;
- diferenças de férias e 13º;
- reflexos de aviso prévio indenizado;
- verbas lançadas após o envio do desligamento ao eSocial.

A rescisão complementar possui embasamento legal na **CLT** e nas obrigações acessórias do **eSocial**, pois garante o pagamento correto de direitos trabalhistas já constituídos, mesmo após a extinção do vínculo.

Além do pagamento ao colaborador, essa rotina também assegura:

- recálculo correto das bases de INSS e IRRF;
- geração do evento S-1200 complementar;
- possível retificação do S-2299 ou S-2399;
- consistência entre folha, encargos e governo.

⚠️ A Rescisão Complementar **não substitui a rescisão original**, apenas complementa diferenças identificadas posteriormente.

### 1. Descrição da Funcionalidade

A rotina de Rescisão Complementar é composta por **duas etapas obrigatórias dentro da mesma jornada**:

1. **Lançamento das verbas**

   Primeiro, é necessário informar quais eventos compõem a diferença que será paga.

   Esse lançamento é realizado na tela **Lançamento de Movimento**, onde se define:

   - os eventos;
   - a referência;
   - a origem da verba;
   - o tipo de movimento.
2. **Cálculo da Rescisão Complementar**

   Após o lançamento, o sistema utiliza essas verbas para calcular a folha de **Rescisão Complementar**, recompondo bases e tributos quando necessário.

   ⚠️ Sem o lançamento prévio dos eventos, o cálculo não terá verbas para processar.

### 2. Pré-requisitos

Antes de iniciar, valide os seguintes pontos:

**Permissões necessárias**

- Acesso liberado às telas:
  - Lançamento de Movimento;
  - Cálculos;
  - Gerenciador de Folhas.

**Requisitos de negócio**

- Colaborador deve estar **desligado** com rescisão original já calculada.
- Desligamento enviado com sucesso ao eSocial:
  - **S-2299;**
  - ou **S-2399.**
- Verbas da diferença já definidas com a área responsável.
- Referência correta da origem dos valores.

### 3. Jornada de Uso

#### **(1)** Lançar os eventos da diferença

1. Acesse a tela **Lançamento de Movimento** (Pessoal+ > Rotinas Folha).
2. Selecione:

   - **Empresa**;
   - **Tipo de Filtro** como **Funcionário**;
   - **Referência**.
3. Clique em **Pesquisar**.
4. Na aba **Funcionários**, clique sobre o card do colaborador para selecioná-lo.
5. Em **Lançamento**, defina o **Tipo de Movimento** conforme o cenário:

   - **Cenário A — Diferença no mesmo mês da rescisão**

     Use quando a diferença pertence ao **mesmo mês da rescisão original**.

     ![Imagem 1: Use quando a diferença pertence ao mesmo mês da rescisão original .](https://ajuda.sankhya.com.br/hc/article_attachments/39479064315671)
     - No campo **Tipo de Movimento**, selecione a opção **Rescisão Complementar** e preencha os demais campos.

       Esse cenário é indicado para:

       - horas extras lançadas no mesmo mês;
       - comissão esquecida;
       - prêmio não pago;
       - reflexos identificados antes do fechamento da competência.

         **Exemplo prático**

         Colaborador desligado em **05/04**, e no dia **20/04** foi identificada comissão pendente.

- **Cenário B — Diferença em mês posterior**

  Quando o pagamento ocorrer em **competência diferente da rescisão:**

  ![Imagem 2: Quando o pagamento ocorrer em competência diferente da rescisão:](https://ajuda.sankhya.com.br/hc/article_attachments/39479166327063)
  - no campo **Tipo de Movimento** selecione **Verbas de meses anteriores**.
  - Preencha o campo **Referência de Origem** com o **mês da rescisão original** e os demais campos.

    ⚠️ Esse campo é indispensável para que o sistema recompile corretamente a base histórica da rescisão.

    **Exemplo prático**

    Rescisão ocorreu em **04/2025** e a diferença será paga em **05/2025**.

    - Lançe como **Verbas de meses anteriores**
    - Referência de Origem = **04/2025**

6. Salve o cadastro (**Finalizar Adição**) e clique em **Lançar Movimentos**.

   💡Ao calcular folha mensal, rescisão ou rescisão complementar, o sistema verifica se há **Verba de Meses Anteriores** não paga e a inclui automaticamente na primeira folha do colaborador, sem opção de escolha pelo usuário, exceto se o lançamento for feito na aba **Movimentações** da tela **Cálculos**.

   - **Cenário C — Projeção de API dentro do mês data-base**

     Quando o desligamento ocorrer **no mês anterior ao mês data-base do reajuste sindical**, o sistema pode calcular a rescisão complementar considerando **somente os dias do Aviso Prévio Indenizado (API) projetados dentro do mês do reajuste**.

     Esse cenário é utilizado principalmente em:

     - dissídio após desligamento;
     - reajuste coletivo retroativo;
     - diferenças proporcionais sobre API.

       | Rescisão - 02/2025 |  |  |  |  |
       | --- | --- | --- | --- | --- |
       | ![Imagem 3: Rescisão - 02/2025](https://ajuda.sankhya.com.br/hc/article_attachments/42315328888087) |  |  |  |  |
       | Regra de Cálculo - 03/2025 |  |  |  |  |
       | ![Imagem 4: Regra de Cálculo - 03/2025](https://ajuda.sankhya.com.br/hc/article_attachments/42315328888087) |  |  |  |  |
       | Reajuste salarial c/ assinatura da CCT - 04/2025 | ![Imagem 5: Reajuste salarial c/ assinatura da CCT - 04/2025](https://ajuda.sankhya.com.br/hc/article_attachments/42315328888983) | Houve projeçlão API no mês data base? | **Sim** | Cálculo da folha complementar com eventos do API. |
       |  |  | Não |  |  |
       |  |  | Não tem cálculo da folha complementar. |  |  |

       Antes do cálculo:

       1. Habilite o parâmetro **UTILIZAR EVENTOS MARCADOS CALC. RESCISÂO - PAREVERESCISAO** para que os eventos de rescisão que foram marcados sejam recalculados na folha complementar.

       2. Parametrize os eventos

       Na tela **Eventos**, aba **Avançado**, habilite a opção **Evento de indenização integrante do Aviso Prévio Indenizado**

       3. Configure o reajuste

       Faça o **Reajuste Salarial**, com a opção **Considera projeção do aviso prévio indenizado dentro do mês data-base** marcada na seção **Realiza Reajuste Sindical?**.

       4. Execute o cálculo

       Siga a jornada normal da Rescisão Complementar.

       O sistema considerará **somente os dias projetados dentro do mês data-base**.

       **Exemplo prático**

       Desligamento em **28/02**, com API projetado até **10/03**, sendo a data-base em março.

       Nesse caso, a diferença será calculada apenas de **01/03 a 10/03**.

#### **(2)** Calcular a folha

1. Acesse a tela **Cálculos** (Pessoal+ > Rotinas Folha).
2. Clique nos cards **Individual** e **Rescisão Complementar**.
3. Preencha os campos:
   - **Referência**;
   - **Data de Pagamento**;
   - **Empresa**;
   - **Funcionário**.
4. O campo **Referência da Rescisão** será preenchido automaticamente.
5. Informe o motivo da rescisão complementar no campo **Descrição origem do pagamento**.

   Esse campo é importante para rastreabilidade, principalmente em:

   - dissídios;
   - auditorias;
   - justificativas internas;
   - conferência contábil.
6. Marque **Considerar apenas resíduos de eventos já existentes na folha original** quando desejar recalcular somente eventos que já existiam na folha original.

   💡Essa opção é altamente recomendada para:

   - diferenças de dissídio;
   - recomposição de médias;
   - reajustes retroativos;
   - reflexos de eventos já pagos anteriormente.
7. Clique em **Próximo**.

   Caso os eventos de desligamento da rescisão original, S-2299 ou S-2399 não estiverem sido enviados, a seguinte mensagem será exibida:

   **"O cálculo de Rescisão Complementar só é possível para funcionários que tenham o evento de desligamento (S-2299 / S-2399) finalizado com sucesso no eSocial."**
8. Defina o modo de cálculo:
   - Calcular com log;
   - Calcular sem log;
   - Calcular com log de incorporações.

     💡 Recomendado usar **Calcular com log** para auditoria, pois apresenta:

     - fórmulas principais;
     - fórmulas auxiliares;
     - variáveis utilizadas;
     - funções executadas;
     - bases recompostas;
     - eventos acionados por &E e &F.

       O log pode ser exportado em TXT para conferência detalhada.
9. Após o cálculo, [revise cuidadosamente](https://ajuda.sankhya.com.br/hc/pt-br/articles/39318926935191):

   - proventos;
   - descontos;
   - bases de INSS;
   - IRRF;
   - reflexos;
   - médias;
   - API;
   - eventos retroativos.

   ⚠️ Se, durante a conferência notar que ainda faltou o pagamento de alguma verba, na aba **Movimentações**:

   1. clique em **Adicionar Movimento** e informe o **Evento** e o **Índice**;
   2. marque **Verbas de Meses Anteriores** (se aplicável) e informe a **Referência de Origem**;
   3. clique em **Finalizar Adição** e verifique se o evento foi inserido;
   4. clique em **Confirmar alterações** para o sistema efetuar o recálculo automático (apenas os eventos de INSS (desconto e base de cálculo) serão recompostos).

      **Observação:** podem ser lançados eventos não presentes em folhas anteriores ou diferenças de eventos já pagos.
10. Clique em **Confirmar Folha**.

    ⚠️ Na Rescisão Complementar, os valores pagos dependem integralmente dos eventos lançados na etapa inicial.
11. Após a confirmação da folha, podem ser feitas:

- Emissão do holerite.
- Integração contábil (lançamentos na contabilidade).
- Integração financeira (contas a pagar).
- Liberação da folha para o eSocial.

12. Em seguida, acesse a **Central do eSocial** para gerar e enviar:

- **S-1200 complementar**: para pagamento da diferença.
- **Retificação S-2299 / S-2399**: quando houver impacto nos valores da rescisão original já enviada.

  **Exemplo**

  Se a nova verba alterar:

  - base de INSS;
  - valor líquido;
  - férias;
  - 13º.

  O desligamento será retificado. Isso garante aderência legal ao histórico do desligamento.

### 4. Pontos de Atenção

- **O Lançamento é parte obrigatória da jornada**

  A ausência do lançamento prévio impedirá o cálculo correto.
- **Escolha correta do tipo de movimento**
  - **Rescisão Complementar** → mesma referência
  - **Verbas de meses anteriores** → mês posterior
- **Referência de origem**
  - Quando usar mês posterior, a referência da origem deve ser a da rescisão original.
  - O histórico ([Regras de cálculo](https://ajuda.sankhya.com.br/hc/pt-br/articles/39936375428503-Configura%C3%A7%C3%A3o-das-Regras-de-C%C3%A1lculos#h_01KPV4XP0YJ5FR5MT687PSZP0W)) da referência da rescisão de origem impacta diretamente no cálculo de médias na rescisão complementar.
- **Verbas de meses anteriores no eSocial**

  Os valores de meses anteriores são enviados nos eventos S-1200 e S-1210 junto com os do mês atual, seguindo o leiaute oficial.
- **Reprocessamento do eSocial**

  Sempre valide se haverá:

  - novo S-1200;
  - retificação S-2299;
  - retificação S-2399.
- **Dissídio com desligados**

  Quando houver dissídio em período com desligamento, as diferenças podem ser recalculadas também na rescisão complementar.
- **Impressão TRCT**

  Para imprimir o TRCT padrão Sankhya, o parâmetro **Rescisão - FPRELATHOLRESC** não deve estar configurado com nenhum número de relatório.

### 5. Dicas de Usabilidade

- Sempre no campo **Descrição origem do pagamento** o motivo da diferença;
- Use log em cálculos sensíveis;
- Valide a competência da rescisão;
- Revise bases previdenciárias;
- Use a opção **Considerar apenas resíduos de eventos já existentes na folha original** em dissídios e resíduos;
- Confira API dentro do mês data-base;
- Valide reflexos em férias e 13º.

## Perguntas Frequentes (FAQ)

**1. Como saber qual tipo de movimento usar?**

Use:

- **Rescisão Complementar** → mesma referência
- **Verbas de meses anteriores** → mês posterior

**2. Quando devo usar a opção de resíduos?**

Quando quiser recalcular **somente eventos que já existiam na folha original**, sem trazer novos eventos.

**3. A rescisão complementar gera retificação do desligamento?**

Sim. Quando houver impacto na rescisão original, o sistema poderá gerar **retificação do S-2299 ou S-2399**.

**3. Posso calcular sem envio do desligamento?**

Não. O **S-2299 ou S-2399 deve estar finalizado com sucesso**.

**4. Posso recalcular diferenças de aviso prévio indenizado?**

Sim, inclusive com projeção dentro do mês data-base, desde que os eventos estejam corretamente parametrizados.

## Artigos Relacionados

- [Lançamento de Movimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/38268572935319)
- [Cálculos](https://ajuda.sankhya.com.br/hc/pt-br/articles/39309113368599)
- [Gerenciador de Folhas](https://ajuda.sankhya.com.br/hc/pt-br/articles/4424800696599)
