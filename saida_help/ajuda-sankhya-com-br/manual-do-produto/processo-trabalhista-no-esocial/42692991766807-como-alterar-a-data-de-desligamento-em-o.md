---
id: "42692991766807"
titulo: "Como alterar a data de desligamento em outra competência no processo trabalhista"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42692991766807-Como-alterar-a-data-de-desligamento-em-outra-compet%C3%AAncia-no-processo-trabalhista"
trilha: "Manual do Produto > Pessoas+ > Processos Trabalhistas > Processo Trabalhista no eSocial"
atualizado_em: "2026-10-02T17:46:41Z"
---

# Como alterar a data de desligamento em outra competência no processo trabalhista

**Módulo:** Pessoal+
**Caminho de Acesso:** Pessoal+ > Rotinas Folha > Processo Trabalhista > Informações do Contrato de Trabalho
**Versão disponível:** A partir da 5.118 / SaneSocial 3.55
**ID da Tela:** br.com.sankhya.ProcessoTrabalhista

---

## Descrição e Usabilidade

Esta funcionalidade permite tratar processos trabalhistas do **Tipo de Contrato 3 — Trabalhador com vínculo formalizado no eSocial, com inclusão ou alteração de data de desligamento**, quando a nova data de desligamento definida por decisão judicial pertence a uma competência diferente daquela em que ocorreu a rescisão original.

Nessa situação, o sistema atualiza o cadastro do colaborador com as informações do processo trabalhista, registra a nova data de desligamento definida pela decisão judicial e orienta a regularização dos eventos enviados ao eSocial, respeitando a ordem cronológica necessária para o processamento correto das informações.

Esse tratamento é necessário porque a rescisão original já pode ter sido enviada ao eSocial por meio dos eventos **S-2299** e **S-1210**. Quando a decisão judicial altera a data de desligamento para outra competência, os eventos da rescisão original precisam ser ajustados antes do envio dos eventos correspondentes à nova data.

### 1. Pré-requisitos

Utilize este fluxo quando todas as condições abaixo forem atendidas:

- o processo trabalhista estiver cadastrado com **Tipo de Contrato 3 - Trabalhador com vínculo formalizado no eSocial, com inclusão ou alteração de data de desligamento**;
- existir uma rescisão original já enviada ao eSocial pelos eventos **S-2299** e **S-1210**;
- a decisão judicial determinar uma nova data de desligamento;
- a nova data de desligamento estiver em competência diferente da rescisão original;
- a nova data de desligamento estiver preenchida no campo **Data demissão (Decisão Judicial)**.

| **⚠️** **Atenção**  A nova data de desligamento é obrigatória para esse cenário. O sistema não permite confirmar o processo trabalhista do Tipo de Contrato 3 quando essa informação não estiver preenchida. |
| --- |

### 2. Jornada de Uso

#### 2.1 Cadastrar o processo trabalhista

Acesse a tela **Processo Trabalhista** (Pessoal+ > Rotinas Folha), localize o processo cadastrado, e, no menu **Informações do Contrato de Trabalho**:

