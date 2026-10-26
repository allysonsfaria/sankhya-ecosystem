---
id: "42430063644695"
titulo: "WhatsApp Voice - Entrada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430063644695-WhatsApp-Voice-Entrada"
trilha: "NEPPO: Personalização de atendimento > Omnichannel"
atualizado_em: "2026-08-11T16:57:08Z"
rotulos: ["sync_hc", "neppo", "neppo_361725954", "sync_hash_fda77240de49"]
---

# WhatsApp Voice - Entrada

Essa documentação será alterada quando houver o lançamento da central de canais

Essa é uma documentação exclusiva para o time interno da Neppo. Não compartilhar com os clientes.

O objetivo dessa configuração é **habilitar o uso de chamadas de voz via WhatsApp** em um número específico, garantindo:

- Comunicação direta com clientes através de voz integrada ao WhatsApp.
- Centralização das chamadas dentro da infraestrutura da empresa (FreeSWITCH).
- Garantia de segurança (TLS/certificados) e confiabilidade na entrega.
- Cumprimento de requisitos da Meta e do provedor 360dialog.

Em resumo: **permitir que o número de WhatsApp Voice seja usado em produção de forma segura, validada e suportada tecnicamente**.

![Imagem 1: Em resumo: permitir que o número de WhatsApp Voice seja usado em produção de forma segura, validada e suportada…](https://ajuda.sankhya.com.br/hc/article_attachments/42639451207447)

---

## Visão geral do fluxo

1. **Meta Business**: habilitação inicial do número de voz.
2. **360dialog**: configuração do tronco SIP e API Key.
3. **FreeSWITCH**: implementação do trunk, rotas e certificados.
4. **Validação**: testes de chamada, checagem de áudio e ajuste final.

---

## Etapas técnicas

### Habilitação no Meta Business

- Acessar a conta **Meta Business Manager**.
- Habilitar o número de voz desejado.
- Confirmar que o número aparece como ativo para WhatsApp Voice.
- Esse passo é pré-requisito obrigatório para qualquer configuração posterior.

**Resultado esperado**: número disponível e apto para ser integrado via API.

---

### Configuração do Tronco SIP no 360dialog

- Acessar a documentação oficial:

  - Setup inicial
  - Configuração SIP
- Exemplo de configuração JSON:

  ```
  {
    "calling": {
      "sip": {
        "status": "ENABLED",
        "servers": [
          {
            "hostname": "SIP_SERVER_HOSTNAME",
            "port": "SIP_SERVER_PORT",
            "request_uri_user_params": {
              "KEY1": "VALUE1",
              "KEY2": "VALUE2"
            }
          }
        ]
      }
    }
  }
  ```
- Adicionar o **header de autenticação**:

  ```
  D360-API-KEY: xxxxxxxx
  ```

**Resultado esperado**: tronco SIP ativo no 360dialog, aguardando integração com FreeSWITCH.

---

### Configuração de TLS e Certificados

- O tronco SIP exige **TLS (Transport Layer Security)** habilitado.
- Ajustes necessários:

  1. Validar hostname configurado.
  2. Incluir certificados corretos no FreeSWITCH.
  3. Confirmar que a conexão TLS se estabelece sem erro.
- Documentação de apoio:
  [Exemplo de configuração SIP-TLS no FreeSWITCH](https://developer.signalwire.com/freeswitch/FreeSWITCH-Explained/Security/SIP-TLS_9634135/)

**Resultado esperado**: comunicação segura e confiável entre FreeSWITCH e 360dialog.

---

### Configuração no FreeSWITCH

- Criar o tronco SIP apontando para o servidor do 360dialog.
- Definir **rotas de entrada e saída** para chamadas.
- Mapear os parâmetros necessários (usuário, chave, porta).

**Resultado esperado**: FreeSWITCH apto a enviar e receber chamadas via WhatsApp Voice.

---

### Testes de validação

- Realizar chamadas de teste (via Fusion).
- Verificar:

  - Conexão estabelecida.
  - **Áudio bidirecional funcionando**.
  - Logs de FreeSWITCH confirmando fluxo correto.
- Ajustar parâmetros de áudio, codecs e rotas se necessário.

**Resultado esperado**: chamadas de voz operacionais e aprovadas em ambiente de QA.

---

## Resumo do processo

- **Negócio**: habilitar comunicação por voz integrada ao WhatsApp, garantindo experiência fluida com clientes.
- **Técnico**: configurar o número no Meta Business, ajustar SIP no 360dialog, implementar TLS e rotas no FreeSWITCH, validar tráfego com testes de áudio.

---

## Checklist rápido

- Número habilitado no **Meta Business**.
- Tronco SIP configurado no **360dialog** com API Key.
- TLS e certificados validados.
- Trunk configurado no **FreeSWITCH**.
