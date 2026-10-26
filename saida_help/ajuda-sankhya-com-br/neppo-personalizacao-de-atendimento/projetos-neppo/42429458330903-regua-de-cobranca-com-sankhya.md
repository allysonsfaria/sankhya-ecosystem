---
id: "42429458330903"
titulo: "Régua de cobrança com Sankhya"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42429458330903-R%C3%A9gua-de-cobran%C3%A7a-com-Sankhya"
trilha: "NEPPO: Personalização de atendimento > Projetos Neppo"
atualizado_em: "2026-08-11T17:13:39Z"
rotulos: ["sync_hc", "neppo", "neppo_176881665", "sync_hash_a0eec0c3d3cf"]
---

# Régua de cobrança com Sankhya

A Régua de Cobrança da Sankhya, ao integrar-se com a plataforma Neppo, visa aprimorar a eficiência e a eficácia dos processos de cobrança das empresas. Essa integração permite a automação de comunicações com clientes por meio do WhatsApp, facilitando o envio de boletos, notas fiscais, notificações de vencimento e lembretes diretamente por esses meios.

Este projeto será executado no ambiente **Sankhya** do cliente a partir da versão 4.35.
Para consulta da documentação do ERP Sankhya, consulte neste [link](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602534-R%C3%A9gua-de-Cobran%C3%A7a#EnviodeWhatsApp)

Esta documentação é para uso interno

#### O cliente precisar estar na versão 1.0.44 da chat-API ou superior

🎥 [Assistir vídeo na documentação de origem (Confluence): L9yEm9yxDCS74WjxM6S6MGaeyns5CXc7Xy2jNR2c\_transcoded.mp4](https://sankhya.zendesk.com/hc/pt-br/articles/42429458330903)

- [Habilitar parâmetro no ERP](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429458330903-R%C3%A9gua-de-cobran%C3%A7a-com-Sankhya#Habilitar-parametro-no-ERP)
- [Configurações inicias](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429458330903-R%C3%A9gua-de-cobran%C3%A7a-com-Sankhya#Configuracoes-inicias)
- [Configurações de template e campanha](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429458330903-R%C3%A9gua-de-cobran%C3%A7a-com-Sankhya#Configuracoes-de-template-e-campanha)
- [Jornada no ERP](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429458330903-R%C3%A9gua-de-cobran%C3%A7a-com-Sankhya#Jornada-no-ERP)
- [Códigos de erro](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429458330903-R%C3%A9gua-de-cobran%C3%A7a-com-Sankhya#Codigos-de-erro)
- [FAQ](https://ajuda.sankhya.com.br/hc/pt-br/articles/42429458330903-R%C3%A9gua-de-cobran%C3%A7a-com-Sankhya#FAQ)

## Habilitar parâmetro no ERP

Para que o cliente utilize a funcionalidade no ERP, é necessário habilitar o parâmetro:

- USAWHATSREGUA – **Habilita o evento WhatsApp na régua**.

Esse parâmetro pode ser ativado na tela [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias) no ERP Sankhya. Após a ativação, a rotina **Régua de Cobrança** passa a exibir o evento **Envio de WhatsApp** para configuração.

## Configurações inicias

Dentro do modal do envio através de WhatsApp, se o cliente da Sankhya ainda não for cliente da Neppo, ele deverá escolher a opção **"Ainda não sou cliente Neppo"**. Ao selecionar essa opção, será exibido um formulário para preenchimento. As informações preenchidas serão enviadas automaticamente para o time comercial, por meio de uma integração com o Active Campaign.

Para prosseguir, o cliente deverá preencher os seguintes campos e aceitar a política de privacidade:

- Nome completo
- E-mail corporativo
- Nome da empresa
- Telefone

![Imagem 1: Telefone](https://ajuda.sankhya.com.br/hc/article_attachments/42639322929815)

### Para clientes Neppo e Sankhya

![Imagem 2: Para clientes Neppo e Sankhya](https://ajuda.sankhya.com.br/hc/article_attachments/42639339404183)

Se o cliente **já for cliente da Neppo**, ele deverá selecionar a opção **"Já sou cliente Neppo"**. Em seguida, será necessário informar as credenciais do ambiente produtivo da Neppo, preenchendo os seguintes dados:

- Chave do Consumidor
- Senha do Consumidor
- Usuário
- Senha

Para acessar as credenciais, acesse: **Integrações > Neppo Token API > Gerar credenciais**

[GIF animado: Imagem 3: Para acessar as credenciais, acesse: Integrações > Neppo Token API > Gerar credenciais](https://ajuda.sankhya.com.br/hc/article_attachments/42639323482647)

- Copia e cole as informações no ERP

Com essas informações, será possível prosseguir com o envio de cobranças via WhatsApp.

## Configurações de template e campanha

### Parte 1: No broker

Para iniciar, é necessário ter dois tipos de templates cadastrados no Broker de Whatsapp oficial do cliente.

- **Campanha com anexo. Exemplo:**

![Imagem 4: Campanha com anexo. Exemplo:](https://ajuda.sankhya.com.br/hc/article_attachments/42639347763991)

- **Campanha sem anexo. Exemplo:**

![Imagem 5: Campanha sem anexo. Exemplo:](https://ajuda.sankhya.com.br/hc/article_attachments/42639347959831)

**Exemplo de template:**

| Prezado cliente &{NOME\_PARCEIRO},  Sua(s) fatura(s) está(ão) se aproximando do vencimento.  Dados do título(s):  &Número\_Nota  Qualquer dúvida, entre em contato conosco respondendo esta mensagem. |
| --- |

Para concluir, realize o cadastro dos templates dentro da Neppo.

A partir da entrega do CORE-613, não será necessário cadastrar os templates no Neppo, somente no broker 360dialog.

### Parte 2: Na Neppo

Regras:

- Após cadastrar o template no Neppo. Acesse a tela de campanha e selecione o tipo **"Régua de cobrança com Sankhya".**

Para acessar, siga: **Home > Campanha**

Preencha os parâmetros de acordo com os campos disponíveis da Sankhya.

[GIF animado: Imagem 6: Preencha os parâmetros de acordo com os campos disponíveis da Sankhya.](https://ajuda.sankhya.com.br/hc/article_attachments/42639354581143)

Há uma campanha com o nome **Campanha régua de cobrança Sankhya sem anexos** com **ID 999999999 na URL**. **Não altere o nome desta campanha!** Ela serve de referência para o teste de conexão de API no ERP. O template deve ser cadastrado no broker do cliente. Essa campanha tem finalidade apenas de testes.

## Jornada no ERP

**Etapas da configuração do envio**
Após a autenticação, ao configurar o evento **Envio de WhatsApp**, siga as etapas abaixo:

#### Evento

- Informe a **Descrição do evento** (texto que será exibido ao passar o mouse sobre o ícone na régua).

![Imagem 7: Informe a Descrição do evento (texto que será exibido ao passar o mouse sobre o ícone na régua).](https://ajuda.sankhya.com.br/hc/article_attachments/42639335869463)

#### Template

- Defina se deseja **enviar anexo**:

  - Não Enviar;
  - PDF do DANFE;
  - Anexar Boleto.

![Imagem 8: Anexar Boleto.](https://ajuda.sankhya.com.br/hc/article_attachments/42639354924183)

**Observação**: a Meta não permite mais de um anexo por mensagem. Portanto, **não é permitido enviar boleto e PDF no mesmo evento**.

- No campo **Mensagem para envio de WhatsApp (Template de mensagens Neppo)**, será exibida a lista de templates cadastrados na Neppo para o parceiro. Selecione o template desejado.

A lista de templates é carregada automaticamente da Neppo. Ao criar novos templates, utilize o botão "Atualizar".

A seleção do template depende do tipo de anexo:

- **PDF do DANFE** ou **Anexar Boleto** → exige templates com variáveis de anexo;
- **Não Enviar** → permite apenas templates sem variáveis de anexo.
- No campo **Acontece**, defina o momento do disparo:

  - Antes do vencimento (informe o número de dias);
  - No vencimento;
  - Após o vencimento (informe o número de dias);
  - Ao baixar (quando o título for baixado).
- Marque a opção **Executar apenas em dias úteis**, se necessário.
- Avance clicando em **"Próximo"**.

**Destinatários**

![Imagem 9: Destinatários](https://ajuda.sankhya.com.br/hc/article_attachments/42639324690839)

Selecione o(s) destinatário(s) da cobrança:

- **Parceiro**: utiliza o telefone cadastrado na aba Endereço do Cadastro de Parceiros;
- **Contato do parceiro**: utiliza o número de celular da aba Contatos, sub-aba Geral.

**Regras para envio:**

1. Envia para todos os contatos **ativos** com número de celular preenchido e com a marcação **"Responsável pela cobrança"**.
2. Se não houver, envia para o primeiro contato **ativo** com celular preenchido e marcação **"Recebe boleto/Pix p/ email"**.
3. Se nenhum contato atender às condições acima, **nenhuma mensagem será enviada**.

**Teste de conexão**

Essa etapa verifica se as credenciais estão corretas e permite validar a conexão com a API da Neppo.

![Imagem 10: Essa etapa verifica se as credenciais estão corretas e permite validar a conexão com a API da Neppo.](https://ajuda.sankhya.com.br/hc/article_attachments/42639370128279)

Para realizar o teste:

1. Preencha o campo **Destinatário** com um número de telefone (com DDD);
2. Informe um **Número Único Financeiro** válido (utilizado para buscar variáveis da mensagem);
3. Clique no botão **"Testar conexão"**.

Se a conexão com a API for bem-sucedida, será exibida a mensagem:

**"Sucesso: Conexão da API bem-sucedida"**

Este teste valida apenas a entrega da mensagem para a Neppo, não garante a entrega final via WhatsApp (Meta).

**Filtro**

Nesta etapa, você pode aplicar **filtros específicos** conforme as regras de cobrança da empresa.

![Imagem 11: Nesta etapa, você pode aplicar filtros específicos conforme as regras de cobrança da empresa.](https://ajuda.sankhya.com.br/hc/article_attachments/42639349415831)

Ao clicar em  **"Testar resultado"**, será exibido um pop-up para informar a **Data de execução**. Após aplicar, o sistema listará os títulos que seriam considerados para envio de cobrança naquela data.

Finalize clicando em **"Concluir"**, e o evento será incluído na régua de cobrança.

#### Exemplo prático da usuabilidade:

Imagine uma régua com os seguintes eventos configurados:

- **Envio de WhatsApp:** 3 dias antes do vencimento;
- **Envio de e-mail:** no vencimento;
- **Envio de SMS:** 3 dias após o vencimento.

![Imagem 12: Envio de SMS: 3 dias após o vencimento.](https://ajuda.sankhya.com.br/hc/article_attachments/42639386833175)

Na execução do evento, serão enviados à Neppo os seguintes dados para cada cobrança:

- Número Único Financeiro
- Telefone do destinatário
- Número da nota
- Data de vencimento
- Valor líquido
- Linha digitável
- E-mail da empresa
- Nome da empresa
- CNPJ da empresa
- Razão Social da empresa
- Nome do parceiro
- CNPJ do parceiro
- Template selecionado

| Parametro | Exemplo |
| --- | --- |
| - Número Único Financeiro |  |
| - Telefone do destinatário | "recipient": "+5534991731440" |
| - Número da nota | "numnota": "689" |
| - Data de vencimento | "dt\_vencimento": "01-01-2024" |
| - Valor líquido | "vlr\_liquido": "1.55" |
| - Linha digitável | "linha\_digitavel": "12345678910" |
| - E-mail da empresa |  |
| - Nome da empresa |  |
| - CNPJ da empresa | "empresa\_cnpj": "77.136.423/0001-68", |
| - Razão Social da empresa | "empresa\_razao\_social": "Sankhya/Jiva" |
| - Nome do parceiro | "parceiro\_nome": "Start", |
| - CNPJ do parceiro | "parceiro\_cnpj": "01.644.080/0001-80", |
| - Template selecionado |  |

A Neppo processará essas informações, substituirá as variáveis no template e enviará a mensagem ao cliente.

**Observação:** o envio ocorre por **número financeiro/destinatário**. Por exemplo:

- Nota 10 → financeiro 112425 → parceiro Joseph → telefone (34) 99999-9999
- Nota 11 → financeiro 112427 → parceiro Joseph → telefone (34) 99999-9999
  Resultado: **duas mensagens serão enviadas**, contabilizando **dois disparos ativos**.

![Imagem 13: Nota 11 → financeiro 112427 → parceiro Joseph → telefone (34) 99999-9999 Resultado: duas mensagens serão enviadas ,…](https://ajuda.sankhya.com.br/hc/article_attachments/42639325629975)

## Códigos de erro

| Código HTTP | Erro | Descrição | Ação Recomendada |
| --- | --- | --- | --- |
| **401** | `invalid credentials` | As credenciais fornecidas para autenticação são inválidas ou expiraram. | Verifique credenciais utilizadas. Refaça a autenticação, se necessário. |
| **400** | `data is invalid or empty` | Os dados enviados na requisição estão vazios ou com formato inválido. | Confirme se os campos obrigatórios estão preenchidos corretamente e com dados válidos. |
| **400** | `campaignId invalid` | O ID da campanha informado não existe ou não está registrado corretamente. | Verifique o ID da campanha na plataforma de origem antes de realizar a requisição. |
| **400** | `campaign not active` | A campanha informada não está ativa, impossibilitando o envio pela régua de cobrança. | Ative a campanha na plataforma ou selecione uma campanha ativa. |
| **400** | `campaign without transformation data script` | A campanha não possui um script de transformação de dados configurado, necessário para o envio | Configure corretamente o script de transformação no cadastro da campanha. |
| **400** | `campaign don't have default send group` | A campanha não possui um grupo de envio padrão definido, o que impede a execução da régua. | Defina um grupo de envio padrão nas configurações da campanha. |

Para consulta de erros relacionado a API oficial do whatsapp, consultar na documentação da Meta: <https://developers.facebook.com/docs/whatsapp/cloud-api/support/error-codes/#error-codes>

## FAQ

Sim, é possível. O usuário deve gerar as credenciais no ambiente Neppo e configurá-las dentro do ERP. Importante destacar que a criação de templates e campanhas também precisa ser realizada conforme documentação acima.

Neste projeto da Régua de Cobrança Sankhya com a Neppo, o ERP transmite para a Neppo apenas os campos padrão do próprio sistema. Campos personalizados do cliente não são suportados. Para tratar essas necessidades, consulte a equipe de Produtos, Implantação ou Serviços da Neppo.

A integração nesse cenário funcionará normalmente, utilizando o conceito de Operações da plataforma. Na Neppo, cada número de WhatsApp é associado a um grupo de envio, e no momento do cadastro da campanha é possível selecionar esse grupo, definindo assim por qual número a campanha será enviada. Por isso, como boa prática, recomenda-se incluir no título da campanha o nome da empresa ou operação responsável, facilitando a visualização e distinção no ERP.
