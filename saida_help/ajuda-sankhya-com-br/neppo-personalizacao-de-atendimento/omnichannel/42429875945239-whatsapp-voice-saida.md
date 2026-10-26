---
id: "42429875945239"
titulo: "WhatsApp Voice - Saída"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42429875945239-WhatsApp-Voice-Sa%C3%ADda"
trilha: "NEPPO: Personalização de atendimento > Omnichannel"
atualizado_em: "2026-08-11T16:56:54Z"
rotulos: ["sync_hc", "neppo", "neppo_302317569", "sync_hash_268e62e105b5"]
---

# WhatsApp Voice - Saída

Documentação oficial do procedimento de habilitação do recurso **WhatsApp Voz** dentro da plataforma Neppo.
O objetivo é orientar implantação, suporte, produto e parceiros na ativação correta do canal.

Essa é uma documentação exclusiva para o time interno da Neppo. Não compartilhar com os clientes.

[GIF animado: Imagem 1: Essa é uma documentação exclusiva para o time interno da Neppo. Não compartilhar com os clientes.](https://ajuda.sankhya.com.br/hc/article_attachments/42639399794839)

Versão neppochat-server 2.10.956 ou superior

Versão voice-gateway 2.5.80 ou superior

whatsapp-gateway-multitenant 1.0.57 ou superior

Link da API:

Indice:

- [Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429875945239-WhatsApp-Voice-Sa%C3%ADda#Configuracoes)
- [Habilitação em Configurar Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429875945239-WhatsApp-Voice-Sa%C3%ADda#Habilitacao-em-Configurar-Propriedades)
- [Habilitação no grupo de atendimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429875945239-WhatsApp-Voice-Sa%C3%ADda#Habilitacao-no-grupo-de-atendimento)
- [Área de atendimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429875945239-WhatsApp-Voice-Sa%C3%ADda#Area-de-atendimento)
- [Solicitar permissão de ligação](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429875945239-WhatsApp-Voice-Sa%C3%ADda#Solicitar-permissao-de-ligacao)
- [Realizar ligação](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429875945239-WhatsApp-Voice-Sa%C3%ADda#Realizar-ligacao)
- [Acompanhamento da permissão na conversa](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429875945239-WhatsApp-Voice-Sa%C3%ADda#Acompanhamento-da-permissao-na-conversa)
- [Realizando a ligação com WhatsApp Voz](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429875945239-WhatsApp-Voice-Sa%C3%ADda#Realizando-a-ligacao-com-WhatsApp-Voz)
- [Relatórios e acompanhamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429875945239-WhatsApp-Voice-Sa%C3%ADda#Relatorios-e-acompanhamentos)
- [Status](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429875945239-WhatsApp-Voice-Sa%C3%ADda#Status)
- [FAQ](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429875945239-WhatsApp-Voice-Sa%C3%ADda#FAQ)

---

## Configurações

Para acessar as configurações de rotas de entrada e saída, [acesse essa documentação.](https://sankhya.zendesk.com/hc/pt-br)

---

## Habilitação em Configurar Propriedades

Esta etapa libera o recurso no nível do ambiente.
Sem essa configuração, nenhum grupo poderá utilizar WhatsApp Voz.

![Imagem 2: Esta etapa libera o recurso no nível do ambiente. Sem essa configuração, nenhum grupo poderá utilizar WhatsApp Voz.](https://ajuda.sankhya.com.br/hc/article_attachments/42639399933591)

**Passo a passo**

1. Acesse o menu da plataforma digite e clique em **Configurar Propriedades**.
2. Na seção relacionada a integrações e canais, localize a opção **WhatsApp Voz**.
3. Marque o checkbox:

   **✔ Usar WhatsApp Voz**
4. Preencha os campos obrigatórios:

   - **URL WhatsApp Voz (whatsapp-gateway-multitenant)**
     Endpoint responsável pelo processamento das requisições de voz.
   - **Token WhatsApp Voz (secret whatsapp-gateway-multitenant**)
     Token de autenticação utilizado para validação das chamadas API.

URL Whatsapp Voz: multitenant-360-cloud.neppo.com.br
Token WhatsApp Voz: LAemnaMhRhDo652lrSEb

5. Clique em **Salvar**.

O canal WhatsApp Voz está agora habilitado, permitindo que grupos individuais ativem o recurso posteriormente.

---

## Habilitação no grupo de atendimento

Mesmo com o recurso ativo nas propriedades, cada grupo decide se irá usar WhatsApp Voz.
Isso garante controle granular e evita ativação acidental.

![Imagem 3: Mesmo com o recurso ativo nas propriedades, cada grupo decide se irá usar WhatsApp Voz. Isso garante controle granular…](https://ajuda.sankhya.com.br/hc/article_attachments/42639420394135)

**Passo a passo**

1. Acesse **Grupo de Atendimento** no menu lateral.
2. Selecione o grupo desejado.
3. Vá para a aba **Configurações do Grupo**.
4. Ative:

   **✔ Habilitar WhatsApp Voz**
5. Salve as alterações.

O grupo passa a aceitar interações via WhatsApp Voz.
A partir desse momento, todo o fluxo de voz ficará disponível conforme o comportamento definido no canal.

---

## Área de atendimento

Quando um atendimento é iniciado pelo canal **WhatsApp**, o agente visualizará no **header da conversa** um botão específico para ações de voz.

[GIF animado: Imagem 4: Quando um atendimento é iniciado pelo canal WhatsApp , o agente visualizará no header da conversa um botão específico…](https://ajuda.sankhya.com.br/hc/article_attachments/42639386427159)

Esse botão abre um menu com três funcionalidades principais:

Exibe a situação atual do número do cliente em relação à autorização para receber chamadas da empresa:

- **Permissão autorizada**
- **Aguardando permissão**
- **Permissão não concedida**

Esse status é retornado diretamente pela API responsável por gerenciar permissões do canal.

## Solicitar permissão de ligação

Caso o cliente ainda não tenha autorizado receber ligações via WhatsApp:

[GIF animado: Imagem 5: Caso o cliente ainda não tenha autorizado receber ligações via WhatsApp:](https://ajuda.sankhya.com.br/hc/article_attachments/42639416993815)

- O agente pode enviar um **template de solicitação de permissão** diretamente pela tela.
- O template deve estar previamente cadastrado no **broker 360 dialog** da empresa.
- Após o envio, a conversa exibirá automaticamente:

  ✔ Confirmação do envio
  ✔ Status atualizado conforme o cliente responde

[GIF animado: Imagem 6: ✔ Confirmação do envio ✔ Status atualizado conforme o cliente responde](https://ajuda.sankhya.com.br/hc/article_attachments/42639446698391)

A resposta do cliente aparece como uma mensagem automática na linha do tempo do atendimento.

## Realizar ligação

Após a permissão ser concedida, o agente pode iniciar a chamada via WhatsApp.

Ao clicar em **Realizar Ligação**, a plataforma abre o **Dial Pad**, onde o agente escolhe a saída de voz:

- **Neppo Voz** (caso a empresa utilize a telefonia nativa)
- **WhatsApp Voz** (com status de permissão exibido ao lado)

[GIF animado: Imagem 7: WhatsApp Voz (com status de permissão exibido ao lado)](https://ajuda.sankhya.com.br/hc/article_attachments/42639401241239)

## Acompanhamento da permissão na conversa

Após o envio do template:

- A área central da conversa exibirá mensagens automáticas informando:

  - “Envio ativo realizado”
  - “Permissão para ligação concedida” ou “recusada”

Esses status permitem que o agente tome a ação correta sem sair da tela.

---

## Realizando a ligação com WhatsApp Voz

Com a permissão concedida:

1. O agente abre o botão de ligação.
2. Seleciona **Realizar Ligação**.
3. O Dial Pad abre com duas opções de rota de voz:

   - **Neppo Voz**
   - **WhatsApp Voz** (com indicativo “Permissão autorizada”)
4. Após selecionar a rota, clicar em **Confirmar**.

Durante a chamada, o dialpad apresentará as ações disponíveis (mutar, desligar, pausar, etc.).

---

## Relatórios e acompanhamentos

Toda sessão iniciada via WhatsApp permite a solicitação de uma chamada. As ligações realizadas serão registradas diretamente no protocolo da própria sessão, sem a criação de um novo atendimento. A interação de voz ficará vinculada ao atendimento em andamento. Ao concluir a ligação, o registro completo da chamada será gravado e disponibilizado ao agente para consulta e acompanhamento.

![Imagem 8: Toda sessão iniciada via WhatsApp permite a solicitação de uma chamada. As ligações realizadas serão registradas…](https://ajuda.sankhya.com.br/hc/article_attachments/42639432877207)

Os relatórios de interação podem ser identificados na tela de histórico de atendimento, relatório analítico e relatório de sessões.

---

## Status

**A Meta atualizou a política de chamadas:**
o limite, que antes permitia até **5 chamadas** por número em uma janela de **24 horas**, agora foi ampliado para **10 chamadas** no mesmo período.

| Situação | Usabilidade sugerida | Regra na documentação |
| --- | --- | --- |
| Solicitar permissão | ![Imagem 9: Solicitar permissão](https://ajuda.sankhya.com.br/hc/article_attachments/42639432998679) | Antes de realizar uma ligação direta, deve ser enviado uma solicitação de ligação, onde será disparo uma mensagem para o cliente |
| Permissão não concedida | ![Imagem 10: Permissão não concedida](https://ajuda.sankhya.com.br/hc/article_attachments/42639418048279) | É necessário solicitar permissão antes de iniciar chamadas outbound. |
| Permissão pendente | ![Imagem 11: Permissão pendente](https://ajuda.sankhya.com.br/hc/article_attachments/42639447707927) | Solicitação enviada, aguardando resposta do usuário. |
| Permissão ativa | ![Imagem 12: Permissão ativa](https://ajuda.sankhya.com.br/hc/article_attachments/42639418404375) | Permissão tem validade de 7 dias a partir da concessão. |
| Permissão expirada ou revogada | ![Imagem 13: Permissão expirada ou revogada](https://ajuda.sankhya.com.br/hc/article_attachments/42639448045975) | Permissão expira após 7 dias ou é revogada após 4 chamadas não atendidas. |
| Limite diário – dentro do limite | ![Imagem 14: Limite diário – dentro do limite](https://ajuda.sankhya.com.br/hc/article_attachments/42639422648087) | Máximo de 5 chamadas outbound por usuário em 24h. |
| Limite diário – atingido | ![Imagem 15: Limite diário – atingido](https://ajuda.sankhya.com.br/hc/article_attachments/42639448386327) | Após 5 chamadas em 24h, novas tentativas são bloqueadas. |
| 1ª chamada não atendida | ![Imagem 16: 1ª chamada não atendida](https://ajuda.sankhya.com.br/hc/article_attachments/42639434127383) | Registro de status de chamada rejeitada ou sem resposta. Inserir informação na conversa para o agente |
| 2 chamadas consecutivas não atendidas | ![Imagem 17: 2 chamadas consecutivas não atendidas](https://ajuda.sankhya.com.br/hc/article_attachments/42639448669591) | Documentação recomenda limitar insistência; após 2 chamadas ignoradas, é preciso avaliar continuidade. Inserir informação na conversa para o agente |
| 4 chamadas não atendidas (revoga permissão) | ![Imagem 18: 4 chamadas não atendidas (revoga permissão)](https://ajuda.sankhya.com.br/hc/article_attachments/42639448866839)![Imagem 19: 4 chamadas não atendidas (revoga permissão)](https://ajuda.sankhya.com.br/hc/article_attachments/42639403122199) | Regra: permissão é automaticamente revogada após 4 chamadas sem resposta. |
| Solicitação de permissão – limite semanal | ![Imagem 20: Solicitação de permissão – limite semanal](https://ajuda.sankhya.com.br/hc/article_attachments/42639434798487) | Máximo de 2 solicitações de permissão em um intervalo de 7 dias. |
| Reset após chamada atendida | **Não é necessário nenhuma mensagem, mas realizar a ação de forma automática.** | Limites de chamadas são resetados quando ocorre uma chamada conectada entre empresa e usuário. |
| Status – iniciando | “Iniciando chamada…”  **Seguir comportamento do dial pad** | Estado SIP INVITE enviado, aguardando resposta. |
| Status – ringing | “Chamando…”  **Seguir comportamento do dial pad** | Evento `ringing` via webhook recebido. |
| Status – conectando | “Conectando com o contato…”  **Seguir comportamento do dial pad** | Estado de negociação SDP antes da resposta final. |
| Status – em chamada | “Chamada em andamento.”  **Seguir comportamento do dial pad** | Evento `connect` via webhook confirma sessão ativa. |
| Status – finalizada | “Chamada encerrada.” ![Imagem 21: “Chamada encerrada.”](https://ajuda.sankhya.com.br/hc/article_attachments/42639423819287)   **Permanecer dentro da conversa** | Evento `terminate` via webhook indica término. |
| Status – rejeitada | “O contato rejeitou a chamada.” ![Imagem 22: “O contato rejeitou a chamada.”](https://ajuda.sankhya.com.br/hc/article_attachments/42639470632983) | Evento `rejected` retornado pela API. |
| Status – erro/falha | ![Imagem 23: Status – erro/falha](https://ajuda.sankhya.com.br/hc/article_attachments/42639440206999) | Erros possíveis: SIP 407 (auth), rede, limites ou falha técnica. |

---

## FAQ

**O que é o WhatsApp Voice dentro da plataforma Neppo?**

É o recurso que permite realizar **ligações de voz via WhatsApp** diretamente pela plataforma de atendimento da Neppo, utilizando o número oficial do cliente, com registro completo no protocolo da sessão.

---

**O que é necessário para habilitar o WhatsApp Voice?**

São necessárias três etapas:

1. **Configuração na 360dialog**

   - Ativar o ícone de ligação e o suporte SIP.
   - Realizar o POST na rota `/calling/settings` com as configurações obrigatórias.
2. **Configuração no PBX**

   - Criar rotas de entrada e saída (inbound/outbound).
   - Configurar as credenciais SIP e gateway.
3. **Configurações dentro da plataforma Neppo**

   - Habilitar parâmetros no tenant.
   - Configurar permissões de ligação por agente.
   - Ajustar as telas de atendimento para exibição do botão de chamada.

---

**Qual endpoint deve ser configurado na 360dialog?**

```
POST https://waba-v2.360dialog.io/calling/settings
```

---

**Como funciona o fluxo de permissão de ligação do cliente via WhatsApp?**

1. O agente clica no botão do telefone no header da conversa.
2. A plataforma exibe três opções:

   - **Status da permissão**
   - **Enviar solicitação de permissão** (template)
   - **Realizar ligação**
3. O cliente recebe o template e escolhe permitir ou negar.
4. A página de conversa exibe para o agente o status **Permitido** ou **Negado**.
5. Caso permitido, o agente pode iniciar a ligação.

---

**Como o agente sabe se pode ligar para o cliente?**

O status da permissão aparece:

- No modal de opções do botão de ligação
- No Dial Pad na opção WhatsApp
- Em mensagens de acompanhamento na conversa
- Ícone e cores conforme status exibidos no header

---

**A chamada via WhatsApp cria um novo protocolo?**

Sim.
A ligação fica registrada **na mesma sessão aberta** do atendimento, junto com mensagens, mídia e eventos.

---

**Quantas chamadas podem ser feitas por número?**

A Meta atualizou o limite de **5 para 10 chamadas em uma janela de 24 horas** por cliente.

---

**Como o agente acompanha a ligação dentro da plataforma?**

Durante a chamada são exibidos:

- **Status da chamada**
- **Timer da ligação**
- **Opção de encerrar**
- **Indicadores de falha ou sucesso**
- **Permissão ou bloqueio registrado na conversa**

Após a ligação, o agente vê:

- Registro do evento “Chamada realizada via WhatsApp Voice”

---

**Quais mensagens de erro ou status o agente pode visualizar?**

Alguns exemplos:

- Cliente não permitiu ligação
- Permissão pendente
- Chamada encerrada pelo cliente
- etc

Esses status aparecem em cartões coloridos no chat.

---

**Quais funcionalidades estão disponíveis para o agente no WhatsApp Voice?**

- Verificar permissão
- Enviar solicitação via template
- Realizar chamada
- Selecionar saída de voz (WhatsApp, SIP etc.)
- Visualizar eventos em tempo real
- Consultar histórico da sessão

---

**Como funciona o ambiente de testes?**

A Neppo valida as configurações em ambiente **QA PBX** (`qa-pbx.neppo.com.br`) antes de liberar em produção.

---

**Onde configurar permissões e parâmetros na Neppo?**

Em **Configurar Parâmetros**:

- Habilitar “WhatsApp Voice”
- Configurar permissões gerais
- Ajustes por agente ou equipe
- Revogar permissão se necessário

---

**Como habilitar o WhatsApp Voice para grupos de atendimento?**

Na tela:

**Grupos de Atendimento**

- Habilite a opção “WhatsApp Voice”
- Salve

---

**Como funciona a usabilidade na tela de atendimento?**

Na conversa:

1. O header exibe o ícone de chamada.
2. O agente abre o menu com 3 opções:

   - Status da permissão
   - Solicitar permissão
   - Ligar
3. O dial pad aparece com opções de saída.
4. Durante a chamada, aparecem ações e status.
5. Após a chamada, o registro entra no histórico.

---

**O que acontece se o cliente negar a permissão?**

- O agente vê “Permissão negada”
- A opção de ligação fica desabilitada
- Pode reenviar a solicitação posteriormente

---

**Quais dados são registrados em relatórios?**

- Total de chamadas realizadas
- Permissões enviadas
- Permissões aprovadas/negadas
- Resultado da chamada
- Status final (sucesso, falha, não atendida)
- Origem da chamada dentro do fluxo de atendimento
- Identificadores SIP e de sessão

---

**O cliente enxerga alguma diferença no WhatsApp?**

Não.
A experiência é **nativa do WhatsApp**, como uma ligação comum, porém trafegando via API com gravação, registro e controle.

---

**O que é necessário para o template de solicitação?**

O template deve:

- Ser aprovado pela Meta
- Conter variáveis claras
- Informar que o cliente está autorizando receber ligações

---

**O que acontece se o template não estiver configurado?**

O agente:

- Não consegue solicitar permissão

---

**É possível revogar a permissão?**

Sim, pelo cliente.
