---
id: "42427480363927"
titulo: "Quais são os campos obrigatórios para realizar importação em cada entidade?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427480363927-Quais-s%C3%A3o-os-campos-obrigat%C3%B3rios-para-realizar-importa%C3%A7%C3%A3o-em-cada-entidade"
trilha: "PLOOMES: Automação de propostas  > Importações"
atualizado_em: "2026-08-11T16:14:37Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5724761", "sync_hash_ab3a5b792264"]
---

# Quais são os campos obrigatórios para realizar importação em cada entidade?

Antes de mergulharmos nos detalhes dos campos específicos, é fundamental entender a estrutura do Ploomes, composta por módulos e entidades que organizam e categorizam suas informações.

#### Divisão em módulos:

No Ploomes, as funcionalidades são agrupadas em módulos, cada um dedicado a aspectos específicos do seu negócio. Abordaremos quatro módulos principais: **Clientes**, **Negócios**, **Registros de Interação** e **Produtos**.

#### Entidades dentro de cada módulo:

Dentro de cada módulo, ao realizar o mapeamento de importações, você encontrará entidades, categorias específicas de dados. Por exemplo, no módulo de Clientes, as entidades incluem "**Clientes**" e "**Produtos de Cliente**". Já no módulo de Produtos, as entidades variam desde "**Produto**" e "**Grupo de Produto**" até "**Produtox de Client**e" e "**Vínculos**".

Continue a leitura para obter informações detalhadas sobre os campos obrigatórios de cada entidade.

---

## Como iniciar uma importação

Para iniciar uma importação, acesse a entidade desejada (listadas nesse artigo) e clique em **Menu > Importar pelo Excel**.

Exemplo:

![Imagem 1: Exemplo:](https://downloads.intercomcdn.com/i/o/937423608/9efb717acc86f421e91fce2b/image.png?expires=1786536000&signature=f87cab119232501814251e6da4ac149162617f695900892216529f4cd9474e5b&req=fSMgEst9m4FXFb4V1XW4gYyYtuMhijxyrK0wQbWY6VUZGKCoS6AKav86DwgJ%0AAxy9z4g1SPq1CCM8LilStKrUXg%3D%3D%0A)

---

## Importação no módulo de Clientes

### Clientes

Nenhum campo é obrigatório ao importar clientes.

Recomendações:

Mapeie Nome. Se não mapear esse campo, o cliente será criado como "Empresa" ou "Pessoa".

Para saber mais sobre a importação de clientes, [clique aqui.](https://sankhya.zendesk.com/hc/pt-br/articles/42427480771223)

### Produtos de cliente

Ao mapear Produto: Nome (Produto).

Ao mapear Grupo do Produto: Nome (Grupo).

Ao mapear Família do Produto: Nome (Família).

Ao mapear Cliente: nenhum campo é obrigatório.

Ao mapear Produto de cliente: nenhum campo é obrigatório.

## Importação no módulo de Leads

Importante: esse módulo foi inativado e substituído pelo módulo de Negócios.

Para realizar a importação de Leads é recomendado ter em sua planilha a coluna que contém o **Nome do Contato** e/ou o **Nome da Empresa.**

**Atenção**: cuidado com o campo **Empresa** e **Nome da Empresa**. O empresa vincula o Lead a uma Empresa já existente e o Nome da Empresa irá criar o Lead com aquele nome.

## Importação no módulo de Negócios

Nenhum campo é obrigatório ao importar negócios.

Recomendações:

- Mapeie Estágio e Título do negócio.

  - Se não mapear esses campos, o negócio será criado sem título em um funil aleatório;
  - É importante que o estágio seja o único com aquele nome, caso contrário o sistema escolherá o estágio aleatório dentre os com o mesmo nome.
- Mapeie Empresa > Nome para vincular o negócio ao cliente;
- Ao importar "Responsável" pelo negócio, o nome precisa ser EXATAMENTE igual ao que está cadastrado no usuário do Ploomes.

## Importação no módulo de Produtos

Dica: no mapeamento o grupo **não** é Produto > Grupo e **sim**: Grupo do Produto > Nome.

### Produtos

Ao mapear Produto: Nome (Produto) e Nome (Grupo).

Ao mapear Grupo do Produto: Nome (Grupo).

Ao mapear Família do Produto: Nome (Família).

Ao mapear Produto de Cliente: nenhum campo é obrigatório.

Para saber mais sobre a importação de produtos, [clique aqui.](https://sankhya.zendesk.com/hc/pt-br/articles/42427511545367)

### Grupos de produto

Ao mapear Produto: Nome (Produto) e Nome (Grupo).

Ao mapear Grupo do Produto: Nome (Grupo).

Ao mapear Família do Produto: Nome (Família).

Ao mapear Produto de Cliente: nenhum campo é obrigatório.

### Famílias de produto

Ao mapear Produto: Nome (Produto) e Nome (Grupo).

Ao mapear Grupo do Produto: Nome (Grupo).

Ao mapear Família do Produto: Nome (Família).

Ao mapear Produto de Cliente: nenhum campo é obrigatório.

### Produtos de cliente

Ao mapear Produto: Nome (Produto) e Nome (Grupo).

Ao mapear Família do Produto: Nome (Família).

Ao mapear Grupo do Produto: Nome (Grupo).

Ao mapear Produto de Cliente: nenhum campo é obrigatório.

Para saber mais sobre a importação de produto do cliente, [clique aqui.](https://sankhya.zendesk.com/hc/pt-br/articles/42427449343639)

### Vínculos

Ao mapear Produto pai: Nome (Produto)

Ao mapear Grupo do produto pai: Nome (Grupo)

Ao mapear Família do produto pai: Nome (Família).

Ao mapear Produto Filho: Nome (Produto).

Ao mapear Vínculo de Produtos: Categoria.

Ao mapear Produto de Cliente: nenhum campo é obrigatório.

Para saber mais sobre a importação de produtos pai e filho, [clique aqui.](https://sankhya.zendesk.com/hc/pt-br/articles/42427524600855)

## Importação no módulo de Registros de Interação

Nenhum campo é obrigatório ao importar registros de interação.

Recomendações:

- Mapeie Descrição.
- Mapeie um campo de "Cliente" ou "Negócio" para vincular a entidade desejada.

---

## Acesse a Universidade Ploomes para saber mais

A Ploomes disponibiliza uma plataforma de educação digital criada para capacitar seus clientes, oferecendo uma variedade de cursos, shorts, casos de uso e webinars.

Abaixo você confere uma sugestão de conteúdo disponível em nossa plataforma que se relaciona ao tema deste artigo.

[![Imagem 2: Abaixo você confere uma sugestão de conteúdo disponível em nossa plataforma que se relaciona ao tema deste artigo.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2048792473/5d46f57f658a8f3bb2a2f5c22999/Teste+01.png?expires=1786536000&signature=19c67ec2366e166762b798c50985c3878c1ea34ff95e17343f57aade1e8b13c5&req=diAjHs53n4VYWvMW3nq%2BgVrd0AwA4WD7R5XarSkp7JdgPr3zDPbeMNI51yKg%0AynjkO15UziZQkvMeC1mCENJiYzc%3D%0A)](https://universidade.ploomes.com/courses/boas-praticas-para-a-importacao-de-dados)

Dúvidas, comentários ou sugestões? Entre em contato com nosso time de suporte! Nos vemos online.
