---
id: "36918861607959"
titulo: "Carta de autorização: boleto rápido via CNAB automático"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36918861607959-Carta-de-autoriza%C3%A7%C3%A3o-boleto-r%C3%A1pido-via-CNAB-autom%C3%A1tico"
trilha: "Manual do Produto > Financeiro e Patrimônio > Sankhya Fintech > Banking"
atualizado_em: "2026-07-29T13:13:42Z"
rotulos: ["Configuração", "Parceiro", "Boleto", "Financeiro", "CNAB", "Documentos Eletrônicos"]
---

# FAQs

**1. O status está parado em “Aguardando liberação”. O que devo fazer?**
Entre em contato com o gerente responsável pela sua conta bancária e solicite a configuração do canal de troca automática de arquivos CNAB. Se essa configuração já tiver sido realizada, peça que o gerente:

- envie as informações do canal para a VAN e-Sales,
- compartilhe o ID do canal configurado.

Caso essas ações já tenham sido feitas, solicite que o gerente reforce diretamente com a e-Sales a confirmação do recebimento dos dados.

⚠️ Importante
O avanço dessa etapa depende exclusivamente de o banco configurar o canal e informar a e-Sales. Nenhuma ação adicional no ERP fará o status evoluir enquanto essa etapa não for concluída. A Sankhya, a Kobana e a e-Sales não conseguem realizar essa configuração por conta própria. A simples assinatura da carta ou a liberação interna do banco não são suficientes para concluir a etapa.

**2. Se eu errar algum dado da carta ou da conta, o que acontece?**
O processo pode:

- ser recusado pelo banco,
- ser configurado erroneamente e impossibilitar a troca automática de arquivos,
- ficar travado sem avanço,
- gerar retrabalho e atraso.

Por isso, é essencial preencher todos os dados corretamente antes de enviar.
Caso você identifique que algum dado foi informado incorretamente, entre em contato com o seu gerente bancário e forneça os dados corretos diretamente ao banco.
Não é obrigatória a geração de uma nova carta, pois ela tem caráter formal e o ajuste pode ser realizado diretamente entre o responsável pela conta e a instituição bancária.

**3. Quando posso finalizar o credenciamento no ERP?**
Quando o status estiver como “Pronto para credenciar”. A partir daí, basta clicar em “Credenciar” na jornada de credenciamento para concluir.

**4. O que acontece após preencher os dados solicitados para geração da carta de autorização e clicar em “Enviar” na jornada de adesão?**

A carta é gerada automaticamente e um e-mail é disparado para todos os envolvidos. Na carta de autorização, solicitamos acesso da Kobana e da e-Sales para compartilhar dados dos boletos através do canal de troca de arquivos CNAB.

Caso você seja o responsável pela conta ou pela carta, indicamos procurar no seu e-mail pelo título “Carta para Autorização de Integração” que você terá acesso ao e-mail com a carta que também foi compartilhada com o seu gerente do banco.

**5. Preciso entrar em contato com a Kobana ou com a e-Sales?**
Não. A Kobana e a e-Sales são contratadas pela Sankhya Fintech e não atendem clientes Sankhya diretamente. Caso haja algum problema no fluxo, entre em contato com o Service Desk Sankhya através da abertura de ticket.

⚠️ Importante

Antes de abrir o ticket, recomendamos fortemente que entre em contato com o seu gerente de conta da instituição bancária, valide se o canal de troca automática de arquivos está devidamente configurado e se a VAN e-Sales já recebeu o id do canal ativo em produção.

**6. O banco solicitou homologação de credenciais. O que devo fazer?**
Caso o seu banco seja Caixa ou Safra, casos de integração mista, não utilizamos credenciais no processo. Retorne para o banco e informe que você deseja configurar a troca automática de arquivos CNAB e siga com eles por este processo.

**7. A liberação do processo depende da Sankhya?**
Não. A liberação depende exclusivamente do banco configurar as credenciais e informar a VAN e-Sales. Após este processo, a Sankhya recebe uma confirmação que o processo está configurado e a abertura para finalização do credenciamento é feita automaticamente. Mesmo sendo responsável pelo serviço, neste caso, a Sankhya entra como orquestradora da jornada, mas não tem ingerência sobre as etapas bancárias.

