---
id: "30801000122519"
titulo: "Como obter as credenciais do banco Sicredi"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30801000122519-Como-obter-as-credenciais-do-banco-Sicredi"
trilha: "Manual do Produto > Financeiro e Patrimônio > Sankhya Fintech > Banking"
atualizado_em: "2026-07-29T13:13:25Z"
rotulos: ["Configuração", "Parceiro", "Financeiro", "Boleto Rápido API", "Sicredi"]
---

# Como obter as credenciais do banco Sicredi

Para adquirir as credenciais do Sicredi e ativar a funcionalidade de [Boleto Rápido API](https://ajuda.sankhya.com.br/hc/pt-br/articles/5840766689559-Boleto-R%C3%A1pido-API#BoletoR%C3%A1pidoAPIBancodoBrasil), siga as instruções abaixo.

### Gerar Client ID

![Imagem 1: Acesse o Portal do Desenvolvedor do Sicredi e faça o cadastro e login com os dados de sua conta.](https://ajuda.sankhya.com.br/hc/article_attachments/30801377647127) Acesse o [Portal do Desenvolvedor do Sicredi](https://developer.sicredi.com.br/api-portal/pt-br) e faça o cadastro e login com os dados de sua conta.

![Imagem 2: Após entrar, clique em Criar uma nova aplicação para ser utilizada em produção. No nome da aplicação, use o prefixo API…](https://ajuda.sankhya.com.br/hc/article_attachments/30802130938007) Após entrar, clique em **Criar uma nova aplicação** para ser utilizada em produção. No nome da aplicação, use o prefixo **API Sankhya** + o **seu código de beneficiário** + o final com o nome **Produção** para ficar fácil de identificar.

 Exemplo: **APISankhya123456Produção**

![Imagem 3: Em seguida, selecione as APIs conforme o tipo de boleto que será utilizado:](https://ajuda.sankhya.com.br/hc/article_attachments/30802333192343) Em seguida, selecione as APIs conforme o tipo de boleto que será utilizado:

**Boleto Simples:**

- API de Cobrança (API Boleto 1.0.0);
- API de Autenticação Parceiros.

**Boleto Híbrido (com QR Code):**

- API de Cobrança (API Boleto 1.0.0);
- API de Autenticação Parceiros;
- API Authorization Parceiros 3.0.0.

Após criar a aplicação, você terá acesso ao Client ID, que será usado no próximo passo.

![Imagem 4: Após criar a aplicação, você terá acesso ao Client ID, que será usado no próximo passo.](https://ajuda.sankhya.com.br/hc/article_attachments/40387987093527)

> **Observação:** A ausência da API Authorization Parceiros 3.0.0 no credenciamento do Boleto Híbrido é a principal causa do erro "Erro no acesso à API de boletos do Sicredi (V3)". Caso você esteja migrando do Boleto Simples para o Boleto Híbrido, será necessário gerar novas credenciais habilitando essa API adicional.

---

### Gerar token de acesso e passaword

![Imagem 5: Com a aplicação criada, para gerar o token de acesso no portal do desenvolvedor, vá em Suporte > Abrir chamado :](https://ajuda.sankhya.com.br/hc/article_attachments/30801377647127) Com a aplicação criada, para gerar o token de acesso no portal do desenvolvedor, vá em **Suporte > Abrir chamado**:

- preencha o campo **Client ID ou Nome da App** com o nome da aplicação que você criou;
- após a aprovação, o **Token de Acesso** estará disponível no menu **Minhas Apps**, em **Ver detalhes**.

![Imagem 6: após a aprovação, o Token de Acesso estará disponível no menu Minhas Apps , em Ver detalhes .](https://ajuda.sankhya.com.br/hc/article_attachments/30817637563799)

![Imagem 7: Para gerar a password (código de acesso):](https://ajuda.sankhya.com.br/hc/article_attachments/30802130938007) Para gerar a **password** (código de acesso):

- entre no **Internet Banking** e vá em **Cobrança > Código de Acesso > Gerar**;
- esse menu só aparece para os beneficiários que tem a API de cobrança habilitada no convênio;
- a chave será gerada após registrar um dispositivo de segurança.

![Imagem 8: a chave será gerada após registrar um dispositivo de segurança.](https://ajuda.sankhya.com.br/hc/article_attachments/30817794522007)

Ao finalizar, você terá as duas credenciais necessárias para ativar o serviço no sistema. Certifique-se que as credenciais foram geradas para o ambiente de **Produção**.

![Imagem 9: Com o Token de Acesso e a Password em mãos, copie essas credenciais no cadastro da conta bancária; acesse a tela Contas…](https://ajuda.sankhya.com.br/hc/article_attachments/30802333192343) Com o **Token de Acesso** e a **Password** em mãos, copie essas credenciais no cadastro da conta bancária; acesse a tela [Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113), aba **Boletos/Duplicatas** e clique no botão **Configurar Credenciais** da opção **Boleto Rápido**.

![Imagem 10: Com o Token de Acesso e a Password em mãos, copie essas credenciais no cadastro da conta bancária; acesse a tela Contas…](https://ajuda.sankhya.com.br/hc/article_attachments/30818748097047)
