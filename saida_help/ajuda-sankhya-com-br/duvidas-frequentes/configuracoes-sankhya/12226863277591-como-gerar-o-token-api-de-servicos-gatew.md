---
id: "12226863277591"
titulo: "Como gerar o TOKEN - API de Serviços Gateway"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/12226863277591-Como-gerar-o-TOKEN-API-de-Servi%C3%A7os-Gateway"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-09-21T21:39:09Z"
rotulos: ["Configuração", "Segurança", "Parceiro", "Sankhya ID", "API", "Geração do TOKEN para API"]
---

# Como gerar o TOKEN - API de Serviços Gateway

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/24109138546711) SITUAÇÃO:**

Instruções para solicitar as chaves TOKEN e APPKEY, para API de Serviços Gateway

O TOKEN identifica qual integração o parceiro vai acessar e autoriza o acesso aos dados daquela aplicação. Ele está vinculado ao ambiente do cliente e, para cada ambiente (Produção ou Teste), deve ser gerado um TOKEN específico.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/24109138563863) SOLUÇÃO:**

Para gerar o TOKEN, acesse a tela **Configurações Gateway** no Sankhya e siga os passos abaixo:

![Imagem 3: Endereço Sankhya : informe o endereço externo de acesso ao Sankhya OM. Ao salvar o registro, o sistema irá validar se:](https://ajuda.sankhya.com.br/hc/article_attachments/24109138579991) **Endereço Sankhya**: informe o endereço externo de acesso ao Sankhya OM. Ao salvar o registro, o sistema irá validar se:

- O endereço pode ser acessado externamente;
- É um endereço sintaticamente correto;
- O ambiente está vinculado ao cliente ou se houve algum erro interno de servidor.

![Imagem 4: Nome : insira o tipo do ambiente (Produção, Teste, Treinamento).](https://ajuda.sankhya.com.br/hc/article_attachments/24109164186775) **Nome**: insira o tipo do ambiente (Produção, Teste, Treinamento).

**Aplicação**: indique a aplicação que será integrada.

![Imagem 5: Cod. Usuário : insira um usuário vinculado ao Sankhya ID.](https://ajuda.sankhya.com.br/hc/article_attachments/24109138619543) **Cod. Usuário**: insira um usuário vinculado ao Sankhya ID.

![Imagem 6: Cod. Usuário : insira um usuário vinculado ao Sankhya ID.](https://ajuda.sankhya.com.br/hc/article_attachments/29425311384983)

**Importante:**

**(1)**O ambiente Sankhya OM deve estar habilitado para trabalhar com o Sankhya ID, pois o TOKEN depende de um usuário vinculado a ele.

**(1)**Caso o registro da base de dados seja alterado, na aba **"Registro de Base de Dados"** da tela [Administração do Servidor](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor), ao tentar atualizar o campo Endereço Sankhya no Gateway, o sistema exibirá a mensagem:

**"Identificamos que já existe um ambiente "XYZ" registrado para este mesmo endereço URL Sankhya, mas com informações divergentes no registro de base. Isso pode ocorrer quando o registro da base de dados é atualizado na tela de Administração do Servidor (geralmente devido a uma troca de banco de dados utilizado pela aplicação ou uma alteração na URL JDBC)"**

Ao clicar em**"Atualizar"**, o código de identificação da base e/ou o tipo do ambiente serão atualizados. Além disso, a tela será recarregada com os dados do ambiente, URL, nome, e integrações, se existirem.

Ao clicar em**"Cancelar"**, a atualização não será realizada e a tela permanecerá sem os dados do ambiente.
