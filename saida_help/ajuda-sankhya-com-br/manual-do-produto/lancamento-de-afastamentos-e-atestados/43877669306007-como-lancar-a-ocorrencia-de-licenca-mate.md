---
id: "43877669306007"
titulo: "Como lançar a ocorrência de licença-maternidade para uma funcionária"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43877669306007-Como-lan%C3%A7ar-a-ocorr%C3%AAncia-de-licen%C3%A7a-maternidade-para-uma-funcion%C3%A1ria"
trilha: "Manual do Produto > Pessoas+ > Afastamentos e Ocorrências > Lançamento de Afastamentos e Atestados"
atualizado_em: "2026-10-09T17:36:37Z"
rotulos: ["br.com.sankhya.rh.LancamentoOcorrencias", "Licença Maternidade", "Licença Maternidade Cidadã", "Programa Empresa Cidadã", "S-2230 — Afastamento Temporário"]
---

# Como lançar a ocorrência de licença-maternidade para uma funcionária

**Módulo:** Pessoal+
**Caminho de Acesso:** Pessoal+ > Rotinas Folha > Ocorrências > Lançamento
**ID da Tela:** br.com.sankhya.rh.LancamentoOcorrencias

---

### O que é e para que serve

A **licença-maternidade** é registrada como uma ocorrência de afastamento na tela **Ocorrências**. Depois do lançamento, a situação da colaboradora é atualizada para **afastada por licença gestante** e o sistema considera o afastamento em processos como folha, férias, 13º salário, período concessivo, estabilidade e eSocial.

O lançamento deve ser feito com as informações do documento que comprova o afastamento, principalmente a **Data de Início** e a quantidade de dias previstos.

### Antes de começar

Antes de lançar a ocorrência, verifique se existe um tipo de ocorrência já cadastrado para a licença-maternidade.

Verifique na aba **Cadastro** da tela **Ocorrências**:

- **Licença maternidade**: licença comum de 120 dias.
- **Licença Maternidade Cidadã**: utilizada por empresas participantes do **Programa Empresa Cidadã**, com licença de 180 dias.

  | **⚠️** **Atenção**  O tipo de ocorrência deve estar configurado com o motivo de afastamento correspondente ao eSocial. Para a licença-maternidade, os motivos utilizados são **17** (Licença-maternidade) ou **18** (Prorrogação por 60 dias - Empresa Cidadã). |
  | --- |

### Como lançar a licença-maternidade

