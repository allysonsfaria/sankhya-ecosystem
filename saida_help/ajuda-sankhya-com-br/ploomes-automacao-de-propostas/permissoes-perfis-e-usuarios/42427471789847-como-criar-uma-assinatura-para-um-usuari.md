---
id: "42427471789847"
titulo: "Como criar uma assinatura para um usuário no Ploomes?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427471789847-Como-criar-uma-assinatura-para-um-usu%C3%A1rio-no-Ploomes"
trilha: "PLOOMES: Automação de propostas  > Permissões, perfis e usuários"
atualizado_em: "2026-08-10T18:03:04Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452307", "sync_hash_d90ffdef2a93"]
---

# Como criar uma assinatura para um usuário no Ploomes?

Neste artigo, você verá como adicionar uma assinatura a um usuário, configurar o campo no perfil e utilizar a URL da imagem com uma TAG de HTML para que apareça corretamente nos e-mails enviados pelo Ploomes.

## Como criar uma assinatura

## 1. Adicionar o campo de assinatura no usuário (Administração)

Para que um usuário possa ter assinatura, primeiro é necessário criar o campo no perfil:

1. Vá em: **Administração > Campos e Formulários > Usuários > Adicionar Campo > Criar Campo**
2. Escolha **Tipo:** Imagem
3. Nome do Campo: **Assinatura**
4. Clique em **Salvar**

[GIF animado: Imagem 1: Clique em Salvar](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1565046572/0c9f74a7abfd4e3903022ffec9fb/1.gif?expires=1786536000&signature=909cc48fc665c8de06d0c414a42cb268dd1bfafd8e9d932bae158b4d211ede3d&req=dSUhE8l6m4RYW%2FMW3nq%2BgRkgbbY75mzZ%2F67YRCJRyUWcgdiCVmeXyyihEgTe%0Ah4smaphgYhDBcNt0CEbu%2BdTiZ34%3D%0A)

## 2. Inserir a assinatura do usuário

1. Acesse o menu lateral **Administração** e selecione **Usuários ativos**
2. Clique sobre o usuário desejado para abrir as configurações
3. Expanda **Dados Básicos > Assinatura**
4. Clique em **Adicionar**, selecione a **imagem** e copie a **URL**

   [GIF animado: Imagem 2: Clique em Adicionar , selecione a imagem e copie a URL](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2071847588/fa77fa4b1552215e9a5542793672/2.gif?expires=1786536000&signature=cd767abc317a7397d3d363f158c85947700750fb90e6bf8aea64958bc5a180f0&req=diAgF8F6moRXUfMW3nq%2BgQ0V1%2BGK52rVxpBVUieZfVBi8uDtIbhO4xzTRisC%0ATqWHw%2B19saunuVsxEyVOIL%2FbBOE%3D%0A)
5. Se desejar apenas visual, clique em **Salvar**. Ficará assim:

![Imagem 3: Se desejar apenas visual, clique em Salvar . Ficará assim:](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1565047339/4fda52c980e02033e485b316124e/3.png?expires=1786536000&signature=b04f919b52f099bde0180469b7e60d2fd4ed53c9ce261444461d6e10742a015b&req=dSUhE8l6moJcUPMW3nq%2BgcV9biMT5Lk2lkG9S53WFz%2BO4AnoPLTxcW7lp5vJ%0AUMND9xDGFBiRhIhw0gTmTXbdSEo%3D%0A)

Para utilizar a Assinatura do Usuário (como o responsável por um negócio ou cliente) em um **E-mail**, **copie** somente a **URL** da imagem. Não é necessário salvar a imagem no campo **Assinatura**, pois, caso seja salva, a visualização no E-mail ocorrerá da seguinte forma:

![Imagem 4: Para utilizar a Assinatura do Usuário (como o responsável por um negócio ou cliente) em um E-mail , copie somente a URL…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2152208414/969e79ee956a8becc9c04892b20e/4.png?expires=1786536000&signature=509e99332552884877b7b2ed8ba49ac23bbe6f79da1475bde64f6c61058c990c&req=diEiFMt%2BlYVeXfMW3nq%2Bgam7FZk9dz5hfCSIALrNvyUfvFB4xNC%2BWT5dDOpJ%0ArxQMwlGkHXm7%2FpaTJHpbcMNWnDg%3D%0A)

## Como criar uma TAG de HTML

Para que a imagem da assinatura seja exibida corretamente no e-mail, é necessário adicionar uma tag HTML com a seguinte estrutura:

`<imgsrc="INSIRA A URL DA IMAGEM QUE COPIOU AQUI">`

## Passo a passo:

1. Acesse o menu lateral **Administração** e selecione **Usuários ativos**
2. Clique sobre o usuário desejado para abrir as configurações
3. Vá em **Assinatura**
4. Clique no botão **Editar**
5. Cole o código HTML da imagem conforme a estrutura acima

[GIF animado: Imagem 5: Cole o código HTML da imagem conforme a estrutura acima](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1565047918/31ac63b834177b2d7faced913ef5/5.gif?expires=1786536000&signature=7da22a86fcdbc27ba4d5d03971d87a24c04e22131b616bbb3d1a91edd9ecc905&req=dSUhE8l6moheUfMW3nq%2BgT1zXQ6BvWOP%2FhOhKNVvAzg07JKHbWVjYKXa0SXj%0AT3Eg5azNlvrokfgEkBYHiq7NDB4%3D%0A)

A imagem não permanecerá visível no campo **Assinatura**, mas será exibida corretamente nos e-mails enviados ao utilizar os campos **`Responsavel.Assinatura`** ou **`Usuario.Assinatura`**, conforme o exemplo abaixo:

![Imagem 6: A imagem não permanecerá visível no campo Assinatura , mas será exibida corretamente nos e-mails enviados ao utilizar…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2152187772/f60cf6ae0df51070e9c25f1b04a0/6.png?expires=1786536000&signature=77aaa8dc2deaa62c0beccc9cb5d6132e4e83b71e9f4eaee10d5e4ced25b50bb6&req=diEiFMh2moZYW%2FMW3nq%2BgQcpwRnWHYpWaT4YCb9E%2BZ45Ph0X60DdFq1NHF%2Bo%0ApfLlduFqmdxlFe5IkXbXSLHZZMY%3D%0A)

---

**Esse artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).
