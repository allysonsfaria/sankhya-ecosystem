---
id: "44011200883223"
titulo: "Integração Meetime + WhatsApp + Salesforce"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011200883223-Integra%C3%A7%C3%A3o-Meetime-WhatsApp-Salesforce"
trilha: "Meetime > Integrações"
atualizado_em: "2026-10-05T18:58:56Z"
rotulos: ["sync_hc", "meetime", "sync_hash_b73707693811", "meetime_1288"]
---

# Integração Meetime + WhatsApp + Salesforce

A integração entre WhatsApp e Salesforce, permite que todas as conversas realizadas através do número corporativo de WhatsApp conectado à Meetime sejam registradas automaticamente dentro do Salesforce, em formato de Tarefas (Tasks).

Sempre que um usuário da Meetime envia ou recebe uma mensagem pelo WhatsApp, ocorre o seguinte fluxo:

1. A Meetime captura essa mensagem
2. O sistema identifica para qual Oportunidade, Contato, Conta ou Lead ela está vinculada no Salesforce
3. Em seguida, registra o histórico completo dentro do CRM

Dessa forma, o time comercial e os gestores conseguem visualizar, dentro do Salesforce, todo o histórico de conversas realizadas pelo WhatsApp corporativo. Isso garante rastreabilidade, centralização das interações no CRM e acompanhamento completo da comunicação, inclusive em estágios iniciais, antes mesmo da conversão de Leads.

## Pré-requisitos para funcionar

### 1. WhatsApp integrado ao Flow

A conta precisa estar conectada ao WhatsApp na Meetime Flow.

Para integrar, basta clicar no seu nome no canto superior direito da tela > Integrações > WhatsApp > Conectar WhatsApp

![Imagem 1: Para integrar, basta clicar no seu nome no canto superior direito da tela > Integrações > WhatsApp > Conectar WhatsApp](https://ajuda.sankhya.com.br/hc/article_attachments/44011225953943)

Para mais informações de como funciona a integração com WhatsApp, é só acessar o artigo [Integração WhatsApp e Meetime](https://cloudchat2.cloudhumans.com/hc/meetime/articles/1768594435-integracao-whats_app-e-meetime).

### 2. Habilitar integração com CRM

É preciso habilitar a integração com o CRM, acessando a página de integrações (mesma página do passo acima) e clicar em “Integre seu CRM”

![Imagem 2: É preciso habilitar a integração com o CRM, acessando a página de integrações (mesma página do passo acima) e clicar em…](https://ajuda.sankhya.com.br/hc/article_attachments/44011227825815)

### 3. Usuários conectados individualmente com Salesforce

Cada usuário precisa conectar sua própria conta do Salesforce a Meetime, através da conexão via OAuth.

É isso que permite preencher o campo “Atribuído” dentro do Salesforce.

### 4. Telefone com formato correto

O telefone precisa estar salvo no formato correto no Salesforce.

O formato que deve ser seguido é de números corridos, sem espaços e sem parênteses no DDD: **“45999099900”.**

Formatos que não funcionam: (47) 99909-9900, 47 99909-9900, 47-99909-9900.

Campos suportados no Salesforce:

- **Contato →** Telefone / Celular / OtherPhone / HomePhone
- **Conta →** Telefone
- **Lead** → Phone / MobilePhone

## Como a integração funciona?

1. O usuário envia ou recebe uma mensagem no WhatsApp pela Meetime
2. A integração captura e normaliza o número de telefone
3. O sistema procura esse número no Salesforce
4. Se encontrar mais de um registro, aplica as regras de prioridade
5. É criada uma tarefa no Salesforce com status “Completed”
6. A tarefa é atribuída ao usuário Meetime autenticado

⚠️ **O registro pode levar alguns minutos para aparecer no Salesforce.**

Tela de Conversas na Meetime:

![Imagem 3: Tela de Conversas na Meetime:](https://ajuda.sankhya.com.br/hc/article_attachments/44011212979607)

Tela de Contato no Salesforce:

![Imagem 4: Tela de Contato no Salesforce:](https://ajuda.sankhya.com.br/hc/article_attachments/44011260362135)

## Regras de decisão: onde a Task será registrada

A integração segue estritamente a seguinte ordem de prioridade:

### 1. Oportunidade aberta

- Quando há mais de uma oportunidade aberta, a mais recente será utilizada.
- A Task é registrada:
- no Contato
- e na Oportunidade relacionada

![Imagem 5: e na Oportunidade relacionada](https://ajuda.sankhya.com.br/hc/article_attachments/44011243777303)

### 2. Contato

Usado quando não há Oportunidade aberta associada.

![Imagem 6: Usado quando não há Oportunidade aberta associada.](https://ajuda.sankhya.com.br/hc/article_attachments/44011236140951)

### 3. Conta

Usado apenas quando não existe Contato com o telefone.

![Imagem 7: Usado apenas quando não existe Contato com o telefone.](https://ajuda.sankhya.com.br/hc/article_attachments/44011229066263)

### 4. Lead

Usado **somente quando o telefone não é encontrado** em:

- Oportunidades
- Contatos
- Contas

Nesse caso:

- A Task é registrada no **Lead**
- Não há vínculo com Conta ou Oportunidade

![Imagem 8: Não há vínculo com Conta ou Oportunidade](https://ajuda.sankhya.com.br/hc/article_attachments/44011214038295)

**Observações:**

‼️Se o mesmo telefone existir em um Lead e em um Contato, a Task será registrada no Contato. Isso ocorre porque a existência de um Contato indica um relacionamento já ativo com a empresa, tornando o registro no Lead desnecessário.

‼️Não registra em:

- Case
- Contract
- Outras entidades fora do fluxo acima
- Não cria entidades novas
- Não envia mensagens a partir do Salesforce

## Como as conversas aparecem no Salesforce?

As mensagens aparecem como **Tasks concluídas** com:

![Imagem 9: As mensagens aparecem como Tasks concluídas com:](https://ajuda.sankhya.com.br/hc/article_attachments/44011244813207)

- Ao criar na atividade no Salesforce, é assim que ela aparece:

![Imagem 10: Ao criar na atividade no Salesforce, é assim que ela aparece:](https://ajuda.sankhya.com.br/hc/article_attachments/44011245022487)

## Como a Meetime cria e atualiza as Tasks no Salesforce?

- Uma task representa uma conversa contínua no WhatsApp.
- Se o contato ficar 24h sem responder ou sem novas mensagens, a Meetime irá criar uma nova Task.
- O registro pode levar alguns minutos para aparecer no Salesforce, porque o processamento de mensagens acontece em ciclos contínuos.

---

Ainda tem dúvidas? Entre em contato com a gente através do 
e-mail [suporte@meetime.com.br](mailto:suporte@meetime.com.br) ou WhatsApp através do número de telefone [(48) 3204-7590](https://wa.me/554832047590).