- Certifique-se de que o **Tipo de Contrato** seja **3 — Trabalhador com vínculo formalizado no eSocial, com inclusão ou alteração de data de desligamento.**
- Informe a nova data de desligamento definida pela decisão judicial no campo **Data demissão (Decisão Judicial)**.
- Confirme o cadastro.

  ![Imagem 1: Confirme o cadastro.](https://ajuda.sankhya.com.br/hc/article_attachments/42694686931991)

  Dessa forma, o sistema identifica que a nova data pertence a uma competência diferente da rescisão original e:

  - atualiza o cadastro do colaborador com o número do processo trabalhista e nova **Data demissão (Decisão Judicial)**;
  - gera os gatilhos necessários para a regularização dos eventos da competência original;
  - apresenta uma orientação com a ordem cronológica para regularizar os eventos do eSocial.

    ![Imagem 2: apresenta uma orientação com a ordem cronológica para regularizar os eventos do eSocial.](https://ajuda.sankhya.com.br/hc/article_attachments/42694529919127)

#### 2.2 Regularizar a competência da rescisão original

Acesse a **Central do eSocial** e, na competência em que ocorreu a rescisão original, siga esta ordem:

1. Reabra a referência por meio do **S-1298**, quando necessário.
2. Exclua o evento **S-1210** na referência em que o pagamento foi realizado.
3. Exclua o evento **S-2299** da rescisão original.
4. Gere novamente o **S-1200**.
5. Gere novamente o **S-1210**.
6. Envie o **S-1200**.
7. Na sequência, envie o **S-1210**.
8. Feche novamente a referência por meio do **S-1299**.

O **S-1200** deve manter as mesmas rubricas e valores da rescisão original, enquanto o **S-1210** deve manter as informações do pagamento correspondente. A nova geração desses eventos somente deve ocorrer após a exclusão do **S-1210** e do **S-2299** originais.

| **⚠️** **Atenção**  O evento **S-1210** permanece vinculado à competência em que o pagamento foi realizado. Portanto, se o pagamento da rescisão ocorreu em uma competência diferente daquela em que ocorreu o desligamento, a referência correspondente ao pagamento também deverá ser reaberta para a correção e o reenvio do S-1210. |
| --- |

#### 2.3 Processar a competência da nova data de desligamento

Após regularizar a competência original, acesse a competência correspondente à nova data de desligamento definida pela decisão judicial.

Gere e envie os eventos na seguinte ordem:

1. **S-2299 — Desligamento**;
2. **S-2500 — Processo Trabalhista**;
3. **S-2501 — Informações dos Tributos Decorrentes de Processo Trabalhista**, quando houver tributos decorrentes do processo.

#### 2.4 Evento S-2299 da nova competência

Na competência da nova data de desligamento, o **S-2299** deve registrar:

- a nova data de desligamento;
- o número do processo trabalhista.

O evento **não deve conter verbas da rescisão original nem verbas do processo trabalhista**. As bases de cálculo e as informações do processo devem ser tratadas nos eventos próprios do processo trabalhista.

#### 2.5 Evento S-2500

Após a geração do S-2299 da nova competência, gere o **S-2500**, que deve reunir as informações do processo trabalhista, incluindo, quando aplicável:

- dados cadastrais do processo;
- informações do trabalhador;
- informações do contrato de trabalho;
- bases de cálculo de Contribuição Previdenciária, quando aplicável;
- bases de cálculo de FGTS, quando aplicável.

#### 2.6 Evento S-2501

Quando existirem informações de tributos decorrentes do processo trabalhista, gere o **S-2501** após o **S-2500**.

O evento não deve ser gerado quando não houver informações tributárias decorrentes do processo.

#### 2.7 Conferir o retorno dos eventos

Após os envios, consulte os retornos do eSocial para verificar se:

- a nova data de desligamento foi processada corretamente;
- o processo trabalhista foi recepcionado;
- os eventos foram processados na sequência esperada;
- não existem rejeições ou pendências relacionadas ao processo.

### 3. Pontos de Atenção

- Este fluxo aplica-se exclusivamente ao **Tipo de Contrato 3** quando a nova data de desligamento estiver em competência diferente da rescisão original.
- Quando a nova data de desligamento estiver na mesma competência da rescisão original, este tratamento específico não deve ser aplicado.
- Os demais tipos de contrato continuam seguindo o comportamento já existente da rotina.
- O **S-1210** deve ser tratado na competência em que o pagamento foi realizado, mesmo que essa competência seja diferente da competência da nova data de desligamento.
- A exclusão da rescisão original deve seguir a ordem **S-1210** e depois **S-2299**.
- O **S-2299** da nova competência não deve conter verbas da rescisão original nem do processo trabalhista.
- As rubricas e os valores pagos da rescisão original devem permanecer na competência original, por meio dos eventos **S-1200** e **S-1210**.
- As informações do processo trabalhista devem ser tratadas no **S-2500** e, quando houver tributos decorrentes, no **S-2501**.
- O cadastro do funcionário é atualizado com a nova data de desligamento somente após a confirmação do processo trabalhista.
- O sistema deve preservar a rastreabilidade entre o processo trabalhista, o funcionário, os eventos gerados e os retornos do eSocial.
- Se o processo trabalhista for excluído, as informações atualizadas no cadastro do funcionário em decorrência desse processo deverão ser removidas, mantendo o funcionário com a situação **Desligado** e a data de demissão original.

### 4. Dicas de Usabilidade

- Siga a ordem dos eventos indicada pelo sistema para evitar rejeições no eSocial.
- Antes de iniciar o tratamento da nova competência, confirme se a competência da rescisão original e, quando necessário, a competência do pagamento foram devidamente regularizadas.
- Após reenviar os eventos da competência original, confirme os retornos antes de prosseguir para a nova competência.
- Confira os retornos do **S-2299**, **S-2500** e **S-2501** após os respectivos envios.
- Sempre mantenha o cadastro do processo trabalhista e as informações do funcionário consistentes com a decisão judicial.

## Perguntas Frequentes (FAQ)

**1. Quando devo utilizar este tratamento?**

Quando um processo trabalhista do **Tipo de Contrato 3** determinar uma nova data de desligamento que esteja em competência diferente da rescisão original.

**2. Preciso informar a nova data de desligamento?**

Sim. O campo **Data demissão (Decisão Judicial)** é obrigatório nesse cenário.

**3. Qual evento deve ser excluído primeiro na competência original?**

Primeiro o **S-1210** e, depois, o **S-2299**.

**4. Preciso gerar novamente o S-1200 e o S-1210?**

Sim. Depois da exclusão dos eventos originais, o sistema deve permitir a nova geração do **S-1200** e do **S-1210**, preservando as rubricas, os valores e as informações de pagamento da rescisão original.

**5. O S-1210 deve ser enviado na competência da nova data de desligamento?**

Não necessariamente. O **S-1210** permanece relacionado à competência em que o pagamento ocorreu.

**6. O novo S-2299 leva as verbas do processo trabalhista?**

Não. O S-2299 da nova competência deve conter a nova data de desligamento e o número do processo trabalhista, sem as verbas da rescisão original ou do processo trabalhista.

**7. Quando devo gerar o S-2501?**

Somente quando houver informações de tributos decorrentes do processo trabalhista. O evento deve ser gerado após o S-2500.

**8. O que acontece se a nova data de desligamento estiver na mesma competência da rescisão original?**

Este fluxo específico não será aplicado.

**9. O que acontece se o processo trabalhista for excluído?**

As informações atualizadas no cadastro do funcionário em decorrência do processo são removidas. O funcionário permanece com a situação **Desligado** e com a data de demissão original.
