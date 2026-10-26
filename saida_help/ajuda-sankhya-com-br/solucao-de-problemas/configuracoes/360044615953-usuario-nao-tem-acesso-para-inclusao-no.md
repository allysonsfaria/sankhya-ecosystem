---
id: "360044615953"
titulo: "Usuário não tem acesso para inclusão no Tipo de Movimento 'X'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044615953-Usu%C3%A1rio-n%C3%A3o-tem-acesso-para-inclus%C3%A3o-no-Tipo-de-Movimento-X"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:54:35Z"
rotulos: ["#PUBLIFER", "CORE_E04607", "Configuração", "Movimentação Financeira", "Portal de Vendas", "Portal de Movimentação Interna", "Acessos de Usuário", "Liberações de Inclusão", "Acesso", "Erro"]
---

# Usuário não tem acesso para inclusão no Tipo de Movimento 'X'

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16592849775511) MENSAGEM:**

[CORE\_E04607]:  Usuário não tem acesso para inclusão no Tipo de Movimento 'X'.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16592878817303) SOLUÇÃO:**

Será necessário que o responsável por liberações de acesso na empresa revise os acessos do usuário logado no momento dessa validação, de forma que a opção **"Incluir"** esteja liberada para o tipo de movimentado mencionado.

![Imagem 3: Acesse a tela " Acessos" (Caminho de acesso: Configurações » Controle de Acesso) e de acordo com o Portal e 'Tipo de…](https://ajuda.sankhya.com.br/hc/article_attachments/16592849785751) Acesse a tela "**Acessos"** (Caminho de acesso: Configurações » Controle de Acesso) e de acordo com o Portal e 'Tipo de Movimento' a serem utilizados, verifique as liberações abaixo:

**Portal de Vendas:**

- Comercial » Rotinas » Portal de vendas » Pedidos » **Incluir**
- Comercial » Rotinas » Portal de vendas » Notas » **Incluir**
- Comercial » Rotinas » Portal de vendas » Devolução » **Incluir**

Veja o exemplo abaixo, em que o usuário **Gerente**, ao tentar faturar um pedido para nota de venda, por não ter acesso a opção de Incluir dentro de **"Notas"** obteve a seguinte validação:

![Imagem 4: Veja o exemplo abaixo, em que o usuário Gerente , ao tentar faturar um pedido para nota de venda, por não ter acesso a…](https://ajuda.sankhya.com.br/hc/article_attachments/360060103674)

Conforme .gif abaixo, as liberações foram devidamente realizadas:

[GIF animado: Imagem 5: Conforme .gif abaixo, as liberações foram devidamente realizadas:](https://ajuda.sankhya.com.br/hc/article_attachments/360060103714)

**(1)** Caso a validação ocorra para Compras ou Mov.Interna, seguem as liberações necessárias:

(2)** Portal de Compras:**

- Comercial » Rotinas » Portal de Compras » Pedidos » **Incluir**
- Comercial » Rotinas » Portal de vendas » Notas » **Incluir**
- Comercial » Rotinas » Portal de vendas » Devolução » **Incluir**

(2)** Portal de Mov.Internas:**

- Comercial » Rotinas » Portal de Mov.Internas » Devoluções de Requisição » **Incluir**
- Comercial » Rotinas » Portal de Mov.Internas » Pedidos de Requisição » **Incluir**
- Comercial » Rotinas » Portal de Mov.Internas » Requisições » **Incluir**
- Comercial » Rotinas » Portal de Mov.Internas » Transferências » **Incluir**

![Imagem 6: Realizadas as liberações acima, conforme necessidade do usuário, faça um novo teste.](https://ajuda.sankhya.com.br/hc/article_attachments/16592866851735) Realizadas as liberações acima, conforme necessidade do usuário, faça um novo teste.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16592866855575) CAUSA:**

Mensagem apresentada ao tentar incluir novos documentos referente determinado tipo de movimento, quando o usuário logado não possuir os acessos de inclusão necessários.
