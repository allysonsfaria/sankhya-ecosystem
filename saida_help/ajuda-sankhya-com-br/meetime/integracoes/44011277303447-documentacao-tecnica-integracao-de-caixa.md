---
id: "44011277303447"
titulo: "Documentação técnica - Integração de caixa com o Microsoft Outlook/Microsoft 365"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011277303447-Documenta%C3%A7%C3%A3o-t%C3%A9cnica-Integra%C3%A7%C3%A3o-de-caixa-com-o-Microsoft-Outlook-Microsoft-365"
trilha: "Meetime > Integrações"
atualizado_em: "2026-10-05T18:58:57Z"
rotulos: ["sync_hc", "meetime", "meetime_1585", "sync_hash_8bf157b6d571"]
---

# Documentação técnica - Integração de caixa com o Microsoft Outlook/Microsoft 365

## Propósito e Escopo

Este documento descreve a arquitetura técnica, os fluxos de dados, o mecanismo de autenticação e as permissões necessárias para a integração da Meetime com as caixas de correio do Microsoft Outlook / Microsoft 365 através da API Nylas v3.

Destina-se às equipes de Segurança, Privacidade e Governança de TI responsáveis por aprovar integrações de terceiros e avaliar sua postura em relação ao tratamento de dados.

A integração permite à Meetime ler, enviar, organizar e monitorar mensagens de e-mail em nome de usuários finais autorizados. Todo o acesso à caixa de correio é restrito à concessão (grant) individual do usuário e regido pelos fluxos padrão de permissão delegada do OAuth 2.0.

## O que é a Nylas?

A Nylas é uma Plataforma de Comunicação como Serviço (CPaaS) baseada em nuvem que fornece uma camada unificada de API REST para interagir com provedores de e-mail, calendário e contatos, incluindo Microsoft 365 / Outlook, Google Workspace e sistemas baseados em IMAP. A Nylas atua como uma intermediária entre o aplicativo cliente e o provedor de caixa de correio de origem.

Do ponto de vista da topologia de rede, o fluxo de dados é:

- **Caixa de Correio Outlook 365 do Usuário Final** (Microsoft Graph API / Exchange Online)
- ↕ Concessão de acesso delegado OAuth 2.0 emitida pelo Microsoft Entra ID
- **Plataforma Cloud Nylas** (intermediária de processamento de dados)
- ↕ API Nylas v3 (HTTPS/TLS 1.2+)
- **Meetime** (nosso produto)

A Nylas não armazena permanentemente o corpo completo de todos os e-mails; sua plataforma armazena principalmente dados da caixa de correio em cache para atender a solicitações de API e notificações de webhook. Opções de residência de dados estão disponíveis (regiões dos EUA ou UE) e podem ser configuradas no nível do aplicativo Nylas.

## Arquitetura de Autenticação e Autorização

### OAuth 2.0 com Microsoft Entra ID (Azure AD)

A integração usa o fluxo de Código de Autorização do OAuth 2.0 (autenticação moderna) por meio do Microsoft Entra ID (anteriormente Azure Active Directory). Nenhuma senha é compartilhada com a Nylas ou com o aplicativo cliente. As etapas exatas são:

- **Passo 1:** O aplicativo redireciona o usuário para a Autenticação Hospedada pela Nylas, que, por sua vez, redireciona o usuário para a página de login do Microsoft Entra ID.
- **Passo 2:** O usuário se autentica diretamente na Microsoft (SSO, MFA e políticas de acesso condicional se aplicam todas nesta etapa).
- **Passo 3:** A Microsoft emite um Código de Autorização para a Nylas depois que o usuário concede os escopos solicitados.
- **Passo 4:** A Nylas troca o Código de Autorização por um Token de Acesso e um Token de Atualização (Refresh Token) e armazena a credencial como um objeto Grant (Concessão).
- **Passo 5:** O aplicativo recebe um ID de Grant da Nylas, que é utilizado como uma referência estável e opaca para a caixa de correio do usuário — nenhum token OAuth bruto é exposto à camada do aplicativo.

### Modelo de Grant

No modelo Nylas v3, cada caixa de correio conectada é representada como um Grant. Um Grant encapsula o token de acesso OAuth, o token de atualização e os metadados associados. Os Grants são:

