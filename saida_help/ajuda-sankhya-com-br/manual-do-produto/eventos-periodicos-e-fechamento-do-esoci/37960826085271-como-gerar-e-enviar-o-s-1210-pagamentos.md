---
id: "37960826085271"
titulo: "Como gerar e enviar o S-1210 (Pagamentos)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37960826085271-Como-gerar-e-enviar-o-S-1210-Pagamentos"
trilha: "Manual do Produto > Pessoas+ > eSocial > Eventos Periódicos e Fechamento do eSocial"
atualizado_em: "2026-10-20T18:45:12Z"
rotulos: ["Eventos", "Pagamentos", "eSocial", "br.com.sankhya.CentraleSocial", "Folha de Pagamento", "Central do eSocial", "Evento S-1210", "Pessoal+"]
---

# Como gerar e enviar o S-1210 (Pagamentos)

**Módulo:** Pessoal+
**Caminho de Acesso:** Pessoal+ > Rotinas Folha > Central do eSocial
**ID da Tela:** br.com.sankhya.CentraleSocial

---

### O que é e para que serve

O evento **S-1210 – Pagamentos de Rendimentos do Trabalho** é utilizado para informar ao eSocial os **valores efetivamente pagos** aos trabalhadores.

Diferente do S-1200, que informa a **remuneração devida**, o S-1210 registra o **pagamento realizado**, considerando datas, valores líquidos e formas de pagamento.

Esse evento é essencial para:

- Comprovar o pagamento dos rendimentos;
- Validar o recolhimento correto de **INSS, FGTS e IRRF**;
- Garantir a consistência das informações financeiras e trabalhistas no eSocial.

### Quem está obrigado

Devem enviar o evento **S-1210** todas as empresas e empregadores obrigados ao eSocial que realizam **pagamento de remuneração** a trabalhadores.

O envio é obrigatório sempre que houver:

- Pagamento de salário;
- Pagamento de férias;
- Pagamento de rescisão;
- Qualquer outro rendimento informado previamente no S-1200.

### Prazo de envio

O evento **S-1210 deve ser enviado na referência do pagamento**, ou seja, no mês em que o valor foi **efetivamente pago ao trabalhador**.

Por isso, antes de gerar o S-1210, verifique se a **Data de Pagamento** informada na folha corresponde à competência em que o pagamento foi efetivamente realizado.

Por exemplo:

- a folha da **competência de janeiro** foi calculada normalmente;
- o pagamento ocorreu em **fevereiro** (regime de caixa);
- Nesse cenário:
  - o **S-1200** é enviado com a **competência de janeiro**;
  - o **S-1210** é enviado com a **referência de fevereiro**, que é o mês do pagamento.

O envio do S-1210 deve respeitar o prazo legal do eSocial, que é:

- **Até o dia 15 do mês seguinte** ao da competência;
- Quando o dia 15 não for dia útil, o prazo é antecipado.

💡 O S-1210 deve ser enviado **antes do fechamento da folha**, realizado pelo evento S-1299.

### Pré-requisitos

Antes de gerar e enviar o evento S-1210, é necessário que os seguintes eventos já tenham sido enviados e aceitos no eSocial:

- **S-1000 – Informações do Empregador**
- **S-1005 – Estabelecimentos**
- **S-1010 – Tabela de Rubricas**
- **S-1020 – Lotações Tributárias**
- **S-1200 – Remuneração do Trabalhador**
- **S-2299 – Desligamento**, para colaboradores desligados cujo pagamento da rescisão será informado no S-1210.

Além disso, é necessário:

- Folha de pagamento **calculada e paga** no sistema;
- Informações bancárias ou de pagamento corretamente registradas;
- Certificado digital válido;
- Ambiente do eSocial configurado em Produção.

| **⚠️** **Atenção**  Antes de gerar ou reenviar o S-1210, confira na **Central do eSocial**, menu **Acompanhamento**, se:   - o **S-1200** da competência está com status de aceito pelo eSocial; - para colaboradores desligados, o **S-2299** foi enviado e aceito, e não está pendente.   Se algum desses eventos estiver pendente ou rejeitado, o S-1210 do colaborador não é processado com sucesso. Corrija e reenvie primeiro o evento pendente. |
| --- |

### Jornada de Uso

