---
id: "44393057288215"
titulo: "Como finalizar um evento ou informar o número do recibo na Central do eSocial"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44393057288215-Como-finalizar-um-evento-ou-informar-o-n%C3%BAmero-do-recibo-na-Central-do-eSocial"
trilha: "Manual do Produto > Pessoas+ > eSocial > Eventos Periódicos e Fechamento do eSocial"
atualizado_em: "2026-10-21T11:44:02Z"
rotulos: ["br.com.sankhya.CentraleSocial", "Central do eSocial", "Portal do eSocial", "Finalizar Evento"]
---

# Como finalizar um evento ou informar o número do recibo na Central do eSocial

**Módulo:** Pessoas+
**Caminho de acesso:** Pessoal+ > Rotinas Folha > Central do eSocial
**ID da tela:** br.com.sankhya.CentraleSocial

---

### Sumário

- [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/44393057288215-Como-finalizar-um-evento-ou-informar-o-n%C3%BAmero-do-recibo-na-Central-do-eSocial#o-que-e)
- [Antes de começar](https://ajuda.sankhya.com.br/hc/pt-br/articles/44393057288215-Como-finalizar-um-evento-ou-informar-o-n%C3%BAmero-do-recibo-na-Central-do-eSocial#antes-de-comecar)
- [Jornada de uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/44393057288215-Como-finalizar-um-evento-ou-informar-o-n%C3%BAmero-do-recibo-na-Central-do-eSocial#jornada-de-uso)
- [Pontos de atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/44393057288215-Como-finalizar-um-evento-ou-informar-o-n%C3%BAmero-do-recibo-na-Central-do-eSocial#pontos-de-atencao)
- [Perguntas frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/44393057288215-Como-finalizar-um-evento-ou-informar-o-n%C3%BAmero-do-recibo-na-Central-do-eSocial#perguntas-frequentes)

---

### O que é e para que serve

Todo evento processado com sucesso pelo eSocial recebe um **número de recibo**. A **Central do eSocial** guarda esse número e o usa para acompanhar o evento, retificá-lo, excluí-lo e liberar outras rotinas da folha.

Em algumas situações, o evento é processado pelo eSocial, mas o número de recibo não volta para o sistema. Isso pode acontecer, por exemplo, quando o envio é cancelado antes de terminar ou quando o evento foi transmitido por fora do sistema. Nesses casos, o evento fica sem recibo na Central do eSocial, mesmo estando aceito no Portal do eSocial.

A opção **Alterar Dados** permite corrigir essa situação de duas formas:

- **Finalizar Evento:** informa o número do recibo de um evento que foi processado pelo eSocial, mas ficou sem recibo no sistema.
- **Alterar Número de Recibo Anterior:** corrige o número do recibo anterior registrado para o evento.

Use este procedimento, por exemplo, quando a folha não puder ser reaberta porque um evento do eSocial está sem número de recibo.

### Antes de começar

- **Acesso à tela:** ter acesso à **Central do eSocial** (Pessoal+ > Rotinas Folha), liberado na tela **Acessos** (Configurações > Controle de Acesso) pelo usuário administrador do sistema.
- **Acesso ao Portal do eSocial:** ter acesso ao Portal do eSocial com o certificado digital da empresa, para consultar o número do recibo de cada evento.
- **Evento processado com sucesso:** confirmar no Portal do eSocial que o evento foi aceito. Se o evento não consta no Portal, ele deve ser enviado novamente, e não finalizado.

### Jornada de uso

#### 1. Consulte o número do recibo no Portal do eSocial

1. Acesse o Portal do eSocial com o certificado digital da empresa.
2. Localize o evento pelo tipo, pelo período de apuração e, quando for um evento do trabalhador, pelo CPF.
3. Confirme que o evento foi processado com sucesso e anote o **número do recibo**.

Repita a consulta para cada evento que estiver sem recibo no sistema.

#### 2. Finalize o evento na Central do eSocial

[GIF animado: Imagem 1: 2. Finalize o evento na Central do eSocial](https://ajuda.sankhya.com.br/hc/article_attachments/44409425233687)

1. Acesse a **Central do eSocial** (Pessoal+ > Rotinas Folha).
2. Selecione a **Empresa** e a **Referência** do período de apuração do evento e clique em **Carregar**.
3. Habilite apenas os eventos que precisam ser ajustados.
4. Clique no evento. É exibida a lista de ações a serem incluídas ou alteradas.
5. Selecione a opção **Alterar Dados**.
6. No pop-up, escolha **Finalizar Evento** e informe o número do recibo consultado no Portal do eSocial.
7. Confirme a operação.

Depois da finalização, o evento passa a constar como processado na Central do eSocial, com o número de recibo informado.

| 🚨 **Risco operacional**  Informe somente o número de recibo de um evento que consta como processado com sucesso no Portal do eSocial e que corresponde exatamente ao evento selecionado na Central do eSocial.  Um recibo incorreto deixa o sistema diferente do eSocial e pode causar erros em retificações e exclusões futuras, como o **Erro 459** (evento não localizado para o recibo informado). |
| --- |

#### 3. Conclua a rotina que estava bloqueada

Depois de finalizar todos os eventos sem recibo, volte à rotina que estava bloqueada, como a reabertura da folha, e execute-a novamente.

📚 Para saber mais, acesse: [Como reabrir referências anteriores de folha de pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/39352384694039).

### Pontos de atenção

- A opção **Finalizar Evento** não envia nada ao eSocial. Ela apenas registra no sistema o recibo de um evento que o eSocial já processou.
- Se o evento não aparece no Portal do eSocial, ele não foi processado. Nesse caso, envie o evento novamente pela Central do eSocial.
- Faça o ajuste evento por evento, conferindo o tipo, o período de apuração e o trabalhador antes de informar o recibo.

### Perguntas frequentes

**1. Por que não consigo reabrir a folha?**

Uma das causas é existir evento do eSocial da competência sem número de recibo no sistema. Consulte o recibo no Portal do eSocial e finalize o evento pela opção **Alterar Dados > Finalizar Evento**. Depois, tente reabrir a folha novamente.

**2. Quando devo usar Alterar Número de Recibo Anterior em vez de Finalizar Evento?**

Use **Finalizar Evento** quando o evento está sem recibo. Use **Alterar Número de Recibo Anterior** quando o recibo anterior registrado para o evento está errado.

**3. Posso finalizar um evento que foi rejeitado pelo eSocial?**

Não. Eventos rejeitados não têm recibo. Corrija o erro apontado no retorno e envie o evento novamente.