- **Por usuário** — um grant por caixa de correio, sem escopo cruzado entre usuários.
- **Revogáveis** — o usuário final ou um administrador pode revogar um grant a qualquer momento através do centro de administração do Microsoft Entra, o que invalida imediatamente a capacidade da Nylas de acessar aquela caixa de correio.
- **Tokens de acesso de curta duração** — os tokens de acesso da Microsoft normalmente expiram após 1 hora; a Nylas os atualiza de forma transparente usando o Token de Atualização.
- **Auditáveis** — todos os eventos de criação e revogação de grants são registrados na trilha de auditoria da Nylas.

### Armazenamento de Tokens

Os tokens OAuth são armazenados exclusivamente dentro da plataforma Nylas usando criptografia em repouso (AES-256) e em trânsito (TLS 1.2+). A Meetime nunca lida com tokens OAuth brutos; ela mantém apenas o ID de Grant opaco da Nylas, que é uma referência interna usada para chamar a API da Nylas em nome da caixa de correio conectada.

## Permissões da API Microsoft Graph (Escopos OAuth)

### Permissões Delegadas Exigidas

A integração solicita as seguintes permissões delegadas do Microsoft Graph. Permissões delegadas operam no contexto do usuário conectado e não podem exceder os próprios privilégios do usuário. Nenhuma permissão em nível de aplicativo (app-only) que permita acesso sem um usuário conectado é solicitada para o fluxo padrão de integração de e-mail.

| Escopo Microsoft Graph | Tipo de Permissão | Propósito |
| --- | --- | --- |
| `Mail.Read` | Delegada | Ler mensagens e metadados de mensagens na caixa de correio do usuário. |
| `Mail.ReadWrite` | Delegada | Atualizar propriedades da mensagem (ex.: marcar como lida, mover para pasta, excluir). |
| `Mail.Send` | Delegada | Enviar e-mail em nome do usuário conectado. |
| `offline_access` | Delegada | Obter e usar Tokens de Atualização para que a integração possa operar sem reautenticação contínua. |
| `openid` | Delegada | Escopo padrão OIDC — recuperar um ID Token que identifica o usuário autenticado. |
| `User.Read` | Delegada | Ler dados básicos do perfil do usuário (nome de exibição, endereço de e-mail) para identificação do grant. |

### O Que NÃO É Solicitado

As seguintes permissões estão explicitamente fora do escopo e não são solicitadas:

- `Mail.ReadBasic.All` / `Mail.Read.All` / `Mail.ReadWrite.All` — Permissões em nível de aplicativo (app-only) que permitem acesso à caixa de correio de qualquer usuário sem login.
- `Contacts.Read` / `Contacts.ReadWrite` — Acesso aos contatos do usuário.
- `Files.Read` / `Files.ReadWrite` — Acesso a arquivos do SharePoint/OneDrive.
- `Calendars.Read` / `Calendars.ReadWrite` — Acesso ao calendário.
- `Directory.Read.All` — Listagem do diretório de todo o locatário (tenant).
- `User.Read.All` — Leitura de todos os usuários no locatário.

### Requisitos de Registro de Aplicativo Azure

### Visão Geral

Para conectar contas Microsoft 365 / Outlook via Nylas, deve existir um Registro de Aplicativo Azure (Azure App Registration) no próprio locatário (tenant) Azure do cliente ou no locatário compartilhado da Nylas. A escolha afeta a experiência de consentimento e o nível de controle disponível para a equipe de TI/Segurança.

| Opção | Descrição | Recomendado Para |
| --- | --- | --- |
| **Aplicativo Compartilhado Nylas** | Usa o Registro de Aplicativo Azure pré-configurado da Nylas. Nenhuma configuração é necessária no locatário do cliente. | Prova de conceito rápida; baixa sobrecarga para a TI. |
| **Aplicativo do Cliente** | Registra um Aplicativo Azure dedicado no próprio locatário do cliente. Controle total sobre permissões, políticas e logs de auditoria. | Produção; ambientes sensíveis à segurança ou regulamentados. RECOMENDADO. |

### Passos para Criar um Registro de Aplicativo Azure do Cliente

