---
id: "36551875605911"
titulo: "Como obter credenciais do Banco Bradesco?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36551875605911-Como-obter-credenciais-do-Banco-Bradesco"
trilha: "Manual do Produto > Financeiro e Patrimônio > Sankhya Fintech > Banking"
atualizado_em: "2026-09-25T12:39:38Z"
rotulos: ["Parceiro", "Boleto", "PIX", "API", "Credenciais", "Bradesco"]
---

# Como obter credenciais do Banco Bradesco?

Para adquirir as credenciais do **Banco Bradesco** e ativar a funcionalidade de Boleto Simples, Híbrido ou PIX via API, siga as instruções abaixo:

**Vincular  a SANKHYA como um PARCEIRO através da sua Conta Bradesco:**

1.1 Acesse o [Net Empresa](https://www.ne12.bradesconetempresa.b.br/ibpjlogin/login.jsf) do Bradesco e realize o login com seu usuário/senha

![Imagem 1: 1.1 Acesse o Net Empresa do Bradesco e realize o login com seu usuário/senha](https://ajuda.sankhya.com.br/hc/article_attachments/36551875594135)

1.2 Acesse a aba **‘Serviços Operacionais’**

![Imagem 2: 1.2 Acesse a aba ‘Serviços Operacionais’](https://ajuda.sankhya.com.br/hc/article_attachments/36551853648023)

1.3 Clique em API :: **Integração com parceiros**

![Imagem 3: 1.3 Clique em API :: Integração com parceiros](https://ajuda.sankhya.com.br/hc/article_attachments/36551853653015)

1.4 Preencha os dados

- Produto = **API**
- Serviço = **Integração com Parceiro**
- Tipo = **Contratação**

![Imagem 4: Tipo = Contratação](https://ajuda.sankhya.com.br/hc/article_attachments/36551853653783)

1.5 Preencha os dados solicitados no cadastro

**Importante:** Em ‘Parceiro Integrador’ selecione o parceiro = **SANKHYA**

![Imagem 5: Importante: Em ‘Parceiro Integrador’ selecione o parceiro = SANKHYA](https://ajuda.sankhya.com.br/hc/article_attachments/36551875599895)

1.8 Siga as etapas para que o usuário MASTER aprove  a solicitação

1.9 Certifique-se que a solicitação foi confirmada

![Imagem 6: 1.9 Certifique-se que a solicitação foi confirmada](https://ajuda.sankhya.com.br/hc/article_attachments/36551875602071)

Feito isso, inicie o processo de geração das credenciais:

**Geração das Credenciais:**

**Importante:**

| Para facilitar sua integração, reunimos aqui o passo a passo disponibilizado pelo Bradesco para criação das credenciais. Caso surjam dúvidas ou seja necessário suporte durante o processo, o **contato deve ser feito diretamente com o Bradesco**, |
| --- |

**2.1 Inscrição ao Portal Developers**

Acessar o [Portal Developers](https://developers.bradesco.com.br/#iss=https%3A%2F%2Flogin.axway.com%2Fauth%2Frealms%2FBroker) e seguir as etapas demonstradas abaixo, conforme instruções Bradesco :

![Imagem 7: Acessar o Portal Developers e seguir as etapas demonstradas abaixo, conforme instruções Bradesco :](https://ajuda.sankhya.com.br/hc/article_attachments/36782473793431)

![Imagem 8: Acessar o Portal Developers e seguir as etapas demonstradas abaixo, conforme instruções Bradesco :](https://ajuda.sankhya.com.br/hc/article_attachments/36782473794327)

![Imagem 9: Acessar o Portal Developers e seguir as etapas demonstradas abaixo, conforme instruções Bradesco :](https://ajuda.sankhya.com.br/hc/article_attachments/36782473795223)

![Imagem 10: Acessar o Portal Developers e seguir as etapas demonstradas abaixo, conforme instruções Bradesco :](https://ajuda.sankhya.com.br/hc/article_attachments/36782435015447)

**2.2 Acesso ao Portal Developers**

![Imagem 11: 2.2 Acesso ao Portal Developers](https://ajuda.sankhya.com.br/hc/article_attachments/36782473797015)

![Imagem 12: 2.2 Acesso ao Portal Developers](https://ajuda.sankhya.com.br/hc/article_attachments/36782473798167)

**2.3 Inscrição para os produtos desejados**

Nesta etapa, selecione apenas o produto — o que corresponde à modalidade de boleto ou ao serviço que o cliente vai utilizar:

![Imagem 13: Nesta etapa, selecione apenas o produto — o que corresponde à modalidade de boleto ou ao serviço que o cliente vai…](https://ajuda.sankhya.com.br/hc/article_attachments/36782473799191)

- Boleto Híbrido (boleto com QR Code para pagamento via PIX): selecione **Cobrança com QR Code**
- Boleto Simples (cobrança exclusivamente por código de barras ou linha digitável): selecione **Cobrança**
- Para PIX: selecione **PIX - Geração de QR Code**

**⚠️ Atenção**

Selecionar o produto errado para a modalidade de boleto contratada gera falha ao usar a API de boletos do Bradesco — o credenciamento é concluído, mas as chamadas à API retornam erro. Confirme com o cliente qual modalidade foi contratada (Boleto Híbrido ou Boleto Simples) antes de inscrever o produto no Portal Developers.

![Imagem 14: Selecionar o produto errado para a modalidade de boleto contratada gera falha ao usar a API de boletos do Bradesco — o…](https://ajuda.sankhya.com.br/hc/article_attachments/36782473804311)

Selecionado o produto, clique em ‘Inscrever-se’ para efetuar a assinatura no produto selecionado

![Imagem 15: Selecionado o produto, clique em ‘Inscrever-se’ para efetuar a assinatura no produto selecionado](https://ajuda.sankhya.com.br/hc/article_attachments/36782473805591)

**Importante !**

No próximo passo, atente-se a seguinte informação : Para Integração aos serviços Fintech só serão aceitas Credenciais geradas em **PRODUÇÃO**.

![Imagem 16: No próximo passo, atente-se a seguinte informação : Para Integração aos serviços Fintech só serão aceitas Credenciais…](https://ajuda.sankhya.com.br/hc/article_attachments/36782435024791)

![Imagem 17: No próximo passo, atente-se a seguinte informação : Para Integração aos serviços Fintech só serão aceitas Credenciais…](https://ajuda.sankhya.com.br/hc/article_attachments/36782435025815)

**2.4 Registro da aplicação**

![Imagem 18: 2.4 Registro da aplicação](https://ajuda.sankhya.com.br/hc/article_attachments/36782435027735)

![Imagem 19: 2.4 Registro da aplicação](https://ajuda.sankhya.com.br/hc/article_attachments/36782473808791)

![Imagem 20: 2.4 Registro da aplicação](https://ajuda.sankhya.com.br/hc/article_attachments/36782435029911)

![Imagem 21: 2.4 Registro da aplicação](https://ajuda.sankhya.com.br/hc/article_attachments/36782473810455)

![Imagem 22: 2.4 Registro da aplicação](https://ajuda.sankhya.com.br/hc/article_attachments/36782473811223)

Obs: Indicamos que todos os recursos ‘Produção’ sejam selecionados

![Imagem 23: Obs: Indicamos que todos os recursos ‘Produção’ sejam selecionados](https://ajuda.sankhya.com.br/hc/article_attachments/36782435034391)

**2.5 Geração das Credenciais**

![Imagem 24: 2.5 Geração das Credenciais](https://ajuda.sankhya.com.br/hc/article_attachments/36782473812631)

![Imagem 25: 2.5 Geração das Credenciais](https://ajuda.sankhya.com.br/hc/article_attachments/36782435036823)

**Importante:**

| Na etapa acima, no campo ‘**Certificado Público no formato .pem .cer ou .crt’**, deverá ser inserido o certificado baixado no SANKHYA.  Este certificado será encontrado em : Assistente de Melhores Práticas :: Configurações serviços Fintech :: Boleto Rápido :: Selecionar Conta Bradesco :: Etapa ‘Credenciais via API’ :: Campo **‘Baixar Certificado’**  ![Imagem 26: Este certificado será encontrado em : Assistente de Melhores Práticas :: Configurações serviços Fintech :: Boleto…](https://ajuda.sankhya.com.br/hc/article_attachments/42309696246807) |
| --- |

![Imagem 27: Este certificado será encontrado em : Assistente de Melhores Práticas :: Configurações serviços Fintech :: Boleto…](https://ajuda.sankhya.com.br/hc/article_attachments/36782473815063)

![Imagem 28: Este certificado será encontrado em : Assistente de Melhores Práticas :: Configurações serviços Fintech :: Boleto…](https://ajuda.sankhya.com.br/hc/article_attachments/36782435040279)

![Imagem 29: Este certificado será encontrado em : Assistente de Melhores Práticas :: Configurações serviços Fintech :: Boleto…](https://ajuda.sankhya.com.br/hc/article_attachments/36782435041687)

![Imagem 30: Este certificado será encontrado em : Assistente de Melhores Práticas :: Configurações serviços Fintech :: Boleto…](https://ajuda.sankhya.com.br/hc/article_attachments/36782473819287)

![Imagem 31: Este certificado será encontrado em : Assistente de Melhores Práticas :: Configurações serviços Fintech :: Boleto…](https://ajuda.sankhya.com.br/hc/article_attachments/36782435043607)
