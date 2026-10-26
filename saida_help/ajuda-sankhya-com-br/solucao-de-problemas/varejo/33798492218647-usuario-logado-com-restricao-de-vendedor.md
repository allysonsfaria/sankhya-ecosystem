---
id: "33798492218647"
titulo: "Usuário logado com restrição de vendedor. Verifique na tela de 'Usuários', na aba 'Segurança', no campo 'Ver Pedidos/Notas(WEB)'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33798492218647-Usu%C3%A1rio-logado-com-restri%C3%A7%C3%A3o-de-vendedor-Verifique-na-tela-de-Usu%C3%A1rios-na-aba-Seguran%C3%A7a-no-campo-Ver-Pedidos-Notas-WEB"
trilha: "Solução de Problemas > Varejo"
atualizado_em: "2026-07-22T14:28:20Z"
rotulos: ["Configuração", "Usuários", "Segurança", "Vendedor", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Erro", "Nota/Pedido", "Restrição de vendedor", "PDV Web (Novo Layout)", "Usuário do caixa", "Squad Varejo"]
---

# Usuário logado com restrição de vendedor. Verifique na tela de 'Usuários', na aba 'Segurança', no campo 'Ver Pedidos/Notas(WEB)'

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/33798504573079) **MENSAGEM:**

**"**Usuário logado com restrição de vendedor. Verifique na tela de 'Usuários', na aba 'Segurança', no campo 'Ver Pedidos/Notas(WEB)'"

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/33798504575767)SOLUÇÃO:**

**(1)** Acesse a tela [**''PDV Web (Novo Layout)''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/8046603009047-PDV-Web) (Comercial > Rotinas) e acesse a venda/pedido.

**(2)** Abra o cabeçalho utilizando o botão **''[F2]''**.

**(3)** No pop-up ''**Nota/Pedido''**, verifique o campo **''Vendedor''.**

![Imagem 3: (3) No pop-up '' Nota/Pedido'' , verifique o campo ''Vendedor''.](https://ajuda.sankhya.com.br/hc/article_attachments/33798492204183)

#### Solução 1 (Vendedor informado incorretamente):

Se o processo da empresa **não permitir** que o vendedor seja diferente do vendedor vinculado ao usuário:

- Altere o vendedor no pop-up ''Nota/Pedido'', ajustando-o para o vendedor correto (aquele vinculado ao usuário do caixa).

#### Solução 2 (Quando o usuário do caixa for vendedor):

##### Se o usuário do caixa for um vendedor, mas possui permissão para lançar pedidos/notas para outros vendedores:

**(1)** Acesse a tela [**''Usuários''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios) (Configurações » Controle de Acesso » Usuários).

**(2)** Na aba **''Segurança''** no campo **''Ver Pedidos/Notas (WEB)''** selecione uma opção diferente de **''Desse vendedor''**.

![Imagem 4: (2) Na aba ''Segurança'' no campo ''Ver Pedidos/Notas (WEB)'' selecione uma opção diferente de ''Desse vendedor'' .](https://ajuda.sankhya.com.br/hc/article_attachments/33798504578455)

#### Solução 3 (Quando o usuário do caixa NÃO for vendedor):

##### Se o usuário do caixa não deveria ter vendedor vinculado, porém existe um vendedor cadastrado no usuário:

##### **(1)** Acesse a tela ''Usuários'' (Configurações » Controle de Acesso » Usuários)

##### **(2)** Na aba ''Identificação'' no campo "Vendedor" remova o vendedor vinculado ao usuário, deixando o campo em branco/vazio.

![Imagem 5: (2) Na aba '' Identificação'' no campo "Vendedor" remova o vendedor vinculado ao usuário, deixando o campo em…](https://ajuda.sankhya.com.br/hc/article_attachments/33798504581143)

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/33798492208279)CAUSA:**

A mensagem de erro ocorre quando há uma inconsistência entre as permissões do usuário e o vendedor informado no pedido/nota.

Isso acontece quando:

- O **usuário do caixa possui um vendedor vinculado**,
- A opção **"Ver Pedidos/Notas (WEB)"** está configurada como **"Desse vendedor"**,
- E o pedido/nota está registrado com **um vendedor diferente** daquele vinculado ao usuário.

Desta forma, o sistema bloqueia a visualização ou alteração do documento, exibindo a mensagem de restrição.
