---
id: "42427362012439"
titulo: "Integração WhatsApp Coex"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427362012439-Integra%C3%A7%C3%A3o-WhatsApp-Coex"
trilha: "PLOOMES: Automação de propostas  > Geral"
atualizado_em: "2026-08-03T12:56:45Z"
rotulos: ["sync_hc", "ploomes_16052959", "sync_hash_3fd96f322f37", "ploomes"]
---

# Integração WhatsApp Coex

## 1) Sobre a Integração WhatsApp Coex

A **Integração WhatsApp Coex** conecta o Ploomes ao WhatsApp Business por meio do modelo de **coexistência (Coexistence)** da Meta. Esse modelo permite vincular um número de WhatsApp Business que já está em uso no aplicativo oficial (app do WhatsApp Business) à conta da Meta usada pela integração, sem exigir a migração para um número exclusivo de API.

Com a integração ativa, mensagens recebidas no WhatsApp passam a gerar automaticamente **registros de interação** no Ploomes, vinculados ao contato e ao usuário responsável pelo número. Também é possível gerar um **resumo automático da conversa por IA** e visualizar as mensagens em um leitor (viewer) dentro do próprio registro de interação, no formato semelhante ao do WhatsApp.

Essa funcionalidade é voltada a dois perfis:

- **Administradores**, que configuram a integração e o webhook na Meta.
- **Usuários (vendedores)**, que recebem os registros de interação gerados a partir das mensagens do WhatsApp vinculadas ao seu número.

---

## 2) Pré-requisitos

- Ter uma **conta comercial na Meta (Meta Business)** com o **modelo de coexistência (WhatsApp Coexistence)** habilitado para o número de WhatsApp Business que será integrado.
- Ter um **número de WhatsApp Business já verificado** e em uso no aplicativo oficial, pois é esse número que será vinculado via coexistência — a integração não substitui o app do WhatsApp Business no celular.
- Ter **permissão de administrador** na conta Ploomes para acessar a tela de configuração da integração.
- Ter, no cadastro de **Usuário**, um **campo de telefone** (nativo ou personalizado, do tipo texto simples) preenchido e mapeável, que será usado para vincular as mensagens recebidas ao vendedor responsável.

**Importante:** a Integração WhatsApp Coex não oferece suporte a **grupos de WhatsApp**. Apenas conversas individuais são processadas.

---

## 3) Configurando a Integração WhatsApp Coex

