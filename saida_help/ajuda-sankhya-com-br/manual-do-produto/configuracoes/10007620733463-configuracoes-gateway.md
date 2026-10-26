---
id: "10007620733463"
titulo: "Configurações Gateway"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10007620733463-Configura%C3%A7%C3%B5es-Gateway"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-08-27T15:23:22Z"
rotulos: ["Configuração", "Segurança", "Parceiro", "Integração", "8746", "Configurações Gateway", "Sankhya Om"]
---

# Configurações Gateway

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42310459173015) Módulo: Configurações > Avançado        ![Imagem 2](https://ajuda.sankhya.com.br/hc/article_attachments/42310448636695) Versão disponível: a partir da 4.16
```

A tela Configurações Gateway é utilizada para a geração de Tokens de integração.

Esta permitirá que o cliente tenha autonomia para liberar uma integração em seu EIP. Além disso, também irá possibilitar a revogação de um token quando a integração não for mais necessária, garantindo assim, a segurança de dados.

Lembre-se que, um pré-requisito para utilização dessa tela é possuir a versão **4.16** ou superior do sistema **Sankhya Om**.

![Imagem 3: Lembre-se que, um pré-requisito para utilização dessa tela é possuir a versão 4.16 ou superior do sistema Sankhya Om .](https://ajuda.sankhya.com.br/hc/article_attachments/10169552934039)

---

**Gerência do token no Sankhya Om**

Essa tela é responsável por centralizar todo o cadastro das novas integrações e gerenciamento dos registros já existentes. Dessa forma, informe os dados dos seguintes campos:

O **"Endereço Sankhya"** é um campo que já é preenchido automaticamente como padrão com o endereço origem do **Sankhya Om** que está sendo acessado. Ao salvar o registro, o sistema irá validar se:

- O endereço pode ser acessado externamente;
- É um endereço sintaticamente correto;
- O ambiente está vinculado ao cliente ou se houve algum erro interno de servidor.

Então, caso o EIP esteja em uma rede restrita, é necessário que o endereço do Gateway também esteja liberado no firewall do cliente (IPs: 144.22.228.211 e 144.22.217.141).

**Importante:** após alterar o registro da base de dados na aba **"Registro de Base de Dados"** da tela [Administração do Servidor](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor), ao tentar atualizar o campo Endereço Sankhya no Gateway, o sistema exibirá a mensagem:

**"Identificamos que já existe um ambiente "XYZ" registrado para este mesmo endereço URL Sankhya, mas com informações divergentes no registro de base. Isso pode ocorrer quando o registro da base de dados é atualizado na tela de Administração do Servidor (geralmente devido a uma troca de banco de dados utilizado pela aplicação ou uma alteração na URL JDBC)"**

**(1)** Ao clicar em **"Atualizar"**, o código de identificação da base e/ou o tipo do ambiente serão atualizados. Além disso, a tela será recarregada com os dados do ambiente, URL, nome, e integrações, se existirem.

**(1)** Ao clicar em **"Cancelar"**, a atualização não será realizada e a tela permanecerá sem os dados do ambiente.

O campo **"Nome"** poderá ser preenchido para identificar a base.

O **"Tipo de Ambiente"** é identificado de maneira automática conforme o registro da base que está efetuando a configuração.

Na aba **"Aplicações Vinculadas"** deve ser cadastradas todas as integrações que deseja-se liberar para acessar o ambiente.

![Imagem 4: Na aba "Aplicações Vinculadas" deve ser cadastradas todas as integrações que deseja-se liberar para acessar o ambiente.](https://ajuda.sankhya.com.br/hc/article_attachments/10169547541143)

Dessa forma, têm-se os seguintes campos:

A **"Aplicação"**, onde será possível efetuar a consulta de aplicação de todos os parceiros cadastrados no **Sankhya Om**.

O campo **"Parceiro"** será carregado quando o campo acima for preenchido e não poderá ser alterado.

O **"Status"** indicará se a aplicação está ativa ou não, sendo que, será possível desativá-la se necessário.

Na seção **"Usuário de Integração"**, insira o **"Cód. Usuário"** da integração.

Desse modo, após o preenchimento de todos os campos salve as informações para, em seguida, serem validadas.

O token será gerado vinculado ao ambiente do cliente e o usuário informado no campo Cód. Usuário. Assim, se todas as informações estiverem corretas, o Token será gerado.

![Imagem 5: Caso tenha alguma dúvida técnica referente a essa tela, ou ainda, queira mais informações, confira o artigo API de…](https://ajuda.sankhya.com.br/hc/article_attachments/16116199994263) Caso tenha alguma dúvida técnica referente a essa tela, ou ainda, queira mais informações, confira o artigo [API de Serviços Gateway no Developer Sankhya](https://developer.sankhya.com.br/reference/api-de-integra%C3%A7%C3%B5es-sankhya).

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/10007620733463-Configura%C3%A7%C3%B5es-Gateway#top)
