---
id: "42430134787479"
titulo: "Ativar envio de Mensagem MMLite"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430134787479-Ativar-envio-de-Mensagem-MMLite"
trilha: "NEPPO: Personalização de atendimento > Omnichannel"
atualizado_em: "2026-08-11T16:57:37Z"
rotulos: ["sync_hc", "neppo", "neppo_392036362", "sync_hash_2fd1f08772bd"]
---

# Ativar envio de Mensagem MMLite

**O MM Lite é a API otimizada do 360dialog para envio de mensagens de marketing (Marketing Messages).**
Oferece TTL, métricas avançadas, eventos de clique e melhor desempenho para campanhas. Para habilitar, o cliente deve aceitar os termos no Business Manager.

## Antes de iniciar, verifique se todos os requisitos abaixo estão atendidos:

- O Business Manager possui **ao menos uma Ad Account ativa**
- O responsável pelo onboarding é **Administrador do BM**
- O mesmo usuário é **Admin de todas as WABAs** envolvidas
- A conta 360dialog está ativa e funcional (API Key, Webhook etc.)

Parceiros **NÃO** podem aceitar os termos. Isso deve ser feito **EXCLUSIVAMENTE** pelo cliente (admin do BM).

## Como habilitar o MM Lite na Meta

**Self-Onboard via WhatsApp Manager (Recomendado)**

Este é o método oficial recomendado pela Meta e pelo 360dialog. Click aqui

## Como habilitar o envio pelo MM Lite no gateway

## Cadastrar parâmetro

1. Acesse o **Gateway Manager**
2. No menu **Tipos de Gateway**, edite o **DIALOG\_360\_CLOUD**.
3. Adicione o parâmetro **useMMLite** com tipo **boolean** e clique em **Salvar**.

![Imagem 1: Adicione o parâmetro useMMLite com tipo boolean e clique em Salvar .](https://ajuda.sankhya.com.br/hc/article_attachments/42639453607447)

## Habilitar o parâmetro

1. Acesse o **Gateway Manager**
2. No menu **Clientes**, selecione o cliente em que o gateway está cadastrado.
3. Marque o **checkbox** referente ao parâmetro **useMMLite**.

![Imagem 2: Marque o checkbox referente ao parâmetro useMMLite .](https://ajuda.sankhya.com.br/hc/article_attachments/42639427840023)

Com o parâmetro **useMMLite** habilitado, todos os envios deste gateway classificados como **Marketing** são enviados automaticamente pelo endpoint **MM Lite**.

## Como verificar se o envio foi feito corretamente pelo MM Lite

Analisar os logs do **WhatsApp Gateway Multitenant** e verificar os eventos de status de envio que devem incluir o valor **"marketing\_lite"**, indicando que a mensagem foi enviada por meio da **API MMLite**. Ex:

```
{
  "object": "whatsapp_business_account",
  "entry": [
    {
      "id": "WHATSAPP_BUSINESS_ACCOUNT_ID",
      "changes": [
        {
          "value": {
            "messaging_product": "whatsapp",
            "metadata": {
              "display_phone_number": "BUSINESS_DISPLAY_PHONE_NUMBER",
              "phone_number_id": "BUSINESS_PHONE_NUMBER_ID"
            },
            "statuses": [
              {
                "id": "<WHATSAPP_MESSAGE_ID>",
                "status": "sent",
                "timestamp": "TIMESTAMP",
                "recipient_id": "<CUSTOMER_PHONE_NUMBER>",
                "conversation": {
                  "id": "<conversation_id>",
                  "expiration_timestamp": "TIMESTAMP",
                  "origin": {
                    "type": "marketing_lite"
                  }
                },
                "pricing": {
                  "billable": true,
                  "pricing_model": "CBP",
                  "category": "marketing_lite"
                }
              }
            ]
          },
          "field": "messages"
        }
      ]
    }
  ]
}
```
