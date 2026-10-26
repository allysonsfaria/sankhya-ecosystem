---
id: "39012707197719"
titulo: "É obrigatório o preenchimento de um Email no campo Sankhya ID do usuário, mas o campo não está disponível"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39012707197719-%C3%89-obrigat%C3%B3rio-o-preenchimento-de-um-Email-no-campo-Sankhya-ID-do-usu%C3%A1rio-mas-o-campo-n%C3%A3o-est%C3%A1-dispon%C3%ADvel"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-07-22T14:00:37Z"
rotulos: ["Configuração", "Segurança", "Email", "Preferências", "Sankhya ID", "HABILITAACCOUNT", "Cadastro", "Erro", "Habilita Sankhya ID", "Sankhya ID vinculado"]
---

# É obrigatório o preenchimento de um Email no campo Sankhya ID do usuário, mas o campo não está disponível

SITUAÇÃO
Durante o **cadastro ou alteração de usuários no sistema**, pode ocorrer a seguinte mensagem de erro:

> **“É obrigatório o preenchimento de um Email no campo Sankhya ID do usuário.”**

Entretanto, o campo **“Sankhya ID”** não é exibido na tela, impossibilitando o preenchimento da informação exigida pelo sistema. Esse cenário normalmente ocorre quando o ambiente exige a vinculação de **Sankhya ID**, mas o parâmetro responsável por habilitar esse campo ainda não está ativado.

CAUSA

Esse comportamento ocorre em **ambientes SaaS Cloud que utilizam a BIA**, onde é obrigatório que cada usuário possua um **Sankhya ID vinculado**.

O Sankhya ID é utilizado para autenticação e integração com serviços da plataforma Sankhya. Quando o sistema exige esse vínculo, mas o **parâmetro que habilita a funcionalidade não está ativo**, o sistema passa a exigir o preenchimento do campo, porém **o campo não aparece na tela de cadastro de usuários**.

####

#### SOLUÇÃO

Para disponibilizar o campo ''Sankhya ID'' no cadastro de usuários, é necessário habilitar o parâmetro responsável pela funcionalidade.

**(1)** Acesse a tela **''Preferências''** (Configurações » Avançado » Preferências).

**(2)** Busque e pesquise o parâmetro **''HABILITAACCOUNT - Habilita Sankhya ID''**.

**(3)** Habilite o parâmetro.

![Imagem 1: (3) Habilite o parâmetro.](https://ajuda.sankhya.com.br/hc/article_attachments/39024708898967)

**(4)** Após habilitar o parâmetro, realize as seguintes ações:

- Limpe o **cache do navegador**
- Limpe o **cache do servidor**

![Imagem 2: Limpe o cache do servidor](https://ajuda.sankhya.com.br/hc/article_attachments/39012683414679)![Imagem 3: Limpe o cache do servidor](https://ajuda.sankhya.com.br/hc/article_attachments/39024708899735)

**(5)** Realize **novo login no sistema**.

**(6)** Acesse novamente a tela **''Usuários''** (Configurações » Controle de Acesso » Usuários).

**(7)** Clique no **botão da engrenagem (configuração de campos)** e procure pelo campo ''Sankhya ID''

**(8)** Habilite sua exibição.

![Imagem 4: (8) Habilite sua exibição.](https://ajuda.sankhya.com.br/hc/article_attachments/39012960569239)![Imagem 5: (8) Habilite sua exibição.](https://ajuda.sankhya.com.br/hc/article_attachments/39012707192983)![Imagem 6: (8) Habilite sua exibição.](https://ajuda.sankhya.com.br/hc/article_attachments/39012707194135)

**(9)**Após habilitar o parâmetro ''HABILITAACCOUNT'' e atualizar os caches do ambiente:

- O campo ''Sankhya ID'' ficará disponível no cadastro de usuários;
- Será possível informar o **e-mail vinculado ao Sankhya ID**;
- O erro deixará de ocorrer ao salvar ou alterar o usuário.
