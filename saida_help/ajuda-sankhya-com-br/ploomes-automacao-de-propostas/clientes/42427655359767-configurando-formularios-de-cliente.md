---
id: "42427655359767"
titulo: "Configurando formulários de cliente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427655359767-Configurando-formul%C3%A1rios-de-cliente"
trilha: "PLOOMES: Automação de propostas  > Clientes"
atualizado_em: "2026-08-11T16:14:06Z"
rotulos: ["sync_hc", "ploomes", "ploomes_7897961", "sync_hash_bf7115e0ee3a"]
---

# Configurando formulários de cliente

## Como adicionar e criar campos em clientes?

Podemos seguir 2 caminhos:

1º - Cliente > Menu > Configurar campos de cliente

![Imagem 1: 1º - Cliente > Menu > Configurar campos de cliente](https://downloads.intercomcdn.com/i/o/743263473/8c85b14744f3d6f5beceee2c/2023-05-16+16_24_47-.png?expires=1786536000&signature=bdb3558bd5d15fa29e12e3eea161a7feea8eb2af289fcf687eab7ed614236ec8&req=cyQkFM99mYZcFb4V1XW4gTybvJn7ovaDPNZkNV2WqsGuMl3PuA5%2FBbB0A4ye%0AXEJotg6oIaXJTo%2BxshgpFvy8CA%3D%3D%0A)

2º - Administração > Campos e formulários > Clientes

![Imagem 2: 2º - Administração > Campos e formulários > Clientes](https://downloads.intercomcdn.com/i/o/743250167/59949cb2f5f7324b61f1d28e/2023-05-16+16_05_15-Suporte+Ploomes+-+Artigos+_+Administra%C3%A7%C3%A3o.png?expires=1786536000&signature=e320835abb9afbc60f82d3b57e146097f1799134061a5c3403f2e4b95f0a7350&req=cyQkFMx%2BnIdYFb4V1XW4gfwcdMoCiJ4qOSNmqGgqSDuZRt%2BUGckl8xKIyHqW%0AQCvE9EmOmGVHU9K2WVlCkmpQUA%3D%3D%0A)

![Imagem 3: 2º - Administração > Campos e formulários > Clientes](https://downloads.intercomcdn.com/i/o/743251856/4b537a911abc6d82e62ed3ba/2023-05-16+16_07_45-Suporte+Ploomes+-+Artigos+_+Administra%C3%A7%C3%A3o.png?expires=1786536000&signature=6437ab0ba4a7d3897560bd6312478ecd841464a7a9eb28f45a82df8e0b92b070&req=cyQkFMx%2FlYRZFb4V1XW4gRaO4UY2tB90TspZNFiRnA7Wu2PERTPpYBLntWJC%0A60KK8zSfM%2Bf4YqsrpiP62bQlhA%3D%3D%0A)

Selecione em qual entidade/módulo deseja criar o campo, em seguida utilize a opção de "Adicionar campo" ou "Criar campo" de acordo com sua necessidade.

![Imagem 4: Selecione em qual entidade/módulo deseja criar o campo, em seguida utilize a opção de "Adicionar campo" ou "Criar…](https://downloads.intercomcdn.com/i/o/740805321/b29d705ada730af7f2235b8d/2023-05-12+16_33_28-Suporte+Ploomes+-+Artigos+_+Administra%C3%A7%C3%A3o.png?expires=1786536000&signature=32e9f8233e7d494b6bbed87c8e396525db1fe06d2b79b8bc6dab61d6d83ac185&req=cyQnHsl7noNeFb4V1XW4gTZF6nf9DPLkU5GaAgzK5yGLZR%2BURzw21bVKyhba%0AzxCmUGkgEWaBdLFNjQx%2FheMP9g%3D%3D%0A)

## Tipos de campos

Para criações de campos, podemos escolher qual o "tipo" do campo a ser criado para atingir o resultado desejado. São eles:

- **Texto simples**Texto limitado a 250 caracteres
- **Texto multilinha**
  Texto de caracteres ilimitados
- **Número inteiro**
  Integer
- **Moeda**
  Número limitado a 2 casas decimais
- **Número com casas decimais ilimitadas**
  Float
- **Opções pré-cadastradas**
  Lista de opções cadastráveis
- **Data**
  Campo de preenchimento de data
- **Horário**
  Campo de preenchimento de horário
- **Checkbox**
  Campo de 'sim' ou 'não'
- **CPF**
  Campo com máscara de CPF
- **CNPJ**
  Campo com máscara de CNPJ
- **Porcentagem**
  Campo com indicador de porcentagem (age como casas decimais em fórmula; para usar como porcentagem, é necessário dividi-lo por 100)
- **Endereço**
  Campo integrado ao Google Maps
- **Anexo**
  Campo para subir arquivos, limitado a 20mb
- **Cor**
  Paleta de cores.
- **Usuário**
  Lista de usuários da conta
- **Produto**
  Lista de produtos da conta
- **Cliente**
  Lista de clientes da conta
- **Símbolo de moeda**
  Cria um símbolo de moeda, geralmente utilizado antes de um campo de valor
- **Assinatura**
  Recebe assinaturas pelo APP

É importante que o tipo do campo seja escolhido durante a criação do campo, pois não poderá ser alterado posteriormente.

![Imagem 5: É importante que o tipo do campo seja escolhido durante a criação do campo, pois não poderá ser alterado posteriormente.](https://downloads.intercomcdn.com/i/o/743275302/c15d24edb31505ddfcde5429/2023-05-16+16_44_56-Suporte+Ploomes+-+Artigos+_+Administra%C3%A7%C3%A3o.png?expires=1786536000&signature=ed7ad68ebe236d730582d898294f9a048e41f242077cfd564f032bdfc569aea5&req=cyQkFM57noFdFb4V1XW4gQ9wlBzYTJzpTdAruyHNTO2%2F7v4mfNi6Mf2YFxDe%0AIEKXaEITH%2B2zYnqiX42eYOHqlA%3D%3D%0A)

## Configurações de campo

Dentro das configurações do campo é possível determinar as especificidades do campo

- **Título do campo**
- **Valor padrão** - determina como o campo vem preenchido ao se abrir um formulário. Não tem 'gatilho', portanto só aparece na criação da entidade.
  Pode ser configurado para que puxe valor de outro campo - mas só vai ser puxado um valor caso o mesmo já esteja preenchido no momento da criação.
- **Preenchimento Obrigatório** - Torna o campo obrigatório ao realizar um cadastro;
- **Campo Chave** - impede o usuário de salvar o formulário caso o campo esteja preenchido com um valor já cadastrado no sistema, impedindo duplicidade.
- **Campo de duas Colunas** - Visualmente, ocupará uma linha inteira do formulário.

![Imagem 6: Campo de duas Colunas - Visualmente, ocupará uma linha inteira do formulário.](https://downloads.intercomcdn.com/i/o/743280073/9f01b3dab2fa8e7fa4bfe82b/2023-05-16+16_52_23-Suporte+Ploomes+-+Artigos+_+Administra%C3%A7%C3%A3o.png?expires=1786536000&signature=2b56921b92f0ac15e11bc3b5d0fcffe522e9002c39b308089e46aee3f5e05e90&req=cyQkFMF%2BnYZcFb4V1XW4gYBrzqbLh0ru%2FiGrdcksbPsWx2FtFT99XiqkohD%2B%0A7pWDUS9AhZOdPM%2F9R7sbQHcpng%3D%3D%0A)

## Configurações avançadas

**Fórmulas**

Em "Configurações avançadas", é possível criar uma fórmula para o campo.
As fórmulas rodam apenas no formulário, e seguem a lógica do JavaScript.
É possível criar uma fórmula de JavaScript simples, uma fórmula integrada de JSON, uma fórmula condicional (Condicional simples em JavaScript, mas de preenchimento sem programação), ou uma fórmula Excel.
As fórmulas aceitam campos dinâmicos, clicando em "Campos", e em "Códigos JS" é possível selecionar uma das fórmulas padrão para preenchimento automático.

É possível utilizar várias fórmulas. Sendo:

- **Simples**
- **[Integrada](https://universidade.ploomes.com/courses/cpq-avancado)**
- **[Condicional](https://sankhya.zendesk.com/hc/pt-br/articles/42427667158295)**
- **[Excel](https://sankhya.zendesk.com/hc/pt-br/articles/42427663597207)**

**Dados de pessoa física**

Em "Configurações avançadas", a chave Marcar como dado de pessoa física garante que o campo será completamente apagado de nosso banco de dados caso o cliente seja excluído. Isso garante conformidade da sua empresa com a LGPD.

**Filtro de lista**

Em "Configurações Avançadas" nos campos de Opções pré-cadastradas, Usuário, Produto e Cliente, é possível limitar quais itens aparecem na lista dependendo de uma fórmula criada.

![Imagem 7: Em "Configurações Avançadas" nos campos de Opções pré-cadastradas, Usuário, Produto e Cliente, é possível limitar quais…](https://downloads.intercomcdn.com/i/o/743287711/b2cc28f30a245d1a82e9b350/2023-05-16+17_03_07-Suporte+Ploomes+-+Artigos+_+Administra%C3%A7%C3%A3o.png?expires=1786536000&signature=b7ca22a095905b7b164b0a77f890856632585632df0e028b0c9ec3e526ec0eb7&req=cyQkFMF5moBeFb4V1XW4gav19BCYX2qmIOK7s7VyN%2FbmIf%2FYfI3cYxrZgvQe%0Abnma4c23uGdgEqOybxmTLAJ9Sw%3D%3D%0A)

![Imagem 8: Em "Configurações Avançadas" nos campos de Opções pré-cadastradas, Usuário, Produto e Cliente, é possível limitar quais…](https://downloads.intercomcdn.com/i/o/743287876/a3110e093e4704ec43c2fc62/2023-05-16+17_03_41-Suporte+Ploomes+-+Artigos+_+Administra%C3%A7%C3%A3o.png?expires=1786536000&signature=abc6512e27b5d1b9c5cf8da2210eab45d452f75f16c59ca2e4b83628220bd4be&req=cyQkFMF5lYZZFb4V1XW4geer2oGKzLtSeFmWupXTntAPjc4teBZki2sfixVe%0Afoapedd2RzUYHrr%2Bch8A3auMHQ%3D%3D%0A)

## Configurações de edição e bloqueio do campo

Nesta seção podemos limitar quais usuários editam o campo em "Edição restrita";
Também é possível bloquear a edição por padrão para todos os usuários;
As "Regras de edição" podem liberar ou bloquear a edição dependendo de uma fórmula criada, semelhante ao filtro de lista.

![Imagem 9: Nesta seção podemos limitar quais usuários editam o campo em "Edição restrita"; Também é possível bloquear a edição por…](https://downloads.intercomcdn.com/i/o/743292313/7deb03f1ae35db99c8aa6c35/2023-05-16+17_10_20-Suporte+Ploomes+-+Artigos+_+Administra%C3%A7%C3%A3o.png?expires=1786536000&signature=3208993ff5159f594f5b567b1fc0ea13211dc723f0587adabab1c1e39aa39e1e&req=cyQkFMB8noBcFb4V1XW4gWmYxOq%2F2VQPHZrvdu59P8SCzfI55kaMkwqxWXkp%0ALjnATH5qPrNxug0G7x52XenDYQ%3D%3D%0A)

## Configurações de visualização do campo

As mesmas configurações de edição existem para a visualização do campo, podendo ocultar condicionalmente um campo do formulário.
Administradores podem revelar um campo oculto manualmente apertando "Shift+F"

![Imagem 10: As mesmas configurações de edição existem para a visualização do campo, podendo ocultar condicionalmente um campo do…](https://downloads.intercomcdn.com/i/o/743299768/01810356bcca2e33e16d7521/2023-05-16+17_20_48-Suporte+Ploomes+-+Artigos+_+Administra%C3%A7%C3%A3o.png?expires=1786536000&signature=9662eca2fd5e8906f3c6ca325a69ad89e9a3e406b11630d54756a0520f8f3229&req=cyQkFMB3modXFb4V1XW4gXIMn14LCjX3G9de28LhMMI4nsAYY4e7WxYFmN1w%0AsNI3Umnj%2FBRmiyLENrYiBUh9XA%3D%3D%0A)

## Seções no formulário

Na configuração do formulário, é possível adicionar uma seção em "Nova seção" e remanejar campos ao arrastá-los.
As seções têm sua própria limitação de visualização por usuário.

Um formulário organizado diminui o atrito do usuário no uso do sistema! Garanta que todo campo seja necessário nesse momento, e que a edição e criação seja fácil e fluida.

![Imagem 11: Um formulário organizado diminui o atrito do usuário no uso do sistema! Garanta que todo campo seja necessário nesse…](https://downloads.intercomcdn.com/i/o/744015554/6fbdd1389d51b13a404cbb82/nova+se%C3%A7%C3%A3o.png?expires=1786536000&signature=fef1a5910a7b07a7fcba110afea4b317c981cd45c7dbd48f21760d84c226fd9c&req=cyQjFsh7mIRbFb4V1XW4gbkVjEZIQ7t3SDA6dIqxYqovFLQ1xxoTDe%2FQBixS%0AUw%2FeiCWQT7zy8oc0nKiS6jM1xQ%3D%3D%0A)

![Imagem 12: Um formulário organizado diminui o atrito do usuário no uso do sistema! Garanta que todo campo seja necessário nesse…](https://downloads.intercomcdn.com/i/o/744016755/af809b98c92c45d3f6cc525d/2023-05-17+13_24_15-Suporte+Ploomes+-+Artigos+_+Administra%C3%A7%C3%A3o.png?expires=1786536000&signature=cacdf9e8fdb2328ca96bc04f143b292b49a49a71a8964348fc7d8d4a26b9e656&req=cyQjFsh4moRaFb4V1XW4gcaWKMP028orAhtK%2B83n3w3plTg%2F4q3Sqr7UWO2X%0AgeJwS%2FdBiIvsQYMkmqCht3QV%2Bw%3D%3D%0A)

![Imagem 13: Um formulário organizado diminui o atrito do usuário no uso do sistema! Garanta que todo campo seja necessário nesse…](https://downloads.intercomcdn.com/i/o/744016127/d1b032c5e43b6431f4a5e075/2023-05-17+13_23_52-Suporte+Ploomes+-+Artigos+_+Administra%C3%A7%C3%A3o.png?expires=1786536000&signature=65054da9c868b7760e1ccb9b0d8dd700ad997a8133f453aee9ce4e132c1d1635&req=cyQjFsh4nINYFb4V1XW4gWq0GNeKNAj%2BnJXn2EiqkbiKoiDaRq%2Fg1rEjNrLz%0AGQyC3R0lw9YbkMwNvFR%2BasiXrw%3D%3D%0A)

---

## Acesse a Universidade Ploomes para saber mais

A Ploomes disponibiliza uma plataforma de educação digital criada para capacitar seus clientes, oferecendo uma variedade de cursos, shorts e casos de uso.

Abaixo, você confere sugestões de conteúdos disponíveis em nossa plataforma que se relacionam ao tema deste artigo.

[![Imagem 14: Abaixo, você confere sugestões de conteúdos disponíveis em nossa plataforma que se relacionam ao tema deste artigo.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1385567797/23e51a0ac21c9e4d67a063a4d499/CRM.png?expires=1786536000&signature=99f35cbb5eb522c543d982e3eedafa6cd2f3aea467e3c6ad7887346e6e24c606&req=dSMvE8x4moZWXvMW3nq%2BgYa7k3sR0bCFlI2zAXfPryrLD15BX6czoKV3VbCb%0Aoz2EENyluKPUzCbKqr9NdqcRibk%3D%0A)](https://universidade.ploomes.com/courses/trilha-adm-passo3-crm)

---

Esse artigo te ajudou? Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

Ficou com alguma dúvida? Não hesite em chamar o Suporte pelo chat.
