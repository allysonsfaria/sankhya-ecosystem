---
id: "41186451711895"
titulo: "Pague Rápido Fintech"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/41186451711895-Pague-R%C3%A1pido-Fintech"
trilha: "Manual do Produto > Financeiro e Patrimônio > Sankhya Fintech > Banking"
atualizado_em: "2026-10-06T13:07:26Z"
rotulos: ["Configuração", "Movimentação Financeira", "Financeiro", "Pagamentos", "br.com.sankhya.fintech.paguerapido", "Fintech"]
---

# Pague Rápido Fintech

**Módulo:** Configurações › Rotinas › Pague Rápido Fintech

**Neste artigo**

- [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/41186451711895-Pague-R%C3%A1pido-Fintech#o-que-e)
- [Antes de começar](https://ajuda.sankhya.com.br/hc/pt-br/articles/41186451711895-Pague-R%C3%A1pido-Fintech#antes-de-comecar)
- [Credenciamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/41186451711895-Pague-R%C3%A1pido-Fintech#credenciamento)
- [Jornada de pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/41186451711895-Pague-R%C3%A1pido-Fintech#jornada)
- [Baixa automática](https://ajuda.sankhya.com.br/hc/pt-br/articles/41186451711895-Pague-R%C3%A1pido-Fintech#baixa-automatica)
- [Conciliação bancária](https://ajuda.sankhya.com.br/hc/pt-br/articles/41186451711895-Pague-R%C3%A1pido-Fintech#conciliacao)
- [Linha do tempo](https://ajuda.sankhya.com.br/hc/pt-br/articles/41186451711895-Pague-R%C3%A1pido-Fintech#linha-do-tempo)
- [Baixa, exclusão e alteração de títulos no ERP](https://ajuda.sankhya.com.br/hc/pt-br/articles/41186451711895-Pague-R%C3%A1pido-Fintech#alteracoes-erp)
- [Pontos de atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/41186451711895-Pague-R%C3%A1pido-Fintech#pontos-de-atencao)

## O que é e para que serve

O Pague Rápido Fintech é a solução da Sankhya Fintech que **centraliza os títulos a pagar** do Sankhya Om e **automatiza**, de ponta a ponta, o **envio das ordens de pagamento às instituições financeiras.** Com ele, **você programa, libera, envia ao banco e, assim que o pagamento é efetivado, obtém baixa e conciliação de forma automática**.

O Pague Rápido não substitui o cadastro de títulos no Sankhya Om nem opera com títulos de modalidades não suportadas.

O que você ganha com isso:

- Automação do fluxo de pagamento ponta a ponta, do Sankhya Om ao banco
- Redução de erros operacionais associados à operação manual de pagamentos
- Rastreabilidade completa da jornada do título por meio da linha do tempo
- Baixa e conciliação automáticas após confirmação bancária
- Governança de aprovação com até 3 níveis de liberação por conta credenciada

## Antes de começar

Antes de usar o Pague Rápido, verifique:

- Sua empresa precisa ter contratado um pacote de serviços Fintech que inclua o módulo de Pagamentos.
- O Sankhya Om precisa estar na versão 4.35b226 ou superior.
- O BFF Financeiro precisa estar na versão 1.26.0 ou superior.
- Para PIX QR Code, a inserção do PIX COPIA E COLA só será permitido via Design System.
- Conferir as [modalidades suportadas](https://ajuda.sankhya.com.br/hc/pt-br/articles/41186451711895-Pague-R%C3%A1pido-Fintech#h_01KTYQGMCD1SYGW970WBBR6HVE), as [não suportadas](https://ajuda.sankhya.com.br/hc/pt-br/articles/41186451711895-Pague-R%C3%A1pido-Fintech#modalidades-nao-suportadas) e os [bancos disponíveis](https://ajuda.sankhya.com.br/hc/pt-br/articles/41186451711895-Pague-R%C3%A1pido-Fintech#h_01KTYQGMCDZW7KQME69T3PT5Y0) antes de credenciar a conta.

### Modalidades suportadas

O escopo atual do Pague Rápido é operar com as seguintes modalidades de pagamento:

| Modalidade | Campo identificador |
| --- | --- |
| **Boleto** | Código de Barras (Movimentação Financeira) |
| **PIX QR Code** | PIX Copia e Cola (Movimentação Financeira) |
| **PIX Chave** | Chave PIX (Parceiro) + Tipo de título com subtipo = PIX |
| **Transferência Eletrônica Disponível (TED)** | Agência Bancária (parceiro vinculado ao título) Conta bancária parceiro (parceiro vinculado ao título) Banco do parceiro vinculado ao título |

### Modalidades atualmente não suportadas

As modalidades abaixo ainda não podem ser operadas pelo Pague Rápido:

| Modalidade |
| --- |
| **Tributos** |
| **Contas de Consumo** |
| **Pessoal / Folha de Pagamento** |

### Bancos suportados

| Banco | Boleto | PIX QR Code | PIX Chave | TED |
| --- | --- | --- | --- | --- |
| **Banco do Brasil** | API | Indisponível | API | API |
| **Santander** | API | API | API | API |
| **Sicoob** | API | API | API | API |
| **Itaú** | CNAB AUTOMÁTICO | CNAB AUTOMÁTICO | CNAB AUTOMÁTICO | CNAB AUTOMÁTICO |
| **Bradesco** | CNAB AUTOMÁTICO | CNAB AUTOMÁTICO | CNAB AUTOMÁTICO | CNAB AUTOMÁTICO |
| **Safra** | CNAB AUTOMÁTICO | Indisponível | Indisponível | Indisponível |
| **Caixa** | CNAB AUTOMÁTICO | Indisponível | Indisponível | Indisponível |

## Credenciamento

O credenciamento habilita uma conta bancária para operar com o Pague Rápido. É feito uma única vez por conta, exige perfil gerencial e contempla todas as modalidades disponíveis: Boleto, PIX QR Code, PIX Chave e TED.

O processo tem 9 etapas: contratação do serviço, habilitação da integração, seleção de conta, seleção de modalidades, dados da conta, ações automáticas, usuários liberadores, credenciais de acesso e finalização.

### Contratação do serviço

Se sua empresa ainda não tem o pacote de serviços Fintech com o módulo de Pagamentos, esse é o ponto de partida.

1. Acesse o **Assistente de Melhores Práticas**.
2. No menu lateral, acesse **Configurações serviços Fintech › Pague Rápido**.
3. Clique em **Quero contratar**.

Você será direcionado ao MarketPlace Sankhya, onde os pacotes disponíveis serão exibidos. Saiba mais em [**Contratação e cobrança dos serviços Fintech**](https://ajuda.sankhya.com.br/hc/pt-br/articles/14550240434839-Contrata%C3%A7%C3%A3o-e-cobran%C3%A7a-dos-servi%C3%A7os-Fintech).

![Imagem 1: Você será direcionado ao MarketPlace Sankhya, onde os pacotes disponíveis serão exibidos. Saiba mais em Contratação e…](https://ajuda.sankhya.com.br/hc/article_attachments/41186451700887)

### Habilitação da integração

Com o serviço contratado, o próximo passo é ativar a comunicação com as soluções financeiras da Sankhya.

**ℹ️ Nota**

Essa habilitação acontece uma única vez. Se já tiver sido feita, avance para a etapa 1.3.

1. Acesse a tela **Integrar com Produtos Sankhya**.
2. Localize o card **Sankhya Fintech** e clique em **Habilitar Integração**.

![Imagem 2: Localize o card Sankhya Fintech e clique em Habilitar Integração .](https://ajuda.sankhya.com.br/hc/article_attachments/41186451701655)

### Seleção de conta

Com a integração ativa, acesse o credenciamento pelo **Assistente de Melhores Práticas › Configurações serviços Fintech › Pagamentos › Pague Rápido**, clique em **Iniciar/Executar** e selecione a conta a ser credenciada.

![Imagem 3: Com a integração ativa, acesse o credenciamento pelo Assistente de Melhores Práticas › Configurações serviços Fintech ›…](https://ajuda.sankhya.com.br/hc/article_attachments/41186466956823)

![Imagem 4: Com a integração ativa, acesse o credenciamento pelo Assistente de Melhores Práticas › Configurações serviços Fintech ›…](https://ajuda.sankhya.com.br/hc/article_attachments/41235357109655)

### Seleção de modalidades

Após selecionar a conta bancária, escolha as modalidades que serão habilitadas. As opções disponíveis variam conforme o banco.

![Imagem 5: Após selecionar a conta bancária, escolha as modalidades que serão habilitadas. As opções disponíveis variam conforme o…](https://ajuda.sankhya.com.br/hc/article_attachments/41871638660247)

### Dados da conta

Selecione a conta bancária e preencha os dados solicitados. Os campos variam de acordo com o banco.
![Imagem 6: Selecione a conta bancária e preencha os dados solicitados. Os campos variam de acordo com o banco.](https://ajuda.sankhya.com.br/hc/article_attachments/41235357113239)

**⚠️ Atenção**

Para os bancos que solicitam o **Convênio de Pagamento**, entre em contato com seu gerente bancário para verificar os procedimentos necessários e obter essa informação.

No credenciamento PIX QR Code Sicoob é exigido o **CNPJ da Cooperativa**. Essa informação pode ser encontrada nos extratos bancários ou, em caso de dúvidas, com o gerente da sua conta.

### Ações automáticas

Defina se a baixa e a conciliação dos títulos devem ocorrer automaticamente após a confirmação do pagamento pelo banco. Recomenda-se manter ambas as opções ativas para preservar a consistência entre o Sankhya Om e o extrato bancário.

![Imagem 7: Defina se a baixa e a conciliação dos títulos devem ocorrer automaticamente após a confirmação do pagamento pelo banco.…](https://ajuda.sankhya.com.br/hc/article_attachments/41186466957463)

### Usuários Liberadores

A autorização de pagamentos é um dos pilares de segurança do Pague Rápido. Defina quem pode aprovar as transações antes do envio do pagamento ao banco.

Determine o número de aprovações necessárias (até 3) e selecione os usuários liberadores. O sistema lista apenas usuários ativos com **perfil gerencial**, exceto o usuário SUP.

![Imagem 8: Determine o número de aprovações necessárias (até 3) e selecione os usuários liberadores. O sistema lista apenas…](https://ajuda.sankhya.com.br/hc/article_attachments/41186466957847)

| Configuração | O que o sistema exige |
| --- | --- |
| Mínimo de 1 liberador | Selecione ao menos um usuário para habilitar o botão **Avançar** |
| 2 aprovações configuradas | Selecione no mínimo 2 usuários liberadores |
| 3 aprovações configuradas | Selecione no mínimo 3 usuários liberadores |

**⚠️ Atenção**

Alguns bancos não exigem liberações no Internet Banking para pagamentos realizados via API. Garanta total segurança na definição dos usuários liberadores, pois eles são o controle interno na execução dos pagamentos.

### Credenciais de acesso

#### Credenciais (API)

Se ao menos uma modalidade selecionada operar via API, será necessário preencher as credenciais geradas junto ao banco.
![Imagem 9: Se ao menos uma modalidade selecionada operar via API, será necessário preencher as credenciais geradas junto ao banco.](https://ajuda.sankhya.com.br/hc/article_attachments/41235357115799)

| Banco | Boletos | PIX QR Code | PIX Chave | TED |
| --- | --- | --- | --- | --- |
| Banco do Brasil | Serviço 'Pagamento em Lote' | Indisponível | Serviço 'Pagamento em Lote' | Serviço 'Pagamento em Lote' |
| Santander | Serviço 'Pagamento de Contas' | Serviço 'Pagamento de Contas' | Serviço 'Pagamento de Contas' | Serviço 'Pagamento de Contas' |
| Sicoob | Serviço 'Cobrança Bancária Pagamentos' | Serviço 'Cobrança Bancária Pagamentos' | Serviço 'Cobrança Bancária Pagamentos' | Serviço 'SPB Transferências' |

**⚠️ Atenção**

Ao alterar as credenciais de uma conta, todas as modalidades API selecionadas receberão as mesmas credenciais. **Os escopos junto ao banco devem contemplar todos os serviços que estão sendo credenciados.**

A geração de credenciais e possíveis mudanças na relação de serviços x credenciais são de responsabilidade da instituição financeira. Em caso de dúvidas, acione seu gerente bancário.

#### Credenciais (CNAB Automático)

Se ao menos uma modalidade selecionada operar via CNAB Automático, será necessário preencher os responsáveis pelo fluxo da carta de liberação para operar via CNAB Automático.

A troca de arquivos CNAB com o banco é feita automaticamente pela Kobana, parceira autorizada da Sankhya Fintech para esse tipo de serviço. Após o envio das informações, você receberá um e-mail da Kobana confirmando que a carta foi enviada ao banco.

![Imagem 10: A troca de arquivos CNAB com o banco é feita automaticamente pela Kobana, parceira autorizada da Sankhya Fintech para…](https://ajuda.sankhya.com.br/hc/article_attachments/41235382932631)

**ℹ️ Nota**

Você não precisa contratar a Kobana — a Sankhya Fintech já cuidou disso. Você também não precisa configurar nada nem gerar arquivos manualmente. Toda a comunicação com o banco será feita automaticamente pela Kobana.

Para concluir a autorização do CNAB Automático:

1. Preencha os dados para gerar a carta de autorização. Essa carta será enviada por e-mail ao banco e permitirá que a Kobana faça a troca de arquivos. Os e-mails informados também receberão uma cópia da carta e uma apresentação sobre a Kobana.
2. Fale com o gerente do seu banco. Isso ajuda a acelerar a ativação do serviço.
3. Aguarde a confirmação do banco. Você receberá um e-mail confirmando que o serviço foi ativado. Só após essa confirmação será possível seguir para o próximo passo.
4. Volte e finalize o credenciamento. Clique em **Habilitar** para concluir o processo.

**ℹ️ Nota**

Com a ativação do CNAB Automático, alguns bancos podem restringir o acesso manual aos arquivos de remessa e retorno no Internet Banking. Se quiser continuar acessando esses arquivos, consulte seu banco.

### Finalização

1. Ao avançar, a tela de **Resumo** é exibida. Confira atentamente todos os dados inseridos.
2. Com tudo correto, finalize o processo.

Após a finalização, acompanhe pela etapa **Selecionar conta** o status de cada modalidade. As modalidades com status **Credenciada** poderão ser operadas pelo Pague Rápido.

## Jornada de pagamento

Com a conta credenciada, o fluxo de pagamento acontece dentro da tela **Pague Rápido**. A tela organiza os títulos em cards que representam cada etapa, permitindo acompanhamento visual e ações rápidas.

### Quais títulos aparecem no Pague Rápido

Um título é exibido somente se atender a todos os critérios da sua modalidade:

| Critério | Boleto | PIX QR Code | PIX Chave | TED |
| --- | --- | --- | --- | --- |
| Tipo | Despesa | Despesa | Despesa | Despesa |
| Situação | Real | Real | Real | Real |
| Status | Pendente | Pendente | Pendente | Pendente |
| Campo de pagamento | Código de Barras informado na Movimentação Financeira | PIX Copia e Cola preenchido e válido na Movimentação Financeira | PIX Copia e Cola **não** preenchido; Chave PIX preenchida no cadastro do Parceiro vinculado ao título | Código de Barras, PIX Copia e Cola e Chave PIX **não** preenchidos; **Agência Bancária**, **Conta bancária parceiro** e Banco do parceiro preenchidos no cadastro do Parceiro vinculado ao título; Tipo de Título vinculado ao título com o campo **Tipo de pgto para NFC-e / NF-e / CF-e** = 18 |
| Subtipo do Tipo de Título | — | — | PIX | — |

**ℹ️ Nota**

Se o título tiver **Código de Barras** e **PIX Copia e Cola** preenchidos ao mesmo tempo, o tipo exibido será **PIX QR Code**. O sistema prioriza o PIX QR Code nesses casos.

### Classificação do Tipo de Chave PIX

Para títulos do tipo PIX Chave, o sistema calcula automaticamente o **Tipo Chave PIX** com base no conteúdo informado no cadastro do parceiro.

Quando o tipo não é identificado:

- O campo **Tipo Chave PIX** recebe o status **Indefinido** no Pague Rápido.
- Ao selecionar um título com Tipo Chave PIX = Indefinido e tentar programar o pagamento, o sistema exibe um alerta instruindo você a corrigir o campo antes de prosseguir.
- Após a correção para um tipo diferente de Indefinido, o botão **Programar Pagamento** fica disponível no próprio pop-up de validação.

### Regras para Pagamento TED

Para que seja possível realizar pagamentos via TED, é necessário atenção especial no preenchimento dos campos abaixo.

Para pagamentos via TED, o Tipo de Título vinculado ao lançamento precisa ter o campo **Tipo de pgto para NFC-e / NF-e / CF-e** configurado como **18 – TED (Transferência Eletrônica Disponível)** — essa exigência vale para qualquer lançamento, independentemente de ele ter sido originado por uma nota fiscal (NFC-e, NF-e ou CF-e) ou lançado manualmente.

#### Conta Bancária do Parceiro

Informe o número da conta concatenado ao dígito verificador, sem utilizar hífens, pontos ou qualquer outro caractere de formatação.

**Exemplo:** para a conta **1212-5**, informe no campo **Conta bancária parceiro** do ERP: **12125**.

#### Agência Bancária

Informe o número da agência concatenado ao dígito verificador, quando existente, sem utilizar hífens, pontos ou qualquer outro caractere de formatação

**Exemplo:** para a agência **0101-4**, informe no campo **Agência Bancária** do ERP: **01014**.

### Programar pagamento

Esta é a primeira etapa da jornada. Você seleciona os títulos que quer pagar e define os parâmetros de envio ao banco.

![Imagem 11: Esta é a primeira etapa da jornada. Você seleciona os títulos que quer pagar e define os parâmetros de envio ao banco.](https://ajuda.sankhya.com.br/hc/article_attachments/41186451706647)

1. No card **Em aberto**, selecione um ou mais títulos.
2. Clique em **Programar Pagamento**.
3. Preencha a **Data do pagamento**, a **Conta bancária pagadora** e **Observação** (opcional) e clique em **Confirmar**.

![Imagem 12: Preencha a Data do pagamento , a Conta bancária pagadora e Observação (opcional) e clique em Confirmar .](https://ajuda.sankhya.com.br/hc/article_attachments/41186466960023)

**Regras de conta bancária:**

- São exibidas apenas contas com status **Credenciada** para a modalidade do(s) título(s) selecionado(s).
- Se os títulos selecionados forem de modalidades diferentes, apenas contas credenciadas para todas as modalidades selecionadas serão exibidas.
- Se não existir conta credenciada para todas as modalidades selecionadas, o sistema exibe a mensagem: "Não foi encontrada nenhuma conta que esteja credenciada para todos os tipos de pagamento selecionados."

O título vai para o card **Aguardando Autorização** e o fluxo de liberação tem início.

### Liberação

Após a programação, o pagamento aguarda a aprovação dos usuários liberadores configurados no credenciamento da conta.

![Imagem 13: Após a programação, o pagamento aguarda a aprovação dos usuários liberadores configurados no credenciamento da conta.](https://ajuda.sankhya.com.br/hc/article_attachments/41186451708823)

O usuário com perfil de liberador precisa acessar o Pague Rápido, selecionar o(s) título(s) no card **Aguardando Autorização** e clicar em **Autorizar** ou **Negar**.

Poderão ser exigidas até 3 liberações, conforme a configuração definida no credenciamento. Na coluna **Ações**, o ícone de histórico permite consultar o registro de todas as liberações daquele título.

![Imagem 14: Poderão ser exigidas até 3 liberações, conforme a configuração definida no credenciamento. Na coluna Ações , o ícone de…](https://ajuda.sankhya.com.br/hc/article_attachments/41186451709719)

- **Se o pagamento for negado:** o título vai para o card **Erro no Pagamento** com status **Negado**. Se necessário iniciar um novo fluxo de pagamento, acesse [**Gerar novo pagamento**](https://ajuda.sankhya.com.br/hc/pt-br/articles/41186451711895-Pague-R%C3%A1pido-Fintech#novo-pagamento).
- **Se todas as liberações forem aprovadas:** o envio ao banco acontece automaticamente.

### Envio ao banco

Após a aprovação, o título transita de **Autorizado** para **Enviado para pagamento**, podendo existir status intermediários conforme o comportamento de cada banco (exemplo: Aguardando aprovação, Agendado, Aguardando data agendada).

Processado o pagamento, o status será atualizado para **Pago** (se pagamento confirmado) ou o título constará no card **Erro no Pagamento** com algum status de falha retornado pelo banco. Quando o banco detalhar a causa, ela constará no campo **Justificativa de erro**.

### Cancelar pagamento

É possível solicitar o cancelamento de pagamentos junto ao banco, desde que o pagamento não tenha sido confirmado.

1. Selecione o pagamento no card **Enviado para Pagamento**.
2. Clique em **Cancelar Pagamento**.

- Se o banco não aceitar a operação ou houver alguma falha na solicitação, o status será atualizado para **Falha no cancelamento** e o motivo será apresentado na coluna **Justificativa de erro**.
- Se a solicitação for aceita, o status será atualizado para **Cancelado**.
- Na linha do tempo será possível visualizar o histórico desta operação.
- Existem bancos não preparados para este serviço de cancelamento; neste caso, a falha será apresentada.

![Imagem 15: Existem bancos não preparados para este serviço de cancelamento; neste caso, a falha será apresentada.](https://ajuda.sankhya.com.br/hc/article_attachments/41235382934935)

### Exclusão de títulos do fluxo

Você pode remover um título do fluxo de automação sem excluir o registro original no Sankhya Om. O botão **Excluir** (ícone de lixeira) aparece somente quando há títulos com status **Em aberto** selecionados.

Ao excluir: o título continua existindo na Movimentação Financeira, mas sai do fluxo de automação.

![Imagem 16: Ao excluir: o título continua existindo na Movimentação Financeira, mas sai do fluxo de automação.](https://ajuda.sankhya.com.br/hc/article_attachments/41235382935831)

**🚨 Risco operacional**

A exclusão é irreversível dentro do Pague Rápido. O título não retorna ao fluxo após ser excluído por essa opção.

### Pagamentos expirados

Um pagamento é considerado expirado quando a data de pagamento venceu e o título ainda não foi enviado ao banco. Esse é um status interno do sistema — não está relacionado à rejeição do banco.

- O título recebe o status **Expirado**.
- O fluxo é encerrado sem tentativa de envio ao banco.
- O título aparece no card **Erro no Pagamento**.
- O campo **Justificativa Falha Pagamento** registra: "Data de Pagamento Expirada".
- Se necessário iniciar um novo fluxo, acesse [**Gerar novo pagamento**](https://ajuda.sankhya.com.br/hc/pt-br/articles/41186451711895-Pague-R%C3%A1pido-Fintech#novo-pagamento).

### Gerar novo pagamento

Quando um pagamento não é concluído por negação, rejeição, cancelamento ou expiração, você pode iniciar um novo fluxo sem recriar o título.

![Imagem 17: Quando um pagamento não é concluído por negação, rejeição, cancelamento ou expiração, você pode iniciar um novo fluxo…](https://ajuda.sankhya.com.br/hc/article_attachments/41235382937495)

**Quando está disponível:** somente para títulos nos status abaixo:

- Expirado
- Negado
- Rejeitado
- Cancelado

Ao clicar em **Gerar novo pagamento**, o sistema cria um novo registro com status **Em aberto**, replicando os dados do pagamento original. O fluxo segue normalmente a partir daí.

**Duas restrições importantes:**

- Títulos cancelados na origem — por exclusão, baixa ou alteração no Sankhya Om — não permitem gerar novos pagamentos.
- Pagamentos já reabertos não podem ser reabertos novamente.

## Baixa automática

Quando o banco confirma o pagamento e o status passa para **Pago**, o sistema realiza a baixa automaticamente — se essa opção estiver configurada no credenciamento da conta.

Se o valor pago for diferente do valor líquido registrado no Sankhya Om, o sistema faz o ajuste:

- **Valor pago menor que o valor líquido:** diferença lançada em **Valor Desconto**.
- **Valor pago maior que o valor líquido:** diferença lançada em **Valor Juros**.

Você acompanha o resultado no campo **Baixa via API** da Movimentação Financeira:

- **Sucesso:** "Título baixado automaticamente via API"
- **Falha:** o campo registra o motivo da falha.

## Conciliação bancária

Após a confirmação do pagamento pelo banco, a conciliação ocorre automaticamente — se essa opção estiver ativa no credenciamento da conta.

## Linha do tempo

Na coluna **Ações** de cada título, o ícone de linha do tempo registra as principais operações da jornada de pagamento. É por meio dela que você rastreia tudo o que aconteceu — de ponta a ponta.

Exemplos de registros que aparecem na linha do tempo:

- Aguardando liberação
- Autorizado
- Enviado para Pagamento
- Pago
- Erro no pagamento
- Cancelamento solicitado

![Imagem 18: Cancelamento solicitado](https://ajuda.sankhya.com.br/hc/article_attachments/41240991542807)

## Baixa, exclusão e alteração de títulos no ERP

Títulos que estejam na jornada de pagamentos e sofram exclusão, baixa ou remoção do campo de pagamento no ERP (Código de Barras ou PIX Copia e Cola) serão tratados conforme as regras abaixo para cada status.

### Aguardando Autorização e Erro no Pagamento

- O status será atualizado para **Cancelado**, com observação **Cancelado Origem**.
- O título será exibido no card **Erro no Pagamento**.
- A linha do tempo apresentará o registro do cancelamento.
- O campo **Justificativa falha pagamento** será preenchido com as informações do cancelamento.
- O pagamento não poderá mais ser processado pelo Pague Rápido.

### Enviado para Pagamento

- Será realizada solicitação automática de cancelamento junto ao banco.
- O acompanhamento do processo poderá ser feito por meio do status, indicando sucesso ou falha no cancelamento.

### Alteração do campo de pagamento

Ao alterar o campo de pagamento de um título com status **Enviado para Pagamento** (Código de Barras para Boleto, PIX Copia e Cola para PIX QR Code):

- O pagamento vinculado ao dado anterior entra no fluxo de cancelamento, sendo possível acompanhar pela coluna **Status** se o cancelamento será ou não aceito pelo banco.
- O campo **Observação** constará como **Cancelado Origem**, não permitindo gerar novo pagamento a partir deste título.
- Um novo pagamento é aberto com o novo código de pagamento, permitindo refazer o fluxo normalmente.

**🚨** **Proteções contra inconsistência**

- Títulos já pagos via Pague Rápido não podem ser excluídos no Sankhya Om.
- Títulos já pagos via Pague Rápido não podem ter o campo de pagamento alterado ou removido (Código de Barras ou PIX Copia e Cola).
- Essas restrições preservam a integridade do histórico financeiro e da rastreabilidade junto ao banco.

## Pontos de atenção

- O credenciamento é feito uma vez por conta, mas exige perfil gerencial. Garanta que o usuário responsável tenha esse perfil antes de começar.
- A elegibilidade do título varia por modalidade. Se um título não aparecer no Pague Rápido, verifique os campos exigidos para a modalidade correspondente.
- Títulos com **Código de Barras** e **PIX Copia e Cola** preenchidos ao mesmo tempo entram como **PIX QR Code**. O sistema prioriza o PIX QR Code nesses casos.
- O campo **Tipo Chave PIX** pode ficar como **Indefinido** quando o sistema não consegue classificar a chave automaticamente. Corrija-o manualmente ao programar o pagamento.
- Apenas contas credenciadas para todas as modalidades selecionadas aparecem no dropdown. Para lotes mistos (ex: Boleto + PIX QR Code), a conta precisa estar credenciada para ambas.
- A exclusão de um título do Pague Rápido é irreversível. O título sai do fluxo permanentemente — mas continua existindo no Sankhya Om.
- Títulos já pagos via Pague Rápido não podem ser excluídos nem ter o campo de pagamento alterado no Sankhya Om. Qualquer tentativa será bloqueada pelo sistema.
- Pagamentos expirados, negados, rejeitados ou cancelados podem ser reabertos via **Gerar novo pagamento** — exceto os cancelados na origem (por exclusão, baixa ou alteração no Sankhya Om).
