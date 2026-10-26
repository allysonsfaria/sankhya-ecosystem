---
id: "44011650125079"
titulo: "Transparência e Uso de Dados: Integração com a Amazon"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011650125079-Transpar%C3%AAncia-e-Uso-de-Dados-Integra%C3%A7%C3%A3o-com-a-Amazon"
trilha: "Magis5 > Magis5 HUB"
atualizado_em: "2026-10-05T19:07:43Z"
rotulos: ["sync_hc", "magis5", "magis5_217850978166", "sync_hash_27d065b322f4"]
---

# Transparência e Uso de Dados: Integração com a Amazon

## Entenda, neste guia, como funciona a transparência no uso de dados com a Amazon.

---

A integração do **Magis5** com a Amazon, através da Selling Partner API (SP-API), foi desenvolvida para automatizar e otimizar a gestão das suas vendas.

Levamos a privacidade, a segurança e a transparência muito a sério. Este manual explica detalhadamente como nossa aplicação se conecta à sua conta de vendedor da Amazon, quais dados são processados e como garantimos a conformidade com as rigorosas diretrizes de segurança da plataforma.

### 1. Como a Integração Funciona

Nossa aplicação utiliza o padrão OAuth **(Login com a Amazon)** para conectar o nosso sistema à sua conta na **Amazon Seller Central**.

- **Sem necessidade de senhas:** Nós nunca solicitamos ou armazenamos a sua senha da Amazon.
- **Acesso via Tokens:** O acesso é concedido de forma segura via tokens gerados pela própria Amazon, garantindo que você tenha controle total sobre a autorização.

### 2. Finalidade da Coleta de Dados

Operamos sob o princípio da **Minimização de Dados**. Isso significa que a nossa aplicação solicita acesso estritamente aos dados necessários para fornecer o nosso serviço de gestão de pedidos e anúncios.

- Os dados obtidos via **SP-API** são utilizados **exclusivamente para beneficiar você** **(o vendedor parceiro da Amazon)** na operação do seu negócio e no cumprimento das suas obrigações de venda.
- Nós não vendemos, não compartilhamos com terceiros não autorizados e não utilizamos seus dados ou os dados dos seus clientes para análises competitivas ou campanhas de marketing próprias.

### 3. Dados Processados pela Aplicação

Para que o Magis5 funcione corretamente, acessamos as seguintes categorias de dados via SP-API:

- **Dados de Pedidos:** Informações gerais dos pedidos **(produtos, valores e status)** para possibilitar a gestão completa da venda.
- **Dados de Anúncios e Catálogo:** Informações sobre os seus produtos, preços e ofertas para permitir a criação, sincronização e gestão contínua dos seus anúncios entre o nosso sistema e a Amazon.

### 4. Tratamento de Informações Pessoais (PII)

A Amazon classifica dados como nome, endereço e telefone do comprador como **Informações Pessoais (PII - Personally Identifiable Information)**. Tratamos esses dados com o mais alto nível de restrição:

- **Uso Restrito:** Dados de PII de clientes da Amazon são utilizados única e exclusivamente para o cumprimento do pedido, logística e obrigações legais **(como a emissão de Notas Fiscais)**.
- **Proibição de Marketing:** É terminantemente proibido o uso de PII de clientes oriundos da Amazon para o envio de e-mails de marketing, promoções ou qualquer comunicação não relacionada diretamente à entrega do pedido.
- **Criptografia:** Todas as Informações Pessoais são criptografadas tanto em trânsito **(durante a transferência entre a Amazon e nossos servidores)** quanto em repouso **(no nosso banco de dados)**.

### 5. Segurança da Informação

A nossa infraestrutura atende aos rigorosos requisitos de Proteção de Dados da Amazon:

- **Controle de Acesso:** Apenas colaboradores autorizados, treinados e sob acordos de confidencialidade (NDA) têm acesso a sistemas que processam dados de integração, operando sempre sob o princípio do menor privilégio.
- **Monitoramento e Resposta a Incidentes:** Possuímos rotinas contínuas de monitoramento de segurança e planos de resposta a incidentes (Incident Response Plan) para garantir que suas informações estejam sempre blindadas contra acessos não autorizados.

### 6. Como Revogar o Acesso

Você tem o controle total sobre a integração. Caso deseje desconectar o Magis5 da sua conta Amazon, você pode revogar a autorização a qualquer momento diretamente pela sua Seller Central:

1. Acesse sua conta na **Amazon Seller Central**.
2. Vá em **Configurações > Permissões da conta** (ou Appstore > Gerenciar seus aplicativos).
3. Localize o **Magis5** na lista.
4. Clique em **Desativar** ou **Revogar autorização**.

⚠️ **Atenção:** Ao realizar esse procedimento, nosso sistema perderá imediatamente o acesso aos seus dados na Amazon e a sincronização será interrompida.

- **Para dúvidas adicionais sobre como gerenciamos seus dados ou sobre nossa integração técnica com a Amazon, entre em contato através dos nossos canais [oficiais de atendimento](https://ajuda.sankhya.com.br/canais-de-atendimento-magis5?hsLang=pt-br).**
