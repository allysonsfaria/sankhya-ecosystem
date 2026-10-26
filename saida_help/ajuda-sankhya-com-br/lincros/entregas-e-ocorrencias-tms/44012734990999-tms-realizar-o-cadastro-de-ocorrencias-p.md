---
id: "44012734990999"
titulo: "[TMS] - Realizar o cadastro de ocorrências para a empresa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012734990999--TMS-Realizar-o-cadastro-de-ocorr%C3%AAncias-para-a-empresa"
trilha: "Lincros > TMS > Entregas e Ocorrências - TMS"
atualizado_em: "2026-10-05T19:38:25Z"
rotulos: ["sync_hc", "lincros", "lincros_13433244", "sync_hash_39d32018e954"]
---

# [TMS] - Realizar o cadastro de ocorrências para a empresa

## 1. Problema Relatado pelo Cliente

O cliente deseja configurar e gerenciar as ocorrências relacionadas ao transporte das mercadorias dentro do sistema Lincros, a fim de registrar eventos durante a entrega, como atrasos, reentregas, abonos de prazo, entre outros.

Este artigo explica como realizar o cadastro de ocorrências de transporte no sistema, detalhando os campos disponíveis e as funcionalidades relacionadas, como exibição em régua de entregas, envio de SMS, e integrações com Webhook, OCR e aplicativo mobile. Também orienta sobre ações automáticas e vínculos com pendências e tipos de conhecimento.

---

## 2. Passo a Passo para Resolver o Problema

## Acessar a Tela de Ocorrências por Empresa

Menu: **Cadastros Gerais > Configurações da Empresa > Ocorrências**

Nesta tela, é possível visualizar e gerenciar todas as ocorrências cadastradas para a empresa. São exibidos:

- Código
- Nome
- Descrição
- Sequência
- Permissões de crédito, débito e abono de prazo

  ![Imagem 1: Permissões de crédito, débito e abono de prazo](https://ajuda.sankhya.com.br/hc/article_attachments/44012772826007)

## Cadastrar Nova Ocorrência

Clique em **"Novo"** para abrir a tela de cadastro. Preencha os seguintes campos:

- **Código:** identificador da ocorrência
- **Nome:** nome descritivo
- **Descrição:** detalhamento do evento
- **Marcador:** identificação visual da ocorrência. O marcador já deve estar previamente cadastrado.
- **Permitir inserir crédito (desconto)**
- **Permitir inserir débito (acréscimo)**
- **Permite prazo agendado**
- **Visualização restrita:** visível apenas para a empresa
- **Indicador que houve falhas na entrega que implicam no resultado do OTIF do OnFull
  Tipo de Conhecimento**

  - **Ao preencher esse campo, será gerado automaticamente um novo conhecimento do tipo informado, vinculado à NF e ao conhecimento normal.**

![Imagem 2: Ao preencher esse campo, será gerado automaticamente um novo conhecimento do tipo informado, vinculado à NF e ao…](https://ajuda.sankhya.com.br/hc/article_attachments/44012781118871)

## Ações

- **Criar pendência**
- **Responsável pela pendência**
- **Permitir inserir abono para prazo**
- **Abonar prazo de entrega da carga**
- **Suspender prazo de entrega da carga**
- **Retomar prazo de entrega da carga**
- **Permitir informar prazo de resolução da pendência**
- **Validar comprovante com OCR (NF-e e CT-e)** (requer módulo habilitado)

## Outras Ações Disponíveis

As ações definem comportamentos automáticos sempre que a ocorrência for lançada:

- `entreganota`: altera para situação "transportada" e registra a data de entrega.
- `estornoentreganota`: reverte para "em transporte" e remove data de entrega.
- `recalcularprevisaoentrega`: atualiza a previsão
- `notificarrastreamento`: envia notificação ao destinatário
- `finalizartransporte`: define a nota como finalizada
- `confirmacaocoleta`: define início do transporte e insere data de coleta.
- `estornarColetaNota`: volta a nota para situação "associada" (se não tiver CT-e)

  ![Imagem 3: estornarColetaNota : volta a nota para situação "associada" (se não tiver CT-e)](https://ajuda.sankhya.com.br/hc/article_attachments/44012773163671)

## Situações

Permite o lançamento automático da ocorrência ao atingir determinada condição, como a situação de uma pré-nota, nota, conhecimento ou embarque.

![Imagem 4: Permite o lançamento automático da ocorrência ao atingir determinada condição, como a situação de uma pré-nota, nota,…](https://ajuda.sankhya.com.br/hc/article_attachments/44012735589015)

## Configurações da Régua de Entregas

- **Exibir na régua**: apenas com previsão
- **Sempre exibir na régua**: sempre aparece
- **Considerar na previsão de entrega**
- **Sequência**: editável se uma das opções acima estiver marcada

  ![Imagem 5: Sequência : editável se uma das opções acima estiver marcada](https://ajuda.sankhya.com.br/hc/article_attachments/44012757311895)

  ## Configurações de Email

  - Enviar email para o destinatário
  - Enviar previsão de entrega do cliente e da transportadora
  - Enviar XML e DANFE da NF-e
  - Notificar rastreamento
  - Enviar e-mail ao responsável pela pendencia
  - Enviar e-mail de notificação aos usuários

    ![Imagem 6: Enviar e-mail de notificação aos usuários](https://ajuda.sankhya.com.br/hc/article_attachments/44012757450903)

## SMS

Necessário modulo contratado e integrador previamente cadastrado

- **Texto SMS:** até 160 caracteres (requer integrador de SMS e ação `enviarSMS` habilitada)
- **Enviar link no SMS:** mesmo critério do Texto SMS
- **Enviar SMS ao responsável pela pendência**mesmo critério do Texto SMS
- **Enviar SMS de notificação aos usuários**mesmo critério do Texto SMS
- **Texto SMS - Pendência gerada** mesmo critério do Texto SMS
- **Texto SMS - Pendência resolvida**mesmo critério do Texto SMS

  ![Imagem 7: Texto SMS - Pendência resolvida mesmo critério do Texto SMS](https://ajuda.sankhya.com.br/hc/article_attachments/44012757584279)

## Integrações

- **Replicar ocorrência:** publica a ocorrência no Webhook
- **Quantidade de anexos:** define o número mínimo de anexos para a publicação
- **Vtex**Envia atualização do status de rastreament**o**

  ![Imagem 8: Vtex Envia atualização do status de rastreament o](https://ajuda.sankhya.com.br/hc/article_attachments/44012773897879)

---

## 3. Considerações Importantes

- As ocorrências cadastradas são essenciais para a exibição correta da régua de entregas e cálculo de previsão.
- O envio de SMS exige a configuração do integrador e da ação específica.
- As ações automáticas permitem controle mais preciso sobre o fluxo de entrega.
- A exibição de ocorrências na régua depende das marcações específicas.
- A criação de pendência pode ser vinculada a usuários com prazos definidos para resolução.

---
