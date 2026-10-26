---
id: "360045109533"
titulo: "Configuração p/ leitura de XML no e-mail"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109533-Configura%C3%A7%C3%A3o-p-leitura-de-XML-no-e-mail"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:29:23Z"
rotulos: ["CT-e", "AJUDA DO SKW", "manual", "Configuração", "NF-e", "XML", "Importação", "br.com.sankhya.com.mov.configuracao.email.reciver", "Configuração p/ leitura de XML no e-mail manual", "#comentarioRogerOK", "Configuração de Leitura de XML por E-mail", "Comercial"]
---

# Configuração p/ leitura de XML no e-mail

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312040578071) Módulo: Comercial > Rotinas
```

---

A tela Configuração p/ leitura de XML no e-mail tem a função de proporcionar a leitura dos arquivos XML diretamente da caixa de entrada de um endereço de e-mail específico. Esse processo irá dinamizar consideravelmente a emissão do CT-e pois, ao receber por e-mail o DANFe e o XML das Notas Fiscais transportadas, não será necessário baixar o anexo de seu e-mail e, em seguida, realizar sua importação para emitir o CT-e; como os arquivos serão lidos justamente da caixa de entrada, será necessário apenas bipar a Chave de Acesso do documento, importando assim, seus dados.

Serão processados apenas os e-mails que tiverem anexo, os arquivos XML de NF-e e CT-e; esses arquivos serão salvos na base, de modo que é possível realizar sua importação quando desejado, através da chave do documento.

Essa tela trabalha consultando periodicamente o e-mail nela cadastrado no campo **"Usuário do e-mail"**, de maneira que, ao ser localizado na caixa de entrada um arquivo XML de NF-e e CT-e, terá seu processamento e sua consequente exibição na grade XML baixados. Iremos detalhar sobre essa exibição no decorrer da documentação.

**Observação:** a referida rotina não inclui a importação de Notas Fiscais de emissão própria. Portanto, para serem importados os arquivos referentes a esse tipo de operação, estes deverão ser incluídos manualmente através do [Portal de Importações de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML).

**Importante:** as configurações nessa tela apenas poderão ser alteradas por quem as criou e a exclusão somente poderá ser feita acessando o sistema com o usuário SUP.

![Imagem 2: Importante: as configurações nessa tela apenas poderão ser alteradas por quem as criou e a exclusão somente poderá ser…](https://ajuda.sankhya.com.br/hc/article_attachments/28413243839639)

Os preenchimentos essenciais para o funcionamento dessa rotina, são:

O campo **"Próxima consulta"** é preenchido automaticamente com a Data e Hora de execução da consulta à caixa de entrada do Usuário do e-mail, considerando o intervalo de consultas definido em minutos e inserido no campo seguinte.

Determine no campo **"Intervalo de Consulta em minutos"** a periodicidade em minutos em que a consulta será feita na caixa de entrada informada.

No campo **"Usuário do** **e-mail"**, informe o e-mail que, conforme a rotina de cada empresa, receberá as mensagens contendo os arquivos XML de NF-e ou CT-e. Geralmente, é o e-mail da pessoa responsável pelo processo de Importação de XML's.

No campo **"Senha do e-mail"** tem-se a senha utilizada para acessar o e-mail inserido no campo anterior.

Um **"Servidor de e-mail"** gerencia os e-mails que são enviados e recebidos pelas pessoas que utilizam esse serviço. Cada empresa, para disponibilizar os e-mails a seus colaboradores, possui um servidor de e-mail; esse servidor deve ser informado nesse campo.

Ao realizar a marcação **"Inserir XML no Portal de Importação"**, será feita a consulta dos XML's de NF-e's e/ou CT-e's na caixa de entrada e sua baixa e fará também a inclusão desses documentos no [Portal de importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354).

Através da marcação **"Tipo de Conexão"**, determine o tipo da conexão utilizado na leitura dos XML's no e-mail conforme as seguintes opções:

- Segura com SSL (definição padrão);
- Segura com TLS.

A marcação **"Ignorar validação do certificado no servidor?"** irá definir qual protocolo de segurança será enviado; se estiver selecionada, será enviado imaps; se desmarcada, será enviado imap. Essa marcação ficará habilitada para uso apenas se o Tipo de Conexão estiver definido como Segura com SSL.

Quando a marcação **"Configurar e-mail de leitura por empresa"** for habilitada, permitirá que o sistema busque todas as empresas ativas que contenham as informações de configuração para leitura de XML no e-mail preenchidas na tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), aba [Conf. Leitura XML /E-mail](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abaconf.leituraxmle-mail) e em seguida execute a leitura dos arquivos XML diretamente da caixa de entrada do endereço de e-mail de cada empresa.

Através da marcação **"Apresentar somente xml das NF-e's cadastradas"**, será validado se o XML obtido na caixa de entrada pertence a uma instituição devidamente configurada no [Cadastro de Empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Empresas).

Quando o campo **"Quantidade de dias para considerar e-mails lidos"** for preenchido, fará com que o sistema execute os XMLs dos e-mails lidos da data atual, retornando o número de dias inseridos.

**Nota:** caso o campo não esteja preenchido ou possua valor igual a zero, apenas os e-mails não lidos serão considerados.

Para utilizar o protocolo OAuth, ative a marcação **"Autenticar com OAuth"** e, em seguida, no campo **"Configurações OAuth"**, busque o registro cadastrado na tela [Configurações OAuth](https://ajuda.sankhya.com.br/hc/pt-br/articles/4410197622295). 

Após selecionar a configuração OAuth, efetue a autenticação clicando no botão ![Imagem 3: Após selecionar a configuração OAuth, efetue a autenticação clicando no botão "Autenticação OAuth" .](https://ajuda.sankhya.com.br/hc/article_attachments/27567704348823) **"Autenticação OAuth"**.

**Observação:** com a marcação Autenticar com OAuth ativada, é obrigatório preencher os campos Usuário do e-mail e Intervalo de Consulta em minutos. 

O botão ![Imagem 4: O botão "Salvar" grava o cadastro realizado na tela. Já o botão "Consultar agora" , realiza uma varredura imediata na…](https://ajuda.sankhya.com.br/hc/article_attachments/22212123840791)**"Salvar"** grava o cadastro realizado na tela. Já o botão ![Imagem 5: O botão "Salvar" grava o cadastro realizado na tela. Já o botão "Consultar agora" , realiza uma varredura imediata na…](https://ajuda.sankhya.com.br/hc/article_attachments/22212123853591) **"Consultar agora"**, realiza uma varredura imediata na caixa de entrada correspondente ao e-mail informado, ignorando o tempo de busca inserido no campo Intervalo de Consulta em minutos.

**Observação:** o campo Próxima consulta não será atualizado ao utilizar o botão Consultar agora.

---

**Grade Mensagens Consulta de XML**

Essa grade é alimentada à medida que as consultas são efetuadas na caixa de entrada do Usuário do e-mail. Nela, tem-se a Data da Consulta, a Quantidade de documentos baixados naquela busca e a Mensagem de sucesso ou insucesso no procedimento.

---

**Grade XML baixados**

Essa grade armazena os arquivos XML resultantes de cada busca e que, consequentemente, foram baixados. Pode-se visualizar a Data do Download, o Tipo de arquivo, a Chave do Documento, o XML, o Código Portal de Importação (gerado caso seja solicitado que o XML, seja inserido no Portal de Importação) e o Log de inserção no Portal de Importação (essa coluna apresenta o resultado da tentativa de inclusão do XML no Portal de Importação de XML e, caso necessário, seu conteúdo pode ser copiado para análises posteriores).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109533-Configura%C3%A7%C3%A3o-p-leitura-de-XML-no-e-mail#top)