**8. O que é a VAN bancária e qual seu papel?**
A VAN bancária (e-Sales) é a responsável por:

- receber os arquivos CNAB,
- transmiti-los automaticamente ao banco,
- garantir a segurança e a homologação da troca.

A Kobana, parceira da Sankhya Fintech, é quem envia automaticamente os arquivos para a e-Sales, que então faz a entrega ao banco.

**9. Por que ainda preciso ativar a troca automática de arquivos CNAB se já existe API?**
Porque alguns bancos ainda não oferecem integração 100% via API para todas as operações.
Nos casos da Caixa Econômica Federal e do Banco Safra, por exemplo:

- o registro de boletos ocorre via API,
- alterações, cancelamentos e liquidações precisam ser feitas via CNAB.

Por isso, a automação é completa, porém em modelo misto (API + CNAB). Esse formato garante a continuidade da automação mesmo com limitações tecnológicas do banco.

# Funcionalidade: boleto rápido via CNAB automático

O Boleto Rápido API automatiza a emissão e a gestão de boletos bancários de recebimento diretamente no ERP Sankhya, garantindo maior eficiência, controle e padronização da operação.

No entanto, alguns bancos ainda não disponibilizam integração completa via API. Por esse motivo, para que todo o fluxo de recebimento com boletos seja totalmente automatizado, é necessária a conexão com a instituição bancária por meio da troca automática de arquivos CNAB. Nessas instituições, parte da operação ocorre via API, enquanto outra parte depende da troca automática de arquivos CNAB, realizada por meio da terceirização com uma VAN bancária homologada pela Sankhya Fintech.

Assim, para concluir corretamente o credenciamento da conta nesses bancos, é indispensável também a **ativação do canal de troca automática de arquivos CNAB entre o banco e a VAN bancária**.

Bancos que atualmente utilizam modelo misto de conexão (com API e com CNAB automático):

- Caixa Econômica Federal,
- Banco Safra.

## Como funciona a ativação do canal CNAB

**1. Preenchimento dos dados para envio da carta de autorização**
Nesta etapa, você vai preencher as informações necessárias para enviar uma carta de autorização. Essa carta de autorização formaliza um pedido de ativação do canal de troca automática de arquivos CNAB, dando a permissão para a Kobana, nossa parceira homologada, transmitir os arquivos no diretório bancário.

Dentro da jornada de ativação é necessário preencher os campos que fornecem dados:

- Do responsável pela conta bancária:
  - Nome completo
  - E-mail
  - Telefone
  - CPF
- Do gerente do banco responsável pela sua conta bancária:
  - Nome completo
  - E-mail
  - Telefone
- De quem está preenchendo a carta:
  - Nome completo
  - E-mail
  - Telefone

A troca de arquivos CNAB com o banco será feita de forma automática pela Kobana, nossa parceira autorizada para esse tipo de serviço.

Após o preenchimento correto das informações, clique em “Enviar” para gerar o e-mail automático para todos os e-mails preenchidos no cadastro. Após finalização, o status da sua solicitação deve ser Preenchimento dos dados da carta de autorização - Enviado.

**2. Envio da carta de autorização**
Os dados preenchidos, juntamente com as informações de conta inseridas em “Dados de conta” geram automaticamente a carta de autorização, que é enviada aos destinatários inseridos via e-mail. Procure este e-mail na sua caixa de entrada e informe ao seu gerente que o e-mail foi enviado.

O responsável pela conta bancária e o responsável pela carta também receberão um e-mail da Kobana confirmando que a carta foi mandada para o banco.

Neste momento, o status da sua solicitação deve ser Envio da carta de autorização - Enviado.

**3. Recebimento da carta de autorização**
Ao receber a carta de autorização via e-mail, o banco precisa:

- ativar o canal de transmissão automática de arquivos CNAB em produção,
- configurá-lo para troca automática com a VAN e-Sales,
- avisar a equipe da e-Sales que o canal está devidamente configurado, informando o id do canal,
- a jornada só é ativada após confirmação da VAN e-Sales de que o banco configurou e compartilhou o canal que será utilizado.

Se tudo estiver configurado, o status da sua solicitação deve ser Liberação do processo pela instituição bancária - Feito.
A partir deste status, você poderá finalizar o seu credenciamento clicando no botão “Credenciar”.
