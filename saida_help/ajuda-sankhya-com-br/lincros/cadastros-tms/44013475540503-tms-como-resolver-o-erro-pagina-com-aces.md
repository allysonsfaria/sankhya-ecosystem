---
id: "44013475540503"
titulo: "[TMS] - Como Resolver o Erro \"Página com Acesso Proibido\" no Sistema Lincros devido a Perfil de Usuário"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013475540503--TMS-Como-Resolver-o-Erro-P%C3%A1gina-com-Acesso-Proibido-no-Sistema-Lincros-devido-a-Perfil-de-Usu%C3%A1rio"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T19:58:31Z"
rotulos: ["sync_hc", "lincros", "lincros_13432401", "sync_hash_c75211ad43d7"]
---

# [TMS] - Como Resolver o Erro "Página com Acesso Proibido" no Sistema Lincros devido a Perfil de Usuário

## 1 - Problema Relatado pelo Cliente:

O cliente relatou que não está conseguindo utilizar algumas funcionalidades do sistema Lincros, apresentando o erro "Página com acesso proibido". Ele questionou se houve alguma alteração nas permissões do seu usuário, pois não consegue acessar determinadas páginas ou recursos.

## 2 - Passo a Passo para Resolver o Problema:

1.**Identificação do erro de permissão:**

O erro "Página com acesso proibido" ocorre quando as permissões do usuário são configuradas de forma inadequada.

Foi identificado que o usuário possuía múltiplas permissões, o que estava gerando conflito com o perfil "Administrador".

2.**Verificação de permissões no perfil do usuário:**

Acesse Sistema>Acesso>Usuário>Usuários da empresa

Selecione o usuário no qual esta com essa dificuldade.

3.**Remoção de permissões conflitantes:**

O perfil "Administrador" já garante acesso total ao sistema.

Se houver outras permissões atribuídas além do "Administrador", elas podem entrar em conflito e restringir o acesso, causando o erro.

![Imagem 1: Se houver outras permissões atribuídas além do "Administrador", elas podem entrar em conflito e restringir o acesso,…](https://ajuda.sankhya.com.br/hc/article_attachments/44013438935063)

Remova todas as permissões adicionais, deixando somente a permissão de "Administrador".

4.**Ajuste das permissões:**

Certifique-se de que a única permissão ativa no perfil do usuário seja "Administrador". Isso evita conflitos e garante o acesso correto às funcionalidades do sistema.

![Imagem 2: Certifique-se de que a única permissão ativa no perfil do usuário seja "Administrador". Isso evita conflitos e garante…](https://ajuda.sankhya.com.br/hc/article_attachments/44013469756567)

5.**Salve as alterações e verifique o acesso:**

Após remover as permissões conflitantes, salve as alterações no perfil do usuário.

![Imagem 3: Após remover as permissões conflitantes, salve as alterações no perfil do usuário.](https://ajuda.sankhya.com.br/hc/article_attachments/44013476077975)

Solicite ao cliente que faça o login novamente no sistema para verificar se o erro "Página com acesso proibido" foi resolvido e se o acesso às funcionalidades detalhadas foi restabelecido.
