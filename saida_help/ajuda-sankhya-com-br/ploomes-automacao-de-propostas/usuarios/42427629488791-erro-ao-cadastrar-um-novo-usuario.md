---
id: "42427629488791"
titulo: "Erro ao cadastrar um novo usuário"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427629488791-Erro-ao-cadastrar-um-novo-usu%C3%A1rio"
trilha: "PLOOMES: Automação de propostas  > Usuários"
atualizado_em: "2026-08-11T16:14:16Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452361", "sync_hash_65be710d72e8"]
---

# Erro ao cadastrar um novo usuário

Ao cadastrar um novo usuário, o formulário pode não salvar por dois motivos principais: um **e-mail já em uso** na base ou um **erro de preenchimento** em algum campo (obrigatório não preenchido, campo chave ou máscara inválida). A mensagem exibida pode variar:

- **"Erro! Tente novamente mais tarde."**
- **"Existem erros no formulário!"**
- **"O e-mail [endereço] já está cadastrado em uma conta Ploomes. Por favor, use um e-mail diferente."**

## E-mail já cadastrado

O motivo mais comum para um erro ao cadastrar um novo usuário é o e-mail informado já estar em uso na base do Ploomes. Quando isso acontece, uma mensagem de erro aparece no canto inferior direito da tela.

![Imagem 1: O motivo mais comum para um erro ao cadastrar um novo usuário é o e-mail informado já estar em uso na base do Ploomes.…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2585408257/664660e1ec42ce13bcd9d4975b7c/image.png?expires=1786536000&signature=8532e5a5f536ba694843ded2d91c553df7b6fa50ab67bf55024ab6d590044fba&req=diUvE81%2BlYNaXvMW3nq%2BgTkkD0hYg8zhhlBa4MRobPaKrO32Jm%2Btk%2F3Icf%2FJ%0AsH0YOSyXXSBTquLV6u2QXc5CpCE%3D%0A)

O endereço de e-mail é um identificador no Ploomes, portanto é um dado único: não pode ser utilizado em mais de um usuário, mesmo em contas diferentes.

## Como verificar

1. Acesse **Administração** > **Tabela de usuários**.
2. Busque pelo e-mail informado, verificando tanto os usuários **ativos** quanto os **inativos**.

![Imagem 2: Busque pelo e-mail informado, verificando tanto os usuários ativos quanto os inativos .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2585409232/ec1ba46d230d9541bc9cb41b5acc/image.png?expires=1786536000&signature=145bc83dc7ec67a9f2824666b8c92aa3fb76ad81b07c2d0900b5695676a3749c&req=diUvE81%2BlINcW%2FMW3nq%2BgSNDxBk1DPTu7GGEMSgbD%2B8iHh7FBZn6NZfQ%2BtRr%0AOGVCy5BEuHLOjUprUznJ1ImpweE%3D%0A)

![Imagem 3: Busque pelo e-mail informado, verificando tanto os usuários ativos quanto os inativos .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2585409690/82bdb113267d41a6c32ec6a74869/image.png?expires=1786536000&signature=403a263a99aa8571d633d72eaa8fecaae68c3eddf1b2b82ebc0f6f186b8a252c&req=diUvE81%2BlIdWWfMW3nq%2BgWBt7Mf0SunDtEygEGOWuZUn0DMv0vbnXtHixq8o%0AOP%2FbTffIVylsNCiBPQB0SIVSUY8%3D%0A)

Se encontrar o e-mail em uso por outro usuário da conta, você pode:

- Reativar o usuário, se ele estiver inativo e você quiser reaproveitar o cadastro. Veja como fazer isso em: [Como reativar um usuário?](https://sankhya.zendesk.com/hc/pt-br/articles/42612917646743)
- Trocar o endereço de e-mail do usuário existente, liberando o endereço desejado para o novo cadastro. Veja como fazer isso em: [Como trocar o e-mail de um usuário](https://sankhya.zendesk.com/hc/pt-br/articles/42427497672599)
- Utilizar outro endereço de e-mail no novo cadastro.

Se **não encontrar** o e-mail em nenhum usuário da sua conta, ele provavelmente está sendo utilizado em outra conta Ploomes. Nesse caso, utilize outro endereço de e-mail para concluir o cadastro.

## Erro de preenchimento

Se as mensagens **"Existem erros no formulário!"** ou "**Erro! Tente novamente mais tarde.**" aparecerem, a causa pode ser:

- Um **campo obrigatório não foi preenchido** (por padrão, na criação de usuário, são obrigatórios **nome**, **e-mail** e **perfil**).

  ![Imagem 4: Um campo obrigatório não foi preenchido (por padrão, na criação de usuário, são obrigatórios nome , e-mail e perfil ).](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2585485547/e73e1080d126ea19fbfc903acf18/image.png?expires=1786536000&signature=ad1156578a8d7d46c5ab159d700401ff857e00131ae0a90c2723ea76b13d87ec&req=diUvE812mIRbXvMW3nq%2BgUo4i8mr59w2ZfWweZWddGxdrl1L2o3DLu4guG7n%0A6amPkbI6Gw4gIjm3A3jLFqDtnoY%3D%0A)
- Um **campo com máscara** (como CPF) foi preenchido de forma incompleta ou incorreta.

  ![Imagem 5: Um campo com máscara (como CPF) foi preenchido de forma incompleta ou incorreta.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2585488603/0fe01ec9124fde346092e20dfd00/image.png?expires=1786536000&signature=5892cf98f5ebf353b9a901a1ea8172ef42d88b7c57abb561e566c663d02857f9&req=diUvE812lYdfWvMW3nq%2BgcbvkxgRqh1TJW%2BP%2Bg0fPzzcbUb0YyMh7%2FkFmACV%0A40XbZ2lhdhr1tJ99vg7fQcY8yck%3D%0A)
- Um **campo-chave em conflito**: além do e-mail (que é sempre único por padrão do sistema), a conta pode ter outros campos configurados como "chave". Essa configuração é para identificação e limitação de duplicidade, definindo que o campo não pode ser preenchido com a mesma informação em cadastros diferentes.

  ![Imagem 6: Um campo-chave em conflito : além do e-mail (que é sempre único por padrão do sistema), a conta pode ter outros campos…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2585495600/c21198a60a158cd82e9480885b7b/image.png?expires=1786536000&signature=1818c580e661b52581d560985679718c04987c0c7ba67d46595e9f0542defea0&req=diUvE813mIdfWfMW3nq%2BgamnlrXYuF4QhHqlYLy13%2Fn0oP%2FyLmG%2B8v92YpI%2F%0AJVuIZq59Mjs9Mn1rkvpbU7VALIw%3D%0A)

Verifique os campos do formulário e corrija o preenchimento de acordo com o ícone que estiver em destaque.

Veja também: [O que significa o erro "Existem erros no formulário!"?](https://sankhya.zendesk.com/hc/pt-br/articles/42427634719255)

---

**Esse artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).
