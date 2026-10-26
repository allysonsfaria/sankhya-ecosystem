---
id: "42429531983639"
titulo: "Embedded Sign Up - 360 Dialog"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42429531983639-Embedded-Sign-Up-360-Dialog"
trilha: "NEPPO: Personalização de atendimento > Omnichannel"
atualizado_em: "2026-08-11T17:13:38Z"
rotulos: ["sync_hc", "neppo", "neppo_184582146", "sync_hash_9c583b28d443"]
---

# Embedded Sign Up - 360 Dialog

Neppo, como provedora de soluções omnichannel, utilizará o **Embedded Sign Up** para otimizar e facilitar o processo de ativação de contas WhatsApp Business para os clientes, integrando o fluxo diretamente na plataforma Neppo.

O objetivo é oferecer um onboarding mais rápido, seguro e personalizado, sem a necessidade de múltiplos redirecionamentos ou etapas manuais.

Versão Neppo **Chat Server 2.10.833** ou superior

Versão **Gateway Manager 1.0.9** ou superior

[Jornada do cliente no Neppo](https://sankhya.zendesk.com/hc/pt-br/articles/42429531983639#Jornada-do-cliente-no-Neppo-Omnichannel)

---

## Benefícios do embedded Sign Up

- **Experiência fluida e integrada**: O cliente realiza todo o processo de ativação dentro da plataforma da Neppo.
- **Redução do tempo de ativação**: Processos automatizados e simplificados diminuem o tempo entre o cadastro e o início da operação.
- **Aumento de conversão**: Jornada de ativação mais simples gera maior adesão e satisfação.
- **Controle de jornada**: A Neppo gerencia toda a jornada de onboarding, melhorando a experiência e possibilitando análises.

---

## Pré-requisitos para implementação

- Registro da Neppo como **Tech Provider** aprovado pela Meta.
- Integração oficial com a plataforma **360dialog**.
- Credenciais de API da 360dialog configuradas.
- Infraestrutura própria para hospedagem do fluxo Embedded Sign Up.
- Acesso a permissões Meta adequadas (ex.: `public_profile`, `business_management`, etc.).

---

## Observações importantes

- Apenas números não utilizados anteriormente no WhatsApp Business podem ser ativados.
- Caso o cliente tenha um Gerenciador de Negócios no Facebook, será necessário associar a conta.
- Todo o processo deve ocorrer dentro de uma sessão segura e autenticada.
- A Neppo será responsável por monitorar o sucesso do fluxo e tratar eventuais falhas.

---

## Jornada do cliente no Neppo Omnichannel

1 - Para acessar a tela, no buscador, digite: "**WhatsApp Signup**”

![Imagem 1: 1 - Para acessar a tela, no buscador, digite: " WhatsApp Signup ”](https://ajuda.sankhya.com.br/hc/article_attachments/42639372388759)

2 - Autorize a Neppo a acessar seu nome e foto para confirmar que você é uma pessoa real e assim permitir o andamento do cadastro da empresa na plataforma do WhatsApp Business via API da Meta.

[GIF animado: Imagem 2: 2 - Autorize a Neppo a acessar seu nome e foto para confirmar que você é uma pessoa real e assim permitir o andamento…](https://ajuda.sankhya.com.br/hc/article_attachments/42639372718615)

3 - **Conecte sua conta a Neppo Tecnologia..:** Agora você precisa dar **permissão** para que a Neppo cuide da parte técnica da sua conta de WhatsApp Business, para que você possa usar o canal de atendimento, envio de mensagens, etc.

![Imagem 3: 3 - Conecte sua conta a Neppo Tecnologia..: Agora você precisa dar permissão para que a Neppo cuide da parte técnica da…](https://ajuda.sankhya.com.br/hc/article_attachments/42639372952215)

4 - **Preencha os dados da empresa:** Nesta etapa você está **definindo os dados oficiais da empresa** que vão ficar atrelados à sua conta de WhatsApp Business API. Essas informações serão usadas pela Meta para validar a existência e a autenticidade do negócio.

![Imagem 4: 4 - Preencha os dados da empresa: Nesta etapa você está definindo os dados oficiais da empresa que vão ficar atrelados…](https://ajuda.sankhya.com.br/hc/article_attachments/42639343606807)

5 - **Crie ou selecione sua conta do WhatsApp Business:** Nesta etapa você está **definindo onde o número de telefone será instalado**, em uma conta de WhatsApp Business já existente ou em uma nova que será criada agora.

![Imagem 5: 5 - Crie ou selecione sua conta do WhatsApp Business: Nesta etapa você está definindo onde o número de telefone será…](https://ajuda.sankhya.com.br/hc/article_attachments/42639352414231)

5.1 - Você também estará **criando a identidade pública** da conta de WhatsApp Business.
Essas informações serão exibidas para os clientes finais quando interagirem com a empresa via WhatsApp.

![Imagem 6: 5.1 - Você também estará criando a identidade pública da conta de WhatsApp Business. Essas informações serão exibidas…](https://ajuda.sankhya.com.br/hc/article_attachments/42639373566615)

6 - **Adicione um número de telefone para o WhatsApp:** Nesta etapa você está **definindo e verificando** o número de telefone que será associado à conta do WhatsApp Business.
Após inserir o número e receber o código, basta validar e a configuração estará praticamente concluída.

![Imagem 7: 6 - Adicione um número de telefone para o WhatsApp: Nesta etapa você está definindo e verificando o número de telefone…](https://ajuda.sankhya.com.br/hc/article_attachments/42639352802199)![Imagem 8: 6 - Adicione um número de telefone para o WhatsApp: Nesta etapa você está definindo e verificando o número de telefone…](https://ajuda.sankhya.com.br/hc/article_attachments/42639374074135)

7 - Análise e solicitação: qui você apenas **valida e formaliza** tudo o que foi configurado nas etapas anteriores. É a última confirmação antes da criação completa da estrutura de WhatsApp Business via API.

![Imagem 9: 7 - Análise e solicitação: qui você apenas valida e formaliza tudo o que foi configurado nas etapas anteriores. É a…](https://ajuda.sankhya.com.br/hc/article_attachments/42639358772631)

8 - Sua conta de WhatsApp Business está **ativa**, **conectada à Neppo** e **pronta para operar** via API!
O fluxo Embedded Sign Up foi finalizado com sucesso.

![Imagem 10: 8 - Sua conta de WhatsApp Business está ativa , conectada à Neppo e pronta para operar via API! O fluxo Embedded Sign…](https://ajuda.sankhya.com.br/hc/article_attachments/42639374517911)

Após concluir a etapa da Meta, é possível identificar que o status ainda não está concluido, para isso deve ser realizado algumas etapas no **Gateway Manager**.

![Imagem 11: Após concluir a etapa da Meta, é possível identificar que o status ainda não está concluido, para isso deve ser…](https://ajuda.sankhya.com.br/hc/article_attachments/42639404093335)

9 - Acesse o Gateway Manager através desta URL: <https://gateway-manager.neppo.com.br/#/client>. Acesse a Tab "WhatsApp" e logo após selecione a tab inferior "signup".

![Imagem 12: 9 - Acesse o Gateway Manager através desta URL: https://gateway-manager.neppo.com.br/#/client . Acesse a Tab "WhatsApp"…](https://ajuda.sankhya.com.br/hc/article_attachments/42639378778135)

O número adicionado na jornada da Meta deve aparece na lista dos números na etapa de Signup.

10 - **Vincule a um cliente 360dialog:** Nesta etapa, identifique o número cadastrado na etapa da Meta, clique em **"Vincular A um cliente 360Dialog".**

[GIF animado: Imagem 13: 10 - Vincule a um cliente 360dialog: Nesta etapa, identifique o número cadastrado na etapa da Meta, clique em "Vincular…](https://ajuda.sankhya.com.br/hc/article_attachments/42639404584599)

10.1 - Na aba "Selecionar Cliente" e o campo "Clientes No 360Dialog" será listado todos os clientes que possui o broker 360 Dialog.

10.2 - Caso a configuração seja para um novo cliente, selecione a aba "Novo Cliente", e preencha os campos Nome, email, Nome do Usuário e Tier.

![Imagem 14: 10.2 - Caso a configuração seja para um novo cliente, selecione a aba "Novo Cliente", e preencha os campos Nome, email,…](https://ajuda.sankhya.com.br/hc/article_attachments/42639362998679)

10.3 - Ao selecione o cliente e clicar no botão "Selecione Cliente", é esperado a conclusão da vinculação.

![Imagem 15: 10.3 - Ao selecione o cliente e clicar no botão "Selecione Cliente", é esperado a conclusão da vinculação.](https://ajuda.sankhya.com.br/hc/article_attachments/42639375621527)

No neppo omnichannel, após a vinculação é esperado que o status fique em **"channel\_live",** durante a atualização de status.

![Imagem 16: No neppo omnichannel, após a vinculação é esperado que o status fique em "channel_live", durante a atualização de…](https://ajuda.sankhya.com.br/hc/article_attachments/42639405255959)

10.4 Após a conclusão, o número no Neppo deverá aparecer com status concluído no Neppo Omnichannel, assim como no painel de acompanhamento do 360 Dialog.

![Imagem 17: 10.4 Após a conclusão, o número no Neppo deverá aparecer com status concluído no Neppo Omnichannel, assim como no…](https://ajuda.sankhya.com.br/hc/article_attachments/42639379699607)

11 - Gerar API: Após a conclusão, acesse a tab inferior "Clientes", pesquise pelo número de telefone, verifique os status e caso tudo esteja correto, clique no botão "Gerar chave de API".

[GIF animado: Imagem 18: 11 - Gerar API: Após a conclusão, acesse a tab inferior "Clientes", pesquise pelo número de telefone, verifique os…](https://ajuda.sankhya.com.br/hc/article_attachments/42639391808407)

![Imagem 19: GIF animado: Imagem 18: 11 - Gerar API: Após a conclusão, acesse a tab inferior "Clientes", pesquise pelo número de…](https://ajuda.sankhya.com.br/hc/article_attachments/42639391968279)

12 - Verifique o grupo de atendimento no ambiente Neppo, vá até a área de "Configurações do grupo” e ative a opção "WhatsApp multitenant”, e selecione a opção "MULTITENANT\_360\_CLOUD”

[GIF animado: Imagem 20: 12 - Verifique o grupo de atendimento no ambiente Neppo, vá até a área de "Configurações do grupo” e ative a opção…](https://ajuda.sankhya.com.br/hc/article_attachments/42639376621463)

13 - No **Gateway Manager**, copie a **chave de API** disponível.

- Acesse a aba superior **"Clientes"**.
- Selecione o cliente desejado.
- Clique em **"Configurar Gateways"**.
- Clique no botão **"Novo"** para adicionar um novo gateway.
- Preencha os campos de configuração:

  - **Nome do Gateway**: informe o nome desejado.
  - **Tipo**: selecione **DIALOG\_360\_CLOUD**.
  - **Cluster**: selecione o cluster apropriado.
  - Marque o checkbox **"Ativo"** (se necessário).
  - Em **Propriedades**, cole a **chave de API** copiada.
  - Informe o **Grupo de Atendimento** correspondente.
  - Preencha os demais campos conforme orientação recebida.
- Clique no botão **"Salvar"**.
- Ao finalizar, será exibida a mensagem: **"Gateway configurado com sucesso".**

![Imagem 21: Ao finalizar, será exibida a mensagem: "Gateway configurado com sucesso".](https://ajuda.sankhya.com.br/hc/article_attachments/42639360952343)

Ao finalizar, será exibida a mensagem: **"Gateway configurado com sucesso".**
