---
id: "42427284828439"
titulo: "Acesso por Liderança: como funciona essa Hierarquia"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427284828439-Acesso-por-Lideran%C3%A7a-como-funciona-essa-Hierarquia"
trilha: "PONTOTEL: Sistema de marcação de ponto > Administração"
atualizado_em: "2026-08-03T13:29:48Z"
rotulos: ["sync_hc", "pontotel_6a3328e05312f12b37bb0d78", "sync_hash_891f32bf94cf", "pontotel"]
---

# Acesso por Liderança: como funciona essa Hierarquia

A funcionalidade de **Acesso por Liderança** permite que gestores visualizem e gerenciem as informações dos seus liderados diretos e indiretos dentro da plataforma. Com ela, é possível criar hierarquias independentes gerenciadas por diferentes níveis de gestão, sem depender da configuração por locais ou grupos.

Neste artigo, você vai entender como configurar a hierarquia e como ela impacta o acesso às informações do sistema.

---

## Tipos de permissão no sistema

Antes de começar, é importante entender como as permissões funcionam na Pontotel:

- **Funcionário:** acessa somente os próprios dados.
- **Gestor (Gerente, Supervisor):** acessa dados de empregados ou times que estão sob sua responsabilidade.
- **RH:** acessa todos os dados da empresa, sem limitação.

---

## Como configurar o usuário gestor

A configuração da hierarquia é feita em dois momentos: primeiro no cadastro do **usuário gestor** e depois nos **cadastros dos liderados**.
O usuário gestor precisa ter o tipo de acesso definido como **"só liderados"** para que a hierarquia funcione corretamente.

1. No menu de navegação do [site Gestão](https://gestao.pontotel.com.br/), abra o menu **Admin** e selecione a opção **Usuários**.
2. Localize o usuário que será configurado e clique em **editar** (ícone de lápis), ou **crie** um novo usuário.
3. No campo **"Visualizar por"**, selecione a opção **"só liderados"**.
4. Salve as alterações.

![Imagem 1: Salve as alterações.](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1ci0lt8.png)

Com isso, o usuário passa a ter acesso aos dados da sua hierarquia. O próximo passo é configurar quem são os liderados dele.

## Como configurar os liderados

Os liderados são configurados pelo campo **"Líder direto"**, disponível tanto no cadastro de empregados quanto no cadastro de usuários. As duas formas funcionam da mesma maneira: ao editar em um cadastro, a informação é automaticamente replicada no outro.

### Pelo cadastro de empregados:

1. Acesse **Cadastros > Empregados**.
2. Localize o empregado e clique em **Editar**.
3. Clique no campo **"Líder direto desse empregado"** e selecione o gestor responsável.
4. Salve as alterações.

![Imagem 2: Salve as alterações.](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1f22usk.png)

### Pelo cadastro de usuários:

1. Acesse **Admin > Usuários**.
2. Localize o usuário e clique em **Editar**.
3. Clique no campo **"Líder direto desse usuário"** e selecione o gestor responsável.
4. Salve as alterações.

![Imagem 3: Salve as alterações.](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_lm8t97.png)
> Dica: é possível realizar essa configuração em massa utilizando o importador de usuários. Para mais detalhes, consulte o artigo sobre o [Importador de Usuários](https://sankhya.zendesk.com/hc/pt-br/articles/42427253843223).

---

## Liderados diretos e indiretos

A hierarquia pode ter múltiplos níveis. Um gestor pode ter outros gestores abaixo dele, formando uma cadeia de liderança.

Veja o exemplo abaixo: um Diretor gerencia dois Gerentes (liderados diretos). Cada Gerente possui Coordenadores, Supervisores e Empregados abaixo de si (liderados indiretos do Diretor). Nesse cenário:

- O **Diretor** visualiza dados de toda a hierarquia.
- O **Gerente 1** visualiza apenas os dados da sua própria hierarquia.
- O **Gerente 2** visualiza apenas os dados da sua própria hierarquia.

![Imagem 4: O Gerente 2 visualiza apenas os dados da sua própria hierarquia.](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image-6_611noy.png)

---

## Como visualizar e acompanhar a hierarquia

### Relatórios

Após configurar a hierarquia, é possível consultar os vínculos de liderança de duas formas:

- Pela **Planilha de Usuários**, disponível na tela **Admin > Usuários** (botão "Planilha de usuários").

![Imagem 5: Pela Planilha de Usuários , disponível na tela Admin > Usuários (botão "Planilha de usuários").](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_18hm89a.png)

- Pelo **Relatório R13**, acessado em **Gestão > Relatórios e Registros**. Esse relatório traz as informações cadastrais dos empregados, incluindo o líder direto de cada um. Basta filtrar pela coluna de liderança para visualizar toda a hierarquia.

![Imagem 6: Pelo Relatório R13 , acessado em Gestão > Relatórios e Registros . Esse relatório traz as informações cadastrais dos…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_17g842t.png)

### Acompanhamento pelo Aplicativo Gestão

No aplicativo **Pontotel Gestão**, a aba **"Minha Equipe"** exibe um painel com o status da equipe em tempo real: quem está trabalhando, em atraso, ausente ou ainda não iniciou a jornada.
Com a hierarquia configurada, dois novos filtros ficam disponíveis:

- **Liderados por:** filtra os empregados de um usuário líder específico.
- **Hierarquia:** permite escolher entre visualizar somente os **liderados diretos** ou **toda a hierarquia** (incluindo indiretos).

![Imagem 7: Hierarquia: permite escolher entre visualizar somente os liderados diretos ou toda a hierarquia (incluindo indiretos).](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image-7_2gkf3d.png)

---

## Notificações

As notificações de eventos dos empregados também seguem a hierarquia configurada. Ao criar uma regra de notificação, é possível definir se o gestor receberá alertas apenas dos seus **liderados diretos** ou de **toda a hierarquia**, incluindo os indiretos.

Para saber mais sobre como configurar regras de notificação, consulte o artigo sobre [Notificações](https://sankhya.zendesk.com/hc/pt-br/articles/42427275086103).

![Imagem 8: Para saber mais sobre como configurar regras de notificação, consulte o artigo sobre Notificações .](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1gj3bh4.png)

---

Caso ainda tenha dúvidas ou precise de auxílio, entre em contato com o nosso time de Suporte pelo chat integrado ao [site Gestão](https://gestao.pontotel.com.br/#/cognito/login) ou pelo [WhatsApp](https://api.whatsapp.com/send/?phone=551131852700&text&type=phone_number&app_absent=0).