[GIF animado: Imagem 1: Como lançar a licença-maternidade](https://ajuda.sankhya.com.br/hc/article_attachments/43879689108631)

1. Acesse a tela **Ocorrências** (Pessoal+ > Rotinas Folha).
2. Escolha a **empresa** e filtre por **funcionário**. Clique em **Pesquisar**.
3. Na aba **Lançamento**, habilite a chave de seleção para lançamento no canto superior direito e clique no card da funcionária para selecioná-la.

   Clicar no card sem a seleção ativa abre as ocorrências já lançadas, sem lançar nada novo.
4. Clique em **Lançar ocorrência** e escolha o tipo de ocorrência de licença-maternidade.
5. Anexe o atestado médico.

   São aceitos arquivos nos formatos:

   - PNG;
   - JPG;
   - PDF.

   Depois que o documento for anexado, o botão **Lançar Ocorrência** será habilitado.

   | **⚠️** **Atenção**  Anexe o documento antes de lançar a ocorrência. Sem o anexo, o botão **Lançar Ocorrência** permanece desabilitado. |
   | --- |
6. Clique no botão **Lançar Ocorrência** e preencha a **Descrição** e as datas:
   - **Data de Início**: data exata de início do afastamento, conforme o documento apresentado.

     Para a licença-maternidade, essa data deve corresponder à **data do parto ou a uma data de até 28 dias antes do parto**.

     Essa informação é importante porque o sistema utiliza a ocorrência para controlar também o período de estabilidade da colaboradora.
   - **Data de retorno prevista**: dia previsto para a volta.

     Com a **Data de Início** e os dias de afastamento preenchidos, o sistema calcula a data de retorno prevista.
   - **Dias de afastamento previstos**: 120 dias na licença comum ou 180 dias na Empresa Cidadã.

     A partir dessas informações, o sistema calcula a **Data de retorno prevista**.
   - **Data de término**: deixe em branco no momento do lançamento.

     A **Data de término** deve ser preenchida somente quando a colaboradora efetivamente retornar do afastamento.

     | 🚨 **Risco operacional**  Preencher a **Data de término** antes do retorno efetivo pode causar impactos no cálculo da folha, no envio de eventos ao eSocial e no controle da estabilidade. |
     | --- |
7. Clique em **Atestado** e informe **Emitente do Atestado** e, se quiser, **CID** e o órgão de classe.
8. Clique em **Confirma lançamento** e confirme de novo na mensagem apresentada.

   A mensagem **"Ocorrência salva com sucesso!"** confirma o lançamento.

   Se a funcionária estiver de férias na data de início, o sistema pergunta se deve interromper as férias. Ao confirmar, as férias terminam no dia anterior à licença e o saldo é remarcado para depois dela.

   Após a confirmação, o sistema atualiza a **Situação** da colaboradora na tela **Configuração de Funcionários**, indicando o afastamento por licença gestante.

   ![Imagem 2: Após a confirmação, o sistema atualiza a Situação da colaboradora na tela Configuração de Funcionários , indicando o…](https://ajuda.sankhya.com.br/hc/article_attachments/43879759794967)
9. Acesse a **Central do eSocial** (Pessoal+ > Rotinas Folha) e gere o evento S-2230 (Afastamento Temporário) referente à licença, informando o motivo 17 ou 18 conforme o tipo de licença lançada.

   | **⚠️** **Atenção**  O lançamento da ocorrência não envia o evento S-2230 automaticamente. O envio ao eSocial é uma etapa manual, feita separadamente pela Central do eSocial. |
   | --- |

**O que acontece depois do lançamento?**

O lançamento da licença-maternidade é considerado automaticamente em outros processos do sistema.

- **Folha mensal**

  Durante o período de licença, o salário-maternidade e as médias são considerados nos eventos padrão:

  - **540 e 541** — licença-maternidade comum;
  - **560 e 561** — licença do Programa Empresa Cidadã.
- **13º salário**

  As parcelas do 13º salário referentes ao período de licença utilizam eventos próprios:

  - **308 e 309** — 1ª e 2ª parcela na licença-maternidade comum;
  - **330 e 332** — licença do Programa Empresa Cidadã.

    📚 Para mais detalhes, acesse [Como configurar e calcular o 13º salário durante a licença-maternidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/44103337618455).
- **GPS / INSS**

  O salário-maternidade de 120 dias entra como dedução na linha **Licença Maternidade** da GPS. A prorrogação Empresa Cidadã não é deduzida.
- **FGTS**

  Continua sendo recolhido durante a licença.
- **Contrato de experiência**

  O vencimento é prorrogado pelos dias de licença.
- **Férias**

  O cálculo de férias fica bloqueado durante a licença. O prazo para gozo das férias é estendido pelos dias de licença.

  Ao tentar realizar o cálculo, o sistema apresenta a mensagem: **"Funcionário em licença maternidade. Folha não será calculada."**
- **Se a licença começar durante as férias**

  Se a colaboradora estiver de férias na data de início da licença, o sistema pergunta:

  **"O sistema realizará o lançamento da ocorrência de Licença Gestante interrompendo as férias do funcionário selecionado?"**

  Ao confirmar:

  - a data de término das férias é ajustada para um dia antes do início da licença;
  - o saldo de férias não gozado é reprogramado para depois da licença.

  Esse comportamento ocorre automaticamente para os motivos:

  - **17 — Licença-maternidade**;
  - **18 — Prorrogação por 60 dias - Empresa Cidadã**.

  Para os demais motivos da tabela, confirme manualmente se a interrupção das férias é necessária.

  📚 Veja o passo a passo completo em [Como fazer a concessão de licença maternidade para colaboradoras que estão de férias?](https://ajuda.sankhya.com.br/hc/pt-br/articles/32990306643991).
- **Período concessivo**

  Os dias de licença prorrogam o fim do **período concessivo**.

  O sistema também sugere que a colaboradora entre em férias logo após o retorno da licença.
- **eSocial**

  O afastamento é informado ao eSocial pelo evento **S-2230 — Afastamento Temporário**, gerado e enviado manualmente pela **Central do eSocial**, utilizando o motivo definido no tipo de ocorrência.

  Antes de gerar o S-2230, deve existir um evento **S-2200 — Admissão** ou **S-2300 — TSVE** finalizado para a colaboradora.

  | **⚠️** **Atenção**  Se o motivo de afastamento utilizado na ocorrência tiver sido descontinuado pelo eSocial para a data de início informada, o sistema apresentará uma mensagem indicando o problema. Nesse caso, utilize um tipo de ocorrência com motivo vigente. |
  | --- |
- **Controle da estabilidade da gestante**

  O sistema pode controlar a estabilidade da colaboradora de duas formas.

  - **Pela própria ocorrência de licença-maternidade**

    Quando a ocorrência de licença-maternidade está configurada corretamente, o sistema reconhece automaticamente o período de estabilidade.

    Após o retorno da colaboradora, os controles de estabilidade são aplicados e o sistema emite alertas caso exista uma tentativa de rescisão durante o período protegido.
  - **Por uma ocorrência específica de estabilidade**

    Se a empresa utilizar uma ocorrência própria para controlar a estabilidade, confira se o código dessa ocorrência está informado no parâmetro **Cód. Hist. Ocorr. para Estabilidade - FPCODHISESTABIL**.

  📚 Veja o passo a passo completo de configuração em [Como cadastrar ocorrências com estabilidade?](https://ajuda.sankhya.com.br/hc/pt-br/articles/42546913948055).

**Como registrar o retorno da colaboradora?**

Quando a colaboradora efetivamente retornar do afastamento:

1. Abra a ocorrência de licença-maternidade.
2. Preencha a **Data de término** com a data correspondente ao retorno.
3. Salve a alteração.
4. Quando o sistema perguntar o que fazer com a licença, escolha **Encerrar licença atual e registrar retorno**.

| ℹ️ **Nota**  Não informe a **Data de término antes** do retorno efetivo. O sistema utiliza essa informação em outros processos, por isso o preenchimento antecipado pode gerar inconsistências. |
| --- |

### Pontos de Atenção

- **A colaboradora é intermitente**

  Se a colaboradora for intermitente e não possuir uma convocação cadastrada, o sistema apresentará um aviso durante o lançamento.

  É possível continuar o lançamento, mas confira as convocações para garantir que o cálculo do salário-maternidade seja realizado corretamente.
- **A ocorrência não pode ser editada**

  Se já existir folha calculada na referência de início da ocorrência, não será possível alterar a recorrência da ocorrência.

  Nesse caso:

  1. Exclua o cálculo da folha da referência de início.
  2. Edite a ocorrência.
  3. Calcule novamente a folha.
- **A licença foi lançada por engano**

  É possível excluir a ocorrência.

  Ao excluir a licença, o sistema devolve as férias da colaboradora para o período original.

### Perguntas Frequentes

**1. Qual data devo informar como início da licença-maternidade?**

Informe a data exata de início do afastamento indicada no documento.

Para a licença-maternidade, a data deve corresponder à **data do parto ou a uma data de até 28 dias antes do parto**.

Essa informação também é utilizada pelo sistema no controle da estabilidade. Uma data incorreta pode fazer com que o período de estabilidade seja calculado de forma incorreta.

**2. Preciso preencher a Data de término no lançamento?**

Não.

Deixe a **Data de término** em branco e preencha somente quando a colaboradora efetivamente retornar do afastamento.

**3. Qual quantidade de dias devo informar?**

Informe a quantidade de dias correspondente ao tipo de licença:

- **120 dias** para a licença-maternidade comum;
- **180 dias** para a licença do Programa Empresa Cidadã.

**4. O que fazer se aparecer a mensagem "Motivo de afastamento p/ eSocial da ocorrência escolhida foi descontinuado pelo eSocial"?**

Essa mensagem indica que o motivo de afastamento configurado para o tipo de ocorrência não é válido para a data de início informada.

Utilize um tipo de ocorrência configurado com um motivo de afastamento vigente para o período.

**5. O que acontece com as férias durante a licença-maternidade?**

A folha de férias não é calculada durante o período de licença.

Se a licença começar enquanto as férias estiverem em andamento, o sistema poderá interrompê-las mediante confirmação e reprogramar o saldo não gozado para depois da licença.

**6. Como o sistema controla a estabilidade?**

O controle pode ocorrer pela própria ocorrência de licença-maternidade, quando ela está configurada corretamente, ou por uma ocorrência específica de estabilidade vinculada ao parâmetro **FPCODHISESTABIL**.

**7. O que acontece se eu recalcular a folha depois de lançar a licença?**

A licença será considerada nos cálculos correspondentes ao período do afastamento. Caso a folha seja calculada ou recalculada, confira os eventos gerados para o período de licença.

### Artigos Relacionados

- [Como cadastrar ocorrências com estabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/42546913948055)
- [Como cadastrar a ocorrência de licença-maternidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/43940237985815)
- [Como fazer a concessão de licença maternidade para colaboradoras que estão de férias?](https://ajuda.sankhya.com.br/hc/pt-br/articles/32990306643991)
- [Pessoal+/ Prorrogação da Licença Maternidade - Portaria Conjunta nº 28/2021](https://ajuda.sankhya.com.br/hc/pt-br/articles/4413844578327)
- [Cadastro de Ocorrências da Folha](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044610494)
