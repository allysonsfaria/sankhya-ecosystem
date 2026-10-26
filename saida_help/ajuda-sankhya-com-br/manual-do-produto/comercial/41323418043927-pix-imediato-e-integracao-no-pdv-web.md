---
id: "41323418043927"
titulo: "PIX Imediato e Integração no PDV Web"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/41323418043927-PIX-Imediato-e-Integra%C3%A7%C3%A3o-no-PDV-Web"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:35:12Z"
rotulos: ["Configuração", "Integração", "Financeiro", "PIX", "Sankhya ID", "PDV Web"]
---

# PIX Imediato e Integração no PDV Web

**Você encontra neste artigo:**

| [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/41323418043927-PIX-Imediato-e-Integra%C3%A7%C3%A3o-no-PDV-Web#oque) [Antes de começar](https://ajuda.sankhya.com.br/hc/pt-br/articles/41323418043927-PIX-Imediato-e-Integra%C3%A7%C3%A3o-no-PDV-Web#antes)    ↳ [Requisitos de versão e layout](https://ajuda.sankhya.com.br/hc/pt-br/articles/41323418043927-PIX-Imediato-e-Integra%C3%A7%C3%A3o-no-PDV-Web#requisitos)    ↳ [Bancos ativos](https://ajuda.sankhya.com.br/hc/pt-br/articles/41323418043927-PIX-Imediato-e-Integra%C3%A7%C3%A3o-no-PDV-Web#bancos)    ↳ [Permissões necessárias](https://ajuda.sankhya.com.br/hc/pt-br/articles/41323418043927-PIX-Imediato-e-Integra%C3%A7%C3%A3o-no-PDV-Web#permissoes) [Contratação do serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/41323418043927-PIX-Imediato-e-Integra%C3%A7%C3%A3o-no-PDV-Web#contratacao) | [Credenciamento da conta bancária](https://ajuda.sankhya.com.br/hc/pt-br/articles/41323418043927-PIX-Imediato-e-Integra%C3%A7%C3%A3o-no-PDV-Web#credenciamento) [Parametrização e uso do PIX no PDV Web](https://ajuda.sankhya.com.br/hc/pt-br/articles/41323418043927-PIX-Imediato-e-Integra%C3%A7%C3%A3o-no-PDV-Web#parametrizacao)    ↳ [Fluxo operacional no PDV Web](https://ajuda.sankhya.com.br/hc/pt-br/articles/41323418043927-PIX-Imediato-e-Integra%C3%A7%C3%A3o-no-PDV-Web#fluxo-pdv)    ↳ [Tratamento de exceções e mensagens no caixa](https://ajuda.sankhya.com.br/hc/pt-br/articles/41323418043927-PIX-Imediato-e-Integra%C3%A7%C3%A3o-no-PDV-Web#excecoes) [Pontos de atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/41323418043927-PIX-Imediato-e-Integra%C3%A7%C3%A3o-no-PDV-Web#pontos) [Perguntas frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/41323418043927-PIX-Imediato-e-Integra%C3%A7%C3%A3o-no-PDV-Web#faq) |
| --- | --- |

## O que é e para que serve

O **PIX Imediato** é uma solução Sankhya Fintech que gera um PIX de forma instantânea a partir de títulos de Receita Real em aberto na **Movimentação Financeira**. A solução também permite que as jornadas de varejo no **PDV Web** e no **Checkout** se comuniquem diretamente com a API de PIX da Fintech para gerar o QR Code automaticamente, substituindo a antiga API V1 do Banco do Brasil. O processo não substitui a emissão manual de boletos nem outras formas de recebimento configuradas na empresa.

- **Propósito** — agilizar o recebimento ao gerar um QR Code e um código "copia e cola" com validade de 24 horas, permitindo a liquidação e conciliação automática do título após o pagamento, tanto na rotina financeira padrão quanto nos caixas de varejo.
- **Valor para você** — comodidade ao cliente final, rapidez no pagamento, segurança e rastreabilidade total das transações comerciais.

---

## Antes de começar

Para utilizar o PIX Imediato, sua empresa e seu usuário precisam atender aos seguintes requisitos:

### Requisitos de versão e layout

- Contratação do Pacote Básico de serviços Fintech (Pacote Boleto Rápido)
- Versão ERP: `4.35b226` ou superior
- Versão BFF Financeiro: `1.20.1` ou superior
- Layout do sistema: Design System

### Bancos ativos

Atualmente, o PIX Imediato é compatível com os seguintes bancos:

- Banco do Brasil
- Banco Itaú
- Banco Santander
- Banco SICOOB

**ℹ️ Nota**

O Bradesco está em desenvolvimento.

### Permissões necessárias

- Sankhya ID ativado e conectado
- Permissão de gestor e acesso à tela **Contas** para contratação, descredenciamento e cancelamento do serviço
- Acesso à Baixa de Receita na rotina **Movimentação Financeira** para emissão do PIX

**ℹ️ Nota**

Usuários do tipo SUP não podem realizar o cancelamento do contrato.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/41323418043927-PIX-Imediato-e-Integra%C3%A7%C3%A3o-no-PDV-Web#sumario)

---

## Contratação do serviço

O serviço de PIX Imediato está incluso no mesmo Pacote de Serviços do Boleto Rápido.

- **Se sua empresa já tem o Boleto Rápido ativo** — as transações de PIX Imediato são incluídas na volumetria do pacote atual.
- **Se sua empresa não tem o serviço ativo** — é necessário contratar o pacote, que custa R$ 250,00/mês para até 1.500 transações, com transações excedentes cobradas à parte.

**Passos para contratação:**

1. Clique em **Quero conhecer** para ser direcionado ao Marketplace.
2. Em caso de dúvidas sobre o processo de contratação, acesse o documento Contratação e Cobrança dos serviços Fintech.

Com a contratação concluída, você segue para o credenciamento da conta bancária.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/41323418043927-PIX-Imediato-e-Integra%C3%A7%C3%A3o-no-PDV-Web#sumario)

---

## Credenciamento da conta bancária

O credenciamento ao PIX Imediato só é permitido após a contratação do serviço, descrita na seção anterior.

1. Acesse a tela **Assistente de Melhores Práticas**.
2. Na opção "Configurações serviços Fintech", escolha "PIX Integrado" e clique em **Iniciar**.
3. Selecione a conta bancária a ser credenciada na Etapa 1 e clique em **Avançar**.
4. Preencha os dados da conta (Agência, Dígito, Conta, CNPJ e Chave PIX) na Etapa 2. Se a conta já foi credenciada para Boleto Híbrido, os dados podem vir preenchidos — confira e avance.
5. Defina as ações automáticas (Etapa 3) para Baixa, Lançamento, TOP e Conciliação. É essencial informar o Tipo de Título na Baixa Automática (com Subtipo = PIX e Ativo) para identificar o recebimento.
6. Insira as credenciais (Client ID e Client Secret) fornecidas pelo seu banco (Etapa 4).
7. Na Etapa 5, confira o resumo das informações e clique em **Instalar** para finalizar o credenciamento. O Sankhya Om exibe a mensagem "Configuração realizada com sucesso".

**💡 Dica**

Configure a Baixa Automática e a Conciliação Automática para valores diferentes de "Não realizar". Com essa configuração, ao receber a confirmação do banco, o título na Movimentação Financeira é liquidado — baixado e conciliado — sem intervenção manual.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/41323418043927-PIX-Imediato-e-Integra%C3%A7%C3%A3o-no-PDV-Web#sumario)

---

## Parametrização e uso do PIX no PDV Web

Para receber pagamentos no ambiente de varejo através do PIX integrado com a API da Fintech, certifique-se de que a contratação e o credenciamento estejam **concluídos e ativos**.

### Fluxo operacional no PDV Web

1. **Lançamento e recebimento** — durante o fechamento de uma venda no PDV Web, ao avançar para a tela de formas de pagamento (atalho `[F7] Receber`), selecione a opção **PIX**.
2. **Geração do QR Code** — o Sankhya Om abre automaticamente o pop-up **"Receber com PIX"**, exibindo o QR Code exclusivo e o código Copia e Cola gerados pela API Fintech para aquela transação.
3. **Impressão opcional (PDF)** — no mesmo pop-up, clique em **Baixar PDF** para gerar um documento com o QR Code e os dados do PIX, útil para impressão ou compartilhamento físico com o pagador.
4. **Confirmação automática** — assim que o cliente paga, o status no caixa muda instantaneamente, exibindo a mensagem "PIX recebido com sucesso!" junto com o ID da transação. Clique em **Finalizar** para concluir a venda e emitir o cupom fiscal.

### Tratamento de exceções e mensagens no caixa

- **Cancelamento de operação** — se o cliente desistir do PIX antes de pagar, clique em **Cancelar PIX**. O Sankhya Om exibe a confirmação "Deseja realmente cancelar esta cobrança PIX?". Ao continuar, a ordem é revogada na API e o caixa é liberado.
- **Aviso de Tipo de Título inválido** — se não existir um Tipo de Título configurado para o PDV Web com o subtipo correto, você é alertado e o recebimento não prossegue até que a parametrização (Subtipo = PIX e Ativo) seja associada ao terminal.
- **Acompanhamento de falhas** — falhas de comunicação ou de preenchimento na requisição são exibidas no próprio pop-up de cobrança, impedindo a exibição de um QR Code incorreto e instruindo você a tentar novamente.
- **Validação no ERP** — após a venda, ao consultar o título gerado na Movimentação Financeira, o campo **"Baixa via API"** na aba Lançamento/Histórico estará populado com data, ID da transação e o histórico do ciclo de vida do PIX. Se a baixa automática falhar (por exemplo, lançamento inválido ou regra de transação), o motivo exato da falha aparece nesse mesmo campo — resolva o impeditivo indicado para que o job do sistema conclua a baixa nas próximas tentativas.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/41323418043927-PIX-Imediato-e-Integra%C3%A7%C3%A3o-no-PDV-Web#sumario)

---

## Pontos de atenção

- **Conta utilizada no PDV Web para gerar o PIX** — ao processar um pagamento PIX pelo PDV Web, o sistema define automaticamente qual conta bancária será utilizada seguindo uma ordem de prioridade:

  - primeiro a **conta credenciada na Fintech PIX** (quando ativa);

  - depois a **conta do PDV identificado** e, por último;

  - a **conta do caixa aberto do operador**. 
  Quando a Fintech PIX está ativa, ela assume controle total: **a conta do título financeiro deve ser exatamente a mesma cadastrada no wizard de configuração da Fintech/PIX**. Caso contrário, a cobrança não é criada e o sistema exibe um erro de vínculo de conta. Para resolver, acesse o wizard, confirme qual conta está credenciada e verifique se o título está associado a essa mesma conta.
- **Validação dos dados bancários** — o Sankhya Om não valida os dados bancários (Agência, Conta, Chave PIX) junto ao banco no momento do credenciamento. Confirme todas as informações com o gerente do banco antes de credenciar, para evitar falhas na emissão.
- **Cobrança do serviço** — o PIX Imediato é cobrado através do mesmo pacote do Boleto Rápido. A contagem de transações inclui todos os recebimentos liquidados via código de barras, QR Code do boleto e QR Code do PIX Imediato.
- **Descredenciamento da conta** — para remover uma conta dos serviços, acesse a tela Contas, selecione a conta credenciada, clique em "Descredenciar conta" e confirme. Mesmo com todas as contas descredenciadas, o contrato e a cobrança mensal continuam ativos.
- **Cancelamento do contrato (interrupção da cobrança)** — para interromper a cobrança da Sankhya Fintech, acesse a etapa "Seleção de Contas" no Credenciamento PIX (tela Assistente de Melhores Práticas), clique em "Cancelar contrato" e confirme. Isso descredencia todas as contas dos serviços de Boleto Rápido e PIX Imediato. O cancelamento não pode ser feito por usuários do tipo SUP, exige acesso à tela **Contas** e não está disponível em bases de treinamento.
- **Alteração do valor líquido** — se o valor líquido de um título com PIX ativo for alterado, o PIX anterior é cancelado automaticamente no banco. Um novo PIX deve ser gerado para o valor atualizado.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/41323418043927-PIX-Imediato-e-Integra%C3%A7%C3%A3o-no-PDV-Web#sumario)

---

## Perguntas frequentes

### O PIX Imediato está incluso na mensalidade padrão do ERP?

Não. Ele faz parte do Pacote Boleto Rápido da Sankhya Fintech, com cobrança mensal à parte (R$ 250,00/mês para até 1.500 transações, com taxa de excedente por transação acima do limite).

### O que acontece se eu alterar o valor líquido do título com o PIX já gerado?

O PIX gerado anteriormente é cancelado automaticamente no banco. É necessário gerar um novo PIX para que o cliente pague o valor atualizado.

### O Sankhya Om valida os dados bancários no momento do credenciamento?

Não. A validação junto ao banco não é feita no momento do cadastro. Confira todas as informações com seu gerente bancário antes de finalizar.

### O que significa o registro no campo "Baixa via API" da Movimentação Financeira?

Esse campo registra todo o histórico do ciclo de vida do PIX (recebido, cancelado ou expirado) e também os códigos de erro e motivos de falha, caso a baixa automática encontre algum problema.
