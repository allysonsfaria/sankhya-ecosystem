---
id: "42430480009623"
titulo: "WhatsApp Coex (Beta)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430480009623-WhatsApp-Coex-Beta"
trilha: "NEPPO: Personalização de atendimento > Omnichannel"
atualizado_em: "2026-08-11T17:06:06Z"
rotulos: ["sync_hc", "neppo", "neppo_870547459", "sync_hash_394006adb742"]
---

# WhatsApp Coex (Beta)

O **modo Coexistência (Beta)** permite conectar um número que já está em uso no **WhatsApp Business App** à plataforma Neppo, possibilitando que o aplicativo oficial e a plataforma funcionem simultaneamente utilizando o mesmo número de telefone.

- O WhatsApp Coex ficará em Beta até o 01/10/2026.
- O envio ativo por template para contatos vinculados ao Coex está desabilitado. Para iniciar uma conversa com esses contatos, recomendamos utilizar o aplicativo WhatsApp Business, evitando assim a cobrança pelo disparo de templates.

Com a Cloud API, cada Business Manager (BM) possui inicialmente um limite de até 2 números de telefone vinculados ao CoEx. Após a empresa atingir o volume de 2.000 mensagens, a Meta amplia automaticamente esse limite para até 20 números vinculados ao mesmo Business Manager. Para liberar +20 números, a empresa deverá entrar em contato com a Meta.

Versão mínima que os clientes precisam estar:

**neppochat-server 3.4.3**

Acesse o grafana para ver a versão do cliente

Com essa integração, a empresa continua utilizando normalmente o aplicativo WhatsApp Business no dispositivo móvel, enquanto a Neppo passa a oferecer recursos como atendimento omnichannel, campanhas, automações, templates, integrações via API e relatórios, mantendo o histórico de conversas sincronizado entre ambas as plataformas.

Todo o processo é realizado através do fluxo oficial **Embedded Signup** da Meta, garantindo uma integração segura, sem necessidade de migrar ou desativar o WhatsApp Business App.

