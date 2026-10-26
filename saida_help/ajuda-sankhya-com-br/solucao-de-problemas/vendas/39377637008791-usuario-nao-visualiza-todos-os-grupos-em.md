---
id: "39377637008791"
titulo: "Usuário não visualiza todos os grupos em Relação Produto/Parceiro"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39377637008791-Usu%C3%A1rio-n%C3%A3o-visualiza-todos-os-grupos-em-Rela%C3%A7%C3%A3o-Produto-Parceiro"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-10-01T02:44:44Z"
rotulos: ["Produtos", "Configuração", "Segurança", "Parceiro", "TOP", "Artigo criado KCS", "CVE - KCS"]
---

# Usuário não visualiza todos os grupos em Relação Produto/Parceiro

**Situação**

Ao acessar a tela "Relação Produto/Parceiro" (**Comercial > Consulta > Relação Produto/Parceiro**), o usuário **visualiza apenas alguns grupos**, como "Produção", "Requisição" e "Transferência", na listagem de "Grupos". No entanto, o esperado seria visualizar a lista completa de grupos, incluindo "Ajustes", "Bonificação", "Compras", entre outros.

**Solução**

Para resolver este problema, siga os passos abaixo:

**(1)** Acesse a tela "Usuários" (Configurações > Cadastros > Usuários) e localize o usuário que está com o problema de visualização.
**(2)** Clique na aba "Segurança" no cadastro do usuário.
**(3)** Localize as opções **"Inibe acesso às vendas" e "Inibe acesso às compras"** e desmarque **as que estiverem marcadas**:

**"Inibe acesso às vendas"** esconde os grupos das TOPs de Pedido de Venda, Venda e Devolução de Venda;
**"Inibe acesso às compras"** esconde os grupos das TOPs de Pedido de Compra, Compra e Devolução de Compra.

**(4)** Salve as alterações realizadas no cadastro do usuário.
**(5)** Solicite que o usuário faça logout e login novamente no sistema para que as alterações sejam aplicadas.
**(6)** Acesse novamente a tela "Relação Produto/Parceiro" e verifique se todos os grupos estão sendo apresentados corretamente.

**Causa**

A visualização limitada dos grupos ocorre quando a opção "Inibe acesso às vendas" **e/ou "Inibe acesso às compras"** está marcada no cadastro do usuário, na aba "Segurança". **Essas configurações restringem** o acesso a funcionalidades e informações relacionadas a vendas **e a compras**, incluindo a visualização dos grupos de TOP na tela "Relação Produto/Parceiro". **Os grupos das TOPs de Produção, Requisição e Transferência aparecem sempre; os de venda e de compra só aparecem se a opção correspondente estiver desmarcada.**

**Ao incluir um novo usuário, as duas opções já vêm marcadas por padrão.**