A configuração acontece em duas frentes: primeiro na Meta, onde o webhook é registrado, e depois no Ploomes, onde os parâmetros de negócio da integração são definidos. A URL de callback usada na Meta é gerada pelo próprio Ploomes — por isso, recomendamos abrir a tela de configuração da integração (seção [3.2](https://claude.ai/cowork/local_359257d2-9e1a-4599-9301-69838d830861#32-configurando-a-integra%C3%A7%C3%A3o-no-ploomes)) antes de ir até a Meta, para já ter a URL em mãos.

## 3.1) Configurando o webhook do WhatsApp na Meta

Esta etapa é feita no **Meta for Developers**, fora do Ploomes, e é pré-requisito para que as mensagens do WhatsApp cheguem até a integração.

1. Acesse [developers.facebook.com](https://developers.facebook.com/) e entre com a conta vinculada à sua conta comercial na Meta.
2. Selecione o app associado ao seu número de WhatsApp Business (ou crie um app do tipo Business, se ainda não tiver um).
3. No menu do app, acesse o produto **WhatsApp > Configuração**.
4. Confirme que o número está habilitado no modelo de **coexistência**. Esse vínculo normalmente é feito durante o processo de **Cadastro Incorporado (Embedded Signup)** da Meta, associando o número já usado no app do WhatsApp Business à sua conta de negócios (WABA).
5. Na seção **Webhook**, clique em **Editar**.
6. Preencha os dois campos solicitados pela Meta:

   - **Callback URL:** cole a URL de callback gerada pelo Ploomes (disponível na tela de configuração da integração, seção 3.2).
   - **Verify Token:** informe o mesmo token exibido na tela de configuração da integração no Ploomes.
7. Clique em **Verificar e salvar**. A Meta faz uma chamada de verificação à URL informada; se o Ploomes responder corretamente, o webhook é validado do lado da Meta.
8. Em **Campos do webhook**, localize o campo **messages** e clique em **Assinar**. Sem essa assinatura, nenhuma mensagem é enviada para o Ploomes.

**Observação:** a validação da URL de callback é feita inteiramente pela Meta. O Ploomes não exige nenhuma etapa adicional de validação interna — ele apenas exibe um indicador de status (veja seção 3.2) para facilitar o acompanhamento.

## 3.2) Configurando a integração no Ploomes

1. Acesse a área de integrações **plug and play** do Ploomes e localize a entrada **Integração WhatsApp Coex**.
2. Ative a integração. Ao ativar, o Ploomes **gera automaticamente a URL de callback e o Verify Token** que devem ser usados na configuração da Meta (seção 3.1). Não é necessário gerar essa URL manualmente.
3. Copie a URL de callback e o Verify Token exibidos na tela (há um botão de cópia rápida para cada campo) e utilize-os na configuração do webhook na Meta.
4. Selecione o **campo de telefone** do objeto Usuário que será usado para vincular as mensagens recebidas ao responsável. Por padrão, o campo nativo de telefone do Usuário é sugerido, mas você pode selecionar um campo personalizado do tipo texto simples. Esse campo é obrigatório — o botão de salvar permanece bloqueado até que um campo válido seja selecionado.
5. Revise o **mapeamento de contato**: ao criar um contato a partir de uma mensagem do WhatsApp, o nome do remetente é gravado no campo Nome e o número no campo Telefone do contato. Esse mapeamento é fixo e apenas exibido para conferência, não é editável.
6. Defina o **tempo de inatividade** usado para agrupar mensagens em uma mesma conversa (e, consequentemente, em um mesmo registro de interação). O valor é definido em minutos ou horas, com mínimo de 30 minutos e máximo de 24 horas. O padrão sugerido é de 6 horas. Alterar esse valor depois de ativa a integração recalcula os agrupamentos de mensagens em andamento.
7. Ative ou desative o **resumo automático por IA**. Quando ativo, é possível configurar um modelo (template) de resumo. Quando desativado, o registro de interação traz apenas a transcrição da conversa, sem resumo.
8. Salve a configuração.

Depois de salva a configuração, a tela exibe um indicador de status do webhook:

- **Pendente de validação:** exibido enquanto a integração aguarda o recebimento da primeira mensagem confirmada pela Meta.
- **Validado:** exibido após o recebimento bem-sucedido da primeira mensagem, confirmando que o webhook está funcionando de ponta a ponta.

**Observação:** a URL de callback é única por conta — todos os administradores visualizam a mesma URL. Não existe uma ação isolada de "revogar" a URL; para gerar uma nova, é necessário desativar e reativar a integração.

---

## 4) Utilizando a Integração WhatsApp Coex

## 4.1) Recebimento de mensagens e criação de registros

Ao receber uma mensagem do WhatsApp de um número já configurado, a integração:

1. Verifica se o número remetente está na **lista de bloqueio (blocklist)**. Se estiver, a mensagem é descartada silenciosamente e nenhum registro é criado.
2. Busca um contato correspondente ao número, aplicando a rotina de deduplicação do Ploomes. O resultado pode ser: vínculo com um contato já existente (por correspondência), criação de um novo contato, criação com pendência de revisão, ou bloqueio da criação, conforme a configuração de deduplicação da conta.
3. Agrupa a mensagem em uma conversa em andamento (respeitando o tempo de inatividade configurado) ou inicia uma nova conversa, caso o agrupamento anterior já tenha sido encerrado.
4. Gera ou atualiza o **registro de interação** vinculado ao contato e ao usuário responsável pelo número de telefone mapeado.
5. Se o **resumo automático por IA** estiver ativo, gera o resumo da conversa na descrição do registro; caso contrário, grava a transcrição da conversa.

## 4.2) Visualizando as conversas

Dentro do registro de interação gerado, um **leitor (viewer)** exibe as mensagens da conversa em um formato semelhante ao do WhatsApp, junto com o resumo por IA (quando habilitado).

## 4.3) Vínculo com Negócios (Cards)

Quando o contato vinculado à conversa está associado a mais de um Negócio, a integração prioriza o vínculo do registro de interação ao Negócio em que o usuário responsável pelo número aparece como responsável; na ausência desse critério, prioriza o Negócio em que ele aparece como colaborador. Em caso de empate, prevalece o Negócio com a atualização mais recente.

## 4.4) Consultando os logs

A tela de logs da Integração WhatsApp Coex reúne o histórico de processamento das mensagens recebidas, incluindo o status de cada evento (processado, descartado, com erro). Administradores visualizam os logs de toda a conta; demais usuários visualizam apenas os logs relacionados ao seu próprio número. Os registros ficam disponíveis por um período parametrizável, com padrão de 30 dias.

---

## 5) Limitações

- **Sem suporte a grupos de WhatsApp:** apenas conversas individuais são processadas pela integração.
- **Atribuição de responsável fixa na criação:** o responsável pelo registro de interação é definido no momento da criação e não é recalculado depois, mesmo que o campo de telefone mapeado no Usuário seja alterado posteriormente.
- **Campo de telefone excluído:** se o campo mapeado para vinculação for excluído do cadastro de Usuário, novos registros de interação deixam de ser criados até que um novo campo válido seja mapeado.
- **Usuário inativo:** se o usuário responsável pelo número estiver inativo no Ploomes, nenhum registro de interação é criado para as mensagens recebidas.
- **Mídias com validade limitada:** imagens, áudios e documentos recebidos são referenciados pela URL fornecida pela própria Meta, que expira após aproximadamente duas semanas. A integração não realiza cópia própria dos arquivos de mídia.
- **Limite de capacidade:** a integração opera dentro do limite geral de capacidade da conta (atualmente 200.000 entidades, como contatos). Ao atingir o limite, é necessário liberar espaço (excluindo históricos antigos) ou contratar capacidade adicional.
- **Números fora do padrão internacional:** números sem DDI/DDD no formato padrão podem não ser reconhecidos corretamente pela validação de telefone da integração.
- **Sem revogação isolada da URL de callback:** para invalidar a URL atual, é necessário desativar e reativar a integração — não há um botão de revogação separado.

---

## 6) F.A.Q.

**Preciso criar uma nova URL de callback manualmente?**

Não. A URL de callback e o Verify Token são gerados automaticamente pelo Ploomes assim que você ativa a integração. Basta copiá-los e colá-los na configuração do webhook na Meta.

**Como sei se o webhook está funcionando?**

A tela de configuração exibe o status **Pendente de validação** até que a primeira mensagem seja recebida com sucesso, e passa para **Validado** a partir daí.

**A integração funciona com grupos de WhatsApp?**

Não. Somente conversas individuais são suportadas.

**O que acontece se eu excluir o campo de telefone usado no mapeamento?**

A integração deixa de criar novos registros de interação até que um novo campo de telefone válido seja selecionado na tela de configuração.

**Posso trocar o campo de telefone depois que a integração já está ativa?**

Sim, mas o responsável de registros já criados não é recalculado — a troca vale apenas para novas mensagens recebidas a partir da alteração.

**O resumo por IA é obrigatório?**

Não. Você pode desativar o resumo por IA a qualquer momento; nesse caso, o registro de interação traz apenas a transcrição da conversa.

**Por quanto tempo consigo acessar as mídias recebidas pelo WhatsApp?**

As mídias usam a URL fornecida pela Meta, que expira em aproximadamente duas semanas. Após esse prazo, o conteúdo pode deixar de estar acessível.

**Todos os administradores veem a mesma URL de callback?**

Sim. A URL é única por conta, não por usuário.

**Como faço para gerar uma nova URL de callback?**

Desative e reative a integração. Uma nova URL será gerada automaticamente nesse processo.

---

## 7) Glossário

- **Coexistência (Coexistence):** modelo da Meta que permite vincular um número de WhatsApp Business já em uso no aplicativo oficial a uma conta de negócios, sem exigir migração para um número exclusivo de API.
- **Webhook:** mecanismo pelo qual a Meta envia automaticamente as mensagens recebidas no WhatsApp para a URL de callback configurada.
- **URL de callback:** endereço gerado pelo Ploomes que recebe as notificações de webhook enviadas pela Meta.
- **Verify Token:** token usado pela Meta para validar a URL de callback informada na configuração do webhook.
- **Blocklist:** lista de números bloqueados cujas mensagens são descartadas automaticamente, sem gerar registro.
- **Deduplicador:** rotina do Ploomes que verifica se já existe um contato correspondente ao número remetente antes de criar um novo.
- **Registro de interação:** registro criado no Ploomes a partir de uma conversa do WhatsApp, vinculado ao contato e ao usuário responsável.
- **Tempo de inatividade:** intervalo configurado que determina quando uma nova mensagem inicia uma nova conversa (e um novo registro de interação) em vez de ser agrupada à conversa anterior.
- **Resumo por IA:** resumo automático gerado a partir da conversa do WhatsApp, exibido na descrição do registro de interação.
- **Viewer:** área do registro de interação que exibe as mensagens da conversa em formato semelhante ao do aplicativo WhatsApp.