1. Faça login no centro de administração do Microsoft Entra (<https://entra.microsoft.com>) como Administrador Global ou Administrador de Aplicativos.
2. Navegue até Aplicativos > Registros de aplicativo > Novo registro.
3. Defina o nome do aplicativo (ex.: 'Integração de E-mail Nylas — Produção').
4. Defina os Tipos de conta com suporte para 'Contas somente neste diretório organizacional (Locatário único)'.
5. Adicione o URI de Redirecionamento fornecido pela Nylas (geralmente <https://api.us.nylas.com/v3/connect/callback> ou o equivalente na UE).
6. Em Permissões de API, adicione as permissões delegadas do Microsoft Graph listadas na Seção "Permissões Delegadas Exigidas".
7. Gere um Segredo do Cliente (ou certificado) e forneça o ID do Cliente e o Segredo para a Nylas através da configuração do conector no Painel da Nylas.
8. Conclua o processo de Verificação de Editor da Microsoft (obrigatório desde novembro de 2020) para evitar avisos de 'editor não verificado' durante o consentimento do usuário.

## Consentimento do Administrador e Aprovação no Nível do Locatário

### Por que o Consentimento do Administrador Pode Ser Necessário

Por padrão, o Microsoft Entra ID permite que usuários individuais consintam com permissões delegadas para aplicativos de editores verificados em escopos de 'baixo impacto'. No entanto, muitos locatários corporativos configuram as Configurações de Consentimento do Usuário para exigir a aprovação do administrador para todos os aplicativos de terceiros. Nesses ambientes, os usuários finais verão uma tela de 'Aprovação Necessária' ou 'Precisa de Aprovação do Administrador' e não conseguirão conectar suas caixas de correio sem a intervenção do administrador.

### Concedendo Consentimento de Administrador para Todo o Locatário

Um Administrador Global do Microsoft Entra ou Administrador de Função Privilegiada pode conceder consentimento de administrador em nome de todos os usuários no locatário seguindo estes passos:

1. Faça login no centro de administração do Microsoft Entra.
2. Vá para Aplicativos > Aplicativos Corporativos e localize o Aplicativo Azure registrado.
3. Selecione Permissões no painel de navegação à esquerda.
4. Clique em 'Conceder consentimento de administrador para [nome do locatário]' e confirme.
5. Verifique se todos os escopos necessários mostram o status 'Concedido para [locatário]'.

Após a concessão do consentimento do administrador, os usuários no locatário poderão conectar suas caixas de correio sem a necessidade de solicitações de consentimento individuais.

### Configurando a Política de Consentimento do Usuário (Recomendado)

A documentação da Nylas recomenda a seguinte configuração do Entra ID para equilibrar segurança e experiência do usuário em aplicativos de editores verificados:

> ⚠ **Configuração Recomendada do Entra ID:** No centro de administração do Microsoft Entra > Aplicativos corporativos > Consentimento e permissões > Configurações de consentimento do usuário, selecione: 'Permitir o consentimento do usuário para aplicativos de editores verificados, para permissões selecionadas (Recomendado).'

Isso permite que os usuários realizem o processo por conta própria para escopos de baixo risco, enquanto ainda exige aprovação do administrador para permissões de alto impacto.

### Lidando com Solicitações de Aprovação de Administrador Feitas por Usuários

Se um usuário tentar autenticar e for bloqueado, ele pode enviar uma solicitação de acesso através da tela 'Precisa de Aprovação do Administrador' da Microsoft. O fluxo é:

- O usuário clica em 'Solicitar aprovação' e insere uma justificativa de negócios.
- A Microsoft envia uma notificação por e-mail aos aprovadores configurados.
- O administrador analisa a solicitação em Entra ID > Aplicativos Corporativos > Solicitações de consentimento do administrador.
- O administrador aprova ou nega. Se aprovado, o usuário pode tentar novamente o fluxo OAuth imediatamente.

## Considerações sobre Acesso a Dados, Processamento e Privacidade

### Dados Acessados via API de E-mail

Através dos escopos OAuth concedidos, a integração pode acessar os seguintes elementos de dados:

| Elemento de Dados | Descrição | Notas |
| --- | --- | --- |
| **Metadados da Mensagem** | Remetente, destinatários, assunto, data, ID da mensagem, local da pasta. | Lidos sob demanda; não armazenados permanentemente pela Nylas além do cache. |
| **Corpo da Mensagem** | Texto completo/conteúdo HTML de mensagens de e-mail. | Processado em trânsito; sujeito à política de retenção de dados da Nylas. |
| **Anexos** | Nomes de arquivos, tipos MIME e conteúdo binário de anexos. | Recuperados apenas sob solicitação explícita via API. |
| **Estrutura de Pastas** | Nomes e hierarquia de pastas da caixa de correio. | Somente leitura; usado para recursos de organização. |
| **Enviar em Nome de** | Mensagens de saída enviadas pela conta do Outlook do usuário. | Enviadas apenas quando a Meetime chama explicitamente a API de Envio. |

### Residência de Dados da Nylas

A Nylas oferece opções configuráveis de residência de dados. Todos os dados são processados e armazenados na região selecionada. As regiões disponíveis são Estados Unidos (EUA) e União Europeia (UE). A região é configurada no nível do Aplicativo Nylas e não pode ser alterada após a criação. Para clientes com requisitos de localização de dados, a região da UE deve ser selecionada durante a configuração inicial.

### Modo de Privacidade Nylas

A Nylas oferece um recurso de Modo de Privacidade que impede que determinados conteúdos da mensagem (corpo, assunto, dados de anexo) sejam registrados ou armazenados pela infraestrutura da Nylas além do que é estritamente necessário para concluir a chamada de API. A ativação do Modo de Privacidade é recomendada para implementações que lidam com comunicações sensíveis ou regulamentadas (ex.: saúde, jurídico, financeiro).

### Conformidade com o GDPR

A Nylas é compatível com o GDPR e fornece Acordos de Processamento de Dados (DPAs) aos clientes. Os dados da caixa de correio individual do usuário são processados com base no consentimento explícito do usuário, concedido durante o fluxo OAuth. A revogação do grant serve como mecanismo técnico para exercer o direito de retirar o consentimento; isso encerra imediatamente o acesso da Nylas à caixa de correio.

## Arquitetura e Controles de Segurança

### Segurança de Transporte

Toda comunicação entre a Meetime e a Nylas utiliza HTTPS (mínimo TLS 1.2, preferencialmente TLS 1.3). Toda comunicação entre a Nylas e a Microsoft Graph API utiliza HTTPS imposto pela Microsoft. A Nylas publica seus certificados de domínio e uma lista de endereços IP estáticos de saída que podem ser adicionados à lista de permissões (allowlist) em firewalls ou gateways de e-mail do cliente.

### Segurança de Tokens OAuth

Os tokens OAuth (Token de Acesso e Token de Atualização) são armazenados exclusivamente dentro da plataforma Nylas, criptografados em repouso (AES-256). Eles nunca são transmitidos ou armazenados pela Meetime. Os Tokens de Acesso da Microsoft têm expiração curta (geralmente 1 hora); a Nylas lida com a renovação transparente usando o Token de Atualização, sem exigir a interação do usuário.

### Segurança de Notificação por Webhook

A Nylas entrega notificações de eventos em tempo real (ex.: novo e-mail recebido) via webhooks HTTPS. Cada payload de webhook é assinado com uma assinatura HMAC-SHA256, permitindo que o endpoint receptor verifique sua autenticidade e integridade. Isso evita ataques de repetição e adulteração de carga útil.

### Ciclo de Vida e Revogação do Grant

O acesso a uma caixa de correio é totalmente controlado através do ciclo de vida do Grant da Nylas:

- Os grants são invalidados automaticamente quando o token OAuth subjacente da Microsoft não pode ser atualizado (ex.: alteração de senha, revogação pelo administrador, mudança de política de acesso condicional).
- **Revogação no nível do usuário:** o usuário pode revogar o acesso a qualquer momento através do portal 'Meus Aplicativos' da Microsoft ([myapps.microsoft.com](http://myapps.microsoft.com)).
- **Revogação no nível de administrador:** um Administrador Global pode revogar o acesso do aplicativo em Entra ID > Aplicativos Corporativos > [Aplicativo] > Permissões, cortando imediatamente todo o acesso à caixa de correio para todos os usuários do locatário.
- **Revogação do lado da Meetime:** A Meetime pode excluir um Grant via API Nylas a qualquer momento, por exemplo, quando um usuário for desligado da empresa.

### Limitação de Taxa (Rate Limiting & Throttling)

O Microsoft Graph aplica limitação de taxa (throttling) específica do serviço, incluindo um limite global de 130.000 requisições a cada 10 segundos por locatário. A Nylas implementa lógica de repetição embutida e recuo exponencial (exponential back-off) para lidar de forma transparente com as respostas de limitação da Microsoft (HTTP 429).

## Limitações e Restrições Conhecidas

- **Ambientes de Nuvem Nacionais:** A Nylas não suporta implementações de nuvens nacionais da Microsoft (Governo dos EUA GCC/GCC High, China, Alemanha). Somente os endpoints globais do Microsoft Entra ID ([microsoftonline.com](http://microsoftonline.com), [office365.com](http://office365.com)) são suportados.
- **Caixas de Correio Compartilhadas e Listas de Distribuição:** A Nylas pode autenticar caixas de correio de usuários individuais e caixas de correio compartilhadas. Ela não pode criar grants para listas de distribuição ou Grupos do Microsoft 365; esses só podem ser adicionados como destinatários de mensagens.
- **Caixas de Correio de Grupo de Administradores:** A Nylas não pode sincronizar contas de e-mail que são membros de grupos de administradores.
- **Exchange Local (Legado):** Há suporte limitado via Exchange Web Services (EWS) para Exchange Server 2003+ que não foi migrado para autenticação moderna. Para Exchange Online e Microsoft 365, utiliza-se o caminho do Microsoft Graph (autenticação moderna).
- **Autenticação Básica Descontinuada:** A partir de 1º de outubro de 2022, a Microsoft descontinuou a autenticação básica para todas as contas do Exchange Online. Somente OAuth 2.0 (autenticação moderna) é suportado.
- **Estabilidade do ID da Mensagem (somente EWS):** Para o Exchange local via EWS, os IDs de mensagem podem mudar quando uma mensagem é movida entre pastas. Isso não afeta o Exchange Online / Microsoft 365, que utiliza o Microsoft Graph.
- **Tags HTML Personalizadas:** O Microsoft Graph não suporta tags HTML personalizadas no corpo das mensagens.

## Itens de Ação para a Equipe de TI / Segurança do Cliente

As seguintes ações podem ser necessárias por parte da equipe de Administração de TI / Microsoft 365 do cliente para habilitar a integração:

| # | Ação | Notas |
| --- | --- | --- |
| **1** | Criar um Registro de Aplicativo Azure no locatário Entra ID do cliente (ou aprovar o uso do Aplicativo Compartilhado Nylas). | Obrigatório — consulte a Seção Passos para Criar um Registro de Aplicativo Azure do Cliente |
| **2** | Adicionar as permissões delegadas obrigatórias do Microsoft Graph ao Registro de Aplicativo. | Obrigatório — consulte a Seção Permissões Delegadas Exigidas |
| **3** | Concluir a Verificação de Editor da Microsoft para o Aplicativo Azure. | Obrigatório desde nov/2020 |
| **4** | Conceder Consentimento de Administrador para todo o locatário para o Registro de Aplicativo, OU configurar a Política de Consentimento do Usuário para permitir o auto-consentimento para editores verificados. | Obrigatório se o consentimento do usuário for restrito — consulte a Seção Consentimento do Administrador e Aprovação no Nível do Locatário |
| **5** | Adicionar endereços IP estáticos de saída da Nylas à lista de permissões em qualquer gateway de e-mail ou regras de firewall que inspecionem conexões HTTPS de saída. | Condicional — veja a doc. da Nylas para a lista de IPs |
| **6** | Configurar a região de residência de dados (EUA ou UE) nas configurações do Aplicativo Nylas antes de o primeiro usuário se conectar. | Obrigatório se houver exigência de localização de dados |
| **7** | Habilitar o Modo de Privacidade nas configurações do Aplicativo Nylas se o registro de conteúdo de mensagens pela Nylas precisar ser minimizado. | Recomendado para dados regulamentados |

Para facilitar o entendimento dos termos técnicos mencionados acima, disponibilizamos um artigo que explica cada um deles de forma detalhada. Para acessar, basta clicar [aqui](https://cloudchat2.cloudhumans.com/hc/meetime/articles/1778616555-glossario-de-termos-tecnicos-_-nylas-e-microsoft).