[GIF animado: Imagem 1: Todo o processo é realizado através do fluxo oficial Embedded Signup da Meta, garantindo uma integração segura, sem…](https://ajuda.sankhya.com.br/hc/article_attachments/42639776977559)

- [Pré-requisitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430480009623-WhatsApp-Coex-Beta#Pre-requisitos)
- [Como funciona a Coexistência](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430480009623-WhatsApp-Coex-Beta#Como-funciona-a-Coexistencia)
- [Acessando a Central de Canais](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430480009623-WhatsApp-Coex-Beta#Acessando-a-Central-de-Canais)
- [Selecionando a forma de conexão](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430480009623-WhatsApp-Coex-Beta#Selecionando-a-forma-de-conexao)
- [Informações importantes](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430480009623-WhatsApp-Coex-Beta#Informacoes-importantes)
- [Informar o Agente](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430480009623-WhatsApp-Coex-Beta#Informar-o-Agente)
- [Autorizar a integração com a Meta](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430480009623-WhatsApp-Coex-Beta#Autorizar-a-integracao-com-a-Meta)
- [Selecionar o Portfólio Empresarial](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430480009623-WhatsApp-Coex-Beta#Selecionar-o-Portfolio-Empresarial)
- [Informar o número](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430480009623-WhatsApp-Coex-Beta#Informar-o-numero)
- [Compartilhamento da conta](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430480009623-WhatsApp-Coex-Beta#Compartilhamento-da-conta)
- [Importação do histórico](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430480009623-WhatsApp-Coex-Beta#Importacao-do-historico)
- [Confirmar a conta](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430480009623-WhatsApp-Coex-Beta#Confirmar-a-conta)
- [Revisar permissões](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430480009623-WhatsApp-Coex-Beta#Revisar-permissoes)
- [Código de confirmação](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430480009623-WhatsApp-Coex-Beta#Codigo-de-confirmacao)
- [Finalização](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430480009623-WhatsApp-Coex-Beta#Finalizacao)
- [Observações importantes](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430480009623-WhatsApp-Coex-Beta#Observacoes-importantes)
- [Limitações da integração](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430480009623-WhatsApp-Coex-Beta#Limitacoes-da-integracao)
- [FAQ](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430480009623-WhatsApp-Coex-Beta#FAQ)
- [Resultado esperado](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430480009623-WhatsApp-Coex-Beta#Resultado-esperado)

---

## Pré-requisitos

Antes de iniciar a configuração, verifique se todos os requisitos abaixo foram atendidos:

- Possuir um número ativo no **WhatsApp Business App**;
- Utilizar a versão **2.24.5 ou superior** do WhatsApp Business;
- Possuir uma conta no **Meta Business**;
- Durante o Embedded Signup, o número será vinculado a essa empresa.
- Ter permissões administrativas sobre o portfólio empresarial (Business Portfolio);
- Possuir acesso ao dispositivo onde o WhatsApp Business está instalado;
- Ter permissão para acessar a Central de Canais da Neppo.
- O número deve estar em uso no WhatsApp Business há pelo menos **7 dias** antes da ativação da coexistência.
- A Meta exige que o **WhatsApp Business App seja aberto no dispositivo principal pelo menos uma vez a cada 14 dias**.

---

## Como funciona a Coexistência

Após a conclusão da integração:

- O mesmo número continuará funcionando normalmente no WhatsApp Business App.
- O mesmo número será disponibilizado na Neppo através da API Oficial da Meta.
- Todas as mensagens enviadas pelo aplicativo também serão refletidas na Neppo.
- As mensagens enviadas pela Neppo serão exibidas normalmente no aplicativo.
- O histórico recente poderá ser importado durante o processo de integração.

---

## Acessando a Central de Canais

Acesse:

**Central de Canais → WhatsApp**

Será exibida a lista dos números cadastrados.

Clique em:

**Adicionar Número**

---

## Selecionando a forma de conexão

No assistente de configuração selecione:

**Conectar WhatsApp Business App ao modo Coexistência (Beta)**

Esta opção é indicada para empresas que desejam manter o uso do aplicativo WhatsApp Business e, ao mesmo tempo, utilizar os recursos da plataforma Neppo.

Clique em:

**Avançar**

---

## Informações importantes

Antes de iniciar a integração, serão apresentadas algumas recomendações:

- Certifique-se de já utilizar o WhatsApp Business App.
- Utilize uma versão igual ou superior à **2.24.5**.
- O número será vinculado a um agente dentro da Neppo.
- O histórico de conversas poderá ser sincronizado e consultado posteriormente.

---

## Informar o Agente

Informe o agente que representará esse número dentro da plataforma.

![Imagem 2: Informe o agente que representará esse número dentro da plataforma.](https://ajuda.sankhya.com.br/hc/article_attachments/42639794131607)

Este agente será responsável pelo recebimento das conversas originadas desse número.

> **Importante**
>
> No modo Coexistência existe uma relação **1:1 entre o número do WhatsApp e o agente da Neppo**.
>
> Cada número conectado pode estar associado a apenas um agente, e cada agente representa exclusivamente um número conectado via Coexistência.

Após preencher o campo, clique em:

**Criar conexão**

---

## Autorizar a integração com a Meta

Será aberta uma janela oficial do Facebook para Empresas.

![Imagem 3: Será aberta uma janela oficial do Facebook para Empresas.](https://ajuda.sankhya.com.br/hc/article_attachments/42639777653655)

Leia as permissões solicitadas e clique em:

**Continuar**

Durante esta etapa a Meta solicitará autorização para compartilhar os ativos comerciais com a Neppo.

---

## Selecionar o Portfólio Empresarial

Selecione o **Business Portfolio** ao qual o número pertence.

![Imagem 4: Selecione o Business Portfolio ao qual o número pertence.](https://ajuda.sankhya.com.br/hc/article_attachments/42639778001175)

Na opção **Conta do WhatsApp Business**, escolha:

**Conectar um app do WhatsApp Business**

Clique em:

**Avançar**

---

## Informar o número

Selecione:

- País;
- Código do país;
- Número do WhatsApp Business.

![Imagem 5: Número do WhatsApp Business.](https://ajuda.sankhya.com.br/hc/article_attachments/42639765794071)

Caso o número ainda não pertença ao portfólio empresarial, será necessário realizar sua validação durante o processo.

Clique em:

**Avançar**

---

## Compartilhamento da conta

A Meta exibirá um resumo informando que o aplicativo WhatsApp Business será conectado à plataforma Neppo.

![Imagem 6: A Meta exibirá um resumo informando que o aplicativo WhatsApp Business será conectado à plataforma Neppo.](https://ajuda.sankhya.com.br/hc/article_attachments/42639778521495)

Serão compartilhadas informações como:

- Perfil comercial;
- Número de telefone;
- Contatos;
- Conversas;
- Histórico de conversas.

As mensagens continuarão protegidas pela criptografia ponta a ponta da Meta.

Clique em:

**Avançar**

---

## Importação do histórico

Nesta etapa será possível importar:

- Perfil comercial;
- Contatos;
- Histórico de conversas (até 6 meses, quando disponível);
- Outras informações relevantes da conta.

![Imagem 7: Outras informações relevantes da conta.](https://ajuda.sankhya.com.br/hc/article_attachments/42639782779543)

Será exibido um **QR Code**.

Abra o aplicativo **WhatsApp Business** e faça a leitura do QR Code para autorizar o compartilhamento das informações.

Após a confirmação no aplicativo, o fluxo continuará automaticamente.

---

## Confirmar a conta

Revise as informações da conta:

- Nome da conta WhatsApp Business;
- Fuso horário.

Caso necessário, realize os ajustes e clique em:

**Avançar**.

---

## Revisar permissões

A Meta apresentará um resumo das permissões concedidas à Neppo.

![Imagem 8: A Meta apresentará um resumo das permissões concedidas à Neppo.](https://ajuda.sankhya.com.br/hc/article_attachments/42639782980887)

Entre elas:

- Gerenciar a conta comercial;
- Gerenciar contas do WhatsApp;
- Gerenciar conversas;
- Registrar eventos em nome da conta comercial.

Após revisar as informações, clique em:

**Confirmar**.

---

## Código de confirmação

Dependendo das configurações de segurança da conta Meta, poderá ser solicitada uma verificação adicional.

![Imagem 9: Dependendo das configurações de segurança da conta Meta, poderá ser solicitada uma verificação adicional.](https://ajuda.sankhya.com.br/hc/article_attachments/42639810845719)

Informe o código enviado para o e-mail cadastrado na conta Meta.

Após validar o código, a integração continuará automaticamente.

---

## Finalização

A Meta iniciará a conexão entre o WhatsApp Business App e a Neppo.

Esse processo pode levar alguns minutos.

Ao final será exibida a confirmação de que a conta foi conectada com sucesso.

![Imagem 10: Ao final será exibida a confirmação de que a conta foi conectada com sucesso.](https://ajuda.sankhya.com.br/hc/article_attachments/42639811062679)

Caso necessário, a Meta poderá solicitar posteriormente a configuração de uma forma de pagamento para utilização dos serviços comerciais.

---

## Observações importantes

Antes de utilizar o modo Coexistência, considere as seguintes características da integração:

- Cada número conectado possui associação exclusiva com um único agente da Neppo (relação **1:1**).
- O histórico de conversas pode ser sincronizado durante a integração.
- As mensagens enviadas pelo aplicativo também ficam disponíveis na Neppo.
- As mensagens enviadas pela Neppo também aparecem no aplicativo WhatsApp Business.
- O número continua ativo no aplicativo WhatsApp Business durante toda a utilização da plataforma.
- O modo Coexistência utiliza exclusivamente a API Oficial da Meta.

---

## Limitações da integração

Atualmente o modo Coexistência possui algumas limitações funcionais:

- **Transferência de atendimento não é suportada.**
- **Chamadas de voz e vídeo não são suportadas pela Neppo.**
- O atendimento ocorre sempre entre um único número e um único agente.
- Conversas em grupos não são sincronizadas.
- Mensagens temporárias (Disappearing Messages) não são suportadas.
- Mensagens "Visualizar uma vez" (View Once) não são suportadas.
- Compartilhamento de localização em tempo real (Live Location) não é suportado.
- Listas de transmissão (Broadcast Lists) do aplicativo tornam-se indisponíveis para criação e edição enquanto a coexistência estiver ativa.
- A edição e exclusão de mensagens para todos podem apresentar restrições devido às limitações da Cloud API. ([seven Help Center](https://help.seven.io/en/whatsapp/whatsapp-coexistence?utm_source=chatgpt.com))

---

## FAQ

## Posso continuar utilizando o WhatsApp Business App?

Sim. O principal objetivo da Coexistência é permitir que o aplicativo continue sendo utilizado normalmente enquanto a Neppo utiliza a API Oficial da Meta. ([Documentação do Cliente 360dialog](https://docs.360dialog.com/docs/hub/embedded-signup?utm_source=chatgpt.com))

---

## Preciso migrar meu número para a API?

Não. O número permanece ativo no WhatsApp Business App e passa a funcionar simultaneamente com a API Oficial através do recurso de Coexistência. ([Documentação do Cliente 360dialog](https://docs.360dialog.com/docs/hub/embedded-signup?utm_source=chatgpt.com))

---

## Meu histórico de conversas será perdido?

Não. Durante a configuração, a Meta permite importar contatos e até seis meses de histórico de conversas, quando disponível. ([docs.4geeks.io](https://docs.4geeks.io/en/ai-agents/whatsapp-coexistence/?utm_source=chatgpt.com))

---

## Posso responder pelo aplicativo e pela Neppo ao mesmo tempo?

Sim. As mensagens permanecem sincronizadas entre o aplicativo WhatsApp Business e a plataforma Neppo. ([docs.businessapp.io](https://docs.businessapp.io/business-app/conversations/whatsapp/whatsapp-coexistence/?utm_source=chatgpt.com))

---

## Posso utilizar grupos do WhatsApp?

Não. Conversas em grupos não são suportadas pela Cloud API e não são sincronizadas com a Neppo. ([seven Help Center](https://help.seven.io/en/whatsapp/whatsapp-coexistence?utm_source=chatgpt.com))

---

## Posso utilizar listas de transmissão do aplicativo?

Não. Após ativar a Coexistência, listas de transmissão deixam de permitir criação e edição no aplicativo. ([seven Help Center](https://help.seven.io/en/whatsapp/whatsapp-coexistence?utm_source=chatgpt.com))

---

## Posso utilizar mensagens temporárias?

Não. Mensagens temporárias e conteúdos "Visualizar uma vez" deixam de ser suportados para conversas individuais enquanto a Coexistência estiver ativa. ([seven Help Center](https://help.seven.io/en/whatsapp/whatsapp-coexistence?utm_source=chatgpt.com))

---

## Posso realizar chamadas de voz ou vídeo pela Neppo?

Não. A integração suporta apenas mensagens. Chamadas de voz e vídeo continuam sendo recursos exclusivos do aplicativo WhatsApp Business.

---

## Posso transferir um atendimento para outro agente?

Não. O modo Coexistência não suporta transferência de atendimento. Cada número permanece associado exclusivamente a um único agente da Neppo durante toda a utilização.

---

## Posso conectar um mesmo número a vários agentes?

Não. A associação é **1:1**, ou seja, um número do WhatsApp Business pode estar vinculado apenas a um agente da Neppo.

---

## O que acontece se eu trocar de celular?

Em caso de troca ou reinstalação do WhatsApp Business, a Meta pode exigir uma nova sincronização da conexão para restabelecer a coexistência, dependendo do cenário da conta. ([Reddit](https://www.reddit.com/r/WhatsappBusinessAPI/comments/1tifsll/meta_update_coexistence_clients_who_switch/?utm_source=chatgpt.com))

---

## Em caso de indisponibilidade de rede?

As mensagens recebidas pela Cloud API continuam chegando à plataforma e o app sincroniza quando voltar online.

---

## Como ficará o registro dos protocolos?

Os protocolos serão gerados automaticamente em janelas de 24 horas na Neppo.

Durante a sincronização inicial, todas as conversas antigas também serão organizadas em protocolos de 24 horas, sem qualquer custo.

A cobrança ocorrerá apenas para novas conversas iniciadas após a autenticação e ativação da integração do WhatsApp Coexistente (Coex) com a Neppo.

Os protocolos são criados em janelas de 24 horas ou quando o atendimento é encerrado manualmente.

---

## Quem pode ativar o Coex?

Somente um administrador com permissão na Central de Canais da Neppo e acesso administrativo ao Meta Business Manager.

---

## O vendedor consegue ativar sozinho?

Não. A ativação exige participação de um administrador do Business Manager.

---

## Posso importar conversas antigas?

Não. A ativação exige participação de um administrador do Business Manager.

---

## O COEX possui cobrança da Meta?

Não. A Meta só cobra quando houver envio de templates.

---

## O COEX suporta bots da Neppo?

Não.

---

## O COEX suporta IA da Neppo?

Não.

---

## Posso utilizar automações?

Não.

---

## Posso utilizar fluxos?

Não.

---

## Posso utilizar o mesmo número na API Oficial e no COEX?

Não. O número deve estar em apenas uma modalidade.

---

## Posso compartilhar um número entre vários agentes?

Não. A relação é sempre **1 número → 1 agente**.

---

## O COEX sincroniza grupos?

Não.

---

## Ligações e chamadas de vídeo funcionam?

Funcionam normalmente no WhatsApp Business App, porém não são sincronizadas para a Neppo.

---

## Quais mídias são sincronizadas?

Mensagens de texto, imagens, documentos, áudios e arquivos suportados.

---

## O que não é sincronizado?

- Conversas em grupos
- Chamadas de voz
- Chamadas de vídeo
- Mensagens temporárias
- Mensagens de visualização única
- Compartilhamento de localização
- Lista de transmissão
- Edição de mensagens
- Exclusão de mensagens

---

## Os atendimentos aparecem em tempo real?

Sim. As mensagens são refletidas na tela de atendimento praticamente em tempo real.

---

## O COEX impacta os relatórios?

Sim. Haverá aumento na quantidade de protocolos, mas é possível filtrar por agente e identificar os atendimentos realizados via COEX.

---

## O COEX já está disponível para todos os clientes?

Ainda não. A funcionalidade permanecerá em **Beta** durante o período definido para validação, priorizando testes internos e clientes selecionados antes da liberação ampla. Solicitações devem ser feitas via reunião de CAB as 15h nas segunda-feira.

---

## Resultado esperado

Após a conclusão da configuração, o número permanecerá ativo no **WhatsApp Business App** e também estará disponível na **Central de Canais** da Neppo. A partir desse momento, será possível utilizar simultaneamente o aplicativo e a plataforma para envio e recebimento de mensagens, aproveitando recursos como automações, campanhas, templates, integrações e relatórios, mantendo o histórico sincronizado por meio da integração oficial da Meta.
