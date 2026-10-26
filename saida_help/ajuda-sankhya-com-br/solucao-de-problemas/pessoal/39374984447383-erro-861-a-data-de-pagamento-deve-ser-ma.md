---
id: "39374984447383"
titulo: "Erro 861: A data de pagamento deve ser maior ou igual ao mês anterior à rescisão do contrato de trabalho."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39374984447383-Erro-861-A-data-de-pagamento-deve-ser-maior-ou-igual-ao-m%C3%AAs-anterior-%C3%A0-rescis%C3%A3o-do-contrato-de-trabalho"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-08-07T14:33:11Z"
rotulos: ["Eventos", "eSocial", "Folha de Pagamento", "Rescisão", "Central do eSocial", "Erro", "Artigo criado KCS", "Sankhya RH - KCS"]
---

# Erro 861: A data de pagamento deve ser maior ou igual ao mês anterior à rescisão do contrato de trabalho.

**"[861]"** A data de pagamento deve ser maior ou igual ao mês anterior à rescisão do contrato de trabalho. Elemento: eSocial/evtPgtos/ideBenef/infoPgto/dtPgto

### SITUAÇÃO

Ao tentar enviar o **"Evento S-1210"** (Pagamentos de Rendimentos do Trabalho) para funcionários com rescisão contratual, o sistema retorna os erros **861** e **726**. Esta situação ocorre geralmente durante o fechamento da folha de pagamento ou ao processar pagamentos relacionados a rescisões contratuais.

### SOLUÇÃO

Para resolver os erros **861** e **726**, siga os passos abaixo:

**(1)** Acesse a tela **"Central do eSocial"** (Pessoal+ » Rotinas Folha » Central do eSocial) e verifique se existe algum **"Evento S-2299"** (Desligamento) pendente de envio ou retificação para o funcionário em questão.

**(2)** Caso identifique o **S-2299** pendente, realize o envio ou a retificação deste evento antes de tentar enviar o **S-1210**.

**(3)** Após o **S-2299** ser recepcionado com sucesso pelo eSocial, gere novamente o **S-1210** para o funcionário.

**(4)** Envie o **S-1210** e verifique se o evento foi recepcionado com sucesso, sem apresentar os erros **861** e **726**.

**Observação importante:** Em casos de rescisão complementar, certifique-se de que todos os eventos relacionados à rescisão (**S-2299**) e à remuneração (**"Evento S-1200"**) foram enviados antes do evento de pagamento (**S-1210**).

### CAUSA

Os erros **861** e **726** ocorrem quando o sistema tenta enviar o **S-1210** sem que o **S-2299** correspondente tenha sido previamente enviado ou esteja com retificação pendente no eSocial.

O eSocial exige que a sequência de envio dos eventos seja respeitada: primeiro deve ser enviado o evento de desligamento (**S-2299**), para depois ser possível enviar os eventos de pagamento relacionados à rescisão (**S-1210**). Quando esta ordem não é seguida, o sistema rejeita o **S-1210** com os códigos **861** e **726**, indicando que não localizou o evento de rescisão contratual correspondente.

Além disso, o erro pode ocorrer quando há uma retificação pendente do evento **S-2299** que ainda não foi transmitida ao portal do eSocial.
