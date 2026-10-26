---
id: "1500012219301"
titulo: "Configurações para envio do Informe de Rendimentos por e-mail MGE Pessoal"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/1500012219301-Configura%C3%A7%C3%B5es-para-envio-do-Informe-de-Rendimentos-por-e-mail-MGE-Pessoal"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:31:20Z"
rotulos: ["Configuração", "Funcionários", "Relatórios Gerenciais", "Financeiro", "E-mail", "#emailThiagoFernandes", "#revisadothiago", "Envio de Informes por E-mail", "Configuração SMTP no MGE", "Utilização do PDFCreator", "MGE Pessoal"]
---

# Configurações para envio do Informe de Rendimentos por e-mail MGE Pessoal

O presente artigo dispõe sobre as configurações para o envio do informe de rendimentos por E-mail MGE pessoal.

**![Imagem 1: Objetivo:](https://ajuda.sankhya.com.br/hc/article_attachments/16336947965719) Objetivo:**

Ao final deste artigo será possível configurar a conta do envio dos informes de rendimento por e-mail aos funcionários no MGE Pessoal.

**![Imagem 2: Caso de Uso:](https://ajuda.sankhya.com.br/hc/article_attachments/16336986189847) Caso de Uso:**

Considere que uma determinada empresa utilize o Gmail como servidor de e-mails e deseja configurar sua conta padrão para o envio dos e-mails de Informe de Rendimentos.

| ✎ **Saiba mais:**  Para que o envio de e-mails através de uma conta do Gmail funcione, é  preciso realizar a configuração de "**Autorização a apps menos seguros**" na seção de segurança das configurações da conta. |
| --- |

![Imagem 3: Como configurar conta SMTP no MGE Pessoal](https://ajuda.sankhya.com.br/hc/article_attachments/16336947981207) **Como configurar conta SMTP no MGE Pessoal**

**3.1 Arquivos --> Funcionários**

**(1)** No cadastro de Funcionários aba **"Endereço"** deverá possuir o E-mail do funcionário.

![Imagem 4: (1) No cadastro de Funcionários aba "Endereço" deverá possuir o E-mail do funcionário.](https://ajuda.sankhya.com.br/hc/article_attachments/15071699747479)

**3.2 Arquivos --> Cadastros --> Empresas (Dados básicos):**

**(1)** No Cadastro da Empresa deverá possuir as configurações necessárias na aba SMTP

![Imagem 5: (1) No Cadastro da Empresa deverá possuir as configurações necessárias na aba SMTP](https://ajuda.sankhya.com.br/hc/article_attachments/1500019306502)

**3.3 Arquivos  --> Controle de acessos --> Usuários:**

**(1)** Na aba **"SMTP"** do Usuário deve estar conforme print:

![Imagem 6: (1) Na aba "SMTP" do Usuário deve estar conforme print:](https://ajuda.sankhya.com.br/hc/article_attachments/1500019554241)

**3.4 Relatórios --> Gerenciais --> Comprovante de rendimentos:**

**(1)** Para envio do Informe de Rendimentos por e-mail primeiramente é necessário realizar o download do programa PDFCreator v3.1.1 ou versões superiores.

| **Link para download:**  <https://sankhyadist.s3-sa-east-1.amazonaws.com/PDFCreator-3_4_1-Setup.zip> |
| --- |

**(1)** Necessário alterar no campo **"Impressora"** da tela de geração de Comprovante de Rendimento para a impressora PDFCreator que está disponível após o download do programa PDFCreator.

![Imagem 7: (1) Necessário alterar no campo "Impressora" da tela de geração de Comprovante de Rendimento para a impressora…](https://ajuda.sankhya.com.br/hc/article_attachments/15071730233751)

**(1)** Ao gerar o relatório pela opção Gerar PDF o sistema irá automaticamente gerar um PDF no diretório de destino com o nome: 'Informe de Rendimento\_CNPJ\_CPF';

**(1)** A opção 'Enviar Email', além de enviar o email para o funcionário irá automaticamente gerar um PDF no direito de destino como o nome: Informe de Rendimento\_CNPJ\_CPF?

![Imagem 8: (1) A opção 'Enviar Email', além de enviar o email para o funcionário irá automaticamente gerar um PDF no direito de…](https://ajuda.sankhya.com.br/hc/article_attachments/1500019307482)

**![Imagem 9: Considerações finais](https://ajuda.sankhya.com.br/hc/article_attachments/16336986209815) Considerações finais**

Foi apresentado neste artigo o modo como efetuar as configurações necessárias para envio do Informe de Rendimentos por e-mail. Esperamos este conteúdo tenha te oferecido o auxílio necessário para a realização desse processo.
