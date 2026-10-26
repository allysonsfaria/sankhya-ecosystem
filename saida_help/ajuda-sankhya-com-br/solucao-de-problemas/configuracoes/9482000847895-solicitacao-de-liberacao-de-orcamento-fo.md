---
id: "9482000847895"
titulo: "Solicitação de liberação de orçamento foi aprovada, registro não pode ser alterado ou excluído. Caso necessário solicite ao liberador a exclusão."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9482000847895-Solicita%C3%A7%C3%A3o-de-libera%C3%A7%C3%A3o-de-or%C3%A7amento-foi-aprovada-registro-n%C3%A3o-pode-ser-alterado-ou-exclu%C3%ADdo-Caso-necess%C3%A1rio-solicite-ao-liberador-a-exclus%C3%A3o"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:07:37Z"
rotulos: ["Configuração", "Segurança", "Financeiro", "Orçamento", "CORE_E00976", "CORE_E02428", "Restrição de Alteração em Orçamentos Aprovados", "Erro"]
---

# Solicitação de liberação de orçamento foi aprovada, registro não pode ser alterado ou excluído. Caso necessário solicite ao liberador a exclusão.

**Mensagem:**

[CORE\_E00976] Solicitação de liberação de orçamento foi aprovada, registro não pode ser alterado ou excluído. Caso necessário solicite ao liberador a exclusão.

**Causa:**

Tentar excluir uma nota/pedido que possua solicitação de liberação de orçamento.

**Solução:**

A opção **"Diversos"** traz como funcionalidade a opção **"Excluir Liberações/Negações Orçamentárias"**; esta opção será habilitada caso o parâmetro **"Pode excluir liberações/negações de orçamento? - EXCLIBORC"** esteja ativado;

![Imagem 1: A opção "Diversos" traz como funcionalidade a opção "Excluir Liberações/Negações Orçamentárias" ; esta opção será…](https://ajuda.sankhya.com.br/hc/article_attachments/14597485714711)

Além disso, para o usuário logado, a marcação **"Pode excluir liberações/negações de orçamento"**, presente na aba Segurança do [Cadastro de Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios) (Configurações » Controle de Acesso » Usuários), deve estar realizada.

![Imagem 2: Além disso, para o usuário logado, a marcação "Pode excluir liberações/negações de orçamento" , presente na aba…](https://ajuda.sankhya.com.br/hc/article_attachments/14597513129751)

Selecionando-se um título, desde que este não esteja baixado e possua liberações/negações orçamentárias, ao acionar esta opção, as liberações e negações orçamentárias serão excluídas.

![Imagem 3: Selecionando-se um título, desde que este não esteja baixado e possua liberações/negações orçamentárias, ao acionar…](https://ajuda.sankhya.com.br/hc/article_attachments/14597526215319)

Algumas condições precisam ser atendidas para que seja feita a exclusão, são elas:

- Se o pedido/nota já foram liberados, mas não estiverem confirmados, será permitida a exclusão da liberação ou negação, porém será solicitada uma nova liberação na tentativa de confirmação do pedido/nota;
- Se o pedido/nota (venda) estiverem confirmados, não será possível realizar a exclusão;
- Se o pedido estiver confirmado, foi faturado, a nota gerada foi confirmada e seu respectivo financeiro pago, não será permitida a exclusão;
- Sendo uma nota de "compra", mesmo que esta se encontre confirmada, e seu financeiro não tenha sido baixado, será permitido realizar a exclusão da liberação ou da negação orçamentária.