[GIF animado: Imagem 1: Jornada de Uso](https://ajuda.sankhya.com.br/hc/article_attachments/37961299035799)

**Gerar o evento S-1210**

1. Acesse a **Central do eSocial** (Pessoal+ > Rotinas Folha).
2. Selecione a **Empresa** e a **Referência.**
3. Certifique de que o **Ambiente** esteja em**Produção.**
4. Clique em **Carregar**.
5. No menu lateral, clique em **Geração**.
6. Clique sobre o card **Selecionar Eventos** e em seguida no evento **S-1210 – Pagamentos de Rendimentos do Trabalho.**
7. Clique em **Iniciar Geração**.

O sistema irá gerar um evento S-1210 para cada trabalhador que teve pagamento registrado na competência.

**Enviar o evento ao eSocial**

1. Após a conclusão da geração, o evento S-1210 será exibido no menu **Eventos Pendentes**.
2. Clique no botão **Habilitar/Desabilitar todos** para **desabilitar todos os eventos** gerados.
3. Habilite a opção **Enviar** no card do evento **S-1210 – Pagamentos de Rendimentos do Trabalho**.
4. Ative a opção **Utilizar a data de início padrão do sistema** e clique em **Enviar Dados**.
5. Acompanhe o processo de envio no menu **Eventos na Fila**.
6. Após o envio, o evento passa para o menu **Acompanhamento**, onde é possível verificar:
   - status do envio;
   - retorno do eSocial;
   - mensagens de erro ou rejeição, se houver.
7. Clique sobre o card correspondente para ver os detalhes do retorno do eSocial.

   - Se o evento foi enviado com sucesso, será exibido o número do recibo.
   - Em caso de erro, o sistema exibirá a mensagem retornada pelo eSocial para ajuste da rubrica.

     [GIF animado: Imagem 2: Em caso de erro, o sistema exibirá a mensagem retornada pelo eSocial para ajuste da rubrica.](https://ajuda.sankhya.com.br/hc/article_attachments/37961299040535)
8. Para visualizar os XML de envio e retorno, poderá clicar em **Baixar Arquivos** ou em **Visualizar Dados**.

### Pontos de Atenção

- Antes de gerar o evento **S-1210**, confira se a **Data de Pagamento** da folha está registrada na competência correta.

  A data de pagamento determina a referência do pagamento informada no S-1210. Quando a folha possui uma **Data de Pagamento registrada em uma competência diferente da esperada**, o evento pode não ser gerado ou enviado corretamente ao eSocial.

  Caso a data de pagamento esteja incorreta, corrija a folha antes de realizar a geração do **S-1210**.
- O S-1210 está diretamente relacionado aos eventos:
  - **S-1200 – Remuneração**;
  - **S-2299 – Rescisão** (quando aplicável).
- Não é permitido enviar o S-1210 **sem o** **S-1200** aceito e recepcionado no eSocial.
- Ajustes no pagamento exigem **novo envio do S-1210**, mantendo o histórico.
- Erros comuns no S-1210 estão geralmente relacionados a:
  - divergência entre valores pagos e informados no S-1200;
  - pagamento não registrado no sistema;
  - data de pagamento registrada em competência diferente daquela em que o pagamento foi realizado ou esperada para o envio do S-1210;
  - rubricas ou eventos anteriores não enviados.
- Quando o retorno do eSocial apontar erro nas informações de **plano de saúde** de um colaborador:
  - se faltar o cadastro do plano de saúde para descontos já calculados na folha, utilize o reprocessamento do plano de saúde no Gerenciador de Folhas.

    📚 Para saber mais, acesse: [Como reprocessar o plano de saúde](https://ajuda.sankhya.com.br/hc/pt-br/articles/38167049533079);
  - se for preciso corrigir informações de plano de saúde já transmitidas no S-1210, utilize a tela **IRRF – Períodos Anteriores eSocial**, aba **Plano de Saúde**.

    **📚** Para saber mais, acesse: [Como corrigir o IRRF de anos anteriores no eSocial (S-1210)](https://ajuda.sankhya.com.br/hc/pt-br/articles/37272130595223).

Manter o S-1210 corretamente enviado garante a **consistência financeira da folha**, evita pendências no fechamento e reduz riscos de fiscalização.
