---
id: "44012164482071"
titulo: "[TMS] - Como Liberar Acesso ao Menu de Planejamento Logístico no Sistema Lincros"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012164482071--TMS-Como-Liberar-Acesso-ao-Menu-de-Planejamento-Log%C3%ADstico-no-Sistema-Lincros"
trilha: "Lincros > TMS > Sistema - TMS"
atualizado_em: "2026-10-05T19:21:49Z"
rotulos: ["sync_hc", "lincros", "lincros_13434253", "sync_hash_ef7306879585"]
---

# [TMS] - Como Liberar Acesso ao Menu de Planejamento Logístico no Sistema Lincros

## 1. Problema Relatado pelo Cliente:

O cliente informou que está com acesso ao sistema Lincros, mas a opção de "Planejamento Logístico", que é necessária para solicitar coleta, não está aparecendo para ele. O problema está relacionado à falta de acesso a um menu específico dentro do sistema.

## 2. Passo a Passo para Resolver o Problema:

Para resolver o problema e garantir que o usuário tenha acesso ao menu de "Planejamento Logístico", siga os seguintes passos:

## 1. Acesse o Sistema Lincros:

- Vá para a tela **Sistema > Acesso > Usuário > Usuários da Empresa.**
- Selecione o "usuário" em questão.
- Na tela de usuário, verifique os Perfis Selecionados para o usuário.

## 2. Verifique as Permissões:

- Acesse **Sistema > Acesso > Permissões.**
- Na coluna "Perfis" informe o perfil ou perfis do usuário.
- Verifique se o perfil do usuário possui acesso ao código do menu relacionado ao Planejamento Logístico. Caso não tenha, siga o próximo passo.

## 3. Ajuste das Permissões de Acesso:

- Para liberar o acesso ao menu, verifique a necessidade de conceder permissões aos processos anteriores, que são ramificados. Por exemplo, se o perfil necessita acessar "Ordem de Coleta", será necessário incluir permissões para os processos anteriores:
- Expedição > Coletas
- Expedição > Coletas > Ordem de Coleta

## 4. Configuração de Permissões:

- Após adicionar as permissões necessárias, ajuste as colunas Inserir, Alterar, Remover e Listar:
- "Inserir": Permite adicionar informações.
- "Alterar": Permite modificar informações.
- "Remover": Permite excluir informações.
- "Listar": Permite visualizar as informações sem realizar alterações.
- Para um acesso completo, as opções "Inserir", "Alterar", "Remover" e "Listar" devem estar habilitadas. Caso o perfil tenha apenas a opção "Listar" habilitada, o usuário terá apenas acesso de visualização.

## Observação: Lembre-se que somente a equipe de suporte pode realizar alterações e inclusões de novas permissões para os menus do sistema.

## Essas orientações são para perfis personalizados, perfis padrão do sistema não devem ser alterados.
